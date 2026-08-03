# UNIFIED_REGISTRY_STATUS_REPORT.md — R5 program status (registry-backed)

**Provenance — INHERITED FROZEN REFERENCE (not this repo's live campaign):**
The census and results below are the completed **predecessor** Star-Magic
R0–R5 Unified Registry Program (PAPER_2130): a 2,549-row constant-derivation
registry yielding the framework's 9-primitive → 73-derived-constant results.
These numbers are preserved verbatim as authoritative physics reference.

They do **NOT** describe this repository's paper-wiring campaign. This repo's
live campaign registry is `UNIFIED_REGISTRY.csv` (one row per wired PAPER_N);
its current wired/not-wired state is tracked in `WHITEPAPER_INDEX.md` and the
`CHANGELOG.md` / `SESSION_LOG.md` per-ship entries. Do not regenerate this file
from the campaign CSV — that would overwrite the physics results table.

## Registry census

| Metric | Value |
|---|:-:|
| registry_rows | 2549 |
| canonical_routes_explicit | 109 |
| canonical_routes_sole | 2440 |
| graph_edges | 658 |
| derived_constants_live | 73 |
| derived_constants_exact | 50 |
| independent_primitives | 9 |

### Rows by kind

- observable: 1392
- closure: 1129
- primitive: 16
- kernel_constant: 12

### Rows by status

- derived: 1129
- XGEO_ROUTED_IDENTITY: 1020
- OK: 249
- EXACT: 99
- XGEO_INDEPENDENT: 24
- locked: 16
- CLOSED_flagged_see_2026_05_28_verification: 12

### Phi-variant tags (PAPER_2129 sector rule)

- 0.84: 53
- 5/6: 63

### Graph edges by kind

- primitive->registry_row: 609
- primitive->constant: 35
- constant->route_paper: 14

## Program phases

| Phase | Deliverable | Status |
|---|---|:-:|
| R0 | UNIFIED_REGISTRY.csv (2,544 rows) + schema + citation graph + protected baselines | DONE |
| R1 | 109 explicit canonical routes + 2,435 sole-route auto-canonicalizations + 4 rulings | DONE |
| R2 | 199 registry-keyed corpus notes + pdf2 full parity (2,226 PDFs) | DONE |
| R3 | uqff_registry_primitives single source + 24-attribute rewire + Python=C++=Lean pins | DONE |
| R4 | UNIFIED_REGISTRY_GRAPH.csv (656 edges) + falsifiability report | DONE |
| R5 | This status backend + preprint results table + program landmark paper | DONE |
