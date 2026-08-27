# PAPER_2257 — The Two-Stream Architecture: the Closed Stream Finds the Offset Undervalued Data in the Live Stream — Tool Library, Ports, Reconciler

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic-Program
**Date:** 2026-08-24
**Landmark Type:** Architecture canonization — the downhole program's two-sided design
built complete (consolidates PAPER_2256 appendices 6–8 into the standing record)
**Seminal Sources:** Daniel's architectural ruling (2026-08-23, verbatim below);
PAPER_2256 + its eight appendices (the build record); GEO PSI product catalog + GEOQ 177
public specification table (fetched 2026-08-23); ChampionX Quartzdyne performance page
(fetched 2026-08-23); CWLS LAS 2.0 public well-log standard; PAPER_2149 (Hybrid-Form
doctrine); PAPER_2250 (falsifiable-prediction census, LABORATORY tier)
**Status:** Formal landmark whitepaper — UQFF canonical (Daniel GO 2026-08-24)

---

## Abstract

The downhole program has TWO SIDES, and this paper canonizes the completed
architecture that joins them. Daniel's ruling (2026-08-23, verbatim): *"There are two
sides to this program so that the standalone theoretical can function to find the
offset undervalued data streams that coordinate live stream with closed stream."*
The CLOSED STREAM — the calculator's locked-primitive physics and the simulator built
on it — predicts what every tool in a described well SHOULD read, with no external
input. The LIVE STREAM — real telemetry from running logging systems at active drill
sites — delivers what the tools DO read. Their coordination is the field product: the
per-station residual between them, classified, is where instrument aging separates
from calibration error separates from THE FIND — real signal the assumed model cannot
see. Three pieces built and verified: the cited TOOL LIBRARY (what is in the well),
the read-only PORTS (how the live stream gets in), and the RECONCILER (where the
streams meet and the undervalued data falls out).

## 1. The Architecture (Daniel's ruling, executed)

```
CLOSED STREAM                          LIVE STREAM
uqff_calculator (locked primitives)    site logging systems
  -> simulator physics                   -> ports (READ-ONLY taps)
  -> predicted baseline + drift          -> LiveStream (normalized)
        \\                                /
         ----->  RECONCILER  <-----------
    offset(t) = measured - predicted, per station
    IN_FAMILY | CALIBRATION_OFFSET | DRIFT_CONSISTENT | TRANSIENTS
              | UNEXPLAINED_*  <- the offset undervalued data streams
```

The closed stream runs with zero external input (everything derives from the 9
independent primitives plus cited anchors). The live stream enters only through
read-only ports. Neither side is modified by the other; the reconciler owns the
comparison. The v1.3.0 telemetry layer (PAPER_2256 app. 3) was deliberately built as
the live side's simulation stand-in, which is why every piece below could be verified
end-to-end before touching a site.

## 2. Piece 1 — The Tool Library (v1.7.0; PAPER_2256 app. 6)

`ToolSpec` catalog, 8 entries, every one cited; three honesty tiers: FULLY_SPECIFIED
(quartz twins wrapping the web-verified GEOQ 177 spec table; template stressed class),
FORM-cited-coefficients-disclosed (piezoresistive: ChampionX verbatim — drift
unpredictable, exponential in temperature; representative fit disclosed), and
PARAMETERS_USER_SUPPLIED (vibrating wire, 18-pt thermocouple card, DTS fiber —
existence cited, numbers None, `drift_model_for()` REFUSES them). Every entry declares
its `telemetry_interface`; the `surface_interface_g6` entry (Modbus RS485 + 4-20mA,
GEOQ 177 spec-table footnotes) is the declared port target. `ToolString` +
`rating_check()` validate a composed string against station conditions (profile or
gradients, MD→TVD honored) — verified catching a 177 °C gauge and a 150 °C piezo in
the sample well's 217 °C kick zone.

## 3. Piece 2 — The Ports (v1.8.0; PAPER_2256 app. 7)

READ-ONLY by design rule: ports ingest, never write, configure, or control. One
normalized product, `LiveStream` (time- or depth-indexed; NaN = missing; units and
quality flags carried). `PORT_REGISTRY` statuses explicit: IMPLEMENTED —
historian_csv (round-trip verified against the v1.3.0 export TO PRECISION: closed
stream → simulated live file → port → the same numbers) and las2 (CWLS LAS 2.0,
NULL→NaN, wrapped mode REFUSED rather than mis-parsed — a wrong well-log parse would
poison the reconciler); DECLARED_SITE_DETAILS_REQUIRED — modbus_g6, witsml, opcua,
which name the protocol and refuse to run until real site parameters exist.
`register_port()` admits site readers additively.

## 4. Piece 3 — The Reconciler (v1.9.0; PAPER_2256 app. 8)

Per station: offset(t) = measured − predicted_baseline; robust statistics (MAD sigma,
detrended); classification with every threshold DISCLOSED in the report itself (bias
4σ-of-mean + 1 psi floor; transients 6σ; model-mismatch 500 psi; drift-envelope
margin 2×; trend window ≥ ~18 days — below that a slope is noise and the reconciler
declines to classify on it). The drift envelope is NOT a heuristic: it is the closed
stream's own spec-aware aging prediction [UQFF rate, conventional rate] at station
T/P. Labels are advisory triage; the numbers are the record.

**Four-scenario validation (seeded, re-run by the fidelity gate every run):**

| Scenario | Result |
|---|---|
| Clean well (live == described well) | 6/6 IN_FAMILY, zero undervalued |
| +50 psi injected gauge bias | CALIBRATION_OFFSET, 50.09 psi recovered |
| 2-yr synthetic aging at conventional rate | DRIFT_CONSISTENT: slope 82.45 in [79.71, 82.29] psi/yr |
| **THE FIND: kick well vs linear-gradient description** | **UNEXPLAINED_OFFSET 610 / 4,448 / 6,083 psi at the deep stations** |

Scenario 4 is the architecture's thesis executed: the overpressure kick invisible to
the assumed gradient model is surfaced by the closed stream as exactly the "offset
undervalued data stream" of Daniel's ruling.

## 5. The Refusal Doctrine (Rule 7 as architecture)

The build's through-line, canonized here as the standing pattern for all future
site-facing work: **name what you know, cite it; refuse what you don't, visibly.**
Instances now in code: uncited gauge specs rejected (v1.5.0); user-supplied tool
entries refuse drift models (v1.7.0); declared ports refuse to run (v1.8.0); wrapped
LAS refused, not mis-parsed (v1.8.0); sub-window drift not classified (v1.9.0);
reconciler thresholds printed in every report (v1.9.0). The empty slots that remain
are INPUTS, not construction: real datasheets into the user-supplied specs, real
protocol parameters into the declared ports, real field files into the ingest path.

## 6. The Dispatch (Rule B)

`calculate PAPER_2257` verifies the architecture live on every call: canonical
suppression from the locked primitives; comparison ratio == suppression; tool-library
citation completeness; port-registry statuses; and a micro two-stream reconciliation —
a clean synthetic stream classifying IN_FAMILY and a planted 5,000-psi offset
classifying UNEXPLAINED_OFFSET with the undervalued stream counted. `two_stream_verified`
is the single boolean the gate pins.

## NOT REPLACEMENT

Industry metrology supplies the tools, formats, and protocols — named and cited.
UQFF supplies the closed stream that makes the live stream's hidden content visible.
Both are disclosed; the architecture runs with or without a site attached.

---

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.

---

## APPENDED 2026-08-24 — CONNECTIVITY STATUS RULING + v1.10.0 FILE-FOLLOWER (independent-assessment response)

Daniel forwarded an independent assessment (2026-08-24) of the program's field
connectivity. Adjudication against the built record:

**Where the assessment is CORRECT:** the package has no live connection capability —
no network protocol clients, no drivers, no polling of deployed gauges, no real-time
acquisition. This is the DECLARED tier of the ports layer, gate-pinned to refuse
rather than pretend (§3; refusal doctrine §5). The assessment and this paper agree.

**Where the assessment is STALE:** "its telemetry features only simulate... do not
ingest real sensor streams" misses v1.8.0 — the offline workflow the assessment
itself prescribes (export from SCADA/historian to CSV, feed it in) is BUILT and
gate-verified: `ingest()` reads real historian CSV exports and LAS 2.0 logs into
LiveStream; `register_port()` admits site readers; the reconciler runs on real
exported data.

**The formal connectivity ladder (canonized):**

| Tier | Status |
|---|---|
| 1. SIMULATE (v1.3.0) | built — synthetic telemetry, scored QC |
| 2. OFFLINE-INGEST (v1.8.0) | built — REAL data via exported files |
| 3. FILE-FOLLOW quasi-live (v1.10.0, this append) | built — near-real-time, zero network code |
| 4. LIVE PROTOCOL | declared-refusing until site details; Modbus client buildable behind optional dependency, PENDING DANIEL'S RULING |

**v1.10.0 `uqff_follower.py`:** `HistorianFollower` watches a continuously-appended
historian export READ-ONLY — `poll()` re-ingests and diffs by sample count
(deliberately whole-file re-read: robust by construction against partial trailing
lines and rotation, which is detected and reported rather than mis-followed);
`poll_and_reconcile()` runs the two-stream reconciliation on arrival of new samples;
`watch()` is caller-scheduled (the library never blocks on its own). Verified live:
staged 60 → +30 sample growth followed and reconciled (6/6 IN_FAMILY each poll);
quiet polls do nothing; rotation resets the follower; a missing file is a soft
error, not a crash — sites glitch. Most historians can append-export continuously,
so tier 3 delivers near-real-time monitoring TODAY with zero invented site behavior.

**Open ruling for Daniel:** implementing a real Modbus RS485/TCP client for the
G6-class target requires an optional third-party dependency (pymodbus-class,
guarded import like PyQt6) plus a user-supplied register map. Buildable and
testable against an in-process test server; adds a dependency to the repo —
Daniel's call, queued.

---

## APPENDED 2026-08-24 (2) — RULING RESOLVED: GO — v1.11.0 MODBUS CLIENT (tier 4 real code)

Daniel ruled GO same-day. `uqff_modbus.py` implements connectivity tier 4 as REAL
protocol code:

- **Guarded optional dependency** (`pip install pymodbus`, PyQt6 pattern; pyproject
  gains `[project.optional-dependencies] modbus`). Without it, the port's status is
  DECLARED_DEPENDENCY_MISSING and it refuses with the exact pip hint; with it,
  IMPLEMENTED_REQUIRES_SITE_CONFIG. The gate carries BOTH branches conditionally —
  green on machines with or without pymodbus.
