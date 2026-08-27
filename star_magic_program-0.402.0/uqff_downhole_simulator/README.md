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

## Connectivity status (formal statement, 2026-08-24)

An independent assessment (2026-08-24) correctly noted this package has **no
live connection capability** — no network protocol clients, drivers, polling,
or real-time acquisition — and partially-stale noted that it "only simulates"
telemetry. The honest tier ladder, so nothing is oversold or undersold:

| Tier | Status | What it means |
|---|---|---|
| SIMULATE | ✅ built (v1.3.0) | synthetic field telemetry with faults, flags, scored QC |
| OFFLINE-INGEST | ✅ built (v1.8.0) | **real** sensor data via exported files: historian CSV, LAS 2.0, `register_port()` site readers — reconciler runs on real data |
| FILE-FOLLOW (quasi-live) | ✅ built (v1.10.0) | `HistorianFollower` polls a continuously-appended historian export and reconciles new samples — near-real-time with zero network code |
| LIVE PROTOCOL | 🟡 tier 4 real code (v1.11.0) | `modbus_g6` is a REAL pymodbus TCP client (optional `pip install pymodbus`; READ-ONLY; citation-mandatory register maps; loopback-verified) awaiting site config; witsml / opcua remain declared-refusing |

The workflow the assessment prescribes — export well surveys, gauge
inventories, and historical readings from your SCADA/historian into CSV and
feed them in — is exactly tiers 2–3, already built and gate-verified.

## v1.10.0 extension: the file-follower (Daniel-directed, 2026-08-24)

`uqff_follower.py` — `HistorianFollower(path, reconciler=...)` watches a
growing historian export READ-ONLY: `poll()` re-ingests and diffs by sample
count (robust by construction against partial lines and file rotation, which
is detected and reported); `poll_and_reconcile()` runs the two-stream
reconciliation whenever new samples arrive; `watch()` is a caller-scheduled
generator (the library never blocks on its own). Verified: 60 → +30 samples
followed and reconciled 6/6 IN_FAMILY per poll; quiet poll does nothing;
rotation resets; missing file is a soft error.

```python
from uqff_downhole_simulator import HistorianFollower, Reconciler, SimulatorConfig
f = HistorianFollower("historian_export.csv", reconciler=Reconciler(SimulatorConfig()))
for poll in f.watch(interval_s=60.0):
    r = f.poll_and_reconcile()
    if r['reconciliation'] and r['reconciliation']['undervalued_streams']:
        print("FOUND:", r['reconciliation']['undervalued_streams'])
```

## v1.11.0 extension: the Modbus client (Daniel GO, 2026-08-24 — tier 4 real code)

`uqff_modbus.py` — a real Modbus TCP client (`ModbusHistorianTap`) behind the
guarded optional dependency `pip install pymodbus` (same pattern as PyQt6; the
package runs fully without it, the port refuses with the pip hint). READ-ONLY
by construction: only read_holding/read_input calls exist. Register maps are
user-supplied JSON with a MANDATORY source citation — no public G6 register
map exists in the fetched sources, so none is shipped; the included
`example_register_map.json` is labeled EXAMPLE_TEST_FIXTURE and describes the
in-process loopback server used for verification. Decoding is raw-`struct` on
the 16-bit registers (word order from the map), stable across pymodbus
versions. Loopback-verified: a real TCP client polled an in-process pymodbus
server and decoded float32/uint16 registers exactly, emitting the same
LiveStream every other port emits — the reconciler doesn't know the samples
came over a wire.

```python
from uqff_downhole_simulator import ingest
stream = ingest({'host': '10.0.0.5', 'port': 502, 'polls': 60,
                 'interval_s': 60.0, 'register_map': 'my_site_g6_map.json'},
                port='modbus_g6')
```

## v1.12.0 extension: the well-profile catalogue (Daniel GO, 2026-08-24)

`uqff_profile_catalog.py` + `catalog/` — the closed stream gets REAL wells.
Three parts: (1) `PROFILE_SOURCES` — a machine-readable table of six public
geophysical databases (KGS Kansas LAS archive, Equinor Volve, DOE GDR / Utah
FORGE T-P logs, NLOG, US state regulators, offshore nationals) each with URL,
license, and an HONEST access note — several serve only ZIPs or need
registration, so those are documented pull-it-yourself paths. (2) `CATALOG` —
shipped entries with MANDATORY provenance sidecars; the first is a verbatim
excerpt of **real Equinor Volve well 15/9-19 SR** composite-log data (Statoil,
North Sea; excerpt coverage disclosed in-file and in provenance), which
ingests through the las2 port with the first GR value (5.3274 GAPI) verbatim.
(3) `las_to_profile()` — the converter to the engine's profile-CSV format:
measured T/P curves used when present; otherwise REAL depth stations with
DERIVED_GRADIENTS-labeled conditions (Rule 7 — derived is fine, unlabeled is
not). Verified end-to-end: real Volve geometry → profile CSV → engine.

```python
from uqff_downhole_simulator import CATALOG, las_to_profile
r = las_to_profile(CATALOG['volve_15_9_19_sr_excerpt'].stream(), out_csv='volve_profile.csv')
```

## v1.13.0 extension: three real wells + two port upgrades (Daniel-directed, 2026-08-24)

Cataloguing continued one well at a time, each grabbed verbatim and test-verified:

| Entry | Well | Region | Dialect exercised |
|---|---|---|---|
| volve_15_9_19_sr_excerpt | 15/9-19 SR (Statoil) | North Sea | unwrapped, NULL −999.25 |
| scorpio_e1_sa_excerpt | Scorpio E1 (UWI 6038-187) | South Australia | NULL −99999, divider comments, inline column headers |
| kennetcook_2_p129_excerpt | Kennetcook #2 (P-129, Schlumberger 2007) | Nova Scotia | **WRAP. YES** (PETREL), 25 curves |

