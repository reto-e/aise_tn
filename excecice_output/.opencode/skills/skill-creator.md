---
name: skill-creator
description: Create a new reusable OpenCode skill file
---

# Skill Creator

Use this skill to create a new skill for OpenCode.

## Steps

1. **Choose a name** — use lowercase kebab-case (e.g. `my-skill`).

2. **Create the file** at `.opencode/skills/<name>.md` inside the project root.

3. **Add frontmatter** at the top of the file:
   ```markdown
   ---
   name: <skill-name>
   description: One sentence describing when this skill is triggered
   ---
   ```

4. **Write the skill body** — use clear, imperative instructions:
   - Break the task into numbered steps
   - Reference specific file paths, commands, or patterns where relevant
   - Keep the skill focused on a single, well-defined task
   - Avoid vague instructions — be concrete about what to do and in what order

5. **Keep skills reusable** — do not hardcode project-specific values unless the skill is intentionally project-scoped. Use placeholders like `<component-name>` for variable parts.

6. **Verify** the skill appears when typing `/` in OpenCode from the project directory.
