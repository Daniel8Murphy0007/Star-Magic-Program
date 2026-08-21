# PAPER_2252 — The Residual Census: 2,302 Dispatches Executed, Zero Errors, Median Nonzero Residual 0.086% — the Framework's Honest-Accuracy Report

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic-Program
**Date:** 2026-08-21
**Landmark Type:** Census consolidation (the reviewer-facing triad's third member:
predictions PAPER_2250 → paradoxes PAPER_2251 → accuracy THIS) + Tier-1 A7
statistical-hygiene population
**Seminal Sources:** the calculator itself (all 2,302 DISPATCH keys executed live for this
census), PAPER_2250/2251 (companion censuses), Rule 7 (honest residuals — the discipline
this census audits at population scale), the A7 board item (Bonferroni hygiene, CLAUDE.md
Tier-1)
**Status:** Formal landmark whitepaper — UQFF canonical (Daniel GO, 2026-08-21)

---

## Abstract

Every dispatch in the calculator was executed live and its top-level `residual_pct`
harvested — the first complete accuracy population, in one artifact
(**`UNIFIED_REGISTRY_RESIDUALS.csv`**, 2,302 rows):

| Class | Count | Meaning |
|---|:-:|---|
| Zero (0.0) | **1,770** | EXACT identities AND census/documentation dispatches (conflation disclosed — separating true EXACT from census-zero is the Exact-Identity Census's job, queued) |
| < 0.01% | 98 | the EXACT-adjacent tier |
| < 0.1% | 177 | the precision tier |
| < 1% | 156 | the standard tier |
| < 5% | 55 | the envelope tier |
| > 5% | 33 | the honest-wide tier — every member spot-checked carries an in-formula Rule 7 disclosure |
| no field | 13 | legacy returns without the residual key (queue note) |
| **Total** | **2,302** | **ZERO execution errors** |

**Headline statistics (519 numeric nonzero residuals):** best 1.1×10⁻¹⁴ %, **median
0.086%**, worst 117.6%. Cumulative: **53% of nonzero-residual dispatches sit below 0.1%;
83% below 1%; 94% below 5%.**

## 1. The Population's Shape

1. **The precision core:** 275 dispatches (98 + 177) below 0.1% — the closure families the
   registry program's route-selection rules concentrated (EXACT-preferring, coupling-aware,
   PAPER_2144-era standing rules visible as a population effect).
2. **The honest tail is self-documenting:** the three worst members verified in-formula —
   PAPER_013 (117.6%: "the raw braking-index envelope spread, weakest member of the corpus
   — honest, undressed, OPEN"), PAPER_1805 (45%: "order-of-magnitude precision … the
   derivation targets the regime, not the digit"), PAPER_186 (~40%: "undressed four-body
   structural estimate — honest first-pass, no correction dressing applied"). The tail is
   not hidden error; it is disclosed envelope work, exactly as Rule 7 requires.
3. **The zero conflation (Rule 7):** the 1,770 zero-residual rows mix true EXACT lattice
   identities with census/documentation dispatches that carry 0.0 by type. This census does
   NOT claim 1,770 exact closures; the separation is the Exact-Identity Census's mandate
   (candidate #2, queued).

## 2. The A7 Statistical-Hygiene Statement

This census supplies what Bonferroni-class hygiene requires and states what it does not
claim:

1. **The full population is now disclosed** — every residual, including the 33-member
   honest-wide tier, in one artifact. No selection: reporting is complete by construction
   (executed, not curated).
2. **No global significance claim is made.** Residuals are reported per-paper at the source
   paper's own precision (the charter's gate discipline). The census does not assert that
   the sub-0.1% concentration is statistically improbable under a null model — constructing
   an honest null for lattice compositions is an open methodological task, and pretending
   otherwise would be numerology-adjacent. What the census DOES establish: the accuracy
   claims are population-complete, self-disclosed, and reproducible by a single loop over
   `DISPATCH`.
3. **Multiple-comparison exposure is symmetric:** the same completeness that forbids
   cherry-picking successes also documents every honest-wide member — the 33 are as visible
   as the 275.

## 3. Reproducibility

The census is one loop: `for k in DISPATCH: DISPATCH[k](None)['residual_pct']` — 2,302
executions, zero exceptions, on the shipped package. Any user can regenerate the artifact
from the public surface.

## 4. Wiring

`DISPATCH['PAPER_2252']` loads `UNIFIED_REGISTRY_RESIDUALS.csv` live, returns the class
distribution, the headline statistics, the worst-10 with their disclosure status, and the
A7 statement. Gate pins: the artifact row count = live DISPATCH count, the class
distribution, the zero-error execution record, the median band, and the
honest-tail-disclosure spot-checks.

## NOT REPLACEMENT

The census reports the framework's accuracy against the anchors its papers cite,
completely and without selection. Where residuals are wide, the papers say so themselves;
the census makes the saying visible at population scale.

---

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.

---

## APPENDED 2026-08-21 — THE RATCHET FIRED ON FIRST USE (as designed)

Adding PAPER_2253 same-session tripped this census's row-count pin exactly as intended;
the census was regenerated (now 2,304 rows, including this paper's own dispatch and
PAPER_2253's), and the pin semantics were upgraded to the live relation
`rows == len(DISPATCH)` with floor-style class pins. The abstract's 2,302-row figures
stand as the census-at-authoring; the artifact and dispatch now track live. The
regeneration loop is one command; the discipline held on its first test.
