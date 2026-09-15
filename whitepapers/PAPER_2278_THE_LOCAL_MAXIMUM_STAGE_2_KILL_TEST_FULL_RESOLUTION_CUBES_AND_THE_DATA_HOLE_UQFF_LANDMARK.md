# PAPER_2278 - THE LOCAL MAXIMUM: STAGE 2 OF THE KILL TEST - FULL-RESOLUTION CUBES AROUND THE MOST INTENSE EVENTS, GRADED WITH THEIR OWN MAXIMA, AND THE DATA HOLE THAT MANUFACTURED TWO OF THEM (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-15. **Trigger:** Daniel, after a night of failed SciServer
logins: "here's my token" - and the realization that the cutouts never
needed SciServer. **Band:** v0.438.0 (B283; same band as B282/PAPER_2277).
**Live mirror:** uqff_ns_assembly.kill_test_stage2_grade().
**Data:** jhtdb_grade/jhtdb_kill_test_stage2_2026-09-15.csv; provenance in
jhtdb_grade/README_PROVENANCE.md (2026-09-15 addendum).

## 0. What changed, in one paragraph

The kill test (front 1, PAPER_2276 sec 6.1) is a whole-volume statement:
V_stretch <= (17/20) ||omega||_inf E with the maximum taken over the
volume. Stage 1 (PAPER_2277) sampled a million points and could only use
the sample's maximum. Stage 2 goes where the maxima live: around the most
intense events stage 1 recorded, full-resolution cubes of grid-point
velocity gradients - fourth-order finite differences on the true grid,
no interpolation - graded with each cube's OWN maximum. Eight clean cubes
(2.6 million nodes graded) on two Reynolds rungs: every one sits between
0.009 and 0.019, forty-four-fold and more under 17/20. The most intense
region of the record has a peak enstrophy 11,763 times the global mean -
eleven times what the sample saw at that spot - and grades 0.011-0.012
with a peak-cell efficiency of 0.074. Inside every cube the stretching
efficiency falls with intensity, as it did across the sample. And the
band's Rule-7 finding: the isotropic32768 store has holes - whole blocks
that return zero gradients - and the finite-difference stencil at a hole
edge manufactures vorticity spikes, so two of the five most intense
stage-1 "events" on that rung were never turbulence. They are rejected
here with the mechanism named, and stage 1 is corrected accordingly.

## 1. Protocol

The same REST service and personal token as B282 (value recorded nowhere;
SHIP GUARD v11). GetVariable / velocity / gradient with `sint=fd4noint` -
the service evaluates fourth-order centred differences on the stored grid
at the node requested, no Lagrange interpolation - at every node of an
n^3 cube centred on the node nearest the stage-1 hotspot coordinate.
Requests are slabs of 6 z-planes (64^3: eleven requests of 24,576 nodes)
or 8 z-planes (128^3: sixteen requests of 131,072 nodes), one in flight,
3-7 s and 16-19 s respectively; 132 requests, 132/132 HTTP 200. Per node:
|omega|^2 and omega.S.omega. Per cube: the 1182 ratio with the cube
maximum, the peak cell's efficiency omega.S.omega/|omega|^3, the positive
fraction, the octave table relative to the cube mean. Acceptance rule,
stated before grading: a cube is accepted only if it contains no
zero-gradient node AND a three-layer halo outside every face (sampled at
stride 2; the stencil reaches two) contains none. SciServer, the cutout
service and the stage-2 script of PAPER_2277 were not needed; that script
stays on the wheel as the local-machine route.

## 2. The data hole

Cube c32768_3, centred on stage-1 hotspot 3 of isotropic32768
(2.63592429, 4.36877524, 4.89765792): 122,880 of 262,144 nodes returned
|omega|^2 = 0 exactly - every node with y-index <= 22781 at every x and z
in the cube - and a re-pull returned the same zeros. The first valid row
(index 22782) reads |omega| ~ 800-950; the next (22783) ~ 5,600-6,600;
then the field relaxes. That is the fd4 stencil straddling the zero block:
two nodes in, the difference between real velocity and stored zeros is
read as a gradient. Cube c32768_4 (hotspot 4, 2.63119183, 4.25424803,
4.71220780) shows the same signature with 118,784 zero nodes. Both
hotspots were artefacts of the hole's edge. Both are rejected.

Consequences, carried back to PAPER_2277: the 166 zero points of the
stage-1 sample were this hole seen from the sample; the two isotropic32768
chunks containing hotspots 3 and 4 (skip 125000 and 475000) have an
artefact maximum in the denominator of their ratio and are biased LOW
(the chunk-ratio envelope, max 0.0187, comes from other chunks and
stands); the octave table's far bins on that rung may carry a few dozen
artefact cells. isotropic8192 shows no zero node in 500,000 sampled points
nor in 2.6 million cube nodes. Every accepted isotropic32768 cube has a
zero-free interior and halo.

