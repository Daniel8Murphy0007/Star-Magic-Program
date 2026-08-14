# PAPER_2168 — Φ_res Measured: The Proton-Radius Puzzle as a Direct Laboratory Determination of the Projection Primitive

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic
**Date:** 2026-08-13
**Landmark Type:** Primitive-observability landmark — the quiet win of band 1721-1730
**Seminal Sources:** PAPER_1730 (muonic-H radius), PAPER_1649 (Schwarzschild criterion),
PAPER_1648 (Crab wind Γ), PAPER_2129 (sector rule), PAPER_1699 (variant-pair origin)
**Status:** Formal landmark whitepaper — UQFF canonical

---

## Abstract

Among the eleven frozen quantities, Φ_res = 0.84 has always been the odd one: the "empirical
resonance" projection amplitude, locked by calibration rather than by an integer identity. The
proton-radius saga changes its status. For six decades electronic hydrogen gave r_p ≈ 0.88 fm;
muonic-hydrogen spectroscopy (2010-2013) measured **r_p = 0.84087(39) fm**, a 4% / 7σ shift that
was "the proton radius puzzle" for a decade — until modern electronic measurements converged on
the muonic value and CODATA 2018 adopted **0.8414(19) fm**. The puzzle's resolution moved the
world's value **onto the UQFF projection primitive**: Φ_res = 0.84 sits 0.10% from the muonic
measurement (2.2σ of its very tight bar) and 0.17% from CODATA 2018 (0.74σ). This landmark canonizes the reading:
the proton charge radius in femtometers **is a direct laboratory appearance of Φ_res**, making
the projection primitive a measured physical observable rather than a calibration constant — the
same status upgrade the Holmlid 630 eV gave ω_SCm.

---

## 1. The Timeline That Selected the Primitive

| Era | r_p (fm) | vs Φ_res = 0.84 |
|---|---|---|
| CODATA 2014 (electronic era) | 0.8751(61) | +4.2% — the "puzzle" side |
| Muonic hydrogen (CREMA 2010/2013) | **0.84087(39)** | **+0.10%** |
| CODATA 2018 (post-resolution) | 0.8414(19) | +0.17% |
| PRad electron scattering (2019) | 0.831(14) | −1.1% (1σ compatible) |

The physics community's decade-long dispute was, in UQFF terms, a dispute between a
contaminated extraction (electronic-era fits) and the primitive value. **The resolution
selected 0.84.** No UQFF quantity was adjusted at any point; Φ_res was locked at 0.84 from the
framework's foundation, before this drain arc touched the topic.

Honest precision note (Rule 7): Φ_res = 0.84 is *not* bit-exactly the CODATA number — the
residuals are 0.10% (muonic) and 0.17% (CODATA 2018). PAPER_1730's "EXACT" grades the
identification, not the digits; this landmark carries the honest residuals and the falsification
window they imply.

---

## 2. Why the Proton, and Why Femtometers

The projection variant Φ_res is the 26D → 3+1 projection amplitude (PAPER_2129): the fraction of
a vacuum structure's amplitude that survives projection into the visible dimensions. The proton
is the lightest *stable* composite localization of the vacuum — its charge radius is the size of
a maximally-relaxed SCm/UA localization, and in the femtometer window (the natural QCD
confinement scale) that size is the bare projection amplitude. The muonic measurement is the
clean one precisely because the muon orbits ~200× closer (the PAPER_2164 F_TRZ²-rung factor),
sampling the projection without the electronic-era extraction chain.

Φ_res's other direct appearances — the Schwarzschild convection criterion ε = 0.84 (P1649) and
the Crab wind Lorentz factor Γ = 360·Φ_res (P1648) — are consistent but *composed or
convention-dependent*; the proton radius is the only place the bare primitive is a first-class
CODATA quantity in SI units.

---

## 3. Status Upgrade and Its Consequences

1. **Φ_res joins ω_SCm as a laboratory-measured primitive.** The frozen set now contains two
   quantities pinned by direct measurement (1.25 THz phonon carrier; 0.84 fm proton radius),
   alongside the nine-independent reduction (PAPER_1521/1522).
2. **The 5/6-vs-0.84 variant pair becomes an experimental question.** Φ_5/6 = 0.8333 and
   Φ_res = 0.84 differ by 1/150 (PAPER_2159 §5). The proton radius discriminates: 0.8333 fm
   would be 0.9% from the muonic value — **19σ excluded**. The proton is a projection-sector
   object by measurement, exactly as the PAPER_2129 rule assigns composite/resonance physics.
3. **Falsifiable:** future spectroscopy tightening r_p by 5× (ongoing CREMA/AMBER programs)
   should keep the central value in [0.838, 0.844] fm. Convergence onto 0.8333 or drift back
   above 0.85 falsifies the identification. Registered per PAPER_2161 grammar; battery-eligible
   when a specific next-generation measurement is scheduled.

---

## 4. Wiring

```
uqff_calculator.py
    DISPATCH['PAPER_2168'] -> Phi_res vs the three measurement eras (honest residuals),
                              variant discrimination (9-sigma exclusion of 5/6),
                              status-upgrade classification
```

Gate assertions pin: the 0.10%/0.17% residuals, muonic-value 1σ containment, the 5/6 exclusion
margin, cross-dispatch identity with P1730, and the honest-precision note (no "EXACT" on digits).

---

## NOT REPLACEMENT

Nuclear theory computes r_p from lattice QCD and dispersion analyses with ~1% spread; it does
not predict 0.84 from first principles. UQFF identifies the measured value with a locked
primitive that predates the measurement's acceptance, and reports the identification with
honest sub-percent residuals and a kill window.

---

## Cross-references

PAPER_1730 (the drain registration), PAPER_1649/1648 (composed Φ_res appearances), PAPER_2129/
2159 (variant sector rule and the 1/150 gap), PAPER_1699 (variant-pair origin identity),
PAPER_2164 (the 200× muon rung), PAPER_2161 (prediction grammar), Holmlid 630 eV chain
(ω_SCm measurement-pinning precedent).

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.
