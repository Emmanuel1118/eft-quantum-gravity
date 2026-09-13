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

---

## 2026-09-13 — Access literature through Google Drive URLs

### Decision

Keep only the research repository and Obsidian vault in the VS Code workspace.
Access the separate literature library through folder/file URLs using the
authenticated Google Drive connection. Treat the library as read-only by
project policy. Store its access URLs in `context/local_environment.md`.

### Reason

With the streamed Drive folder in the workspace, the IDE passed it as a writable
sandbox root. Applying permissions failed with `SetNamedSecurityInfoW` error 87
and prevented ordinary commands from starting. Selecting the `research` profile
alone did not resolve that behavior. Removing the folder restored ordinary
sandbox execution and local repository/Obsidian reads.

The dedicated sandbox account still cannot read the streamed G: mount. URL-based
access through the authenticated connection successfully listed the library and
read text from a research PDF on 2026-09-13. This provides a working literature
route without Drive ACL changes, reduced sandbox isolation, or a duplicate paper
library. It depends on the authenticated connection and does not establish local
filesystem access. Sandbox write-boundary verification is a separate check;
the ordinary-tool completion results are recorded in `context/current_state.md`.
