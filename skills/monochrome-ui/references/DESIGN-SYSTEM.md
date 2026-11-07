# Monochrome UI design system

This reference describes a reusable, **light-mode-first**, high-contrast UI language for real web applications. It is a design specification, not a mandate to reproduce the demo's page structure verbatim. Prefer the target product's established component patterns and user workflows.

## Tokens

| Role | Default | Usage |
|---|---|---|
| Ink / primary | `#000000` | Main text, active controls, outlines |
| Hover emphasis | `#222222` | Primary-button hover |
| Muted text | `#555555` | Metadata, supportive copy, labels |
| Soft text | `#777777` | Non-essential hints (verify contrast) |
| Border | `#dedede` | Everyday separators, card outlines |
| Surface | `#ffffff` | Page, panels, fields, cards |
| Soft surface | `#f5f5f5` | Subtle hover and secondary toolbars |
| Focus | `#000000` | Visible focus outline (often 2px + offset) |

Use CSS custom properties or the host design-token mechanism. Avoid scattered opaque colors. Black/white are defaults, not a reason to erase meaningful semantic feedback such as errors; preserve recognizable labels, icons, and accessible announcements where needed.

**Typography:** `system-ui, -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif`; body `15px / 1.6`; main heading ~`27px` (mobile ~`23px`); panel heading ~`18px`; card heading `17px` (mobile `15px`); controls `12–13px`; metadata `11–12px`. Weight creates structure: headings around 750–800, labels/buttons around 700–800. Keep Korean text legible with `word-break: keep-all` where appropriate; allow breaking long URLs and controls when necessary.

**Surface rules:** 1px borders, no card shadows, no gradients, no ornamental illustrations by default. Everyday surface radius `0`; dialogs may intentionally use ~`8–12px` radius and a restrained shadow. Spacing should make dense data readable, not cramped. For touch controls target ~44px when practical.

## Page geometry (starting points, not fixed templates)

| Pattern | Desktop | Narrow |
|---|---|---|
| Shell | `min(1192px, calc(100% - 48px))` | `min(590px, calc(100% - 32px))` below 710px |
| Header | 80px high with bottom border | 70px below 710px |
| Content + filters | `264px minmax(0, 1fr)` with 26px gap | Single column below 710px |
| Intermediate widths | Sidebar 225px, 18px gap below 950px | — |
| Section top spacing | 34px | 22px below 710px |
| Search field | 58px tall | 54px below 710px |
| Result cards | `22px 23px` padding, 12px vertical gap | 17px padding below 710px |
| Filter panel | 23px padding | 18px, 2-column inner grid below 710px |

At ≤440px, stack results count/sort toolbar as needed. At ≤390px, permit action buttons to stretch or wrap and hide nonessential hints. Validate at 320px and with enlarged browser text. Never rely on a single viewport size.

## Component recipes

### Header
- One compact brand/section identity plus essential navigation/actions.
- Avoid redundant brand label + hero + repeating heading. Show the user what they came to accomplish.
- A condensed icon-only action requires an explicit accessible name and usable touch target.

### Filters
- Desktop: separate white panel with clear border, label-above-control, short reset action.
- Prefer segmented controls for 2–3 mutually exclusive categories and select menus for larger option sets.
- A selected item uses white text on black fill; nonselected uses black on white. Keep `aria-pressed`, `aria-selected`, checked state, etc. in sync as appropriate.
- Mobile: move filters above results, and let important segmented controls span the full filter width. Avoid long, awkward labels.

### Search, lists, dashboards
- Put a clear page heading, concise subtitle, then the main search/action where it is discoverable.
- Full-width search, simple 1px black border, icon if useful, visible focus-within state. Optional `/` shortcut only if actually implemented.
- Toolbar: result count prominent, sort/filter detail secondary; wrap without overlap.
- Card: small neutral metadata tags → strong title → concise optional summary → thin separator → context-specific actions. Hover can change border black without a shadow.
- For tables/dashboards, retain the same thin-rule and typographic hierarchy rather than forcing card layouts.
- Primary actions black on white or white on black. Place primary and secondary actions consistently.

### Loading, errors, empty states, dialogs
- Surface honest loading and failures in the same visual language, with distinct readable text and accessible status announcements when appropriate.
- A native `<dialog>` or accessible existing dialog library is preferred. Manage focus, keyboard Escape, modal close, and long headings. Modals are an intentional exception to zero-radius/zero-shadow if useful.
- Do not create nonfunctional navigation or placeholder action buttons in production UI.

## Accessibility and behavior checklist

- Semantic landmarks, accessible names, associated `<label>`s.
- Visible keyboard focus on interactive controls; no suppression of outlines without an equivalent.
- At least clear text/background contrast; check muted hints and disabled states against relevant WCAG thresholds.
- Keyboard interaction, Escape for modal, selected state reflected in ARIA, meaningful hover and active states.
- Text scaling, 320px width, wrapping Korean titles, narrow cards, long file names/URLs.
- Respect `prefers-reduced-motion: reduce`; no auto-flashing or decorative motion.
- Maintain the host app's error handling, data fetching, authentication, translations, and routing.

## Adapting to different stacks

- **Plain HTML/CSS:** start from `assets/monochrome.css` and `assets/demo.html`, then remove unused components. `.mono-page` scopes tokens and base styles; component classes use `mono-`.
- **React/Vue/Svelte:** convert recipes into existing reusable components; state drives selected/disabled ARIA and CSS. Do not copy imperative demo JavaScript.
- **Tailwind:** map tokens into existing theme and utility classes; avoid introducing a second CSS framework. Preserve semantic states and responsive breakpoints.
- **Established design system:** prefer reskinning existing components and tokens, not wholesale replacing their underlying behavior.

## Anti-patterns

Avoid giant introductory banners, random accent colors, unneeded animations, rounded cards with stacked shadows, fake glass effects, monochrome-only status indicators, clipping text, invisible keyboard focus, inaccessible icon-only controls, and copying the demo's content or feature set into unrelated products.
