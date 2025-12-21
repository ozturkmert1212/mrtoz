# Active Context

## Current Work Focus
 Selected stack and choices (2025-12-21):
 - Backend: Flask (Python)
 - Model providers: Google Gemini API, Grok (xAI), and OpenAI
 - Supported models: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemma-3-12b`, `grok-3`, `gpt-4o`
 - Database: none for chat logs (logging declined); SQLite unused.
 - Authentication: none (no auth requested)
 - Logging: disabled (no conversation logs stored)

UI/UX (2025-12-21):
- Tailwind-based chat theme; floating desktop model picker bottom-right; modern header/input styling.
- Model picker covers all 5 models: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemma-3-12b`, `grok-3`, `gpt-4o`; selection persists in localStorage and syncs desktop/mobile.
- Images in replies render inline (URLs/data URIs from Grok/Gemini/OpenAI).
- Sidebar rebuilt as Bootstrap offcanvas on mobile and static on desktop; holds conversation list, controls, mobile model picker, and footer links.
- Branding: `mrtoz.ai`; favicon/bot avatar `/static/img/mrtozai.PNG`; bot name blue (light) / yellow (dark); user bubbles forced black text.
- TR/EN toggle with i18n for UI/errors; locale-aware timestamps.
- Mobile UX: hamburger opens offcanvas; mobile model picker moved into sidebar above "made by MRTOZ / Information"; header sticky with proper z-index/background to avoid disappearing when keyboard opens.
- Error handling: quota/rate-limit messages surfaced clearly with body text when available (Gemini, Grok, OpenAI).
- `/information` page bilingual; relative link.

## Recent Changes
- **GPT-4o Integration (2025-12-21)**: Added OpenAI GPT-4o model support with complete API client implementation in `app.py`; added to both desktop and mobile model pickers.
- **Git Security (2025-12-21)**: Created `.gitignore` file, removed `.env` from Git tracking to protect API keys from being pushed to GitHub.
- **README Translation (2025-12-21)**: Translated README.md from Turkish to English with comprehensive documentation including GPT-4o, security notes, and troubleshooting.
- Sidebar refactored to Bootstrap offcanvas (mobile) + static (desktop); hamburger wired via data attributes, custom JS removed.
- Mobile model picker relocated into sidebar above footer links; footer pinned to bottom of offcanvas.
- Mobile header made sticky with z-index/background to prevent disappearance when keyboard opens; spacing tweaked for message area.
- Model list expanded to include GPT-4o alongside existing models (2.5-flash, 2.5-flash-lite, gemma-3-12b, grok-3) without silent fallback.
- TR/EN i18n, quota messaging for Gemini/Grok/OpenAI, and image rendering retained.
- `.gitignore` now protects `.env`, `node_modules/`, `__pycache__/` from Git.
## Next Steps
- Add OpenAI API key to `.env` file and test GPT-4o integration end-to-end.
- Verify all API keys (Gemini, Grok, OpenAI) work correctly; confirm quota parsing matches real responses.
- Commit Git changes with `.gitignore` and push to GitHub (API keys now protected).
- Optional: run `npx update-browserslist-db@latest` to silence the CLI warning.
## Active Decisions & Considerations
- Files are authoritative and must be read at session start.
- Keep entries concise and timestamped when making substantive updates.

## Important Patterns & Preferences
- Prefer short bullets, explicit action items, and references to other files in this folder.

## Learnings & Insights
- Establishing templates reduces cognitive load after resets.