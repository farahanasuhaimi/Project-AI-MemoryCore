# Current Session Memory - 2026-05-19
*Active working memory for current conversation*

## Session Context
**Session Type**: cms-takaful Hostinger deploy (home PC)
**Last Active Project**: cms-takaful (`K:\cms-takaful`, live at `list.drtakaful.com`)
**Status**: Focus Points feature fully deployed to production. ✅

## What Was Done

### cms-takaful — Focus Points deployed to Hostinger ✅
- `focus_points` table migration applied on Hostinger
- `strategy_focus_point` pivot migration applied on Hostinger
- `FocusPointSeeder` run — 22 focus points live across 6 groups
- Caches cleared (`optimize:clear`)

**Deploy command used:**
```
SSH_BASE="domains/drtakaful.com/public_html/list" python tools/hostinger_ssh.py "git pull" "php artisan migrate --force" "php artisan db:seed --class=FocusPointSeeder --force" "php artisan optimize:clear"
```

## Next Up

### cms-takaful — Wire focus points into strategy UI
- Attach focus points picker when creating/editing a strategy
- Show linked focus points on strategy show/index views

### rox-bot — Input bar coordinate verification (carry-over)
1. Trigger a CAPTCHA in RoX
2. Run `python rox_agent.py` → wait for `[DEBUG] Saved debug_captcha.png`
3. Open `debug_captcha.png` — verify red circle lands on the dark input bar
4. If off, adjust Gemma4 prompt or apply coordinate offset

### drtakaful — Phase 3 Retheme (6 tool/form pages)
- `kalkulator-hibah.html`
- `kalkulator-belanjawanku.html`
- `analisis-keperluan.html`
- `borang-permohonan.html`
- `borang-fact-finding-medical-card.html`
- `konsultasi-percuma.html`

## Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | cms-takaful | Focus points live on Hostinger ✅. Next: wire into strategy UI |
| 2 | rox-bot | Agent loop built. Input bar coordinate pending verification |
| 3 | win-board | Phase 4 (Goal Cascade) next |
| 4 | Project-B | Phase 5c done — dashboard live |
| 5 | takaful-content-planner | Blocked on Google OAuth |
| 6 | drtakaful | FAQPage schema done ✅. Phase 3 retheme next |
| 7 | bookkeeping (RezTax) | 🔴 Audit pending |

## Notes
- cms-takaful on home PC at `K:\cms-takaful`
- drtakaful local paths: `D:\Kerja\Codes\drtakaful` (office) / `D:\WebDev\Takaful` (home)
- Hermes3 installed on home PC Ollama (`hermes3:latest`, 4.7GB)
- LDPlayer ADB: `C:\LDPlayer\LDPlayer9\adb.exe`, device `emulator-5556`, resolution 1600×900
- rox-bot at `K:\indie-projects\rox-bot` — not a git repo
- Hostinger SSH tool: `python K:\Project-AI-MemoryCore\tools\hostinger_ssh.py "command"`
- Hostinger needs `SSH_BASE` env var set per project

---
*Session: 2026-05-19 — home PC, cms-takaful focus points deployed to Hostinger*
