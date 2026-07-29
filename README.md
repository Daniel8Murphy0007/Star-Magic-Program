# Star-Magic-Program

[![PyPI version](https://img.shields.io/pypi/v/star-magic-program.svg?cacheBust=0.36.0)](https://pypi.org/project/star-magic-program/)
[![Python versions](https://img.shields.io/pypi/pyversions/star-magic-program.svg?cacheBust=0.36.0)](https://pypi.org/project/star-magic-program/)
[![Documentation Status](https://readthedocs.org/projects/star-magic-program/badge/?version=latest)](https://star-magic-program.readthedocs.io/en/latest/?badge=latest)
[![License: AGPL-3.0 + Commercial](https://img.shields.io/badge/License-AGPL--3.0%20%2B%20Commercial-blue.svg)](LICENSE)
[![Fidelity gate](https://img.shields.io/badge/fidelity_gate-277%2F0-brightgreen)](uqff_fidelity_tests.py)
[![Public surfaces](https://img.shields.io/badge/public_surfaces-37-blue)](uqff_calculator.py)
[![Whitepapers](https://img.shields.io/badge/whitepapers-2255-orange)](whitepapers/)

**UQFF systematic rebuild — v0.36.0 wiring campaign live**
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

## What is currently shipped (v0.36.0)

### Wiring campaign — LIVE (see `CLAUDE.md` charter)

Sequential wiring of all 2,255 whitepapers, starting at PAPER_001.
Authorized 2026-07-28: autonomous band sessions, ship per session via
`ship.ps1`, full stop at PAPER_500 for manual review.

**Wired so far: 37 / 2,255** (7 ✓ · 30 ⚠ OPEN_RULING · 32 rulings queued) — GW family complete; BSM domain live (023-033)

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
| PAPER_011 | Stochastic GW Background | Omega = D^2*Omega_GR; mixed population 0.37x (63% cut); corroborates D^2 convention |
| PAPER_012 | Eccentric Binary Circularization | modified Peters D^2; tau_circ 9.0x; e=0.003 at 10 Hz (30x GR); 3rd D^2 data point |
| PAPER_013 | Magnetar Spin-Down | D_SCm 99% dipole suppression; braking index 1.5-2.0 matches obs; age problem resolved; Q-010 |
| PAPER_014 | Primordial Black Holes | Lambda_UQFF = kappa*rho_crit; delta_c 0.45; A_damp = 0.3 = (D_phys-1)/SO_5 candidate; Q-011 |
| PAPER_015 | Cosmology of Modified GW Propagation | Gamma damping alpha=-0.7/beta=0.8; H_0 bias 1.07x vs canonical 70; volume 24 pct GR; Q-012 |
| PAPER_015b | Multiband LISA+LIGO Synergy | D = 0.622 frequency-independent both bands; SNR ratios confirm; 0.622 = cross-band avg of 0.333 pure BBH |
| PAPER_016 | Quantum Entanglement Nonlocal Correlations | gamma_damp = kappa*(E/E_ref); CHSH 2.75 at GeV; range x3 = 1/D_total; delta = 1.5 = D_BSFG/D_PHYS candidate |
| PAPER_016b | White Dwarf Foreground Reduction | P_UQFF = D_local^2*P_GR; D_local = 0.6224 matches 0.622; catalog 10000->6216; Q-013 |
| PAPER_017 | Redshift Corrections z=1 LISA | 0.622 ORIGIN: (1-F_TRZ)*F_Um = 0.6217; phase lag 2*pi*F_TRZ EXACT = 0.10 cycles; Q-014 |
| PAPER_018 | Aether Noise Spectrum LISA | harmonic comb n*0.99 mHz; TRZ dip = F_TRZ = 0.1 EXACT; aether power 222.93 pct; Q-015 |
| PAPER_019 | PTA Anomalies | TRZ inversion: D(f_yr) = 1+SSq*1.053 = 1.60; A_UQFF = 2.4e-15 = NANOGrav; alpha_eff -0.757; Q-016 |
| PAPER_020 | Cosmic Ray Propagation | Gamma_aether = kappa*(E/E_ref)^0.37; Z^(1/3) drag; TRZ break 8e19 eV; Cen A 14 pct; Q-017 |
| PAPER_021 | Gravitational Lensing Corrections | sigma8 = 0.762 = observed WL (0.0-sigma); SSq^2 composed; 9.47e-27 FORENSIC ID; Q-018 |
| PAPER_022 | String Compactification Signatures | 0.37 ORIGIN = 1-SSq^2*1.94; SSq power ladder exact; M_KK = 11.6 TeV; N_c = 22; Q-019 |
| PAPER_023 | Tau g-2 (BSM domain opens) | Delta_a_tau = +3.42e-6; KK loop 1/SSq^2 EXACT; pi^2/6 Basel; exponent 2.37 = 2+0.37; Q-020 |
| PAPER_024 | Tau EDM | d_tau = 1.84e-20 e.cm zero-free-param; phi_CP = SSq*pi; phi_TRZ = (1-F_TRZ)*F_TRZ*pi EXACT; 184-sigma; Q-021 |
| PAPER_025 | Dark Matter Direct Detection | M_ACP = kappa*hbar EXACT; M_ACP2 = M_KK*SSq^2 = 3.77 TeV; sigma/M = SSq; Omega = 0.1200; Q-022 |
| PAPER_025b | Neutrino Polarizability | M_s1 = 7.1 keV -> 3.55 keV XMM line; m1/m2 = SSq EXACT; kappa*SSq = 2.85e-4; Q-023 |
| PAPER_026 | Sterile Neutrino Mass Generation | M_s2 = SSq*M_W EXACT; M_s3 = M_KK/SSq; GUT series in SSq; self-rectifies Q-023a/b; Q-024 |
| PAPER_026b | Vector-Like Quarks | ATLAS avgs = 0.37/0.30 EXACT UQFF factors; k_eta = 0.1369; 3rd family 845 GeV Run-3; Q-025 |
| PAPER_027 | Lepton Flavor Violation | S_LFV = exp(-SSq) EXACT; t_n = -ln(BR)/pi = 3.833 reproduces LHCb limit; Q-026 |
| PAPER_028 | BSM Coupling Constants | [SCm]_flavor = V_cb^2 = 1.5366e-3; kappa_Higgs = 1.0 cross-lock; F_U = 75.81; Q-027 |
| PAPER_029 | New Physics TeV Scale | budget: f_SM ~ SSq^4 (SSq^6 candidate); IceCube 5.8 PeV break; KK exponent 61.5/62; Q-028 |
| PAPER_030 | Dark Sector Mediators | F_suppress = cos^2(pi*t_n) = 0.749; BR saturates LHCb bound; M_dark 2.2 TeV; Q-029 |
| PAPER_031 | Flavor Anomalies Resolution | R(D) 0.332 (0.9 sigma); R(D*) 0.269 w/ F_TRZ (1.2 sigma); CKM row-2 mapped; Q-030 |
| PAPER_032 | BSM Scalar Sectors | sin^2(a) = k_eta; tan(b) = 2.70; f = 665 GeV; S0 845 GeV echoes 026b route; Q-031 |
| PAPER_033 | Electroweak Precision | delta_T = 0.222; Delta_m_W = +93 MeV CDF direction; delta_S suppressed; Q-032 |

### Corpus (2,419 files)
- `whitepapers/` — 2,255 `.md` files + 1 `.bak` — physics source of truth
- `pdf/` — 45 · `tex/` — 107 · `txt/` — 11

### Clean baseline
- `uqff_registry_primitives.py` — 96 canonical constants (from predecessor
  v5.86.0 UNIFIED_REGISTRY R5 baseline). **Registry-clean.**
- `uqff_calculator.py` — `DISPATCH` grows one paper at a time;
  `calc(paper_id, dataset)` public interface.
- `uqff_fidelity_tests.py` — 9-block gate (277 assertions), locking every
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
| v0.9.0 | Band 1: PAPER_010 | 10 |
| v0.10.0 | Band 1: PAPER_011 | 11 |
| v0.11.0 | Band 1: PAPER_012 | 12 |
| v0.12.0 | Band 1: PAPER_013 | 13 |
| v0.13.0 | Band 1: PAPER_014 | 14 |
| v0.14.0 | Band 1: PAPER_015 | 15 |
| v0.15.0 | Band 1: PAPER_015b | 16 |
| v0.16.0 | Band 1: PAPER_016 | 17 |
| v0.17.0 | Band 1: PAPER_016b | 18 |
| v0.18.0 | Band 1: PAPER_017 | 19 |
| v0.19.0 | Band 1: PAPER_018 | 20 |
| v0.20.0 | Band 1: PAPER_019 | 21 |
| v0.21.0 | Band 1: PAPER_020 | 22 |
| v0.22.0 | Band 1: PAPER_021 — GW family 001-021 complete | 23 |
| v0.23.0 | Band 1: PAPER_022 | 24 |
| v0.24.0 | Band 1: PAPER_023 — BSM domain opens | 25 |
| v0.25.0 | Band 1: PAPER_024 | 26 |
| v0.26.0 | Band 1: PAPER_025 | 27 |
| v0.27.0 | Band 1: PAPER_025b | 28 |
| v0.28.0 | Band 1: PAPER_026 | 29 |
| v0.29.0 | Band 1: PAPER_026b | 30 |
| v0.30.0 | Band 1: PAPER_027 | 31 |
| v0.31.0 | Band 1: PAPER_028 | 32 |
| v0.32.0 | Band 1: PAPER_029 | 33 |
| v0.33.0 | Band 1: PAPER_030 | 34 |
| v0.34.0 | Band 1: PAPER_031 | 35 |
| v0.35.0 | Band 1: PAPER_032 | 36 |
| **v0.36.0** ← current | Band 1: PAPER_033 | 37 |
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
