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

## v1.2.0 extension: service-life drift accumulation (Daniel-directed, 2026-08-23)

`uqff_service_life.py` turns the instantaneous drift RATES into accumulated
gauge ERROR over months/years of simulated service — the divergence curves a
real bench test or field trial would record. Twin legs at every station (UQFF
vs conventional), optional periodic recalibration resets, optional small
random-walk component (seeded, deterministic at 0), CSV divergence-curve
export. Anchors: 30,000 psi HPHT full-scale class; 0.5 %FS total-error spec
budget (both inline-commented).

`divergence_summary()` reports, per sensor: both rates, the predicted
separation rate (%FS/yr and psi/yr), the measured final separation, the
accumulated-error ratio against the canonical suppression (converges to
1.0324 at unity trims), and the service-life arithmetic — years to error
budget for each leg and the extra service life the suppression buys.
Default 6-gauge well, 5 years: separation grows 2.0–3.0 psi/yr per station,
10–15 psi at horizon; ratio lands on the suppression. This is the full
simulation instrument for the PAPER_2250 LABORATORY-tier bench test: the
separation you'd measure, not just the ratio you'd predict.

```python
from uqff_downhole_simulator import ServiceLifeConfig, ServiceLifeSimulator
sim = ServiceLifeSimulator(config=ServiceLifeConfig(years=5.0, seed=42)).run()
print(sim.divergence_summary())
sim.export_csv("divergence_curves.csv")
```

## v1.3.0 extension: field-telemetry realism (Daniel-directed, 2026-08-23)

`uqff_telemetry.py` (`TelemetryConfig` / `TelemetryRecorder`) wraps the engine
in what real permanent-gauge telemetry actually looks like: fixed-cadence
timestamped sampling (anchor: 1 reading/min permanent-quartz class), plus a
fault injector with ground-truth masks — telemetry-line burst dropouts
(string-wide MISSING), stuck gauges (electronics freeze, both channels repeat),
and single-sample spikes per channel. Every sample carries a historian-style
quality flag.

On top sits a field-grade QC pipeline, scored against the injected ground
truth: frozen-value detection (identical consecutive samples — precision and
recall 1.0), and a Hampel MAD despiker with a **common-mode veto** — a gauge
fault hits one gauge, a well transient hits the string, so multi-gauge
coincidence or a matching median residual across the other gauges restores the
raw values instead of "cleaning" real physics. Typical seeded 24-h scores:
spike-P precision 0.83–1.0 / recall 0.67–0.88 (misses are sub-threshold
spikes — honestly undetectable), spike-T recall ~1.0 with a ~0.1%
false-alarm floor. `telemetry_summary()` reports uptime, fault counts, and
precision/recall per fault class; `export_csv()` writes a field-historian-style
file (ISO timestamps, raw + flag + cleaned columns, blanks on dropout) — a
ready-made test bench for downhole analysis pipelines.

```python
from uqff_downhole_simulator import TelemetryConfig, TelemetryRecorder
rec = TelemetryRecorder(config=TelemetryConfig(duration_hours=24.0, seed=11)).run()
print(rec.telemetry_summary())
rec.export_csv("field_telemetry.csv")
```

## v1.4.0 extension: depth-sweep case-study mode (Daniel-directed, 2026-08-23)

`uqff_case_study.py` (`CaseStudyConfig` / `depth_sweep` / `case_study` /
`write_markdown`) sweeps a well from top to TD — linear gradients or a real
CSV profile — and reports both drift legs at every depth, the separation in
psi/yr, the HPHT knee crossings, and the extra service life. Headlines
identify **where the UQFF advantage is largest**: the deep hot interval past
the 150 °C / 15,000 psi knees, exactly where gauges are hardest to replace
(default well: 2.04 psi/yr flat below the knees growing to 3.04 psi/yr at
20,000 ft; a 30,000-ft well reaches 4.21 psi/yr).

`write_markdown()` renders the one-page customer-facing case: claim, depth
table, headlines, the twin-gauge bench test to run, and the honest
DERIVED_HYBRID classification note. Also a CLI:

