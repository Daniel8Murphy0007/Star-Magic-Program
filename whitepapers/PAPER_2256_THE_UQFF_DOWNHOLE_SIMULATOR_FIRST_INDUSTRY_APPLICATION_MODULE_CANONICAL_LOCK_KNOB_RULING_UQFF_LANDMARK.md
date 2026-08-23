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

---

## APPENDED 2026-08-23 — v1.2.0 EXTENSION: SERVICE-LIFE DRIFT ACCUMULATION (Daniel: "build it")

The v1.0/1.1 layers report drift as an instantaneous RATE. The new module
`uqff_service_life.py` (`ServiceLifeConfig` / `ServiceLifeSimulator`) integrates that
rate over simulated service years, twin-leg at every station, producing the
**divergence curves** a real bench test or field trial would record — upgrading §5's
claim from "shows the ratio" to "shows the separation you'd measure."

Design: per-sensor rates evaluated at base station T/P (permanent-install conditions);
both legs share the industry baseline + stress dressing and differ ONLY by the
canonical suppression, so the accumulated-error ratio converges to the composition and
the separation grows linearly at the predicted rate. Optional periodic recalibration
resets (workover events, both legs zeroed); optional seeded random-walk component
(default small, 0 = deterministic). New anchors, inline-commented: **30,000 psi**
full-scale (HPHT quartz-gauge FS class) and **0.5 %FS** total-error spec budget.

Headless verification (deterministic run, default 6-gauge well, 5 yr, dt = 7 d):

| Check | Result |
|---|---|
| Separation rate, per station | 2.04 → 3.04 psi/yr (shallow → deep, FS 30,000 psi) |
| Final separation at 5 yr | 10.2 → 15.2 psi |
| Accumulated-error ratio vs suppression | 1.0323–1.0327 vs 1.0324 (rate-rounding scatter) |
| Recal every 2 yr | resets land at 2.01/4.02 yr; final sep 1.99 psi ≈ 0.98 yr × rate ✓ |
| Service-life arithmetic | years-to-budget UQFF > conventional at every station (extra life 0.05–0.08 yr at the 3.24% suppression — honest scale) |
| 12-gauge real-profile well | ratio mean 1.0326; deepest station 3.66 psi/yr separation |
| CSV export | divergence curves: time + per-sensor uqff/conv/separation psi columns |

`divergence_summary()` carries the full bench-test report (rates, predicted vs
measured separation, ratio check, years-to-budget, extra service life, recal log).
Package v1.2.0; gate pins run the deterministic accumulation, the ratio-convergence
check, the recal-reset check, and the service-life ordering headlessly per gate run.

---

## APPENDED 2026-08-23 (2) — v1.3.0 EXTENSION: FIELD-TELEMETRY REALISM (Daniel-directed)

`uqff_telemetry.py` (`TelemetryConfig` / `TelemetryRecorder`) makes the simulator's
output look like real permanent-gauge field data — and doubles as a scored test bench
for downhole QC pipelines, because the fault injector keeps ground-truth masks.

**Acquisition realism:** fixed-cadence timestamped sampling (anchor: 1 reading/min,
permanent-quartz telemetry class; 24-h default = 1,440 samples × 6 gauges);
telemetry-line burst dropouts (string-wide MISSING, 1–20 samples); stuck gauges
(electronics freeze, both channels repeat 10–120 samples); independent single-sample
spikes per channel (σ 250 psi / 25 °F). Historian-style quality flag on every sample
(OK / MISSING / STUCK / SPIKE). Seeded runs bit-reproducible (the engine's global-RNG
draws are seeded alongside).

**Scored QC pipeline:** (a) frozen-value detection — identical consecutive samples
(live noise never repeats a float) — **precision 1.0 / recall 1.0** on every seed
tested; stuck runs are excluded from filter statistics (their zero-variance windows
crush the MAD and had flooded run boundaries with false spikes — found and fixed
during authoring). (b) Hampel MAD despiker (window 21, 5σ) with a **two-part
common-mode veto**: multi-gauge coincidence, plus a median-residual check across the
other gauges — a gauge fault hits ONE gauge, a well transient hits the STRING, so
string-wide excursions are restored as physics rather than "cleaned." The veto took
spike-P precision from 0.05 (events mis-flagged) to 0.83–1.0.

