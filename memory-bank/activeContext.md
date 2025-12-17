# Active Context

## Current Work Focus
 Selected stack and choices (2025-12-17):
 - Backend: Flask (Python)
 - Model providers: Google Gemini API and Grok (xAI)
 - Supported models: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemma-3-12b`, `grok-3`
 - Database: none for chat logs (logging declined); SQLite unused.
 - Authentication: none (no auth requested)
 - Logging: disabled (no conversation logs stored)

UI/UX (2025-12-17):
- Applied Tailwind-based chat theme with floating model picker (bottom-right) and modern header/input styling.
 - Model picker now includes `grok-3`.
 - Frontend now renders image outputs (detects image URLs or data URIs from Grok/Gemini replies) directly in chat bubbles.
 - Added left sidebar (≈15% width on lg+) listing conversations stored only in localStorage; supports multi-select checkboxes and deletion, plus “Yeni konuşma” button.
 - Branding updated to `mrtoz.ai`; favicon and bot avatar use `/static/img/mrtozai.PNG`.
 - Dark/light themes with toggle: bot name is blue in light, yellow in dark. Sidebar footer “made by MRTOZ” link lives inside the sidebar and inherits theme colors (blue light / yellow dark) linking to mrtoz.com.
 - Model picker includes `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemma-3-12b`, `grok-3`; no silent fallback when user selects a model.
 - Frontend renders image outputs (detects image URLs or data URIs from Grok/Gemini replies) directly in chat bubbles.
 - Left sidebar (≈15% width on lg+) lists conversations from localStorage; supports multi-select deletion and “Yeni konuşma”.
 - Branding: `mrtoz.ai`; favicon/bot avatar `/static/img/mrtozai.PNG`.
 - Dark/light themes with toggle; bot name blue (light) / yellow (dark); user bubble text forced black even in dark mode. Sidebar footer holds “made by MRTOZ” and `Information` link.
 - Language toggle (TR/EN) with i18n for labels/placeholders/errors; locale-based timestamps; model label translated.
 - Mobile UX: header inline model picker for phones, desktop picker hidden on mobile, selectors stay in sync; extra spacing to prevent overlap with input.
 - Error handling: quota/rate-limit responses from Gemini/Grok surface a clear one-line message; errors include body text when available.
 - `/information` page with bilingual notice; link uses `/information` path for deployable hosts.

## Recent Changes
 - Model list updated (2.5-flash, 2.5-flash-lite, gemma-3-12b, grok-3); removed silent fallbacks when a model is explicitly chosen.
 - Added TR/EN language toggle with i18n for UI and error/quota messages; locale-aware timestamps.
 - Added quota detection for Gemini and Grok (429/402/403 and body-text heuristics) with frontend messaging.
 - Ensured user bubble text stays black in dark mode.
 - Added `/information` route/page and sidebar footer link; link is relative for deployment.
 - Added `.gitignore` to exclude `.env`, `node_modules/`, `__pycache__/`.
- Mobile responsive fixes: raised/centered picker on small screens, inline picker beside name on mobile, synced pickers.
## Next Steps
- Verify Gemini access with the currently available models (2.5-flash, 2.5-pro) and adjust if ListModels changes.
 - Verify Gemini access with current models (2.5-flash, 2.5-flash-lite, gemma-3-12b) and adjust if needed.
 - Validate Grok (`grok-3`) end-to-end with real key; confirm quota/error parsing matches production responses.
 - Document architecture/integration notes in `systemPatterns.md`.
 - Optional: run `npx update-browserslist-db@latest` to silence the CLI warning.
## Active Decisions & Considerations
- Files are authoritative and must be read at session start.
- Keep entries concise and timestamped when making substantive updates.

## Important Patterns & Preferences
- Prefer short bullets, explicit action items, and references to other files in this folder.

## Learnings & Insights
- Establishing templates reduces cognitive load after resets.