# monochrome-ui

A reusable **Codex Agent Skill** for clean, high-contrast monochrome websites and web apps: square controls, neutral borders, information-dense layouts, and responsive accessible components.

The skill adapts to the project's existing framework and behavior; the standalone demo and CSS are optional reference assets.

## Install in Codex

Ask the built-in `$skill-installer` in Codex to install this GitHub **directory**:

```text
$skill-installer install https://github.com/Transient-Onlooker/monochrome-ui/tree/main/skills/monochrome-ui
```

To install manually for **personal** use on Windows (PowerShell):

```powershell
$checkout = Join-Path $env:TEMP "monochrome-ui-checkout"
git clone --depth 1 https://github.com/Transient-Onlooker/monochrome-ui.git $checkout
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse "$checkout\skills\monochrome-ui" "$HOME\.agents\skills\"
```

This manual command assumes neither the temporary checkout nor the destination skill directory already exists. To update an installed copy, remove the prior skill directory intentionally before copying the replacement, or use a controlled git-based update.

For **one project only**, copy `skills/monochrome-ui/` to `<project>/.agents/skills/monochrome-ui/`.

Codex discovers skills in these paths; if needed, restart Codex or inspect `/skills`. The skill installer also supports other GitHub repos using their skill-directory URLs.

## Use

```text
$monochrome-ui Restyle this search page. Keep all existing functionality and adapt the existing components.
```

Alternatively, request a monochrome, sharp-edged, minimalist dashboard/search UI and let Codex match the skill automatically.

## Contents

```text
skills/monochrome-ui/
  SKILL.md                    Agent Skills metadata and workflow
  references/DESIGN-SYSTEM.md Tokens, geometry, component and accessibility rules
  assets/monochrome.css       Standalone, scoped reference CSS
  assets/demo.html            Local interactive HTML demo
  scripts/smoke_test.py       Dependency-free package checks
  scripts/browser_check.py    Optional Playwright interaction/overflow checks
```

## Validate

From `skills/monochrome-ui/`:

```bash
python scripts/smoke_test.py
# Optional: pip install playwright && python -m playwright install chromium
python scripts/browser_check.py
```

Open `assets/demo.html` in a browser for an interactive example. It has no backend, network requests, or external dependencies.

## References

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI skills examples](https://github.com/openai/skills)