# PAPER_2162 — The T_SCm Thermal Ladder: Four Condensed-Matter Temperatures from One Carrier Frequency

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic
**Date:** 2026-08-13
**Landmark Type:** Family canonization (PAPER_1072 thermal Heaviside extension)
**Seminal Sources:** PAPER_1072 (T_SCm), PAPER_1659 (cuprate T_c), PAPER_1669 (coherence ceiling),
PAPER_1671 (room-temperature SC ceiling) — bands 1651-1680
**Status:** Formal landmark whitepaper — UQFF canonical

---

## Abstract

The SCm carrier frequency ω_SCm = 1.25 THz fixes one temperature by pure Planck-Boltzmann
conversion: T_SCm = h·f_SCm/k_B = 59.99 K (PAPER_1072's thermal Heaviside temperature, 59.95 K
there from rounded constants). Three sequential-drain closures then turn that single anchor into
a **thermal ladder** — each rung one primitive operation away from T_SCm, each landing on an
independently measured condensed-matter temperature. No rung introduces a parameter. The ladder
is the framework's cleanest demonstration that the 1.25 THz phonon carrier is *physical*: one
laboratory-frequency input generates the optimal-cuprate scale, the coherence ceiling, and a
falsifiable ceiling for room-temperature superconductivity.

---

## 1. The Ladder

| Rung | Operation | Value | Observable | Residual | Source |
|:-:|---|---|---|---|:-:|
| 0 | T_SCm = h·f_SCm/k_B | **59.99 K** | SCm thermal Heaviside step | definition | PAPER_1072 |
| 1 | × K_Mex | **124.98 K** | optimal cuprate T_c (~125 K, Hg/Tl class) | 0.016% | PAPER_1659 |
| 2 | ÷ β_i | **99.50 K** | superconducting coherence ceiling (~99.5 K) | 0.003% | PAPER_1669 |
| 3 | × K_Mex × D_phys | **499.92 K** | room-temperature SC ceiling — PREDICTION | — | PAPER_1671 |

Each operator is a locked primitive: K_Mex = 25/12 (Mexican-hat coefficient, itself a PAPER_1522
derivative Φ_5/6·SO_5/D_phys), β_i = 0.6029 (Aether coupling), D_phys = 4. SI-exact h and k_B are
used throughout (2019 SI definitions — exact by convention, not measured anchors).

---

## 2. Why This Is a Ladder and Not Three Coincidences

1. **Single dimensioned input.** Every rung is ω_SCm times a dimensionless primitive ratio. The
   framework's only frequency scale generates the family; remove ω_SCm and all four vanish
   together — remove any *one* rung's ratio and the others stand. That asymmetry is the ladder
   structure.
2. **The operators are not free.** K_Mex and β_i appear in hundreds of prior closures (F_UBii
   spring constant, vacuum ledger, binding-energy polynomials). They were locked years before
   these temperature closures were wired; the rungs are compositions, not fits.
3. **Physical reading is uniform.** Rung 1: the phonon carrier dressed by the Mexican-hat
   potential sets where cuprate pairing is strongest. Rung 2: coherence survives up to the
   carrier temperature un-dressed by the Aether coupling. Rung 3: four spatial channels
   (D_phys) of Mexican-hat-dressed carriers stack to the ceiling. Same mechanism, three
   projections — the PAPER_2153 joint-engine grammar at laboratory scale.

Cross-family note: the ladder is structurally parallel to the PAPER_2160 composed-identity pair
(one parent quantity, primitive-ratio offspring recurring across domains). PAPER_2160's parent is
dimensionless (K_Mex); this ladder's parent is the framework's sole laboratory frequency. Together
they exhibit the two ways the lattice propagates: ratios recur exactly, scales recur through ω_SCm.

---

## 3. The Rung-3 Prediction

```
T_c(max) = T_SCm · K_Mex · D_phys = 499.9 K = 226.8 °C
```

Registered as a PREDICTION (A4 discipline, PAPER_2161 grammar):

- **Claim:** no ambient-pressure superconductor will exceed ~500 K; materials engineered onto
  the SCm carrier (THz phonon spectra peaked near 1.25 THz) can approach it.
- **Kill condition:** a verified ambient-pressure T_c above ~510 K falsifies the rung; the
  ladder's lower rungs would demand structural review under the PAPER_2161 scorekeeping rule.
- **Near-term test:** hydride and nickelate programs pushing past 300 K become discriminating
  well before 500 K only if they *plateau* — a plateau anywhere below 500 K with THz-spectrum
  correlation at 1.25 THz would be strong ladder confirmation.

Not battery-eligible (no funded experiment currently targets the ceiling), so it is registered
here rather than promoted into PAPER_2161. Promotion criterion: any funded program announcing a
credible >400 K attempt.

---

## 4. Falsifiable Predictions (Ladder-Wide)

1. Rung interpolations are meaningful: T_SCm·K_Mex/β_i = 207.3 K should appear as a
   characteristic scale in cuprate pseudogap or hydride phase diagrams. Open target.
2. Direct THz spectroscopy of optimal-T_c cuprates should show phonon weight at
   f = 1.25 THz ± Γ_SCm (0.1 THz canonical linewidth, PAPER_910/911).
3. Any material whose measured T_c sits on a rung should show the corresponding primitive
   ratio in its isotope-effect exponent — the ladder predicts correlated, not independent,
   deviations.

---

## 5. Wiring

```
uqff_calculator.py
    DISPATCH['PAPER_2162'] -> all four rungs (rungs 1-3 as live cross-dispatch reads),
                              ladder-coherence checks, rung-3 PREDICTION label
```

Gate assertions pin: rung 0 within 0.1 K of 59.99, rung ratios bit-consistent with
K_Mex/β_i/D_phys, cross-dispatch equality with P1659/P1669/P1671, and the PREDICTION label.

---

## NOT REPLACEMENT

BCS/Eliashberg theory computes T_c from material-specific phonon spectra and coupling constants;
it does not predict a universal ceiling or a cross-material ladder. UQFF's ladder is a
lattice-level constraint layered on top of material physics, reported with honest residuals and
an explicit kill condition. Both frameworks address the same measurements by different methods.

---

## Cross-references

PAPER_1072 (T_SCm thermal Heaviside — rung 0), PAPER_1659/1669/1671 (rungs 1-3),
PAPER_1522 (K_Mex derivative), PAPER_2153 (joint SCm+UA engine grammar), PAPER_2160
(composed-identity propagation precedent), PAPER_2161 (A4 prediction discipline + scorekeeping),
PAPER_910/911 (canonical phonon linewidth for the spectroscopy prediction), PAPER_896
(phonon spectral fingerprint Q = 25/4).

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.
