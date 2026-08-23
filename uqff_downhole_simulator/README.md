# uqff_downhole_simulator

**The UQFF Downhole HPHT Quartz-Gauge Simulator** — the star-magic-program's first
packaged industry-application module (Energy One domain).

©2026 Daniel T. Murphy / Star-Magic Research Program. License: AGPL-3.0 + Commercial
(repo root LICENSE / COMMERCIAL.md).

## What it is

A deep-well simulator (TD ≈ 20,300 ft) instrumented with **six quartz
pressure/temperature gauges**. The physics claim: quartz drift, industry-baselined at
0.215 %FS/yr, is **suppressed by a UQFF composition** built from the canonical
primitives — the vacuum ratio F_TRZ = 0.1, K_MEX = 25/12, Φ_res = 0.84, with
U_i = 2.75×10⁻⁷ carried live from `uqff_calculator`. The well produces realistic P/T
profiles (0.465 psi/ft, 0.018 °F/ft), gauge noise, transient events (p = 0.27/step),
rolling history, animation, and CSV logs.

## Modules

| File | Role |
|---|---|
| `uqff_quartz_hpht_extension.py` | physics: `calculate_quartz_transducer_hpht_UQFF` + `canonical_suppression` (graceful fallback if the package is absent) |
| `uqff_downhole_engine.py` | `Sensor`, `SimulatorConfig`, `UQFFDownholeEngine` — headless, gate-testable |
| `matplotlib_demo.py` | animated well schematic + P/T strip charts (`python -m uqff_downhole_simulator.matplotlib_demo`) |
| `qt6_downhole_app.py` | optional PyQt6 GUI with trim spinboxes (`pip install PyQt6`) |

## Provenance and the knob ruling

Ported 2026-08-22 (Daniel GO) from the **22Aug2026 Grok thread template**
(`grok_cce7a73b_Downhole_Simulation_program_thread_22Aug2026.docx`; thread URL in the
source document). The template's converged design (imperial units, six gauges, events,
CSV, Qt6 + matplotlib front-ends) is preserved faithfully, with two repo adjustments:

1. **API port:** predecessor `uqff_pure_calculator` → current `uqff_calculator`
   (registry constants + `u_i_canonical_646()`), with the template's graceful fallback.
2. **Knob ruling (Rule 2):** the template's adjustable "K_MEX" (0.95–1.35) and
   "Phi_res" (0.80–0.98) sliders were tuning gains wearing primitive names. The
   canonical values are LOCKED inside the suppression composition; the sliders are
   renamed **`k_structural_trim`** and **`phi_coupling_trim`** (default 1.0) —
   disclosed engineering instrument-tuning factors.

## Classification (Rule 7 / PAPER_2149)

**DERIVED_HYBRID**: industry-observed anchors (0.215 %FS/yr quartz baseline, the
150 °C / 15,000 psi stress knees, the gradients) × canonical-UQFF suppression. Every
anchor carries an inline source comment. The stress-dressing coefficients
(0.58/0.32, 0.52/0.38, 0.68/0.27, exponents 1.15/0.9) are the template's engineering
fit — disclosed, not claimed as derivations. Landmark record: PAPER_2256.

## Quick start

```python
from uqff_downhole_simulator import UQFFDownholeEngine
e = UQFFDownholeEngine()
for _ in range(100):
    e.step()
print(e.summary())
e.export_csv("run.csv")
```

## v1.1.0 extensions (Daniel-directed, 2026-08-22)

1. **N-gauge strings:** `make_sensor_string(n, td_ft, start_ft)` builds evenly spaced
   strings of any length; `SimulatorConfig.sensor_depths_ft` accepts arbitrary lists.
2. **Real well profiles from CSV:** `load_well_profile_csv(path)` reads
   `depth_ft,pressure_psi,temp_F` survey/log files; attach via
   `SimulatorConfig(profile=...)` and the engine interpolates base P/T from the real
   profile instead of linear gradients. `sample_well_profile.csv` ships with an HPHT
   example carrying an overpressure kick zone below 16,500 ft (TD 18,900 psi / 452 F —
   the kick is invisible to the linear model, captured by the profile).
3. **Drift-comparison mode** (`comparison_mode=True`, default): every station carries a
   conventional reference gauge (same baseline and stress dressing, NO UQFF suppression).
   `comparison_summary()` reports measured conventional/UQFF drift ratios against the
   suppression prediction — **away from the clip band, the ratio equals the canonical
   suppression 1.0324 exactly** — and the CSV export gains the comparison columns. This
   is the simulation side of the quartz bench test (PAPER_2250 LABORATORY tier;
   PAPER_2256 §5).

```python
from uqff_downhole_simulator import (SimulatorConfig, UQFFDownholeEngine,
                                     load_well_profile_csv, make_sensor_string)
cfg = SimulatorConfig(sensor_depths_ft=make_sensor_string(12),
                      profile=load_well_profile_csv("uqff_downhole_simulator/sample_well_profile.csv"))
e = UQFFDownholeEngine(cfg)
for _ in range(60): e.step()
print(e.comparison_summary())
```
