# Research Decisions

This file records durable methodological, computational, and organizational
decisions whose rationale may otherwise be forgotten.

Do not record routine actions or temporary experiments.

---

## 2026-09-13 — Use a VS Code-centered research environment

### Decision

Use VS Code as the main operational research workspace.

Maintain separate sources of truth for:

- reproducible work in Git;
- conceptual notes in Obsidian;
- literature in Google Drive.

### Reason

The research workflow should not depend on the state or memory of a particular
AI chat application.

AI agents should be able to reconstruct the current project state from files.

---

## 2026-09-13 — Prefer textual Wolfram Language source for durable calculations

### Decision

Prefer `.wl` files for important reproducible Mathematica calculations while
retaining `.nb` notebooks where interactive exploration or visualization is
useful.

### Reason

Textual source files are easier to:

- version control;
- diff;
- edit with AI tools;
- execute automatically;
- review for reproducibility.