# JHTDB cap grade - provenance (B276, 2026-09-10)

Source: Johns Hopkins Turbulence Database (JHTDB), dataset
**isotropic8192** (8192^3 DNS of forced isotropic turbulence,
Re_lambda ~ 1300 - the highest-Reynolds public DNS), snapshot t = 1.0.
Access: the OFFICIAL public REST service
(web.idies.jhu.edu/turbulence-svc/values), function GetVariable,
var=velocity, sop=gradient, sint=fd4lag4, tint=none, queried from the
JHTDB site origin using the PUBLICLY SANCTIONED testing token
(edu.jhu.pha.turbulence.testing-201406; JHTDB states it is valid for
requests under 4,096 points). Two requests of 1,000 points each -
well inside the sanctioned limit. Citation obligations: JHTDB
citation policy (turbulence.idies.jhu.edu/citing) applies to any
publication using these numbers.

Points: deterministic 64-bit LCG (Knuth MMIX constants
a=6364136223846793005, c=1442695040888963407, x0=seed; u = (x>>11)/2^53),
seeds 26 and 27, coordinates u*2*pi per axis, 1,000 points per seed,
8 decimals. ANYONE can re-pull the identical samples.

Computed per point from the returned gradient tensor A_ij = du_i/dx_j:
omega = curl u; S = (A + A^T)/2; enstrophy density w2 = |omega|^2;
production density prod = omega.S.omega.
Spot-check anchors (seed 27, first two points, %.6g):
  w2 = 72778.5,  prod = -2304670
  w2 = 13137.6,  prod = 233286

THE GRADED STATISTIC (the sampled transcription of PAPER_1182 S300,
V_stretch <= (17/20)*||omega||_inf*E):
  ratio = mean(prod) / ( max|omega| * mean(w2) )
Results:  seed 26: 0.028660   seed 27: 0.024624
Ten 100-point sub-batches (seed 27): max 0.084421.
ALL <= 17/20 = 0.85. **CAP HOLDS on this dataset** (margin ~10-30x).

POWER LIMITATION (Rule 7, stated where it acts): random pointwise
sampling has essentially no power in the far tail - the extreme-event
scan (reconnection/trefoil-class events; full-field cutouts) remains
the OPEN stronger test. A sampled PASS is a real grade, not the final
word. Consistency check that the pipeline computes real physics: the
positive-stretching fraction came out 0.778/0.754 (seeds 26/27) -
the textbook DNS net-positive vortex-stretching skewness.

---

## ADDENDUM 2026-09-10 - the IN-MEDIUM sample (channel flow, B277-pending)

Second acquisition, same method, Daniel-authorized (token re-supplied):
dataset **channel** (JHTDB turbulent channel flow, Re_tau ~ 1000 -
wall-bounded IN-MEDIUM shear turbulence), t = 1.0, var=velocity,
sop=gradient, sint=fd4lag4, tint=none, official REST service, public
testing token, 2 x 1,000 points (seeds 28/29 of the same LCG;
x in [0, 8pi], y in [-0.9, 0.9] - walls excluded, disclosed -
z in [0, 3pi]).

Results (file: jhtdb_channel_grade_2026-09-10.csv):
  global ratios: seed 28 = 0.039143, seed 29 = 0.031072
  sub-batch max (20 batches of 100): 0.073405
  positive-stretching fraction: 0.736 / 0.764

**IN-MEDIUM BRANCH HOLDS**: all values are far under BOTH the
in-medium pair cap 197/200 = 0.985 AND the vacuum cap 17/20 = 0.85.

HONESTY (Rule 7): at these margins the sampled statistic CANNOT
DISCRIMINATE between the two pair-cap branches - both pass by orders
of magnitude. This acquisition is a CONSISTENCY PASS for the in-medium
branch, NOT the pair-cap discrimination; discrimination lives in the
far tail (extreme events), same as the kill test. Wall-region
(|y| > 0.9) stretching is also unsampled - disclosed.

