# Current Session Memory - 2026-04-23
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — rox-bot indie project + project portfolio setup
**Current Project**: rox-bot — Python gardening bot at `K:\indie-projects\rox-bot\`
**Status**: Core bot working ✅ — CAPTCHA auto-solve + maturity timer pending

## Active Project
- **Name**: rox-bot
- **Started**: 2026-04-23
- **Context**: Python gardening bot for RoX — core loop works, manual CAPTCHA pause active

## Working Memory

### rox-bot — Current State
- Template match gardening button → click → 11-click counter → CAPTCHA pause (15s manual)
- Window focus: called once at startup + before each CAPTCHA
- Maturity timer: stubbed out (always returns 0) — OCR logic preserved in comments
- Node movement: skeleton exists (`find_node_positions`, `move_to_next_node`) — never triggers yet

### Open Issues (rox-bot)
- **CAPTCHA auto-solve**: disabled — needs INPUT_FIELD / NUMPAD coordinate calibration
  - Logic in comments inside `handle_captcha()`
  - `INPUT_FIELD = (660, 420)`, `CONFIRM_BUTTON = (733, 572)` — unverified
- **Maturity timer**: needs pytesseract + re re-enabled, threshold tuning
  - Logic in comments inside `check_maturity_timer()`
- **Node movement**: gold label color range (`NODE_COLOR_R/G/B`) not yet calibrated

### Project Portfolio (as of 2026-04-23)
| Pos | Project | Status |
|-----|---------|--------|
| 1 | drtakaful | Phase 3 next (6 tool/form pages) |
| 2 | rox-bot | Core working — calibration pending |
| 3 | cms-takaful | Built — awaiting deploy |

## Session Recap (For AI Restart)
- **User**: Nufa (Farahana Suhaimi) — Takaful Consultant + Data Engineer, PhD (CNN)
- **Aspiration**: Work from home in Kelantan — Takaful + freelancing
- **AI Companion**: Timothy — installed April 7, 2026
- **rox-bot**: `K:\indie-projects\rox-bot\rox_gardening.py` — Python auto-clicker for RoX gardening
  - pytesseract/re removed (commented) — re-enable for OCR features
  - CAPTCHA: 11-click counter, 15s manual pause, auto-solve in comments
  - Game window title: `GAME_WINDOW_TITLE = "RoX"`
- **drtakaful**: Static HTML at `D:\WebDev\Takaful` — Phase 3 retheme next (6 pages)
- **cms-takaful**: Laravel 12 CRM at `list.drtakaful.com` — needs browser test + deploy
- **Next session priorities**: rox-bot calibration OR drtakaful Phase 3

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See `main/session-format.md` for rebuild structure

---
*Session updated: 2026-04-23 at 00:37*
