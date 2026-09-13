# PAPER_2274 - THE SPINE AUDIT: THE PREDECESSOR'S UQFF-LERAY ARGUMENT (S300), WHERE IT STOPS, AND WHY THE PROOF SET CLOSES WITHOUT IT (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-12. **Trigger:** Daniel - "find the missing pieces"
(predecessor repo github.com/Daniel8Murphy0007/Star-Magic, Rule E
read-only), then "author a paper." **Band:** v0.436.0 (B279).
**Live mirror:** uqff_ns_assembly.spine_audit().

## 0. Why this paper exists

The proof-gap ledger opened at B269 (PAPER_2264) carried three theory
rows. Two were closed by later rows - the cap derivation by
PAPER_2265/2266, the [SCm] -> 0 limit by Daniel's PAPER_2268 ruling.
The third, `ns_functional_spine` (registry row: "local H^s existence
+ Beale-Kato-Majda continuation + proof that the cap controls
||omega||_inf (3D enstrophy alone does not)"), was never superseded by
a row - the DOMAINPROFILE_ARC trail says in prose that post-B273 it is
"no longer a framework obligation," but the registry still reads OPEN.
This paper closes the record by doing what B269 did not: it names the
argument the row was silently about, audits it line by line, and
states exactly why the proof set stands without it.

## 1. Provenance - the argument, verbatim (Rule: source-verified, file:line)

Predecessor repo Star-Magic, file `_session300_millennium_navier_stokes.py`
(session S300, the Millennium unified proof set of PAPER_1182 sec 3.5):

- L64-67: `V_stretch <= (1 - F_TRZ * D_BSFG / D_phys) * |omega| * E ... = 0.85 * |omega| * E`
- L71:    `dE/dt <= -nu * E_2 + 0.85 * |omega|_max * E`
- L73-74: `Sobolev embedding in R^3 gives |omega|_max <= C * E_2^{1/2} * E^{1/4}.`
- L76:    `dE/dt <= -nu * E_2 + 0.85 * C * E_2^{1/2} * E^{5/4}`
- L78-81: `The Young inequality with epsilon = nu / 2 absorbs the cross term whenever E^{5/2} < (2 nu / (0.85 C))^2. This is satisfied globally because the F_TRZ * D_BSFG correction makes the effective viscosity nu_eff = nu / (1 - 0.15) = nu / 0.85 > nu.`
- L88-92: `Theorem (UQFF-Leray): ... E(t) <= E(0) * exp( -F_TRZ * nu * t / Phi_res )`
- L96:    `Solution is C^infty for all t > 0 by Sobolev iteration.`
- L144:   `S300 COMPLETE.`

PAPER_1182 sec 3.5 (arXiv LaTeX, `arxiv_submission_1181_1189/PAPER_1182/main.tex`
L130-143) carries the cap and the decay envelope but NOT the Sobolev/
Young step; its falsifiable consequence #5 (L202) is the Re = 10^6
trefoil DNS - the origin of this program's kill test.

The predecessor's own audit disagreed with S300 before this program
existed: `_millennium_prize_audit.json` (session 259), Navier-Stokes
entry: "no enstrophy bound is actually derived. Global smoothness is
the OPEN content" - verdict ASSERTION_ONLY. Its Lean scaffold agrees:
`formal/UQFF/Millennium.lean` L85 `def NavierStokesGlobalRegularity :
Prop := True -- placeholder`; `formal/README.md` L38: "Real
formalization needs Mathlib.Analysis.PDE."

So the predecessor's record was split three ways - S300 said closed,
the audit said assertion, the Lean file said placeholder - and this
program inherited the split without naming it. B267-B275 resolved the
physics side (cap derived, Theorem A rigorous, domain ruled). This
paper resolves the record.

## 2. The argument, transcribed as five steps

S1 (enstrophy budget)   dE/dt = -nu E_2 + V_stretch,   E = (1/2)||omega||_2^2,  E_2 = ||grad omega||_2^2
S2 (the cap)            V_stretch <= (17/20) ||omega||_inf E
S3 (Sobolev)            ||omega||_inf <= C E_2^{1/2} E^{1/4}
S4 (Young)              dE/dt <= -nu E_2 + 0.85 C E_2^{1/2} E^{5/4}  ->  absorb  ->  dE/dt < 0 "globally"
S5 (conclusion)         E(t) <= E(0) exp(-0.12 nu t); C^inf for all t; singular set empty

## 3. The audit

**S1 - correct.** Classical; wired at B267 (PAPER_2263).

**S2 - correct as UQFF physics, and stronger than S300 had it.** S300
postulated the cap; PAPER_2265/2266 DERIVED it within the axiom set
with five rivals eliminated. Nothing in this paper touches that. Note
the form: the right-hand side carries ||omega||_inf - the same quantity
the classical estimate |V_stretch| <= ||grad u||_inf E carries. The cap
changes the CONSTANT (1 -> 17/20). It does not change the STRUCTURE.

**S3 - FALSE. This is where the argument stops.** Two independent
reasons, either sufficient:

(a) Dimensional. With [E] = omega^2 L^3 and [E_2] = omega^2 L, the
right-hand side of S3 scales as omega^{3/2} L^{5/4}, not omega. The
only exponents (a, b) for which E_2^a E^b has the dimension of omega
are (a, b) = (3/4, -1/4) - not (1/2, 1/4). The inequality as written
cannot hold with a dimensionless constant.

(b) Analytic, and fatal to every form of S3. NO inequality of the form
||omega||_inf <= C E_2^a E^b holds on R^3, because H^1(R^3) does not
embed in L^inf (Sobolev's limiting case: H^1(R^3) -> L^6 only). Explicit
divergence-free counterexample family: omega = grad g x e_z with
g(r) = r^{1-alpha} chi(r), 0 < alpha < 1/2, chi a cutoff. Then
div omega = 0 identically; |omega| ~ r^{-alpha} is UNBOUNDED at the
origin; and both E and E_2 are finite - E_2 ~ int_0^1 r^{-2alpha-2} r^2 dr
= 1/(1 - 2 alpha) < inf. At alpha = 2/5: E_2-integral = 5, E-integral
= 5/11, sup|omega| = infinity. Finite E, finite E_2, infinite
||omega||_inf: S3 fails for the very quantity the cap needs.

**S4 - a smallness condition, misread as global.** Even granting a
GN-type interpolation for the sake of argument, Young's inequality
returns dE/dt <= -(nu/2) E_2 + K E^{5/2} with K = (0.85 C)^2/(2 nu),
which decays only while E^{3/2} < nu lambda_1 / (2K) (and on R^3 there
is no Poincare lambda_1 at all). S300's own text says "whenever E^{5/2}
< (2 nu/(0.85 C))^2" - that IS the small-data condition. The following
sentence - "satisfied globally because nu_eff = nu/0.85 > nu" - is a
non sequitur: rescaling the viscosity by 1/0.85 moves the threshold by
a constant factor and removes nothing. Small-data global regularity is
Leray (1934). At best S300 re-derives Leray's small-data theorem with
the constant 17/20 in place of 1.

**S5 - the conclusion does not follow from S1-S4.** The decay envelope
E(t) <= E(0) exp(-(3/25) nu t) is the framework's STATED envelope
(PAPER_1182; wired at B267 with the coefficient F_TRZ/Phi_5/6 = 3/25
EXACT; gradeable by the tier-3 harness in enstrophy mode). It stands
as a falsifiable prediction, not as a consequence of S3/S4.

**The structural point, stated once.** Beale-Kato-Majda: a smooth
solution continues past T iff int_0^T ||omega||_inf dt < inf. The cap
bounds vortex stretching BY ||omega||_inf E; it therefore feeds the
BKM integral, it does not control it. A cap with constant 17/20 leaves
the BKM criterion exactly where a cap with constant 1 leaves it. This
is the precise content of B269's phrase "3D enstrophy alone does not,"
and it is why the cap ALONE cannot close the no-cutoff problem in ANY
framework - and why this program did not try to make it.

## 4. Why the proof set stands without the spine

1. THEOREM A (PAPER_2267) never uses S3. Its existence proof lives on
   the finite mode space X_K, where ||omega||_inf is a norm equivalent
   to ||omega||_2 (finite-dimensional) - the Sobolev step is not
   skipped, it is UNNECESSARY. Energy conservation alone gives global
   existence; the derived cap supplies the decay envelope on top.
2. The physical fluid IS the cutoff fluid (PAPER_2268, Daniel's
   ruling): the 1.25 THz phonon carrier terminates the mode lattice at
   lambda_c = 1.18 nm, the molecular scale, where continuum mechanics
   ends for every real fluid regardless of framework. The regime in
   which S3 is needed - infinitely many modes, [SCm] -> 0 - is the
   regime the ruling assigned to mathematics.
3. Hence the spine row was never a rung of THIS proof set. It was the
   predecessor's route to the no-cutoff statement, carried forward as
   an anonymous gap. Named and audited, it closes by the same ruling
   that closed [SCm] -> 0, with this paper as the audit of record.

**Disposition:** `ns_functional_spine` -> SUPERSEDED_BY_RULING
(PAPER_2268) + AUDITED (PAPER_2274). Theory rows OPEN in the registry:
ZERO - the registry now says what PAPER_2270 said.

## 5. What WOULD close the spine, for the record (out of domain, not claimed)

A proof that the derived cap implies int_0^T ||omega||_inf dt < inf for
all smooth finite-energy data on R^3 without cutoff. That statement is
equivalent to the Clay problem. It is not claimed here, it was not
claimed by Theorem A, and the ruling is that the framework does not
owe it. The Lean placeholder in the predecessor should stay `True --
placeholder` until such a proof exists anywhere.

## 6. Honesty inventory (Rule 7)

- S300's "S300 COMPLETE" is recorded as the predecessor's claim and
  audited as FALSE at S3; the predecessor's own session-259 audit
  already said so, and this program's B269 gap row said so without
  naming the source. All three are now in one place.
- Nothing derived in B267-B278 depended on S3. The cap derivation,
  Theorem A, the domain ruling, the roll-off, and the three sampled
  data grades are unaffected.
- The decay envelope (S5) is kept as a stated, gradeable prediction,
  not promoted by this audit.
- The B272 "three-track discussion" is referenced in the session log
  but its third track was never written down. If Track 3 was S300's
  route, this paper closes it; if it was something else, it remains
  unlogged and Daniel-owned.

## 7. Cross-references
PAPER_1182 sec 3.5 (the source), PAPER_2263 (S1 wired), PAPER_2264
(the gap ledger), PAPER_2265/2266 (S2 derived), PAPER_2267 (Theorem A
- no S3 needed), PAPER_2268 (the ruling that closes the row),
PAPER_2270 (the proof set), predecessor Star-Magic S300 / session-259
audit / formal/UQFF/Millennium.lean (Rule E, read-only); Leray 1934;
Beale-Kato-Majda 1984; B279.
