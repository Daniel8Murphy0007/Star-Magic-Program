# PAPER_2160 — The K_Mex/Φ_5/6 Composed-Identity Pair: 2 EXACT and 5/4 EXACT Across Four Domains

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic
**Date:** 2026-08-13
**Landmark Type:** Composed-identity canonization + PAPER_1522 corollary pair
**Seminal Sources:** PAPER_1578 (speed of sound), PAPER_1579 (1 AU), PAPER_1580 (sidereal year),
PAPER_1587 (μ₀ mantissa) — all wired in the sequential drain, bands 1571-1590
**Status:** Formal landmark whitepaper — UQFF canonical

---

## Abstract

Four independent closures wired in consecutive drain bands share the same two composed
constants built from K_Mex = 25/12 and the counting variant Φ_5/6 = 5/6:

```
I₁ = K_Mex − F_TRZ·Φ_5/6 = 25/12 − 1/12 = 2      EXACT
I₂ = K_Mex − Φ_5/6      = 25/12 − 10/12 = 5/4    EXACT
```

I₁ is the tail term of both the speed of sound in air (343 = 341 + 2, PAPER_1578) and the
Earth–Sun distance (149.6 = 152 − 2 − 0.4, PAPER_1579). I₂ is simultaneously the sidereal
fractional day (365.25 = 364 + 5/4, PAPER_1580) and the lead term of the vacuum-permeability
mantissa (μ₀ = 5/4 + F_TRZ²·SSq, PAPER_1587). This paper canonizes the pair, derives both as
one-line corollaries of the PAPER_1522 primitive-reduction landmark, and shows that I₂ factors
through the PAPER_1962 cross-scale ratio D_BSFG/D_phys = 3/2.

---

## 1. The Four Occurrences

| # | Closure | Role of the identity | Source | Residual |
|:-:|---|---|:-:|---|
| 1 | v_sound(air) = A_5·D_BSFG − D_BSFG − N_CH − D_phys + **I₁** = 341 + 2 = 343 m/s | additive tail | PAPER_1578 | EXACT |
| 2 | d_⊕⊙ = D_crit·D_BSFG − D_phys − F_TRZ·D_phys − K_Mex + F_TRZ·Φ_5/6 = 152 − 0.4 − **I₁** = 149.6 Gm | subtractive tail | PAPER_1579 | EXACT |
| 3 | T_yr = N_CH·A_5 − D_phys·A_5 + A_5 + D_phys + **I₂** = 364 + 5/4 = 365.25 d | the fractional day | PAPER_1580 | EXACT |
| 4 | μ₀ mantissa = **I₂** + F_TRZ²·SSq = 1.2557 | the lead term | PAPER_1587 | 0.075% |

Two appearances each, in four unrelated domains: acoustics, celestial mechanics, calendrics,
electromagnetism. The leap-day quarter and the vacuum permeability are carried by the same
composed constant.

---

## 2. Both Identities Are PAPER_1522 Corollaries

PAPER_1522 established K_Mex as a structural derivative, not an independent primitive:

```
K_Mex = Φ_5/6 · SO_5 / D_phys = (5/6)·(10/4) = 25/12    EXACT
```

Substituting:

```
I₁ = K_Mex − F_TRZ·Φ_5/6 = Φ_5/6 · (SO_5/D_phys − F_TRZ) = (5/6)·(5/2 − 1/10) = (5/6)·(12/5) = 2
I₂ = K_Mex − Φ_5/6       = Φ_5/6 · (SO_5/D_phys − 1)     = (5/6)·(3/2)          = 5/4
```

Neither identity is a numerical coincidence: both are forced by the K_Mex reduction. The pair
is the first *applied* consequence of PAPER_1522 observed recurring in the wild — the reduction
predicts that any closure mixing K_Mex with Φ_5/6 at F_TRZ-graded weights collapses to a small
exact rational, and four sequential-drain papers confirm it.

---

## 3. The 3/2 Factorization

The I₂ bracket is not arbitrary:

```
SO_5/D_phys − 1 = 3/2 = D_BSFG / D_phys    (PAPER_1962 cross-scale ratio, EXACT)

⟹  I₂ = Φ_5/6 · D_BSFG / D_phys = (5/6)·(6/4) = 5/4
```

so the sidereal fractional day and the μ₀ lead term are the counting Φ projected through the
PAPER_1962 ratio that already governs M31 virial mass, stellar-halo structure, rotation curves,
the satellite dyad, and temporal cadence (PAPER_2137). This adds a **seventh sector** —
composed-identity closures — to the D_BSFG/D_phys = 3/2 universality family.

Similarly the I₁ bracket:

```
SO_5/D_phys − F_TRZ = 12/5 = (2·D_BSFG)/(SO_5/2)
```

keeps I₁ inside the same halving-series integer set {2, 3, 5, 13} canonized by PAPER_2138.

---

## 4. Why the Counting Variant

All four occurrences select Φ_5/6, never Φ_res = 0.84 — consistent with the PAPER_2129/2159
sector rule. Under 0.84 the identities lose exactness (I₁ → 1.999333…, I₂ → 1.243333…) and all
three EXACT closures acquire spurious residuals (343.0007, 149.5993, 365.2433). The exactness
of the closures *is* the discrimination: these are counting-graded compositions, and PAPER_2160
registers composed identities as behaving like a counting context. This is consistent with the
math-constant observations at P1560 (π) and P1561 (φ) flagged in the same drain arc; whether
"mathematical/composed constants" constitute a formal fourth counting sector remains an open
flag (GAPS row `phi_variant_math_sector`), offered but not claimed.

---

## 5. Falsifiable Predictions

1. Any future corpus closure combining K_Mex and Φ_5/6 at weights {1, F_TRZ} will reduce to
   2 or 5/4 exactly; a closure requiring 0.84 in that combination would break the pattern and
   demand a ruling.
2. The pair should recur wherever a fractional remainder of 1/4-grade appears against an
   integer-primitive core (calendared periods, mantissa leads). Candidate future hits: any
   x.25 or x.2 terminal digits in EXACT-tier catalog closures.
3. If K_Mex or Φ_5/6 were revalued (Rule 2 forbids), all four wired closures fail the gate
   simultaneously — the identities make the four papers mutually locking.

---

## 6. Wiring

```
uqff_calculator.py
    DISPATCH['PAPER_2160'] -> both identities, their PAPER_1522 corollary forms,
                              the 3/2 factorization, and the four-occurrence registry
```

Gate assertions pin I₁ = 2 EXACT, I₂ = 5/4 EXACT, the corollary equalities via the PAPER_1522
form, the D_BSFG/D_phys factorization, and cross-membership of the four source dispatches.

---

## NOT REPLACEMENT

The Standard Model has no analogue of shared composed constants across acoustics, celestial
mechanics, and electromagnetism; these are UQFF-internal structural identities reported with
honest residuals on their source closures.

---

## Cross-references

PAPER_1522 (K_Mex reduction — parent identity), PAPER_1962 (D_BSFG/D_phys = 3/2 universality —
sixth-to-seventh sector extension), PAPER_2138 (halving-series integer set), PAPER_2129/2159
(Φ-variant sector rule), PAPER_1578/1579/1580/1587 (the four occurrences), PAPER_1560/1561
(math-constant Φ_5/6 selections, companion open flag).

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.