The Kennetcook well drove two upgrades: **wrapped-LAS parsing** in `read_las`
(records assembled by curve count, trailing partials dropped not guessed —
the earlier honest refusal superseded by honest parsing once a real wrapped
file existed to verify against), and header-anchor capture (BHT/TMAX/TDL/TDD
into stream meta). Its **real measured BHT — 42.0 °C at TD 1,935 m**, stated
"used in calculations" on the log itself — feeds the converter's new
`DERIVED_FROM_MEASURED_BHT` tier: a real two-point thermal profile, stronger
than pure gradients, weaker than a full curve, labeled as exactly that.

Verification (all gate-pinned per run): every entry's first values verbatim
(GR 5.3274 / GAMN 72.0574 / CALI 2.4438154697), NULLs → NaN in all three
dialects, provenance complete on all entries, BHT-anchor math checked against
the surface→42 °C@TD line, wrapped safety (partial records dropped).

## v1.14.0 extension: catalogue well 4 — Texas (Daniel-directed, 2026-08-24)

**UNIVERSITY 6-17 NO.1** (Wildcat field, Section 17, Reagan County, Texas —
Permian region; API 42-303-34774; logged by Halliburton, 06-21-97; via the
public PetroPy library redistribution of Texas University Lands data): 50
verbatim sonic-run rows at 2,747–2,771.5 ft from a 17-curve, 2,587–9,110 ft
well. Three firsts: **LAS VERSION 1.2** (the catalogue's third version
dialect — its value-after-colon header convention exposed a meta-capture bug,
fixed by branching on VERS, so the well identity now reads correctly);
**first imperial-depth well** (converter `depth_unit='ft'` path); and the
**second real BHT anchor — 141.0 °F at TD 9,097 ft** — in DEGF, exercising
the converter's no-conversion unit branch (T(2,747 ft) = 94.9 °F on the
surface→141 °F line, arithmetic gate-checked).

Catalogue standing: **four real wells, four regions** (North Sea, South
Australia, Nova Scotia, Texas), **three LAS version dialects**, **two real
BHT anchors**, every entry provenance-complete.

## v1.15.0 extension: catalogue well 5 — Kansas, the first complete file (Daniel-directed, 2026-08-24)

**COLLINGWOOD 1-28** (Amoco Production, Nicholas field, Stanton County, Kansas;
API 15-187-20743; Sec 28-T30S-R39W; Halliburton, 31-MAY-94; KGS ID 1001178549 —
the Kansas Geological Survey archive reached at last, via the public lasio
redistribution, complete with the KGS update-history comments riding in-file).
Three catalogue milestones: the **first COMPLETE entry** (the entire public
file verbatim — the 5-station interval slice at 1,783.5–1,784.5 ft was KGS's
own archiving, disclosed as theirs); the **second wrapped shape** (27 curves,
depth line + 7/7/7/5-value continuation lines — IDGR 50.6465 API verbatim);
and the **third real BHT (125 °F)** which, with NO TD parameter in the file,
exercises the converter's honest-fallback branch: no TD → no fabricated
anchor line → labeled DERIVED_GRADIENTS. Refusal-over-invention, proven on
real data.

**Catalogue standing: five real wells, five regions** (North Sea, South
Australia, Nova Scotia, Texas, Kansas), three LAS version dialects, two
wrapped record shapes, three real BHT anchors — every entry
provenance-complete, every pinned value verbatim.

## v1.16.0 extension: catalogue well 6 — GISP2, the temperature-curve prize (Daniel-directed, 2026-08-24)

**GISP2** (Greenland Ice Sheet Project 2 borehole, Summit, Greenland — the
USGS/Clow precision temperature log of one of Earth's most famous boreholes),
via the GEUS ice-temperature database (Løkkegaard et al. 2023, *The
Cryosphere*, doi:10.5194/tc-17-3829-2023; data DOI 10.22008/FK2/3BVF9V). The
prize the hunt was for: the catalogue's **first continuous MEASURED
temperature profile** — 598 stations, 72.61–3,053.15 m to bedrock, the
COMPLETE file verbatim, from −31.41 °C near surface through the −32.13 °C
glacial-memory minimum (1,495 m) to −9.29 °C at the bed.

New machinery: `read_temperature_csv` ingests the GEUS `d,t` format as a
depth-indexed LiveStream with a TEMP channel; the catalogue loader accepts
CSV entries with the same mandatory provenance sidecars. With this entry the
converter's **top tier (MEASURED_CURVES) runs on real data for the first
time** (°C→°F branch checked at the bed: 15.29 °F) — **all three tiers of the
honesty ladder are now proven on real wells.** Transcription integrity is
gate-screened: endpoints and the minimum verbatim, depth strictly monotonic,
max step-to-step ΔT 0.13 °C. Disclosed honestly: it's an ice borehole, and
the pressure column remains DERIVED hydrostatic, labeled.

**Catalogue standing: six entries, six regions** (North Sea, South Australia,
Nova Scotia, Texas, Kansas, Greenland), four formats (LAS 1.2, LAS 2.0
unwrapped, LAS 2.0 wrapped ×2 shapes, temperature-CSV), three real BHTs, one
full measured temperature curve. The prize hunt is closed.

## v1.17.0 extension: catalogue well 7 — Agassiz77, Canada (Daniel-directed, 2026-08-24)

**Agassiz77** (Agassiz Ice Cap, Ellesmere Island, Canadian Arctic; measured
1977 — the catalogue's oldest measurement; Clarke/Fisher/Waddington science
lineage) via the same GEUS database as GISP2. COMPLETE file: 67 stations at
10.91–340.91 m, −24.16 → −16.74 °C — a thin High Arctic cap's monotonic
profile, the thermal-regime counterpart to GISP2's deep-sheet glacial-memory
curve. The MEASURED_CURVES tier now holds **two real wells in two different
thermal regimes**. The database's own metadata caveats (approximate location;
thickness mismatch vs Vinther 2008) are carried verbatim in the provenance —
their disclosure, preserved. **Seven entries, seven regions** (North Sea,
South Australia, Nova Scotia, Texas, Kansas, Greenland, Canada).

