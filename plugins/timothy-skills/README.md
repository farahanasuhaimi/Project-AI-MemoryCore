# Timothy Skills Plugin

Auto-triggered skill set for Timothy, Nufa's AI companion.

## Active Skills

| Skill | Trigger | Level |
|-------|---------|-------|
| `save-memory` | "save", "save memory", "save progress", "update memory" | Lv.1 |

## Adding New Skills

1. Create a new folder: `skills/[skill-name]/`
2. Create `SKILL.md` inside with YAML frontmatter + protocol
3. Reference `skill-format.md` for the standard structure
4. Done — skill auto-activates based on its description field

## Plugin Info
- **Plugin name**: timothy-skills
- **Author**: Farahana Suhaimi
- **Created**: April 7, 2026
- **Platform**: Claude Code (Anthropic CLI)
