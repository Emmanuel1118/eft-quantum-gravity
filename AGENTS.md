# AI Agent Instructions

## Project

This repository contains computational and reproducible work for an M.Sc.
research project on effective-field-theory approaches to quantum gravity.

The VS Code workspace contains this repository and an Obsidian vault containing
conceptual research notes. Research papers and reference material remain in
Google Drive, accessed through folder/file URLs using the authenticated Google
Drive connection. The streamed Drive folder is not a VS Code workspace root.

These are separate sources of truth and should not be duplicated into this repository.

## Before substantial work

1. Read `context/current_state.md`.
2. Read `context/research_overview.md` when broader scientific context is needed.
3. Inspect relevant existing calculations before creating new ones.
4. Consult relevant notes in the Obsidian vault.
5. Consult relevant papers when the task depends on the literature.

Do not assume that chat history is authoritative if it conflicts with project files.

## Repository responsibilities

Use this repository for:

- reproducible calculations;
- Mathematica / Wolfram Language source;
- Python calculations and utilities;
- tests;
- scripts;
- research-state tracking;
- methodological decisions.

Do not copy the research-paper library or entire Obsidian vault into this repository.

## Mathematica

Prefer textual `.wl` source files for reproducible calculations.

Interactive `.nb` notebooks may be used when appropriate for exploration or
visualization, but important reusable calculations should eventually have a
textual source representation.

Place Wolfram Language calculations under:

`calculations/mathematica/`

Do not overwrite a working calculation merely to reorganize it.

## Python

Place scientific Python calculations under:

`calculations/python/`

Supporting utilities belong under:

`scripts/`

Tests belong under:

`tests/`

## Obsidian vault

The Obsidian vault contains conceptual scientific knowledge and research notes.

Agents may read relevant notes freely.

Agents may edit or create notes when explicitly required by the task.

Do not:

- delete notes;
- rename notes;
- move notes;
- reorganize folders;
- rewrite large groups of notes;

unless explicitly instructed.

Preserve Obsidian links and existing Markdown conventions.

## Research paper library

Treat the Google Drive research-paper directory as READ-ONLY by default.

Use the library URL in `context/local_environment.md` through the Google Drive
connection for discovery and reading. Do not depend on sandbox access to the
local `G:` mount. Including that mount as a workspace root caused Windows
sandbox initialization to fail; URL access has been verified separately.

Agents may:

- search it;
- read papers;
- identify relevant literature;
- cite papers in notes and research output.

Do not rename, move, delete, or reorganize papers unless explicitly instructed.

## Research state

After substantial research work, update:

`context/current_state.md`

when the active understanding, open questions, or next step has changed.

Record durable methodological or organizational choices in:

`context/decisions.md`

Do not fill these files with session transcripts. Keep them concise and useful
to a future researcher or AI agent.

## Outputs

Generated temporary output belongs under:

`output/`

Do not treat generated output as authoritative when the calculation that
produced it is available.

## General working principle

Chats are for discussion.

Files are the durable source of truth.

If `context/local_environment.md` exists, read it to determine the
machine-specific locations of external research resources.
