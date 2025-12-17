# Active Context

## Current Work Focus
Selected stack and choices (2025-12-17):
- Backend: Flask (Python)
- Model provider: Google Gemini API
- Database: SQLite (user initially selected, but logging was later declined — no DB used for logs)
- Authentication: none (no auth requested)
- Logging: disabled (no conversation logs will be stored)
 - Added optional Grok (xAI) integration (`grok-3`) alongside Gemini models.

UI/UX (2025-12-17):
- Applied Tailwind-based chat theme with floating model picker (bottom-right) and modern header/input styling.
 - Model picker now includes `grok-3`.
 - Frontend now renders image outputs (detects image URLs or data URIs from Grok/Gemini replies) directly in chat bubbles.
 - Added left sidebar (≈15% width on lg+) listing conversations stored only in localStorage; supports multi-select checkboxes and deletion, plus “Yeni konuşma” button.
 - Branding updated to `mrtoz.ai`; favicon and bot avatar use `/static/img/mrtozai.PNG`.
 - Dark/light themes with toggle: bot name is blue in light, yellow in dark. Sidebar footer “made by MRTOZ” link lives inside the sidebar and inherits theme colors (blue light / yellow dark) linking to mrtoz.com.

## Recent Changes
Populated `techContext.md` with setup, Gemini generateContent examples, and Waitress run notes.
Scaffolded Flask + Gemini example app in `ai-chat-site/` with model selector (gemini-2.5-flash / gemini-2.5-pro / grok-3).
Applied Tailwind chat theme and floating model picker; Grok support added in backend.
Initialized npm in `ai-chat-site`, pinned Tailwind to v3, added `build:css` script, and rebuilt `static/css/tailwind.css` from `src/input.css`.
Added client-side conversation persistence (localStorage), selectable/deletable sidebar list, and new branding/assets (mrtoz.ai, favicon/avatar from `static/img/mrtozai.PNG`).
Added dark mode overrides, theme persistence, responsive input bar, and themed footer link in sidebar.
## Next Steps
- Verify Gemini access with the currently available models (2.5-flash, 2.5-pro) and adjust if ListModels changes.
- Document architecture/integration notes in `systemPatterns.md`.
- Keep `progress.md` updated as tests run.
 - Validate Grok (grok-3) responses end-to-end with a real key; adjust parsing if response shape changes.
 - Optional: run `npx update-browserslist-db@latest` to silence the CLI warning.

## Active Decisions & Considerations
- Files are authoritative and must be read at session start.
- Keep entries concise and timestamped when making substantive updates.

## Important Patterns & Preferences
- Prefer short bullets, explicit action items, and references to other files in this folder.

## Learnings & Insights
- Establishing templates reduces cognitive load after resets.