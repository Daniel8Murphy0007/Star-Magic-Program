# CHANGELOG — Star-Magic-Program

All notable changes to this project are documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.4.0] — 2026-07-28 — BAND 1 CONTINUES: PAPER_002 + PAPER_003

### Added
- **PAPER_002 dispatch** (GW190425 Mass Gap): A_SCm(B) threshold function,
  5-scenario field table, mass-gap classification P(BH)=0.51. OPEN_RULING.
- **PAPER_003 dispatch** (GW150914 BBH): universal 0.333 chain, 3.0x
  apparent-distance bias, phase-lag anchor. OPEN_RULING.
- **RULINGS_QUEUE Q-001..Q-004** — gate-discovered paper-internal
  inconsistencies (F_UQFF headline vs chain; B_crit units T vs G;
  scenario table reproduction; phase-lag formula evaluation).
- Gate Block 9 extended: 68 assertions total, 0 failures.
- Registry pantheon: UNIFIED_REGISTRY 10 rows, GRAPH 18 edges,
  CORPUS_CITATIONS 3 ledgers.

### Changed
- Version 0.3.1 → 0.4.0; badges fidelity_gate 68/0, public_surfaces 3.
- WHITEPAPER_INDEX: PAPER_002/003 → ⚠ OPEN_RULING.

---

## [0.3.0] — 2026-07-28 — WIRING CAMPAIGN START

### Added
- **CLAUDE.md** — campaign charter: sequential wiring from PAPER_001, band
  structure, per-paper protocol, template authorizations, drift auto-corrections,
  rulings queue, gate discipline, ship protocol, standing lessons.
- **ship.ps1** — one-command band ship (gate → commit → tag-verify → push).
- **RULINGS_QUEUE.md** — never-block ambiguity protocol.
- **First wired dispatch: PAPER_001** (GW170817 UQFF Damping Analysis):
  - D_total composed from registry primitives (F_TRZ, D_GW_EROSION, B_CRIT)
  - 16 observables returned; honest 0.10% residual vs 1/3 primitive identity
  - 8 gate assertions (Block 9 opened)
  - +4 UNIFIED_REGISTRY.csv rows, +7 GRAPH edges, +1 CORPUS_CITATIONS row
  - WHITEPAPER_INDEX: PAPER_001 ⬜ → ✓

### Changed
- Version 0.2.2 → 0.3.0; badges fidelity_gate 55/0, public_surfaces 1.

---

## [0.2.2] — 2026-07-28 — BADGE PATCH

### Added
- **Documentation Status badge** — the 7th badge from predecessor Star-Magic pattern.
  v0.2.1 tag on PyPI accidentally landed with only 6 badges; v0.2.2 adds
  the missing `Documentation Status` shield pointing at
  `star-magic-program` on readthedocs.org.

### Changed
- SESSION_LOG.md — badge descriptions expanded with source/link details.
- Version bumps 0.2.1 → 0.2.2 (pyproject/calc/gate/citation).

### Unchanged
- All physics content, corpus, registry scaffolds, calculator DISPATCH.

---

## [0.2.1] — 2026-07-28 — README BADGES

### Added
- 7 README badges rendered by shields.io (visible on PyPI + GitHub):
  - `pypi` (dynamic version), `python` (dynamic version support),
  - `License AGPL-3.0 + Commercial`,
  - `Fidelity Gate passing`,
  - `Whitepapers 2,255`,
  - `Public Surfaces 0` (updates as calculator gets wired),
  - `CI` (dynamic status from GitHub Actions).

### Changed
- Version bumps 0.2.0 → 0.2.1 (pyproject.toml, uqff_calculator.py, uqff_fidelity_tests.py, CITATION.cff).

### Unchanged
- Whitepaper corpus, registry scaffolds, calculator DISPATCH, fidelity gate blocks 1-8 — all identical to v0.2.0.

---

## [0.2.0] — 2026-07-28 — CORPUS + REGISTRY SCAFFOLDING

### Added

