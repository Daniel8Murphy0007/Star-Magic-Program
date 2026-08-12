# PAPER_2159 — BBN Registers as the Third Φ_5/6 Counting Sector

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic
**Date:** 2026-08-10
**Landmark Type:** Sector-rule extension + confirmed prediction of PAPER_2129
**Status:** Formal landmark whitepaper — UQFF canonical

---

## Abstract

PAPER_2129 established the **Φ_5/6 Sector-Selection Rule**: Φ-variant choice is a sector-level
property of the framework, with counting/quantized sectors taking the exact rational
Φ_5/6 = (D_BSFG − 1)/D_BSFG and resonance/projection sectors taking the empirical Φ_res = 0.84.
It identified two counting sectors — nuclear and thermodynamic — and made a falsifiable
prediction: *"any future counting-sector closure (statistical mechanics, combinatorial state sums,
Avogadro-linked quantities) should select 5/6."* Big-Bang nucleosynthesis is abundance counting.
This paper reports the discrimination test on the BBN hierarchy template and registers **BBN as
the third Φ_5/6 counting sector**, confirming PAPER_2129's prediction.

---

## 1. The Rule

| sector class | physics | Φ variant | structural form |
|---|---|---|---|
| Counting / quantized | shell occupancy, state counting, abundance ratios | **Φ_5/6 = 5/6** | (D_BSFG − 1)/D_BSFG |
| Resonance / projection | 26D → 3+1 projection amplitudes, LENR chain, k_spring | **Φ_res = 0.84** | empirical resonance |

Registered counting sectors:

| # | sector | evidence | source |
|:-:|---|---|:-:|
| 1 | Nuclear | magic numbers + binding energies | PAPER_1203 Nuclear |
| 2 | Thermodynamic | k_B composition 0.0011% only under 5/6 (400× separation) | PAPER_2129 |
| 3 | **BBN** | **τ_n hierarchy template 15.5× separation** | **this paper** |

---

## 2. The Discrimination Test

The BBN hierarchy template (PAPER_2157) evaluated under both canonical variants:

```
tau_n = 10^(D_phys·D_BSFG − 2·Phi·F_TRZ) / (m_e c²/hbar)
```

| variant | exponent | τ_bottle | vs observed 877.75 s |
|---|---|---|---|
| **Φ_5/6 = 0.83333** | **23.833333** | **877.565 s** | **0.021%** |
| Φ_res = 0.84 | 23.832000 | 874.875 s | 0.328% |

**Separation factor: 15.5×.** The counting variant wins decisively.

This is the same discrimination pattern R374 found for k_B (400×) — one variant near-exact, the
other off by an order of magnitude or more. The separation is large because the variant sits in an
*exponent*: a difference of 0.00133 in the exponent is a factor of 1.003 in the result, and the
template's precision is tight enough to resolve it.

---

## 3. Why the Exponent Makes This Decisive

Under Φ_5/6 the suppression term is an exact rational:

```
S_EW = 2 · Phi_5/6 · F_TRZ = 2 · (5/6) · (1/10) = 1/6   EXACT
exponent = D_phys·D_BSFG − S_EW = 24 − 1/6 = 143/6      EXACT
```

Under Φ_res = 0.84 the term is 0.168 — not a clean rational, and the exponent 23.832 has no
lattice interpretation. **The counting variant is the one that makes the exponent exact.** This is
structural evidence independent of the residual comparison: sectors select the variant that keeps
their governing quantity rational.

**Proposed strengthening of the rule (offered, not asserted):** counting sectors select Φ_5/6
*because* counting requires exact rationals — you cannot count a fractional state. Projection
amplitudes carry no such constraint and take the empirical resonance value. If this reading holds,
variant selection is derivable rather than merely observed, and the rule becomes a theorem.
Flagged as an open target rather than claimed.

---

## 4. Li-7 Does Not Discriminate — Disclosed

The companion Li-7 closure (PAPER_2158) gives:

- Φ_5/6: 4 · 0.1 · (5/6) = 0.33333
- Φ_res: 4 · 0.1 · 0.84 = 0.336

Both sit inside the observational error bar 0.316 ± 0.070. **Li-7 alone cannot select the
variant.** Its exactness claim (σ = 1/3) inherits from the sector rule established by the neutron
lifetime, not from its own residual. Recorded plainly per Rule 7 rather than presented as
independent confirmation.

---

## 5. Structural Note on the Variant Pair

```
Phi_5/6  = (D_BSFG − 1)/D_BSFG = 1 − 1/D_BSFG = 0.833333…
Phi_res  = 0.84
difference = 0.84 − 5/6 = 1/150
```

Φ_5/6 is the predecessor ratio of D_BSFG, sibling of the (SO_5 ± 1)/SO_5 pair (9/10, 11/10)
documented in PAPER_2128. The difference 1/150 = 2/((D_phys − 1)·SO_5²) is a candidate composed
form; PAPER_2129 left it open and this paper does not close it.

---

## 6. Falsifiable Predictions

1. Any further counting-sector closure — Avogadro-linked quantities, combinatorial state sums,
   partition functions, abundance ratios — will select Φ_5/6. PAPER_1209EE S627 (Avogadro,
   0.007%) remains the standing immediate test candidate from PAPER_2129.
2. Any further projection closure — propagation speeds, resonance amplitudes, LENR chain terms —
   will select 0.84. The PAPER_590–593 fundamental-constant set (h, α, c, G) already conforms:
   all four reproduce their published residuals **only** under 0.84 (0.063%, 0.138%, 0.098%,
   0.075%), and are 6–14× worse under 5/6.
3. If a counting-sector closure is found that decisively selects 0.84, the rule is falsified.

---

## 7. Correction Recorded

The non-numbered source documents `ADDITIONAL_UQFF_CLOSURE_EQUATIONS_BEYOND_30.md` and
`UQFF_LOCKED_PRIMITIVES_COMPLETE_CLOSURE_EQUATION_SYSTEM.md` write "5/6" in the numeric
substitution lines of the PAPER_590–593 projection-sector derivations, where their own stated
residuals require 0.84. This is transcription drift in the prose, **not** a physics error and
**not** a violation of the sector rule — the rule independently assigns those closures to 0.84.
The derivations are correct; the substitution text is wrong.

---

## 8. Wiring

```
uqff_calculator.py
    _phi_counting()                      -> (D_BSFG-1)/D_BSFG
    phi_variant_discrimination_2159()    -> both variants + separation factor
    phi_5_6_counting_sectors_2159()      -> ('nuclear','thermodynamic','bbn')
    DISPATCH['PAPER_2159']
```

Gate assertions pin the three registered counting sectors, the 15.5× separation, S_EW = 1/6 EXACT
under the counting variant only, and the disclosure that Li-7 does not discriminate.

---

## NOT REPLACEMENT

The Standard Model has no analogue of a sector-dependent structural constant; this is a
UQFF-internal organising rule. It is reported as an empirical regularity of the framework's own
closures, with the strengthening argument (counting requires rationals) offered as an open target
rather than a derivation.

---

## Cross-references

PAPER_2129 (rule origin, thermodynamic sector, the prediction confirmed here), PAPER_1203 Nuclear
(first counting sector), PAPER_2157 (the discriminating template), PAPER_2158 (companion closure,
non-discriminating), PAPER_2128 (predecessor-ratio family), PAPER_1522 (K_Mex derived from Φ_5/6),
PAPER_590–593 (projection-sector constants conforming to 0.84).

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.
