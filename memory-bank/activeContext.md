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
- Tailwind-based chat theme; floating desktop model picker bottom-right; modern header/input styling.
- Model picker covers `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemma-3-12b`, `grok-3`; selection persists in localStorage and syncs desktop/mobile.
- Images in replies render inline (URLs/data URIs from Grok/Gemini).
- Sidebar rebuilt as Bootstrap offcanvas on mobile and static on desktop; holds conversation list, controls, mobile model picker, and footer links.
- Branding: `mrtoz.ai`; favicon/bot avatar `/static/img/mrtozai.PNG`; bot name blue (light) / yellow (dark); user bubbles forced black text.
- TR/EN toggle with i18n for UI/errors; locale-aware timestamps.
- Mobile UX: hamburger opens offcanvas; mobile model picker moved into sidebar above “made by MRTOZ / Information”; header sticky with proper z-index/background to avoid disappearing when keyboard opens.
- Error handling: quota/rate-limit messages surfaced clearly with body text when available.
- `/information` page bilingual; relative link.

## Recent Changes
- Sidebar refactored to Bootstrap offcanvas (mobile) + static (desktop); hamburger wired via data attributes, custom JS removed.
- Mobile model picker relocated into sidebar above footer links; footer pinned to bottom of offcanvas.
- Mobile header made sticky with z-index/background to prevent disappearance when keyboard opens; spacing tweaked for message area.
- Model list maintained (2.5-flash, 2.5-flash-lite, gemma-3-12b, grok-3) without silent fallback.
- TR/EN i18n, quota messaging for Gemini/Grok, and image rendering retained.
- `.gitignore` covers `.env`, `node_modules/`, `__pycache__/`.
## Next Steps
- Verify Gemini and Grok keys live; confirm 2.5-flash/flash-lite, gemma-3-12b, grok-3 all respond and quota parsing matches real responses.
- Add note in `systemPatterns.md` about Bootstrap offcanvas integration and mobile header stickiness.
- Optional: run `npx update-browserslist-db@latest` to silence the CLI warning.
## Active Decisions & Considerations
- Files are authoritative and must be read at session start.
- Keep entries concise and timestamped when making substantive updates.

## Important Patterns & Preferences
- Prefer short bullets, explicit action items, and references to other files in this folder.

## Learnings & Insights
- Establishing templates reduces cognitive load after resets.