# PAPER_2269 - THE PHONON ROLL-OFF PROFILE: THE GAUSSIAN ENVELOPE AT 1.25 THZ, DERIVED AND FALSIFIABLE (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-10. **Order:** Daniel - "go for ... roll-off derivation."
**Band:** v0.433.0 (B274).

## 1. The profile

    Phi(f) = exp( -(f - f_c)^2 / (2 Gamma^2) )
    f_c = 1.25 THz (omega_SCm, canonical)
    Gamma = 0.1 THz (PAPER_910/911 canonical phonon linewidth)
    Q = f_c/Gamma = 25/2 = K_MEX * D_BSFG EXACT (PAPER_1804)

**Two-tier Rule 4 compliance (the envelope is corpus-selected, not
imported):** PAPER_910 derives the inputs (Gamma, omega_SCm) AND
itself uses this exact Gaussian envelope in its jet modulation factor
M_jet = exp(-(omega-omega_SCm)^2/(2 Gamma^2)) * S_26 * (2 F_UBi/F_U - 1).
Tier 1 satisfied; nothing classical is substituted.

## 2. What the profile closes

The Theorem A step-function cutoff is now JUSTIFIED, not assumed:
low-frequency leakage Phi(0) = exp(-Q^2/2) = exp(-78.125) ~ 1.2e-34.
The sharp cutoff was honest to thirty-four decimal places - it was
never an idealization, it was a Gaussian this narrow.

## 3. Falsifiable predictions

1. THz-bench transmission dip: centered 1.25 THz, GAUSSIAN shape,
   FWHM = 2 sqrt(2 ln 2) Gamma = 0.235 THz (on the 910/911 linewidth).
   This gives the B112 canonical-branch "THz-bench transmission dip"
   observable its PROFILE.
2. DISCRIMINATOR, disclosed: the corpus carries a second Gaussian
   width - PAPER_896's modulation envelope at 0.2 THz (FWHM 0.471 THz,
   as corrected by the PAPER_2154 Flag-(d) audit). The bench
   experiment DISCRIMINATES between the two widths. The discrepancy is
   FLAGGED for Daniel's ruling, not resolved here: 910/911 (linewidth,
   Q = 25/2 primitive-locked) vs 896 (modulation envelope) may be two
   different physical objects or one drifted value.
3. DNS/experimental spectra: no independent dynamics above
   f_c + ~2 Gamma; the roll-on of damping approaching the line is
   Gaussian, not power-law.

## 4. Primitive content

Gamma/f_c = 2/25 = 1/(K_MEX*D_BSFG) EXACT; FWHM/f_c =
2 sqrt(2 ln 2)/Q (mathematical constant over a locked primitive).
No new free parameters.

## 5. Cross-references
PAPER_910/911 (linewidth + envelope precedent), PAPER_1804 (Q =
25/2), PAPER_896 + PAPER_2154 Flag (d) (the second width, flagged),
PAPER_2267 (Theorem A, step now justified), B112 (THz-bench
observable), B274 (this order).
