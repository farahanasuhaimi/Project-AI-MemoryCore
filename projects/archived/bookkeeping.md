# bookkeeping — RezTax Personal Finance App

## Project Info
- **Local path**: `D:\Kerja\Codes\bookkeeping`
- **GitHub**: `https://github.com/farahanasuhaimi/bookkeeping`
- **Live URL**: Not deployed (local only)
- **Stack**: Laravel 12 + Tailwind v4 + MySQL + Lemon Squeezy + dompdf
- **Last commit**: 2026-04-07

## Current Status
**Archived before review session — unknown what's missing before deploy.**
Last commit: `fix: port category slug fix to main branch` (2026-04-07).
No known next phase — needs a review session to determine what's missing before deploy.

## What's Built
- Auth — login, register, forgot/reset password
- Dashboard
- Income CRUD (`/incomes`)
- Expense CRUD (`/expenses`)
- Tax summary page + PDF export (LHDN context)
- Savings tracking + savings goals
- CSV import — preview flow before committing
- Settings — profile, password, payment methods, categories, preferences (tooltip toggle)
- Admin panel — user list, plan management, categories
- Pricing page (Lemon Squeezy integration stub)
- Tooltips system (user-configurable)

## Database
```
users               — standard auth + plan field
incomes             — user_id, amount, category, date, notes
expenses            — user_id, amount, category, payment_method, date, notes
savings             — user_id, amount, goal_id, date
savings_goals       — user_id, name, target_amount, target_date
categories          — user_id (or global), name, slug, type
payment_methods     — user_id, name
```
*(schema inferred from controllers — verify if needed)*

## What's Next (Unknown)
- Needs a session to assess what's missing before deploy
- Possible candidates: reports/charts, recurring transactions, actual Lemon Squeezy wiring

## Key Notes
- Project referenced as "RezTax" in Timothy's memory — folder name is `bookkeeping`
- Lemon Squeezy vendor package present (`lemonsqueezy/laravel`) — payment gating may be partially wired

---
**Last Updated**: 2026-04-07 | **Status**: Archived (manual) — 2026-06-08
**Resume when**: Ready for pre-deploy review + launch sprint