## v1.18.0 extension: catalogue well 8 — L07-01, Netherlands (Daniel-directed, 2026-08-24)

**L07-01** (Petroland, Dutch North Sea offshore; NLOG UBID 7264; logged 1971;
TD 3,934 m) via the NLOG open-data mandate, redistributed publicly. 50 verbatim
deep quad-combo rows (GR/DT/RHOB/NPHI at 3,915.8–3,910.9 m; GR[0] = 122.553802
GAPI). New dialect coverage: the catalogue's first **descending depth index**
(STEP = −0.1 m, logged bottom-up 3,928 → 64.9 m) — preserved as-logged through
ingest, then handled order-agnostically by the converter → sorting profile
loader → engine chain, gate-verified. **Eight entries, eight regions** (North
Sea NO, South Australia, Nova Scotia, Texas, Kansas, Greenland, Canada,
Netherlands).

## v1.19.0 extension: catalogue entry 9 — the L06-06 real trajectory (Daniel-directed, 2026-08-24)

**L06-06 deviation survey** (Dutch North Sea, NLOG open archive via public
redistribution): the catalogue's first **REAL_DEVIATION_SURVEY** — the
COMPLETE file, 200 measured stations verbatim (MD, inclination 0–5.82°,
azimuth, TVD, X/Y offsets; MD 74.2 → 5,605 with TVD 5,595.27; a gently
deviated S-shaped deep well). New machinery: `read_survey_csv` (long-form
NLOG headers → `DeviationSurvey`, MD→TVD taken directly from the measured
columns — no minimum-curvature reconstruction needed); the catalogue
distinguishes CSV kinds by header, and a survey entry **refuses `stream()`**
with direction to `.survey()` — a trajectory is not a log stream. Honest
notes carried in provenance: units not declared in-file (recorded, not
assumed away; MD/TVD are used relative to each other, which is
unit-invariant), and real tie-on duplicate stations preserved. Verified:
TVD ≤ MD at every station; the real trajectory drives the engine's MD→TVD
physics (deepest-gauge ΔP 4.5 psi vs vertical — small and real, exactly what
a 5.8°-max well should do). **Nine catalogue entries.**

## v1.20.0 extension: catalogue entry 10 — Volve core analysis (Daniel-directed, 2026-08-24)

**15/9-19 A conventional core analysis** (Equinor Volve open data via public
redistribution): the catalogue's first **REAL_CORE_ANALYSIS** — laboratory
ground truth. 87 verbatim core-plug samples: core 1 complete (3,838.6–3,853.8
m) plus the core-2 ultra-permeability streak (incl. **20,800 mD** — the
excerpt alone spans ×138,000 in permeability), with core porosity,
oil/water saturations, and grain density; the lab's interleaved
saturation-vs-plug sample pattern preserved exactly. New machinery:
`read_core_csv` (Volve-style header → depth-indexed LiveStream, blanks →
NaN); units are interpretive-not-in-file and disclosed as such in
provenance. Core data is the calibration endpoint a petrophysics layer would
tie logs to — the closed stream's future ground truth, now in the repo.
**Ten catalogue entries, five kinds** (log excerpts, complete logs, measured
temperature curves, real trajectory, core analysis).

## v1.21.0 extension: catalogue entry 11 — Volve daily production (Daniel-directed, 2026-08-25)

**15/9-F-12 H + 15/9-F-14 H daily production history** (Equinor Volve open
data via a public redistribution of the "Volve production data.xlsx" Daily
Production Data sheet — processing DISCLOSED: original 24 columns preserved
verbatim, 9 redistributor-derived columns appended and labeled as such):
the catalogue's first **REAL_PRODUCTION_TIME_SERIES** — 166 daily records
from FIRST OIL 2008-02-12 through 2008-07-21, the field's two main
producers, source order and calendar gaps preserved exactly.

Why it matters: every prior entry is depth-indexed; the live stream —
telemetry, historian exports, the reconciler — is TIME-indexed. This entry
is the live stream's native shape as real field data, and it carries REAL
sensor-fault phenomenology: a genuine 9-day stuck downhole-pressure run
(264.08789 bar frozen, 2008-05-11→05-19), a wellhead-pressure dropout to
0.0 bar, a negative water volume, water-volume spikes, and blank annulus
cells — the exact fault classes the v1.3.0 QC pipeline injects
synthetically, now in the record for real. New machinery:
`read_production_csv` (DATEPRD header → time-indexed LiveStream, elapsed
seconds at 86,400 s cadence, per-well namespaced channels COL[well],
blanks/absent dates → NaN; units interpretive per the provenance data
dictionary, not claimed as in-file). **Eleven catalogue entries, six
kinds.**

## v1.22.0 extension: catalogue entry 12 — KTB Main Hole hot temperature log (Daniel-directed, 2026-08-25)

**KTB-Oberpfalz HB, log HB-246** (German Continental Deep Drilling Program,
ICDP legacy KTB Information System; canonical citation
doi:10.5880/GFZ.KTB.BM.temperature): the catalogue's first **HOT temperature
data** — 1,589 verbatim rows at 0.1524 m sampling, 7,743.14 → 7,985.15 m,
**169.67 → 183.58 °C** (in-capture max 185.53 °C at 7,974.94 m) — real
crystalline rock in exactly the HPHT regime the simulator models, from the
deepest research borehole complex on Earth (Main Hole TD 9,101 m, ~265 °C).
Germany is region NINE. Both prior measured temperature curves are ice
boreholes; the MEASURED temperature family now spans −32 °C (GISP2) to
+185 °C (KTB) on real data.

