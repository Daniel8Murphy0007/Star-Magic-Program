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