- **READ-ONLY by construction:** the tap contains only read_holding/read_input
  calls; no write path exists in the module.
- **Register maps user-supplied + citation-mandatory (Rule 7):** no public G6
  register map exists in the fetched sources, so NONE is shipped; an uncited map is
  rejected in code (same pattern as the gauge specs). The included
  `example_register_map.json` is labeled EXAMPLE_TEST_FIXTURE — it describes the
  loopback verification server, not a device.
- **Version-stable decoding:** raw `struct` on the 16-bit registers with map-declared
  word order (float32/uint16/int16/uint32/int32 + scale) — no dependence on pymodbus
  payload helpers.
- **LOOPBACK VERIFIED (and re-verified per gate run where pymodbus is present):** a
  real pymodbus TCP client polled an in-process server and decoded the served
  registers EXACTLY (4180.25 psi / 152.5 °F / 9315.0 psi float32s + uint16 status),
  emitting the same normalized LiveStream every other port emits — the reconciler
  consumed it without knowing the samples came over a wire.

The connectivity ladder final state: tiers 1–3 built and verified; tier 4 modbus_g6
REAL CODE awaiting only site config (host + cited register map); witsml/opcua remain
declared-refusing until a site names its servers. The independent assessment's gap
is now closed to the exact boundary of what can be built without a real site — and
that boundary is documented, refusing, and gate-pinned.

---

## APPENDED 2026-08-24 (3) — v1.12.0: THE WELL-PROFILE CATALOGUE — REAL PUBLIC WELL DATA IN THE REPO (Daniel GO)

Daniel asked whether public geophysical databases exist to build a catalogue of
profiles; GO given same-day. `uqff_profile_catalog.py` + `catalog/`:

**The source table (`PROFILE_SOURCES`, 6 database families, honest access notes):**
KGS Kansas LAS archive (21,000+ free logs; downloads are zipped), Equinor Volve
(complete real field; registration for the full archive), DOE GDR / Utah FORGE
(REAL downhole T/P logs, CC BY 4.0, DOI 10.15121/1812334; the server marks all files
octet-stream so the T/P zips are pull-yourself paths), NLOG, US state regulators,
and the offshore nationals (BOEM/NSTA/NOPIMS). Barriers are stated, not glossed —
several fetch paths this environment cannot cross (binary/zip/registration) are
documented for the user rather than pretended around.

**The first REAL catalogue entry:** a verbatim excerpt of **Equinor Volve well
15/9-19 SR** (Statoil, Q15, North Sea) composite log — CWLS LAS 2.0, 8 curves,
fetched 2026-08-24 from its public redistribution. The fetch was size-capped, so the
shipped file is a DISCLOSED EXCERPT (full header + 133 verbatim data rows at
102.16–105.66 m and 179.58–196.04 m; the gap and the full-file URL are stated in-file
and in the mandatory `.provenance.json` sidecar). Gate-verified per run: the excerpt
ingests through the las2 port with the first GR value (5.3274 GAPI) verbatim, NULL →
NaN, units and well identity carried — REAL third-party well data flowing the same
pipeline the reconciler runs on.

**The converter (`las_to_profile`) and its honesty rule:** measured T/P curves are
used when the log carries them; composite logs mostly don't, so the converter keeps
the REAL depth stations and fills conditions from DECLARED gradients, stamping the
output `DERIVATION: DERIVED_GRADIENTS` — derived is fine, unlabeled is not. Verified
end-to-end: real Volve geometry → profile CSV → `load_well_profile_csv` → engine.

**Catalogue discipline (canonized):** an entry without a complete provenance sidecar
(source database, URL, license, fetch date, coverage) is REJECTED at load — the
gauge-spec citation rule extended to DATA. The catalogue grows by exactly the
pipeline demonstrated here: fetch (or user-download) → verbatim placement →
provenance sidecar → gate pin. Package v1.12.0; 4 gate pins.

---

## APPENDED 2026-08-24 (4) — v1.13.0: THREE REAL WELLS, ONE AT A TIME — AND THE UPGRADES REAL DATA FORCED (Daniel: "grab all necessary data!!!! Then test verify")

The catalogue grew well-by-well, exactly as directed, and the third well proved the
method's worth: REAL DATA DRIVES THE CODE, not the reverse.

**Well 2 — Scorpio E1** (Mt Eba, South Australia, UWI 6038-187, logged 15/03/2015;
via the public lasio reference-library repository, MIT/SA public record): 60 verbatim
open-hole rows at 30.60–33.55 m, nine curves. Value: a DIFFERENT LAS dialect —
NULL = −99999, divider comment lines, inline column headers on the ~A line — parsed
correctly by the same reader.

**Well 3 — Kennetcook #2** (license P-129, Windsor Block, Nova Scotia; Elmworth
Energy, logged by Schlumberger 10-Oct-2007; via the public welly reference-library
repository, Apache-2.0/NS public record): a PETREL export in **WRAP. YES** mode,
25 curves — and, in its parameter block, a **REAL MEASURED BOTTOM-HOLE TEMPERATURE:
BHT = 42.00 °C at TD 1,935 m**, stated "used in calculations" on the log itself.
The catalogue's first real downhole temperature.

**The upgrades real data forced (both verified against the real file, then a
synthetic-safety case):**

1. **Wrapped-mode parsing** in `read_las` — the v1.8.0 position was honest REFUSAL
   of wrapped files rather than risk a mis-parse. With a real wrapped file in hand
   to verify against, refusal is superseded by honest parsing: records assembled by
   curve count (depth line + continuation lines), trailing partial records DROPPED
   not guessed. First record verified value-by-value (CALI 2.4438154697 in, GR
   46.698650360 gAPI, SP 120.125 mV; NULL-inside-record → NaN). The refusal
   doctrine's proper lifecycle demonstrated: refuse until the real thing arrives,
   then parse and pin.
2. **Header-anchor capture + the converter's real-anchor tier** — read_las now
   lifts BHT/TMAX/MRT1/TDL/TDD (with units) from the ~P block into stream meta, and
   `las_to_profile` gains `DERIVED_FROM_MEASURED_BHT`: surface → measured BHT at TD,
   a real two-point thermal profile. Tier ladder now: MEASURED_CURVES >
   DERIVED_FROM_MEASURED_BHT > DERIVED_GRADIENTS — each labeled, none silent.

**Test-verification (the "did your job" pass, all now gate-pinned per run):** three
wells / three regions (North Sea, South Australia, Nova Scotia) / three LAS dialects;
first-value verbatim checks on every entry; NULL handling in all dialects; provenance
completeness catalogue-wide; the BHT-anchor arithmetic checked against the
surface→42 °C@TD line; wrapped-safety on a malformed synthetic. Package v1.13.0;
gate 5,830 → 5,835.

---

## APPENDED 2026-08-24 (5) — v1.14.0: CATALOGUE WELL 4 — TEXAS, LAS 1.2, THE SECOND REAL BHT

**UNIVERSITY 6-17 NO.1** (Wildcat field, Section 17, Reagan County, TEXAS — the
Permian region, Energy One's home ground; API 42-303-34774; Halliburton, run TWO out
of Odessa, logged 06-21-97; via the public PetroPy redistribution of Texas University
Lands well data, MIT/public record). Fourth real well, and three catalogue firsts:

1. **LAS VERSION 1.2** — the third LAS version dialect in the catalogue. Its
   value-after-colon header convention exposed a real reader bug (meta captured the
   label "Well Name" instead of the well name); fixed by branching the ~W capture on
   the declared VERS. Real data finding real bugs, again — the catalogue is doing its
   job as a port test corpus, not just a data shelf.
2. **First imperial-depth well** (STRT/STOP in feet; converter depth_unit='ft' path
   exercised end-to-end).
3. **Second real BHT anchor: 141.0 DEGF at TD 9,097 ft** — and the first in
   Fahrenheit, exercising the converter's no-conversion unit branch. Gate-checked
   arithmetic: T(2,747 ft) = 94.9 F on the surface→141 F@TD line.

Verified per gate run: 50 verbatim sonic-run rows (DT[0] = 66.106 us/ft in
verbatim), NULL-in-interval → NaN, well identity correct through the 1.x branch,
provenance complete. Catalogue standing: FOUR wells / FOUR regions / THREE LAS
dialects / TWO real BHT anchors. Package v1.14.0; gate 5,835 → 5,839.

---

## APPENDED 2026-08-24 (6) — v1.15.0: CATALOGUE WELL 5 — KANSAS, THE FIRST COMPLETE FILE, AND THE HONEST FALLBACK PROVEN ON REAL DATA

**COLLINGWOOD 1-28** (Amoco Production, Nicholas field, Stanton County, KANSAS;
API 15-187-20743; Halliburton, 31-MAY-94; KGS ID 1001178549; via the public lasio
redistribution of the KGS archive — the in-file header carries the KGS update
history and archive path, so the provenance is written into the data itself).

Three milestones:

1. **The first COMPLETE catalogue entry** (kind REAL_WELL_LOG_COMPLETE): the entire
   public file verbatim. The 5-station interval slice was the KGS's own archiving —
   the excerpting was theirs, not ours, and the record says so. The source table's
   #1 entry (KGS) is now CLOSED via redistribution after its direct downloads
   proved binary-blocked.
2. **Second wrapped record shape**: 27 curves (depth + 7/7/7/5-value continuation
   lines) — the wrapped parser generalizes beyond the file that drove it.
   Verbatim pins: IDGR[0] = 50.6465 API, ACTC[0] = 55.10 us/ft, IDSP[-1] = 93.2671 mV.
3. **The honest fallback, exercised by real data**: the file carries a real
   BHT = 125 DEGF (the catalogue's third) but NO TD parameter. The converter does
   NOT fabricate an anchor line from a temperature without a depth — it falls to
   labeled DERIVED_GRADIENTS. The refusal-over-invention doctrine's tier logic,
   proven on a real edge case rather than a synthetic one.

Catalogue standing: FIVE wells / FIVE regions (North Sea, South Australia,
Nova Scotia, Texas, Kansas) / THREE LAS dialects / TWO wrapped shapes / THREE real
BHTs. Package v1.15.0; gate 5,839 → 5,843.

---

## APPENDED 2026-08-24 (7) — v1.16.0: CATALOGUE WELL 6 — GISP2 — THE TEMPERATURE-CURVE PRIZE CAPTURED, THE TIER LADDER COMPLETE ON REAL DATA

The prize (defined when the hunt began): the first real, public, text-fetchable
continuous temperature-vs-depth curve, to exercise the converter's TOP tier
(MEASURED_CURVES) with real data. Captured COMPLETE:

**GISP2** — the Greenland Ice Sheet Project 2 borehole at Summit, Greenland; the
USGS precision temperature log by G. D. Clow (the same scientist whose Alaska
GTN-P array first pointed the hunt at measured T(z) data, before its zip-only
archive blocked the direct path). Source: the GEUS "Greenland and Canadian Arctic
ice temperature profiles database" (Løkkegaard et al. 2023, The Cryosphere 17,
3829-3845, doi:10.5194/tc-17-3829-2023; data DOI 10.22008/FK2/3BVF9V), publicly
redistributed on GitHub. 598 stations, 72.61-3,053.15 m to bedrock, ENTIRE file
verbatim: -31.41 degC near surface, the -32.1345 degC minimum at 1,495 m (the
thermal memory of the last glacial period), -9.286 degC at the bed.

