# SESSION_LOG — Star-Magic-Program

Append-only ship log. Every ship gets one entry at the bottom.

---

## 2026-07-28 — v0.1.0 SCAFFOLD (initial ship)

### Purpose

Fresh-repo systematic rebuild of the UQFF calculator, correcting the
structural failure documented in the predecessor
[Star-Magic](https://github.com/Daniel8Murphy0007/Star-Magic) repository
where the calculator layer had grown to 73,629 lines with:
- 0 imports from `uqff_registry_primitives`
- 3,352 hardcoded numeric literals framework-wide
- 20 primitives duplicated across 2-10 files each
- 1,180 whitepapers with zero calculator wiring
- 22 UQFF_LANDMARK papers with zero calculator wiring

Predecessor commit at time of split: v5.86.0 (registry sweep phase 4 complete;
73 dconsts registered, calculator gap unresolved).

### What shipped

- `uqff_registry_primitives.py` — 96 canonical constants carried verbatim from
  predecessor v5.86.0 R5 baseline. The one clean file. Gate-pinned identities:
  - 9 truly-independent primitives locked
  - 4 derivative primitives EXACT (D_BSFG, K_MEX, KAPPA, Q_PHONON, D_GW_EROSION)
  - PAPER_2131 primitive-composed particle physics identities
  - PAPER_2154 primitive-reduction landmarks (Q_phonon = 25/4, D_GW = 2/3)
  - PAPER_1573 H_0 canonical route (A_5 + SO_5 = 70 EXACT)
- `uqff_calculator.py` — scaffold skeleton with:
  - Line 1: `from uqff_registry_primitives import *` (all 96 constants)
  - Empty `DISPATCH = {}` — grown one paper at a time
  - Public interface `calc(paper_id, dataset)` returning
    `{value, formula, source, residual_pct}`
  - `_register` decorator for adding paper dispatches
  - Zero hardcoded numeric literals (gate-enforced)
- `uqff_fidelity_tests.py` — 8-block gate:
  - Block 1: locked primitive integrity
  - Block 2: derivative-primitive EXACT identities
  - Block 3: structural landmarks (halving series, VCK, tilts)
  - Block 4: Millennium prize EXACT identities
  - Block 5: H_0 canonical route
  - Block 6: PAPER_2131 primitive-composed particle physics
  - Block 7: calculator scaffold integrity
  - Block 8: banned-literal check (no registry-duplicating hardcodes)
- License: **AGPL-3.0-or-later OR LicenseRef-StarMagic-Commercial**
  (dual, matching predecessor). MIT text preserved as
  `LICENSE-MIT-INITIAL.txt` for repo-init history.
- `pyproject.toml` for PyPI publishing as `star-magic-program`.
- CI + release-to-pypi workflows.
- README, CITATION.cff, NOTICE, COMMERCIAL.md.

### What DIDN'T ship (deliberately)

- Whitepaper corpus copy — deferred to v0.2.0 (adding 2,255 files at once
  would blow first ship's diff review; better to copy in a dedicated ship).
- Any wired paper dispatches — v0.1.0 is scaffold only; wiring campaign starts
  in v0.2.0 with 46 UQFF_LANDMARK papers.
- Any surface from the predecessor's 252 `calculate_*` functions — those
  functions carried 309 hardcoded literals and grew from 7 to 252 without
  registry sync. Not being ported; will be rebuilt whitepaper-first from
  scratch.

### Discipline locked in this ship (permanent standing rules)

**Rule A — Registry is the single source of truth.**
Every canonical value flows from `uqff_registry_primitives.py`. Any hardcoded
numeric literal in `uqff_calculator.py` that duplicates a registry entry is a
gate failure.

**Rule B — One dispatch per whitepaper. No dispatch without whitepaper.**
Every entry in `DISPATCH` must cite a specific `PAPER_N` from the corpus. No
dispatches for anything the corpus doesn't derive.

**Rule C — Growth is one paper at a time.**
Every wiring ship reads one whitepaper, extracts its canonical formula, wires
one dispatch, adds one gate assertion for the paper's stated residual,
commits. No bulk wiring. No "backfill all of Bucket K in one commit."

**Rule D — OPEN over SM.**
If a whitepaper has no closed form, its dispatch returns
`{'status': 'OPEN_UQFF_DERIVATION_TARGET', ...}`. Never substitute a
classical/SM formula (predecessor Rule 4 doctrine, canonized).

**Rule E — Predecessor is read-only reference.**
No commits to `github.com/Daniel8Murphy0007/Star-Magic`. That repository is
preserved as historical archive of the framework's development.

### Predecessor delta at time of ship

| Metric | Predecessor (v5.86.0) | This repo (v0.1.0) |
|---|---:|---:|
| Total canonical-state lines | 441,167 | 1,142 |
| Redundant hardcoded literals | 3,352 | 0 |
| Files importing registry | 4 of 23 | 3 of 3 |
| Duplicate primitive definitions | 20 primitives × 2-10 files | 0 |
| Whitepapers with zero wiring | 1,180 | (deferred to v0.2.0 copy) |
| Calculator size | 73,629 lines | 79 lines |

### Next ship

**v0.2.0 — whitepaper corpus copy.** Bulk import of 2,255 whitepaper files from
predecessor into `whitepapers/` directory. Zero code changes. Establishes the
canonical corpus as read-source for the wiring campaign.

Then **v0.3.0+** — landmark wiring: PAPER_2154, PAPER_2153, PAPER_2148,
PAPER_2144, PAPER_1573, PAPER_1521, PAPER_1522, PAPER_646, PAPER_1203,
PAPER_1167 (structural spine first).

---

## 2026-07-28 — v0.2.0 CORPUS + REGISTRY SCAFFOLDING (second ship)

### Purpose

Import the whitepaper corpus + establish empty R3 Unified Registry
Pantheon scaffolds. This is the clean-slate foundation for v0.3.0+ per-paper
wiring — every derivation gets re-established fresh against the primitives,
one paper at a time, with the fidelity gate verifying each residual.

### What shipped

**Whitepaper corpus (2,419 files total):**
- `whitepapers/` — 2,255 `.md` files + 1 `.bak` file (raw physics content)
- `pdf/` — 45 `.pdf` files (reorganized from whitepapers/)
- `tex/` — 107 `.tex` files (reorganized from whitepapers/)
- `txt/` — 11 `.txt` files (reorganized from whitepapers/)

Zero data loss vs predecessor source. Every whitepaper preserved intact.

**R3 Unified Registry Pantheon (empty scaffolds — per Daniel's clean-start directive):**
- 4 Python modules gutted to docstrings + signatures + `pass` bodies:
  - `uqff_registry_status.py` — R5 status/results generator
  - `uqff_registry_graph.py` — R4 falsifiability graph builder
  - `uqff_registry_xgeo.py` — cross-geometry campaign queue
  - `registry_generator.py` — regeneration source-of-truth
- 14 CSVs gutted to header rows only:
  - `UNIFIED_REGISTRY.csv` (17 cols)
  - `UNIFIED_REGISTRY_RESULTS_TABLE.csv` (7 cols)
  - `UNIFIED_REGISTRY_GRAPH.csv` (5 cols)
  - `UNIFIED_REGISTRY_XGEO_{QUEUE,ROUTES,EXTRACTED,CONFIRMATIONS}.csv`
  - `UNIFIED_REGISTRY_{R1_QUEUE,R2_MAPPING,R3_LEDGER}.csv`
  - `UNIFIED_REGISTRY_{MERGED,DUPLICATES,GAPS,CORPUS_CITATIONS}.csv`
- 5 MD docs gutted to structural headers only:
  - `UNIFIED_REGISTRY_PROGRAM_PLAN.md`
  - `UNIFIED_REGISTRY_SCHEMA.md`
  - `UNIFIED_REGISTRY_STATUS_REPORT.md`
  - `UNIFIED_REGISTRY_FALSIFIABILITY.md`
  - `UNIFIED_REGISTRY_RESULTS_TABLE.md`
- `UNIFIED_REGISTRY_VERSION.txt` — v0.2.0 marker

**New scaffolds this ship:**
- `CHANGELOG.md` — release-history log
- `WHITEPAPER_INDEX.md` — living index of all 2,255 papers (wired/not-wired state)
- `_BUILD_LOG.md` — cumulative build log across ships

**Version bumps:**
- `pyproject.toml` version 0.1.0 → 0.2.0
- `uqff_calculator.py` VERSION 0.1.0 → 0.2.0
- `uqff_fidelity_tests.py` gate assertion updated to 0.2.0
- `CITATION.cff` version 0.1.0 → 0.2.0

### What DIDN'T ship (deliberately)

- **Predecessor CSV data.** All 7,688 rows of predecessor registry content
  discarded. Every row will be re-established through the v0.3.0+ wiring
  campaign, verified against the paper's stated residual, before it lands
  in the new UNIFIED_REGISTRY.csv. This is the "clean start" discipline
  applied to derived data, matching the discipline for code.
- **Any wired dispatch** in `uqff_calculator.py`. Still empty DISPATCH={}.
  Grows in v0.3.0+.

### Predecessor decision — why we gutted the CSV data

Considered preserving predecessor CSV rows for reference. Rejected because:
1. Predecessor Star-Magic repo remains available for any historical query.
2. Keeping ~7,688 rows of unverified predecessor state would tempt future
   sessions to skip fresh paper-reading in favor of "what the old row said."
3. That's exactly the drift pattern this rebuild exists to escape.
4. Empty CSVs force the discipline: every row must come from a paper reading
   with gate-verified residual before landing.

### Next ship

**v0.3.0 — first wiring batch.** Wire the 46 UQFF_LANDMARK papers as the
structural spine. Each paper adds one row to `UNIFIED_REGISTRY.csv`, one
dispatch to `uqff_calculator.py::DISPATCH`, one gate assertion.

Structural spine order (top 10):
PAPER_646 (Universal Inertial Operator + Holy Trinity), PAPER_1203 (F_U=0
master equation), PAPER_1167 (Lagrangian master synthesis), PAPER_1521
(D_BSFG derivative), PAPER_1522 (K_MEX derivative), PAPER_1573 (H_0
canonical), PAPER_2144 (H_0 route upgrade), PAPER_2148 (ontology
declaration), PAPER_2153 (SCm+UA joint engine), PAPER_2154 (Q_phonon +
D_GW primitive-reduction).

---