```
python -m uqff_downhole_simulator.uqff_case_study --td 25000 --out case.md
python -m uqff_downhole_simulator.uqff_case_study --profile my_well.csv --name "Well A-7"
```

## v1.5.0 extension: real-datasheet gauge specs (Daniel-directed, 2026-08-23)

`uqff_gauge_specs.py` (`GaugeSpec` / `GAUGE_SPECS` / `load_gauge_spec_json`)
runs the whole stack on a REAL gauge's published numbers instead of the
template anchors. Every spec carries a mandatory `source` citation (an
uncited spec is rejected — Rule 7). Web-verified presets, fetched 2026-08-23:
`geoq177_16k` and `geoq177_30k` from the **GEO PSI GEOQ 177 public
specification table** (Quartzdyne sensor; drift <0.01 %FS/yr; accuracy
±0.02/±0.025 %FS; 177 °C), plus `template_generic` (the v1.0–1.4 default,
labeled as the stressed-service class it is). Sourcing bonus: the ChampionX
Quartzdyne performance page independently confirms the drift-vs-temperature
mechanism with engineering focus at ≥150 °C — external support for the
template's 150 °C knee anchor.

Pass `spec=` to the physics functions, `gauge_spec=` to `SimulatorConfig` /
`CaseStudyConfig`, and service-life picks it up from the engine (full scale
included). With no spec, every number is bit-identical to v1.0–1.4.

Honest scale disclosure: the datasheet drift bound is a reference-condition
spec limit ~20× below the template's stressed-service baseline, so absolute
separation shrinks accordingly (0.09–0.16 psi/yr vs 2–3 psi/yr) while the
suppression RATIO (1.0324) is baseline-independent. Case-study reports name
the spec and its citation on every page.

```python
from uqff_downhole_simulator import GAUGE_SPECS, CaseStudyConfig, case_study
cs = case_study(CaseStudyConfig(gauge_spec=GAUGE_SPECS['geoq177_30k']))
```

## v1.6.0 extensions: deviation, batch runs, headless CLI (Daniel-directed, 2026-08-23)

1. **Wellbore deviation (MD/TVD)** — `uqff_deviation.py`: gauges sit at
   MEASURED depth (along the string); pressure and temperature are set by TRUE
   VERTICAL depth. `DeviationSurvey.from_kickoff(md, inclination, td)` builds
   the common vertical-then-tangent shape; `load_deviation_csv` reads real
   survey pairs (`md_ft,tvd_ft`). Attach via `SimulatorConfig(deviation=...)`
   or `CaseStudyConfig(deviation=...)`. On a 60° tangent from 8,000 ft, the
   deepest gauge at MD 20,000 reads 6,525 psi / 327 °F where a vertical model
   claims 9,315 psi / 435 °F — the deviation the vertical model cannot see.
2. **Multi-well batch runs** — `run_batch({name: SimulatorConfig}, steps=N)`
   runs a whole field in one call and returns per-well summaries (drift,
   comparison ratio, deviation, spec) for field-wide studies.
3. **Headless CLI** — `python -m uqff_downhole_simulator <run|service-life|telemetry|case-study>`
   with shared well options (`--td --gauges --profile --spec --kickoff
   --inclination`): every workflow now runs from a shell with no Python code
   and no display.

```
python -m uqff_downhole_simulator run --steps 200 --gauges 8 --out run.csv
python -m uqff_downhole_simulator case-study --td 22000 --kickoff 9000 --inclination 45 --spec geoq177_30k --out case.md
```

## v1.7.0 extension: the tool library (Daniel-directed, 2026-08-23 — first piece of the two-stream build)

`uqff_tool_library.py` generalizes the gauge-spec discipline to the whole
toolstring: a cited catalog (`TOOL_LIBRARY`, 8 entries) of downhole and
surface tools — UQFF/conventional quartz P/T (wrapping the v1.5.0 GaugeSpecs),
a piezoresistive class (drift FORM cited from ChampionX: unpredictable,
exponential in temperature; coefficients disclosed as representative fit),
vibrating-wire, 18-point thermocouple string, DTS fiber, and the **G6 surface
interface (Modbus RS485 + 4-20mA)** — every entry declaring the telemetry
interface it speaks, which is the declaration the live-stream ports/plug-in
layer will implement.