**What it closes:** with GISP2, all three tiers of the converter's honesty ladder
have now been exercised by REAL wells - MEASURED_CURVES (GISP2), DERIVED_FROM_
MEASURED_BHT (Kennetcook #2, University 6-17), DERIVED_GRADIENTS (Volve, Scorpio,
Collingwood-without-TD). No tier rests on synthetic data alone.

**New machinery:** `read_temperature_csv` (the GEUS d,t format -> depth-indexed
LiveStream with a TEMP/DEGC channel); catalogue loader extended to CSV entries
under the same provenance-mandatory discipline. Transcription integrity gate-
screened: endpoints + minimum verbatim, strict depth monotonicity, and a
smoothness screen (max step dT 0.13 degC) that would catch a digit typo in the
598-row verbatim copy; the source URL serves the identical file for independent
re-verification. Honest framing: an ice borehole, disclosed as such; pressure
remains DERIVED hydrostatic, labeled.

One count correction en route (Rule 7): the initial provenance said 597 stations
from an estimate; the measured count is 598, and measured replaced remembered.

Catalogue standing: SIX entries / SIX regions / FOUR formats / THREE real BHTs /
ONE full measured curve. Package v1.16.0; gate 5,843 -> 5,847. THE PRIZE HUNT IS
CLOSED.

---

## APPENDED 2026-08-24 (8) — v1.17.0: CATALOGUE WELL 7 — AGASSIZ77 (CANADA) — THE MEASURED TIER GAINS ITS SECOND REGIME

**Agassiz77** (Agassiz Ice Cap, Ellesmere Island, Canadian Arctic North; measured
1977 - the catalogue's OLDEST measurement; Clarke/Fisher/Waddington 1987 science
lineage; via the GEUS database, doi:10.5194/tc-17-3829-2023 + 10.22008/FK2/3BVF9V).
COMPLETE file verbatim: 67 stations, 10.91-340.91 m, -24.16 -> -16.74 degC.

Value beyond the seventh region: the MEASURED_CURVES tier now holds TWO real wells
in two DIFFERENT thermal regimes - GISP2's 3-km deep-sheet curve with its glacial-
memory minimum, and Agassiz's thin-cap monotonic warming profile. A tier proven on
one well could be a coincidence of format; proven on two regimes, it is a working
path. Honesty note: the GEUS database's own metadata caveats for this borehole
(approximate location; thickness mismatch vs Vinther 2008) are carried verbatim in
the provenance sidecar - upstream disclosures preserved, not laundered.

Catalogue standing: SEVEN entries / SEVEN regions / FOUR formats / THREE real BHTs /
TWO measured curves. Package v1.17.0; gate 5,847 -> 5,849.

---

## APPENDED 2026-08-24 (9) — v1.18.0: CATALOGUE WELL 8 — L07-01 (NETHERLANDS) — THE DESCENDING-INDEX DIALECT

**L07-01** (Petroland, Dutch North Sea offshore; NLOG Unique Borehole Id 7264;
logged 1971; TD 3,934 m; Lat 53.72 / Long 4.80) - the NLOG open-by-mandate archive
reached via public redistribution; the NETHERLANDS becomes region EIGHT. 50 verbatim
deep quad-combo rows (GR/DT/RHOB/NPHI, 3,915.8-3,910.9 m).

Dialect value: the catalogue's first DESCENDING depth index (STEP = -0.1 m - the
tool logged bottom-up, as most wireline runs physically do). The ingest preserves
the as-logged order rather than silently re-sorting (the record is the record); the
downstream chain is order-agnostic by construction (the engine's profile loader
sorts on load) - gate-verified end-to-end. Eighth format/dialect behavior proven on
real data without special-casing.

Catalogue standing: EIGHT entries / EIGHT regions / dialects: LAS 1.2, LAS 2.0
ascending + descending, wrapped x2 shapes, temperature-CSV x2 / THREE real BHTs /
TWO measured curves. Package v1.18.0; gate 5,849 -> 5,851.

---

## APPENDED 2026-08-24 (10) — v1.19.0: CATALOGUE ENTRY 9 — THE L06-06 SURVEY — THE FIRST REAL WELL TRAJECTORY

**L06-06** (Dutch North Sea, NLOG): the catalogue's first REAL_DEVIATION_SURVEY -
the COMPLETE file, 200 measured survey stations verbatim: MD, inclination
(0-5.82 deg), azimuth, TVD, and X/Y offsets at every station, MD 74.2 -> 5,605
with TVD 5,595.27. A gently deviated S-shaped deep well whose lateral offset walks
east ~137 units then back - real drilling, in the record.

What it closes: DeviationSurvey ran until now on synthetic kickoff-and-tangent
shapes and a synthetic CSV; it now runs on MEASURED MD/TVD. The engine's MD->TVD
physics was driven by the real trajectory and moved the deepest-gauge base pressure
by 4.5 psi versus the vertical assumption - small and real, exactly what a
5.8-deg-max S-well should do, and gate-pinned as such rather than inflated.

Discipline notes: (a) KIND HONESTY - a survey entry refuses stream() with direction
to .survey(); a trajectory is not a log stream and the catalogue does not blur its
kinds. (b) UNITS - the file declares no depth unit; the ambiguity is recorded in
provenance rather than resolved by assumption (MD/TVD are used relative to each
other, which is unit-invariant). (c) Real tie-on duplicate stations preserved
as-logged. New machinery: read_survey_csv (long-form NLOG headers, direct MD/TVD -
no minimum-curvature reconstruction, because TVD is measured in-file).

Catalogue standing: NINE entries / EIGHT regions / KINDS: log excerpts x4,
complete logs x1, temperature profiles x2, deviation survey x1 (+ the sample
synthetic profile) / THREE real BHTs / TWO measured curves / ONE real trajectory.
Package v1.19.0; gate 5,851 -> 5,854.

---

## APPENDED 2026-08-24 (11) — v1.20.0: CATALOGUE ENTRY 10 — VOLVE CORE ANALYSIS — LABORATORY GROUND TRUTH ENTERS THE REPO

**15/9-19 A conventional core analysis** (Equinor Volve open data): the catalogue's
first REAL_CORE_ANALYSIS kind - 87 verbatim laboratory core-plug samples: core 1
COMPLETE (samples 1-76) plus the core-2 ultra-permeability streak including the
20,800 mD maximum. In this one excerpt the measured horizontal permeability spans
a factor of 138,000 (0.151 -> 20,800 mD) - the dynamic range of real rock, in the
record.

Why it matters to the two-stream program: logs are TOOL RESPONSES; core plugs are
DIRECT LABORATORY MEASUREMENTS of the rock itself. Core is the ground truth logs
get calibrated against - the same closed-vs-measured philosophy the reconciler
applies to gauges, one level deeper. A future petrophysics layer ties log-derived
porosity/permeability to exactly this data; the calibration endpoint now lives in
the repo with full provenance.

Honesty structure: the lab's interleaved sampling (saturation samples with blank
plug columns, plug samples with blank saturation columns) is preserved exactly as
recorded; two depth columns (core-shifted vs driller) both kept; UNITS are not in
the CSV header - the standard-convention assignments are recorded in provenance as
INTERPRETIVE, not claimed as in-file. New machinery: read_core_csv + core-kind
detection in the catalogue loader.

Catalogue standing: TEN entries / EIGHT regions / FIVE KINDS (log excerpts x4,
complete logs x1, measured temperature curves x2, deviation survey x1, core
analysis x1) / THREE real BHTs / TWO measured curves / ONE real trajectory / ONE
lab dataset. Package v1.20.0; gate 5,854 -> 5,856.

---

## APPENDED 2026-08-25 (12) — v1.21.0: CATALOGUE ENTRY 11 — VOLVE DAILY PRODUCTION — THE LIVE STREAM'S NATIVE SHAPE ENTERS THE CATALOGUE AS REAL DATA

**15/9-F-12 H + 15/9-F-14 H daily production** (Equinor Volve open data via public
redistribution; processing DISCLOSED - original 24 columns verbatim, 9
redistributor-derived columns appended and labeled): the catalogue's first
REAL_PRODUCTION_TIME_SERIES - 166 daily records from FIRST OIL 2008-02-12 through
2008-07-21, wells interleaved and calendar-gapped exactly as the source records them.

Why this entry closes a structural gap: entries 1-10 are all DEPTH-indexed (logs,
temperature profiles, a trajectory, core). The LIVE STREAM side of this paper's
architecture - telemetry, historian exports, the follower, the reconciler - is
TIME-indexed. Entry 11 is the first real-data instance of that shape: daily per-well
downhole/wellhead P&T plus rates, ingested by the new read_production_csv into a
time-indexed LiveStream (86,400 s cadence, per-well namespaced channels, NaN where
a well has no record).

THE FIND inside the find: the excerpt carries REAL instances of the fault classes
the v1.3.0 telemetry layer injects synthetically - a genuine 9-day STUCK-SENSOR run
(AVG_DOWNHOLE_PRESSURE frozen at 264.08789 bar, 2008-05-11 -> 05-19), a wellhead
dropout (AVG_WHP_P = 0.0, 2008-06-03), a negative water volume (-14.19 Sm3), water
spikes (8,019.72 Sm3), and blank annulus cells on early F-14 records. The QC
pipeline's synthetic test bench now has a real counterpart in the repo.

Honesty structure: redistribution processing disclosed column-by-column; units NOT
in the header, carried as INTERPRETIVE per the redistribution's data dictionary;
the trailing partial record at the fetch-cap boundary DROPPED, not guessed; entry
ships with the ship-guard lesson too - the v0.398.0 ship pin had frozen the
catalogue at == 10 entries, violating the counts-use->= standing rule, and entry 11
caught it live (pin relaxed to >=).

