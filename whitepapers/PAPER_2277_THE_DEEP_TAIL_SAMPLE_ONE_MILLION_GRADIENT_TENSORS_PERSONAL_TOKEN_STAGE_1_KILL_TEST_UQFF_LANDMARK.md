# PAPER_2277 - THE DEEP TAIL SAMPLE: ONE MILLION VELOCITY-GRADIENT TENSORS UNDER THE PERSONAL TOKEN - STAGE 1 OF THE KILL TEST, THE OCTAVE EFFICIENCY, AND WHERE THE TAIL STRETCHES LESS (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-13. **Trigger:** Daniel obtained a personal JHTDB
authorization token the same day the request was sent ("is this what you
are looking for?" - yes). **Band:** v0.438.0 (B282).
**Live mirror:** uqff_ns_assembly.deep_tail_grade().
**Data:** jhtdb_grade/jhtdb_deep_tail_2026-09-13.csv; provenance in
jhtdb_grade/README_PROVENANCE.md (2026-09-13 addendum).
**Stage 2 script:** jhtdb_grade/kt_stage2_cutouts.py (OPEN).

## 0. What changed, in one paragraph

Front 1 of the proof set (PAPER_2276 sec 6.1) was gated on a token. The
token arrived within hours of the request, with the database's usage
rules attached: at most 2 million points per query, cutouts of 3 GB
(local) or 16 GB (SciServer), one query at a time, and the stated intent
of "small, targeted subsets" rather than whole-field crawls. Those rules
reshape "whole-volume" into a two-stage hotspot scan, which is what a kill
test should have been anyway. This paper is STAGE 1: a deterministic
sample one thousand times deeper than B276-B278 - 500,000 gradient tensors
on isotropic8192 (Re_lambda 1200-1300) and 500,000 on isotropic32768
(Re_lambda ~2,500), forty sequential requests, zero errors - graded three
ways. The cap holds by a wide margin on every chunk and on the aggregate.
More than that: resolved by enstrophy octave, the stretching efficiency
FALLS with intensity on both rungs, and the single most intense cell in a
million (1052x the mean, on the 32768^3 grid) is being compressed along
its own vorticity. The tail runs away from the cap, not toward it. Stage 2
(full-resolution cubes around the recorded hotspots, graded with the
cube's own maximum) is scripted, on the wheel, and OPEN.

## 1. The token and the rules (Rule 7 first)

The personal token is a credential. Its value appears nowhere in this
repository - not in the CSV, not in the provenance file, not here - because
the wheel publishes the repository; SHIP GUARD v11 greps the tracked tree
for its prefix on every gate run and goes red if it ever lands. The public
testing identifier of B276-B278 was different in kind (published on the
database's own page) and is recorded there.

Rules received with the token, and kept: 2,000,000 points per GetData
query; 3 GB / 16 GB per cutout; no simultaneous queries; targeted subsets.
Every request of this paper was issued one at a time with the previous
one complete. A first 200,000-point request was cut off by the service's
front proxy (HTTP 502 after several minutes) - a duration cap distinct
from the point cap - so the chunk size was set at 25,000 points (~100 s on
isotropic8192, ~170 s on isotropic32768). Request 806 KB, response 4.4 MB.

## 2. Protocol

Official REST service, GetVariable / velocity / gradient / fd4lag4 / no
time interpolation, at t = 1 on both datasets (isotropic8192 snapshot 1,
Re_lambda 1200-1300; isotropic32768, Re_lambda ~2,500). Points from the
Knuth MMIX LCG of B276-B278 (three draws per point, coords u*2pi to eight
decimals), seed 40 on isotropic8192 and seed 50 on isotropic32768, taken
as twenty consecutive chunks of 25,000 (chunk k = draws 75,000k onward),
so any chunk is re-pullable bit-exact from (seed, skip). Per point:
omega = antisymmetric part of grad u, S = symmetric part, |omega|^2 and
omega.S.omega. Per chunk: the 1182-form ratio mean(omega.S.omega) /
(max|omega| mean|omega|^2), the positive-stretching fraction, and an
octave histogram of log2(|omega|^2 / chunk mean) carrying cell counts,
stretching sums and enstrophy sums; the ten most intense cells with
coordinates. Aggregation over chunks is exact for the sums, and the
aggregate ratio uses the sample-global maximum.

Disclosed anomaly: 166 of the 500,000 isotropic32768 points came back with
|omega|^2 = 0 exactly (0.033 pct; none on isotropic8192 beyond two cells
below 2^-18 of the mean). They are counted in n, excluded from the octave
table, and treated as service artefacts.

**CORRECTION (2026-09-15, PAPER_2278 sec 2):** the 166 zero points are a
DATA HOLE in the isotropic32768 store (whole blocks returning zero
gradients), and the finite-difference stencil at a hole edge manufactures
vorticity spikes: hotspots 3 and 4 of isotropic32768 in the CSV are
hole-edge artefacts, not turbulence; the two chunks containing them (skip
125000, 475000) have artefact maxima in their ratio denominators (biased
low); the chunk-ratio envelope 0.0187 comes from other chunks and stands;
isotropic8192 is unaffected. Hotspots 1, 2 and 5 of isotropic32768 were
verified hole-free (interior + halo) in stage 2.

## 3. Results

### 3.1 The harness statistic (the cap as B276-B278 graded it)

| dataset | points | mean |omega|^2 | max |omega|^2 | max / mean | aggregate ratio | chunk ratios (20) | positive fraction |
|---|---|---|---|---|---|---|---|
| isotropic8192, t=1 | 500,000 | 30,319 | 1.008e7 | 333 | 0.010882 | 0.0123 - 0.0200 | 0.7601 |
| isotropic32768, t=1 | 500,000 | 115,121 | 1.211e8 | 1,052 | 0.006552 | 0.0047 - 0.0187 | 0.7580 |

Every chunk sits 40-180x under 17/20. The aggregate ratio FALLS with
sample depth by construction - the denominator carries the sample's
maximum, which keeps rising as the tail is sampled deeper (B276 at 1,000
points: 0.02-0.03; here at 500,000: 0.011 and 0.0066) - so it is reported
and not leaned on. The chunk-level envelope carries the honest content:
at 25,000-point depth the maximum chunk ratio is 0.0200 on isotropic8192
and 0.0187 on isotropic32768 - NO Reynolds-number trend. The B278 flag
(100-point sub-batch envelope drifting 0.068 -> 0.107 with Re) does not
persist at this scale; it is retired at 25k-sample depth and stays on
record at 100-point depth as a small-sample effect.

### 3.2 The octave efficiency (the scale-resolved form; sharper than the cap)

Define, on the cells whose enstrophy lies in octave o (2^o <= |omega|^2 /
mean < 2^(o+1)),

    eff(o) = sum(omega.S.omega) / ( sum|omega|^2 * sqrt(mean|omega|^2 * 2^(o+1/2)) )

- the stretching per unit enstrophy per unit |omega| at that intensity.
The cap 17/20 is a GLOBAL, |omega|^2-weighted statement; eff is its
octave-resolved shadow and a strictly sharper diagnostic. It is graded
here only on load-bearing octaves (>= 20 cells, >= 1/64 of the mean):
as |omega| -> 0 at finite strain the per-|omega| ratio diverges trivially
and those cells carry under 0.1 pct of the stretching.

| octave | x mean | isotropic8192: cells / eff / share of stretching | isotropic32768: cells / eff / share |
|---|---|---|---|
| -3 | 1/8 | 77,454 / 0.190 / 1.1 pct | 74,347 / 0.182 / 1.0 pct |
| -1 | 1/2 | 71,319 / 0.137 / 5.9 pct | 67,187 / 0.137 / 5.2 pct |
| 0 | 1 | 51,731 / 0.118 / 10.3 pct | 49,412 / 0.118 / 9.2 pct |
| 1 | 2 | 31,279 / 0.102 / 15.1 pct | 30,127 / 0.103 / 13.7 pct |
| 2 | 4 | 15,277 / 0.087 / 17.5 pct | 14,986 / 0.091 / 16.8 pct |
| 3 | 8 | 6,242 / 0.075 / 17.3 pct | 6,291 / 0.080 / 17.4 pct |
| 4 | 16 | 2,184 / 0.062 / 14.0 pct | 2,161 / 0.070 / 14.6 pct |
| 5 | 32 | 597 / 0.052 / 9.0 pct | 653 / 0.058 / 10.2 pct |
| 6 | 64 | 112 / 0.033 / 3.0 pct | 157 / 0.049 / 5.8 pct |
| 7 | 128 | 18 / 0.048 / 1.9 pct | 40 / 0.033 / 2.8 pct |
| 8 | 256 | 2 / 0.128 / 1.5 pct | 7 / 0.032 / 1.3 pct |
| 10 | 1,024 | - | 1 / -0.022 / -0.8 pct |

Read down either column: the efficiency FALLS with intensity, from ~0.19
at one-eighth of the mean to ~0.03-0.05 at 64-256x, as |omega|^-0.66
(8192) and |omega|^-0.56 (32768) over octaves 2-8. Its maximum on any
load-bearing octave is 0.312 (at 1/64 of the mean) - 2.7x under 17/20,
and on the octaves that carry the budget (0 to 5, ~75 pct of all
stretching) it is 0.05-0.12. The two rungs agree octave by octave to
within 0.01. The tail is where the framework said a violation would live;
the tail stretches LESS per unit of its own vorticity.

### 3.3 The tail's share and the most intense cell

Cells above 16x the mean enstrophy are 0.6 pct of the sample and carry
29 pct (8192) / 34 pct (32768) of the stretching; above 64x, 0.03-0.04
pct of cells carry 6-9 pct. The stretching budget is concentrated, and
the concentration is the same on both rungs. The single most intense
cell in the million - isotropic32768, |omega|^2 = 1.211e8 = 1052x mean,
at (3.53782826, 2.80878540, 4.77024541) - has omega.S.omega < 0
(local omega.S.omega / |omega|^3 = -0.026): it is compressed along its
vorticity, as an intense tube caught after its stretching phase would
be. The ten most intense cells per dataset are recorded with
coordinates in the CSV for stage 2.

## 4. What this closes, and what it does not

CLOSES: the question "does the sampled statistic approach the cap when
the tail is sampled a thousand times deeper?" - no, on two Reynolds rungs,
with the efficiency trend running away from the cap. RETIRES at 25k-depth:
the B278 envelope-drift flag. DOES NOT CLOSE: the kill test itself, which
is a statement about whole volumes with their own maxima. Stage 2 -
full-resolution GetCutout cubes (256^3, ~200 MB each) around the recorded
hotspots, gradients by fourth-order central differences on the grid,
graded with the cube's OWN maximum by the same 1182 form plus the octave
efficiency - is scripted in jhtdb_grade/kt_stage2_cutouts.py, runs on
SciServer (the volumes should not be streamed to a laptop) or locally
under the 3 GB cap, and is OPEN. A single cube with ratio_local > 0.85
kills the vacuum-branch cap; the paper will then say so.

## 5. Honesty inventory (Rule 7)

1. Sampled points, not whole volumes; the local-max test is stage 2.
2. The aggregate 1182 ratio is depth-dependent by construction; the chunk
   envelope and the octave efficiency are the statistics that mean
   something here.
3. The octave efficiency is a sharper diagnostic than the cap and is
   NOT the cap; its trivial divergence in near-zero-vorticity cells is
   disclosed and excluded from the grade.
4. 166 zero-gradient points on isotropic32768: disclosed, excluded from
   the octave table, counted in n.
5. The 200,000-point request that the proxy cut off is disclosed; no
   partial data from it was used.
6. The token value is not recorded; the rules that came with it are, and
   were kept: one query at a time, 25,000 points each, forty requests.
7. Not claimed: that the cap is proved by data (it is derived and, here,
   not falsified); that front 1 is closed; anything about front 2, 3, 4.

## 6. Cross-references

PAPER_2276 (index; front 1 instrument and access route), PAPER_2271/2272/
2273 (B276-B278 sampled grades), PAPER_2264 (pair cap), PAPER_2265/2266
(the derived cap), PAPER_1182 (the 1182 form), PAPER_2270 (proof set).