Honesty structure, pinned: this is a **MUD-temperature log**, run ~22.75 h
after circulation stopped (the in-file header's TCS/TLAB times are parsed
into stream meta and gate-pinned) — NOT an equilibrium profile; the KTB
equilibrium set exists only inside a ZIP this environment cannot fetch, so
the disturbed log is carried as what it is. Verbatim header preserved
(PT1000 sensor, calibration GAIN/OFFS, tool string, datum). New machinery:
`read_ktb_dat` ('!'-comment header + space-separated DEPT/TMP3/HTEN/MRES →
depth-indexed LiveStream), .dat dialect added to the loader. **Twelve
catalogue entries, nine regions.**

## v1.23.0 extension: catalogue entry 13 — KTB Pilot Hole twin-sensor log (Daniel-directed, 2026-08-25)

**KTB-Oberpfalz VB1A, log VB-251** (KTB Pilot Hole, 1988; ICDP legacy KTB
Information System; canonical citation doi:10.5880/GFZ.KTB.BM.temperature):
a **REAL TWIN-SENSOR instrument** — two calibrated temperature sensors
1,140 mm apart on one sonde, with the in-file accuracy statement
"absolute = 0.05 deg C; relative = 0.01 deg C" (a real cited instrument
spec). 1,082 verbatim six-column rows (DEPT/TMP1/TMP2/GR/HTEN/MRES),
3,268.22 → 3,432.96 m at 95–101 °C. The trailing sensor reads the
just-disturbed mud cooler at EVERY row (mean offset 0.87 °C, all-positive,
gate-pinned) — the simulator's twin-leg comparison, existing in 1988
hardware.

Real instrument artifacts preserved and pinned: a 69-row sensor-settling
FROZEN run at log start (TMP1 = 95.374 repeated while the sensors
equilibrate — the frozen-value fault class, caused by physics not
electronics) and the head-tension collapse 279 → 111 lbf at the 3,425 m
stand-up noted in the header. Honesty: the header's TLAB field carries no
value in the source and stays ABSENT from stream meta — nothing invented.
This file drove the `read_ktb_dat` upgrade to DYNAMIC column-block parsing
(entry 12's 4-column log re-verified under the same parser). **Thirteen
catalogue entries; KTB is the first complex with two catalogued boreholes.**

## v1.24.0 extension: catalogue entry 14 — KTB Main Hole trajectory (Daniel-directed, 2026-08-25)

**KTB-Oberpfalz HB TVD file, 0–9,080 m** (ICDP legacy KTB Information
System; first 2,804 rows captured at exact 1 m sampling, 0 → 2,803 m): the
catalogue's **second real well trajectory** — and the opposite extreme from
the deviated L06-06. In the vertical-drilling-system section of the deepest
research borehole on Earth, **|TVD − MD| stays within 0.35 m over 2.8 km**:
a real NULL CONTROL for the engine's MD→TVD physics (a deviation survey
whose correct effect is almost exactly nothing). The ~0.152 m datum offset
at MD 0 present in the source is preserved verbatim, not corrected away.

With entry 12 (hlog246 temperature) this makes **KTB-HB the first well with
both temperature and trajectory in the catalogue** — the closed stream can
describe this well from its own real data. Port upgrades: `survey()` now
accepts ktb_dat TVD files, and the column-block parser's format-code match
widened (`F` → `F\d*`) — three KTB dialects on one parser. Transcription
method for the highly regular rows disclosed in provenance (run-faithful
transcription, every boundary and all 32 exceptional rows read directly,
structural verification against the capture; source URL for byte-level
re-verification). **Fourteen catalogue entries.**

## v1.25.0 extension: catalogue entry 15 — KTB-HB borehole gravimetry (Daniel-directed, 2026-08-25)

**KTB Main Hole BHGM density profile** (EDCON borehole gravity meter, KTB
deep crustal lab 1996, Univ. Bochum reduction; ICDP legacy KTB Information
System; COMPLETE 9.1 KB file in one fetch): the catalogue's first **REAL
DENSITY PROFILE** — 197 stations, 0 → 8,400 m MD (TVD 8,364 m), in-situ
apparent density 2.55–2.95 g/cm³ with every reduction constant preserved
in-header (IGSN71 absolute gravity, IGF 1967, free-air gradient, reduction
density). Transcription self-check: the mean of the transcribed rock
densities equals the header's own stated average (2.752 g/cm³) to the
millidigit.

Why it matters: this is the PRESSURE-side ingredient the catalogue lacked.
The gate now computes **overburden at TD from measured density over
measured TVD, live in the pin: ~226 MPa ≈ 32,750 psi** — real crustal
overburden in exactly the simulator's 30,000-psi-class regime. Disclosures
pinned: the surface station's RHO = 0.000 is the gravity reference tie
(not rock); the −1.7 mGal discontinuity at the 5,990→6,000 m run boundary
is the header's tool-size change, preserved as real survey structure; the
deep TVD divergence (36 m at 8,400) complements entry 14's near-vertical
section. **KTB-HB now carries temperature + trajectory + density — the
closed stream can describe this well entirely from catalogued real data.
Fifteen entries, nine kinds.**

## v1.26.0 extension: catalogue entry 16 — KTB Pilot Hole rock mechanics (Daniel-directed, 2026-08-25)

**KTB-VB core compressive-strength table** (ICDP legacy KTB Information
System, COMPLETE 11 KB file): the catalogue's first **LABORATORY ROCK
STRENGTH** data — 113 uniaxial tests on Pilot Hole cores, 189.79 →
3,831.88 m, UCS 3.2 → 265.4 MPa, with E-modulus, rock type, foliation dip,
and per-sample timestamps (1987–1989 field lab). New `read_ktb_table`
(typed F/C/I column blocks; rock type carried as per-sample quality).

The geomechanics pair closes LIVE: using entry 15's measured mean density,
the gate counts **59 of 113 samples whose strength falls BELOW the
overburden at their own depth** — weak foliated gneisses (mean ~49 MPa)
against strong amphibolites (~137 MPa): the physical reason the KTB pilot
hole developed breakouts, computed from catalogued data on every run.
Strength (what the rock can bear) vs overburden (what it does bear) is the
two-stream comparison at the geomechanics level.