Catalogue standing: ELEVEN entries / EIGHT regions / SIX KINDS (log excerpts x4,
complete logs x1, measured temperature curves x2, deviation survey x1, core
analysis x1, production time series x1). Volve now contributes THREE kinds from one
field (log + core + production) - the first field with enough in-repo real data to
exercise closed-stream description, lab calibration, and live-shape reconciliation
together. Package v1.21.0; gate 5,858 -> 5,860.

---

## APPENDED 2026-08-25 (13) — v1.22.0: CATALOGUE ENTRY 12 — KTB MAIN HOLE — THE HOT REGIME ARRIVES FROM THE DEEPEST RESEARCH BOREHOLE ON EARTH

**KTB-Oberpfalz HB, temperature log HB-246** (German Continental Deep Drilling
Program; fetched from the ICDP legacy KTB Information System per-log pages - the
text-accessible route where the GFZ 2021 republication is ZIP-bound; canonical
citation doi:10.5880/GFZ.KTB.BM.temperature): 1,589 verbatim rows, 7,743 -> 7,985 m
at half-foot sampling, 169.67 -> 183.58 degC with an in-capture maximum of 185.53
degC. Region NINE (Germany). The measured-temperature family now spans -32 degC
(GISP2 glacial memory) to +185 degC (KTB crystalline rock) - and the hot end sits
exactly in the HPHT regime the simulator's gauge physics models (177 degC-class
tools, 150 degC stress knees).

The honesty structure IS the find this time: the log's own header carries Time
Circulation Stopped (09:00 01/01/94) and Time Logger At Bottom (07:45 02/01/94) -
a ~22.75 h shut-in - and the GFZ data report states all KTB single temperature
logs are drilling-disturbed. So the entry is carried as a MUD-TEMPERATURE log, not
equilibrium; the reader parses the disturbance-relevant header fields into stream
meta and the gate PINS them. A future closed-stream comparison against this log
must model the disturbed state or disclose the mismatch - the two-stream
discipline applied to a 30-year-old measurement.

Also recorded: the fetch-route forensics (GDR/OEDI = blocked binary; GFZ datapub =
ZIP; the ICDP legacy Apache tree = per-log text files, found via directory
walking) - the connectivity ladder's offline-ingest tier exercised at its
adversarial edge. New machinery: read_ktb_dat + .dat dialect in the loader.

Catalogue standing: TWELVE entries / NINE regions / SEVEN kind-strings (log
excerpts x4, complete log x1, ice temperature curves x2, HOT temperature excerpt
x1, real trajectory x1, core analysis x1, production time series x1). Package
v1.22.0; gate 5,860 -> 5,862.

---

## APPENDED 2026-08-25 (14) — v1.23.0: CATALOGUE ENTRY 13 — THE TWIN-LEG COMPARISON EXISTED IN 1988 HARDWARE

**KTB Pilot Hole (VB1A), temperature log VB-251** (07 Nov 1988, ICDP legacy KTB
Information System): 1,082 verbatim six-column rows, 3,268 -> 3,433 m at 95-101
degC - and the find is the INSTRUMENT: a twin-sensor temperature sonde, two
calibrated sensors 1,140 mm apart, carrying its own accuracy specification in the
file header (absolute 0.05 degC, relative 0.01 degC - a real, citable instrument
spec of exactly the kind the v1.5.0 gauge-spec layer demands).

The physics of the pair is the thesis of this whole program in miniature: the
trailing sensor passes through mud the leading sensor just disturbed, and reads
COOLER at every one of 1,082 rows (mean offset 0.87 degC, all-positive,
gate-pinned). Two co-located channels, one physical cause, a measurable
systematic offset between them - the twin-leg comparison the simulator runs
synthetically (UQFF leg vs conventional leg) was being run in hardware in 1988,
and its residual is in the record.

Real artifacts, pinned verbatim: a 69-row sensor-settling FROZEN run at log start
(the frozen-value fault class arising from thermal physics, not electronics - the
QC pipeline's stuck-detector would flag it, and would be wrong about the cause: a
classification lesson for the reconciler) and the head-tension collapse 279 -> 111
lbf at the 3,425 m stand-up the header itself announces. Refusal discipline: the
header's TLAB field is empty in the source and stays absent from meta.

Port upgrade #6 driven by real data: read_ktb_dat now parses the column-definition
block DYNAMICALLY (names + units from the file), verified against both the
6-column VB log and the 4-column HB log. Catalogue standing: THIRTEEN entries /
NINE regions; KTB is the first complex with two catalogued boreholes (Main +
Pilot). Package v1.23.0; gate 5,862 -> 5,864.

---

## APPENDED 2026-08-25 (15) — v1.24.0: CATALOGUE ENTRY 14 — THE STRAIGHTEST DEEP HOLE AS A NULL CONTROL

**KTB Main Hole TVD file (0-9,080 m; first 2,804 rows at exact 1 m sampling)**:
the second real trajectory in the catalogue, chosen for being the OPPOSITE of the
first. L06-06 is a real S-shaped deviated well that bends the engine's pressures;
KTB-HB's vertical-drilling-system section holds |TVD - MD| <= 0.35 m over 2.8 km -
the deepest research borehole on Earth is, in this section, among the straightest
ever drilled. A deviation survey whose correct physical effect is almost exactly
NOTHING is a null control: if the closed stream's MD->TVD machinery produces a
material pressure shift on this data, the machinery is wrong.

Honesty items, pinned: the source's ~0.152 m datum offset at MD 0 (TVD starts at
0.15239, and TVD exceeds MD in the top ~1,400 m) is PRESERVED, not corrected -
the naive TVD<=MD invariant fails on this real file for a documented reason, which
is exactly the kind of lesson synthetic data never teaches. And a transcription-
method disclosure: the 2,804 highly regular rows were reproduced by run-faithful
transcription (every run boundary and all 32 exceptional rows read directly from
the capture, hard-coded, then structurally verified: row count, exact MD sequence,
TVD monotonicity, drift envelope, 16 spot rows) - method stated in provenance,
source URL carried for independent byte-level re-verification.

Milestone: KTB-HB becomes the FIRST WELL with both temperature (entry 12) and
trajectory (entry 14) in the catalogue - the closed stream can now describe one
real well's geometry and thermal state entirely from catalogued real data. Port
upgrades #7 and #8: survey() accepts ktb_dat TVD files; the KTB column-block
parser's format-code match widened (F -> F\d*) - three KTB dialects (4-column
temp, 6-column twin-sensor, 2-column TVD) on one parser.

Catalogue standing: FOURTEEN entries / NINE regions / EIGHT kind-strings / TWO
real trajectories. Package v1.24.0; gate 5,864 -> 5,866.

---

## APPENDED 2026-08-25 (16) — v1.25.0: CATALOGUE ENTRY 15 — REAL DENSITY, REAL OVERBURDEN: THE PRESSURE SIDE GETS ITS INGREDIENT

**KTB-HB borehole gravimetry, 0-8,400 m, COMPLETE file** (EDCON tool, KTB deep
crustal lab 1996, Univ. Bochum reduction): 197 stations of in-situ apparent
density - the crust weighing itself, 2.55-2.95 g/cm3 over 8.4 km, with every
reduction constant carried in the header (IGSN71 tie, IGF 1967, free-air
gradient, reduction density 2.742).

Two closures in one entry. FIRST, the transcription cross-check nobody had to
invent: the file states its own average well density (2.752 g/cm3), and the mean
of the 196 transcribed rock stations reproduces it to the millidigit - the source
document audits the catalogue copy. SECOND, the pressure side: the catalogue had
temperature, geometry, rates, core, but nothing to build PRESSURE from. Now the
gate integrates rho*g*dz from measured density over measured TVD live on every
run: overburden at TD = ~226 MPa = ~32,750 psi at 8,364 m - real crustal
overburden landing exactly in the simulator's 30,000-psi-class HPHT regime.

Honesty structure, pinned: surface station RHO = 0.000 is the gravity reference
tie, pinned as NOT-a-rock-density (an integral that used it naively would be
wrong - the pin handles it explicitly and discloses the handling); the -1.7 mGal
discontinuity at the 5,990 -> 6,000 m run boundary is the header's own tool-size
change, preserved as real survey structure; GRAV is not monotonic because real
surveys re-occupy tie stations. And the deep TVD divergence (MD 8,400 -> TVD
8,364) records the HB's deep deviation - the region entry 14's capture could not
reach, so the two trajectory sources now bracket the hole.

Milestone: KTB-HB carries TEMPERATURE (entry 12) + TRAJECTORY (entry 14) +
DENSITY (entry 15) - the first well the closed stream can describe (thermal
state, geometry, overburden) entirely from catalogued real data. Catalogue
standing: FIFTEEN entries / NINE regions / NINE kind-strings. Package v1.25.0;
gate 5,866 -> 5,868.

---

## APPENDED 2026-08-25 (17) — v1.26.0: CATALOGUE ENTRY 16 — STRENGTH MEETS OVERBURDEN: THE GEOMECHANICS PAIR CLOSES ON REAL DATA

**KTB Pilot Hole core compressive-strength table (COMPLETE, 113 samples,
190-3,832 m)**: the catalogue's first laboratory rock-strength data - UCS 3.2 to
265.4 MPa with E-modulus, rock type, foliation dip, and sampling timestamps from
the 1987-89 KTB field laboratory.

The entry exists for one comparison, and the gate now runs it live: entry 15
measured the crust's density (2.752 g/cm3 mean, borehole gravimetry); entry 16
measures what that crust can BEAR. Dividing one by the other, 59 OF 113 SAMPLES
ARE WEAKER THAN THE OVERBURDEN AT THEIR OWN DEPTH - the weak foliated gneisses
(mean ~49 MPa) sitting under loads their amphibolite neighbours (~137 MPa) shrug
off. That imbalance is the documented physical reason the KTB pilot hole
developed breakouts, and it is now COUNTED from catalogued data in a pin, not
asserted from literature. Strength-vs-overburden is the two-stream comparison
operating at the geomechanics level: a closed-stream load model meeting measured
capacity, with the residual classified.

Refusal discipline reaches the CELL level with this entry: the source declares
TAB separators; the legacy HTML rendering collapses them, so an empty interior
cell loses its position in short rows. The read_ktb_table reader assigns trailing
tokens by DECLARED COLUMN TYPE only - a token with a decimal point cannot belong
to the I2 dip column - and the 9 rows whose trailing integer could be either an
integer-valued E-modulus or a dip are REFUSED: both cells NaN, the raw token
preserved in a per-row quality flag, the source URL carried for byte-level
(tab-preserving) resolution. Nothing is guessed from geology.

