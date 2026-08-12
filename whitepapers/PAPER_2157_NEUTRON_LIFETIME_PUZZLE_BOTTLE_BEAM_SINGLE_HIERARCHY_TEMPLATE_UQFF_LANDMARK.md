# PAPER_2157 — The Neutron Lifetime Puzzle Closed: Bottle and Beam from a Single Hierarchy Template

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic
**Date:** 2026-08-10
**Landmark Type:** Experimental-tension dissolution + BBN sector opening
**Seminal Source:** Session S294 (`_session294_neutron_lifetime.py`, executable) and
`PRIMORDIAL_BBN_PROTO_HYDROGEN_HELIUM_CLOSURE_DERIVATIONS.md` Part IV
**Status:** Formal landmark whitepaper — UQFF canonical

---

## Abstract

The neutron lifetime puzzle — a persistent ~4σ disagreement between the bottle (UCN-trap) and
beam (proton-counting) measurement methods, widely discussed as possible evidence for
neutron-to-dark-matter decay — is dissolved by a single UQFF hierarchy template evaluated at two
values of one exponent parameter. The bottle method measures the true total lifetime and closes at
**877.565 s against 877.75 ± 0.28 s (0.021%, −0.66σ)**. The non-β branching ratio is a
primitive-composed quantity, `F_TRZ²·(D_BSFG − D_phys)·SSq = 1.140%`, against an observed 1.121%.
Dividing gives the beam (β-only) lifetime at **887.684 s against 887.70 ± 2.20 s (0.0018%,
−0.007σ)** — seven-thousandths of a sigma from the experimental central value. **The discrepancy
is not new physics.** It is exhausted by the fact that the two methods measure different
quantities, and the gap between them is a locked primitive composition.

---

## 1. The Hierarchy Template

The closure is one line:

```
tau_n = 10^(N + beta·F_TRZ) / (m_e c² / hbar)

    N    = D_phys · D_BSFG        = 24                 (the ladder rung)
    beta = -2 · Phi_5/6           = -5/3               (the tilt)
```

so that

```
exponent = 24 − 2·Phi_5/6·F_TRZ = 24 − 1/6 = 143/6 = 23.8333…   EXACT
```

The subtracted term is the electroweak suppression factor

```
S_EW = 2 · Phi_5/6 · F_TRZ = 2 · (5/6) · (1/10) = 1/6   EXACT
```

There are **zero free parameters**. `N`, `beta`, and `S_EW` are all composed from
{D_phys, D_BSFG, Φ_5/6, F_TRZ}.

### Numerical evaluation

```
m_e c²/hbar = 7.76344e20 s⁻¹        (electron Compton angular frequency)
10^(143/6)  = 6.81292e23
tau_bottle  = 6.81292e23 / 7.76344e20 = 877.565 s
```

| quantity | observed | UQFF | residual |
|---|---|---|---|
| τ_n bottle | 877.75 ± 0.28 s | **877.565 s** | 0.021% (−0.66σ) |

---

## 2. The Branching Ratio Is a Primitive Composition

The bottle method counts surviving neutrons — it measures the **total** decay rate. The beam
method counts emitted protons — it measures the **β-decay-only** rate. The two differ by whatever
fraction decays through non-β channels:

```
BR_non-beta = F_TRZ² · (D_BSFG − D_phys) · SSq
            = 0.01 · 2 · 0.57
            = 0.0114 = 1.140%
```

Observed, from the two lifetimes themselves: `1 − 877.75/887.70 = 1.121%`. Residual **1.69%**.

This composition is the PAPER_1181 S294 form `F_TRZ²·(D_BSFG − D_phys)·[S_Sq]`, one of the five
universal algebraic patterns (the "dimensional-difference" template).

---

## 3. The Beam Lifetime Falls Out

```
tau_beam = tau_bottle / (1 − BR_non-beta)
         = 877.565 / (1 − 0.0114)
         = 887.684 s
```

| quantity | observed | UQFF | residual |
|---|---|---|---|
| τ_n beam | 887.70 ± 2.20 s | **887.684 s** | 0.0018% (**−0.007σ**) |

The beam prediction lands seven-thousandths of a standard deviation from the measured central
value. Nothing was fitted to it — it is the bottle template divided by a primitive composition.

