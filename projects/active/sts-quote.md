---
project: sts-quote
status: active
started: 2026-06-10
last_updated: 2026-06-11
---

# sts-quote — STS EDAC Engineering Quotation System

## Purpose
Internal quotation management system for STS EDAC Engineering Sdn Bhd. Handles client → project → scope → quotation flow, with a Smart Add panel for detailed line-item building and PDF export.

## Stack
Laravel 12 · PHP 8.2 · Alpine.js v3 · Tailwind CSS · MySQL · DomPDF · Spatie Laravel-Permission

## Local Path
`D:\Kerja\Codes\sts-quote`

## Current State (2026-06-11)

### What's Done
| Area | Detail |
|------|--------|
| Full scaffold | Migrations, models, seeders, controllers, routes ✅ |
| All views | Clients, projects, packages, quotations (edit + show + pdf) ✅ |
| Smart Add panel | 4 tabs: Manpower, Scaffolding, T&C%, Cost Plus ✅ |
| Manpower input | 6 fields: NOR/SUN/PH days + NOR O/T / SUN O/T / PH O/T hours ✅ |
| Rate card | 6-column structure (Unit Rate, Sun Rate, Pub. Hol × NOR/OT) ✅ |
| PDF ordering | Indirect Manpower → Direct → Indirect OT → Direct OT → rest ✅ |
| PDF row expansion | NOR / SUN / PH / NOR O/T / SUN O/T / PH O/T shown as separate lines ✅ |
| Role middleware | Spatie `role` alias registered in bootstrap/app.php ✅ |
| Migration | `item_type` + `meta` columns live on office DB ✅ |
| DB | Migrated + seeded with real rates ✅ |

### meta Column Structure
- Regular manpower rows: `{nor_days, sun_days, pub_days}`
- OT rows: `{nor_ot_hours, sun_ot_hours, pub_ot_hours}`
- Scaffolding: `{actual_cost, markup_pct}` *(not yet expanded in PDF)*
- Cost Plus: `{actual_cost, markup_pct}`

## What's Next (priority order)
1. **Cleanup temp code** — remove CSRF bypass, `/dev/reset` route, `\Log::info` debug lines
2. **Fix non-manpower calculations** — Scaffolding, T&C%, Cost Plus row totals need review
3. **Phase 2 planning** — Expense Ledger + Claims module

## Known Notes
- OT rows saved before 2026-06-11 use old meta `{ot_hours: N}` — fall through to single-row display in PDF (correct, no breakage)
- Grand total in PDF uses blended stored `qty × unit_price`; displayed expanded rows use actual rates — ~cents rounding gap is expected
- Smoke test (subagent-verified 2026-06-11): Rate card ✅ · Calculation ✅ · Save ✅ · Reload ✅
