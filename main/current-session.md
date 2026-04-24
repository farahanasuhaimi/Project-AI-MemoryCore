# Current Session Memory - 2026-04-25
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — rox-bot OCR debugging (continued)
**Current Project**: rox-bot — `K:\indie-projects\rox-bot\rox_gardening.py`
**Status**: 3 bugs fixed — final test pending

## Active Project
- **Name**: rox-bot
- **Started**: 2026-04-23
- **Context**: Python gardening bot for RoX — CAPTCHA auto-solve pipeline iteratively debugged

## Working Memory

### rox-bot — Current State
- `ocr_expression()` pipeline: projection-based island detection → valley split → digit OCR
- All 3 known bugs fixed this session (see below)
- **NOT YET TESTED** with final fix applied — user left before running the last test

### Bug Fixes Applied This Session (2026-04-25)
| Bug | Fix |
|-----|-----|
| Dead space picked as operator | Find largest contiguous island first; valley threshold computed from island mean only |
| "+" creates two sub-valleys; first one picked, splitting mid-operator | `merge_gap=30` merges nearby valleys into one operator region |
| "1" trailing space (37px) merged into operator with merge_gap=40 | Reduced to merge_gap=30 (< 37px, so trailing space stays separate) |
| `bitwise_not` flipping threshold output — Tesseract got white-on-black | Removed NOT; `THRESH_BINARY(225)` already gives black char on white bg |

### Key Code State
- `EXPR_REGION = (910, 960, 1120, 1310)` — y1,y2,x1,x2 (confirmed correct from images)
- `EXPR_SCALE = 5` — 5x INTER_CUBIC upscale
- `merge_gap = 30` in `_split_expression()`
- `_ocr_digit_gray()` — uses `THRESH_BINARY(225)` directly (no NOT), tries PSM 10, 8, 13
- `test_ocr.py` — diagnostic script, synced to use `bot._split_expression()` directly

### Calibrated Coordinates (3840×2160)
| Element | Coords |
|---------|--------|
| INPUT_FIELD | (1097, 735) |
| CONFIRM_BUTTON | (1101, 1005) |
| Numpad 1 | (1389, 895) |
| Numpad 2 | (1497, 895) |
| Numpad 3 | (1606, 895) |
| Numpad 4 | (1389, 1006) |
| Numpad 5 | (1497, 1006) |
| Numpad 6 | (1606, 1006) |
| Numpad 0 | (1713, 1006) |
| Numpad 7 | (1389, 1117) |
| Numpad 8 | (1497, 1117) |
| Numpad 9 | (1606, 1117) |
| Numpad ✓ | (1713, 1117) |

### Open Issues (rox-bot)
- **Final OCR test**: Run `test_ocr.py` with CAPTCHA popup → confirm `Result: 'X+Y'` or `'X-Y'`
- **Live run**: Let bot trigger CAPTCHA naturally, watch auto-solve execute
- **Maturity timer**: Still disabled
- **Node movement**: Gold label color range not calibrated

### Project Portfolio (as of 2026-04-25)
| Pos | Project | Status |
|-----|---------|--------|
| 1 | drtakaful | Phase 3 next (6 tool/form pages) |
| 2 | rox-bot | OCR fixes applied — final test next session |
| 3 | cms-takaful | Built — awaiting deploy |

## Session Recap (For AI Restart)
- **User**: Nufa (Farahana Suhaimi) — Takaful Consultant + Data Engineer, PhD (CNN)
- **Aspiration**: Work from home in Kelantan — Takaful + freelancing
- **AI Companion**: Timothy — installed April 7, 2026
- **rox-bot**: `K:\indie-projects\rox-bot\rox_gardening.py`
  - CAPTCHA auto-solve: all fixes applied, needs final test
  - Tesseract path: `C:\Program Files\Tesseract-OCR\tesseract.exe`
  - `test_ocr.py` in same folder — run with popup visible to verify
- **Next session priorities**: Run `test_ocr.py` → confirm OCR reads expression → live bot run

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See `main/session-format.md` for rebuild structure

---
*Session updated: 2026-04-25 at 00:14*