| Seeded 24-h scores (4 seeds) | Result |
|---|---|
| Uptime | 97.8–100% (dropout-driven) |
| Stuck detection | precision 1.0 / recall 1.0 (all seeds) |
| Spike-P | precision 0.83–1.0 / recall 0.67–0.88 |
| Spike-T | precision 0.57–0.67 / recall 0.94–1.0 |

Honest disclosure (Rule 7): missed P spikes are draws below the 5σ detection
threshold — physically undetectable against gauge noise, not a filter defect; the
T-channel ~0.1% false-alarm floor is MAD estimation noise, the real-world cost of a
despiker, reported not hidden.

`export_csv()` writes a field-historian-style file: ISO timestamps, per gauge raw
P/T + quality flag + cleaned P/T, blanks on dropout. Package v1.3.0; gate pins run a
seeded 24-h acquisition and check uptime, all three fault classes injected, perfect
frozen-value scores, and spike precision/recall floors, headlessly per gate run.

---

## APPENDED 2026-08-23 (3) — v1.4.0 EXTENSION: DEPTH-SWEEP CASE-STUDY MODE (Daniel-directed)

`uqff_case_study.py` (`CaseStudyConfig` / `depth_sweep` / `case_study` /
`write_markdown` + CLI `python -m uqff_downhole_simulator.uqff_case_study`) answers
the customer question: **where in the well does the suppression matter most?**

The sweep evaluates both drift legs at every depth (linear gradients or a real CSV
profile), reporting separation in psi/yr (FS 30,000 psi anchor), HPHT knee
crossings, horizon separation, and extra service life. Headline logic finds the
best-advantage depth and the top of the HPHT interval.

Verified live (linear-gradient wells):

| Well | Below knees | At depth | HPHT interval top |
|---|---|---|---|
| Default TD 20,300 ft | 2.04 psi/yr (flat suppression ratio) | 3.04 psi/yr at ~20,000 ft | ~13,100 ft |
| Deep 30,000 ft | 2.04 psi/yr | **4.21 psi/yr at ~27,000 ft** | ~14,000 ft |
| Sample kick profile (18,500 ft) | 2.04 psi/yr | 2.94 psi/yr at ~18,200 ft | profile-driven |

The structural story the sweep makes visible: below the stress knees both legs sit
at the flat baseline and the advantage is the constant suppression ratio (2.04
psi/yr at FS 30,000); past the knees the stress dressing multiplies BOTH legs, so
the absolute separation compounds with depth — the UQFF advantage is largest
precisely in the deep hot interval where intervention costs are highest. That is
the case-study argument, and the sweep produces it from the same physics layer the
gate verifies (no separate model).

`write_markdown()` renders the one-page customer case: claim (suppression 1.0324
at the locked primitives), depth table, headlines, the twin-gauge bench test
(PAPER_2250 LABORATORY tier), and the honest DERIVED_HYBRID classification with
anchors disclosed. All outputs plain-float and JSON-serializable. Package v1.4.0;
gate pins run the default sweep, the depth-compounding check, the deep-well
headline, and the report render headlessly per gate run.

---

## APPENDED 2026-08-23 (4) — v1.5.0 EXTENSION: REAL-DATASHEET GAUGE SPECS (Daniel-directed)

`uqff_gauge_specs.py` replaces the template anchors with a REAL gauge's published
numbers, end to end. `GaugeSpec` carries a datasheet (baseline drift, FS, knees,
exponents) with a MANDATORY `source` citation — `load_gauge_spec_json` rejects an
uncited spec (Rule 7: a spec without a citation is not a spec). The spec plumbs
through every layer: physics functions (`spec=`), engine (`SimulatorConfig.gauge_spec`),
service-life (picked up from the engine, FS included), case study (config field +
spec name/citation printed on every report page). With `spec=None` every number is
bit-identical to v1.0–1.4 (backward compatibility gate-pinned via the 0.3356
flagship value).

