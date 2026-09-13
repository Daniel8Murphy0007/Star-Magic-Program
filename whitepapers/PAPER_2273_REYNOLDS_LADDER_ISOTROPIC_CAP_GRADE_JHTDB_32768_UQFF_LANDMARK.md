# PAPER_2273 - THE REYNOLDS LADDER: THE NS CAP ACROSS Re_lambda 433 -> 2,500, UP TO THE LARGEST DNS IN EXISTENCE (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-11. **Trigger:** Daniel supplied the publicly
sanctioned JHTDB testing token a third time; the JHTDB service now
lists **isotropic32768** (32,768^3, ~3.5e13 grid points, Re_lambda
~2,500 - the record-setting Frontier exascale run), and it answers the
same token. **Band:** v0.436.0 (B278).

## 1. The question this paper answers

B276 graded the cap at ONE Reynolds number. A cap that holds at one Re
and climbs toward violation with Re would be a cap on borrowed time.
The ladder asks: does the sampled 1182-form statistic trend toward
17/20 as Re_lambda grows? Four rungs of forced isotropic turbulence,
one resolution check, same protocol throughout (official REST service,
POST of tab-separated points, var = velocity, sop = gradient, sint =
fd4lag4, public testing token, 1,000 deterministic-LCG points per seed,
NEW seeds - every rung bit-reproducible by anyone; provenance and
spot-check anchors in jhtdb_grade/README_PROVENANCE.md).

## 2. The ladder

    ratio = mean(omega.S.omega) / ( max|omega| * mean|omega|^2 )   vs 17/20

| Rung | Dataset (snapshot) | Re_lambda | Seeds | Global ratios | Sub-batch max (10 x 100 per seed) | frac(+) |
|---|---|---|---|---|---|---|
| 1 | isotropic1024coarse (t = 1.0) | ~433 | 30 / 31 | 0.030460 / 0.027190 | 0.067520 | 0.765 / 0.750 |
| 2 | isotropic4096 (t = 1) | 610.57 | 32 / 33 | 0.026534 / 0.038909 | 0.070039 | 0.769 / 0.772 |
| 2' | isotropic8192 snapshot 6 (8192^3 at Re ~610) | ~610 | 36 / 37 | 0.020592 / 0.025278 | 0.081592 | 0.750 / 0.757 |
| 3 | isotropic8192 snapshot 1 (B276) | 1200-1300 | 26 / 27 | 0.028660 / 0.024624 | 0.084421 | 0.778 / 0.754 |
| 4 | isotropic32768 (t = 1) | ~2,500 | 34 / 35 | 0.024620 / 0.019006 | 0.107323 | 0.764 / 0.749 |

**Verdict (grade_cap_against_dns on all 88 rows): CAP HOLDS - worst
ratio anywhere 0.107323, eight times under 17/20, on the highest-
Reynolds DNS that exists.**

## 3. What the ladder shows

- **Global statistic: no trend toward the cap.** Per-rung means
  0.0288, 0.0327, 0.0229, 0.0266, 0.0218 across Re_lambda 433 -> 2,500;
  the highest rung carries the LOWEST mean. Seed-to-seed scatter on one
  dataset (~0.01) exceeds any rung-to-rung difference.
- **Sub-batch envelope: drifts upward with Re - FLAGGED.** The maximum
  over 100-point sub-batches rises monotonically 0.068 -> 0.070 -> 0.082
  -> 0.084 -> 0.107. This is the intermittency direction (max|omega| /
  omega_rms grows 5.4 -> 6.3 -> 7.5 -> ~9 -> 9.7 up the ladder, the
  textbook growth) and it is exactly the direction in which a violation
  would live. It is recorded as a flag for the full-token extreme-event
  scan: does the envelope keep growing with sample size and Re, or does
  it saturate far below 17/20? A naive extrapolation stays far under
  the cap; a naive extrapolation is not evidence, so the flag stands.
- **Resolution check at Re_lambda ~610:** 4096^3 (0.0265 / 0.0389) vs
  8192^3 snapshot 6 (0.0206 / 0.0253) agree within seed scatter - no
  resolution dependence detected at n = 1,000. The statistic is not an
  artefact of grid spacing at this sample size.
- **Pipeline sanity at every rung:** positive-stretching fraction in
  the 0.75-0.78 band throughout - the DNS skewness reproduced five
  times over.

## 4. What this grade is and is not (Rule 7)

IS: the first multi-Reynolds grade of the derived cap; the first
contact between the cap and the 32,768^3 record run; a negative answer
to "does the sampled statistic climb toward the cap with Re" over
nearly a decade of Re_lambda; a resolution-independence check.
IS NOT: the extreme-event scan. Random pointwise sampling still has no
power in the far tail; the flagged envelope drift is the sampled shadow
of that tail, not a measurement of it. The kill test - full-field
cutouts or the Kerr trefoil DNS - remains OPEN on Daniel's ledger.
Service note: isotropic4096 returned "result was not filled correctly"
on roughly ten attempts before both seeds landed; a transient JHTDB
backend fault, disclosed; every recorded number came from a 200.
Snapshot-index note: for the snapshot datasets `t` is an integer index
(isotropic8192: 1..6; 1-5 are the Re 1200-1300 frames, 6 the Re ~610
high-resolution frame) - B276's t = 1 is a high-Re frame as claimed.

## 5. Cross-references
PAPER_1182 (the cap statistic), PAPER_2263 (harness), PAPER_2267
(Theorem A - the resolution check speaks to its mode-count claim only
at DNS scales, not at k_c), PAPER_2270 (proof set - data front 1 now
SAMPLED PASS + LADDER PASS, envelope FLAGGED), PAPER_2271 (B276),
PAPER_2272 (B277), JHTDB citation policy (turbulence.idies.jhu.edu/
citing; isotropic32768 provenance: GESTS code, Georgia Tech, Frontier),
B278.
