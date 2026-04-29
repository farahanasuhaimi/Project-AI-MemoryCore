# Current Session Memory - 2026-04-29
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — win-board new project setup
**Current Project**: win-board — `D:\Kerja\Codes\win-board`
**Status**: Scaffold complete, Google OAuth working, pushed to GitHub with precompiled assets

## Active Project
- **Name**: win-board (Daily Win Board)
- **Started**: 2026-04-29
- **Context**: Laravel 12 daily task board — commitment-first, dopamine-driven

## Working Memory

### win-board — Current State (end of 2026-04-29 session)

**Stack**: Laravel 12.58 + Tailwind v4 (`@tailwindcss/vite`) + MySQL + Google OAuth (Socialite)

**What's built**:
- Full scaffold: models, migrations, controllers, routes, views
- Gumroad UI (Syne/DM Sans/JetBrains Mono, thick borders, hard shadows, Gumroad palette)
- Google OAuth login — working locally
- Dashboard: daily commitment lock, 4-tier task board (Must/Should/Good/Parking Lot), streak + wins bar, celebration toasts, reset modal
- All task mutations AJAX — no page reloads
- SSL cert fix for Windows: Guzzle configured with `cacert.pem` in `AppServiceProvider`

**Database**: `daily_win_board` (MySQL) — all 7 migrations run

**GitHub**: `https://github.com/farahanasuhaimi/win-board` — 3 commits pushed
- Precompiled Vite assets in `public/build/` (for Hostinger — no Node needed)

**Not yet done**:
- Full end-to-end dashboard test
- Hostinger deployment
- Google OAuth production callback URL

### Hostinger Deploy — Next Steps
- SSH into Hostinger → git clone or git pull
- Set document root to `/public`
- Copy `.env.example` → `.env`, fill production values (DB, Google OAuth with production callback URL)
- `composer install --no-dev --optimize-autoloader`
- `php artisan key:generate && php artisan migrate --force && php artisan config:cache && php artisan route:cache`
- Update Google Cloud Console: add production callback URI

### Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | win-board | Scaffold done — deploy to Hostinger next |
| 2 | drtakaful | Phase 3 next (6 tool/form pages) |
| 3 | rox-bot | Dynamic detection done — test_ocr.py run needed |
| 4 | cms-takaful | Built — awaiting deploy |

## Session Recap (For AI Restart)
- **User**: Nufa (Farahana Suhaimi) — Takaful Consultant + Data Engineer, PhD (CNN)
- **win-board**: `D:\Kerja\Codes\win-board` — Laravel 12 daily task board
  - Google OAuth working (SSL fix via AppServiceProvider + cacert.pem at `C:\Users\IGS\cacert.pem`)
  - Precompiled assets pushed to GitHub for Hostinger
  - Next: deploy to Hostinger, test dashboard end-to-end
- **rox-bot**: `K:\indie-projects\rox-bot\rox_gardening.py` — still needs test_ocr.py run

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See `main/session-format.md` for rebuild structure

---
*Session updated: 2026-04-29*
