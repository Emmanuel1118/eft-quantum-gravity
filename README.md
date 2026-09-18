# eft-quantum-gravity

M.Sc. research repository for calculations and computational tools related to
the effective-field-theory treatment of quantum gravity.

The VS Code workspace contains this repository and the separate Obsidian vault.
The literature library remains in Google Drive and is accessed through URLs
using the authenticated Drive connection, with read-only treatment by default.
The streamed Drive folder was removed from the workspace because it caused
Windows sandbox initialization failures.

See [research state](context/current_state.md) for setup status and
[decisions](context/decisions.md) for the access rationale. Machine-specific
paths and library URLs are recorded in the untracked `context/local_environment.md`.

For literature work, see [paper reading and catalog workflow](context/paper_workflow.md).
Start with relevant vault notes; open source pages when evidence is missing or
exact verification is needed. For new records, use
[metadata-first paper registration](context/paper_registration.md).
The native Research Paper Index in Drive holds the bibliography and reading
status. PDF extraction/rendering utilities live in `scripts/`; selected source
caches and generated outputs stay under ignored `output/`.
