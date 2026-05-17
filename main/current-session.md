# Current Session Memory - 2026-05-17
*Active working memory for current conversation*

## Session Context
**Session Type**: Infrastructure + rox-bot Hermes agent exploration (home PC)
**Last Active Project**: rox-bot (`K:\indie-projects\rox-bot`)
**Status**: Agent loop running. Input bar coordinate needs verification.

## What Was Done

### cms-takaful — Seeder (Done)
- Ran `ReachAngleSeeder` on Hostinger via SSH — 10 angles seeded for `admin@drtakaful.com` ✅

### rox-bot — Hermes Agent Architecture Built
New file: `K:\indie-projects\rox-bot\rox_agent.py`

**Stack:**
- Gemma4 (Ollama) → vision: classify game state + locate input bar
- Hermes3 (Ollama, pulled today) → agent brain: tool calling for non-captcha decisions
- ADB (`C:\LDPlayer\LDPlayer9\adb.exe`, device `emulator-5556`) → all taps + screenshots

**CAPTCHA flow (correct sequence):**
1. Gemma4 detects state=captcha + input bar coordinates
2. OCR reads expression from region above input bar
3. Click input bar → numpad slides up
4. Fresh screenshot → detect numpad grid (validated 3×4)
5. Click digits → click Confirm

**What works:**
- ADB connected, screenshot + tap working
- Agent loop ticking
- Numpad grid validation (rejects false positives from game UI)
- Hermes bypassed for CAPTCHA (deterministic)
- Debug image auto-saved as `debug_captcha.png` when captcha detected

**What's pending:**
- Gemma4's input bar coordinates slightly off — need to check `debug_captcha.png` with CAPTCHA visible
- Once input bar click lands correctly, full loop should complete

**Changes made to rox_gardening.py:**
- Multi-scale `find_gardening_button()` (scales 0.3–1.5)
- `detect_numpad_buttons()` with bottom-half constraint + grid validation
- `find_captcha_input_bar()` and `find_captcha_confirm_button()` (color detection)
- Absolute paths for all templates (`_HERE = os.path.dirname(__file__)`)
- `ocr_expression()` accepts optional `numpad_positions` for region derivation

## ⚠️ First Thing Next Session (rox-bot)
1. Trigger a CAPTCHA in RoX
2. Run `python rox_agent.py` and wait for `[DEBUG] Saved debug_captcha.png`
3. Open `debug_captcha.png` — verify red circle lands on the dark input bar
4. If off, adjust Gemma4 prompt or apply coordinate offset

## Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | cms-takaful | Seeder done. Next: shareable client link, lead linking |
| 2 | rox-bot | Agent loop built. Input bar coordinate pending verification |
| 3 | win-board | Phase 4 (Goal Cascade) next |
| 4 | Project-B | Phase 5c done — dashboard live |
| 5 | takaful-content-planner | Blocked on Google OAuth |
| 6 | drtakaful | FAQPage schema in progress |
| 7 | bookkeeping (RezTax) | 🔴 Audit pending |

## Notes
- Hermes3 now installed on Ollama (4.7GB, `hermes3:latest`)
- LDPlayer ADB: `C:\LDPlayer\LDPlayer9\adb.exe`, device `emulator-5556`, resolution 1600×900
- rox-bot at `K:\indie-projects\rox-bot` — not a git repo

---
*Session: 2026-05-17 — home PC, cms-takaful seeder + rox-bot Hermes agent*
