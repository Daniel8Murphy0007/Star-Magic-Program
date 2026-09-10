# PAPER_2271 - THE FIRST REAL-DATA GRADE: THE NS CAP HOLDS ON JHTDB ISOTROPIC8192 (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-10. **Trigger:** Daniel supplied the JHTDB portal;
the publicly sanctioned testing token (< 4,096 points) made an
immediate sampled grade possible. **Band:** v0.434.0 (B276).

## 1. What was done

Two 1,000-point samples of the velocity-gradient tensor were queried
from the HIGHEST-REYNOLDS public DNS in existence - JHTDB
isotropic8192 (8192^3, Re_lambda ~ 1300), snapshot t = 1.0 - through
the official REST service with the public testing token, at
deterministic LCG points (seeds 26/27; bit-reproducible by anyone).
Full provenance: jhtdb_grade/README_PROVENANCE.md.

## 2. The grade

Sampled transcription of the PAPER_1182 cap
(V_stretch <= (17/20) ||omega||_inf E):

    ratio = mean(omega.S.omega) / ( max|omega| * mean|omega|^2 )

| Sample | n | ratio | vs cap 17/20 |
|---|---|---|---|
| seed 26 | 1000 | 0.028660 | HOLDS (30x margin) |
| seed 27 | 1000 | 0.024624 | HOLDS (35x margin) |
| seed 27 sub-batches (10 x 100) | 100 | max 0.084421 | HOLDS (10x margin) |

**Verdict (via grade_cap_against_dns, the tier-3 harness): CAP HOLDS
on this dataset.** The proof set's first outside-data front returns
PASS.

## 3. Pipeline honesty checks

- Positive-stretching fraction: 0.778 / 0.754 - the textbook DNS
  net-positive skewness of vortex stretching, reproduced. The
  pipeline computes real physics.
- Enstrophy scale: omega_rms ~ 167-187 /s (code units), max sampled
  |omega| ~ 7.8-9.6 x rms - consistent with a 1,000-point sample of
  high-Re intermittency.

## 4. What this grade is and is not (Rule 7)

IS: the first contact between the derived cap and measured turbulence
at Re_lambda ~ 1300; a real PASS through the pre-built harness on
bit-reproducible public data. IS NOT: the extreme-event scan. Random
pointwise sampling has essentially no power in the far tail where a
violation would live (reconnection/trefoil-class events); that scan -
full-field cutouts or the Kerr trefoil DNS - remains THE kill test,
OPEN, on Daniel's ledger (full token) exactly as before. A sampled
PASS is a real grade, not the final word.

## 5. Cross-references
PAPER_1182 (the cap), PAPER_2263 (harness), PAPER_2270 (proof set -
data front 1 now SAMPLED-PASS), JHTDB citation policy
(turbulence.idies.jhu.edu/citing), B276.
