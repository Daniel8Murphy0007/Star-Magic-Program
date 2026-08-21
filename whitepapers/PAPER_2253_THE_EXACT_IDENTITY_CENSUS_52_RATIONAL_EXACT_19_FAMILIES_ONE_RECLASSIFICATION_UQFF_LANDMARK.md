# PAPER_2253 — The Exact-Identity Census: 52 Rational-EXACT Lattice Identities in 19 Families, Every One Re-Verified on Every Call — and One Over-Claim Caught and Reclassified

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic-Program
**Date:** 2026-08-21
**Landmark Type:** Census consolidation (the fourth census: predictions → paradoxes →
residuals → THE IDENTITY LATTICE) + P2252 zero-conflation resolution + one Rule 7
reclassification
**Seminal Sources:** the identity landmarks themselves (PAPER_1521/1522/2112/2154 the
primitive-reduction family; PAPER_1203-Nuclear the magic numbers; PAPER_2132/2237 the
kernel; PAPER_1156/2133/2178 the tilt; PAPER_2128 successors; PAPER_2138 halving;
PAPER_2238 budgets; PAPER_2239/2240/2241 the ladder/sector identities; PAPER_1954/1962/2143
cross-scale; PAPER_2136/1804 tidal; PAPER_2065/2116/2126/2137/2139 composed integers),
PAPER_2252 (the zero-conflation this resolves), Fraction-arithmetic verification (this
census's method)
**Status:** Formal landmark whitepaper — UQFF canonical (Daniel-directed: census #2 of the
queue)

---

## Abstract

The framework's EXACT identities — its crown jewels — are enumerated, classified, and
**re-verified in exact rational arithmetic** for the first time as one population:

| Result | Count |
|---|:-:|
| Flagship identities censused | **53** |
| **Rational-EXACT verified** (Fraction arithmetic, zero tolerance) | **52** |
| Reclassified (printed-precision, not rational-exact) | **1** |
| Families | **19** |

The artifact — **`UNIFIED_REGISTRY_EXACT_IDENTITIES.csv`** — carries each identity's
statement, family, both sides as exact rationals, verification status, and source papers.
The wired dispatch **re-verifies all 52 on every call** (Fraction arithmetic in-dispatch —
the strongest pin the framework has: the identity lattice cannot drift without the public
surface itself failing).

**The Rule 7 catch:** the REM-index composition **0.579 = SSq·Φ_res + F_TRZ** evaluates to
0.5788 (= 1447/2500) — it is exact only AT PRINTED PRECISION (rounds to 0.579), not
rational-exact. Reclassified from the EXACT class to a new `printed_precision` class; the
PAPER_1839/2238 usages remain valid at their stated 3-digit precision, but the census
separates the classes so the EXACT count is honest.

## 1. The 19 Families (with member counts)

| Family | n | Flagships |
|---|:-:|---|
| magic | 7 | all seven magic numbers {2, 8, 20, 28, 50, 82, 126} from integer arithmetic |
| primitive_reduction | 5 | D_BSFG = D_crit−2·SO_5; K_MEX = Φ₅/₆·SO_5/D_phys; κ = (SO_5/2)·F_TRZ⁴; Q_phonon = 25/4; D_GW = 2/3 |
| tilt | 4 | K_MEX−2 = 1/12; F_TRZ·Φ₅/₆ = 1/12; 137 = 125+12; the Hubble tilt |
| budget | 4 | Page 24899/25000; WH share 101/25000; NS 17/20+3/20 = 1; Poincaré 7/12 = 1/2 + 1/12 |
| composed_integer | 4 | 62 = 2·D_crit+SO_5; 44 = D_phys·(SO_5+1); 25 = SO_5²/D_phys; d_g's D_crit·SO_5¹⁹ |
| kernel | 3 | K = 19/160; γ_Immirzi = 19/80; F_TRZ·K_MEX = 5/24 |
| successor | 3 | SO_5+1 = 11; N_CH = SO_5−1; λ_vac ratio 11 |
| cross_scale | 3 | A_5·K_MEX = 125; A_5/D_phys = 15; D_BSFG/D_phys = 3/2 |
| ladder_rung | 3 | E₀ exponent 20 = D_crit−D_BSFG; E_pair exponent 22 = D_crit−D_phys = 2·(SO_5+1); pair exponent 13 = D_crit/2 |
| composition | 3 | Φ_0.84 = 1−(D_phys·F_TRZ)² = 21/25; γ_recip = κ·F_TRZ; (rem_579 → reclassified out) |
| sector_ladder | 2 | Σ1..5 = 15 = A_5/D_phys; +UA = 25 = SO_5²/D_phys |
| tidal | 2 | k₂/Q = 3/125; Q_tidal = 25/2 |
| angular | 2 | 360 = D_BSFG·A_5; 45 = A_5·(D_phys−1)/D_phys |
| anchor_lattice | 2 | 6000 = A_5·SO_5²; k₁ = SO_5¹⁵ |
| ratio | 2 | F_TRZ = 1/SO_5; mass-gap 5/2 = SO_5/D_phys |
| integer_sum | 1 | H₀ = A_5+SO_5 = 70 |
| halving | 1 | {2, 3, 5, 13} = the four even primitives halved |
| cross_regime | 1 | 0.3 = (D_phys−1)/SO_5 |
| composed | 1 | 0.03 = (D_phys−1)/SO_5² |

## 2. The P2252 Zero-Conflation Resolved

The residual census's 1,770 zero-residual dispatches split three ways (measured live):

| Class | Count | Meaning |
|---|:-:|---|
| EXACT-claiming | **531** | formula carries an EXACT claim (611 total dispatches claim EXACT; 531 of them at zero residual) |
| Census-type | 104 | census/audit/ledger dispatches — zero by type |
| **Paper-value reproduction** | **1,136** | the wired composition reproduces the source paper's stated value bit-identically — accuracy at paper precision, not lattice-EXACT claims |

The 53-member flagship table is the CURATED core of the 531 — the identities with named
landmark papers and primitive decompositions; the remaining EXACT-claiming dispatches carry
the same identities in their applied contexts (the correlated-lock structure makes them
dependents, not independents).

## 3. Method (Rule 7)

1. All verification in `fractions.Fraction` — zero floating-point tolerance for the EXACT
   class. IEEE float-exact identities (μ₀ = 4π·F_TRZ⁷ class) are NOT in this table — they
   carry their own disclosure class (PAPER_2108) and are excluded rather than blurred in.
2. The one failure was not forced: 0.5788 ≠ 0.579 in rationals, so the member was
   RECLASSIFIED, not massaged. The census's value is exactly this willingness.
3. Sources named per row; nothing canonized here — every identity cites the landmark that
   canonized it.

## 4. Wiring

`DISPATCH['PAPER_2253']` loads the artifact AND re-verifies all 52 rational identities live
with Fraction arithmetic on every call, returning the family census, the verification
scoreboard (52/52 required), the printed-precision reclassification record, and the P2252
zero-split. Gate pins: the 52/52 live verification, the artifact row count, the family
count, the rem_579 reclassification, and the zero-split figures.

## NOT REPLACEMENT

The identity lattice is the framework's own arithmetic; the census verifies it against
itself with zero tolerance and separates what is rational-exact from what is
precision-matched. Honest classes, honestly divided.

---

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.
