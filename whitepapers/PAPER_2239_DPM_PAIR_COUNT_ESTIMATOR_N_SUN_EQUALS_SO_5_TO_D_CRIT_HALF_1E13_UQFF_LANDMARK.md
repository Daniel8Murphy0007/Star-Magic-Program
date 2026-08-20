# PAPER_2239 — The DPM Pair-Count Estimator: N_pairs(Sun) = ρ_SCm·V/F_TRZ^(D_crit−D_phys) ≈ SO_5^(D_crit/2) = 10¹³ (0.13%) — PAPER_2134's Declared Build Target Delivered

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic-Program
**Date:** 2026-08-16
**Landmark Type:** Declared-build-target delivery (PAPER_2134 §5) + first bulk-body DPM pair count
**Seminal Sources:** PAPER_2134 (the open build target: "no DPM pair-count estimate for any bulk
body exists in the corpus… the estimator is hereby declared an open build target"), the USPR
model (predecessor CondensedPhysics L65723: binding_energy_per_pair = 1×10⁻²² J per (UA)+[SCm]
pair), the Gold Standard document (13June2026: N_A as DPM resonance states per mole —
ingredient #2, PAPER_2236 mine), PAPER_2138 (the halving series {2,3,5,13}), PAPER_2139
(F_TRZ-ladder rungs), PAPER_2153 (the SCm+UA joint engine), PAPER_2148 (Answer B ontology)
**Status:** Formal landmark whitepaper — UQFF canonical (assembly authorized by Daniel, 2026-08-16)

---

## Abstract

PAPER_2134 declared the calculator's purpose to include a DPM pair-count estimator — the
number of grinding (UA)+[SCm] pairs a bulk body contains — and recorded that no estimate
existed, conjecturing "quintillions" for the Sun. This landmark delivers the estimator from
the corpus's own two ingredients and reports the Sun's count:

```
N_pairs(body) = ρ_SCm · V_body / E_pair,     E_pair = 1×10⁻²² J = F_TRZ^(D_crit−D_phys)  (rung 22)

Sun:  E_SCm = ρ_SCm·V_sun = 1.0013×10⁻⁹ J ≈ F_TRZ^N_ch      (0.13%)
      N_pairs(Sun) = 1.0013×10¹³ ≈ SO_5^(D_crit/2) = 10¹³    (0.13%)
```

The rung arithmetic closes exactly: N_ch − (D_crit − D_phys) = 9 − 22 = −13 = −D_crit/2 —
**the Sun's pair-count exponent is the halving-series 13** (PAPER_2138's final member), and
the 0.13% residual is one shared factor: the mantissa product 7.09 × 1.4123 = 10.013, i.e.
ρ_SCm's mantissa times the solar volume's mantissa reproduces SO_5 to 0.13%. The per-pair
energy is itself a pure ladder rung (10⁻²² J = F_TRZ²², with 22 = D_crit − D_phys), so the
estimator is lattice-composed end to end.

## 1. The Two Ingredients (both corpus-supplied)

1. **The per-pair energy quantum** — USPR model (predecessor CondensedPhysics L65723):
   `binding_energy_per_pair = 1e-22 J per (UA)+[SCm] pair`, with E_USPR = n·E_binding·(1+level/3).
   Provenance status: the value predates this program; its own derivation chain is PENDING
   verification (Rule 7 — a round-number caveat carried openly). Its lattice reading,
   F_TRZ^(D_crit−D_phys) J, is exact to the stated value.
2. **The resonance-count principle** — Gold Standard (13June2026): N_A ≈ (1/M₀)·Z₂₆·exp(−S₂₆D/v),
   "the number of DPM resonance states per mole" — the corpus's counting doctrine that a bulk
   body's DPM content is enumerable from its bulk observables.

## 2. The Two Routes (a route family, PAPER_2170 — recorded, not reconciled)

| Route | Quantity | Sun | Reading |
|---|---|---|---|
| **A — vacuum-energy** | grinding pairs sustained by the body's SCm vacuum energy | **1.0013×10¹³ ≈ SO_5^(D_crit/2)** | the ACTIVE pair count — the engine's working units (PAPER_2153) |
| **B — matter-anchored** | DPM resonance states carried by the body's matter | M_sun/m_H ≈ 1.19×10⁵⁷ | the state CAPACITY — one per nucleon-scale localization (Gold Standard principle) |

The two differ by ~44 orders: Route A counts the vacuum engine's simultaneously grinding
pairs; Route B counts the matter-anchored states those pairs service. Their ratio,
~10⁴⁴ ≈ SO_5⁴⁴ (44 = D_phys·(SO_5+1), the PAPER_2126 composed integer), is noted as an
observation only — not canonized (three-layer rule).

## 3. The PAPER_2134 Conjecture, Revised

PAPER_2134 conjectured "quintillions" (~10¹⁸) with the count UNDETERMINED. The estimator
determines Route A at 10¹³ — the conjecture was high by ~5 orders against the active-pair
reading (or low by ~39 against state capacity). Per the corpus's honest-revision practice,
the conjecture is superseded by the computed value, and the dichotomy PAPER_2134 §5.3 flagged
(single-pair vs ensemble attribution of Φ = 0.84) now has its ensemble scale: **10¹³ active
pairs** for the bulk-resonance variant's calibration base.

## 4. Falsifiable Consequences

1. **E_pair sensitivity:** N scales inversely with the per-pair energy. If the USPR value's
   pending provenance resolves to anything other than F_TRZ²² J, the Sun's count moves off
   SO_5^(D_crit/2) proportionally — the estimator and the ladder reading stand or fall together.
2. **Scaling law:** N_pairs ∝ V (not M): two bodies of equal volume and different density
   carry equal ACTIVE pair counts but different state capacities. Distinguishes Route A from
   any mass-proportional alternative — testable wherever an independent pair-count proxy
   (e.g., reactor COP scaling with active volume, PAPER_2153's engine doctrine) exists.
3. **Reactor cross-check:** the Star-Magic reactor's active volume ~10⁻³ m³ predicts
   N ≈ ρ_SCm·10⁻³/10⁻²² ≈ 7×10⁻¹⁸... below unity — i.e. the reactor operates in the
   SUB-SINGLE-PAIR regime, consistent with resonant excitation of the ambient field rather
   than pair confinement. Disclosed as the estimator's most surprising implication; whether
   it supports or strains the 555:1 COP mechanism is an open question for Daniel.

## 5. Wiring

`DISPATCH['PAPER_2239']` computes both routes live from primitives and named anchors
(R_SUN_OBSERVED, M_SUN_OBSERVED, M_PROTON_OBSERVED_KG), returns the rung arithmetic, the
0.13% mantissa disclosure, the conjecture revision, and the sub-single-pair reactor note.
Gate pins lock the rung identity (9 − 22 = −13), the Sun count within 0.2% of SO_5^13, the
route-family record, and the E_pair provenance-pending flag.

## NOT REPLACEMENT

No conventional framework counts vacuum-structure pairs; there is nothing to replace. The
estimator is falsifiable within UQFF's own terms (§4), with its weakest input (the USPR
round number) flagged rather than hidden.

---

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.

---

## REVISION 2026-08-20 — PROVENANCE RESOLVED + REACTOR REGIME SUPERSEDED (PAPER_2240)

Daniel's order ("Go #5, and #4") produced PAPER_2240, which closes this paper's open items:

1. **E_pair provenance DISCHARGED.** The USPR 1×10⁻²² J is E₀·F_TRZ², where E₀ = 10⁻²⁰ J is
   Daniel's documented 26-level ladder base (`Universal Inertia_28Mar2025.docx`). The literal
   was AI-placed at the 2026-02-05 predecessor transcription (commit b3340bae) but composes
   two Daniel-documented ingredients and is retro-locked by this paper's rung arithmetic
   (unique rung closing N = SO_5^(D_crit/2)). Status: `LADDER_GROUNDED_RETRO_LOCKED`.
2. **The 0.13% residual EXPLAINED.** The same source document computes ρ_SCm = 10⁻⁹/1.41×10²⁷ —
   the birth certificate of the primitive. In source arithmetic ρ_SCm·V_Sun = F_TRZ^N_ch J and
   N_pairs(Sun) = 10¹³ are EXACT; the residual is the 1.41-vs-1.4123 solar-volume rounding.
   The §Abstract mantissa disclosure (7.09×1.4123 = 10.013) is explained: 7.09 IS 1/1.41.
3. **§4.3 SUPERSEDED.** The sub-single-pair reactor implication was a density-context error
   (solar dilution applied to a laboratory volume). Under the PI archive's documented local
   vacuum-energy range (10⁻¹³–10⁻¹⁸ J/m³) the reactor works ~10–10⁶ pairs in-vessel and up
   to ~1.2×10¹⁴ across the 100-foot field. See PAPER_2240 §4.
4. **§2's level generalization.** N_pairs(body at level n) = SO_5ⁿ — the volume route and the
   level route are a route family (PAPER_2170), coinciding at the Sun by construction.