STATUS: data recorded 2026-09-10; the B277 fold was DEFERRED one
session (the gate sandbox died - disk, see SESSION_LOG) because pins
are never wired without a green gate run to verify them. FOLDED
2026-09-11 in the v0.435.0 band: PAPER_2272, dispatch PAPER_2272,
in_medium_sample_grade() in uqff_ns_assembly, the `cap` argument on
grade_cap_against_dns (graded here against BOTH 197/200 and 17/20),
the B277 gate pin, registry rows, ns_proof_set() data front 2.

---

## ADDENDUM 2026-09-11 - THE REYNOLDS LADDER (isotropic family, B278)

Third acquisition, same method, Daniel-supplied token (third supply):
the vacuum-branch statistic across FOUR Reynolds numbers of forced
isotropic turbulence, plus a resolution check at fixed Re. All via the
official REST service (POST, tab-separated x/y/z lines, var=velocity,
sop=gradient, sint=fd4lag4, tint=none), the public testing token,
1,000 points per request, the same Knuth-MMIX LCG (coords u*2*pi, 8
decimals), NEW seeds so every rung is bit-reproducible by anyone:

| dataset | t | Re_lambda (JHTDB page) | seeds | global ratios | sub-batch max | frac(+) |
|---|---|---|---|---|---|---|
| isotropic1024coarse | 1.0 | ~433 | 30 / 31 | 0.030460 / 0.027190 | 0.067520 | 0.765 / 0.750 |
| isotropic4096 | 1 | 610.57 | 32 / 33 | 0.026534 / 0.038909 | 0.070039 | 0.769 / 0.772 |
| isotropic8192 (snapshot 6) | 6 | ~610 on the 8192^3 grid | 36 / 37 | 0.020592 / 0.025278 | 0.081592 | 0.750 / 0.757 |
| isotropic8192 (snapshot 1) | 1 | 1200-1300 | 26 / 27 (B276) | 0.028660 / 0.024624 | 0.084421 | 0.778 / 0.754 |
| isotropic32768 | 1 | ~2,500 | 34 / 35 | 0.024620 / 0.019006 | 0.107323 | 0.764 / 0.749 |

File: jhtdb_ladder_grade_2026-09-11.csv (8 global rows + 80 sub-batch
rows; the B276 rows stay in their own file). Enstrophy scale per rung
(omega_rms / max sampled |omega|, code units): 21.5/115.9, 85.6/535.8,
94.1/664.6, 167-187/7.8-9.6x rms (B276), 339.3/3303.9 - the max/rms ratio grows 5.4 ->
6.3 -> 7.5 -> ~9 -> 9.7 with Re, the textbook intermittency growth.

Snapshot-index note: for the snapshot datasets `t` is an integer
index (isotropic8192: 1..6; snapshots 1-5 are the Re_lambda 1200-1300
frames, snapshot 6 is the Re_lambda ~610 high-resolution frame), so
B276's t = 1 IS a high-Re frame, as claimed. isotropic32768 exposes one
snapshot (t = 1); Re_lambda ~2,500 per its JHTDB page (GESTS code,
Frontier exascale run, 3.5e13 grid points).

Spot-check anchors (%.6g; first two points of each seed):
  seed 30 (1024coarse): w2 65.9057 / 230.348, prod -130.587 / -955.081
  seed 32 (4096):       w2 11669.8 / 1365.04, prod 95611.9 / 5879.13
  seed 36 (8192 t=6):   w2 502.801 / 124474,  prod 2350.06 / -851318
  seed 34 (32768):      w2 130429 / 45531.3,  prod -3936998 / 1371119
Re-pull check performed first: seed 27's first two isotropic8192 points
reproduced the B276 anchors (72778.5 / 13137.6; -2.30467e6 / 2.33286e5).

RESULT - THE CAP HOLDS AT EVERY RUNG (worst ratio anywhere 0.107323,
8x under 17/20, on the highest-Reynolds DNS in existence). The GLOBAL
statistic shows NO trend toward the cap across Re_lambda 433 -> 2,500
(per-rung means 0.0288, 0.0327, 0.0229, 0.0266, 0.0218). The 100-point
sub-batch ENVELOPE drifts upward with Re (0.068, 0.070, 0.082, 0.084,
0.107) - the direction intermittency predicts and exactly the direction
in which a violation would live; stated as a FLAG for the full-token
scan, not softened. Resolution check at Re_lambda ~610: 4096^3
(0.0265/0.0389) vs 8192^3 (0.0206/0.0253) agree within the seed-to-seed
scatter (~0.01) - no resolution dependence detected at n = 1,000.

