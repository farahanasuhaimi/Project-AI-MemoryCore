# cms-takaful — Dr Takaful CMS

## Project Info
- **Local path**: `K:\cms-takaful`
- **GitHub**: `https://github.com/farahanasuhaimi/cms-takaful`
- **Live URL**: `https://list.drtakaful.com`
- **Stack**: Laravel 12 + Blade + Alpine.js v3 + Tailwind v3 + MySQL + Laravel Breeze
- **Theme**: Matcha × strawberry
- **Auth**: Single-user session login (no registration). Session: 120 min.

## What It Is
A private, self-hosted CRM and business dashboard for Hana (Dr Takaful / AIA agent). Not SaaS — single user. Manages policyholders, leads, client interactions, prospecting strategies, commissions, and renewal alerts.

## Current Status
**Production — fully deployed and live at `list.drtakaful.com`.**
All core modules built and deployed. A few nice-to-haves pending.

## What's Built
| Module | Status |
|---|---|
| Auth (Breeze, single-user login only) | ✅ |
| Dashboard — stats, renewal alerts, commission totals, recent activity | ✅ |
| Policyholders — full CRUD + inline policy management | ✅ |
| Client detail view — WhatsApp deep links, policy history | ✅ |
| Leads — hot/warm split, stage tracking, convert to client | ✅ |
| Touchpoints — polymorphic interaction log (clients + leads) | ✅ |
| Reach Angles — prospecting strategy cards, tag clients, track rate | ✅ |
| Content Library — AI-generated content per angle, batch, pinning | ✅ |
| Plan Catalog — insurance product registry with commission rates | ✅ |
| Auto-renewal — computed dynamically from start_date + frequency | ✅ |
| Renewal alerts — ≤30 days banner, ≤7 days red badge | ✅ |
| Commission tracking — per-plan rate, estimated 1st-year per client | ✅ |
| Edit views for all entities | ✅ |
| Mobile responsive — collapsible sidebar, horizontal scroll | ✅ |

## Pending (Nice-to-haves)
- Export clients to CSV
- Search across leads (currently clients only)
- Birthday reminders
- Dark mode toggle

## Database (9 Models)
```
users               — single admin user
clients             — name, phone, ic_no, email, notes
policies            — client_id, plan_product_id, plan_type, coverage_amount,
                      start_date, frequency, premium_monthly
leads               — name, phone, source, temperature (hot/warm), stage,
                      interest_area, next_contact, converted_at
touchpoints         — polymorphic (client OR lead), channel, topic, notes,
                      next_action, next_action_date, contacted_at
reach_angles        — title, description, target_segment, status
angle_client        — pivot: reach_angle_id, client_id, reached_at
angle_contents      — AI content per angle: batch, style, content, is_pinned, model
plan_products       — plan_type, name, commission_first_year (%), attributes (JSON)
settings            — key/value store (API keys, config)
```

## Key Architecture Notes
- **Polymorphic touchpoints** — one log covers both clients and leads
- **Renewal date** computed from `start_date` + `frequency` — no stored column
- **Commission**: `annual_premium × (commission_rate / 100)`
- **Blade only** — no Vue/React/Livewire. Alpine.js for dropdowns/modals only
- **Alpine.js**: Use `{key, value}` objects for reactive arrays, not index syntax

## Resume Command
```
cd K:\cms-takaful && php artisan serve
```