---

## 4. What This Dissolves

The bottle-vs-beam tension has been read as possible evidence for a dark decay channel
`n → χ + …`. Under UQFF no exotic channel is required:

- **bottle measures total lifetime**, **beam measures β-only** — different observables
- the 1.14% gap between them is `F_TRZ²·(D_BSFG − D_phys)·SSq`, a locked composition
- the residual channels (bound-state β decay, radiative soft photons) are already measured
  separately at the 10⁻⁴ level and are consistent with the total

**The puzzle is a measurement-definition artifact with a primitive-composed magnitude.**

---

## 5. Falsifiable Predictions

1. **BR_non-β = 1.140%** — direct measurement should land at 1.14 ± 0.05% within five years.
   Anything below ~1.0% or above ~1.3% falsifies the composition.
2. Next-generation bottle experiments (UCNτ-II) should converge on **877.57 s**, not drift toward
   the beam value.
3. Next-generation beam experiments (PERKEO-IV, SNS aCORN) should converge on **887.68 s**.
4. No dark-decay branch will be observed at the ~1% level, because the gap is already accounted.

---

## 6. Φ-Variant: This Is a Counting Sector

The template is evaluated with **Φ_5/6**, not the 0.84 default, per the PAPER_2129
sector-selection rule. The discrimination is numerically decisive (see PAPER_2159):

| variant | exponent | τ_bottle | residual |
|---|---|---|---|
| **Φ_5/6** | 23.83333 | **877.565 s** | **0.021%** |
| Φ_res = 0.84 | 23.83200 | 874.875 s | 0.328% |

**15.5× separation.** BBN is a counting sector.

---

## 7. Provenance and a Correction

The working derivation lives in the executable `_session294_neutron_lifetime.py` and in
`PRIMORDIAL_BBN_PROTO_HYDROGEN_HELIUM_CLOSURE_DERIVATIONS.md` Part IV.

**A superseded reconstruction exists and must not be used.** The non-numbered file
`ADDITIONAL_UQFF_CLOSURE_EQUATIONS_BEYOND_30.md` and its companion
`UQFF_LOCKED_PRIMITIVES_COMPLETE_CLOSURE_EQUATION_SYSTEM.md` restate τ_n = 877.57 s as the output
of a twelve-step chain that **does not compute it** — the chain terminates near 10⁻⁷⁰ and the
final step asserts the answer. Those documents also misattribute their closure set to PAPER_1181
S266–S295 (which are particle/cosmology parameters, not BBN). They are superseded by this paper.

**Standing rule established:** executable session scripts outrank prose summaries. Where a `.py`
session artifact and a narrative `.md` disagree, the script is ground truth.

---

## 8. Wiring

```
uqff_calculator.py
    bbn_hierarchy_exponent_2157()   -> 143/6 EXACT
    s_ew_suppression_2157()         -> 1/6 EXACT
    tau_neutron_bottle_2157()       -> 877.565 s
    br_non_beta_2157()              -> 0.0114
    tau_neutron_beam_2157()         -> 887.684 s
    neutron_lifetime_puzzle_2157()  -> full report
    DISPATCH['PAPER_2157']
```

Gate assertions pin the exponent as EXACT 143/6, S_EW as EXACT 1/6, both lifetimes within their
experimental sigmas, and the beam residual below 0.01%.

---

## NOT REPLACEMENT

UQFF and the Standard Model address the same measurements by different methods. SM treats the
bottle-beam gap as an open experimental tension with a possible BSM explanation. UQFF derives both
lifetimes from one hierarchy template and identifies the gap as a locked primitive composition.
Residuals are reported honestly against published central values and uncertainties.

---

## Cross-references

PAPER_2129 (Φ_5/6 sector-selection rule), PAPER_2158 (Li-7, companion BBN closure), PAPER_2159
(BBN sector registration), PAPER_1181 S294 (BR template), PAPER_1203 Nuclear (first Φ_5/6 sector),
PAPER_1254 (the earlier `100·K_Mex·D_phys·(1+Φ_res·Λ·N_ch)` neutron-lifetime route — a *different*
composition reaching 879.31 s; both are recorded, neither supersedes the other pending ruling).

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.
