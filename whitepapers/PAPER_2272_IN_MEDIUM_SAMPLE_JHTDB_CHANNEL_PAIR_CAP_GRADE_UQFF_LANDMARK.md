# PAPER_2272 - THE IN-MEDIUM SAMPLE: THE PAIR CAP'S SECOND BRANCH ON JHTDB CHANNEL FLOW (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-10 (data) / 2026-09-11 (fold). **Trigger:** Daniel
re-supplied the publicly sanctioned JHTDB testing token after B276;
the pair cap of PAPER_2264 names an IN-MEDIUM branch (197/200) that
only wall-bounded, medium-dominated turbulence can address.
**Band:** v0.435.0 (B277).

## 1. What was done

Two 1,000-point samples of the velocity-gradient tensor were queried
from JHTDB **channel** - the turbulent channel-flow DNS at Re_tau ~ 1000
(wall-bounded shear turbulence, the IN-MEDIUM regime of the B112
context split) - snapshot t = 1.0, var = velocity, sop = gradient,
sint = fd4lag4, through the official REST service with the public
testing token (2 x 1,000 points, well under the sanctioned 4,096), at
deterministic LCG points (seeds 28/29 of the same generator as B276;
bit-reproducible by anyone). Sampling box: x in [0, 8pi], y in
[-0.9, 0.9], z in [0, 3pi]. **The walls (|y| > 0.9) were excluded** -
disclosed here, in the module, and in the provenance file.
Full provenance: jhtdb_grade/README_PROVENANCE.md (2026-09-10 addendum).

## 2. The grade

Sampled transcription of the PAPER_1182 cap, graded against BOTH
branches of the PAPER_2264 pair
(vacuum 1 - F_TRZ*(D_BSFG/D_phys) = 17/20;
 in-medium 1 - F_TRZ^2*(D_BSFG/D_phys) = 197/200):

    ratio = mean(omega.S.omega) / ( max|omega| * mean|omega|^2 )

| Sample | n | ratio | vs 197/200 (in-medium) | vs 17/20 (vacuum) |
|---|---|---|---|---|
| seed 28 | 1000 | 0.039143 | HOLDS (25x margin) | HOLDS (22x) |
| seed 29 | 1000 | 0.031072 | HOLDS (32x margin) | HOLDS (27x) |
| sub-batches (2 x 10 x 100) | 100 | max 0.073405 | HOLDS (13x margin) | HOLDS (11x) |

**Verdict (via grade_cap_against_dns with the `cap` argument - the
tier-3 harness, first use of the pair-cap argument its B269 docstring
promised): THE IN-MEDIUM BRANCH HOLDS on this dataset.** Under both
caps, by an order of magnitude.

## 3. Pipeline honesty checks

- Positive-stretching fraction: 0.736 / 0.764 - the DNS net-positive
  vortex-stretching skewness reproduced in a wall-bounded shear flow
  (slightly below the isotropic 0.778/0.754 of B276, as the mean shear
  would suggest). The pipeline computes real physics.
- Same code path, same statistic, same token discipline as B276; the
  only construct added to the package is the `cap` argument.

## 4. What this grade is and is not (Rule 7)

IS: the first contact between the pair cap's in-medium branch and
measured wall-bounded turbulence; a real PASS through the pre-built
harness on bit-reproducible public data; data front 2 of the proof set
(PAPER_2270) moves from AWAITING to SAMPLED CONSISTENCY PASS.

IS NOT: the pair-cap DISCRIMINATION. At these margins the sampled
statistic passes BOTH branches by more than 10x - it cannot pick
between 197/200 and 17/20, so it cannot confirm the prediction that
lab/in-medium turbulence caps near 0.985 while vacuum-coupled flows cap
near 0.85. That discrimination lives in the far tail (extreme
stretching events), exactly where the B276 kill test lives. Front 2
therefore reads: in-medium branch CONSISTENT - discrimination OPEN.
Also not sampled: the wall region (|y| > 0.9), where the strongest
shear-driven stretching would sit. A consistency PASS is a real grade,
and it is labeled as consistency everywhere it appears.

## 5. What would settle front 2

Far-tail statistics from full-field cutouts (JHTDB full token) or the
Kerr trefoil/reconnection DNS, graded separately in a vacuum-coupled
astrophysical flow and in a laboratory/in-medium flow. If the in-medium
tail ever exceeds 197/200, the pair cap is dead; if it sits between
17/20 and 197/200 while the vacuum tail stays under 17/20, the pair is
discriminated. Daniel ledger, unchanged.

## 6. Cross-references
PAPER_1182 (the cap statistic), PAPER_2264 (the pair cap, B269),
PAPER_2263 (harness), PAPER_2270 (proof set - front 2 now SAMPLED
CONSISTENCY PASS), PAPER_2271 (B276, the vacuum-branch first contact),
JHTDB citation policy (turbulence.idies.jhu.edu/citing), B277.
