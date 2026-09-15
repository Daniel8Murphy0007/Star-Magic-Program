# PAPER_2279 - FRONT 2: THE PAIR-CAP DISCRIMINATION TAKEN TO THE NEAR-WALL TAIL - WALL-BOUNDED IN-MEDIUM TURBULENCE (JHTDB CHANNEL Re_tau ~ 1000) GRADED AGAINST 17/20 AND 197/200, AND WHAT THE DATA CANNOT DECIDE (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-15. **Trigger:** "proceed with front 2" - the second
data front of the proof set (PAPER_2276 sec 6.2), the day v0.438.0 (THE
KILL TEST SHIP) shipped. **Band:** v0.439.0 (B284).
**Live mirror:** uqff_ns_assembly.in_medium_tail_grade().
**Data:** jhtdb_grade/jhtdb_front2_channel_2026-09-15.csv; provenance in
jhtdb_grade/README_PROVENANCE.md (2026-09-15 front-2 addendum).

## 0. What changed, in one paragraph

Front 2 is not the kill test. The kill test (front 1) asks whether ANY
flow's stretching statistic reaches the cap. Front 2 asks a sharper
question the framework itself raised: the cap is a PAIR - vacuum-branch
flows obey 17/20 = 0.85, in-medium (wall-bounded, stratified) flows obey
197/200 = 0.985 (PAPER_2264, B269), the two differing by exactly 0.135 -
and whether real wall turbulence lands nearer the in-medium branch than
the vacuum one. B277 (PAPER_2272) sampled the channel BULK with the walls
excluded (|y| < 0.9, i.e. y+ > 100) and found ratios 0.03-0.07: a
consistency pass, but it disclosed two gaps - the near-wall region, where
in-medium production peaks, was never sampled, and at those margins
neither branch could be distinguished. This paper closes the first gap
and settles the second in the honest direction. Under Daniel's personal
JHTDB token, on the channel (Re_tau ~ 1000): STAGE 1, a near-wall deep
sample - 250,000 gradient tensors in the band y+ in [0.5, 150] plus
100,000 in the bulk, the 1182 ratio resolved by wall distance; STAGE 2,
wall-parallel full-resolution grid slabs (fd4noint, the channel's own
grid, no interpolation) through the layers, each graded with its OWN
maximum. The in-medium branch HOLDS - the ratio peaks at 0.024 (stage 1,
buffer layer) and 0.041 (stage 2, y+ ~ 50), everywhere 20-130x under BOTH
caps. The two branches are 0.135 apart; the flow sits an order of
magnitude below the nearer of them, so the DISCRIMINATION is out of reach.
That is not a failure - it is the same result the kill test gave for the
vacuum branch (B283), stated on the wall side: real turbulence, in medium
or vacuum, runs an order of magnitude under its cap, so the two caps are
consistent with the data and indistinguishable by it.

## 1. The token and the geometry (Rule 7 first)

The personal token's value appears nowhere in this repository - not in
the CSV, not in the provenance, not here; SHIP GUARD v11 greps the tracked
tree for its prefix on every gate run. The database rules received with it
(GetData <= 2,000,000 points/query; no simultaneous queries; targeted
subsets) were kept: sampling in sequential 25,000-point requests, one in
flight, on the same LCG as B276-B278.

The channel domain is x in [0, 8pi], y in [-1, 1] (wall-normal,
non-uniform Chebyshev-type grid, walls at y = +/-1), z in [0, 3pi], at
Re_tau ~ 1000, so wall units are y+ = (1 - |y|) * 1000. The x and z grids
are uniform (dx = 8pi/2048 = 12.3 wall units, dz = 3pi/1536 = 6.1);
y clusters at the walls. Points are drawn from the Knuth MMIX LCG
(x = u*8pi, z = w*3pi, y uniform within the target band, three draws per
point, eight decimals). The 1182 statistic uses the FULL velocity
gradient the service returns (var=velocity, sop=gradient) - including the
mean shear - because the cap is a statement about the full gradient, as in
B276-B278 and B282-B283.

## 2. Protocol

