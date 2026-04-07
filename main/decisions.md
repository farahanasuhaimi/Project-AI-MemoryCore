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