Refusal discipline at the cell level: the source declares TAB separators,
which the legacy rendering collapses — so empty interior cells lose their
position. The reader assigns trailing tokens by DECLARED TYPE only (a
decimal cannot be an I2 dip), and the 9 genuinely ambiguous trailing
integers are REFUSED: NaN plus the raw token preserved in a per-row quality
flag, with the source URL carried for byte-level resolution. **Sixteen
catalogue entries, ten kinds.**

## v1.27.0 extension: catalogue entry 17 — KTB Main Hole strength table (Daniel-directed, 2026-08-25)

**KTB-HB core compressive-strength table** (ICDP legacy site, COMPLETE
2.5 KB file): the strength pair completes. 21 samples from the Main Hole's
sparse deep coring (4,151 → 7,400 m; core is rare in the HB — it was mostly
cutting-drilled): 20 amphibolites at 96.6–307.9 MPa plus one MUS-GNS at
5,282 m (49.1 MPa, dip 60°) — the deep analogue of the VB's weak-gneiss
story. `read_ktb_table` reused unchanged: the reader generalizes across
both holes; the 4 TAB-collapse-ambiguous cells are refused with raw tokens
preserved, exactly as in entry 16.

The three-entry comparison now runs live in the gate: HB mean strength
(199 MPa) doubles the VB's (77 MPa) — the deep section holds because it is
amphibolite — yet at 5.5–6.2 km even amphibolites begin to fall below the
density-derived overburden (**5 of 21 samples**, including the 49.1 MPa
gneiss under 142.6 MPa of rock): the mechanical squeeze of true depth,
counted from entries 15+16+17 together rather than asserted. **Seventeen
catalogue entries; KTB contributes six, and both holes carry a strength
table.**

## v1.28.0 extension: catalogue entry 18 — ODP Hole 504B borehole fluids (Daniel-directed, 2026-08-25)

**The ocean's KTB.** ODP Hole 504B (Costa Rica Rift flank, North Pacific;
seafloor at −3,474 m) is the deepest hole ever drilled into oceanic crust —
and it joins the catalogue as **region TEN**, the first sub-seafloor entry,
and the **eleventh kind**: borehole-fluid chemistry (PANGAEA
doi:10.1594/PANGAEA.805957, Magenheim et al. 1995, COMPLETE dataset — 8
samples, 350–1,550 mbsf, 42 numeric channels at ambient >160 °C).

The science is a depth gradient and the gate computes it live: Mg falls
(corr −0.81) while Ca rises (+0.80) and ⁸⁷Sr/⁸⁶Sr slides from the seawater
value (0.70921) toward basaltic (0.70758) — seawater mixing with a reacted
end-member down the hole. The paper's own honest framing ("borehole fluids,
not confirmed formation waters") is preserved as the entry's meaning; the
near-seawater parcel at 950 m and the short-row NaN padding are real
structure, kept. For the downhole program this is the chemistry of the
fluid the tools actually live in — corrosion- and scaling-relevant.

Route milestone: the **PANGAEA textfile export** serves complete datasets
as tab-separated text whose header carries its own citation, abstract,
coordinates, per-parameter methods and license (CC-BY-3.0) — all parsed to
stream meta by the new `read_pangaea_txt`. The richest-provenance source
format in the catalogue, and a whole source family for future entries.
**Eighteen entries, ten regions, eleven kinds.**

## v1.29.0 extension: catalogue entry 19 — IODP U1324 measured pore pressure (Daniel-directed, 2026-08-25)

**The last missing quantity arrives.** IODP Site 308-U1324 (Ursa Basin,
continental slope offshore Louisiana, GULF OF MEXICO — region ELEVEN;
seafloor −1,056 m): in-situ pore-pressure penetrometer measurements
(PANGAEA doi:10.1594/PANGAEA.725472, Flemings et al. 2008, COMPLETE — 18
deployments, 50–608.2 mbsf). The catalogue had temperature, geometry,
density, strength, rates, core, and fluids; now it has **measured downhole
pressure** (twelfth kind) — with hydrostatic AND overburden baselines
travelling in the same file, so overpressure is computed, never asserted.

And it is THE FIND occurring in nature: **every one of the 12 baselined
stations reads above hydrostatic** (max +2.07 MPa; at the 608.2 m headline
station, measured 18.80 MPa vs hydrostatic 16.73 vs overburden 22.11 —
λ* = 0.385) — the shallow overpressure that preconditions the submarine
landslides this site was drilled to study. Measured-vs-baseline residual as
real geology: the reconciler's founding scenario, in the record and pinned
live. Bonus instrument lineage: the T2P probe carries tip AND shaft
pressure sensors (duplicate-depth row pairs preserved) — the catalogue's
second real dual-sensor instrument; tip rows' blank baseline cells stay
NaN, as the source reported them once per deployment. `read_pangaea_txt`
needed zero changes. **Nineteen entries, eleven regions, twelve kinds.**

## v1.30.0 extension: catalogue entry 20 — the CORK observatory (Daniel-directed, 2026-08-25)

**The twentieth entry is the instrument class this package simulates.**
ODP Hole 1027C, Juan de Fuca Ridge flank (region TWELVE; seafloor
−2,656 m; crustal age 3.6 Ma): a **CORK sealed-borehole observatory** —
the real-world permanent downhole monitoring installation (PANGAEA
doi:10.1594/PANGAEA.722627, Davis & Becker 2002, COMPLETE). Thirteenth
kind: observatory profile.

