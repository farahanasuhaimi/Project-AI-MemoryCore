# cms-takaful — Dr Takaful CMS

## Project Info
- **Local path**: `D:\Kerja\Codes\cms-takaful`
- **GitHub**: `https://github.com/farahanasuhaimi/cms-takaful`
- **Live URL**: `https://list.drtakaful.com`
- **Stack**: Laravel 12 + Blade + Alpine.js v3 + Tailwind v3 + MySQL + Laravel Breeze
- **Theme**: Matcha × strawberry
- **Auth**: Invite-only registration. Admin creates token links; 7-day expiry. Session: 120 min.

## What It Is
A private, invite-only multi-tenant CRM for Hana and up to ~10 trusted friends (AIA takaful agents). Each user's data is fully isolated. Manages policyholders, leads, client interactions, prospecting strategies, commissions, and a two-sided marketplace for sharing AI content and plan products.

## Current Status
**Production — fully deployed and live at `list.drtakaful.com`.**
All phases complete. Marketplace (Strategy + Policy) live as of 2026-05-12.

## What's Built
| Module | Status |
|---|---|
| Auth — invite-only registration, admin-created token links (7-day expiry) | ✅ |
| Multi-tenancy — per-user data isolation via Eloquent global scopes on all 8 data models | ✅ |
| PII encryption — name, phone, IC on clients + leads (AES-256-CBC via APP_KEY encrypted cast) | ✅ |
| Dashboard — stats, renewal alerts, commission totals, recent activity | ✅ |
| Policyholders — full CRUD + inline policy management | ✅ |
| Client detail view — WhatsApp deep links, policy history | ✅ |
| Leads — hot/warm split, stage tracking, convert to client | ✅ |
| Touchpoints — polymorphic interaction log (clients + leads) | ✅ |
| Reach Angles — prospecting strategy cards, tag clients, track rate | ✅ |
| Content Library — AI-generated content per angle, pinning, copy | ✅ |
| Plan Catalog — insurance product registry with commission rates | ✅ |
| Auto-renewal — computed dynamically from start_date + frequency | ✅ |
| Renewal alerts — ≤30 days banner, ≤7 days red badge | ✅ |
| Commission tracking — per-plan rate, estimated 1st-year per client | ✅ |
| Activity log — admin view of all user actions across the system | ✅ |
| Admin panel — user management, toggle active, issue invitations, credits top-up | ✅ |
| Credits system — users earn/spend credits; transactions logged; balance in sidebar | ✅ |
| Strategy Marketplace — list AI content for sale; buyer pays credits; content copied to buyer's library | ✅ |
| Policy Marketplace — share plan products for free; star system; one-click import to own catalog | ✅ |
| Mobile responsive — collapsible sidebar, horizontal scroll | ✅ |

## Pending (Nice-to-haves)
- Export clients to CSV
- Search across leads (currently clients only)
- Birthday reminders
- Dark mode toggle

## Database (15+ Models / 20 Migrations)
```
users                    — name, email, password, credits, is_admin, is_active
invitations              — token, email, invited_by, used_at, expires_at
credit_transactions      — user_id, amount (±INT), type (bonus/topup/sale/purchase), description
activity_logs            — user_id (nullable), action, subject_type, subject_id, description

clients                  — user_id, name (enc), phone (enc), ic_no (enc), email, notes
policies                 — client_id, plan_product_id, plan_type, coverage_amount,
                           start_date, frequency, premium_monthly
leads                    — user_id, name (enc), phone (enc), source, temperature, stage,
                           interest_area, next_contact, converted_at
touchpoints              — polymorphic (client OR lead), channel, topic, notes,
                           next_action, next_action_date, contacted_at
reach_angles             — user_id, title, description, target_segment, status
angle_client             — pivot: reach_angle_id, client_id, reached_at
angle_contents           — user_id, angle_id, batch, style, content, is_pinned, model
plan_products            — user_id, plan_type, name, commission_first_year (%), attributes (JSON),
                           is_shared, shared_note
marketplace_policy_stars — user_id, plan_product_id (unique pair)
marketplace_listings     — seller_user_id, angle_content_id, title, description,
                           price_credits, status (active/removed)
marketplace_purchases    — buyer_user_id, listing_id, credits_paid, imported_content_id
settings                 — user_id, key, value
```

## Key Architecture Notes
- **Multi-tenancy**: Eloquent global scopes on all 8 user-owned models — zero query changes needed in most views
- **Marketplace isolation**: marketplace queries use `withoutGlobalScopes()` to see all users' shared content
- **PII search**: SQL LIKE impossible on encrypted columns — use collection filter after `.get()` (acceptable at ≤100 records/user)
- **Credits atomicity**: `CreditService::spend()` / `award()` both use `DB::transaction()` with increment/decrement
- **Content purchase flow**: buy() copies angle_content to buyer + auto-creates "Marketplace Imports" angle via `firstOrCreate`
- **Polymorphic touchpoints**: one log table covers both clients and leads
- **Renewal date**: computed from `start_date` + `frequency` — no stored column
- **Blade only** — no Vue/React/Livewire. Alpine.js for dropdowns/modals/optimistic UI

## Key Services
- `CreditService` — `award()`, `spend()` with DB transaction safety
- `AngleContentService` — AI content generation per reach angle
- `InvitationController` — token generation, expiry check, user registration with starter credits

## Resume Command
```
cd D:\Kerja\Codes\cms-takaful
php artisan serve
```

## Deploy Command
```
SSH_BASE="domains/drtakaful.com/public_html/list" python tools/hostinger_ssh.py "git pull && php artisan migrate --force"
```
