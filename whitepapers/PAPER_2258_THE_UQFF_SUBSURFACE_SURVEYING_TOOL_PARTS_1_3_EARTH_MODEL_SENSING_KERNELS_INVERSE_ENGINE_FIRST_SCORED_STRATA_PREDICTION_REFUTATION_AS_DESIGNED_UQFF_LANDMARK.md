# PAPER_2258: The UQFF Subsurface Surveying Tool — Parts 1–3, and the First Scored Strata Prediction (Refutation as Designed)

**Author:** Daniel T. Murphy (ENRGYONE / Star-Magic Research Program)
**Assembled:** 2026-08-29, from the v1.69.0–v1.79.0 build arc of `uqff_downhole_simulator`
**Status:** LANDMARK — authored and wired; every number below is re-verified live by the
`PAPER_2258` calculator dispatch and by the fidelity gate on every run.

---

## 1. Mission (Daniel's directive, 2026-08-29, verbatim intent)

> "We are making a geological subsurface surveying tool... building the technology similar
> to downhole-Lidar, but we want to image/map continents one site at a time."

Not a better traditional logging program. A sensing-and-imaging system whose interpretation
layer is the UQFF framework — constants and structure derived from the locked primitive
lattice rather than fitted to industry baselines — grounded in a verbatim, provenance-locked
library of real ground truth, and governed end to end by disclosure machinery that refuses
to overstate what it knows.

## 2. The foundation it stands on

- **The library:** 52 public catalogue entries across 37 regions and 39 physical kinds —
  every entry license-checked before ingestion, transcribed verbatim, carrying a mandatory
  provenance sidecar, its archive's own declared Size re-counted at gate time and its
  archive's own arithmetic re-derived on every run. One license refusal on record.
- **The private operator tier:** the first client field data (Retama Ranch #403H — a full
  horizontal-well survey minimum-curvature-verified to 0.005 ft over three miles, drilling
  mechanics, and plan-tracking) held under the same sidecar discipline but private by
  construction: gitignored, absent from the wheel manifest (gate-enforced), never required
  by any test. Confidentiality is proven in the build artifacts, not promised.
- **The instrument layer:** quartz-gauge engine, tool library, read-only ingestion
  (LAS/historian/PANGAEA/IODP/operator tables, file-follower, Modbus TCP), and the
  two-stream reconciler of PAPER_2257.

## 3. Part 1 — The Earth Model (v1.74.0)

The library's scattered 1-D columns register into ONE geographic frame:

- 29+ sites placed by **archive-declared coordinates only** (nothing geolocated from
  memory; every coordinate-less entry listed with its reason), grouped at a disclosed
  ~1.1 km resolution, spanning 163° of latitude and a measured 19,313 km of great circle.
- A common vertical frame (elevation-referenced metres) with a rule that earned its keep
  the day it was written: a deviated well's measured depth is NOT a height — vertical
  registration goes through the well's own TVD channel (the rule caught a −5,016 m vs
  −3,424 m error before it shipped).
- Registration DISCOVERED structure no single archive held: the U1324 pore-pressure and
  Ursa clay-mineralogy entries — catalogued months apart as separate wells — are one site.

## 4. Part 2 — The sensing kernels

**K2, the gravity kernel (v1.75.0).** Composed ONLY from UQFF-derived constants, papers
and honest residuals named: g = N_CH + Φ₅/₆ − F²·K_MEX = 9.8125 m/s² (PAPER_1598, 0.025%);
G = 6.669×10⁻¹¹ parameter-free (PAPER_593, 0.08%); R⊕ = A₅·SO₅² + A₅·D_BSFG + SO₅ + F·SO₅
= 6371 km EXACT (PAPER_1209CC S603). These compose a free-air gradient of **0.30804 mGal/m
that was never fit to anything**. Against the KTB borehole gravimeter (197 stations to
8,400 m): predicted vs measured interstation gravity correlates at **0.9968** with mean
residual −0.007 mGal (one archive null excluded with disclosure). The circularity caveat
rides inside the result object itself: BHGM density is vendor-inverted from gravity, so
this is a falsifiable CONSTANTS test, not yet an independent strata test.