One file, both thermal states, at the same 10 thermistor stations: the
drilling-disturbed profile at installation (max 19.6 °C) and the
near-equilibrium profile after ~3 sealed years (max 60.7 °C) — a
**+42.6 °C recovery at 586.8 m**. The disturbed-vs-equilibrium distinction
the KTB temperature entries could only disclose in provenance is here
MEASURED on both sides, and the gate computes the physics live: a steep
~104 °C/km conductive sediment gradient (young hot crust) collapsing to an
**isothermal basement** (0.1 °C spread across the deepest five stations,
vs 1.1 °C while disturbed) — vigorous hydrothermal circulation
homogenizing the upper crust, the Davis-Becker result from the data.

And the file's own Comment block is a service-life record: CORK installed
1996, data recoveries 1997/1999/2000, **logger replaced 1999**, current
status "Operational (pressure only)", plus the formation-pressure summary
(−69 kPa initial → −26 kPa equilibrium: young crust slightly
UNDERpressured). Multi-year sealed-hole monitoring with maintenance events
— the ServiceLifeSimulator's world as history. `read_pangaea_txt`
unchanged (third entry on the parser). **Twenty entries, twelve regions,
thirteen kinds.**

## v1.31.0 extension: catalogue entry 21 — 1027B thermal conductivity (Daniel-directed, 2026-08-25)

**The heat-flow closure.** Thermal conductivity of ODP Hole 1027B
(PANGAEA doi:10.1594/PANGAEA.792214, JANUS shipboard set, COMPLETE — 32
needle-probe measurements, k = 0.84–1.72 W/m/K, with per-sample core
labels and full probe lineage): the **fourteenth kind**, measured at the
SAME SITE as entry 20's CORK observatory, ~30 m away.

Which means the gate can now do what a heat-flow survey does — from
catalogued data alone: **q = k · dT/dz**, with k from the 1027B core
(arithmetic mean 1.43, harmonic 1.42 W/m/K over the 446–519 m overlap)
and dT/dz from the 1027C sealed thermistor string (~91 K/km between the
bracketing stations) → **~130 mW/m² of young-crust heat flow**, an order
of magnitude above continental values — computed live in a pin, never
quoted from literature. Site 1027 joins KTB-HB as a multi-dataset site
family, and is the first whose cross-dataset physics runs in the gate.

Honesty items: the source's depth coverage is BIMODAL (5 measurements at
0.65–3.4 m, 27 at 445.8–518.9 m, nothing archived between) — preserved
and pinned as source structure, not interpolated over; harmonic and
arithmetic means both computed (layered-media physics disclosed); DOI
found by probing JANUS's sequential numbering — first probe hit.
`read_pangaea_txt` unchanged (fourth entry). **Twenty-one entries,
fourteen kinds.**

## v1.32.0 extension: catalogue entry 22 — DSDP 504B physical properties (Daniel-directed, 2026-08-25)

**The catalogue reaches back to the Glomar Challenger.** Physical
properties of DSDP Hole 69-504B (PANGAEA doi:10.1594/PANGAEA.221630,
COMPLETE — 61 basalt samples, 281–484 mbsf, from 504B's FIRST campaign in
1979): the **fifteenth kind** (porosity/density physical properties) and
the catalogue's first DSDP-era data — scientific ocean drilling's founding
vessel enters the record. Porosity 2.66–11.39 % (fresh massive units vs
altered/brecciated horizons — newborn 504B's alteration structure in
numbers), wet-bulk density 2.73–2.95, grain density 2.94–3.03 g/cm³.

And it is THE SELF-AUDITING DATASET: porosity, grain density and bulk
density are bound by WBD = φ·ρw + (1−φ)·ρ_grain, and the file carries all
three — so the gate re-runs the 1979 laboratory's internal consistency on
every run: **all 61 rows close the identity** (mean |residual| 0.0028
g/cm³, max 0.0096, at seawater ρw = 1.025). One computation audits the
lab's bench work AND this catalogue's transcription simultaneously.

Hole 504B becomes the third multi-dataset family: entry 18's borehole
fluids at >160 °C ambient, and now the physical properties of the very
rock those fluids react with. `read_pangaea_txt` unchanged (fifth entry).
**Twenty-two entries, fifteen kinds.**

## v1.33.0 - Catalogue entry 23: ODP Hole 1165B thermal conductivity (Prydz Bay - ANTARCTICA, region thirteen)

