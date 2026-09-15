# PAPER_2280 - FRONT 2 EXTENSION: CHANNEL5200 - THE IN-MEDIUM REYNOLDS RUNG - THE NEAR-WALL TAIL AT Re_tau 5186 GRADED SIDE BY SIDE WITH Re_tau 1000 IN WALL UNITS, AND NO TREND TOWARD EITHER CAP (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-15. **Trigger:** "proceed with channel5200" - the deeper
tail PAPER_2279 named as front 2's natural extension. **Band:** v0.439.0
(B285; same band as B284).
**Live mirror:** uqff_ns_assembly.in_medium_reynolds_rung().
**Data:** jhtdb_grade/jhtdb_front2_channel5200_2026-09-15.csv; provenance
in jhtdb_grade/README_PROVENANCE.md (2026-09-15 channel5200 addendum).

## 0. What changed, in one paragraph

PAPER_2279 (B284) took front 2 - the pair-cap discrimination, vacuum
17/20 vs in-medium 197/200 - to the near-wall tail of the JHTDB channel
at Re_tau ~ 1000 and found the in-medium branch holding by a factor of
twenty with the discrimination out of reach. It named one extension:
channel5200, the largest public wall-bounded DNS (Re_tau = 5186, 10240 x
1536 x 7680 nodes), a five-fold higher friction Reynolds number and a
proportionally deeper near-wall tail. This paper runs the identical
protocol on it - the same LCG, the same wall-unit band y+ in [0.5, 150],
the same 25,000-point sequential requests, the same wall-parallel
full-resolution slabs graded with their own maxima - and grades the two
rungs side by side in wall units. The result is the in-medium twin of the
isotropic Reynolds ladder (B278/B282): NO trend. Band by band the 1182
ratio and the positive-stretching fraction are the same at Re_tau 5186 as
at 1000 to within the chunk scatter (the positive fraction agrees to 0.005
in all eight shared bands); the local-max envelope is 0.0418 against
0.0413 - one percent apart across a fivefold rise in Re_tau; both sit 20x
under 17/20 and 24x under 197/200. The in-medium branch holds on the
largest wall-bounded DNS in existence, the discrimination stays out of
reach for the same reason, and the ladder is flat: no Reynolds trend.
NOT CLAIMED: the discrimination; a full 3D cube on the non-uniform
y-grid; frames other than t = 1.0.

## 1. Protocol (identical to PAPER_2279 sec 2, one parameter changed)