STAGE 1 (fd4lag4, interpolated - sampled points are not on the grid):
near-wall band y in [-0.9995, -0.85] = y+ in [0.5, 150], seed 60, t = 1.0,
250,000 points as ten sequential chunks of 25,000; bulk band y in
[-0.85, 0.85] = y+ in [150, 1000], seed 61, t = 1.0, 100,000 points as
four chunks. Per point: omega and S from the gradient, |omega|^2 and
omega.S.omega. Aggregated exactly over chunks and binned by y+; per band
the 1182 ratio mean(omega.S.omega)/(max|omega| mean|omega|^2) with that
band's own maximum.

STAGE 2 (fd4noint - fourth-order finite differences on the channel's OWN
grid, no interpolation): four wall-parallel x-z grid slabs of 64x64 = 4096
nodes, centred on the grid, at fixed y through the layers (viscous
sublayer y+ ~ 1.5, production peak y+ 15, buffer/log y+ 50, log y+ 100),
each graded with the slab's OWN maximum by the same 1182 form plus the
peak-cell efficiency omega.S.omega/|omega|^3. The wall-parallel plane is
the local-max neighbourhood for wall turbulence: near-wall structures
(low-speed streaks, quasi-streamwise vortices) are organised in the x-z
plane, elongated in x. A zero-node check is applied (as B283): every slab
returned zero zero-nodes - the channel store carries no holes.

## 3. Results

### 3.1 Stage 1 - the near-wall tail, resolved by wall distance

| region | y+ band | points | mean |omega|^2 | max |omega|^2 | 1182 ratio | positive fraction |
|---|---|---|---|---|---|---|
| near-wall | 0-10 (viscous sublayer) | 15,870 | 2,216 | 23,047 | 0.00670 | 0.548 |
| near-wall | 10-20 (buffer) | 16,611 | 632 | 9,546 | 0.01422 | 0.611 |
| near-wall | 20-40 | 33,300 | 231 | 6,155 | 0.02372 | 0.706 |
| near-wall | 40-60 | 33,344 | 118 | 7,857 | 0.01857 | 0.728 |
| near-wall | 60-100 | 67,218 | 67.0 | 3,044 | 0.02376 | 0.735 |
| near-wall | 100-150 | 83,657 | 40.7 | 2,837 | 0.02004 | 0.744 |
| bulk | 150-300 | 17,555 | 22.4 | 1,466 | 0.01930 | 0.747 |
| bulk | 300-1000 (core) | 82,445 | 6.31 | 953 | 0.01552 | 0.753 |

Near-wall aggregate (250k): ratio 0.00815, mean |omega|^2 = 261 (the mean
shear), max 23,047. Bulk aggregate (100k): ratio 0.01544, chunk envelope
0.0156-0.0222. The ratio PEAKS at 0.024 in the buffer/lower-log layer
(y+ 20-100) and is smaller both at the wall (mean shear inflates the
denominator) and in the core (weaker turbulence). Its maximum anywhere is
0.024 - 35x under 0.85, 41x under 0.985. The positive-stretching fraction
RISES monotonically away from the wall (0.55 at the wall to 0.75 in the
core): near-wall blocking suppresses vortex stretching.

### 3.2 Stage 2 - the local maximum through the layers

| slab | y+ | layer | nodes | ratio_local (own max) | max |omega|^2 | peak-cell efficiency | positive fraction |
|---|---|---|---|---|---|---|---|
| s1 | 1.5 | viscous sublayer | 4,096 | 0.00453 | 31,988 | 0.047 | 0.523 |
| s2 | 15 | production peak | 4,096 | 0.02207 | 9,643 | 0.177 | 0.661 |
| s3 | 50 | buffer/log | 4,096 | 0.04129 | 2,634 | 0.170 | 0.680 |
| s4 | 100 | log | 4,096 | 0.03678 | 1,319 | 0.041 | 0.748 |