Catalogue standing: SIXTEEN entries / NINE regions / TEN kinds. KTB now
contributes five entries across four kinds; the VB (like the HB before it)
carries two. A small HB strength table exists at the same site and is noted in
provenance as not-yet-catalogued. Package v1.26.0; gate 5,870 -> 5,872.

---

## APPENDED 2026-08-25 (18) — v1.27.0: CATALOGUE ENTRY 17 — THE STRENGTH PAIR COMPLETES, AND DEPTH WINS

**KTB Main Hole core strength table (COMPLETE, 21 samples, 4,151-7,400 m)**: the
companion to entry 16, and the closing panel of the KTB geomechanics triptych.
The HB was mostly cutting-drilled, so its core is sparse and deep - 20
amphibolites (96.6-307.9 MPa) and a single muscovite gneiss (49.1 MPa at 5,282 m)
that replays the VB weak-foliation story three kilometres deeper.

With entries 15+16+17 together the gate now tells the whole mechanical story of
the deepest borehole complex on Earth from catalogued data alone: the Pilot
Hole's mixed section averages 77 MPa and fails against its own overburden at 59
of 113 sample depths (breakouts); the Main Hole's amphibolites average 199 MPa -
which is WHY a 9.1 km hole could stand - and yet at 5.5-6.2 km even amphibolites
begin to lose to the density-derived load (5 of 21 samples below their own
overburden, the gneiss under a 2.9x excess). Strength is lithology; load is
depth; depth wins eventually. All of it counted live in pins, none of it
asserted from literature.

Reader maturity note: read_ktb_table needed ZERO changes for this file - the
typed-column parser, the type-declared assignment rule, and the ambiguous-cell
refusal (4 rows here) generalized from the VB table unchanged. Five KTB dialects,
two readers.

Catalogue standing: SEVENTEEN entries / NINE regions / TEN kinds; KTB contributes
SIX entries and both of its holes now carry temperature AND strength data.
Package v1.27.0; gate 5,872 -> 5,874.

---

## APPENDED 2026-08-25 (19) — v1.28.0: CATALOGUE ENTRY 18 — THE OCEAN'S KTB, AND A SOURCE FAMILY THAT CITES ITSELF

**ODP Hole 504B borehole fluids, Leg 137** (PANGAEA doi:10.1594/PANGAEA.805957,
COMPLETE): the deepest hole in oceanic crust - the exact oceanic counterpart of
the KTB arc - joins as region TEN and the catalogue's first SUB-SEAFLOOR entry
(seafloor -3,474 m; ambient in-hole >160 degC). Eight samples, 350-1,550 mbsf,
42 numeric channels: pH, majors, traces, and a full isotope suite.

