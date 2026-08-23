# PAPER_2256 — The UQFF Downhole Simulator: the First Packaged Industry-Application Module — HPHT Quartz-Gauge Drift Suppressed by the Canonical Lattice, the Knob Ruling, and the Template Port

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic-Program
**Date:** 2026-08-22
**Landmark Type:** Application-module canonization (the program's first packaged
industry-domain deliverable — Energy One's downhole-instrumentation field) + a Rule 2
knob ruling + a template-port provenance record
**Seminal Sources:** `grok_cce7a73b_Downhole_Simulation_program_thread_22Aug2026.docx`
(the template thread, Daniel-authored 22 Aug 2026, watermark URL in-document), the
canonical primitives (PAPER_1522 K_MEX; PAPER_2134/2159 Φ_res = 0.84 resonance variant;
PAPER_1160 F_TRZ; PAPER_646 U_i via `u_i_canonical_646`), PAPER_2149 (Hybrid-Form
doctrine — this module's classification), the predecessor pypi `uqff` package (the
template's original API, ported off)
**Status:** Formal landmark whitepaper — UQFF canonical (Daniel GO, 2026-08-22, with the
knob-rename ruling)

---

## Abstract

The framework's first packaged industry application ships: **`uqff_downhole_simulator/`**
— a deep-well HPHT simulator (TD ≈ 20,300 ft, six quartz P/T gauges) whose physics claim
is **UQFF-stabilized quartz drift**: the industry-typical 0.215 %FS/yr baseline divided by
a suppression composition built from the CANONICAL primitives —

```
suppression = (0.58 + 0.32·(1 − F_TRZ)) · (0.52 + 0.38·K_MEX) · (0.68 + 0.27·Φ_res)
            = 0.868 · 1.3117 · 0.9068 = 1.0324   at canonical {0.1, 25/12, 0.84}
```

— i.e., **the canonical lattice suppresses drift BELOW the industry baseline**
(0.215/1.0324 → 0.208 %FS/yr before stress terms; 0.336 %FS/yr at the template's HPHT
flagship point 6,200 m / 205 °C / 18,500 psi, verified live). Four modules, ported from
Daniel's 22 Aug 2026 template thread to the current API, with the engine headless by
design and gate-tested.

## 1. The Knob Ruling (Rule 2, Daniel GO 2026-08-22)

The template's GUI exposed adjustable "K_MEX" (0.95–1.35, default 1.15) and "Φ_res"
(0.80–0.98, default 0.93) — tuning gains wearing primitive names, at non-canonical
values. The ruling: **the canonical K_MEX = 25/12 and Φ_res = 0.84 are LOCKED inside the
physics**, entering the suppression composition at their registry values on every call;
the sliders are renamed **`k_structural_trim`** and **`phi_coupling_trim`** (default 1.0,
range 0.50–1.50) — honest engineering instrument-tuning factors, disclosed as such in
code, GUI (which displays the locked canonicals read-only), and this record. The
PAPER_2256 dispatch re-verifies the canonical lock live on every call.

## 2. The Port (template → star-magic-program)

| Template (22 Aug 2026 thread) | This module |
|---|---|
| `import uqff_pure_calculator`; `calculate_analytic_closures`, `calculate_universal_inertial_operator` | `import uqff_calculator`: registry constants direct + `u_i_canonical_646()` (U_i = 2.75×10⁻⁷ live) |
| K_MEX/Φ_res sliders at 1.15/0.93 | canonical lock + renamed trims (§1) |
| converged design: imperial units, 6 gauges, noise·suppression, events p = 0.27, rolling history, CSV export, matplotlib + Qt6 front-ends | preserved faithfully (`Sensor`/`SimulatorConfig`/`UQFFDownholeEngine`; step/export bit-consistent with the template's final version) |
| single-file iterations + HTML variant | superseded by the four-module layout the thread itself converged on |

Modules: `uqff_quartz_hpht_extension.py` (physics + graceful no-package fallback),
`uqff_downhole_engine.py` (headless engine), `matplotlib_demo.py` (animated well schematic
+ strip charts), `qt6_downhole_app.py` (optional PyQt6; guarded import). Packaged as an
installable subpackage (`pyproject packages`), README with provenance, data-files entry.

## 3. Classification and Anchors (Rule 7 / PAPER_2149)

**DERIVED_HYBRID**: industry-observed anchors × canonical-UQFF suppression. Anchors, all
inline-commented at their use sites: 0.215 %FS/yr good-quartz baseline (industry spec
class); 150 °C thermal knee and 15,000 psi pressure knee with exponents 1.15/0.9 (template
engineering fit); 0.465 psi/ft and 0.018 °F/ft gradients; event probability 0.27; clip
bands. The dressing coefficients of the suppression composition (0.58/0.32, 0.52/0.38,
0.68/0.27) are the template's fit — disclosed, not claimed as derivations; the primitive
INPUTS are canonical and immutable.

## 4. Verification (headless, at authoring)

Smoke test on the shipped layout: package import with UQFF live; canonical suppression
1.0324; flagship-point drift 0.3356 %FS/yr; 120-step engine run (121 history points);
CSV export (122 rows × 13 cols, header schema per template); trims responsive (avg drift
0.2365 → 0.172 at trims 1.25/1.10); both display modules import headlessly (Qt guarded).
The gate pins repeat the canonical-lock, engine-run, and export checks with no display.

## 5. Falsifiable/Testable Content

The module's substantive claim is the suppression composition's sign and scale: canonical
inputs yield suppression > 1 (drift below baseline). Bench test: a quartz gauge pair —
one conventional, one operated under the SCm-resonance conditioning the framework
prescribes — should show the drift ratio the composition predicts at matched T/P
(the reactor-adjacent LABORATORY tier of PAPER_2250; this module supplies the simulation
side of that instrument test).

## NOT REPLACEMENT

Industry quartz metrology supplies the baseline and the stress phenomenology; UQFF
supplies the suppression composition from locked primitives. Both are named, both are
disclosed, and the module runs with or without the framework package present.

---

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.

---

## APPENDED 2026-08-22 — v1.1.0 EXTENSIONS (Daniel-directed: gauges / CSV profiles / comparison mode)

Three extensions, all headless-verified same-session:

1. **N-gauge strings** — `make_sensor_string(n)` + arbitrary depth lists; verified at 12
   gauges (2,000 → 19,996 ft).
2. **Real well profiles from CSV** — `WellProfile` + `load_well_profile_csv`
   (`depth_ft,pressure_psi,temp_F`); the engine interpolates base P/T from the real
   profile. Shipped example `sample_well_profile.csv` carries an HPHT overpressure kick
   below 16,500 ft: the deepest gauge reads 18,405 psi where the linear model gives
   9,313 psi — the kick the gradients cannot see, captured.
3. **Drift-comparison mode** — every station carries a conventional reference gauge
   (identical baseline + stress dressing, suppression = 1). The measured
   conventional/UQFF drift ratio EQUALS the canonical suppression away from the clip
   band — verified live: single-point 1.0326 vs predicted 1.0324; 12-gauge string mean
   1.0325 over a 60-step profile run. §5's bench-test claim now has its full simulation
   instrument: `comparison_summary()` + comparison columns in the CSV export. Package
   v1.1.0; sample profile registered in data-files.