`odp_1165b_thermal_conductivity` - the COMPLETE shipboard thermal-conductivity dataset of ODP Hole 188-1165B
(O'Brien et al. via JANUS, PANGAEA doi:10.1594/PANGAEA.792386, CC-BY-3.0 declared in-file): 81 full-space
needle-probe measurements, 3.75-503.65 mbsf through the Prydz Bay glacio-marine drift at -64.38 S on the
Antarctic continental rise (seafloor -3,538 m), k = 0.432-1.062 W/m/K. Antarctica joins as region THIRTEEN,
completing the catalogue's pole-to-pole span. No reader changes - `read_pangaea_txt` handled its fifth
dataset unchanged.

The find: the Comment column carries the three raw replicate readings behind every archived value, so the
dataset ships its own repeatability record - and re-running the mean on all 81 rows closes on 80 and fails
on exactly one: 317.35 m, where the printed replicates "1.013, 0.016, 1.031" cannot average to the archived
1.0200 - but substituting 1.016 for 0.016 restores the identity exactly. A dropped leading digit in the
SOURCE archive, detected by the catalogue's own verification discipline, preserved verbatim, disclosed in
provenance, and pinned in the gate as the identity-detected exception.

## v1.34.0 - Catalogue entry 24: ODP 111-504B sheeted-dike elastic moduli (the four-identity audit)

`odp_504b_dike_elastic_moduli` - the COMPLETE laboratory elastic-properties table for the sheeted-dike
complex of ODP Hole 111-504B (Christensen, Wepfer & Baud 1989, PANGAEA doi:10.1594/PANGAEA.754017,
CC-BY-3.0 declared in-file; 519 cells / 63 rows, verified against the header's own Size declaration):
8 dike core samples, each swept through confining pressures 200 -> 6,000 bar, with Vp (6,170-6,960 m/s),
Vs (3,400-3,820 m/s), Vp/Vs, Poisson's ratio, bulk and shear moduli, ambient density and porosity.
504B is now a THREE-dataset site family - Leg 69 (1979) physical properties, Leg 111 (1986) dike
elastics, Leg 137 (1991) borehole fluids - three expeditions, 24 years, one hole.

Reader: first label-indexed PANGAEA export (no depth column) - `read_pangaea_txt` now falls back to an
ordinal index with the sample labels riding as quality; all six prior depth-indexed .txt entries
regression-verified unchanged.

The audit: four internally-derivable columns, all re-derived by the gate on every run - Vp/Vs (63/63,
max dev 0.0054), Poisson from (r^2-2)/(2(r^2-1)) (63/63, max dev 0.011), shear modulus rho*Vs^2 and bulk
modulus rho*(Vp^2 - 4/3*Vs^2) (56/56 density-bearing rows, max dev 930 / 1,168 MPa vs the table's
1,000-MPa rounding). And the sweep's monotonic-pressure structure caught two source-archive quirks,
preserved verbatim: sample 161R carries nine rows led by an out-of-sequence duplicate 6,000-bar row
while neighbouring 155R is missing its 6,000-bar row (the orphan continues 155R's trend exactly), and
sample 148R lacks both its density and its 400-bar step.

## v1.35.0 - Catalogue entry 25: DSDP 69-504B sound velocity (the cross-entry impedance join)

`dsdp_504b_sound_velocity` - the COMPLETE Leg 69 shipboard sonic dataset for Hole 504B
(Cann/White/Langseth, PANGAEA doi:10.1594/PANGAEA.229754, CC-BY-3.0 declared in-file; 189 cells /
63 rows): compressional-wave velocity on the 1979 basalt cores, 279.08-484.04 mbsf, Vp = 5,105-6,390
m/s, every row instrument-tagged. Found by sequential-DOI probe (the 69-505 sibling at 229755 ->
504B at 229754, first probe). 504B is now a FOUR-dataset site family - 1979 sound velocity, 1979
physical properties, 1986 dike elastic moduli, 1991 borehole fluids - the deepest scientific record
of any site in the catalogue.

The join: this table and the physical-properties table archive the SAME core suite as separate
datasets. Joined on depth (|dz| <= 0.05 m), 60 of 63 rows pair up - four at identical cm positions -
and the gate computes a live acoustic-impedance profile Z = rho x Vp = 13.94-18.50 x1e6 kg/m2/s
(mean 16.59) from two independently archived 1979 datasets on every run: the physics of seismic
reflection imaging as a fidelity assertion. Bonus disclosure: the only duplicate depth in the profile
is a repeat measurement archived twice (484.04 m, sample 29-1,4: 5,105 vs 5,136 m/s - a 0.6%
repeatability spread the archive kept), preserved verbatim.

## v1.36.0 - Catalogue entry 26: Nankai megasplay shear strength (the slope-stability re-derivation)

`nankai_megasplay_shear_strength` - the COMPLETE laboratory shear-strength table behind Ikari,
Strasser, Saffer & Kopf (2011, EPSL): submarine-landslide potential near the Nankai megasplay fault
(PANGAEA doi:10.1594/PANGAEA.786715, CC-BY-3.0 declared in-file; 150 cells / 15 rows, full paper
abstract preserved in the header). A double first: the NANKAI TROUGH accretionary prism offshore
Japan joins as region FOURTEEN (first subduction-zone data, first entry drilled by D/V Chikyu), and
slope-sediment shear strength is kind EIGHTEEN - the soft-sediment counterpart to the KTB crystalline
strength tables. 15 measurements from three holes spanning the megasplay (C0001E / C0004C / C0008A,
seafloor slopes 3/7/12 degrees), 7.91-121.29 mbsf, clay 31-59%, tau = 40-470 kPa, all best-fit
R^2 >= 0.995.

The audit: the gate re-derives the paper's headline conclusion on every run - infinite-slope driving
stress sigma'_v*sin(a)*cos(a) against measured strength gives factor-of-safety 2.38-15.31, ALL 15
stations statically stable, exactly the published finding - and the effective/total stress ratio
sits in a tight buoyancy band (0.359-0.413) across all three holes. Detected source quirk, preserved
verbatim: all ten Expedition-316 rows carry Event labels '316-C000xx' but sample labels prefixed
'315-' - an expedition-number typo in the source table, caught by cross-checking the file's own two
label columns.

## v1.37.0 - Catalogue entry 27: ODP 118-735B gabbro elastic moduli (the crustal ladder completes)

`odp_735b_gabbro_elastic_moduli` - the COMPLETE Table 4 of Iturrino, Christensen, Kirby & Salisbury
(1991): average velocities and elastic constants for the Atlantis Bank gabbros of ODP Hole 118-735B
(PANGAEA doi:10.1594/PANGAEA.757872, CC-BY-3.0 declared in-file; 1,144 cells / 104 rows verified
against the header's own Size declaration; found via the parent publication-series page - bundle DOIs
do not export textfile, child tables do). The SOUTHWEST INDIAN RIDGE joins as region FIFTEEN
(seafloor -731 m, the catalogue's shallowest ocean site), and the catalogue completes the
OCEANIC-CRUST LADDER: sediments -> pillow basalts (504B Leg 69) -> sheeted dikes (504B Leg 111) ->
layer-3 gabbro (735B Leg 118) - the full ophiolite sequence as verbatim public data. 13 gabbro
samples (olivine gabbros, Fe-Ti oxide gabbros, metagabbros) x 8 confining pressures 100-2,000 bar:
Vp 6,350-7,310 m/s, Vs 3,510-4,040 m/s, density 2.84-3.27 g/cm3, full petrographic modal mineralogy
verbatim in every row.

The audit - five this time: the four elastic identities close on ALL 104 rows (density rides on every
row, unlike the dike table): Vp/Vs max dev 0.0077, Poisson max dev 0.0059, G = rho*Vs^2 max dev
671 MPa, K = rho*(Vp^2 - 4/3*Vs^2) max dev 792 MPa vs the table's 1,000-MPa rounding. The fifth is
unique to this entry: the modal percentages in each sample's comment sum to ~100% on all 13 samples,
parsed live from the file. Four source spelling quirks preserved verbatim and pinned: the dataset's
own PANGAEA title says 'share-wave'; 48R says 'Grabbo'; 83R says 'tracee'; 55R's modal list reads
'10 oxides' with the percent sign missing.

## v1.38.0 - Catalogue entry 28: ODP 209-1274A mantle peridotite (the ladder goes below the crust)

`odp_1274a_mantle_peridotite_mad` - the COMPLETE shipboard moisture-and-density dataset of ODP Hole
209-1274A (Miller, Kelemen & Kikawa, PANGAEA doi:10.1594/PANGAEA.259148, CC-BY-3.0 declared in-file;
180 cells / 18 rows; found by a three-probe sequential-DOI walk of the leg-ordered JANUS MAD series).
The MID-ATLANTIC RIDGE joins as region SIXTEEN: serpentinized mantle harzburgite from the 15deg20min
Fracture Zone (seafloor -3,940 m, 22.2% hard-rock recovery), 17.79-146.93 mbsf. With it the ladder is
complete from seafloor mud to the MANTLE: sediments -> pillow basalts (504B) -> sheeted dikes (504B)
-> layer-3 gabbro (735B) -> residual peridotite (1274A).

The physics is in the numbers: every grain density (2.588-2.823 g/cm3) sits far below fresh
peridotite's ~3.3 - the mass deficit serpentinization leaves when seawater hydrates the mantle.

The audit - the FIVE-IDENTITY LOCK, the cleanest interlocked table in the catalogue: WBD =
phi*rho_w + (1-phi)*rho_grain (max dev 0.001 g/cm3), DBD = (1-phi)*rho_grain (0.0016), void ratio
e = phi/(1-phi) (0.0008), water content wet (0.05%) and dry (0.07%) - all five re-derived by the
gate on all 18 rows, every derived column closing against every other within table rounding.

## v1.39.0 - Catalogue entry 29: Chicxulub M0077A peak-ring P-wave (the crater that ended the Cretaceous)

`chicxulub_m0077a_pwave_velocity` - the COMPLETE discrete-sample P-wave dataset of IODP Hole
364-M0077A (Expedition 364 Scientists, PANGAEA doi:10.1594/PANGAEA.883479, CC-BY-3.0 declared
in-file; 2,170 cells / 717 rows, the largest verbatim PANGAEA table in the catalogue). The
CHICXULUB IMPACT CRATER joins as region SEVENTEEN: first impact structure, first mission-specific
platform (L/B Myrtle), shallowest site (19.8 m of water over the Yucatan shelf). 828 m of profile,
506.17-1334.51 mbsf, through post-impact sediment, suevite, impact melt, and the shocked
peak-ring granite of the K-Pg impactor.

The physics: the 523 granite-basement rows average 4,171 m/s, and NO sample in the entire profile
reaches 5,400 m/s where intact granite runs 5,500-6,000 - the measured velocity deficit IS the
pervasive shock damage that let the peak ring rise. The archive's fingerprints ride verbatim:
sample 44R-3,54-56 measured twice (3,082/3,118 m/s), 38 non-monotonic archival steps (the 37R-40R
block filed 600+ m out of place near the end of the file), 19 shipboard QC comments.

The audit: this dataset checksums its own transcription - Depth = Top + (label cm-interval
midpoint)/100 EXACTLY, down to fractional intervals (232R-1,91-93.5) and the decimal-start oddity
(299R-2,84.1-96). The gate re-runs the identity on all 717 rows and re-derives the header's own
Size declaration (3x717 + 19 comments = 2,170) on every run.

## v1.40.0 - Catalogue entry 30: ACEX Lomonosov age-depth model (the thirtieth entry reaches the pole)

`acex_lomonosov_age_depth_model` - the canonical age model of the Arctic Coring Expedition (Backman
et al. 2008, Paleoceanography; PANGAEA doi:10.1594/PANGAEA.705517, CC-BY-3.0 declared in-file;
COMPLETE, 38 cells / 10 control points). The CENTRAL ARCTIC OCEAN joins as region EIGHTEEN: the ACEX
composite site sits at 87.89 N on the Lomonosov Ridge, 235 km from the North Pole, drilled from the
icebreaker Vidar Viking with two escort icebreakers holding station in moving sea ice - the
catalogue's first icebreaker entry and first composite virtual core (spliced from four holes). And
AGE-DEPTH GEOCHRONOLOGY is kind NINETEEN - the catalogue's first time axis: 399.63 m of core
carrying 56 million years of Arctic history.

The structure IS the science: both ACEX hiatuses are encoded in the table itself. 198.70 m appears
TWICE, with ages 18,200 and 44,400 ka - the same centimetre of seafloor is both early Miocene and
middle Eocene, a 26.2-Myr gap held as a duplicate-depth pair - and the 2.2-Myr Miocene hiatus sits
between 135.49 and 140.44 m.

The audit: all six sedimentation rates re-derive live as delta-depth/delta-age between the correct
hiatus-aware bounds - the A-B rate closes ONLY if the Miocene hiatus is excluded, so the audit
verifies the hiatus itself - with B-C landing at the exact two-decimal rounding boundary (0.8051 ->
archived 0.80). The header's Neogene average closes too (198.7/16.0 = 12.4 m/Myr). Disclosed source
quirk: the archive's own Comment field is truncated mid-sentence ('...Average sedimentation'),
preserved verbatim including the cut, the missing Paleogene rate re-derivable at 17.5 m/Myr.
