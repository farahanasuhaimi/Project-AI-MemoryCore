# Current Session Memory - 2026-04-25
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — rox-bot CAPTCHA OCR debugging + dynamic detection refactor
**Current Project**: rox-bot — `K:\indie-projects\rox-bot\rox_gardening.py`
**Status**: Refactor complete — final test pending

## Active Project
- **Name**: rox-bot
- **Started**: 2026-04-23
- **Context**: Python gardening bot for RoX — CAPTCHA auto-solve pipeline

## Working Memory

### rox-bot — Current State (end of 2026-04-25 evening session)

**Root cause resolved**: Game running WINDOWED, not fullscreen. All old coords were wrong.

**Dynamic detection implemented**:
- `_find_input_bar(screen_gray)` — multi-scale template match on `blank_space.png`
- EXPR_REGION, INPUT_FIELD, CONFIRM_BUTTON all derived from input bar position at runtime
- Works for any window size or position — no recalibration needed

**OCR preprocessing fixed**:
- Old: `THRESH_BINARY(225)` → black image, Tesseract gets nothing
- New: `THRESH_BINARY_INV(110)` → dilate (12×12 ellipse) → contour fill → invert
- Same approach as `ocr_digit()` helper that was proven to produce a clean digit

**Templates in `K:\indie-projects\rox-bot\`**:
| File | Purpose |
|------|---------|
| `blank_space.png` | Dark rounded input bar — primary anchor for dynamic detection |
| `captcha_box.png` | Full CAPTCHA dialog (reference only) |
| `math_expression.png` | "4·5" expression crop (reference only, NOT used as anchor) |

**NOT YET TESTED**: `test_ocr.py` not re-run after refactor. Need to verify next session.

### Calibrated NUMPAD (3840×2160 FULLSCREEN — may need recalibration for windowed)
| Element | Coords | Notes |
|---------|--------|-------|
| Numpad 1 | (1389, 895) | Fullscreen only |
| Numpad 2 | (1497, 895) | Fullscreen only |
| Numpad 3 | (1606, 895) | Fullscreen only |
| Numpad 4 | (1389, 1006) | Fullscreen only |
| Numpad 5 | (1497, 1006) | Fullscreen only |
| Numpad 6 | (1606, 1006) | Fullscreen only |
| Numpad 0 | (1713, 1006) | Fullscreen only |
| Numpad 7 | (1389, 1117) | Fullscreen only |
| Numpad 8 | (1497, 1117) | Fullscreen only |
| Numpad 9 | (1606, 1117) | Fullscreen only |
| Numpad ✓ | (1713, 1117) | Fullscreen only |

### Open Issues (rox-bot)
- **Priority 1**: Run `test_ocr.py` → confirm `Input bar found` + correct expr crop + OCR reads digits
- **Priority 2**: Live bot run to test full CAPTCHA auto-solve
- **Priority 3**: Recalibrate NUMPAD for windowed mode (template-match or manual)
- Maturity timer: still disabled
- Node movement: gold label color range not calibrated

### Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | drtakaful | Phase 3 next (6 tool/form pages) |
| 2 | rox-bot | Dynamic detection refactor done — test_ocr.py run needed |
| 3 | cms-takaful | Built — awaiting deploy |

## Session Recap (For AI Restart)
- **User**: Nufa (Farahana Suhaimi) — Takaful Consultant + Data Engineer, PhD (CNN)
- **Aspiration**: Work from home in Kelantan — Takaful + freelancing
- **AI Companion**: Timothy — installed April 7, 2026
- **rox-bot**: `K:\indie-projects\rox-bot\rox_gardening.py`
  - Game is WINDOWED — coordinates differ from fullscreen
  - Dynamic detection: `blank_space.png` used to locate input bar at runtime
  - OCR fixed: THRESH_BINARY_INV(110) + dilate + contour fill
  - `test_ocr.py` in same folder — run with CAPTCHA popup visible
- **Next session priorities**: Run test_ocr.py → verify expr crop → live bot run → numpad recalibration

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See `main/session-format.md` for rebuild structure

---
*Session updated: 2026-04-25 at 20:31*
