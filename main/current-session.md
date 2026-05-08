# Current Session Memory - 2026-05-08
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — Project-B memory refactor + content file saving + RudyG planning
**Last Active Project**: Project-B (`D:\Kerja\Codes\Project-B`)
**Status**: Phase 3b complete. Phase 3c (RudyG/HuggingFace) scoped, not started.

## Last Session Recap

### Project-B — What Was Done (2026-05-08)

1. **Memory architecture refactor** — Rudy now owns all note-saving. Each agent has its own notes file (`{agent}_notes.json`). Rudy emits `SAVE_FINANCE/MARKETING/HR/RUDY_NOTE` tags at routing time; agents read-only.

2. **`rudy_notes.json`** — Standing instructions for Rudy himself (cross-domain preferences, coordination rules). Loaded into routing prompt as "Standing Instructions" every call.

3. **`SAVE_CONTENT_FILE` tag** — Marketing agent now writes full content to `library/content/<filename>.md`. Confirmed working: `content_week1_thread.md` created during testing.

4. **Phase 3b confirmed working** — Notes saving, content files, conversation history all functioning end-to-end.

5. **RudyG plan** — HuggingFace Inference API (OpenAI-compatible), triggered by "RudyG" prefix. Model TBD. Documented as Phase 3c in `project-b.md`.

### Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | win-board | Stable — deployed, Calendar working, onboarding live |
| 2 | Project-B | Phase 3b done — Phase 3c (RudyG/HF) next |
| 3 | drtakaful | FAQPage schema campaign in progress (9/~30 done) |
| 4 | rox-bot | Dynamic CAPTCHA detection done — test_ocr.py run needed |
| 5 | cms-takaful | Built — awaiting deploy |

## Next Session Resume Points
- **Project-B Phase 3c**: Choose HF model → build `config/local_client.py` → detect "RudyG" in `main.py` → wire alternate call path in `router.py`
- **drtakaful**: Resume FAQPage schema from `kenapa-takaful-penting.html`
- **rox-bot**: Run `test_ocr.py`

## Notes
- Project root: `D:\Kerja\Codes\Project-B`
- Project-B entry point: `python -m orchestrator.main`
- HF token needed for RudyG — add to `config/secrets.py` when ready

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See `main/session-format.md` for rebuild structure

---
*Session updated: 2026-05-08 16:00*
