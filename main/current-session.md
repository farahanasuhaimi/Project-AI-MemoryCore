# Current Session Memory - 2026-04-24
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — rox-bot CAPTCHA auto-solve calibration
**Current Project**: rox-bot — `K:\indie-projects\rox-bot\rox_gardening.py`
**Status**: Auto-solve code enabled ✅ — OCR test pending

## Active Project
- **Name**: rox-bot
- **Started**: 2026-04-23
- **Context**: Python gardening bot for RoX — CAPTCHA auto-solve wired up, needs OCR verification

## Working Memory

### rox-bot — Current State
- All CAPTCHA coordinates calibrated from live 4K screenshot pixel analysis
- `handle_captcha()` fully rewritten — OCR → solve → numpad click → confirm
- Tesseract v5.5.0 installed at `C:\Program Files\Tesseract-OCR\` ✓
- OCR test incomplete — popup wasn't visible when test screenshot was taken

### Calibrated Coordinates (3840×2160)
| Element | Coords |
|---------|--------|
| INPUT_FIELD | (1097, 735) |
| CONFIRM_BUTTON | (1101, 1005) |
| Numpad 1 | (1389, 895) |
| Numpad 2 | (1497, 895) |
| Numpad 3 | (1606, 895) |
| Numpad X (clear) | (1713, 895) |
| Numpad 4 | (1389, 1006) |
| Numpad 5 | (1497, 1006) |
| Numpad 6 | (1606, 1006) |
| Numpad 0 | (1713, 1006) |
| Numpad 7 | (1389, 1117) |
| Numpad 8 | (1497, 1117) |
| Numpad 9 | (1606, 1117) |
| Numpad ✓ | (1713, 1117) |

### Open Issues (rox-bot)
- **OCR test**: Trigger CAPTCHA popup → run OCR → verify it reads the math question
- **Live run**: Let bot trigger CAPTCHA naturally and watch auto-solve execute
- **Maturity timer**: Still disabled — pytesseract import now available, can re-enable anytime
- **Node movement**: Gold label color range not calibrated

### Project Portfolio (as of 2026-04-24)
| Pos | Project | Status |
|-----|---------|--------|
| 1 | drtakaful | Phase 3 next (6 tool/form pages) |
| 2 | rox-bot | Auto-solve wired — OCR test pending |
| 3 | cms-takaful | Built — awaiting deploy |

## Session Recap (For AI Restart)
- **User**: Nufa (Farahana Suhaimi) — Takaful Consultant + Data Engineer, PhD (CNN)
- **Aspiration**: Work from home in Kelantan — Takaful + freelancing
- **AI Companion**: Timothy — installed April 7, 2026
- **rox-bot**: `K:\indie-projects\rox-bot\rox_gardening.py`
  - CAPTCHA auto-solve: enabled, coordinates calibrated for 4K screen
  - Tesseract path: `C:\Program Files\Tesseract-OCR\tesseract.exe`
  - OCR reads from (1097, 735) ±200w ±35h, BINARY_INV, PSM 8
  - Confirm button: (1101, 1005) — blue button in dialog
- **Next session priorities**: OCR test → live run → tune if needed

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See `main/session-format.md` for rebuild structure

---
*Session updated: 2026-04-24 at 18:45*