**K1, the structural ladder (v1.76.0).** PAPER_1209CC's Earth shells composed live from
the registry primitives — Earth radius 6371, core 3485, continental crust 35 = D_crit +
N_CH, Mariana 11, oceanic Moho 7, mean ocean 3.7, Kármán 100: **seven EXACT**, Everest
8.846 at 0.019%. Audited against the Earth Model: twenty-nine independent archives, none
of which ever consulted the lattice, all inside its Everest/Mariana envelope — zero
violations. The library's vertical reach measured honestly: 15.7% of the crustal rung.

## 5. Part 3 — The inverse engine (v1.77.0)

Measured gravity → implied density (K2 inverted) → posterior strata properties (the
library's own joint distributions; the strata-join engine had already recovered the
velocity–porosity relation empirically at r = −0.71 from archives transcribed months
apart) → layer-boundary candidates above a disclosed threshold. Every estimate carries
n, spread, support, an extrapolation flag, and its transfer assumption in words.

## 6. The cycle that is the point: predict → score → correct

**The prediction (pinned before its data existed).** From measured gravity alone, through
the UQFF constants and a prior learned at oceanic 504B, the engine predicted the KTB sonic
column: Vp = 5,675 ± 109 m/s at implied densities 2.80–2.90 g/cc — labeled
PREDICTION_AWAITING_DATA and pinned in the fidelity gate before the answer was known.

**The score (entry 52).** A verbatim excerpt of the KTB composite log (co-located DTCO +
RHOB, 6,020–6,030 m) answered: at matched density, KTB's own Vp is **6,228 m/s mean** —
the prediction REFUTED as transferred, ~+10%, beyond 3σ. The diagnosis was the sentence
the engine had printed on every estimate before the data arrived: *"a prior learned in
oceanic basalt applied to continental gneiss is an assumption, not a fact."* The disclosed
assumption WAS the failure mode; the UQFF constants layer (0.9968) was not implicated.

**The correction (v1.79.0).** Priors became geological families. The very data that
refuted the transfer now supplies the continental_crystalline prior (46 washout stations
excluded by a disclosed filter), and it reproduces its own ground in-sample: at ρ = 2.86,
**6,231 ± 297 vs measured 6,228**. Prediction V2 stands pinned and unsettled: Vp
5,981–6,263 m/s (mean ~6,051) across 182 intervals — with error bars honestly WIDER than
v1's, because nineteen real pairs support them and the engine refuses to pretend otherwise.

## 7. The honesty machinery (why a client can trust the numbers)

Refusals are first-class outputs: thin data refuses with counts; missing measurements
refuse rather than template-fill; the engine bridge refused the U1324 well for months
until the archive supplied its temperature. Archive anomalies are carried verbatim with
disclosure, never repaired. Predictions are pinned before their data arrives. Seven ship
guards make label and packaging honesty mechanical (the newest, v7, caught its own author
within hours of being written). The fidelity gate — 5,997 assertions at this writing —
re-derives every claim in this paper from the archives on every run, and the acceptance
suite does so corpus-blind on machines that have never seen the physics.

## 8. Falsifiable claims on record

1. **Prediction V2** (§6) — settled the day the deep KTB sonic (6,500–7,700 m) is ingested.
2. The K2 constants chain — any correction to UQFF g, G, or R⊕ appears directly as bias
   against the KTB gravimeter.
3. The structural-ladder envelope — one archive-declared site elevation above the Everest
   rung or seafloor below the Mariana rung breaks a live pin.
4. The bench protocol's 1.0324 drift ratio (PAPER_2257 lineage) — awaiting hardware.

## 9. Commercial posture

The tool ships inside `star-magic-program` (PyPI) under the AGPL-3.0 + Commercial dual
license (ENRGYONE); the private operator tier is the working proof of client-data
confidentiality. Contact: daniel.murphy00@enrgyone.com.

---

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026-08-29, Youngstown OH.