Graded with each slab's own maximum, the local ratio rises from the
sublayer (0.0045) through the production peak (0.022) to a MAXIMUM in the
buffer/log layer, 0.0413 at y+ ~ 50, then falls - the single highest
local-max grade anywhere in the in-medium flow, 20.6x under 0.85 and
23.8x under 0.985. The peak-cell efficiency tops at 0.177 at the
production peak (y+ 15) - the most efficiently stretched cell in the wall
region, still 4.8x under 0.85 - and is small at the wall (0.047), where
the intense enstrophy is mean shear. The sublayer slab, whose own maximum
(31,988) exceeds the stage-1 sample maximum, grades LOWER than stage 1,
not higher: the true near-wall local maximum is mean shear, which the
sample already resolved, so unlike the isotropic case (B283) stage 2 does
not raise the grade.

### 3.3 The reading of the pair cap

Both branches - vacuum 17/20 = 0.85, in-medium 197/200 = 0.985 - are cross-
checked here against the live primitives 1 - F_TRZ^k (D_BSFG/D_phys), k = 1
and 2, and match. The largest 1182 ratio anywhere in this in-medium flow,
across 350,000 sampled points and four local-max slabs, is 0.041. The two
branches are 0.135 apart; the data sit a factor of ~24 below the nearer
one. The in-medium branch HOLDS trivially, but so would the vacuum branch
applied to the same data - the flow does not approach either, so the
measurement cannot say which cap governs wall turbulence. This is the
in-medium counterpart of the kill test's finding for the vacuum branch:
real turbulence, near a wall or in isotropic vacuum, runs an order of
magnitude under its cap, and the efficiency trend runs away from the cap
with intensity. The pair cap is CONSISTENT with the data on both branches
and DISCRIMINATED by neither.

## 4. What this closes, and what it does not

CLOSES: B277's disclosed near-wall gap - the region y+ < 100, where
in-medium production peaks, is now sampled at 250,000 points and graded to
its local maximum, and it too sits far under both caps. SETTLES, in the
honest direction: the pair-cap discrimination is OUT OF REACH for wall
turbulence at Re_tau 1000 - not because the branches are wrong but because
the flow sits an order of magnitude below the nearer of them, the same
verdict the kill test gave the vacuum branch. DOES NOT CLOSE: front 2 as a
DISCRIMINATION. That would need a flow whose far-tail statistic actually
approaches 0.85-0.985; nothing in the public DNS record - isotropic to
Re_lambda 2500, channel to Re_tau 1000 - does. The natural extension is
channel5200 (Re_tau ~ 5200, a deeper near-wall tail); it sharpens this,
it does not change its direction unless it finds what these did not.

**ADDENDUM (2026-09-15, same band, PAPER_2280):** channel5200 was run by
the identical protocol. Same wall-unit profile, positive fraction agreeing
to 0.005 in all eight shared bands, local-max envelope 0.0418 against the
0.0413 here - no Reynolds trend across a fivefold rise in Re_tau. The
direction did not change.

## 5. Honesty inventory (Rule 7)

1. Consistency pass, not a discrimination: stated in sec 0, 3.3 and 4.
   The in-medium branch "holds" only in the weak sense that the data are
   far under it - the vacuum branch would "hold" on the same data.
2. The near-wall 1182 ratio is depressed by the mean shear in the
   denominator (max |omega| near the wall is mean shear); the y+-banded
   and local-max readings are given so the statistic is not leaned on
   through a single global number.
3. Stage 1 is interpolated (fd4lag4, off-grid sample points); stage 2 is
   on-grid (fd4noint). The wall-parallel slab is the local-max
   neighbourhood for wall turbulence; a full 3D fd4noint cube on the
   non-uniform y-grid is the heavier extension and is noted, not claimed.
4. The peak-cell efficiency is a pointwise diagnostic, not the cap.
5. The channel store returned no zero nodes in any slab (contrast the
   isotropic32768 data hole of B283) - stated so the difference between
   the two stores is on record.
6. The token value is not recorded; the rules that came with it were
   kept (sequential 25k requests). channel5200 was not queried.

## 6. Cross-references

PAPER_2276 (index; front 2 instrument and access route), PAPER_2272
(B277, the bulk in-medium consistency pass this extends), PAPER_2264
(B269, the pair cap 17/20 vs 197/200), PAPER_2277/2278 (B282/B283, the
kill test - front 1, the vacuum-branch analogue of this result),
PAPER_1182 (the 1182 form), PAPER_2270 (proof set).
