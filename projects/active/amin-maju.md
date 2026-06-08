---
project: amin-maju
status: active
started: 2026-06-08
last_updated: 2026-06-08
---

# amin-maju — Home Contractor Management System

## Purpose
Bookkeeping + project management app for Kak Amin's home contractor business. Built by Nufa to help sister manage projects from land purchase to key handover.

## Users
| Role | Person |
|------|--------|
| Owner | Kak Amin (sister) |
| Worker | Husband |
| Bookkeeper | Nufa |

## Stack
Laravel 12 · Tailwind v4 · Alpine.js v3 · MySQL · Hostinger

## Current State (2026-06-08)
- Full scaffold complete (all 5 phases built in one session)
- Smoke-testing in progress — Auth ✅, Projects ✅, Tasks (checkbox AJAX) ✅
- Quotation edit bug fixed (HTML attribute encoding + @json)
- Dashboard owner panel — live task grouping (now / this week / next week)
- Git repo initialized, pushed to GitHub (private)
- Hostinger deploy: NOT yet configured

## Next Steps
- Continue smoke test: Finance, Reports, Role restrictions
- Fix any remaining bugs from testing
- Hostinger subdomain + auto-deploy setup
- Change seed credentials to real user data before production seed

## Repo
GitHub private: `amin-maju`
Local: `D:\Kerja\Codes\amin-maju`
