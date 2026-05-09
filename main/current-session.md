# Current Session Memory - 2026-05-09
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — Project-B Phase 5 (Dashboard + Coordinator)
**Last Active Project**: Project-B (`K:\Project-B` on home PC)
**Status**: Phase 5c complete. Dashboard live with coordinator voice. Claude light-mode theme applied.

## Last Session Recap

### Project-B — What Was Done (2026-05-09 afternoon)

1. **Ollama fixed** — gemma4:latest confirmed working at ~98 tok/s on RTX 5080. `OLLAMA_KEEP_ALIVE=30m` set as User env var.

2. **Bug fix** — `router.py` `_decide_agent_local` empty-string crash fixed.

3. **Phase 5 — Dashboard (5a, 5b, 5c complete)**

   **New files:**
   - `orchestrator/dashboard.py` — `generate_dashboard()` → `{focus, urgent, pulse}` via native Ollama API
   - `orchestrator/action_handler.py` — `process_action()` → parse + save + coordinator voice
   - `web/templates/dashboard.html` — full dashboard UI (replaces chat)

   **Modified:**
   - `web/app.py` — added `/dashboard`, `/action` endpoints

   **Key architecture:**
   - Native Ollama API (`POST /api/generate` with `format:"json"`) — OpenAI-compat drops content on structured prompts
   - gemma4 wraps JSON under `"fields"` key — flattened in parser
   - 8 action types: commission, expense, extra_income, content_create, content_posted, followup, setup, query
   - Coordinator voice: Rudy speaks first (1-3 sentences), `✓ Saved · summary` is quiet footer
   - Commission math always recomputed from rate (never trusts LLM math)
   - Commission rates stored in `finance_notes.json` as `{topic:"commission_rate", product:"...", rate:0.30}`

   **UI:**
   - Claude light mode: `#f5f4ef` bg, white cards, Claude orange `#d97757` accent
   - Focus Today / Urgent / Business Pulse / Action Panel / Cards feed
   - Pulse bar: red (< 40%) → orange (< 80%) → bright orange (≥ 80%)

### Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | Project-B | Phase 5c done — dashboard live |
| 2 | win-board | Stable — deployed |
| 3 | drtakaful | FAQPage schema in progress |
| 4 | rox-bot | test_ocr.py needed |
| 5 | cms-takaful | Built — awaiting deploy |

## Next Session Resume Points
- **Run**: `cd K:\Project-B && uvicorn web.app:app --reload --port 8000`
- **Test live**: close a policy, ask financial health, make content, record expense
- **Onboard Rudy**: type "A-Life Idaman commission is 30%" etc. to seed finance_notes
- **Phase 5d** (next): onboarding nudge if no finance_notes set
- **drtakaful**: Resume FAQPage schema from `kenapa-takaful-penting.html`
- **rox-bot**: Run `test_ocr.py`
- **Deferred**: markdown/Excel export feature

## Notes
- Run: `cd K:\Project-B && uvicorn web.app:app --reload --port 8000`
- Old chat UI still at `/chat-ui`
- Native Ollama API: `POST http://localhost:11434/api/generate` with `format:"json"`
- `OLLAMA_KEEP_ALIVE=30m` active — gemma4 stays 30 min idle

---
*Session updated: 2026-05-09 13:29*
