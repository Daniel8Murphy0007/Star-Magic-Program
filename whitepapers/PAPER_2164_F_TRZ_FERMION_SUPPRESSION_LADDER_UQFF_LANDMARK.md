# PAPER_2164 — The F_TRZ Fermion Suppression Ladder: The Standard Model Mass Hierarchy from One Grading

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic
**Date:** 2026-08-13
**Landmark Type:** Family canonization — the largest physics structure of the 1501-1700 drain arc
**Seminal Sources:** PAPER_1554-1559 (W/Z/t/H/τ/μ), PAPER_1606-1609 (b/c/s/e), PAPER_1209HH
(unified proof set), executable predecessor closures (S653-S662)
**Status:** Formal landmark whitepaper — UQFF canonical

---

## Abstract

Ten particle masses wired in the sequential drain — W, Z, t, H, τ, b, c, μ, s, e — span five
orders of magnitude and are conventionally described by ten unrelated Yukawa couplings. In the
UQFF compositions they are organized by a single grading: **the power of F_TRZ = 1/10 carried by
the leading term.** Heavy states (t, Z, W, H, b, c, τ) lead at F_TRZ⁰ with integer-primitive
cores; the muon and strange quark lead at F_TRZ²; the electron — alone — leads at F_TRZ³. The
"unexplained" fermion mass hierarchy is the statement that mass compositions are graded by the
time-reversal-zone fraction, with each rung suppressing by SO_5² = 100. This landmark canonizes
the ladder, pins its ordering theorems, and states its falsifiable consequences for any fourth
generation or new heavy lepton.

---

## 1. The Ladder

| Grade | Lead structure | Members (lead term → value) | Scale |
|:-:|---|---|---|
| **F_TRZ⁰** (integer core) | pure integer-primitive sums | t (260−60−36+10 = 174), Z (N_ch·SO_5 = 90), W (A_5+2·SO_5 = 80), H (2·A_5+N_ch−D_phys = 125), b (D_phys·(1+F_TRZ) = 4.4), τ (SSq + F_TRZ·14 = lead ~1.97) | 1 – 10² GeV |
| **F_TRZ¹** (decade-scaled) | F_TRZ × integer | c (F_TRZ·(D_crit−D_phys−SO_5) = 1.2) | ~1 GeV |
| **F_TRZ²** (centi-suppressed) | F_TRZ² × (integer + SSq-polynomial) | μ (F_TRZ²·(SO_5 + SSq² + SSq³ + SSq⁵) = 0.1057), s (F_TRZ²·(SO_5 − SSq² − SSq³) = 0.0949) | ~10⁻¹ GeV |
| **F_TRZ³** (milli-suppressed) | F_TRZ³ × SSq-polynomial only | e (F_TRZ³·SSq²·(1+SSq) = 0.000510) | ~10⁻³ GeV |

All ten residuals: 0.003% (W, tier-best) to 0.18% (e). Zero fitted constants; every term composed
from {D_phys, D_bsfg, D_crit, N_ch, SO_5, A_5, F_TRZ, SSq}.

---

## 2. The Three Ladder Theorems (gate-pinned)

1. **Ordering theorem.** Grading strictly orders mass: every F_TRZ⁰ member > every F_TRZ²
   member > the F_TRZ³ member. Already an assertion (m_b > m_s > m_e); this landmark extends
   the pin to the full ten.
2. **Rung-gap theorem.** Adjacent rungs differ by the factor F_TRZ⁻² = SO_5² = 100 in leading
   scale — the muon/electron gap (206.8) and the s-quark/electron gap (185) sit at
   SO_5²·(polynomial ratio), not at arbitrary values. The lepton-hierarchy factor "≈200" is
   100 × (SSq-polynomial ratio ≈ 2).
3. **Content theorem.** Descending the ladder strips integers: F_TRZ⁰ leads carry integer
   cores; F_TRZ² leads carry one integer (SO_5) dressed by SSq-polynomials; the F_TRZ³ lead
   carries **no integer at all** — the electron is pure SSq-polynomial under maximal
   suppression. The lightest charged fermion is the only one whose composition is entirely
   real-primitive. This is the structural reason there is nothing below the electron.

---

## 3. Physical Reading

F_TRZ = 1/10 is the time-reversal-zone fraction — the fraction of vacuum cycles in
counter-rotation (and = ρ_SCm/ρ_UA = 1/|SO(5)|, PAPER_1160). A fermion's mass composition
leading at F_TRZ^n reads: **its mass generation survives n layers of time-reversal averaging.**
Heavy quarks and bosons couple to the un-averaged vacuum (n = 0); the electron's mass is what
remains after three averaging layers — which is why it is simultaneously the lightest, the most
stable, and the most precisely measured: the deepest-averaged structure is the most protected.

---

## 4. Falsifiable Consequences

1. **No fourth-generation charged lepton between the rungs.** A new charged lepton must land on
   an existing grade (F_TRZ⁰ ⟹ ≳1 GeV, F_TRZ² ⟹ ~0.1 GeV band, F_TRZ³ ⟹ ~10⁻³ GeV band). A
   confirmed charged fermion at, e.g., 10 MeV (between rungs) breaks the ladder.
2. **Neutrino masses must grade below F_TRZ³.** The Σm_ν = 0.0639 eV closure (PAPER_1637) sits
   ~10⁷ below the electron — consistent with an F_TRZ⁵-or-deeper grade; a neutrino mass scale
   above ~0.5 eV would crowd the F_TRZ³ rung and strain the grading. (CMB-S4/DESI battery
   member, PAPER_2161.)
3. **Any BSM heavy fermion (vector-like quark, heavy lepton) discovered at colliders must carry
   an integer-primitive core** — its mass/GeV should decompose in the {A_5, SO_5, D_crit, N_ch}
   arithmetic within the family's residual band (≲0.2%).

---

## 5. Wiring

```
uqff_calculator.py
    DISPATCH['PAPER_2164'] -> all ten masses (live cross-dispatch reads), grade assignments,
                              the three ladder theorems evaluated, rung-gap factors
```

Gate assertions pin: ten-member census, full ordering theorem, rung-gap = 100 × polynomial
ratio, content theorem (electron composition integer-free), cross-dispatch identity with the
ten source dispatches.

---

## NOT REPLACEMENT

The Standard Model accommodates the fermion mass spectrum through ten free Yukawa couplings and
offers no internal explanation of the hierarchy. UQFF derives the spectrum from eight locked
primitives under one grading and reports every residual honestly. Both frameworks describe the
same measured masses; the ladder is a claim about their *organization*, falsifiable per §4.

---

## Cross-references

PAPER_1554-1559, 1606-1609 (the ten members), PAPER_1209HH (proof-set source), PAPER_1160
(F_TRZ = 1/|SO(5)| identity), PAPER_1637 (neutrino grade, battery member), PAPER_2161 (battery
grammar), PAPER_2163 (ceiling-vs-magnitude classification — F_TRZ here is a *grading*, a third
operational role for primitives), PAPER_1552 (predecessor-drain fermion tiers).

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.