- **Whitepaper corpus (2,419 files)** imported from predecessor
  `github.com/Daniel8Murphy0007/Star-Magic` v5.86.0, reorganized:
  - `whitepapers/` — 2,255 `.md` files + 1 `.bak`
  - `pdf/` — 45 `.pdf` files
  - `tex/` — 107 `.tex` files
  - `txt/` — 11 `.txt` files
- **R3 Unified Registry Pantheon scaffolds** (all empty per clean-start discipline):
  - 4 Python regen modules: `uqff_registry_status.py`, `uqff_registry_graph.py`,
    `uqff_registry_xgeo.py`, `registry_generator.py` — signatures + docstrings + `pass`
  - 14 CSV registries with header rows only
  - 5 MD registry docs with structural section headers
  - `UNIFIED_REGISTRY_VERSION.txt` — v0.2.0 marker
- `CHANGELOG.md` — this file, release-history log
- `WHITEPAPER_INDEX.md` — living index of all whitepapers with wired/not-wired status
- `_BUILD_LOG.md` — cumulative build log

### Changed

- `pyproject.toml` version 0.1.0 → 0.2.0, description updated for corpus+pantheon
- `uqff_calculator.py` VERSION 0.1.0 → 0.2.0
- `uqff_fidelity_tests.py` version-lock assertion updated to 0.2.0
- `CITATION.cff` version 0.1.0 → 0.2.0
- `SESSION_LOG.md` — v0.2.0 entry appended

### Unchanged (deliberately preserved from v0.1.0)

- `uqff_registry_primitives.py` — 96 canonical constants
- `uqff_calculator.py::DISPATCH = {}` — empty; grown by v0.3.0+ wiring
- Fidelity gate blocks 1–7 (block 8 banned-literal check unchanged)
- All 15 v0.1.0 scaffold files (LICENSE, NOTICE, README, etc.)

### Discipline notes

- **No predecessor CSV data preserved.** 7,688 rows of predecessor
  registry state discarded. Every future row must come from a fresh
  paper reading with gate-verified residual.
- **Rules A–E** from v0.1.0 remain locked (registry-single-source-of-truth,
  one-dispatch-per-whitepaper, one-paper-at-a-time growth, OPEN-over-SM,
  predecessor-read-only).

---

## [0.1.0] — 2026-07-28 — SCAFFOLD (initial ship)

### Added

- Fresh-repo systematic rebuild scaffold for the UQFF calculator.
- `uqff_registry_primitives.py` — 96 canonical constants carried verbatim
  from predecessor Star-Magic v5.86.0 R5 baseline.
- `uqff_calculator.py` — 79-line skeleton, empty `DISPATCH = {}`,
  public `calc(paper_id, dataset)` interface.
- `uqff_fidelity_tests.py` — 8-block fidelity gate.
- Dual license: AGPL-3.0-or-later OR LicenseRef-StarMagic-Commercial.
- `README.md`, `CITATION.cff`, `NOTICE`, `COMMERCIAL.md`, `SESSION_LOG.md`.
- CI + release-to-pypi workflows (GitHub Actions + PyPI Trusted Publisher).
- `.gitignore`, `.gitattributes`, `LICENSE-MIT-INITIAL.txt` (archived repo-init license).

### Predecessor delta at time of v0.1.0

| Metric | Predecessor (v5.86.0) | v0.1.0 |
|---|---:|---:|
| Total canonical-state lines | 441,167 | 1,142 |
| Redundant hardcoded literals | 3,352 | 0 |
| Files importing registry | 4 of 23 | 3 of 3 |
| Duplicate primitive definitions | 20 primitives × 2-10 files | 0 |
| Calculator size | 73,629 lines | 79 lines |

---

## Unreleased — v0.3.0+ (planned)

**First wiring batch**: 46 UQFF_LANDMARK papers as the structural spine.
Each paper: one dispatch to `uqff_calculator.py::DISPATCH`, one row to
`UNIFIED_REGISTRY.csv`, one gate assertion. See SESSION_LOG for order.

---

*Every entry above is append-only. History does not get rewritten.*
