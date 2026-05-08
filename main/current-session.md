# Current Session Memory - 2026-05-08
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — Project-B Phase 3c (RudyG local model)
**Last Active Project**: Project-B (`K:\Project-B` on home PC)
**Status**: Phase 3c complete and working.

## Last Session Recap

### Project-B — What Was Done (2026-05-08 evening)

1. **Phase 3c complete** — RudyG local model path built and tested.
   - `config/local_client.py` — OpenAI SDK → Ollama at `localhost:11434/v1`
   - `config/settings.py` — `LOCAL_MODEL = "gemma4:latest"`, `LOCAL_BASE_URL`
   - `orchestrator/router.py` — `route_rudyg()`, `_decide_agent_local()`, `_call_agent_local()`
   - `orchestrator/main.py` — regex detects `RudyG[,\s]` prefix
   - No evaluator loop on local path (DeepSeek not available on this machine)

2. **Project cloned to home PC** — `K:\Project-B` (was `D:\Kerja\Codes\Project-B` on work PC)

3. **Ollama setup** — v0.20.5, `gemma4:latest` (9.6GB). Swap to `qwen3:14b` after pull.

### Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | win-board | Stable — deployed, Calendar working, onboarding live |
| 2 | Project-B | Phase 3c done — Phase 4 (Web GUI) next |
| 3 | drtakaful | FAQPage schema campaign in progress (9/~30 done) |
| 4 | rox-bot | Dynamic CAPTCHA detection done — test_ocr.py run needed |
| 5 | cms-takaful | Built — awaiting deploy |

## Next Session Resume Points
- **Project-B Phase 4**: Web GUI (FastAPI + HTML)
- **Project-B**: Pull `qwen3:14b` via Ollama → change `LOCAL_MODEL` in `config/settings.py`
- **drtakaful**: Resume FAQPage schema from `kenapa-takaful-penting.html`
- **rox-bot**: Run `test_ocr.py`

## Notes
- Home PC project root: `K:\Project-B`
- Project-B entry point: `python -m orchestrator.main`
- RudyG trigger: prefix with `RudyG` (comma/space both work)
- DeepSeek key not on this machine — Rudy path will fail, only RudyG works here

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See `main/session-format.md` for rebuild structure

---
*Session updated: 2026-05-08 22:55*