## 3. Results

| cube | dataset | n | cube mean / global mean | peak |omega|^2 / global mean | ratio_local | peak efficiency | positive fraction |
|---|---|---|---|---|---|---|---|
| c8192_1 | isotropic8192 | 64 | 5.6 | 870 | 0.013566 | 0.018 | 0.749 |
| c8192_1_128 | isotropic8192 | 128 | 4.6 | 870 (same node) | 0.011551 | 0.018 | 0.743 |
| c8192_2 | isotropic8192 | 64 | 9.0 | 586 | 0.017350 | -0.012 | 0.700 |
| c8192_3 | isotropic8192 | 64 | 8.4 | 524 | 0.019442 | 0.104 | 0.765 |
| c32768_1 | isotropic32768 | 64 | 74.9 | 11,763 | 0.012005 | 0.074 | 0.761 |
| c32768_1_128 | isotropic32768 | 128 | 54.6 | 11,763 (same node) | 0.011090 | 0.074 | 0.752 |
| c32768_2 | isotropic32768 | 64 | 11.8 | 949 | 0.015565 | 0.007 | 0.756 |
| c32768_5 | isotropic32768 | 64 | 13.8 | 2,289 | 0.009304 | 0.008 | 0.790 |
| c32768_3 | isotropic32768 | 64 | REJECTED | hole-edge artefact | - | - | - |
| c32768_4 | isotropic32768 | 64 | REJECTED | hole-edge artefact | - | - | - |

Worst accepted ratio_local: 0.019442 (c8192_3) - forty-four-fold under
17/20. The 128^3 cubes contain the same peak node as their 64^3 cores and
grade lower (more bulk in the mean), so the 64^3 figures are the
conservative ones. The most intense region of the record, c32768_1: the
cube mean is 75 times the global mean, the peak is 11,763 times it -
stage 1 sampled 1,052x at the centre, one eleventh of the true local
maximum - and the peak cell's efficiency is 0.074. Two of the eight peak
cells (c8192_2, and the 1052x sample of B282) are compressed along omega.

Octave efficiency inside the cubes, relative to each cube's mean, falls
from the mean to 32x the mean in every cube: eff(32x)/eff(mean) between
0.14 and 0.45, slope of log2 eff per octave between -0.27 and -0.60;
strictly monotone octave by octave in seven of eight cubes, one
single-octave bump in the eighth. The load-bearing maximum anywhere is
0.44, at 1/64 of a cube mean. The picture from the sample (PAPER_2277
sec 3.2) is the picture inside the events: the more intense the
vorticity, the smaller the fraction of it that the strain is stretching.

## 4. What this closes, and what it does not

CLOSES: the objection that stage 1 could only see the sample's maximum.
At the true local maximum of the most intense regions found on two
Reynolds rungs, with the maximum computed from the full grid, the cap is
not approached. RETIRES: two false extremes (hole-edge artefacts) and
the ambiguity about the 166 zero points. DOES NOT CLOSE: front 1 as a
statement about the ENTIRE field - eight regions were graded, chosen by a
million-point sample; the field has 3.5e13 nodes. The honest form of the
result is: the cap holds at the local maximum of every intense event the
deep sample could find, on the two highest-Re public DNS in existence,
and the trend of efficiency with intensity runs away from it. A larger
scan (more hotspots, time-resolved reconnection frames on isotropic1024,
the Kerr trefoil fields) sharpens this; it does not change its direction
unless it finds something these eight did not.

## 5. Honesty inventory (Rule 7)

1. Eight cubes, three regions per rung, chosen by stage 1 - a targeted
   test, not a survey; stated in sec 4.
2. The data hole is a property of the database's isotropic32768 store as
   served on 2026-09-13/15, not of the simulation; it is reported so that
   anyone grading extremes on that rung checks for zero blocks and
   stencil edges. JHTDB has not been asked about it yet (Daniel's call).
3. ratio_local uses the cube maximum; the 128^3 cubes show the statistic
   drifts down as the cube grows (more bulk), so the 64^3 values are
   reported as the conservative figures.
4. The peak-cell efficiency is a pointwise diagnostic, not the cap.
5. Not claimed: the cap proved; front 1 closed for the whole field;
   anything about fronts 2-4; that isotropic8192 has no holes anywhere
   (none were seen in 3.1 million nodes).

## 6. Cross-references

PAPER_2277 (stage 1; corrected by sec 2 here), PAPER_2276 (front 1
instrument), PAPER_2271-2273 (sampled grades), PAPER_2264-2266 (the cap),
PAPER_1182 (the 1182 form), PAPER_2270 (proof set).