HONESTY (Rule 7): sampled global statistic; the far-tail power limit of
B276/B277 is unchanged - this ladder answers "does the sampled statistic
climb toward the cap with Reynolds number?" (NO) and NOT "is there an
extreme event above the cap?" (OPEN, full token / Kerr). Service note:
isotropic4096 answered "result was not filled correctly" on ~10
attempts before both seeds landed - a transient backend fault on the
JHTDB side, disclosed; every number above came from a 200 response.

## ADDENDUM 2026-09-13 - THE DEEP TAIL SAMPLE (stage 1 of the kill test, B282)

Token: Daniel's PERSONAL JHTDB authorization token, issued 2026-09-13 by
JHTDB staff on request to turbulence@lists.johnshopkins.edu. Its value is
a credential and is NOT recorded anywhere in this repository (the wheel
publishes the repository); SHIP GUARD v11 greps the tracked tree for its
prefix on every gate run. Usage rules that came with it and were kept:
GetData <= 2,000,000 points per query; GetCutout <= 3 GB local / 16 GB on
SciServer; no simultaneous queries; small targeted subsets, not
whole-field crawls.

Protocol: official REST (`/turbulence-svc/values`, function GetVariable,
var velocity, sop gradient, sint fd4lag4, tint none), POST body of
tab-separated x y z lines, run from the in-app browser at the site
origin. Points: Knuth MMIX LCG (a = 6364136223846793005, c =
1442695040888963407, u = (x >> 11)/2^53, coords u*2pi to 8 decimals,
three draws per point), seed 40 on isotropic8192 t=1 and seed 50 on
isotropic32768 t=1, 500,000 points each taken as twenty consecutive
25,000-point chunks (chunk k = draws 75000k .. 75000k+74999). One request
in flight at a time. Request size 806 KB, response 4.4 MB (JSON, 9
gradient components per point). Timing: 98-109 s per chunk on
isotropic8192, 163-181 s on isotropic32768. Errors: none (40/40 HTTP
200). Sizing note: a first 200,000-point request was cut off by the
service front proxy with HTTP 502 after several minutes - the duration
cap is separate from the point cap - so 25k was chosen to stay near 100
s; a 20,000-point calibration slab (100 x 100 x 2 lattice, t=1,
isotropic8192) took 81 s and is not part of the graded sample.

Per point: omega from the antisymmetric part, S from the symmetric part,
|omega|^2 and omega.S.omega; per chunk: mean |omega|^2, max |omega|^2,
mean omega.S.omega, the 1182-form ratio, the positive-stretching
fraction, and an enstrophy-octave histogram (bins of log2(|omega|^2 /
chunk mean)) carrying cell counts, stretching sums and enstrophy sums;
the ten highest-enstrophy points per chunk with coordinates. All of it
is in jhtdb_deep_tail_2026-09-13.csv (chunk rows, octave rows, aggregate
rows, hotspot rows) and re-graded live by uqff_ns_assembly.deep_tail_
grade(). Anomaly: 166 of the 500,000 isotropic32768 points came back
with |omega|^2 = 0 exactly (0.033 pct); treated as service artefacts,
counted in the aggregate n, excluded from the octave table, disclosed.

Results: isotropic8192 - max |omega|^2 = 1.008e7 = 333x mean, aggregate
1182 ratio 0.010882, chunk ratios 0.0123-0.0200, positive fraction
0.7601; isotropic32768 - max |omega|^2 = 1.211e8 = 1052x mean, aggregate
ratio 0.006552, chunk ratios 0.0047-0.0187, positive fraction 0.7580.
Octave efficiency eff = sum(omega.S.omega) / (sum|omega|^2 *
sqrt(|omega|^2 at bin centre)) FALLS with intensity on both rungs
(0.118 at the mean, 0.062/0.070 at 16x, 0.033/0.049 at 64x); max on
any load-bearing octave 0.312 (at 1/64 of mean, the weak end). Cells
above 16x mean are 0.6 pct of the sample and carry 29-34 pct of the
stretching. The most intense cell of the record (1052x, isotropic32768,
x y z = 3.53782826 2.80878540 4.77024541) has omega.S.omega < 0 (local
st/|omega|^3 = -0.026): compressed along its vorticity.