Re_tau = 5185.897 (JHTDB), so y+ = (1 - |y|) * 5185.897; the near-wall
band y+ in [0.5, 150] is y in [-0.9999036, -0.9710754]; x, z as before
(x = u*8pi, z = w*3pi); dx+ = 12.7, dz+ = 6.4 (the channel's were 12.3 and
6.1, so the slab footprints match in wall units). t = 1.0 (the store's
frames at t = 0 and 0.01 return a server error; t = 1.0 is the frame
queried; disclosed). STAGE 1 (fd4lag4): near-wall seed 70, 250,000 points
as ten chunks of 25,000 (~40 s each on this store, 10/10 HTTP 200); bulk
y+ > 150, seed 71, 100,000 points as four chunks. STAGE 2 (fd4noint, the
store's own grid): seven wall-parallel x-z slabs - 64x64 at y+ 1.5, 15,
50, 100, 300 and 1000, plus one 128x128 at y+ 50 as the resolution check
of PAPER_2278 - centred on the x, z of the most intense near-wall sample
events, each graded with its OWN maximum. Personal token; value recorded
nowhere (SHIP GUARD v11).

## 2. Results

### 2.1 Stage 1 - the two rungs in wall units

| y+ band | Re_tau 1000: ratio / positive fraction (B284) | Re_tau 5186: ratio / positive fraction (this paper) | n (5186) |
|---|---|---|---|
| 0-10 (viscous sublayer) | 0.0067 / 0.548 | 0.0054 / 0.547 | 15,862 |
| 10-20 (buffer) | 0.0142 / 0.611 | 0.0155 / 0.610 | 16,842 |
| 20-40 | 0.0237 / 0.706 | 0.0197 / 0.704 | 33,346 |
| 40-60 | 0.0186 / 0.728 | 0.0210 / 0.724 | 33,597 |
| 60-100 | 0.0238 / 0.735 | 0.0228 / 0.732 | 66,605 |
| 100-150 | 0.0200 / 0.744 | 0.0246 / 0.741 | 83,748 |
| 150-300 | 0.0193 / 0.747 | 0.0338 / 0.751 | 2,888 |
| 300-1000 | 0.0155 / 0.753 | 0.0251 / 0.758 | 13,746 |
| 1000-6000 (core) | - | 0.0151 / 0.757 | 83,366 |

Near-wall aggregates: 0.00815 (1000) and 0.00656 (5186); mean |omega|^2
in the band 261 and 4,980 - the 19x rise is the mean shear scaling as
Re_tau^2 (27x) softened by the band's y+ weighting - and the maximum
23,047 and 759,119. The ratio is a dimensionless combination and the
table shows it in wall units: the same profile on both rungs - lowest at
the wall, rising through the buffer, peaking in the log layer - with the
peak sitting further out at the higher Reynolds number (y+ 150-300, ratio
0.034 on 2,888 points) as the log layer itself extends further. The
positive-stretching fraction agrees between the rungs to 0.005 in every
one of the eight shared bands. The chunk envelope is 0.0099 (near-wall)
and 0.0260 (bulk) at 5186 against 0.0099 and 0.0222 at 1000.

### 2.2 Stage 2 - the local maximum through the layers

| slab | y+ | nodes | ratio_local (own max) | max |omega|^2 | peak-cell efficiency | positive fraction |
|---|---|---|---|---|---|---|
| s1 | 1.5 | 64x64 | 0.00797 | 1.16e6 | 0.065 | 0.539 |
| s2 | 15 | 64x64 | 0.02702 | 187,078 | 0.040 | 0.678 |
| s3 | 50 | 64x64 | 0.04002 | 54,093 | -0.012 | 0.724 |
| s4 | 100 | 64x64 | 0.04183 | 23,128 | -0.006 | 0.729 |
| s5 | 300 | 64x64 | 0.02853 | 13,883 | 0.011 | 0.752 |
| s6 | 1000 | 64x64 | 0.04029 | 848 | 0.006 | 0.700 |
| s3b | 50 | 128x128 | 0.02661 | 129,761 | 0.047 | 0.704 |

Worst 64x64 grade: 0.0418 at y+ 100, against 0.0413 at y+ 50 for Re_tau
1000 - a relative difference of 1.3 percent across a fivefold rise in
Re_tau. 20.3x under 17/20 and 23.5x under 197/200. The 128x128 slab at
y+ 50 contains a larger maximum (129,761 against 54,093) and grades LOWER
(0.027 against 0.040), the same behaviour as the 128^3 cubes of
PAPER_2278: the larger box adds bulk to the mean faster than it raises
the statistic, so 64x64 is the conservative figure. The peak cells at
y+ 50 and y+ 100 - the two most intense cells of the log layer - are
COMPRESSED along omega (negative local efficiency), as the 1052x cell of
isotropic32768 was (PAPER_2277): the most intense vorticity of the flow
is, once again, not being stretched. Every slab and every chunk returned
zero zero-nodes; the channel5200 store is clean.

### 2.3 The reading

Two rungs of the in-medium ladder, Re_tau 1000 and 5186, graded by the
same protocol in the same wall units: the statistic's profile, its peak
value, its positive fraction and its local-max envelope are the same to
within the noise of the measurement. There is NO trend toward either cap
with Reynolds number on the wall side, exactly as there was none on the
isotropic side from Re_lambda 433 to 2,500 (B278, B282). The in-medium
branch holds on the largest wall-bounded DNS in existence; the vacuum
branch would hold on the same data; the discrimination remains out of
reach because the flow sits an order of magnitude below the nearer
branch, and raising Re_tau fivefold moved it by one percent.

## 3. What this closes, and what it does not

CLOSES: the channel5200 extension PAPER_2279 named. ESTABLISHES: the
in-medium Reynolds ladder (two rungs, flat) as the wall-side twin of the
isotropic ladder. DOES NOT CLOSE: front 2 as a discrimination - the
public DNS record, isotropic to Re_lambda 2,500 and wall-bounded to
Re_tau 5,186, never approaches the 0.85-0.985 band where the branches
separate, and the ladders say raising the Reynolds number does not bring
it closer. What would: a flow in a different regime entirely (the
[SCm]-loaded branch of PAPER_2264, or a laboratory measurement of the
stretching statistic in a strongly in-medium fluid), not a bigger DNS.

## 4. Honesty inventory (Rule 7)

1. Same caveats as PAPER_2279 sec 5, items 1-4 (consistency, not
   discrimination; mean shear in the denominator; stage 1 interpolated,
   stage 2 on-grid; peak-cell efficiency is pointwise).
2. One frame (t = 1.0); t = 0 and 0.01 returned server errors and were
   not used; no partial data.
3. The y+ 150-300 band at Re_tau 5186 rests on 2,888 points (its 0.034
   is the largest sampled-band ratio of the record and carries the
   widest error bar); the local-max slabs at y+ 100-300 (0.042, 0.029)
   are the on-grid figures for that region.
4. "One percent apart" is the envelope of two single slabs; the
   Reynolds-invariance claim rests on the eight-band profile and the
   positive fraction, which are the population statistics.
5. Not queried: channel5200 above y+ 6000 (the core is sampled to the
   centreline by the bulk band); more than seven slabs; any 3D cube.

## 5. Cross-references

PAPER_2279 (B284, the protocol and the Re_tau 1000 rung), PAPER_2272
(B277), PAPER_2264 (the pair cap), PAPER_2273 (B278, the isotropic
Reynolds ladder this twins), PAPER_2277/2278 (B282/B283), PAPER_2276
(index; front 2), PAPER_1182 (the 1182 form).
