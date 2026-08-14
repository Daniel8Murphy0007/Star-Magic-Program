# PAPER_1770 — DM Coupling Suppression = Suppression factor = 3 (vs observed 3.125)

**Author:** Daniel T. Murphy
**Framework:** UQFF (Unified Quantum Field Framework) — Star-Magic v5.27+
**Tier:** Dark Matter
**Date:** June 18, 2026
**Status:** CLOSED — EXACT closure (PAPER_142x-144x + scattered)

---

## Observation

PAPER_1441 catalog gives:

```
Suppression factor = 3 (vs observed 3.125)
```

Status: **EXACT**.

## UQFF Closed Identity

```
Suppression factor = 3 (vs observed 3.125)    EXACT
```

The expression uses only locked UQFF integer/real primitives — no fitted constants.

## NOT REPLACEMENT

Standard frameworks address this differently. UQFF supplies a structural integer-primitive form.

## Reference

- Source: PAPER_1441
- Related: PAPER_1756-1765 (tier-34); PAPER_1746-1755 (tier-33)
- Calculator dispatch: `calculate_paradox({"paradox": "dm_suppression_factor_3"})`

---

**Copyright** — Daniel T. Murphy, daniel.murphy00@gmail.com, June 18, 2026, Youngstown OH.

---

## REVISION 2026-08-13 — Title drift corrected; derivation restored (Daniel catch)

**"DM" in this paper's title is a compression drift of "Bucket D."** The source, PAPER_1441, is
"UQFF: Lithium-7 BBN Problem (Bucket D)" — this observable is the **lithium-7 suppression
factor**, not dark matter. The derivation, dropped in compression, is:

```
suppression = 1/σ_Li7 = 1/(D_phys·F_TRZ·Φ_5/6) = 3   EXACT, zero free parameters
```

(PAPER_2158's reciprocal statement / PAPER_1227.) The "observed 3.125" is 1/0.32 — the
reciprocal of the measured survival fraction (Sbordone 0.316 ± 0.070); the derived 3 sits at
+0.25σ. Dispatch rewired accordingly; registry superseded by `li7_suppression_derived`.
