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
