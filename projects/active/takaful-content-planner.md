# takaful-content-planner — Dr Takaful Content Planner

## Project Info
- **Local path**: `K:\content-takaful-app\takaful-content-planner`
- **GitHub**: not set up yet (still using laravel/laravel remote)
- **Live URL**: not deployed yet
- **Stack**: Laravel 11 + Tailwind v3 + MySQL + Google OAuth (Socialite) + PWA + Web Push
- **Dev port**: `http://localhost:8002`

## What It Is
A PWA for a Malaysian takaful content creator (Dr Takaful / AIA agent) to plan, schedule, and auto-generate social media posts across IG, FB, WhatsApp Broadcast, and WA DM. Includes AI content generation using user's own LLM API key.

## Current Status
**Phase 1 — Foundation complete (2026-05-10)**
Phase 2 (Content CRUD) is next.

## Blocker
**Google OAuth not configured yet.** App loads but login requires Google Client ID + Secret.
- Go to [console.cloud.google.com](https://console.cloud.google.com) → Create OAuth credentials
- Add to `.env`: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`
- Authorised redirect URI: `http://localhost:8002/auth/google/callback`

## What's Built (Phase 1)
- DB migrations: `users` (google_id, avatar), `content_posts`, `push_subscriptions`, `user_settings`
- Models: `User`, `ContentPost`, `UserSetting`, `PushSubscription` with relationships
- API key stored encrypted via Laravel `Crypt`
- Google OAuth — `SocialAuthController` (redirectToGoogle + handleGoogleCallback)
- Base layout — sidebar (desktop) + bottom nav (mobile)
- Login page (Google sign-in button)
- Dashboard stub — today's posts, overdue, upcoming 7 days, stats bar
- All routes wired up
- Assets compiled (Tailwind v3, Plus Jakarta Sans + Inter)

## Build Plan
| Phase | Feature | Status |
|---|---|---|
| 1 | Foundation — DB, models, auth, layout | ✅ Done |
| 2 | Content CRUD — create/edit form, list view, filters | 🔜 Next |
| 3 | Dashboard — today, overdue, upcoming, stats | 🔜 |
| 4 | Settings — LLM config (encrypted), notifications toggle | 🔜 |
| 5 | AI Content Generator — timing + topic rotation + LLM call | 🔜 |
| 6 | PWA + Push Notifications — manifest, SW, reminders | 🔜 |

## Database
```
users               — id, name, email, google_id, avatar, password (nullable), remember_token
content_posts       — id, user_id, title, body, topic (enum), platform (JSON), status (enum),
                      scheduled_at, posted_at, notes, is_ai_generated, ai_provider
push_subscriptions  — id, user_id, endpoint, public_key, auth_token
user_settings       — id, user_id, llm_provider, llm_api_key (encrypted), llm_base_url,
                      llm_model, notifications_enabled
```

## Topic / Platform / Status Enums
- **Topics**: CI, Medical, PA, Hibah, General, Tips, Promo
- **Platforms**: IG, FB, WA_Broadcast, WA_DM
- **Statuses**: Idea → Draft → Scheduled → Posted

## Resume Command
```
cd K:\content-takaful-app\takaful-content-planner && php artisan serve --port=8002
```
