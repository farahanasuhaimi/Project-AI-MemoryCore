# win-board — Daily Win Board

## Project Info
- **Local path**: `D:\WebDev\win-board`
- **GitHub**: `https://github.com/farahanasuhaimi/win-board`
- **Live URL**: `https://life.drtakaful.com`
- **Stack**: Laravel 12 + Tailwind v4 + MySQL + Google OAuth (Socialite)
- **Hosting**: Hostinger

## Current Status
**Phase 3 (Gamification) — Complete**
Phase 4 (Goal Cascade) is next — no start date set yet.

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
- Google Calendar strip (async load, shows today's events + must-fit check)
- Onboarding modal (3-slide Gumroad style, first login only)
- Task time estimates (10m/30m/1h/2h/6h), required for Must; overload warning >12h
- Urgency emoji scale: ⚠️→🟠→🔴→🚨→🔥→☠️→💀 (1–7+ days late)

### Phase 3 — Gamification (complete, 2026-05-10)
- **HUD strip** — compact bar: streak, wins, shields, level, XP bar in one row
- **XP system** — Must +30, Should +20, Good +10; 10-level curve (Starter → GOAT)
- **Streak shields** — earn 1 shield every 7 days (max 3); auto-consumed on exactly 1 missed day
- **Comeback mechanic** — 2× XP for 3 days after streak break
- **Daily quests** — 3 randomised per day, hidden behind HUD toggle (📋 N/3 ▾); +10 XP each, +20 bonus for all 3
- Quest pool: Clear all Musts / Should Champion / Nice Touch / Early Bird / High Five

## Database
```
users               — id, name, email, google_id, avatar, is_admin, onboarded_at, google tokens
daily_commits       — id, user_id, text, task_id (FK nullable), date, locked_at, unlocked_count
tasks               — id, user_id, text, section, done, date, sort_order, done_at, estimated_minutes, deleted_at
user_stats          — id, user_id, streak, total_wins, last_active_date, xp, level, shields, comeback_days_left
daily_quests        — id, user_id, date, quest_type, completed, completed_at, xp_reward
```

## Services
- `GamificationService` — XP grant, level calculation, 10-level curve
- `QuestService` — daily quest generation, progress evaluation, all-quests bonus
- `GoogleCalendarService` — OAuth token refresh, multi-calendar fetch

## Phase 4 — Goal Cascade (Planned)
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
- XP not deducted on task un-check (standard gamification convention)
- Shield covers exactly 1 missed day; gap > 1 day resets streak regardless
- Quest XP reduced to 10/quest vs task XP to keep task completion the primary reward