The entry's physics is a mixing gradient, and the gate computes it rather than
quotes it: Mg falls with depth (corr -0.81) as Ca rises (+0.80), and 87Sr/86Sr
slides from the seawater value (0.709212) toward basaltic (0.707575) - the ocean
reacting with the crust, sampled in a borehole. Honesty inherited from the source
paper itself: these are BOREHOLE fluids, not confirmed formation waters (in-hole
reaction with rubble is the authors' preferred reading), and that framing is the
entry's framing. The near-seawater parcel at 950 m and the trailing-cell NaN
padding are real structure, preserved.

The route matters as much as the entry: after the LDEO .dat family proved
fetch-blocked (octet-stream) and the Chrome fallback was unavailable, the
PANGAEA TEXTFILE EXPORT route was proven - complete datasets served as
tab-separated text whose header carries its OWN citation, abstract, coordinates,
per-parameter methods and license. read_pangaea_txt parses that self-description
into stream meta: the first source format in the catalogue that arrives already
citing itself. Fetch forensics recorded in provenance; a provenance-grade source
family is now open for everything after this.

Catalogue standing: EIGHTEEN entries / TEN regions / ELEVEN kinds. The two
deepest-borehole programmes on Earth - continental (KTB) and oceanic (504B) -
are both in the record. Package v1.28.0; gate 5,874 -> 5,876.

---

## APPENDED 2026-08-25 (20) — v1.29.0: CATALOGUE ENTRY 19 — MEASURED PRESSURE ARRIVES, AND IT IS THE FIND

**IODP Site U1324 in-situ pore pressure** (PANGAEA doi:10.1594/PANGAEA.725472,
COMPLETE; Gulf of Mexico, region ELEVEN): 18 penetrometer deployments, 50-608.2
mbsf. This closes the physical-quantity ledger the catalogue has been assembling
since entry 1: temperature, trajectory, density, strength, rates, core, fluids -
and now MEASURED DOWNHOLE PRESSURE, the twelfth kind, the quantity the simulator's
gauges exist to read.

The dataset is the two-stream thesis in miniature, because the file carries its
own baselines: per-station HYDROSTATIC pressure (the closed-stream null model)
and OVERBURDEN (the ceiling), alongside the measurement. The gate computes the
residual live: ALL 12 baselined stations read above hydrostatic - max +2.07 MPa,
with lambda* = 0.385 at the 608.2 m headline station (18.80 measured / 16.73
hydrostatic / 22.11 overburden MPa). That residual is not instrument error; it is
the rapid-sedimentation overpressure that preconditions the submarine landslides
this expedition was mounted to study. THE FIND - the offset undervalued data
stream of Daniel's founding ruling - occurring in nature, in a file whose own
structure proves it.

Instrument lineage note: the T2P penetrometer reports TIP and SHAFT pressure
sensors as separate rows at the same depth - the catalogue's second real
dual-sensor instrument (after the KTB twin-temperature sonde). The duplicate-depth
pairs are preserved, and tip rows' blank baseline cells stay NaN because the
source reports baselines once per deployment. read_pangaea_txt required ZERO
changes - the PANGAEA source family generalizes on its second entry.

Catalogue standing: NINETEEN entries / ELEVEN regions / TWELVE kinds - onshore
and offshore, continental and oceanic crust, ice and 185 degC rock, from first
oil to lab bench, with every quantity the closed stream needs now present as
real data. Package v1.29.0; gate 5,876 -> 5,878.

---

## APPENDED 2026-08-25 (21) — v1.30.0: CATALOGUE ENTRY 20 — THE CATALOGUE MEETS ITS OWN SUBJECT

**ODP Hole 1027C CORK observatory** (PANGAEA doi:10.1594/PANGAEA.722627,
COMPLETE; Juan de Fuca Ridge flank, region TWELVE): the twentieth entry is a
SEALED-BOREHOLE PERMANENT OBSERVATORY - the physical instrument class this
entire package exists to simulate. A CORK is the real permanent downhole gauge:
installed 1996, data recoveries 1997/1999/2000, a logger REPLACED in 1999,
status 'Operational (pressure only)' - the ServiceLifeSimulator's decade, as
recorded history in the file's own Comment block, alongside the formation
-pressure summary (-69 kPa initial -> -26 kPa equilibrium: young crust slightly
UNDERpressured - the mirror image of entry 19's Gulf of Mexico overpressure).

The data is one profile measured twice, and it closes the catalogue's oldest
honesty thread: at the same 10 thermistor stations, the drilling-disturbed
state at installation (max 19.6 degC) and the near-equilibrium state after
three sealed years (max 60.7 degC) - a +42.6 degC recovery at 586.8 m. Entries
12 and 13 could only DISCLOSE that KTB logs were disturbed; entry 20 measures
the disturbance AND the recovery. And the sealed profile computes the
Davis-Becker physics live in the gate: ~104 degC/km of conductive sediment
gradient collapsing to an ISOTHERMAL basement (0.1 degC spread, vs 1.1 while
disturbed) - hydrothermal circulation homogenizing young oceanic crust.

read_pangaea_txt: zero changes, third entry on the parser.

TWENTY ENTRIES. Twelve regions, thirteen kinds, five continents' worth of
basins, both deepest-borehole programmes on Earth, every physical quantity the
closed stream needs, and now the real version of the instrument the closed
stream simulates. Package v1.30.0; gate 5,878 -> 5,880.

---

## APPENDED 2026-08-25 (22) — v1.31.0: CATALOGUE ENTRY 21 — THE CATALOGUE STARTS DOING SCIENCE WITH ITSELF

**Thermal conductivity of ODP Hole 1027B** (PANGAEA doi:10.1594/PANGAEA.792214,
COMPLETE JANUS shipboard set): 32 needle-probe measurements at the same site as
entry 20's CORK observatory. Fourteenth kind - and the entry exists for a
computation, not a collection: heat flow.

q = k x dT/dz needs two measured ingredients that never travel in one file: the
rock's conductivity (from core, on deck) and the formation's gradient (from a
sealed borehole, years later). The catalogue now holds both, from the same site,
each with its own provenance chain - so the gate computes the flux live on every
run: mean k 1.43 W/m/K (harmonic 1.42 - the layered-media average disclosed and
computed beside it) times the CORK's sealed 91 K/km over the overlapping interval
= ~130 mW/m2. Young-crust heat flow, an order of magnitude above continental,
derived from two catalogued datasets rather than quoted from a paper. This is
the closed stream's promise operating one level up: not simulating measurements,
but COMPOSING them.

Honesty structure: the source's bimodal depth coverage (5 shallow, 27 deep,
nothing archived between) is preserved and pinned as source structure - no
interpolation across the gap; probe lineage (FULL vs HALF needle, system and
probe IDs) rides with every measurement; the DOI was found by probing JANUS's
sequential numbering (1024A = 792208 -> 792214 = 1027B, first probe), recorded
in provenance as the discovery route.

Catalogue standing: TWENTY-ONE entries / TWELVE regions / FOURTEEN kinds; two
multi-dataset site families (KTB-HB: T + trajectory + density; Site 1027: T +
k -> heat flow). read_pangaea_txt unchanged on its fourth entry. Package
v1.31.0; gate 5,884 -> 5,886.

---

## APPENDED 2026-08-25 (23) — v1.32.0: CATALOGUE ENTRY 22 — 1979, AND THE DATASET THAT AUDITS ITSELF

**Physical properties of DSDP Hole 69-504B** (PANGAEA doi:10.1594/PANGAEA.221630,
COMPLETE): the catalogue's first DSDP-era entry - the GLOMAR CHALLENGER, 1979,
drilling the first 489 m of what would become the deepest hole in oceanic crust.
61 basalt samples, 281-484 mbsf: porosity 2.66-11.39% (fresh massive flows vs
altered breccia horizons - newborn crust's alteration architecture), bulk density
2.73-2.95, grain density 2.94-3.03 g/cm3, every sample carrying its DSDP core
label.

The entry's distinction is epistemological: it is the first catalogued dataset
BOUND BY AN INTERNAL IDENTITY. Porosity, grain density and bulk density are not
three independent numbers - physics ties them: WBD = phi*rho_w + (1-phi)*rho_g.
The file carries all three, so the gate re-runs the 1979 laboratory's bench
consistency on every run: ALL 61 ROWS CLOSE (mean |residual| 0.0028 g/cm3, max
0.0096). One pin, three services: it audits the lab, audits PANGAEA's archival
chain, and audits this catalogue's transcription - a copy error in any of the
three columns would break the identity. The verbatim discipline now has a
dataset that enforces itself.

Family note: 504B joins KTB-HB and Site 1027 as the third multi-dataset family -
entry 18's borehole fluids (reacting at >160 degC) and entry 22's rock (the very
basalts those fluids react with), drilled 12 years apart from two different
vessels, reunited in one catalogue.

Catalogue standing: TWENTY-TWO entries / TWELVE regions / FIFTEEN kinds,
spanning 1971 (L07-01) to 2016 (Volve production) on the industry side and
1979 (Glomar Challenger) to 2005 (IODP 308) in scientific drilling.
read_pangaea_txt unchanged on its fifth entry. Package v1.32.0; gate
5,886 -> 5,888.

## APPENDED 2026-08-25 (24) - v1.33.0: entry 23, ODP 1165B Prydz Bay (ANTARCTICA) - the replicate audit that caught a source typo

Catalogue entry 23 is the complete thermal-conductivity dataset of ODP Hole 188-1165B (PANGAEA
doi:10.1594/PANGAEA.792386): 81 needle-probe measurements, 3.75-503.65 mbsf, k = 0.432-1.062 W/m/K,
Prydz Bay, Antarctic continental rise (-64.3797 S, 67.2190 E, seafloor -3,538 m, Leg 188, 2000).
Antarctica becomes region THIRTEEN and the catalogue's span is now literally pole-to-pole.

The structural landmark: the file's Comment column carries the three raw replicate readings whose mean
is the archived k on every row - a dataset that ships its own repeatability record. The gate re-runs the
shipboard averaging on all 81 rows. Result: 80 close within rounding; the single non-closing row
(317.35 m: replicates 1.013, 0.016, 1.031 vs archived 1.0200; printed-replicate mean 0.687) is a dropped
leading digit IN the source archive - substituting 1.016 restores the identity to the fourth decimal.
Rule 7 handling: the row is preserved verbatim, the anomaly is disclosed in the provenance sidecar, and
the gate pins the DETECTION (80/1 split + the 1.016 restoration) rather than silently repairing the file.
The catalogue's verification discipline now detects upstream archival errors as a side effect of
verifying its own transcription - the same structural self-audit class as entry 22's WBD identity.
Gate 5,888 -> 5,890. Package v1.33.0. Reader unchanged (read_pangaea_txt, fifth dataset).

## APPENDED 2026-08-26 (25) - v1.34.0: entry 24, ODP 111-504B sheeted-dike elastic moduli - the four-identity audit

Catalogue entry 24 is the complete Christensen/Wepfer/Baud (1989) laboratory table for the sheeted-dike
complex of Hole 504B (PANGAEA doi:10.1594/PANGAEA.754017): 8 dike core samples from Leg 111, each swept
through confining pressures 200-6,000 bar, with Vp, Vs, Vp/Vs, Poisson's ratio, bulk and shear moduli,
ambient density and porosity - 519 cells / 63 rows, verified against the header's own Size declaration.
504B becomes a THREE-dataset site family across three expeditions and 24 years of measurement type
(1979 physical properties, 1986 dike elastics, 1991 borehole fluids at >160 C) - one hole, sediment to
sheeted dikes, rock frame to pore fluid.

Structural landmarks: (1) FIRST pressure-swept laboratory dataset and kind SIXTEEN; (2) first
label-indexed PANGAEA export - read_pangaea_txt gained a no-depth ordinal-index fallback, with all six
prior depth-indexed .txt entries regression-verified unchanged; (3) the densest self-audit in the
catalogue: FOUR internally-derivable columns re-derived by the gate on every run (Vp/Vs 63/63 max dev
0.0054; Poisson via (r^2-2)/(2(r^2-1)) 63/63 max dev 0.011; shear modulus rho*Vs^2 and bulk modulus
rho*(Vp^2 - 4/3*Vs^2) on all 56 density-bearing rows, max dev 930 / 1,168 MPa against the table's
1,000-MPa rounding); (4) the sweep's monotonic-pressure structure detected two source-archive quirks,
preserved verbatim per Rule 7: sample 161R's nine rows led by an out-of-sequence duplicate 6,000-bar
row while neighbouring 155R is missing its 6,000-bar row (the orphan continues 155R's pressure trend
exactly - consistent with a one-row attribution slip in the source table), and sample 148R's absent
density and 400-bar step. Disclosed in provenance, pinned as detections, not repaired.
Gate 5,890 -> 5,892. Package v1.34.0.

## APPENDED 2026-08-26 (26) - v1.35.0: entry 25, DSDP 69-504B sound velocity - the cross-entry impedance join

Catalogue entry 25 is the complete Leg 69 shipboard sonic dataset for Hole 504B (PANGAEA
doi:10.1594/PANGAEA.229754, found first-probe by sequential-DOI reasoning from the 69-505 sibling):
63 compressional-wave measurements on the 1979 basalt cores, 279.08-484.04 mbsf, Vp 5,105-6,390 m/s.
504B becomes a FOUR-dataset site family - 1979 sound velocity, 1979 physical properties, 1986 sheeted-
dike elastic moduli, 1991 borehole fluids - the deepest scientific record of any site in the catalogue.

The structural landmark is the catalogue's first CROSS-ENTRY SAMPLE-BY-SAMPLE JOIN: the sonic table
and the physical-properties table archive the same core suite as separate PANGAEA datasets, and
joining on depth (|dz| <= 0.05 m) pairs 60 of 63 rows - four at identical cm positions (6-1,55;
7-5,3; 8-3,73; 13-2,100). The gate computes a live acoustic-impedance profile of ocean-floor basalt,
Z = rho x Vp = 13.94-18.50 x1e6 kg/m2/s (mean 16.59), from two independently archived datasets on
every run - the physics that seismic reflection imaging is built on, running as a fidelity assertion.
Disclosure: the profile's only duplicate depth is a repeat measurement archived twice (484.04 m,
sample 29-1,4: 5,105 vs 5,136 m/s = 0.6% repeatability spread), preserved verbatim and pinned.
Gate 5,892 -> 5,894. Package v1.35.0. Reader unchanged (read_pangaea_txt, depth-indexed path).

## APPENDED 2026-08-26 (27) - v1.36.0: entry 26, Nankai megasplay shear strength - the slope-stability re-derivation

Catalogue entry 26 is the complete laboratory shear-strength table behind Ikari, Strasser, Saffer &
Kopf (2011, EPSL 312): submarine-landslide potential near the Nankai megasplay fault (PANGAEA
doi:10.1594/PANGAEA.786715, 150 cells / 15 rows, full abstract preserved in the header). A double
first: the NANKAI TROUGH accretionary prism joins as region FOURTEEN - the catalogue's first
subduction-zone data and first entry drilled by D/V Chikyu - and slope-sediment shear strength is
kind EIGHTEEN, the soft-sediment counterpart to the KTB crystalline strength tables (entries 16/17).
15 measurements from three holes spanning the megasplay (C0001E/C0004C/C0008A, slopes 3/7/12 deg),
7.91-121.29 mbsf, tau = 40-470 kPa.

Live physics: the gate re-derives the paper's HEADLINE CONCLUSION on every run - infinite-slope
driving stress sigma'_v*sin(a)*cos(a) vs measured strength gives factor-of-safety 2.38-15.31 with all
15 stations statically stable, exactly the published "slopes are stable and submarine landslides are
not expected to occur under static conditions." Second audit: the effective/total stress ratio sits
in a tight buoyancy band 0.359-0.413 across all three holes. Third: a source labeling inconsistency
detected by cross-checking the file's own two label columns - all ten Expedition-316 rows carry Event
'316-C000xx' but sample labels prefixed '315-', an expedition-number typo in the source table,
preserved verbatim and disclosed per Rule 7. Gate 5,894 -> 5,896. Package v1.36.0. Reader unchanged.

## APPENDED 2026-08-26 (28) - v1.37.0: entry 27, ODP 118-735B gabbro elastic moduli - the crustal ladder completes

Catalogue entry 27 is the complete Table 4 of Iturrino, Christensen, Kirby & Salisbury (1991):
average velocities and elastic constants for the Atlantis Bank gabbros of ODP Hole 118-735B (PANGAEA
doi:10.1594/PANGAEA.757872; 1,144 cells / 104 rows verified against the header's own Size
declaration; reached via the parent publication-series page - bundle DOIs do not export textfile,
child tables do, a route note now recorded in provenance). The SOUTHWEST INDIAN RIDGE joins as
region FIFTEEN (seafloor -731 m, the catalogue's shallowest ocean site), and with it the catalogue
COMPLETES THE OCEANIC-CRUST LADDER: sediments -> pillow basalts (504B Leg 69) -> sheeted dikes
(504B Leg 111) -> layer-3 gabbro (735B Leg 118) - the full ophiolite sequence held as verbatim
public data. 13 gabbro samples x 8 confining pressures (100-2,000 bar), Vp 6,350-7,310 m/s,
Vs 3,510-4,040 m/s, density 2.84-3.27 g/cm3, full petrographic modal mineralogy in every row.

FIVE audits pinned: the four elastic identities close on ALL 104 rows (density rides on every row,
unlike the dike table) - Vp/Vs max dev 0.0077, Poisson max dev 0.0059, G = rho*Vs^2 max dev 671 MPa,
K = rho*(Vp^2-4/3*Vs^2) max dev 792 MPa vs the table's 1,000-MPa rounding - plus a fifth unique to
this entry: the modal percentages in each sample's verbatim comment sum to ~100% on all 13 samples,
parsed live from the file. Four source spelling quirks preserved and pinned as presence checks (the
dataset's own PANGAEA title says 'share-wave'; 'Grabbo'; 'tracee'; '10 oxides' missing its percent
sign) - the archive's fingerprints, kept, not cleaned. Same Christensen laboratory lineage as the
504B dike entry: the two pressure-sweep tables are now directly comparable dike-vs-gabbro physics.
Gate 5,896 -> 5,898. Package v1.37.0. Reader unchanged (ordinal fallback, second use).

## APPENDED 2026-08-26 (29) - v1.38.0: entry 28, ODP 209-1274A mantle peridotite - the ladder goes below the crust

Catalogue entry 28 is the complete shipboard moisture-and-density dataset of ODP Hole 209-1274A
(Miller/Kelemen/Kikawa, PANGAEA doi:10.1594/PANGAEA.259148; 180 cells / 18 rows; found by a
three-probe sequential-DOI walk of the leg-ordered JANUS MAD series: Leg 204 at 259099 -> Leg 209
Hole 1271A at 259145 -> 1274A at 259148). The MID-ATLANTIC RIDGE joins as region SIXTEEN:
serpentinized mantle harzburgite from the 15deg20min Fracture Zone, 17.79-146.93 mbsf, 22.2%
hard-rock recovery. THE LADDER IS COMPLETE FROM SEAFLOOR MUD TO THE MANTLE: sediments -> pillow
basalts (504B Leg 69) -> sheeted dikes (504B Leg 111) -> layer-3 gabbro (735B Leg 118) -> residual
peridotite (1274A Leg 209).

The physics is in the numbers: every grain density (2.588-2.823 g/cm3) sits far below fresh
peridotite's ~3.3 - the mass deficit that hydration of the mantle leaves behind, visible in a
moisture-and-density table.

The audit is the FIVE-IDENTITY LOCK, the cleanest fully-interlocked table in the catalogue: WBD =
phi*rho_w + (1-phi)*rho_grain (max dev 0.001 g/cm3), DBD = (1-phi)*rho_grain (0.0016), void ratio
e = phi/(1-phi) (0.0008), and both water contents from WBD/DBD (0.05% / 0.07%) - all five re-derived
by the gate on all 18 rows. No archival anomalies detected: a 2003 shipboard laboratory whose
arithmetic still audits perfectly 23 years later. Gate 5,898 -> 5,900. Package v1.38.0. Reader
unchanged (read_pangaea_txt, depth-indexed path).

## APPENDED 2026-08-26 (30) - v1.39.0: entry 29, Chicxulub M0077A peak-ring P-wave - the crater that ended the Cretaceous

Catalogue entry 29 is the complete discrete-sample P-wave dataset of IODP Hole 364-M0077A (PANGAEA
doi:10.1594/PANGAEA.883479): 717 rows / 2,170 cells, 506.17-1334.51 mbsf - 828 m of velocity profile
through the post-impact sediments, suevite, impact melt and shocked peak-ring granite of the
CHICXULUB CRATER, drilled by mission-specific platform L/B Myrtle in 19.8 m of water on the Yucatan
shelf. Region SEVENTEEN; first impact structure; largest verbatim PANGAEA table in the catalogue.

The physics is the K-Pg impact itself: the 523 granite-basement rows average 4,171 m/s and no sample
in the entire profile reaches 5,400 m/s, against intact granite's 5,500-6,000 - the measured
velocity deficit IS the pervasive shock damage that let the peak ring rise after the impact that
ended the Cretaceous. Archive fingerprints preserved verbatim: a repeat measurement archived twice
(44R-3,54-56: 3,082/3,118 m/s, 1.2%), 38 non-monotonic archival steps including the 37R-40R block
filed 600+ m out of place, and 19 shipboard QC comments ('poor signal', 'dolerite', 'dyke?', 'QAQC').

The structural landmark: A DATASET THAT CHECKSUMS ITS OWN TRANSCRIPTION. Depth = Top + (midpoint of
the sample label's cm interval)/100 holds EXACTLY on every row, including fractional intervals
(232R-1,91-93.5 -> 1116.4125) and a decimal-start oddity (299R-2,84.1-96 -> 1321.3005). The gate
re-runs this identity on all 717 rows and re-derives the header's own Size declaration
(3 x 717 + 19 = 2,170) on every run - any copying error in label, Top or Depth breaks the pin.
Transcribed in two parts; checksum passed on first verification. Gate 5,900 -> 5,902. Package
v1.39.0. Reader unchanged (read_pangaea_txt, depth-indexed path; file order preserved as archived).

## APPENDED 2026-08-26 (31) - v1.40.0: entry 30, ACEX Lomonosov age-depth model - the thirtieth entry reaches the pole

Catalogue entry 30 - the milestone entry - is the canonical ACEX age model (Backman et al. 2008,
PANGAEA doi:10.1594/PANGAEA.705517, COMPLETE 38 cells / 10 control points): the age-depth backbone
of the first scientific drilling of the central Arctic Ocean. The CENTRAL ARCTIC OCEAN joins as
region EIGHTEEN - 87.89 N on the Lomonosov Ridge, 235 km from the North Pole, drilled from the
icebreaker Vidar Viking in moving sea ice - first icebreaker entry, first composite virtual core
(spliced from Holes M0002A/M0003A/M0004A/M0004C). AGE-DEPTH GEOCHRONOLOGY is kind NINETEEN: the
catalogue's first time axis - every earlier entry measures the state of the subsurface; this one
dates it. 399.63 m of composite core spanning 56 million years.

The structure IS the science: both ACEX hiatuses are encoded in the table itself - 198.70 m appears
twice (ages 18,200 and 44,400 ka: the same centimetre of seafloor is both early Miocene and middle
Eocene, a 26.2-Myr unconformity held as a duplicate-depth pair), and the 2.2-Myr Miocene hiatus sits
between 135.49 and 140.44 m. The audit re-derives ALL SIX sedimentation rates live as
delta-depth/delta-age between hiatus-aware bounds - the A-B rate closes ONLY when the Miocene hiatus
is excluded, so the audit verifies the hiatus itself - with B-C at the exact rounding boundary
(0.8051 -> archived 0.80, tolerance set to the honest half-ulp 0.006 and disclosed). The header's
own Neogene average closes (198.7/16.0 = 12.4 m/Myr). Rule 7 disclosure: the archive's Comment field
is TRUNCATED mid-sentence in the source ('...Average sedimentation'), preserved verbatim including
the cut, the missing Paleogene rate re-derivable at 206.1/11.8 = 17.5 m/Myr.

Thirty entries in, the catalogue spans pole to pole (Prydz Bay to the Lomonosov Ridge), seafloor mud
to mantle peridotite, a 66-Myr-old impact's shock damage to day-indexed production data - eighteen
regions, nineteen kinds, every dataset verbatim, every flaw kept, every derivable number re-earned
by the gate on every run. Gate 5,902 -> 5,904. Package v1.40.0. Reader unchanged.

## APPENDED 2026-08-27 (32) - v1.41.0: the independent evaluation, the finish sequence, and step 1 (Modbus unification)

Daniel supplied an independent component-inventory and gap analysis of the v1.30.0 simulator and
ruled: "I want to follow the plan if it looks right." Verification against the code confirmed all
four spot-checked claims (registry/client split as seen statically; engine consuming only
depth/pressure/temp with template anchors; 141-line v1.0-era Qt app; ToolString not driving step()).
Two stale numbers corrected for the record (catalogue is now 30 entries / 18 regions / 19 kinds
after v0.402.0; gate 5,906) - neither changes any finding. THE PLAN IS ADOPTED as the standing
finish sequence: (1) modbus unification, (2) well assembler, (3) engine on measured P/T, (4)
operator UI, (5) acceptance suite = finished offline product; (6) mixed toolstring + gamma/LWD,
(7) one live site path, (8) bench-test protocol for the 1.0324 suppression ratio = field product.
The evaluation's physics-honesty clause is canonized: DERIVED_HYBRID stays DERIVED_HYBRID.

Step 1 executed (v1.41.0): the split was already unified AT RUNTIME (uqff_modbus upgrades the
registry entry at package import - the evaluator's static read could not see it), so the fix is
two-fold honesty hardening: the static source of uqff_ports.py now discloses the import-time upgrade
(a source-honesty pin guards the disclosure), and the config-validation path is disciplined - a call
missing host/register_map refuses in the port discipline's own voice naming exactly what is missing
(citation-mandatory map rule restated), never a raw KeyError, and never refuses when site details
ARE supplied. Loopback re-verified through the registry reader post-edit. Gate 5,906 -> 5,908.
Package v1.41.0. The un-run refusal claim in a shipped source file was itself the bug: a product
must not lie in EITHER direction, including understating what it can do.

## APPENDED 2026-08-27 (33) - v1.42.0: finish-sequence step 2, the well assembler

The evaluation's sharpest finding - "twenty wells are ingested; the engine still only consumes
depth_ft, pressure_psi, temp_F; the data is stranded" - is answered by `uqff_well_assembler.py`:
one WellAssembly per site family, assembled from the catalogue's verbatim entries. Four built-ins
ship: KTB-HB (temperature + trajectory + BHGM density + strength - the four-file family entries
12-17 accumulated), Site 1027 (CORK equilibrium column + thermal conductivity - the heat-flow-
closure pair), U1324 (the catalogue's only MEASURED pore pressure, beside its archived overburden),
and 504B (paired 1979 density + velocity, fluids and dike elastics attached). A generic assemble()
takes any role->(entry, channel) map.

Design rules, all pinned: (1) STRICT lookups - outside measured coverage the assembly refuses,
naming the coverage; it never clamps, never extrapolates, never invents. (2) Labeled derivations -
overburden_kPa() integrates the site's own measured density (KTB: 190.9 MPa at the deepest strength
sample, under its 253-MPa UCS, consistent with the arc's strength-count pins). (3) The engine
bridge to_engine_profile() emits the engine's own WellProfile spanning EXACTLY the measured
temperature coverage, pressure method labeled IN the profile name (Rule 7: measured /
hydrostatic_seawater / hydrostatic_freshwater); where no temperature was measured the bridge
REFUSES to substitute a gradient template - the substitution being exactly the stranding this
module ends. (4) Verified end-to-end: the real UQFFDownholeEngine runs a 3-gauge string inside
KTB's measured 7,743-7,985 m window, base P/T interpolated from the 1994 log. Steps 3 (measured
P/T as default demos) and 4 (operator UI) now have their data object. Gate 5,908 -> 5,910.
Package v1.42.0.

## APPENDED 2026-08-27 (34) - v1.43.0: finish-sequence step 3, measured wells as the default demos

Step 3 closes the evaluation's remaining stranding clauses. (1) demo_config(well) makes the measured
assemblies the engine's default path: gauges hang strictly inside the measured temperature window
(KTB: 25,404-26,198 ft of 1994 log; 1027: the CORK column, never past 612.3 m), td = the measured
window end, and the CLI grows `wells` and `--well` on every subcommand - the 0.465-psi/ft and
0.018-F/ft templates are no longer the demo path, and sites without measured temperature REFUSE via
the assembly bridge rather than fall back. (2) production_live_stream() turns catalogue entry 11's
Volve F-12 MEASURED downhole-gauge pressure into the reconciler's live leg: bar->psi exact and
labeled, NaN days dropped and counted, the source archive's 9-day stuck fault surviving the adapter
at 3,830.27 psi, and the station MD caller-supplied because the archived excerpt does not state the
gauge depth (the adapter refuses to invent it).

The reconciliation result is the arc's best honesty demonstration: Volve F-12 against a static-well
prediction classifies UNEXPLAINED_TREND at ~-1,096 psi/yr - seventeen times outside the drift
envelope - because a producing well's drawdown is reservoir physics, not instrument drift. The
two-stream architecture's founding claim (the closed stream tells you what the live stream should
read IF nothing physical is happening) survives contact with real field data by correctly refusing
to explain depletion away as a gauge problem. Gate 5,910 -> 5,912. Package v1.43.0.
Finish-sequence state: 1 DONE, 2 DONE, 3 DONE; next: 4 operator UI, 5 acceptance suite.

## APPENDED 2026-08-27 (35) - v1.44.0: finish-sequence step 4, the operator surface

Step 4 closes the evaluation's largest hole. Architecture chosen for testability: OperatorSession
is a HEADLESS controller carrying every operator action (well selection from the measured
assemblies or a user CSV; toolstring + rating check; run; service-life; case-study; ingest;
reconcile + undervalued-stream alerts; citations), and the Qt6 window is a thin view over it - so
the product logic is fully gate-tested in an environment with no display, and the GUI layer
refuses with the pip hint where PyQt6 is absent (the ports' own pattern). CLI: 'operator'.

The best moment in the build: the blocking rating check needed no contrived kick zone. The measured
KTB window itself runs to 184 C at its deep end - hotter than the GEOQ 177-class tool's cited
177 C rating - so 'a 177 C tool in a too-hot zone, blocked inside the run' is demonstrated against
the archived 1994 log verbatim: start_run() refuses with the stations named; the only override is
acknowledge_over_rating=True, logged as an explicit operator decision. The citations pane is
permanent and honest per the evaluation's physics clause: suppression labeled DERIVED_HYBRID /
NOT a derived constant in the UI itself, catalogue provenance and licenses per component, tool
sources per hung tool. One API fix en route: ServiceLifeSimulator takes (engine, config) - the
operator's service-life now evaluates rates at the MEASURED well's stations, which is itself a
step-3 dividend. Gate 5,912 -> 5,914. Package v1.44.0.
Finish-sequence state: 1-4 DONE; next: 5 acceptance suite = finished offline product.

## APPENDED 2026-08-27 (36) - v1.45.0: finish-sequence step 5, the acceptance suite - THE OFFLINE-PRODUCT MILESTONE

Step 5 ships the product gate inside the product: acceptance_tests.py, runnable as
'python -m uqff_downhole_simulator accept', 40 checks in six sections (CLI golden runs with seeded
byte-identical determinism goldens; the LAS dialect matrix; the reconciler's six-word classification
vocabulary earned end-to-end on ADAPTIVE synthetic scenarios whose magnitudes come from the
instance's own gates; catalogue verbatim spot pins; the full operator loop; port states). Green on
its first complete run. Independence from the physics corpus is enforced by construction, not
asserted: the fidelity gate executes the suite as a subprocess AND statically verifies the module
never references uqff_calculator or any PAPER_n. The suite immediately paid for itself by catching
a step-3 gap: 'case-study --well' had not been wired through the handler - fixed in this version.

THE MILESTONE: with steps 1-5 of the adopted finish sequence complete - (1) modbus unified,
(2) the well assembler, (3) measured wells as engine defaults, (4) the operator surface, (5) this
suite - the independent evaluation's own criterion is met verbatim: "After 1-5 it is a finished
offline product." Five days ago the simulator was a research library with stranded data and a
v1.0-era GUI; it is now an offline product whose every honesty rule is machine-enforced. The field
tier stays open and unclaimed, exactly as the evaluation drew it: (6) mixed toolstring + gamma/LWD
from the catalogue's own GR curves, (7) one live site path with a real cited register map, (8) the
bench-test protocol that would turn the 1.0324 suppression ratio from simulated composition into
measured physics. Gate 5,914 -> 5,916. Package v1.45.0.

## APPENDED 2026-08-27 (37) - v1.46.0: field-tier step 6a, gamma / lithology from measured curves

The field tier opens. uqff_gamma.py implements the evaluation's "next physics module" - NaI(Tl)-
class GR processing, API units, lithology from GR, LAS curve -> formation flag - working ONLY from
the catalogue's own archived gamma logs. Six entries qualify under unit-disciplined channel
detection, and the discipline is not decorative: the catalogue itself carries the trap cases (KTB
'GRAV' in mGals is gravimetry; 504B 'Density grain' contains the letters G-R; the Texas GR curve is
all-NaN), all excluded by construction and pinned. Results from real logs: the KTB pilot hole's
1,082-point gamma curve yields 80 alternating intervals - metamorphic banding in the gneiss, read
off a 1994 log by a 2026 product - and Volve SR's 5.3-72.5 gAPI span gives the textbook clean-sand-
over-shale split.

Labeling per the Hybrid doctrine, pinned: the linear gamma-ray index is tagged INDUSTRY_STANDARD_
METHOD / NOT a UQFF derivation; the P5/P95 clean/shale picks are tagged STATISTICAL_PICKS
(statistics of THIS log, not formation knowledge); the 0.5 sand/shale cutoff is tagged CONVENTION;
and no detector datasheet ships because none was fetched. Refusals: a flat GR curve (Kennetcook's
constant 46.7) refuses rather than invent contrast; gamma-free entries refuse naming the channels
seen. CLI 'gamma'; acceptance suite grows to 45 checks (section G). Gate 5,916 -> 5,918. Package
v1.46.0. Field-tier remaining: 6b mixed-toolstring step(), 7 one live site path (real cited
register map), 8 the bench-test protocol.

## APPENDED 2026-08-27 (38) - v1.47.0: field-tier step 6b, mixed toolstrings - and Daniel's twin-track audit

Daniel's three-question audit preceded the GO, answered by measurement: (1) THE TWIN TRACK IS
MAINTAINED at every layer - engine legs 0.2363/0.2440 %FS/yr (ratio 1.0324) on the measured KTB
well, service-life per-sensor twin rate arrays with separation curves, the reconciler's twin drift
envelope (67.9 uqff / 70.1 conventional psi/yr at mid-window), twin tool-library entries, the
suppression constant labeled DERIVED_HYBRID in the citations pane. (2) UQFF-catalogue COORDINATION,
honestly inventoried: the quartz extension binds F_TRZ/K_MEX/Phi_res/U_i from the calculator and
those UQFF-composed rates are now EVALUATED AT MEASURED ARCHIVE CONDITIONS (KTB 339.1 F from the
1994 log, not the template), and the UQFF-composed envelope has been CONFRONTED with measured field
data (Volve drawdown, correctly refused as drift) - but no UQFF derivation yet PREDICTS a catalogued
measured value; that coordination is step 8's bench-test territory by design, and U_i remains
loaded-not-used per the evaluation's own honesty clause. (3) The missed-items sweep found three
small real gaps - the gui extra lacked matplotlib, the Qt view lacked an LAS-ingest button and a
drift tab (two of the sweep's own greps were substring false-positives, re-verified before
certifying) - all three fixed in-arc, not deferred.

Then 6b: the engine consumes the ToolString. Per-station models with honest legs (twin /
reference-only / labeled piezo envelope / refused-with-well-P/T-still-streaming), aggregates over
twin stations only with disclosed counts, and the rating check moved INSIDE the engine constructor -
the evaluation's 'blocking inside the run' enforced at the deepest layer, with the acknowledged
override carried on the engine's own rating_report record. Legacy homogeneous path untouched.
Instructive moment: the first mixed-string demo tried to hang a piezo in the KTB window and the
rating check refused - the 1994 log is hotter than the 150 C piezo class EVERYWHERE in its window
(171.7 C at the shallow end) - so the demo moved to the CORK column where every tool is in rating:
the product's own honesty rules now steer test design. Gate 5,918 -> 5,920; acceptance 50 checks.
Package v1.47.0. Field-tier remaining: 7 (one live site path), 8 (bench-test protocol).

## APPENDED 2026-08-27 (39) - v1.48.0: field-tier step 8, the bench-test protocol

Step 8 ships the experiment. BENCH_TEST_PROTOCOL.md (in-package, in the sdist) states the
falsifiable prediction - paired GEOQ-177-class quartz gauges, co-located at a 150 C / 10 kpsi
setpoint, long-term drift-rate ratio R = conventional/UQFF = 1.0324 at unity trims (~2.3 psi/yr
separation at 30k FS) - falsifiable in BOTH directions, with apparatus, >=90-day duration (honoring
the reconciler's own 18-day slope floor: the bench cannot be rushed past the product's standing
rule), procedure, and the labeling rules for both outcomes. Confirmation would move
canonical_suppression()'s label from DERIVED_HYBRID to MEASURED_ON_BENCH with the full test record
attached; refutation keeps DERIVED_HYBRID with the refutation on record; either way there is no
silent retuning of trims to fit the bench, and U_i remains loaded-but-unused until Daniel supplies
its derivation path (Rule 10 - the framework author provides the physics).

uqff_bench.py is the analysis half, verified today: four earned verdicts (MEASURED_CONFIRMS on the
synthetic self-test at R = 1.0263 +/- 0.0118 containing the predicted 1.0324 and excluding 1.0;
MEASURED_REFUTES on a scaled leg - refutation as a first-class outcome; INSUFFICIENT_SPAN under the
18-day floor; INSUFFICIENT_SNR when the band contains both 1.0324 and 1.0). The self-test labels
ITSELF a SIMULATION_SELF_TEST in its own output - arithmetic verified, physics honestly unclaimed:
the product now carries the experiment that would measure its one hybrid constant, and refuses to
pretend the experiment has already happened. CLI 'bench'. Acceptance 55 checks (section I). Gate
5,920 -> 5,922. Package v1.48.0. FIELD TIER: 6a done, 6b done, 8 done; step 7 (one live site path)
is the only remaining item, blocked on real site details - a cited register map and a host - which
only the site can supply.
