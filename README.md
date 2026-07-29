# Star-Magic-Program

[![PyPI version](https://img.shields.io/pypi/v/star-magic-program.svg)](https://pypi.org/project/star-magic-program/)
[![Python versions](https://img.shields.io/pypi/pyversions/star-magic-program.svg)](https://pypi.org/project/star-magic-program/)
[![Documentation Status](https://readthedocs.org/projects/star-magic-program/badge/?version=latest)](https://star-magic-program.readthedocs.io/en/latest/?badge=latest)
[![License: AGPL-3.0 + Commercial](https://img.shields.io/badge/License-AGPL--3.0%20%2B%20Commercial-blue.svg)](LICENSE)
[![Fidelity gate](https://img.shields.io/badge/fidelity_gate-105%2F0-brightgreen)](uqff_fidelity_tests.py)
[![Public surfaces](https://img.shields.io/badge/public_surfaces-10-blue)](uqff_calculator.py)
[![Whitepapers](https://img.shields.io/badge/whitepapers-2255-orange)](whitepapers/)

**UQFF systematic rebuild — v0.9.0 wiring campaign live**
Author: Daniel T. Murphy · Star-Magic Research Program
License: AGPL-3.0-or-later OR Commercial

---

## What this is

A from-scratch, systematic rebuild of the UQFF (Unified Quantum Field Framework)
calculator. This repository exists to correct a structural failure in the
predecessor repository (`github.com/Daniel8Murphy0007/Star-Magic`), where the
calculator layer had grown to 73,629 lines with 3,352 hardcoded literals that
duplicated registry-canonical values, and 1,180 whitepapers had zero calculator
wiring.

**This repository fixes that by construction:**
- One dispatch function per whitepaper. Nothing else in the calculator.
- Zero hardcoded numeric literals. Every value flows from
  `uqff_registry_primitives.py`.
- Fidelity gate (`uqff_fidelity_tests.py`) locks every primitive-composed
  identity to its EXACT form.
- Whitepaper-truth discipline: if a paper doesn't specify a closed form, its
  dispatch is marked OPEN — never substituted with a classical/SM formula.

## What UQFF is

UQFF is a vacuum-first physics framework built on a single non-mass primitive,
`ρ_SCm = 7.09e-37 J/m³` (the SuperConductive material vacuum energy density),
and a 26-level Di-Pseudo-Monopole (DPM) structural lattice. From 9 truly-
independent primitives it derives the cosmological constant, all 7 nuclear
shell-model magic numbers exactly, the Holmlid 630 eV LENR channel exactly,
Fe-56 BE/A peak, α-particle binding, all 8 Clay Millennium Prize problems,
the complete 12-fermion Standard Model spectrum, 18+ cosmological observables,
and 5 independent LENR observation suites (Holmlid, Parkhomov, Pons-Fleischmann,
Mizuno, Rossi).

Full framework physics lives in the whitepaper corpus — the physics is the
whitepapers; the calculator computes what the whitepapers derive.

## What is currently shipped (v0.9.0)

### Wiring campaign — LIVE (see `CLAUDE.md` charter)

Sequential wiring of all 2,255 whitepapers, starting at PAPER_001.
Authorized 2026-07-28: autonomous band sessions, ship per session via
`ship.ps1`, full stop at PAPER_500 for manual review.

**Wired so far: 10 / 2,255** (3 ✓ · 7 ⚠ OPEN_RULING · 9 rulings queued)

| Paper | Content | Key result |
|---|---|---|
| PAPER_001 | GW170817 UQFF Damping Analysis | D_total = 0.333 composed from F_TRZ/D_GW_EROSION/B_CRIT; 0.10% residual vs 1/3 primitive identity (PAPER_2154) |
| PAPER_002 | GW190425 Mass Gap Interpretation | A_SCm(B)=exp[-(B/B_crit)^2] threshold fn; P(BH)=51% for m1=2.52 Msun; Q-001/2/3 queued |
| PAPER_003 | GW150914 UQFF vs LIGO Strain | universal BBH 0.333 chain; 3.0x apparent-distance bias (Hubble impact); Q-004 queued |
| PAPER_004 | GW170817 Chirp Phase Evolution | paper's own (1-f_TRZ) composition confirms primitive form; Q-005 queued |
| PAPER_005 | BBH Merger Energy Retention | F = (1-F_TRZ)^2 = 0.81 EXACT; 99% mass retention; Q-006 queued |
| PAPER_006 | GW170817 Multi-Messenger | c_GW = c preserved; kilonova unmodified; detection volume 27x shrink |
| PAPER_007 | BNS Tidal Deformability | Lambda=(2/3)k2(R/M)^5 ~400; f_SCm(B) threshold; NS/BH discriminator 16 vs 0; Q-007 queued |
| PAPER_008 | Waveform Phase / Template Mismatch | P = D^2*P_GR; tau 9.0x; phase lag ~8x phi_GR; 2310.8 rad full inspiral; Q-008 queued |
| PAPER_009 | Damping Mechanism Decomposition | 4-mechanism synthesis; GW190425 string=0.62 self-rectifies Q-001; BNS/BBH 2.43x; Q-009 queued |
| PAPER_010 | Post-Merger Oscillations / Remnant | QNM f_UQFF=0.95*f_GR (125 Hz shift); ringdown 29% faster; 15% extra dissipation |

### Corpus (2,419 files)
- `whitepapers/` — 2,255 `.md` files + 1 `.bak` — physics source of truth
- `pdf/` — 45 · `tex/` — 107 · `txt/` — 11

### Clean baseline
- `uqff_registry_primitives.py` — 96 canonical constants (from predecessor
  v5.86.0 UNIFIED_REGISTRY R5 baseline). **Registry-clean.**
- `uqff_calculator.py` — `DISPATCH` grows one paper at a time;
  `calc(paper_id, dataset)` public interface.
- `uqff_fidelity_tests.py` — 9-block gate (105 assertions), locking every
  primitive identity + every wired paper's stated values. Runs on every ship.

### Registry pantheon (live, grows per band)
- `UNIFIED_REGISTRY.csv` — master registry (17-col schema), +rows per paper
- `UNIFIED_REGISTRY_GRAPH.csv` — falsifiability edges (primitive→observable→paper)
- `UNIFIED_REGISTRY_CORPUS_CITATIONS.csv` — cross-reference ledger
- XGEO / R1 / R2 / R3 ledgers + QA views + regen modules
- `UNIFIED_REGISTRY_VERSION.txt` — per-ship marker

### Campaign infrastructure
- `CLAUDE.md` — campaign charter (sessions self-configure)
- `ship.ps1` — one-command band ship (gate → commit → tag-verify → push)
- `RULINGS_QUEUE.md` — never-block ambiguity protocol
- `WHITEPAPER_INDEX.md` — per-paper wired/not-wired ledger
- `SHIP_MESSAGE.txt` — per-band commit message
- `_BUILD_LOG.md` · `CHANGELOG.md` · `SESSION_LOG.md`

## Campaign roadmap

| Milestone | Content | Papers wired |
|---|---|---|
| v0.1.0 | Scaffold + registry primitives baseline | 0 |
| v0.2.0 | Corpus (2,419 files) + registry scaffolds | 0 |
| v0.3.0/v0.3.1 | Charter + campaign start | 1 |
| v0.4.0 | Band 1: PAPER_002+003 | 3 |
| v0.5.0 | Band 1: PAPER_004..006 | 6 |
| v0.6.0 | Band 1: PAPER_007 | 7 |
| v0.7.0 | Band 1: PAPER_008 | 8 |
| v0.8.0 | Band 1: PAPER_009 | 9 |
| **v0.9.0** ← current | Band 1: PAPER_010 | 10 |
| v0.4.0+ | One band per session (~20-80 papers each) | growing |
| PAPER_500 milestone | FULL STOP — Daniel's manual review | 500 |
| v1.0.0 | Full whitepaper coverage | 2,255 |

## Predecessor / attribution

Physics content, whitepapers, and canonical primitives originate in
[Star-Magic](https://github.com/Daniel8Murphy0007/Star-Magic).
That repository remains the canonical archive of the framework's development
history and whitepaper corpus. This repository (Star-Magic-Program) inherits
the physics and rebuilds only the code layer, correctly this time.

## Install

```
pip install star-magic-program
```

## Quick start

```python
from uqff_calculator import calc, wired_count, list_wired

print(f"Papers wired: {wired_count()}")

# Look up a specific paper (returns OPEN if not yet wired)
result = calc('PAPER_646')
print(result)
```

## Fidelity gate

Every ship must run and see exit 0:

```
python uqff_fidelity_tests.py
```

## License

- **Free / academic / non-commercial:** AGPL-3.0-or-later (see `LICENSE-AGPL-3.0.txt`)
- **Commercial / proprietary / closed-source SaaS:** contact
  `daniel.murphy00@enrgyone.com` (see `COMMERCIAL.md`)

See also: `NOTICE`, `CITATION.cff`, `CHANGELOG.md`, `SESSION_LOG.md`.
