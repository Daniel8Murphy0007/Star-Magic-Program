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
