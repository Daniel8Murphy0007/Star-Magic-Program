# Star-Magic-Program

**UQFF systematic rebuild — v0.1.0 scaffold**
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

## What is currently shipped (v0.1.0)

**Scaffold only. Zero whitepapers wired yet.** The following are in place:

- `uqff_registry_primitives.py` — 96 canonical constants, carried verbatim
  from `Star-Magic` v5.86.0 UNIFIED_REGISTRY R5 baseline. **Registry-
  clean.** Zero contamination from the predecessor's mess.
- `uqff_calculator.py` — scaffold skeleton with `DISPATCH = {}`, imports all
  96 registry constants, exposes `calc(paper_id, dataset)` public interface.
- `uqff_fidelity_tests.py` — gate assertions locking every primitive-composed
  EXACT identity. Runs on every ship.
- Dual license (AGPL-3.0-or-later + Commercial), citation, notice.
- CI + PyPI publishing workflows.

## What's next

Wiring campaign, one whitepaper at a time:

| Version | Content | Papers wired |
|---|---|---|
| **v0.1.0** ← current | Scaffold + registry baseline | 0 |
| v0.2.0 | 46 UQFF_LANDMARK papers (structural spine) | 46 |
| v0.3.0 | PAPER_001 through PAPER_099 (foundations) | +99 |
| v0.4.0 – v0.9.0 | Bands PAPER_100 – PAPER_1999 | +~1900 |
| v1.0.0 | Full whitepaper coverage (2,156 papers) | 2,156 |

Each wiring ship is atomic: read the paper → extract the canonical formula →
wire the dispatch → verify residual against the paper's stated value → gate
assertion added → commit → repeat.

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

See also: `NOTICE`, `CITATION.cff`.
