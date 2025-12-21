# mrtoz.ai Chat (Flask + Gemini/Grok/GPT-4o)

Multi-model AI chat interface with TR/EN language options and dark/light themes. Conversations are stored only in browser `localStorage`; the server does not keep logs.

## Features
- **Models**: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemma-3-12b`, `grok-3`, `gpt-4o`. When a user selects a model, no fallback occurs; if no model is selected, the system tries in order: flash → flash-lite → gemma.
- **Languages**: TR/EN toggle (UI, placeholders, error/quota messages, and date formats).
- **Themes**: Dark/light mode with user message bubbles always displaying black text.
- **Image Support**: Automatic display of visual responses (URL or data URI images).
- **Local Conversation History**: Sidebar with multi-select deletion and new conversation creation.
- **Quota/Rate-Limit Handling**: Single-sentence warnings for Gemini, Grok, and OpenAI quota/rate-limit situations.
- **Footer**: "made by MRTOZ" and `/information` link (bilingual info page).

## Setup (Python)

### 1. Virtual Environment + Dependencies
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r ai-chat-site\requirements.txt
```

### 2. Environment Variables
Create a `.env` file in the root directory (or use environment variables):
```powershell
# Copy the example file
cp .env.example .env

# Edit .env and add your API keys
GEMINI_API_KEY=your_gemini_key_here
GROK_API_KEY=your_grok_key_here      # optional
OPENAI_API_KEY=your_openai_key_here  # optional
```

> **⚠️ Important**: Never commit the `.env` file to Git. It's already in `.gitignore`.

### 3. Run the Application

**Development Mode (Flask debug server):**
```powershell
python ai-chat-site\app.py
```

**Production Mode (Waitress WSGI server):**
```powershell
python ai-chat-site\run_waitress.py
```

### 4. Access
Open: http://127.0.0.1:5000

## Docker Compose

### 1. Setup Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_key
GROK_API_KEY=your_grok_key
OPENAI_API_KEY=your_openai_key
```

### 2. Build and Run
```powershell
docker compose up --build
```

### 3. Access
Open: http://localhost:5000

## API and Models

### Endpoint
**POST** `/api/chat`

### Request Body
```json
{
  "prompt": "Hello",
  "model": "gemini-2.5-flash"  // optional
}
```

### Supported Models
| Model | Provider | Notes |
|-------|----------|-------|
| `gemini-2.5-flash` | Google Gemini | Primary model |
| `gemini-2.5-flash-lite` | Google Gemini | Fallback #1 |
| `gemma-3-12b` | Google Gemini | Fallback #2 |
| `grok-3` | xAI | Requires `GROK_API_KEY` |
| `gpt-4o` | OpenAI | Requires `OPENAI_API_KEY` |

### Model Selection Behavior
- **With model specified**: Uses only that model, no fallback
- **Without model**: Tries flash → flash-lite → gemma in sequence
- **Grok/GPT-4o**: Requires respective API key

### API Endpoints
- **Google Gemini**: `https://generativelanguage.googleapis.com/v1/models/{model}:generateContent`
- **xAI Grok**: `https://api.x.ai/v1/chat/completions`
- **OpenAI**: `https://api.openai.com/v1/chat/completions`

## Tailwind CSS Build (Optional)

If you need to rebuild the CSS:

```bash
# Install dependencies
npm install

# Build CSS
npm run build:css   # src/input.css -> static/css/tailwind.css
```

## Project Structure

```
mrtoz/
├── ai-chat-site/              # Main application
│   ├── app.py                 # Flask backend
│   ├── run_waitress.py        # Production server
│   ├── requirements.txt       # Python dependencies
│   ├── templates/             # HTML templates
│   ├── static/                # CSS, images
│   └── src/                   # Tailwind source
├── .env                       # API keys (DO NOT COMMIT)
├── .env.example               # Template for .env
├── .gitignore                 # Git ignore rules
├── Dockerfile                 # Container image
├── docker-compose.yml         # Container orchestration
└── README.md                  # This file
```

## Security Notes

- **No Server Logging**: Conversations are stored only in browser `localStorage`
- **API Keys**: Keep your `.env` file secure and never commit it to Git
- **Git Protection**: The `.env` file is already in `.gitignore`
- **Quota/Rate Limits**: The app detects quota/rate-limit errors (402/403/429 status codes or body text containing "quota"/"rate limit"/"billing") and displays user-friendly warnings

## Development Notes

- **No Database**: Chat logs are disabled; SQLite is unused
- **Client-Side Storage**: All conversation history in browser `localStorage`
- **Responsive Design**: Mobile-friendly with Bootstrap offcanvas sidebar
- **Theme Persistence**: User preferences saved across sessions
- **Model Sync**: Desktop and mobile model pickers stay synchronized

## Troubleshooting

### API Key Errors
If you see "API key not set" errors:
1. Verify your `.env` file exists in the root directory
2. Check that API keys are correctly set
3. Restart the application/Docker container

### Model Not Available (404)
If a model returns 404:
1. Verify the model is available in your Google Cloud project
2. Check API key permissions
3. Try a different model from the picker

### Quota Exceeded
If you hit quota limits:
1. Check your API provider's billing/quota settings
2. Wait for quota reset (usually daily)
3. Consider upgrading your API plan

## Contributing

When contributing:
1. Never commit the `.env` file
2. Use `.env.example` as a template
3. Test with all supported models
4. Ensure responsive design works on mobile

## License

This project is for educational and demonstration purposes.

---

**Made by [MRTOZ](https://mrtoz.com)**
