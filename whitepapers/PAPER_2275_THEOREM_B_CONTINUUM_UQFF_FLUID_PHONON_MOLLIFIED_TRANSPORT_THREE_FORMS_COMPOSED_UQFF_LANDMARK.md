# PAPER_2275 - THEOREM B: GLOBAL REGULARITY OF THE CONTINUUM UQFF FLUID VIA PHONON-MOLLIFIED TRANSPORT - THE THREE PHONON FORMS (LINE, THRESHOLD, TAIL) COMPOSED (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-12. **Trigger:** Daniel - "I have a feeling the solution
is all three. Let's solve for all three." **Band:** v0.436.0 (B280).
**Live mirror:** uqff_ns_assembly.theorem_b() (folded 2026-09-13, B280).
**Status of this paper:** WIRED (B280) - dispatch PAPER_2275, gate pin,
registry rows theorem_b_continuum + phonon_mollifier_width_eps, eight
satellite band rows; the PAPER_106 exponent ruling of sec 8 stays OPEN.

## 0. The claim, in one paragraph

Track 3 of the B272 discussion - a regularity theorem for the UQFF
fluid WITHOUT truncation, infinitely many modes, no ruling needed - is
closed by composing three phonon-sector forms the corpus already
carries: the resonance LINE at the carrier (PAPER_893/910/2269), the
THRESHOLD at E_SCm = h f_c (PAPER_1907 sec 2.1, PAPER_1072, PAPER_102
S204), and the Gaussian TAIL in mode number q^{n^2}, q = exp(-beta_i
[SSq]) (PAPER_1042). Composed, they make the phonon sector's action on
the fluid a Fourier multiplier that is unity below k_c, shoulders at
k_c, and falls as a Gaussian above it. A Gaussian multiplier in k is a
Gaussian mollifier in x, and acting on the TRANSPORT velocity it turns
the continuum UQFF fluid into Leray's 1934 regularized system, whose
global existence, uniqueness and smoothness for every smooth
divergence-free finite-energy datum on R^3 is a classical theorem.
That is THEOREM B. It needs neither the cap nor any Sobolev embedding -
the step S300 could not take (PAPER_2274) is not skipped, it is
unnecessary, because mollified transport is bounded. Theorem A
(PAPER_2267) is its sharp-filter limit. The mollifier width is fixed by
primitives with no free parameter, epsilon = sqrt(2 beta_i [SSq])/k_c =
0.156 nm, under ONE flagged identification (sec 6). The constant in the
theorem diverges as epsilon -> 0: that divergence IS the domain boundary
PAPER_2268 ruled - the Clay statement is not claimed.

## 1. The three forms, verbatim (Rule: source-verified, file:line)

**Form A - the LINE (coupling AT the carrier).**
- PAPER_893 L36: `Phi_{1.25THz} = Phi0 * exp[-(omega-omega_SCm)^2/(2 Gamma^2)] * S26`
- PAPER_2269 sec 1 (B274): `Phi(f) = exp(-(f - f_c)^2 / (2 Gamma^2))`, Gamma = 0.1 THz, Q = f_c/Gamma = 25/2 = K_MEX * D_BSFG EXACT
- PAPER_1907 L78-81 (Lorentzian variant): `detuning = |omega_SCm - omega_driver|/omega_SCm; Q_UQFF = 10^6 * SSq * K_MEX = 1.188e6; Lorentzian_amp = 1/(1 + Q^2 * detuning^2)`
Form A says what the phonon sector does AT f_c. It vanishes away from
the line and therefore says nothing about modes far above it - which is
exactly why B274's derived profile could not, by itself, carry a
continuum theorem (PAPER_2274 sec 3, the Track-3 review).

**Form B - the THRESHOLD (where the lattice ends).**
- PAPER_1907 L71: `E_SCm = 8.28e-22 J is the SCm CUTOFF energy - quantum states with E_min > E_SCm are suppressed by the SCm coupling.`
- PAPER_1072 L19: `H_SCm(T) = 1 / (1 + exp(-(T - T_SCm) / Delta_T))` - the smooth Heaviside activation, T_SCm ~ 60 K <-> omega_SCm = 1.25 THz (L27)
- PAPER_102 L168: `Spectral cutoff: modes above 1.25 THz damped`
Form B fixes the location k_c = 2 pi f_c / c_s (lambda_c = 1.18 nm for
water, PAPER_2267) and the shape of the shoulder (logistic). It does not
fix how fast the suppression grows past k_c.

