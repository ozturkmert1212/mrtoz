from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__, template_folder='templates')

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GROK_API_KEY = os.getenv('GROK_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Supported models and default order. Default primary is 2.5-flash with 1.5-pro-latest as final fallback.
SUPPORTED_MODELS = {
    'gemini-2.5-flash': 'https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent',
    'gemini-2.5-flash-lite': 'https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash-lite:generateContent',
    'gemma-3-12b': 'https://generativelanguage.googleapis.com/v1beta/models/gemma-3-12b-it:generateContent',
    'grok-3': 'https://api.x.ai/v1/chat/completions',
    'gpt-4o': 'https://api.openai.com/v1/chat/completions'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    prompt = data.get('prompt', '')
    model = data.get('model')  # optional model selection
    if not prompt:
        return jsonify({'error': 'prompt is required'}), 400
    if not GEMINI_API_KEY:
        return jsonify({'error': 'GEMINI_API_KEY not set in environment'}), 500

    payload = {
        'contents': [
            {
                'parts': [{'text': prompt}]
            }
        ],
        'generationConfig': {
            'temperature': 0.2,
            'maxOutputTokens': 512
        }
    }
    params = {'key': GEMINI_API_KEY}

    # OpenAI GPT-4o path: if model is gpt-4o, route to OpenAI API
    if model and model.startswith('gpt'):
        if not OPENAI_API_KEY:
            return jsonify({'error': 'OPENAI_API_KEY not set in environment'}), 500
        openai_payload = {
            'model': model,
            'messages': [
                {'role': 'user', 'content': prompt}
            ],
            'temperature': 0.2,
            'max_tokens': 512
        }
        try:
            resp = requests.post(
                SUPPORTED_MODELS[model],
                headers={
                    'Authorization': f'Bearer {OPENAI_API_KEY}',
                    'Content-Type': 'application/json'
                },
                json=openai_payload,
                timeout=30
            )
        except Exception as e:
            app.logger.error('OpenAI request error: %s', e)
            return jsonify({'error': str(e)}), 502

        if resp.status_code == 200:
            try:
                j = resp.json()
            except Exception:
                return jsonify({'reply': resp.text})
            text = None
            if isinstance(j, dict) and j.get('choices'):
                msg = j['choices'][0].get('message') or {}
                text = msg.get('content')
            if not text:
                text = str(j)
            return jsonify({'reply': text})

        try:
            body = resp.json()
        except Exception:
            body = resp.text

        def _body_text(val):
            if isinstance(val, dict):
                if 'error' in val:
                    err = val.get('error')
                    if isinstance(err, dict):
                        return str(err.get('message') or err.get('detail') or err)
                    return str(err)
                return str(val)
            return str(val)

        body_text_raw = _body_text(body)
        body_text = body_text_raw.lower()
        quota_hit = resp.status_code in (402, 403, 429) or ('rate limit' in body_text) or ('quota' in body_text) or ('insufficient' in body_text)
        if quota_hit:
            return jsonify({'error': 'OpenAI quota or rate limit exceeded', 'status': resp.status_code, 'body': body, 'quota_exceeded': True}), resp.status_code
        app.logger.error('Upstream OpenAI error %s: %s', resp.status_code, body)
        return jsonify({'error': 'Upstream OpenAI error', 'status': resp.status_code, 'body': body, 'body_text': body_text_raw}), resp.status_code

    # Grok path: if model starts with grok, route to Grok API
    if model and model.startswith('grok'):
        if not GROK_API_KEY:
            return jsonify({'error': 'GROK_API_KEY not set in environment'}), 500
        grok_payload = {
            'model': model,
            'messages': [
                {'role': 'user', 'content': prompt}
            ],
            'temperature': 0.2
        }
        try:
            resp = requests.post(
                SUPPORTED_MODELS[model],
                headers={
                    'Authorization': f'Bearer {GROK_API_KEY}',
                    'Content-Type': 'application/json'
                },
                json=grok_payload,
                timeout=30
            )
        except Exception as e:
            app.logger.error('Grok request error: %s', e)
            return jsonify({'error': str(e)}), 502

        if resp.status_code == 200:
            try:
                j = resp.json()
            except Exception:
                return jsonify({'reply': resp.text})
            text = None
            if isinstance(j, dict) and j.get('choices'):
                msg = j['choices'][0].get('message') or {}
                text = msg.get('content')
            if not text:
                text = str(j)
            return jsonify({'reply': text})

        try:
            body = resp.json()
        except Exception:
            body = resp.text

        def _body_text(val):
            if isinstance(val, dict):
                if 'error' in val:
                    err = val.get('error')
                    if isinstance(err, dict):
                        return str(err.get('message') or err.get('detail') or err)
                    return str(err)
                return str(val)
            return str(val)

        body_text_raw = _body_text(body)
        body_text = body_text_raw.lower()
        quota_hit = resp.status_code in (402, 403, 429) or ('rate limit' in body_text) or ('quota' in body_text) or ('billing' in body_text)
        if quota_hit:
            return jsonify({'error': 'Grok quota or rate limit exceeded', 'status': resp.status_code, 'body': body, 'quota_exceeded': True}), resp.status_code
        app.logger.error('Upstream Grok error %s: %s', resp.status_code, body)
        return jsonify({'error': 'Upstream Grok error', 'status': resp.status_code, 'body': body, 'body_text': body_text_raw}), resp.status_code

    # Select endpoints: when a model is chosen, do not fallback to others to avoid surprise switching
    if model:
        if model not in SUPPORTED_MODELS or model.startswith('grok'):
            return jsonify({'error': 'unsupported model', 'allowed': [m for m in SUPPORTED_MODELS.keys()]}), 400
        endpoints = [SUPPORTED_MODELS[model]]
    else:
        endpoints = [
            SUPPORTED_MODELS['gemini-2.5-flash'],
            SUPPORTED_MODELS['gemini-2.5-flash-lite'],
            SUPPORTED_MODELS['gemma-3-12b']
        ]

    last_resp = None
    for url in endpoints:
        try:
            resp = requests.post(url, params=params, json=payload, timeout=30)
        except Exception as e:
            # network / DNS / timeout errors
            last_resp = None
            app.logger.warning('Request error to %s: %s', url, e)
            continue

        if resp.status_code == 200:
            try:
                j = resp.json()
            except Exception:
                return jsonify({'reply': resp.text})

            text = None
            if isinstance(j, dict) and j.get('candidates'):
                cand = j['candidates'][0]
                content = cand.get('content') or {}
                parts = content.get('parts') or []
                if parts and isinstance(parts[0], dict):
                    text = parts[0].get('text')
            if not text and isinstance(j, dict):
                text = j.get('output') or j.get('response')
            if not text:
                text = str(j)
            return jsonify({'reply': text})

        last_resp = resp

    if last_resp is not None:
        body = None
        try:
            body = last_resp.json()
        except Exception:
            body = last_resp.text

        def _body_text(val):
            if isinstance(val, dict):
                if 'error' in val:
                    err = val.get('error')
                    if isinstance(err, dict):
                        return str(err.get('message') or err.get('detail') or err)
                    return str(err)
                return str(val)
            return str(val)

        body_text = _body_text(body).lower()
        quota_hit = last_resp.status_code in (402, 403, 429) or ('rate limit' in body_text) or ('quota' in body_text) or ('billing' in body_text)
        if quota_hit:
            return jsonify({
                'error': 'Gemini quota or rate limit exceeded',
                'status': last_resp.status_code,
                'body': body,
                'quota_exceeded': True
            }), last_resp.status_code
        app.logger.error('Upstream Gemini error %s: %s', last_resp.status_code, body)
        return jsonify({'error': 'Upstream Gemini error', 'status': last_resp.status_code, 'body': body}), last_resp.status_code

    return jsonify({'error': 'Could not contact Gemini endpoints'}), 502

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
