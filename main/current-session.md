# Current Session Memory - 2026-04-15
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — cms-takaful feature build + deployment
**Current Project**: cms-takaful — live at list.drtakaful.com
**Status**: Complete
**Time**: Night (23:04)

## Current Focus
- **Primary Task**: AI content generation for Reach Angles — built and deployed
- **Progress**: Complete — full feature live on Hostinger

## Working Memory

### Active Context
- **Current Topic**: Session wrap
- **Immediate Goals**: Done for the night
- **Recent Progress**: Vite → Option 1 (pre-build assets), AI generate feature, Content Library, mobile optimisation
- **Next Steps**: Full browser testing of cms-takaful, ML RPG build session, ML Phase 1 (synthetic_data.py)

### Important Decisions
- Tailwind CDN (Option 2) abandoned — broke custom color palette visually
- Option 1 chosen: `npm run build` locally, commit `public/build/`, Hostinger serves pre-built files
- API key stored in DB (`settings` table), never hardcoded — swappable via UI
- DeepSeek API used (OpenAI-compatible endpoint), `withoutVerifying()` for Windows SSL issue
- Content Library page added for browsing + copying all pinned content

## Session Recap (For AI Restart)
- **User**: Nufa (Farahana Suhaimi) — Takaful Consultant + Data Engineer, PhD in medical image processing (CNN)
- **Aspiration**: Work from home in Kelantan — Takaful + freelancing
- **AI Companion**: Timothy — fully installed April 7, 2026
- **cms-takaful**: Laravel 12 CRM live at `list.drtakaful.com` (Hostinger shared hosting)
  - Vite assets: pre-built locally, committed to git (`public/build/` no longer gitignored)
  - AI content generation: DeepSeek API → 3 styles per angle (casual/story/factual), pinned to Content Library
  - Settings page: API key, model, base URL stored in DB
- **Next session priorities**: cms-takaful browser testing, ML RPG build, ML Phase 1 (gradient descent)

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See `main/session-format.md` for rebuild structure
- **Auto-reset**: When line count exceeds 500 — preserve recap, clear details, rebuild from template

---
*Session updated: 2026-04-15 at 23:04*
