# win-board — Daily Win Board

## Project Info
- **Local path**: `D:\WebDev\win-board`
- **GitHub**: `https://github.com/farahanasuhaimi/win-board`
- **Live URL**: `https://life.drtakaful.com`
- **Stack**: Laravel 12 + Tailwind v4 + MySQL + Google OAuth (Socialite)
- **Hosting**: Hostinger

## Current Status
**Phase 1 + Phase 2 + Polish — Complete**
Phase 3 (Goal Cascade) is next — no start date set yet.

## What's Built
- Daily commitment lock (links to a Must task; ticking it marks commitment done)
- Four-tier board: Must (max 3) / Should (max 5) / Good / Parking Lot
- Must task delete guard — confirmation modal with "Park it" option
- Carry-forward: Must + Should + Park tasks persist day-to-day with LATE/URGENT badges
- Win counter + streak tracker
- Move between sections (must → park, should ↔ good ↔ park)
- Reset day
- Google OAuth
- Mobile responsive (two-row navbar, buttons always visible on touch)
- `/history` — weekly summary cards for past completed weeks
- `/review` — Mon-Sun bar chart (by done_at), section completion rates
- `/admin` — user management, stats, is_admin toggle

## Database
```
users               — id, name, email, google_id, avatar, is_admin
daily_commits       — id, user_id, text, task_id (FK nullable), date, locked_at, unlocked_count
tasks               — id, user_id, text, section, done, date, sort_order, done_at, deleted_at
user_stats          — id, user_id, streak, total_wins, last_active_date
```

## Phase 3 — Goal Cascade (Planned)
- 10-year → 5-year → yearly → quarterly → daily goal cascade
- Daily tasks linkable to quarterly goals
- Recurring tasks
- PWA / installable on mobile

## Key Decisions
- Commitment intentionally separate from Must tasks but can be linked
- Park tasks carry forward (ideas shouldn't expire)
- Must cap (3) applies across all dates including carry-forward
- Wins counted by done_at (when completed), not task.date (when assigned)
- History shows past completed weeks only — current week not shown until it ends