Honesty structure: entries whose existence is verified but whose numbers were
not published are `PARAMETERS_USER_SUPPLIED` — their fields are None and
`drift_model_for()` refuses to invent vendor data. `ToolString` composes
mixed strings of stations; `rating_check()` checks every tool against the
well conditions at its station (profile or gradients, deviation honored) —
it catches a 177 °C gauge hung in the sample well's 217 °C kick zone before
the well does.

```python
from uqff_downhole_simulator import ToolString, rating_check, load_well_profile_csv
ts = ToolString([(3000, 'quartz_pt_uqff_geoq177_30k'), (18200, 'piezoresistive_pt_class')])
print(rating_check(ts, profile=load_well_profile_csv("uqff_downhole_simulator/sample_well_profile.csv")))
```

## v1.8.0 extension: the ports/plug-in layer (Daniel-directed, 2026-08-23 — two-stream build, piece 2)

`uqff_ports.py` — READ-ONLY taps ingesting live-stream data into the
normalized `LiveStream` form the reconciler will consume (index = time or
depth; per-channel values with NaN for missing; quality flags carried; units
carried). `PORT_REGISTRY` with explicit statuses: **IMPLEMENTED** —
`historian_csv` (wide-format historian exports, auto-detecting the v1.3.0
telemetry layout) and `las2` (LAS 2.0 well logs, CWLS public standard, NULL
substitution, wrapped mode refused rather than mis-parsed); **DECLARED** —
`modbus_g6` (the tool library's declared port target), `witsml`, `opcua` —
these name the protocol but REFUSE to run until real site details exist (no
invented site behavior). `register_port()` lets a site plug in its own reader
additively.

The proof loop: the simulator's own v1.3.0 field-style export re-ingested
through the port matches the recorder's arrays to export precision, with
MISSING → NaN and flags carried — closed stream → simulated live file →
port → same numbers. The ingest path is verified in simulation before it
ever touches a site. CLI: `python -m uqff_downhole_simulator ingest --file
field.csv` (or `--port las2`).

## v1.9.0 extension: the two-stream reconciler (Daniel-directed, 2026-08-23 — piece 3, the architecture complete)

`uqff_reconciler.py` — the coordinator. The closed stream predicts what every
gauge in a described well *should* read; a `LiveStream` delivers what it
*does* read; the reconciler works the per-station offset series and
classifies each: IN_FAMILY, CALIBRATION_OFFSET (bias recovered),
DRIFT_CONSISTENT (trend inside the closed stream's own drift envelope
[UQFF rate, conventional rate] at station T/P — needs ≥18 days of data,
below that slopes are noise and it says so), TRANSIENTS, or
**UNEXPLAINED_OFFSET/TREND — the undervalued streams**. Thresholds are
disclosed engineering heuristics; labels are advisory triage and the numbers
(bias, slope, sigma, envelope) always ride along.

Validated on four scenarios: clean well → 6/6 IN_FAMILY; +50 psi biased
gauge → CALIBRATION_OFFSET, 50.09 psi recovered; 2-year synthetic drifting
at the conventional rate → DRIFT_CONSISTENT (slope 82.45 vs envelope
[79.71, 82.29] psi/yr); and **the find** — the kick well reconciled against
a linear-gradient assumption flags 610 / 4,448 / 6,083 psi unexplained
offsets at the deep stations. The closed stream exposes what the assumed
model cannot see.

```python
from uqff_downhole_simulator import Reconciler, SimulatorConfig, ingest
report = Reconciler(SimulatorConfig(td_ft=18500)).reconcile(ingest("field.csv"))
print(report['undervalued_streams'])
```

CLI: `python -m uqff_downhole_simulator reconcile --file field.csv --td 18500`
