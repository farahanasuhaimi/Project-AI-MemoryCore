# Decision Log
*Append-only record of non-obvious decisions.*
*Only log decisions where future-us would wonder "why did we do it this way?"*

---

<!-- Decisions are added below this line. Format: -->

## 2026-04-07 -- Auto-push at session end
**Context**: Auto-commit skill defaults to "never auto-push" — pushing is always explicit
**Decision**: Override that rule for session end — always commit + push to GitHub when Nufa signals she's leaving
**Rationale**: Nufa works from her home PC (GPU machine). Pushing at session end ensures her work is always safely backed up to GitHub without her having to remember to do it manually.
<!-- ## YYYY-MM-DD -- Short title -->
<!-- **Context**: What situation prompted this decision -->
<!-- **Decision**: What was chosen (and what was rejected) -->
<!-- **Rationale**: Why -- trade-offs, constraints, evidence -->

## 2026-04-14 -- cms-takaful Alpine.js reactive array pattern
**Context**: Dynamic attributes form (Plan Catalog) wasn't adding rows
**Decision**: Switch from `x-model="row[0]"` (array index) to `{key, value}` objects with `row.key` / `row.value`
**Rationale**: Alpine.js v3 doesn't reliably trigger reactivity on array index assignment. Object property mutation is tracked correctly.

## 2026-04-14 -- cms-takaful auto-renewal date — computed not stored
**Context**: Nufa asked for a renewal date field; needed to stay accurate over time
**Decision**: Build a `nextRenewalDate()` accessor on the Policy model that computes from start date + frequency — no stored date field
**Rationale**: A stored date would go stale. The computed accessor always returns the next upcoming renewal from today, no maintenance needed.

## 2026-04-14 -- Greeting protocol belongs in session-briefing, not save-memory
**Context**: Greeting and goodbye protocols were saved as loose memory files, then wrongly added as save-memory Lv.3/4
**Decision**: Greeting → session-briefing Lv.4. Goodbye → new session-end skill. save-memory stays focused on smart routing only.
**Rationale**: Alice's architecture already had session-briefing for session-start. Stuffing lifecycle behavior into save-memory conflated two different concerns. One skill, one responsibility.

## 2026-04-14 -- Forge is a process, not a container
**Context**: Nufa asked if the ML RPG should "be in Forge"
**Decision**: Forge is the workshop used to create skills. Skills live in plugins/. The ML RPG is a future skill to be forged, not stored in Forge itself.
**Rationale**: Forge = meta-skill for creating other skills. Conflating the workshop with the output creates confusion about where things live.