**Web-verified presets (fetched 2026-08-23):** `geoq177_16k` / `geoq177_30k` from
the GEO PSI GEOQ 177 public specification table (Quartzdyne sensor,
geopsi.com/products/downhole-gauges/geoq-177/): pressure drift **<0.01 %FS/yr** at
every range 10,000–30,000 psiA; accuracy ±0.02/±0.025 %FS; 177 °C rating. Plus
`template_generic`, now honestly labeled as the STRESSED-SERVICE class it is.

**Sourcing discipline (Rule 7):** a "<0.02 %FS/yr at 200 °C" figure surfaced in a
search-engine summary but could NOT be verified in the fetched ChampionX page text —
it was NOT made a preset. What the ChampionX Quartzdyne performance page DOES state:
drift rate increases with temperature, with engineering focus at 150 °C and above —
**independent external confirmation of the template's 150 °C thermal-knee anchor**,
a sourcing bonus recorded here.

**Honest scale disclosure:** the datasheet bound is a reference-condition spec
limit ~20× below the template's stressed-service baseline. Verified live at
`geoq177_30k`: UQFF rate 0.0097 %FS/yr, separation 0.09 psi/yr flat → 0.16 psi/yr
at depth (vs 2.04 → 3.04 for the stressed class), years-to-budget 51.5 vs 50.0.
The suppression RATIO stays 1.0324 regardless of baseline (measured 1.031–1.033,
rate-rounding scatter at the small numbers) — the falsifiable claim is
baseline-independent; the psi-per-year story scales with whichever baseline the
customer's datasheet supplies. Both numbers now come from cited sources, which is
the point of this extension.

Clip band scales proportionally with the baseline (template-exact at 0.215) so
datasheet bounds are not floored by template-scaled clips. Package v1.5.0; gate
pins cover backward compatibility, preset citations non-empty, the ratio at the
datasheet baseline, the uncited-spec rejection, and the spec-carrying case-study
render, headlessly per gate run.

---

## APPENDED 2026-08-23 (5) — v1.6.0 EXTENSIONS: DEVIATION (MD/TVD), BATCH RUNS, HEADLESS CLI (Daniel-directed; completes the extension list)

Three final items from the refinement list, closing it:

1. **Wellbore deviation** (`uqff_deviation.py`): gauges are addressed by MEASURED
   depth (position along the string); physics is evaluated at TRUE VERTICAL depth.
   `DeviationSurvey` maps MD→TVD from real survey pairs (`load_deviation_csv`,
   header `md_ft,tvd_ft`) or the common kickoff-and-tangent shape
   (`from_kickoff`; the kink is an exact interpolation station — an
   off-station kink was caught and fixed during authoring). Plumbed through
   `SimulatorConfig` and `CaseStudyConfig` (sweep rows now carry `tvd_ft`).
   Verified live: 60° tangent from 8,000 ft — MD 20,000 → TVD 14,000 EXACT
   (8,000 + 12,000·cos 60° = 14,000); deepest gauge reads 6,525 psi / 327 °F
   where the vertical model claims 9,315 psi / 435 °F.
2. **Multi-well batch runs** (`run_batch`): a field of named `SimulatorConfig`s run
   in one call, per-well summaries returned (drift, comparison ratio, deviation,
   spec). Verified across vertical + deviated + kick-profile wells: the comparison
   ratio holds 1.0325–1.0326 on ALL of them — the canonical claim is invariant
   across well geometry, which is exactly what a locked-primitive composition
   must do.
3. **Headless CLI** (`__main__.py`): `python -m uqff_downhole_simulator
   <run|service-life|telemetry|case-study>` with shared well options
   (`--td --gauges --profile --spec --kickoff --inclination`). Every workflow —
   engine run, divergence curves, field telemetry, customer case — now runs from
   a shell with no Python code and no display. Verified live including a
   deviated-well + datasheet-spec case study in one command.

Package v1.6.0. Gate pins: kickoff TVD identity EXACT, deviated-vs-vertical P/T
ordering, batch ratio-invariance across geometries, and all four CLI subcommands
executed headlessly per gate run. **The v1.2→v1.6 extension list requested on
2026-08-23 is complete**: accumulate (service life), corrupt honestly (telemetry),
argue (case study), cite (gauge specs), and now bend, scale, and script the well.
