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

## EQUATION-LIBRARY REWIRE (working, not shipped) — PAPER_001-003 full-capture
- Architecture: equation-library layer beneath paper dispatches; every equation an individually-callable, primitive-sourced function; papers are compositions.
- PAPER_001: 35 fields (all 40 equations). PAPER_002: 55 fields (all sections incl. YM BCS, Production Framework, VDS/DVP/BSH). PAPER_003: 45 fields (9-sector Lagrangian, Cosmogenesis, VDS/DVP/BSH).
- Drift corrections gate-pinned: VDS 1.894->F_TRZ (PAPER_2156), rho_vac->LAMBDA_VAC (PAPER_2155), beta_i->BETA_I.
- Full linked-whitepaper maps recorded (54/37/32). Gate 2047/0. NOT SHIPPED until 300+ papers rewired.

---

## 2026-08-04 — COMPLETE-COMPILE campaign status (PAPER_001-015 + b-variants)

**Papers at complete-compile depth:** PAPER_001-015 base + 008b, 009b, 010b, 011b, 012b, 013b, 014b (22 dispatches).
Each invokes the full equation library: core physics + Session-225 phonon upgrades + Production Framework +
Cosmogenesis-Linked Lagrangian (L_cosmo + V_phi_NS + Euler-Lagrange EOM) + VDS/DVP/BSH synthesis +
Kozima-LENR appendix K.1-K.6. 51-85 fields per paper.

**Equation library:** 408 named, individually-callable, primitive-sourced functions. Shared appendix blocks
factored into `_common_uqff_blocks()` (defined once, reused by every GW paper — guarantees no section is dropped).

**Calculator integrity:** 342 registrations, 0 duplicate @_register keys, 18,222 lines. (A backward-slice bug
that duplicated 276 papers was detected and fully reverted via PRE_FULLEQ_BACKUP + safe forward-boundary re-apply.)

**Fidelity gate:** green. Complete-compile verification loop asserts Kozima K.1-K.6 + cosmogenesis EOM + VDS=F_TRZ +
DVP primes + BSH saturation + >=30 shared equations for each of PAPER_001-015.

**Registry (R0 master + derived pantheon):** UNIFIED_REGISTRY.csv (R0, 733 rows), GRAPH (1916 edges),
CORPUS_CITATIONS, R1_QUEUE, R2_MAPPING (24 sectors), R3_LEDGER, RESULTS_TABLE, MERGED, GAPS, DUPLICATES,
FALSIFIABILITY — all advanced through PAPER_015. 0 malformed CSVs.

**NOT SHIPPED** — holding per the 300+ paper mandate. Working version 0.337.0.

*(Windows-side save 2026-08-04 to trigger VS Code file-watcher refresh.)*

## 2026-08-04 (cont.) — batch PAPER_015b-023 complete-compile
Papers at complete-compile depth now: PAPER_001-023 + b-variants (32 dispatches). 13 new paper-specific library
equations (entanglement/redshift/aether-noise/PTA/cosmic-ray/lensing/string-compactification/tau-g2). Registry R0
745 rows, 31 R2 sectors. 342 dispatches, 0 duplicates. Gate green. NOT SHIPPED (300+ mandate).

## 2026-08-05 — batch PAPER_071-080 complete-compile (v0.342.0)
Papers at complete-compile depth: PAPER_001-080 + b-variants. 470-fn equation library. 342 dispatches, 0 duplicates.
Registry R0 823 rows; XGEO queue 154 / confirmations 70; linked-paper mapping through PAPER_080. Gate green (2116 assertions).


---

## LIVE CAMPAIGN STATUS — v0.345.0 (this repo, distinct from frozen reference above)

- Equation library: **2112 total Python functions**, **1767 named callable** (494 equation-library + 1,272 dc_ derived-equation).
- Dispatches: 342 (PAPER_001-080). Registry: **2502 rows**, 0 malformed.
- Linked-paper mapping: GRAPH **3330 edges**, CORPUS_CITATIONS **732 papers** mapped.
- Fidelity gate: **2159 assertions**, green. NO-DUPLICATE-DEF guard active. Rule E / Rule 4 / Rule 7 held.


## LIVE STATUS UPDATE v0.346.0
- 2130 total functions | 1784 named callable | registry 2520 rows | gate 2159 green. Mining mapped in-step (GRAPH+citations).


## LIVE STATUS UPDATE v0.347.0
- LANDMARK-IDENTITY COMPILE: ~40 landmark fns, ~30 gate guards. 2,212 total fns | 1,866 named | registry 2,602 rows | gate 2,189 green.


## LIVE STATUS UPDATE v0.348.0
- LANDMARK COMPILE II complete: landmark family drained (~70/83 papers, 9 rounds). 2,232 fns | 1,886 named | registry 2,622 rows | gate 2,206 green. 2 rulings queued (Q-2118, Q-1412).


## LIVE STATUS UPDATE v0.349.0
- DEEP-MINE COMPILE: +318 generated fns (bb/ml/pi) + formula availability. 2,565 total | 2,219 named | registry 2,950 rows | gate 2,236 green.


## LIVE STATUS UPDATE v0.350.0
- PREDECESSOR-SOURCE SWEEP complete (2,851 classes + modules). 2,662 fns | 2,316 named | 7 modules | registry 3,041 | GRAPH 4,139 | gate 2,264. 3 rulings queued.


## LIVE STATUS v0.351.0 - PREDECESSOR SCRAPE COMPLETE
- 2,756 fns | 2,410 named | 8 modules | registry 3,133 | GRAPH 4,475 | gate 2,277. All sources exhausted. 4 rulings queued.


## LIVE STATUS v0.352.0
- CoAnQi mined + frontier PAPER_110. 2,793 fns | 2,447 named | registry 3,170 | GRAPH 4,544 | gate 2,299. New future-target: 0.755 decomposition.


## LIVE STATUS v0.353.0
- Frontier PAPER_150. 2,830 fns | 2,484 named | registry 3,207 | GRAPH 4,598 | gate 2,318. kappa dual-route closed.


## LIVE STATUS v0.355.0
- RULE 7 REVISED + full-census 001-170 (36 recoveries + 6 implied captures). 2,888 fns | 2,542 named | registry 3,264 | GRAPH 4,667 | gate 2,346. Frontier 170.
