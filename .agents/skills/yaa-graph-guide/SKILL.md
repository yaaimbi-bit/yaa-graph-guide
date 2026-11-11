---
name: yaa-graph-guide
description: Read the project's YAAGRAFGIDE20.md before code or UI work and maintain its brand and architecture constraints.
---

# YAA Graph Guide

Use this skill for development, refactoring, UI implementation, and UI review in a YAA repository that contains `YAAGRAFGIDE20.md`.

## Source of truth

Before writing or changing code, read the complete `./YAAGRAFGIDE20.md` from the active project root. Treat it as the combined source of truth for:

- brand colors, typography, spacing, components, and visual restrictions;
- repository structure, modules, dependencies, and architecture flows.

Do not rely on memory or on a partial read of `BRANDBOOK.md` or the codebase when the graph guide is present.

## Missing graph guide

If `./YAAGRAFGIDE20.md` is absent:

1. Check whether `node` and `npx` are available before running any terminal command that depends on them.
2. If both are available, generate the technical graph with:

   ```sh
   npx -y @colbymchenry/codegraph build --output ./docs/CODE_STRUCT.md
   ```

3. Combine `./BRANDBOOK.md` and `./docs/CODE_STRUCT.md` into `./YAAGRAFGIDE20.md`, preserving both sources and separating them with a Markdown divider.
4. If `node` or `npx` is unavailable, do not report a failed build as the result. Use available filesystem-reading tools to scan the repository directly, create a text map of folders, source files, key modules, and detectable imports, then combine that map with `BRANDBOOK.md` into `YAAGRAFGIDE20.md`.

If `BRANDBOOK.md` is missing, do not invent brand tokens. Report the missing source and keep any generated architecture map clearly marked as incomplete.

## Applying the guide

- Prefer existing tokens from `YAAGRAFGIDE20.md`; do not introduce unapproved colors or fonts as if they were brand defaults.
- If a user explicitly requests a non-brand value, identify it as an intentional exception and isolate it from global tokens.
- For UI review, check the implementation against the brand section and distinguish exact PDF values from visual interpretations and unspecified values.
- For code changes, follow the module boundaries and dependency relationships described in the architecture section.
- Do not copy secrets from `.env` files into the guide, code, logs, or responses.