**Form C - the TAIL (how the suppression grows).**
- PAPER_1042 L26: `Z_phonon = sum_{n=1}^{26} q^{n^2} * chi(n) * S_26(n)`; L21: `q = exp(-beta_i * [SSq])`; L32: `q = exp(-0.344)`
- PAPER_205 L147-149: `Exponential suppression e^{-[SSq]*n/26}: deeper layers (larger n) contribute less ... Layer 26: highest mode, suppressed by e^{-[SSq]}`
Form C is the one Form A and Form B cannot supply: a weight that KEEPS
falling with mode number above the carrier. q^{n^2} is a Gaussian in n.

## 2. The composed multiplier, and the number it fixes

Let n = k/k_c (harmonic index of a fluid mode relative to the carrier -
the ONE identification this paper makes; sec 6). Composing A, B, C:

    m(k) = H_SCm(k_c - k) [Form B shoulder]  x  q^{(k/k_c)^2} [Form C tail]
         ~ 1                        for k << k_c
         ~ exp(-beta_i [SSq] k^2 / k_c^2)   for k > k_c

The tail is a Gaussian in k, i.e. m(k) = exp(-epsilon^2 k^2 / 2) with

    epsilon^2 = 2 beta_i [SSq] / k_c^2
    epsilon   = sqrt(2 * 0.6029 * 0.57) / k_c = 0.8290 / k_c
              = 0.8290 * lambda_c / (2 pi) = 0.1319 lambda_c = 0.156 nm   (water)

No free parameter: beta_i = 0.6029 (PAPER_1203), [SSq] = 0.57
(PAPER_1154), k_c from f_c = 1.25 THz and c_s = 1480 m/s (PAPER_2261
anchor). Multiplier values: m(k_c) = 0.709, m(2k_c) = 0.253, m(3k_c) =
0.045, m(5k_c) = 1.9e-4. Form A rides on top of this as the resonance
at k_c itself and is unchanged (the THz-bench dip, FWHM 0.235 THz,
PAPER_2269, stands as the bench observable).

A Gaussian in k is the Fourier transform of a Gaussian in x:
rho_epsilon(x) = (2 pi epsilon^2)^{-3/2} exp(-|x|^2 / 2 epsilon^2). The
phonon sector therefore acts on the fluid as CONVOLUTION WITH A
GAUSSIAN OF WIDTH 0.156 nm - it smooths the field over roughly one
atomic radius, inside the 1.18 nm molecular scale. (Coincidence,
disclosed and NOT canonized: q = exp(-beta_i [SSq]) = 0.7092 echoes the
rho_SCm mantissa 7.09; the corpus has flagged this mantissa echo before
- PAPER_161 - and it is flagged again here, nothing more.)

## 3. Where the mollifier acts: on the transport (corpus-selected)

PAPER_102 sec 6 and PAPER_154 L162 place the phonon/SCm action in the
transport-and-dissipation balance of the fluid ("forces the viscous
dissipation term to always dominate at small scales"); PAPER_1907 sec
2.1 places the suppression on the STATES that carry energy, not on the
viscosity. The corpus-consistent placement is therefore on the
advecting field: the fluid is transported by its phonon-smoothed self.
This is exactly Leray's regularization. (Placing it on the nonlinear
term as a whole, P m(D)[(u.grad)u], would break the energy identity for
a non-projection m; placing it on the viscosity alone would be
hyperviscosity, which the corpus does not state and this paper does not
need. The transport placement conserves energy and is the one Leray
used. Two-tier Rule 4: the mathematics is classical and says so; the
physics selecting the placement is corpus content.)

## 4. THEOREM B

Let epsilon > 0 (physically, 0.156 nm), rho_epsilon the Gaussian of sec
2, and for a divergence-free field u write u_epsilon = rho_epsilon * u
(convolution; divergence-free is preserved). Consider the continuum
UQFF fluid on R^3 with phonon-mollified transport:

    d_t u + (u_epsilon . grad) u + grad p = nu Laplacian u,   div u = 0,   u(0) = u_0

with u_0 smooth, divergence-free, finite energy. ALL Fourier modes are
present; nothing is truncated.

**THEOREM B.** For every such u_0 there exists a UNIQUE global solution
u in C^inf((0, infinity) x R^3) with ||u(t)||_2 <= ||u_0||_2 for all t.

