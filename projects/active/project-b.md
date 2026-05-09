# Project-B — Rudy AI Business Agent System

## Project Info
- **Local path**: `K:\Project-B` (home PC) / `D:\Kerja\Codes\Project-B` (work PC)
- **GitHub**: `https://github.com/farahanasuhaimi/Project-B` (private)
- **Stack**: Python 3.12, DeepSeek API (Anthropic-compatible), JSON file memory
- **Interface**: CLI → Web GUI (Phase 4)
- **Entry point**: `python -m orchestrator.main`

## Current Status
**Phase 4 in progress — Web GUI built (FastAPI + HTML). Ollama models path issue being resolved (OLLAMA_MODELS set to K:\.ollama\models).**
Next: Confirm Ollama sees models after PC restart, then test web UI end-to-end.

## Phase Tracker

| Phase | Scope | Status |
|-------|-------|--------|
| Phase 1 | Planning + agent blueprints | ✅ Done |
| Phase 2 | Core code (config, tools, agents, orchestrator, CLI) | ✅ Done |
| Phase 3a | Product knowledge base (7 products) + brand voice guide | ✅ Done |
| Phase 3b | End-to-end agent testing + memory system | ✅ Done |
| Phase 3c | RudyG — Ollama local model integration (gemma4, swap to qwen3:14b later) | ✅ Done |
| Phase 4 | Web GUI (FastAPI + HTML) | 🔨 In Progress |
| Phase 5 | PaaS blueprint | Planned |

## What's Built

### Core System
- `config/settings.py` + `config/client.py` — DeepSeek API, SSL bypass via httpx
- `config/secrets.py` — API key (gitignored)
- `tools/file_io.py` + `tools/date_utils.py` — shared helpers

### Agents
- `agents/rudy/` — Coordinator + evaluator identity
- `agents/finance/` — Commission tracking, Zakat, Tabung Haji, LHDN
- `agents/marketing/` — Content agent; loads all 7 products + drtakaful voice at runtime
- `agents/hr/` — Follow-ups, onboarding, training

### Orchestrator
- `orchestrator/router.py` — Routes → agent → eval loop (max 3x) → persist → clean
- `orchestrator/evaluator.py` — Confidence scoring 0–100; ≥90 passes, <90 triggers revision
- `orchestrator/main.py` — CLI entry point with conversation history

### Memory System
- `orchestrator/memory/finance_notes.json` — Rudy-extracted notes for Finance agent
- `orchestrator/memory/marketing_notes.json` — Rudy-extracted notes for Marketing agent
- `orchestrator/memory/hr_notes.json` — Rudy-extracted notes for HR agent
- `orchestrator/memory/rudy_notes.json` — Standing instructions for Rudy himself
- Conversation history threaded through session (last 20 messages)
- Rudy owns note-saving — emits `SAVE_FINANCE/MARKETING/HR/RUDY_NOTE` tags at routing time
- Agents read their own notes as preloaded context; they do not write notes

### Library (Knowledge Base)
- `library/products/` — 7 AIA PUBLIC Takaful product summaries
  - alife-legasi-beyond.md, alife-sejuta-makna.md, alife-mediflex-i.md
  - alife-idaman.md, alife-pelindung.md, alife-kritikal-protector.md, alife-kritikal-flex.md
- `library/voice/drtakaful-voice.md` — Brand voice per platform (Threads/Instagram/Facebook)
- `library/content/` — Generated content files saved by marketing agent (SAVE_CONTENT_FILE)

## Business Context
- **Owner**: Nufa (Farahana Suhaimi)
- **Business**: Takaful consulting — Hibah, CI, Medical Card, PA
- **Mission**: Education-first takaful planning for Malaysian families
- **Vision**: Home-based practice in Kelantan, full WFH by 2027
- **2026 Targets**: RM 1,500/month income, 1 team member, Tabung Haji RM 20K by Dec 2026
- **Hajj**: May 2027

## Memory Files (live data)
```
orchestrator/memory/business-context.json  ← mission, vision, KPIs, targets
orchestrator/memory/finance.json           ← transactions (commissions + expenses)
orchestrator/memory/marketing.json         ← content history metadata
orchestrator/memory/hr.json                ← follow-ups, team
orchestrator/memory/finance_notes.json     ← agent-specific notes (Rudy-written)
orchestrator/memory/marketing_notes.json   ← agent-specific notes (Rudy-written)
orchestrator/memory/hr_notes.json          ← agent-specific notes (Rudy-written)
orchestrator/memory/rudy_notes.json        ← Rudy's own standing instructions
```

## Key Technical Decisions
- DeepSeek API via `https://api.deepseek.com/anthropic` — Anthropic SDK, cheaper cost
- `httpx.Client(verify=False)` in `config/client.py` — SSL bypass for corporate network
- File-based JSON memory — no DB at MVP
- Rudy is both coordinator AND evaluator — not a separate QA agent
- Marketing prompt dynamically loads all 7 product files + voice guide at runtime
- SAVE_* tags parsed by router to persist data without agent tool calls
- Rudy owns context extraction — agents receive notes, never write them
- `SAVE_CONTENT_FILE` tag writes full markdown content to `library/content/`

## Phase 3c — RudyG (Ollama local) ✅
- Trigger: prefix message with `RudyG` (handles `RudyG `, `RudyG,`, `RudyG:` etc.)
- Default route is now fully local — all requests go through Ollama, no prefix needed
- Model: `gemma4:latest` → swap to `qwen3:14b` when pulled (change `LOCAL_MODEL` in `config/settings.py`)
- Client: OpenAI SDK in `config/local_client.py`
- Settings: `LOCAL_MODEL`, `LOCAL_BASE_URL` in `config/settings.py`
- No evaluator loop on local path (DeepSeek not available on this machine)
- Project cloned to `K:\Project-B` on home PC

## Phase 4 — Web GUI 🔨
- `web/app.py` — FastAPI app, 4 endpoints: `GET /`, `GET /models`, `POST /chat`, `POST /clear`
- `web/templates/index.html` — Chat UI (Tailwind CDN, dark theme, model dropdown with ⟳ refresh)
- `orchestrator/router.py` — `route_rudyg()` now accepts `model` param — model swappable at runtime
- Model dropdown auto-populates from Ollama (`/api/tags`); ⟳ button refreshes list manually
- History kept server-side (in-memory, single user); Clear button resets both UI and server
- Run: `uvicorn web.app:app --reload --port 8000` from `K:\Project-B`

## Ollama Setup (Home PC)
- Ollama v0.23.2 installed
- Models stored at `K:\.ollama\models\` (non-default path)
- `OLLAMA_MODELS=K:\.ollama\models` set as User env var — requires Ollama restart to take effect
- After restart: `ollama list` should show downloaded models

---
**Last Updated**: 2026-05-09 | **Position**: Active
