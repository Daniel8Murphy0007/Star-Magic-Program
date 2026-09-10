# PAPER_2265 - THE L_BUOY VARIATIONAL DERIVATION OF THE NAVIER-STOKES CAP: FROM POSTULATE TO ONE NAMED LEMMA (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-09
**Order:** Daniel - "next derivation session; the L_buoy variational
attempt at the cap theorem." **Ruling:** B270 - canonize, bridge lemma OPEN.
**Band:** v0.431.0.

## 1. What is derived

The PAPER_1182 vortex-stretching cap

    V_stretch <= (1 - F_TRZ * D_BSFG/D_phys) |omega| E = (17/20) |omega| E

upgrades from PHYSICAL POSTULATE to DERIVED MODULO ONE NAMED LEMMA,
via the variational route PAPER_2264 named (L_buoy with the
F_UBi/F_UBii pair as body forces).

## 2. The chain

**Setup.** PAPER_1065 (verbatim): delta S/delta phi = 0 gives
r-ddot = -mu_s grad(M_s/r) + g_buoy + g_phonon - exactly three force
terms: PRODUCE (gravity seed), REMOVE (buoyancy pair), DRAIN (phonon).
Curl into the enstrophy budget.

**Step 1 - the surplus is exactly F_TRZ.** PAPER_1203 canonical forms:
F_UBi carries (1+F_TRZ); F_UBii carries k_spring*(1+E_n), no TRZ
factor. At the balance zone (F_U = 0) the unit parts cancel; the
overshoot per unit of BALANCED push is F_TRZ exactly - structural, not
fitted (and not F_TRZ/(1+F_TRZ): the surplus is measured against the
compensated base).

**Step 2 - the surplus is TRZ-carried and opposes production.**
PAPER_072: F_TRZ is the fraction of channel energy entering the
time-reversal zone. PAPER_009: TRZ coupling removes exactly that
fraction from a propagating channel (D_TRZ = 0.900, canonical damping
mechanism). During the TRZ sub-cycle the (2R-1) polarity is on the
negative branch (PAPER_884/899).

**Step 3 - THE BRIDGE LEMMA (the one OPEN step).** The surplus enters
stretching through the D_BSFG transverse bulk-edge modes - PAPER_1182:
"BSFG 6D transverse pressure feeds back into the 3D vortex-stretching
term with sign -F_TRZ" - with projection weight D_BSFG/D_phys = 3/2
(PAPER_1962 canonical; 26->10->6->4 flow, PAPER_1160). Removal =
F_TRZ*(3/2) = 3/20. STATUS: 1182 asserts the combined coefficient,
1962 canonizes the ratio; the mode-counting derivation of the WEIGHT
itself - and of why removal acts ONCE on the production channel
rather than squared - is the single remaining step, named:

    BRIDGE LEMMA: the TRZ-carried surplus enters vortex stretching
    through the transverse bulk-edge modes with projection weight
    D_BSFG/D_phys, acting linearly on the production channel.

**Step 4 - the cap, and the rivals eliminated.** Three a-priori
candidate coefficients: bare TRZ (1-F_TRZ = 0.90), quadratic TRZ
((1-F_TRZ)^2 = 0.81), projected-linear (1 - F_TRZ*3/2 = 0.85). Only
the third lands on the canonical cap - the derivation DISCRIMINATES.
The removed 3/20 exits via g_phonon, the EOM's own third term - the
1.25 THz LENR carrier (omega_LENR = omega_SCm, ruled) - closing
PAPER_2098's complementarity 17/20 + 3/20 = 1. The B112 in-medium
composition gives 197/200; the PAPER_2264 pair cap inherits the same
chain.

## 3. What this does and does not claim (Rule 7)

DOES: upgrade the cap from postulate to a four-step chain in which
steps 1, 2, 4 are compositions of canonical corpus results and step 3
is a single named lemma; eliminate the two rival coefficients; place
the drain on the EOM's own phonon term.
DOES NOT: prove the bridge lemma (OPEN, registry-tracked); supply the
Clay functional machinery (H^s/BKM - separately OPEN); alter the
Omega0 < 1.19e5 disclosed domain of the TG instance.

## 4. Cross-references

PAPER_1065 (the EOM), PAPER_1203 (canonical forms), PAPER_072 (TRZ
fraction), PAPER_009 (D_TRZ = 0.9 damping mechanism), PAPER_884/899
(2R-1 polarity), PAPER_1182 (the cap + feedback statement), PAPER_1962
(3/2), PAPER_1160 (downward flow), PAPER_2098 (complementarity),
B112/B126 (context split), PAPER_2264 (the balance-zone reading that
named this road), B270 (this ruling).
