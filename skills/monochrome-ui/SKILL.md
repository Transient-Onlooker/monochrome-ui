---
name: monochrome-ui
description: Design or restyle websites and web apps using a clean, high-contrast monochrome visual system with square-edged controls, thin borders, compact information-dense layouts, strong typography, and responsive search/filter/card interfaces. Use when the user requests monochrome UI, black-and-white minimal styling, understated dashboards, search and list pages, or wants an existing UI made visually consistent in this style. Not for backend-only tasks or when the user explicitly specifies a different visual brand.
---

# Monochrome UI

Build practical, restrained interfaces that make content and actions immediately accessible. This is a **design and implementation** skill, not an instruction to replace an app's domain logic or framework.

## Workflow

1. **Inspect before editing.** Identify the app framework, existing design tokens, components, routes, current accessibility patterns, and relevant UI tests. Preserve architecture, copy, application behavior, data flow, and branding constraints unless explicitly asked to change them.
2. **Choose scope.** Identify primary user tasks and the few screens/components involved. Favor clear headers and immediate working content over decorative hero sections. Do not impose a filter sidebar on apps that do not need filtering.
3. **Read** [`references/DESIGN-SYSTEM.md`](references/DESIGN-SYSTEM.md) for tokens, geometry, responsive rules, component states, and adaptations. For an implementation reference, inspect [`assets/monochrome.css`](assets/monochrome.css) and [`assets/demo.html`](assets/demo.html) as needed. These are examples, not runtime dependencies.
4. **Implement in the native stack.** Translate tokens and patterns into the project's existing CSS, utility classes, components, or design system. Prefer semantic HTML and minimal changes. For a new vanilla HTML project, the prefixed `.mono-*` CSS can be used directly.
5. **Handle all states.** Specify hover, active/selected, focus-visible, disabled, loading, empty, error, dialog, and long-content states. Use visual labels/shape as well as contrast; do not rely on color alone. Preserve accessible names, keyboard behavior, and natural text wrapping.
6. **Validate.** Run relevant existing tests/build/lint. When browser tooling is available, check ~1366, 800, 390 and 320px widths for overflow, focus, tap targets, dialogs and interactions. Respect `prefers-reduced-motion`. Do not claim visual or automated accessibility validation unless run.
7. **Report concisely** what was changed, what was tested, and what remains unverified.

## Visual invariants

- **Palette:** white surfaces, nearly black text/primary actions, neutral gray secondary text and lines. Do not add accent colors for decoration.
- **Geometry:** everyday buttons, form fields, filters, tags, and cards have square corners (`border-radius: 0`) and usually no shadow. A dialog may use a modest radius/shadow as an intentional layering exception.
- **Hierarchy:** use spacing, compact metadata, weight and 1px rules rather than gradients, glassmorphism, glows, floating decorations, oversized radii, or arbitrary animations.
- **Information architecture:** surface the main job-to-be-done quickly. Use a sidebar only where filters materially help; collapse to a clean, readable single column on mobile.
- **Content resilience:** long Korean or English titles, URLs and action labels must wrap rather than overflow; action groups may wrap or stack.
- **Adapt intelligently:** preserve product-specific requirements. When a user requests dark mode, colored status semantics, or an existing brand, adapt the tokens while keeping the structural principles. Do not reduce accessibility to satisfy a purely aesthetic rule.

## Reference files

- `references/DESIGN-SYSTEM.md` — design tokens, page geometry, component recipes, responsive and accessibility requirements.
- `assets/monochrome.css` — portable, `.mono-page`-scoped CSS, for reference or direct reuse.
- `assets/demo.html` — standalone interactive example (no external dependencies or network requests).
- `scripts/smoke_test.py` — dependency-free package checks (`python scripts/smoke_test.py`).
- `scripts/browser_check.py` — optional Playwright browser checks (`python scripts/browser_check.py`).

Do not introduce unnecessary libraries solely to reproduce this look. Do not present the demo as a full product, nor substitute sample content for real app data.
