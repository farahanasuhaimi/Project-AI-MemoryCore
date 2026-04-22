# rox-bot - RoX Gardening Auto-Clicker
*Python bot to automate gardening in Ragnarok X: Next Generation*

## Project Overview
- **Type**: Tool / Game Automation
- **Period**: 2026-04-23 - Active
- **Tech Stack**: Python + pyautogui + OpenCV + win32gui
- **Completion**: 35%
- **Duration**: 0 min

## Current Status
- **Last Session**: 2026-04-23 - Core bot built, manual CAPTCHA mode active
- **Next Steps**:
  - Calibrate INPUT_FIELD / CONFIRM_BUTTON / NUMPAD coordinates for CAPTCHA auto-solve
  - Re-enable maturity timer detection (OCR via pytesseract — logic in comments)
  - Calibrate gold label color range for node movement
- **Known Issues**:
  - Maturity timer detection disabled (OCR removed temporarily)
  - Node movement exists but never triggers (maturity timer always returns 0)
  - CAPTCHA auto-solve disabled — manual 15s pause instead

## Session History (Last 5)

### 2026-04-23 - Core Bot Built
- **Changes**: Template match gardening button, 11-click CAPTCHA counter, manual CAPTCHA pause with countdown, window focus on startup, node movement skeleton (color detection), maturity timer stub
- **Time Spent**: ~0 min

## Historical Summary
[No history yet — this section is populated when session count exceeds 5]

## Technical Notes
- **Repository**: `K:\indie-projects\rox-bot\`
- **Entry point**: `rox_gardening.py`
- **Key Dependencies**: pyautogui, opencv-python, numpy, Pillow, pywin32, pytesseract (disabled)
- **Game window title**: `GAME_WINDOW_TITLE = "RoX"` — must match emulator title bar
- **CAPTCHA trigger**: every 11 gardening clicks (`CAPTCHA_EVERY_N`)
- **Auto-solve logic**: preserved in comments inside `handle_captcha()` and `check_maturity_timer()`

---
**Last Updated**: 2026-04-23 | **Position**: #1/10 Active