**Proof (classical; Leray 1934, the "equations regularisees").**
(i) Energy. Since div u_epsilon = 0, <(u_epsilon.grad)u, u> = integral
u_epsilon . grad(|u|^2/2) = 0, so d/dt ||u||_2^2 = -2 nu ||grad u||_2^2
<= 0. RIGOROUS.
(ii) The mollified transport is bounded by the energy. ||grad
u_epsilon||_inf <= ||grad rho_epsilon||_2 ||u||_2 = C epsilon^{-5/2}
||u||_2 <= C epsilon^{-5/2} ||u_0||_2 =: M_epsilon, a CONSTANT for fixed
epsilon. (This is the step S300 needed and could not have: it bounds a
sup norm by an L^2 norm, and it is legitimate precisely because the
field being bounded is the SMOOTHED one.) RIGOROUS.
(iii) H^1 bound. Differentiating the equation and testing against grad
u, the transport contributes at most 2 ||grad u_epsilon||_inf ||grad
u||_2^2 (the term with u_epsilon . grad acting on grad u integrates to
zero by (i)'s argument), so d/dt ||grad u||_2^2 <= 2 M_epsilon ||grad
u||_2^2 - 2 nu ||D^2 u||_2^2 <= 2 M_epsilon ||grad u||_2^2, and by
Gronwall ||grad u(t)||_2^2 <= ||grad u_0||_2^2 exp(2 M_epsilon t) <
infinity for every t. RIGOROUS.
(iv) Global existence, uniqueness, smoothness. Local well-posedness in
H^1 is standard for this system (the nonlinearity is Lipschitz on H^1
because u_epsilon is smooth); the a-priori H^1 bound of (iii) forbids
blow-up, so the solution is global; the same estimates at every
derivative order (each higher norm obeys a Gronwall inequality with the
same M_epsilon) give C^inf in x and t; uniqueness follows from the
Lipschitz property. RIGOROUS. QED.

The theorem uses: energy conservation of divergence-free transport, and
the smoothing of ONE field. It does not use the cap, the decay
envelope, Sobolev embedding, BKM, or the truncation.

## 5. What Theorem B closes, and how it sits beside Theorem A

- **Theorem A (PAPER_2267)** is the sharp-filter case: P_K, the
  projection onto |k| <= k_c, is the epsilon -> "sharp" limit of the
  Gaussian multiplier of sec 2; the finite mode space makes the sup-norm
  bound trivial. Theorem B is the same physics with the corpus's own
  smooth tail instead of a step - and B274 already showed the step was
  honest to 34 decimals (PAPER_2269 sec 2). Two faces, one conclusion.
- **The cap (PAPER_2265/2266)** is not needed for existence in either
  theorem (as PAPER_2267 sec 4 already said); it supplies the decay
  envelope on top, and its data grades (B276-B278) stand unchanged.
- **The ruling (PAPER_2268)** now has an equation to point at: the
  constant M_epsilon = C epsilon^{-5/2} ||u_0||_2 DIVERGES as epsilon ->
  0. The framework's solutions at [SCm] -> 0 are exactly Leray's
  approximating sequence; their weak limits are the Leray-Hopf weak
  solutions; whether that limit is smooth is the Clay statement. The
  ruling assigned that question to mathematics. Theorem B makes the
  boundary quantitative - epsilon = 0.156 nm is where the framework's
  rigor ends and the idealization begins - and claims nothing across it.
- **Track 3** (the B272 discussion's unlogged third track) is CLOSED
  POSITIVE: a no-truncation regularity theorem for the UQFF fluid
  exists, in domain, no ruling needed, on the corpus's own three forms.
  What it is NOT: a no-cutoff theorem. The cutoff moved from a step in
  k to a Gaussian in x; it did not disappear. Nothing about real fluids
  requires it to.
- **The spine row (PAPER_2274)** stays closed; Theorem B is a second,
  independent reason it was never a rung: neither theorem the framework
  owns needs it.

## 6. Honesty inventory (Rule 7)

1. THE ONE IDENTIFICATION: mode index n of Form C is read as k/k_c
   (harmonic order of a fluid mode relative to the carrier). PAPER_1042
   runs n over the 26 levels; the corpus does not state n = k/k_c for
   fluid modes. FLAGGED. Theorem B does not depend on it - ANY smooth
   Gaussian or exponential tail gives the theorem for some epsilon > 0;
   only the NUMBER 0.156 nm depends on it. Under PAPER_205's alternative
   e^{-[SSq] n/26} the tail is exponential (a Poisson-type kernel, still
   a valid Leray mollifier) and the scale reads [SSq]/(26 k_c) = 0.004
   nm; the identification is the same. Daniel-gated.
2. Lions hyperviscosity (the route the Track-3 review left open) is NOT
   in the corpus and is NOT needed; a Gaussian filter is stronger than
   any power-law dissipation for this purpose. Recorded so the review's
   third route is closed rather than forgotten.
3. Not claimed: the no-cutoff Clay statement; uniformity of any bound as
   epsilon -> 0; that 0.156 nm is a measured quantity (it is derived).
4. The Gross-Pitaevskii superfluid of PAPER_679/681/1808/1809 is the
   AETHER [UA], not the physical fluid; its own regularity (quantum
   pressure) is a fourth mechanism the corpus has not applied to water
   and this paper does not import.
5. The mantissa echo q = 0.7092 vs rho_SCm 7.09 is a coincidence flag,
   not a chain.

## 7. Falsifiable consequences (added to the proof set's data fronts)

- Front 4 gains a SHAPE: DNS/experimental transfer above k_c should
  roll off as exp(-0.344 (k/k_c)^2) - Gaussian, not power-law - with
  the 1/e point at k = 1.70 k_c. A power-law tail in the phonon regime
  would falsify Form C's placement.
- Front 3 unchanged: the THz-bench dip at 1.25 THz, FWHM 0.235 THz
  (Form A), plus the 910-vs-896 width discriminator.
- Fronts 1-2 unchanged: the kill test and the pair-cap discrimination
  (full token / Kerr; envelope-saturation check from B278).

## 8. REVISION (same day, post-sweep) - the whole corpus, and what it added

The first draft of this paper rested on a title-filtered search (199 of
2,317 papers) and said so. The whole-corpus sweep was then run - every
one of the 2,307 papers outside the current arc, three grep patterns
(above-cutoff statements; damping/suppression laws with a functional
form; hyperviscosity/Leray/mollifier/cutoff vocabulary). It found
THREE statements the title filter had missed, and the paper is revised
against them rather than defended:

**(R1) PAPER_1383 L26 - the structural reading, canonized.**
"omega_SCm = 1.25 THz is the STRUCTURAL UV cutoff - modes above this
do not exist in the SCm vacuum." This is Form B in its hardest
version: not damped, absent. It is the corpus's own statement of
Theorem A's sharp filter, and it makes PAPER_2268's ruling a
consequence of a canonized paper rather than a standalone judgment.

**(R2) PAPER_106 L97-99 - a stated k-dependent law, with FREE
exponents.** In the vacuum-energy mode integral the corpus writes
`k_Q = E_Q/(hbar c)` (the UQFF momentum cutoff), `Gamma_damp(k) =
Gamma_0 (k/k_Q)^a` (momentum-dependent damping) and `F_UQFF(k) = 1/(1
+ (k/k_Q)^beta)` (suppression factor). Both a and beta are left
UNSPECIFIED in the paper (the "1.8 scaling exponent" at L183 belongs
to the cosmological expansion term, not to these). This is exactly the
growth law the Track-3 review said the corpus lacked - it exists, in a
cosmology paper, with its exponents open.

**(R3) PAPER_841 L65 - the hyperviscosity route, already hypothesized
and already self-graded.** "Large-scale F_LENR oscillations at
omega_LENR may act as a turbulence regularization mechanism, analogous
to HYPERVISCOSITY damping high-frequency modes. If F_LENR creates a
spectral gap above omega_LENR, turbulent cascades are cut off,
potentially ensuring smoothness. Feasibility: Speculative. No rigorous
proof." PAPER_831 L153 says the same in one line ("does not constitute
a formal proof"). The corpus proposed Lions' route and honestly
declined to claim it.

**What the three additions do to Theorem B - the 5/2 threshold, twice.**
Theorem B needs one property of the tail: ||grad rho_epsilon||_2 <
infinity (sec 4 step ii). For the PAPER_106 suppression factor as a
Fourier multiplier, rho-hat(k) ~ k^{-beta} at large k, and
||grad rho||_2^2 ~ int k^2 k^{-2 beta} k^2 dk converges iff
4 - 2 beta < -1, i.e. **beta > 5/2**. For the PAPER_106 damping rate
Gamma_0 (k/k_Q)^a acting as dissipation, Lions (1969) gives global
regularity iff the dissipation order satisfies **a >= 5/2** (the
(-Laplacian)^{5/4} threshold, 2 x 5/4). The SAME number gates both
routes - Theorem B's mollifier and the corpus's own hyperviscosity
hypothesis - which is a consistency the two papers could not have
arranged. The Gaussian tail of Form C (PAPER_1042) is the beta ->
infinity member of the PAPER_106 family and satisfies every condition
automatically; Theorem B as stated in sec 4 therefore stands
unchanged, and the sweep ADDS a second, corpus-native way to close
Track 3 (Lions on Gamma_damp) that becomes a theorem the moment a is
fixed at or above 5/2.

**Disposition of the three high-k readings after the sweep.** The
corpus carries all three, as Daniel's intuition said: (i) structural
nonexistence (PAPER_1383) - Theorem A; (ii) a growing power-law
damping Gamma_0 (k/k_Q)^a (PAPER_106) - Lions' theorem iff a >= 5/2;
(iii) a suppression/mollification of the transported field - the
Gaussian tail (PAPER_1042; Theorem B as stated) or the power-law
factor 1/(1 + (k/k_Q)^beta) (PAPER_106; Theorem B iff beta > 5/2).
They are not rivals: (i) is the sharp limit of (iii), and (ii) is an
independent second mechanism. Track 3 is closed on the Gaussian form
and CONDITIONALLY closed on the PAPER_106 forms.

**RULING REQUESTED (Daniel):** fix the PAPER_106 exponents a and beta,
or canonize the PAPER_1042 Gaussian tail as the high-k form for fluid
modes. If a >= 5/2 and beta > 5/2, both routes are theorems; if either
exponent is below 5/2, that route is closed negative and Theorem B
rests on the Gaussian form alone. Sec 2's number (0.156 nm) is
unaffected by the ruling; it belongs to the Gaussian form.

(Also swept and found consistent, not load-bearing: PAPER_1824's UV
cutoff via "26 F_TRZ-averaged phonon modes summing coherently";
PAPER_851's "off-resonance rapidly suppressed by Gaussian envelope"
(Form A); PAPER_585's Euler inviscid proof (a separate SCm-corpus
claim on the Euler system, not used here); thirty-three papers citing
Leray 1934 in bibliographies only. One further note: PAPER_106's k_Q =
E_Q/(hbar c) is the LIGHT-cone momentum of the carrier energy; the
fluid's own cutoff k_c = omega_SCm/c_s (PAPER_2267) is the sound-cone
one. The two differ by c/c_s; sec 2 uses the fluid's.)

## 8a. Coverage appendix (post-sweep)

Whole corpus: 2,317 files in whitepapers/; 2,307 swept (the 10 current-
arc papers 2263-2275 excluded as known); three patterns; hits: A = 1
(PAPER_102 L168), B = 4 (PAPER_106 L98, 1072 L19, 851 L65, 878 L73),
C = 62 lines across 50 files (33 of them the Leray 1934 bibliography
line). Read in full: PAPER_102, 106 (sec 2, 10), 1042, 1072, 1204,
1232, 1383, 1864, 1907, 205 (sec 3), 831 (sec 4.2), 841 (sec 1.1),
893, 898, 2263-2274; predecessor S300, PAPER_1182 LaTeX, session-259
audit, formal/UQFF/Millennium.lean. Still NOT read: predecessor
cfd_paper369_navierstokes.py, AetherSuperfluidDynamics.cpp,
FluidSolver.h, UQFF_SimultaneousProofEngine.py (code, not corpus; Rule
E study-only). The sweep ran through the file bridge into the cloud
sandbox because the Windows-side mount was down on the day of writing;
every file was transferred and grepped, none skipped.

## 9. Cross-references
Forms: PAPER_893/910/2269 (A), PAPER_1907/1072/102/1383 (B),
PAPER_1042/205/106 (C). Hyperviscosity hypothesis: PAPER_841, 831.
Placement: PAPER_102 sec 6, PAPER_154. Theorems: PAPER_2267
(Theorem A), PAPER_2268 (ruling), PAPER_2274 (spine audit), PAPER_2270
(proof set). Primitives: PAPER_1203 (beta_i), PAPER_1154 ([SSq]),
PAPER_2261 (c_s). Classical: Leray 1934 (regularized equations); the
Leray-alpha literature (Cheskidov-Holm-Olson-Titi 2005) for the modern
form. B280.
