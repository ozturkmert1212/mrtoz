# Tech Context

## Technologies
- Primary languages, frameworks, and runtime should be listed here.
- Python 3.10+ (tested with 3.11)
- Flask (simple HTTP backend)
- `requests` for outbound HTTP to Gemini
- SQLite included as an option, but per current user choice chat logs are disabled (no DB used for logs)

## Development Setup
- Local environment, required tools, and minimal reproducible steps.

Quick start (Windows)

1. Create and activate a virtual environment:
## Technologies
- Python 3.10+ (tested with 3.11)
- Flask (simple HTTP backend)
- `requests` for outbound HTTP to Gemini/Grok
- No DB for chat logs (logging disabled; SQLite unused)


```powershell
pip install -r ai-chat-site\requirements.txt
```

3. Set the Gemini API key as an environment variable (do NOT commit this key):

```powershell
#set for current PowerShell session
$env:GEMINI_API_KEY = "YOUR_KEY_HERE"

#or persistently (new terminal sessions):
setx GEMINI_API_KEY "YOUR_KEY_HERE"
```

4. Run the Flask app (dev):

```powershell
python ai-chat-site\app.py
```

4b. Run with Waitress (Windows-friendly WSGI):

```powershell
python ai-chat-site\run_waitress.py
```

5. Open `http://127.0.0.1:5000` in your browser.

## Technical Constraints
- Platform constraints, supported OS, performance limits, and any legacy compatibility notes.

- This scaffold is minimal and synchronous — suitable for light usage and testing.
- For production scale, use an ASGI server (e.g., Gunicorn + uvicorn) and implement request queuing, retries, and rate limiting.
- Keep network timeouts (e.g., 30s) to prevent hung requests.

- For Windows-based WSGI deployment, `waitress` is a simple, reliable choice (see `ai-chat-site/run_waitress.py`).
- For Unix/Linux, prefer `gunicorn` with `uvicorn` (ASGI) for async and streaming improvements.
- UI styling uses a locally checked-in `static/css/tailwind.css` (CDN removed). If visuals drift, rebuild with Tailwind CLI when Node/npm is available.
- Branding/assets: page title and bot name `mrtoz.ai`; favicon and bot avatar use `static/img/mrtozai.PNG`.
## Dependencies
## Technical Constraints
- Minimal synchronous Flask backend, suitable for light usage/testing.
- For production: prefer ASGI (gunicorn+uvicorn), add retries/rate limiting.
- Windows-friendly WSGI: `waitress` (`run_waitress.py`).
- Tailwind build: `npm run build:css` (v3 CLI; input `src/input.css`, output `static/css/tailwind.css`).
- Branding: title/bot name `mrtoz.ai`; favicon/avatar `static/img/mrtozai.PNG`.
- Client-side only storage: conversations in `localStorage`; server does not log.
- Themes: light/dark toggle with persistence; user bubble text forced black even in dark mode; footer has `made by MRTOZ` and `Information` link.
- Language toggle TR/EN with i18n for labels, placeholders, error/quota messages; timestamps localized.
- Mobile: fixed picker hidden on <768px, inline picker in header; pickers stay in sync; extra bottom padding to avoid overlap with input.
- Model selection persisted in `localStorage` and synchronized between desktop/mobile pickers.
- Testing, linting, CI/CD conventions and commands.
- Development workflow: local virtualenv → set `GEMINI_API_KEY` (and optionally `GROK_API_KEY`) → run `python ai-chat-site\app.py`.
## Dependencies
- Google Gemini (Generative Language API) — models: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemma-3-12b`.
- Grok (xAI) — endpoint `https://api.x.ai/v1/chat/completions`, model `grok-3`.
- `requests` for HTTP calls from backend.

- Primary: `gemini-2.5-flash`
## Tool Usage Patterns
- Dev workflow: local venv → set `GEMINI_API_KEY` (and optional `GROK_API_KEY`) → run `python ai-chat-site\app.py` or `run_waitress.py`.
- Do not commit keys or `.env` files; `.env` is gitignored.

Python (`requests`) example matching `ai-chat-site/app.py` structure:

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
url = 'https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent'
payload = {
    'contents': [{ 'parts': [{'text': 'Hello'}] }],
    'generationConfig': {'temperature': 0.2, 'maxOutputTokens': 256}
}
resp = requests.post(url, params={'key': GEMINI_API_KEY}, json=payload, timeout=30)
resp.raise_for_status()
data = resp.json()
```

Curl example (Windows PowerShell using curl.exe):

```powershell
curl.exe -X POST -H "Content-Type: application/json" ^
  -d "{\"contents\":[{\"parts\":[{\"text\":\"Hello\"}]}],\"generationConfig\":{\"temperature\":0.2,\"maxOutputTokens\":256}}" ^
  "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key=YOUR_KEY"
```

  Grok API notes (xAI)

  - Endpoint: `https://api.x.ai/v1/chat/completions`
  - Model: `grok-3`
  - Auth: `Authorization: Bearer $GROK_API_KEY`
  - Example curl (PowerShell using curl.exe):

  ```powershell
  curl.exe -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $env:GROK_API_KEY" ^
  -d "{\"model\":\"grok-3\",\"messages\":[{\"role\":\"user\",\"content\":\"Hello\"}],\"temperature\":0.2}" ^
    "https://api.x.ai/v1/chat/completions"
  ```

Response handling notes
- `generateContent` typically returns `candidates[0].content.parts[0].text`. Fallback to other fields if needed.
- Check HTTP status; 404 often means model not available to the project. Use ListModels to confirm availability.

Security & operational notes
- Never store API keys in source control. Use environment variables or secret managers.
Response handling notes
- `generateContent` typically returns `candidates[0].content.parts[0].text`. Fallback to other fields if needed.
- Check HTTP status; 404 often means model not available to the project. Use ListModels to confirm availability.
- Quota/rate-limit: backend surfaces `quota_exceeded` flag for 402/403/429 and body-text hints; frontend shows one-line message.
- Add retries/backoff and input validation for production.

Troubleshooting
- If 401/403: verify `GEMINI_API_KEY`, API enabled, billing on, and no restrictive key rules.
- If 404 for a model: run `ListModels` to see allowed models and switch to an available one.
- If requests hang: check network/firewall and adjust timeout.

Next steps for production
- Add rate-limiting and input validation.
- Consider async/streaming responses for long outputs.
- Add monitoring and alerting for API errors and latency.