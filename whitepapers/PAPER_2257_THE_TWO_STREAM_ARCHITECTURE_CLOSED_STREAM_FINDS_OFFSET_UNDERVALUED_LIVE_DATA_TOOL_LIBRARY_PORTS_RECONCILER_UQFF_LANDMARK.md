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
