# Progress

## What Works
- Memory Bank folder and core files created with templates.
- Flask + Gemini scaffold created at `ai-chat-site/` (working example).
- Supported models now: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemma-3-12b`, `grok-3`; user-selected model no longer falls back silently.
- Grok (xAI) backend path added; quota/rate-limit responses surfaced to frontend with a clear message.
- Image responses render inline in chat (URL or data URI detection).
- Node/npm initialized; Tailwind v3 build (`npm run build:css`) outputs `static/css/tailwind.css` from `src/input.css`.
- Conversation sidebar (15% on lg+) with localStorage persistence, multi-select deletion, and new conversation creation.
- Branding: `mrtoz.ai` title/bot name; favicon/avatar `static/img/mrtozai.PNG`; dark/light themes with persistence; user bubbles stay black text even in dark mode.
- Language toggle (TR/EN) with i18n map for UI labels, placeholders, and error/quota messages; locale-aware timestamps.
- Sidebar footer holds “made by MRTOZ” link and `Information` link to `/information`.
- `/information` page exists with bilingual notice; link uses relative path for deployment.
- `.gitignore` added to keep `.env`, `node_modules/`, and `__pycache__/` out of repo.
- Mobile UX tweaks: centered/raised model picker on small screens, and inline mobile model picker in header synced with desktop picker; extra padding to avoid overlap with input.
- Model selection now persists in localStorage and is restored on reload (desktop + mobile pickers stay in sync).

## What's Left
- Expand `systemPatterns.md` with actual architecture diagrams and integration notes.
- Decide whether to use SQLite for other purposes; logging remains disabled per user request.
- Verify Gemini access with current models (2.5-flash, 2.5-flash-lite, gemma-3-12b) and adjust if ListModels changes.
- Validate Grok integration end-to-end with a real key; ensure quota detection covers real responses.
- Optional: refresh browserslist DB to silence CLI warning.

## Current Status
- Memory bank initialized and kept current.
- `ai-chat-site/` feature-complete for requested scope: multi-model picker, TR/EN toggle, dark/light theme, localStorage conversations, inline images, quota messaging, and `/information` page. Awaiting real-key validation and deployment.

## Known Issues
- None known; need real API keys to validate quota handling.

## Evolution Notes
- Use this file to track completed milestones and blockers.