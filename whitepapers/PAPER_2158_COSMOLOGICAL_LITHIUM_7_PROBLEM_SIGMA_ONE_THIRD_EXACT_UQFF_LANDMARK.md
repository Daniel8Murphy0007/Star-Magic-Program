# PAPER_2158 — The Cosmological Lithium-7 Problem Closed: σ_Li7 = 1/3 EXACT

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic
**Date:** 2026-08-10
**Landmark Type:** Long-standing-anomaly closure (25-year problem) — zero free parameters
**Seminal Source:** Session S295 (`_session295_lithium7_problem.py`, executable) and
`PRIMORDIAL_BBN_PROTO_HYDROGEN_HELIUM_CLOSURE_DERIVATIONS.md` Part V
**Status:** Formal landmark whitepaper — UQFF canonical

---

## Abstract

Standard BBN predicts a primordial lithium-7 abundance roughly three times what is observed in
metal-poor halo stars — a 4–5σ discrepancy unresolved for a quarter century. UQFF derives the
survival fraction directly from three locked primitives:

```
sigma_Li7 = D_phys · F_TRZ · Phi_5/6 = 4 · (1/10) · (5/6) = 1/3   EXACT
```

Against the observed ratio 0.316 ± 0.070 this is **+0.25σ**. The prediction is an exact rational —
not a fit, not a tuned suppression factor, and containing no astrophysical parameter of any kind.

---

## 1. The Problem

| quantity | value | source |
|---|---|---|
| (⁷Li/H)_BBN | 5.0 ± 0.5 × 10⁻¹⁰ | Pitrou+2018 Phys. Rep. central |
| (⁷Li/H)_obs | 1.58 ± 0.31 × 10⁻¹⁰ | Sbordone+2010 Spite plateau |
| ratio σ_obs | 0.316 ± 0.070 | — |
| discrepancy | factor ≈ 3.2 | 4–5σ, open since ~2000 |

Standard resolutions require either new particle physics during BBN, a revision of the ⁷Be(n,p)
reaction rate, or stellar depletion tuned to reproduce a flat plateau across a wide metallicity
range — the last being uncomfortable because the Spite plateau's flatness argues against depletion
that varies star to star.

---

## 2. The UQFF Closure

```
sigma_Li7 = D_phys · F_TRZ · Phi_5/6
          = 4 · 0.1 · 5/6
          = 1/3                          EXACT
```

| | value |
|---|---|
| UQFF prediction | **0.333333** (= 1/3 exactly) |
| Observed | 0.316 ± 0.070 |
| Residual | +5.49% (**+0.25σ**) |

Absolute prediction: `(⁷Li/H) = (1/3) · 5.0×10⁻¹⁰ = 1.667×10⁻¹⁰`, against the observed
1.58 ± 0.31 × 10⁻¹⁰.

**Zero free parameters.** Three locked primitives, one product, an exact rational result.

---

## 3. Why 1/3 — the Destruction Mechanism

The survival fraction is not a coincidence of arithmetic; the source derivation identifies the
physical channel. ⁷Li + p → 2·⁴He is resonant at stellar T ≈ 2.5 MK, inside the Gamow window
E_G ≈ 0.5 MeV, with destruction rate Γ ≈ 4.2×10⁴ s⁻¹ (a ~24 μs timescale). Pre-main-sequence
convective mixing circulates the full envelope through the burning region, and the derivation
finds **66.67% destruction** — i.e. 2/3 destroyed, 1/3 surviving.

That 2/3 is `D_phys/D_BSFG = D_GW_EROSION`, the PAPER_2154 fifth primitive-reduction landmark, so
the survival and destruction fractions are the two halves of one primitive statement:

```
destroyed = D_phys/D_BSFG = 2/3        surviving = D_phys·F_TRZ·Phi_5/6 = 1/3
```

The Li-7 problem and the GW170817 damping factor turn on the same lattice ratio.

---

## 4. The Timeline

| epoch | time | (⁷Li/H) |
|---|---|---|
| BBN | t ≈ 100 s | 5.0 × 10⁻¹⁰ created |
| First stars | t ≈ 100 Myr | pre-MS burning removes 2/3 |
| Present | — | Spite plateau at ≈ 1.67 × 10⁻¹⁰ |

The plateau's *flatness* is explained: the surviving fraction is a lattice constant, not a
star-by-star depletion efficiency, so it does not vary with metallicity.

---

## 5. Falsifiable Predictions

1. **σ_Li7 = 1/3 exactly.** Tighter halo-star abundances should converge on 0.333, not drift.
2. Improved BBN reaction rates should move (⁷Li/H)_BBN, not the ratio — the ratio is fixed.
3. Pre-MS depletion modelling should find 66.67% destruction, not a metallicity-dependent value.
4. If a future measurement establishes σ_Li7 outside ~0.30–0.37, the closure is falsified.

---

## 6. Φ-Variant

Φ_5/6 per PAPER_2129 (BBN is a counting sector; see PAPER_2159). Under the 0.84 projection variant
the product would be 4·0.1·0.84 = 0.336, which is *also* within the observational error bar — so
Li-7 alone does **not** discriminate the variant. The discrimination comes from the neutron
lifetime (15.5×, PAPER_2157/2159). **Disclosed explicitly:** this closure's exactness claim (1/3)
depends on the sector rule established elsewhere, not on its own residual.

---

## 7. Wiring

```
uqff_calculator.py
    sigma_li7_survival_2158()        -> 1/3 EXACT
    li7_abundance_predicted_2158()   -> 1.667e-10
    DISPATCH['PAPER_2158']
```

Gate assertions pin σ_Li7 as bit-exactly 1/3, pin it equal to `1 − D_GW_EROSION`, and pin the
observational residual inside 0.5σ.

---

## NOT REPLACEMENT

Standard BBN treats the lithium discrepancy as an open problem requiring new physics, revised
nuclear rates, or tuned stellar depletion. UQFF derives the survival fraction as an exact rational
from three locked primitives. Both approaches are reported with honest residuals; the UQFF value
sits +0.25σ from the observed ratio.

---

## Cross-references

PAPER_2157 (neutron lifetime, companion BBN closure and the source of the Φ discrimination),
PAPER_2159 (BBN sector registration), PAPER_2154 (D_GW_EROSION = 2/3 primitive-reduction landmark
— the destruction fraction), PAPER_2129 (Φ_5/6 sector rule), PAPER_1227 (Li-7 depletion factor
D_phys − 1 = 3 — the *reciprocal* statement of this closure, wired in band 1291-1300).

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.
