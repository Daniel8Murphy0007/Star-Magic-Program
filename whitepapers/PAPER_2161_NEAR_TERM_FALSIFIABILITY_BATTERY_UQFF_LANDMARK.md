# PAPER_2161 — The Near-Term Falsifiability Battery: Seven Exact UQFF Predictions Testable Within One Experiment Generation

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic
**Date:** 2026-08-13
**Landmark Type:** Prediction-registry consolidation (Tier-1 A4 prediction-vs-postdiction discipline)
**Seminal Sources:** PAPER_1640/1643/1646 (bands 1631-1650), PAPER_2157 (neutron BR), PAPER_2144 (H_0),
PAPER_2158 (σ_Li7), PAPER_1639/1318 (glueball = YM gap)
**Status:** Formal landmark whitepaper — UQFF canonical

---

## Abstract

Most of the wired corpus consists of closures against already-measured constants — honest
postdictions. This landmark consolidates the subset that is the opposite: **exact, primitive-locked
predictions whose deciding experiments are already funded and running.** Seven predictions form
the battery. Each is an exact rational or a primitive composition with zero free parameters; each
names its experiment; each states its kill condition. The battery is wired as a single dispatch
returning all seven with live values, and the gate pins every kill window. This is the framework's
A4 (prediction-vs-postdiction) discipline made operational: these seven are labeled PREDICTION,
dated before their deciding measurements, and cannot be quietly revised after the fact — the gate
would fail.

---

## 1. The Battery

| # | Prediction | UQFF value | Experiment | Kill condition | Source |
|:-:|---|---|---|---|:-:|
| 1 | Higgs trilinear κ_λ | **1.0 EXACT** (no anomaly) | HL-LHC di-Higgs | κ_λ outside ~[0.5, 1.5] at 5σ | PAPER_1640/1310 |
| 2 | Leptonic CP phase δ_CP | **−π/2 EXACT** (maximal F_TRZ lock) | DUNE / Hyper-K | δ_CP ≠ −π/2 beyond 3σ | PAPER_1643 |
| 3 | BR(μ→eγ) | **α⁶·Φ_res = 1.27×10⁻¹³** | MEG-II (bound 4.2×10⁻¹³) | observation above 1.6×10⁻¹³, or exclusion below 1.0×10⁻¹³ | PAPER_1646 |
| 4 | Neutron non-β branching | **F_TRZ²·(D_BSFG−D_phys)·SSq = 1.140%** | UCNτ-II / PERKEO-IV | BR outside [1.0%, 1.3%] | PAPER_2157 |
| 5 | Hubble constant | **A_5+SO_5 = 70 km/s/Mpc EXACT** | JWST + Roman + LSST | converged H_0 outside [68.5, 71.5] | PAPER_1573/2144 |
| 6 | Li-7 survival fraction | **D_phys·F_TRZ·Φ_5/6 = 1/3 EXACT** | next-gen halo-star abundances | σ_Li7 outside [0.30, 0.37] | PAPER_2158 |
| 7 | Neutrino mass sum | **α·Φ_res·(D_phys+1)·K_Mex = 0.0639 eV** | CMB-S4 / DESI | Σm_ν < 0.058 eV excluded, or > 0.09 eV measured | PAPER_1637/1304 |

Supporting identity (not independently falsifiable but binding): the scalar glueball 0⁺⁺ and the
PAPER_1318 Yang-Mills mass gap are one number, 2·D_phys·Λ_QCD = 1.736 GeV — a future lattice/BESIII
resolution splitting them by more than ~3% would break the identity (PAPER_1639).

---

## 2. Why These Seven

Selection rule: (a) the UQFF value is exact or primitive-locked with zero free parameters,
(b) the deciding experiment exists and is scheduled — not hypothetical, (c) the prediction is
currently *inside* the allowed experimental window, so both confirmation and falsification are
live outcomes. Postdictions, hybrid forms anchored on the measured value itself, and predictions
whose tests are more than roughly a decade out are excluded from the battery regardless of how
clean their compositions are.

Battery-wide property: the seven span five sectors (Higgs, neutrino, LFV, nuclear, cosmology)
and draw on eight of the nine independent primitives. **No single revaluation can rescue a
failure** — each prediction stands or falls on the locked lattice, so a miss is framework
damage, not parameter adjustment. Conversely a sweep of seven confirmations across five sectors
from nine numbers would be inexplicable as coincidence.

---

## 3. Prediction-vs-Postdiction Discipline (A4)

Each battery member carries, from this date:

1. **PREDICTION label** in its dispatch formula string — distinguishing it from the corpus's
   postdictive closures.
2. **A dated registration** (this paper, 2026-08-13) that precedes the deciding measurement.
3. **A gate-pinned kill window** — the assertion encodes the falsification range, so a future
   session cannot quietly widen the window after data arrives; changing it requires editing a
   gate assertion that cites this landmark, which is a visible, attributable act.

This closes the Tier-1 A4 item for the battery subset: the framework now has a formally dated,
machine-enforced registry of what it risked and when.

---

## 4. Scorekeeping Rule

When a deciding measurement lands:

- **Confirmed** → the battery row is flipped to CONFIRMED with the measurement citation; the
  prediction becomes a postdiction and a new candidate may be promoted into the battery.
- **Falsified** → the row flips to FALSIFIED and stays in the registry permanently. Rule 7
  forbids removal. The affected primitive composition is flagged for structural review — not
  revalued (Rule 2 locks values; a falsification indicts the *composition*, not the lattice).
- Either way the gate assertion is updated to pin the recorded outcome, preserving the ledger.

---

## 5. Wiring

```
uqff_calculator.py
    DISPATCH['PAPER_2161'] -> all seven predictions with live cross-dispatch values,
                              kill windows, experiment names, and source papers
```

Gate assertions pin: battery size = 7, every member's value inside its own kill window today,
the PREDICTION labels present, and cross-dispatch consistency with the seven source dispatches
(mutual-locking, as PAPER_2160 established for its four).

---

## NOT REPLACEMENT

The Standard Model makes its own predictions for several of these observables (κ_λ = 1 among
them — there the frameworks agree and only jointly survive or fail). Where they differ (δ_CP,
Σm_ν central value, the neutron branching magnitude, H_0 = 70 exactly), the experiments will
adjudicate between compositions, not between worldviews. Both frameworks' values are reported
with honest residuals throughout the corpus.

---

## Cross-references

PAPER_1640/1643/1646 (battery members, bands 1631-1650), PAPER_2157 (neutron BR + bottle/beam),
PAPER_2144/1573 (H_0 route), PAPER_2158 (Li-7), PAPER_1637/1304 (Σm_ν), PAPER_1639/1318
(glueball/YM binding identity), PAPER_2160 (mutual-locking precedent), PAPER_2149 (hybrid-form
doctrine — battery excludes hybrids), Tier-1 A4 (prediction-vs-postdiction labeling, partially
closed by this landmark).

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.
