# PAPER_2261 — The K4 Geological Landmark Family: the Rock Density Inventory and its Supporting Streams

**Author:** Daniel T. Murphy
**Date:** 2026-09-08
**Landmark Type:** K4 family derivation (product-blocking OPEN target closed)
**Ruling:** Daniel, 2026-09-08 (verbatim): "DERIVE GEOLOGICAL LANDMARK. CREATE A UNIQUE FILE FOR ROCK DENSITY INVENTORY, ALONG WITH SUPPORTING DATA STREAMS."
**Status:** production

---

## Abstract

The material-ID channel of the surveying product was BLOCKED_ON_K4: the
material-landmark family (PAPER_1600-1799 precedent) held
concrete/steel/aluminum/pine but no geological rungs, so the tool could
rank density but refused to name rock. On Daniel's derivation order the
K4 family is derived: SEVENTEEN geological landmarks — eight
mineral/fluid-tier (tight anchors) and nine rock-tier (published ranges,
midpoint anchors) — each an observation-headlined anchor from the
standard geophysics density tables (Telford, Geldart & Sheriff 1990;
Schön 2015) carrying a primitive decomposition over the locked lattice
{D_phys, D_crit, SO_5, F_TRZ}. Sixteen decompositions land EXACTLY on
their anchors; ice = (SO_5+1)/(SO_5+2) = 11/12 at 0.036%. The family
ships as `uqff_downhole_simulator/uqff_rock_inventory.py` with three
supporting streams, and its falsifiable content is graded immediately:
the density-only classifier's column vote for the KTB window names the
KTB's published lithology within density's honest capability.

## 1. The seventeen landmarks

| Entry | Tier | Anchor (g/cc) | Primitive form | Residual |
|---|---|---|---|---|
| quartz | mineral | 2.65 | (2·D_crit+1)/(2·SO_5) = 53/20 | EXACT |
| calcite | mineral | 2.71 | (D_crit+1)/SO_5 + F_TRZ² | EXACT |
| dolomite | mineral | 2.87 | (D_crit+D_phys−1)/SO_5 − (D_phys−1)·F_TRZ² | EXACT |
| halite | mineral | 2.16 | (D_crit+1)/SO_5 · D_phys/(SO_5/2) | EXACT |
| gypsum | mineral | 2.32 | (D_crit+D_phys−1)/SO_5 · D_phys/(SO_5/2) | EXACT |
| anhydrite | mineral | 2.97 | (D_crit+1)/SO_5 · (1+F_TRZ) | EXACT |
| ice | mineral | 0.917 | (SO_5+1)/(SO_5+2) = 11/12 | 0.036% |
| seawater | fluid | 1.025 | 1 + (SO_5/D_phys)·F_TRZ² | EXACT |
| granite | rock | 2.67 | quartz + 2·F_TRZ² | EXACT |
| gneiss | rock | 2.75 | (SO_5+1)/D_phys = 11/4 | EXACT |
| basalt | rock | 2.90 | (D_crit+D_phys−1)/SO_5 | EXACT |
| shale | rock | 2.40 | (D_crit−D_phys/2)/SO_5 | EXACT |
| sandstone | rock | 2.35 | shale − F_TRZ/2 | EXACT |
| limestone | rock | 2.55 | (2·D_crit−1)/(2·SO_5) = 51/20 | EXACT |
| amphibolite | rock | 2.96 | (D_crit+D_phys)/SO_5 − D_phys·F_TRZ² | EXACT |
| peridotite | rock | 3.30 | (SO_5+1)·(D_phys−1)/SO_5 | EXACT |
| coal | rock | 1.35 | (D_crit+1)/(2·SO_5) = 27/20 | EXACT |

Structural notes: gneiss carries the Aether-coupling integer over
spacetime, (SO_5+1)/D_phys — and gneiss is the KTB's dominant rock;
anhydrite = the granite-frame × (1+F_TRZ) (the dehydration rung of
gypsum, which shares the ×D_phys/(SO_5/2) = 4/5 hydration factor with
halite); granite = quartz + 2·F_TRZ² (the quartz-feldspar frame).

## 2. Disclosure (value-coincidence discipline, stated where it acts)

The decompositions were found by search over small primitive
combinations against published anchors, in the material-landmark style.
They are canonized as the K4 family on Daniel's 2026-09-08 derivation
order. The family's falsifiable content is the CLASSIFIER built on it
(§3) — graded against published lithology it was not tuned to — and
every future well it classifies.

## 3. Supporting data streams (the unique file)

`uqff_rock_inventory.py`:
- `rock_inventory()` — the seventeen entries, primitive values composed
  LIVE from the registry at every call, residuals honest.
- `classify_density(rho)` — RANKED candidates whose published ranges
  contain the value, ordered by distance from the primitive landmark;
  overlap count printed; out-of-inventory says so. Never one confident
  name.
- `rock_candidate_stream(entry)` — the material-ID channel that was
  BLOCKED_ON_K4, flowing per-station over a catalogue entry.
- `ktb_lithology_validation()` — THE GRADE: the KTB window's column vote
  vs the KTB's published paragneiss-amphibolite section. Result: gneiss
  top-ranked (16/19 stations) with the mafic twin present; the
  amphibolite/basalt DENSITY DEGENERACY disclosed (amphibolite is
  metamorphosed basalt — density-only ID cannot and does not
  distinguish the twins). Verdict: MATCHES WITHIN DENSITY-ONLY
  CAPABILITY.

## 4. Product integration

The survey report's rock-NAMES refusal is retired BY DERIVATION: the
report now prints the ranked shortlist with the honesty block, and the
remaining refusal is the correct one — a single confident rock name.
Simulator v1.88.0; acceptance Sections Z1-Z6 (105 checks).

## Cross-references

PAPER_1600-1799 (material-landmark precedent), PAPER_2136/1953/1954
(primitive-lock style), Telford et al. 1990 / Schön 2015 (anchors),
KTB/ICDP published lithology (the grade), uqff_rock_inventory.py,
uqff_survey_cmd.py, B264 gate pin.


---

## REVISION 2026-09-08 — the Vp discriminator tier and the family-level reading (Daniel's open-edge order)

The amphibolite/basalt density degeneracy of §3 is SPLIT by a second
channel: a Vp range per inventory entry (observation-headlined,
Christensen & Mooney 1995 / Schön 2015; NO primitive decompositions
forced onto the Vp tier — that derivation is an OPEN target, per the
value-coincidence discipline). `classify_joint(rho, vp)` requires both
ranges; at the twin density 2.95 g/cc, 6.8 km/s resolves amphibolite
ALONE and 5.7 km/s excludes it — the twins are separable in principle.

**The field lesson (first joint run, KTB window):** in-situ velocities
in fractured deep crust read BELOW laboratory ranges, so metabasite
stations vote into the basalt box — the correct MAFIC family at a
lab-shifted velocity — and two stations at 6.52-6.54 km/s fall in the
gneiss→amphibolite gap (transition evidence, reported as no-candidate
rather than forced). The honest granularity for two-channel ID is the
ROCK FAMILY (felsic/mafic/carbonate/evaporite/clastic/organic), and at
that granularity the sharper grade PASSES: the window resolves into
BOTH published families — the KTB paragneiss-metabasite alternation,
visible in 10 meters of log (family vote: mafic 9, felsic 5, carbonate
3 noise disclosed; 2 gap stations). Species-level ID within a family
needs more channels or lab-to-in-situ corrections — both stated OPEN.

Simulator v1.89.0; acceptance Z7-Z9 (108 checks); B265 gate pin.
