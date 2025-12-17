# Progress

## What Works
- Memory Bank folder and core files created with templates.
- Flask + Gemini scaffold created at `ai-chat-site/` (basic working example).
- Chat UI themed with Tailwind; model picker switches between gemini-2.5-flash and gemini-2.5-pro.
- Grok (xAI) backend path added; model picker includes `grok-3`.
- Image responses from models now render inline in chat (URL or data URI detection).
- Node/npm initialized; Tailwind pinned to v3 with `build:css` script and `static/css/tailwind.css` rebuilt from `src/input.css`.
- Conversation sidebar added (15% on lg+), storing chats in localStorage; supports multi-select checkboxes, deletion, and creating new chats.
- Branding updated to `mrtoz.ai`; favicon and bot avatar use `static/img/mrtozai.PNG`.
- Dark/light themes with toggle; bot name blue in light / yellow in dark; sidebar footer “made by MRTOZ” link (mrtoz.com) themed blue/yellow; input bar made more responsive.

## What's Left
- Expand `systemPatterns.md` with actual architecture diagrams and integration notes.
- Decide whether to use SQLite for other purposes; logging is disabled per user request.
- Continue verifying Gemini access with allowed models (2.5-flash, 2.5-pro) and adjust if ListModels changes.
- Validate Grok integration end-to-end with a real key and adjust parsing if needed.
 - Optional: refresh browserslist DB to silence CLI warning.

## Current Status
- Initial memory bank created. Ready for content population.
- `ai-chat-site/` scaffold added. Tailwind build now uses npm script; conversation persistence/selection live in UI. Next: test Gemini integration locally and update `techContext.md` if behavior changes.

## Known Issues
- None at creation time.

## Evolution Notes
- Use this file to track completed milestones and blockers.