What this is and is not: a 1,000x deeper SAMPLE of the tail than
B276-B278, on which the cap holds by a wide margin and the efficiency
trend runs AWAY from the cap with intensity; it is not the whole-volume
local-max test. Stage 2 - full-resolution GetCutout cubes around the
hotspot coordinates above, gradients by central differences on the grid,
graded with the cube's OWN max - is scripted in kt_stage2_cutouts.py
(SciServer or local, token from the environment) and OPEN.

## ADDENDUM 2026-09-15 - THE LOCAL MAXIMUM (stage 2 of the kill test, B283)

Token: the same personal token (value not recorded). Route: the same
REST service from the in-app browser at the site origin - SciServer and
the cutout service were NOT needed: GetVariable with `sint=fd4noint`
returns fourth-order finite-difference gradients evaluated on the true
grid, no interpolation, at every grid node requested. Cubes of n^3 grid
nodes centred on the node nearest each stage-1 hotspot (B282 CSV,
hotspot rows), sent as slabs of 6 z-planes (64^3: 11 requests of 24,576
nodes) or 8 z-planes (128^3: 16 requests of 131,072 nodes), one request
in flight, 3-7 s per 24.6k-node request and 16-19 s per 131k. 132
requests, 132/132 HTTP 200. Per node: |omega|^2 and omega.S.omega; per
cube: mean, max (and its node), the 1182 ratio with the CUBE maximum, the
peak-cell efficiency omega.S.omega/|omega|^3, the positive fraction, and
the octave table relative to the cube mean. All rows in
jhtdb_kill_test_stage2_2026-09-15.csv; re-graded live by
uqff_ns_assembly.kill_test_stage2_grade().

THE DATA HOLE. Cube c32768_3 (centre 2.63592429 4.36877524 4.89765792)
came back with 122,880 of 262,144 nodes at |omega|^2 = 0 exactly: every
node with y-index <= 22781, at every x and z of the cube, deterministic
on re-pull; the first valid row (index 22782) reads |omega| ~ 800-950
and the next (22783) ~ 5,600-6,600 before relaxing - the fd4 stencil
straddling the zero block manufactures a spike two nodes in. Cube
c32768_4 (2.63119183 4.25424803 4.71220780) has the same signature
(118,784 zero nodes). Both are stage-1 hotspots that were never
turbulence; both are REJECTED. Consequence for B282: the 166 zero points
were this hole seen from the sample, and the two isotropic32768 chunks
that contain hotspots 3 and 4 (skip 125000, 475000) carry an artefact
maximum in the denominator of their ratio (biased low); the chunk-ratio
envelope (max 0.0187) comes from other chunks and stands; isotropic8192
shows no zero node in any cube or halo. Every ACCEPTED cube has zero
zero-nodes and a zero-free halo - three grid layers outside each face
sampled at stride 2 (stencil reach is two) - probed for every accepted
isotropic32768 cube; the isotropic8192 cubes had no zeros inside and the
dataset showed none anywhere in 500k + 2.6M nodes.

Results (accepted cubes): isotropic8192 - c8192_1 64^3 ratio 0.013566
(peak 2.639e7 = 870x global mean, peak efficiency 0.018), the same
region at 128^3 0.011551 (same peak node), c8192_2 0.017350 (peak
efficiency -0.012, compressed), c8192_3 0.019442; isotropic32768 -
c32768_1 64^3 0.012005 (cube mean 75x the global mean; peak 1.354e9 =
11,763x the global mean - eleven times the stage-1 sample at that spot -
peak efficiency 0.074), 128^3 0.011090 (same peak), c32768_2 0.015565,
c32768_5 0.009304. Worst local ratio 0.019442 (c8192_3), forty-four-fold
under 17/20. Octave efficiency inside every cube falls from the cube
mean to 32x the cube mean (eff(32x)/eff(mean) = 0.14-0.45); load-bearing
maximum 0.44 (at 1/64 of a cube mean).
