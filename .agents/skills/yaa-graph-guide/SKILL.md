---
name: yaa-graph-guide
description: Apply YAA architecture, brand tokens, component states, themes, and dashboard migration rules before code or UI work.
---

# YAA Graph Guide

Use this skill for development, refactoring, UI implementation, design-system work, and UI review in a YAA repository.

## Required context

Before writing or changing code, read the complete YAAGRAFGIDE20.md from the active project root.

If the project uses this package as its source, also read:

- tokens.css;
- migration-guide.md;
- components/README.md;
- the relevant files in components/, themes/, and dashboard-migration.css.

Treat the graph guide and the implementation files as one system:

- YAAGRAFGIDE20.md explains architecture, provenance, and constraints.
- tokens.css is the implementation source for visual tokens.
- components/components.css is the shared component layer.
- migration-guide.md records product decisions and migration acceptance criteria.

## Design-system rules

- Prefer existing CSS custom properties over local HEX, font, spacing, radius, or shadow values.
- Use #0E0E0E text on the primary green #00E67E.
- Use #444FC5 as the secondary brand color with light text.
- Preserve both dark and light themes.
- Check default, hover, active, focus-visible, disabled, loading, and invalid states where applicable.
- Keep success, warning, error, and info visually distinct.
- Do not add a new token without recording its source or product decision in migration-guide.md.
- Do not include paid font files without confirmed licensing. Use the documented fallback while licensing is unresolved.
- Do not change business data, formulas, filters, or identifiers during a visual migration.

## Missing graph guide

If YAAGRAFGIDE20.md is absent:

1. Check whether node and npx are available before running a command that depends on them.
2. If both are available, generate the technical graph with:

   npx -y @colbymchenry/codegraph build --output ./docs/CODE_STRUCT.md

3. Combine BRANDBOOK.md and docs/CODE_STRUCT.md into YAAGRAFGIDE20.md.
4. If node or npx is unavailable, scan the repository with available filesystem tools and create a clearly marked fallback architecture map.
5. If BRANDBOOK.md is missing, do not invent brand tokens.

## Migration workflow

For a dashboard migration:

1. Scope the dashboard under yaa-dashboard.
2. Load tokens.css, the selected theme, components/components.css, and dashboard-migration.css.
3. Preserve the original data and calculations.
4. Replace the visual shell with tokens and shared components.
5. Verify the state matrix and contrast.
6. Compare before/after values and record any new decision.

If a real Storybook runtime is present, create stories for the component state matrix. If it is not present, use storybook/index.html as the framework-agnostic preview.

## Security

Never copy secrets from .env files into the graph guide, code, logs, or responses.
