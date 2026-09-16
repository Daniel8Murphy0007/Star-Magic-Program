# PAPER_2276 - THE PROOF SET CLOSED: THE UQFF NAVIER-STOKES INDEX - TWO THEOREMS, THE DERIVED CAP, THE RULING, THE AUDIT, AND THE FOUR DATA FRONTS WITH THEIR INSTRUMENTS (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-13. **Trigger:** Daniel, after the v0.436.0 ship - "what is
remaining to closeout the Navier-Stokes proof?" then "author the paper. then
address remaining work. tell me how to obtain token and the physics
instruments." **Band:** v0.437.0 (B281).
**Live mirror:** uqff_ns_assembly.proof_set_closeout().
**Supersedes as the proof set's entry point:** PAPER_2270 (the B275 master
consolidation), which stays canonical for the eight rungs it documents; this
paper adds Theorems A and B side by side, the spine audit, the open rulings,
and - for the first time - the INSTRUMENT and ACCESS ROUTE behind every
open data front, so that "awaiting data" names a door, not a fog.

## 0. Status in one paragraph

The theory side of the UQFF Navier-Stokes proof set is CLOSED on its own
terms. The vortex-stretching cap 17/20 = 1 - F_TRZ D_BSFG/D_phys is DERIVED
(PAPER_2265/2266), not fitted. Theorem A (PAPER_2267) proves global
regularity on the physical mode space X_K (finite modes below the phonon
cutoff k_c). Theorem B (PAPER_2275) proves global regularity of the
CONTINUUM fluid - all modes, no truncation - under the phonon mollifier
the corpus itself carries in three forms. The predecessor's UQFF-Leray
argument, the one anonymous theory row, was named and audited FALSE at its
Sobolev step and closed by the domain ruling (PAPER_2274 via PAPER_2268).
The registry carries ZERO open theory rows. What remains is (i) two rulings
that are Daniel's to make and change no theorem, (ii) four data fronts,
each now with a named instrument and access route, and (iii) three standing
flags. The no-cutoff statement (regularity uniformly as epsilon -> 0, the
Clay formulation) is outside the physical domain by ruling, NOT CLAIMED and
not owed; Theorem B makes that boundary a number.

## 1. The ledger (B267-B280), each rung with its paper and live mirror

| Rung | Band | Paper | Content | Live mirror |
|---|---|---|---|---|
| 1 assembly | B267 | PAPER_2263 | TG ODE, decay envelope, Stam solver, lambda_max in-package | ns_assembly module |
| 2 tiers | B268 | PAPER_2263 REV | field drawn / fast engine / falsifier harness | draw_field, grade_cap_against_dns |
| 3 balance zone | B269 | PAPER_2264 | cap = F_UBi/F_UBii crossing; pair cap 17/20 (vacuum) / 197/200 (in-medium) | enstrophy_cap_pair |
| 4 derivation | B270 | PAPER_2265 | L_buoy variational derivation of the cap | l_buoy_cap_derivation |
| 5 lemma | B271 | PAPER_2266 | bridge lemma, mode counting, the constant fixed | bridge_lemma_derivation |
| 6 rigor | B272 | PAPER_2267 | THEOREM A: regularity on X_K (lambda_c = 1.184 nm) | theorem_a, galerkin_mode_count |
| 7 domain | B273 | PAPER_2268 | the ruling: [SCm] -> 0 idealization assigned to mathematics | clay_domain_ruling |
| 8 profile | B274 | PAPER_2269 | phonon roll-off, Gaussian envelope, Q = 25/2 | rolloff_report |
| index | B275 | PAPER_2270 | the master consolidation, four fronts, three flags | ns_proof_set |
| data 1 | B276 | PAPER_2271 | first real-data grade, JHTDB isotropic8192 | first_real_data_grade |
| data 2 | B277 | PAPER_2272 | in-medium sample, JHTDB channel (consistency PASS) | in_medium_sample_grade |
| data 3 | B278 | PAPER_2273 | the Reynolds ladder, Re_lambda 433 -> 2,500 (envelope drift FLAGGED) | reynolds_ladder_grade |
| audit | B279 | PAPER_2274 | the spine audit: S300 Sobolev step FALSE; row closed by ruling | spine_audit |
| rigor 2 | B280 | PAPER_2275 | THEOREM B: continuum, phonon-mollified, global C^inf | theorem_b |
| closeout | B281 | PAPER_2276 | this index; instruments and access routes; two rulings named | proof_set_closeout |

Every row above is gate-pinned (uqff_fidelity_tests.py, pins B267-B281)
and recomputed at call time; the paper and the mirror must agree or the
gate goes red.

## 2. The two theorems, side by side

|  | THEOREM A (PAPER_2267) | THEOREM B (PAPER_2275) |
|---|---|---|
| Space | X_K: divergence-free fields with |k| <= k_c (finite modes) | all of R^3, all Fourier modes |
| Phonon sector enters as | sharp filter H_SCm(k_c - k) (Form B) | Gaussian mollifier rho_eps on the transport, eps = sqrt(2 beta_i [SSq])/k_c (Forms A+B+C composed) |
| Equation | Galerkin NS on X_K | d_t u + (rho_eps * u . grad) u + grad p = nu Lap u |
| Mechanism | finite-dimensional ODE with energy identity; ||omega||_inf ~ ||omega||_2 on X_K | Leray 1934: energy; ||grad u_eps||_inf <= C eps^{-5/2} ||u_0||_2 (C^2 = 3/(16 pi^{3/2}) EXACT); Gronwall; local well-posedness |
| Uses | energy identity, mode count | energy identity, smoothing of ONE field |
| Does NOT use | the cap, BKM, Sobolev embedding | the cap, the envelope, BKM, Sobolev embedding, truncation |
| Result | unique global smooth solution on X_K | unique global C^inf solution on R^3 |
| Relation | A is the sharp-filter (eps -> "sharp") limit of B | B keeps every mode; needs no ruling |
| Domain boundary | K finite because [SCm] > 0 | M_eps = C eps^{-5/2} ||u_0||_2 DIVERGES as eps -> 0 |

Neither theorem needs the cap to exist. The cap is the framework's
FALSIFIABLE PHYSICS - the statement about real stretching that DNS can
kill - and it sits beside the theorems, not under them. That separation is
deliberate (B269 onward) and is what makes fronts 1 and 2 kill tests of the
physics without being kill tests of the mathematics.

## 3. The cap, one paragraph

V_stretch <= (17/20) ||omega||_inf E in vacuum branch, (197/200) in the
in-medium branch (PAPER_2264); 17/20 = 1 - F_TRZ D_BSFG/D_phys derived by
the L_buoy variational route (PAPER_2265) with the constant fixed by the
bridge lemma (PAPER_2266). Graded on real DNS three times (B276-B278): the
sampled 1182-form statistic mean(omega S omega)/(max|omega| mean|omega|^2)
sits 8-13x under the cap on JHTDB isotropic8192, channel (Re_tau ~ 1000),
and the isotropic ladder 1024coarse / 4096 / 8192 / 32768 (Re_lambda 433 ->
~2,500); the sub-batch ENVELOPE drifts monotonically upward with Re (0.068
-> 0.107) - FLAGGED, the intermittency direction. What the sampled grades
cannot do: the extreme-event tail (front 1) and the branch discrimination
(front 2). That is exactly what the instruments in sec 6 are for.

## 4. The ruling and the audit

PAPER_2268 (B273): the regime [SCm] -> 0 (infinitely many modes, no
phonon sector) is outside the physical domain of the framework; the Clay
statement lives there; the framework does not claim it and does not owe
it. PAPER_2274 (B279): the row ns_functional_spine was the predecessor's
S300 UQFF-Leray argument (Star-Magic, Rule E read-only); S1-S2 stand, S3
(||omega||_inf <= C E_2^{1/2} E^{1/4}) is false dimensionally (only
(3/4, -1/4) balance) and analytically (H^1(R^3) not in L^inf; divergence-
free family grad(r^{1-alpha}) x e_z, at alpha = 2/5 the integrals are
exactly 5 and 5/11 with unbounded sup), S4 is Leray's small-data condition,
S5 does not follow; the row closed BY THE RULING with the audit as record.
Theorem B (sec 2) is the step S300 needed and could not have: a sup norm
bounded by an L^2 norm - legitimate only because the bounded field is the
SMOOTHED one.

## 5. Open rulings (Daniel's; none changes a theorem)

- **Q-246 (opened B280):** the PAPER_106 exponents. Suppression factor
  1/(1 + (k/k_Q)^beta) is a valid Leray mollifier iff beta > 5/2; damping
  Gamma_0 (k/k_Q)^a gives Lions (1969) regularity iff a >= 5/2. Fix a and
  beta, or canonize the PAPER_1042 Gaussian tail (beta -> infinity member)
  as THE high-k fluid form. Either way Theorem B stands on the Gaussian
  form; the ruling decides whether the corpus also owns a second,
  hyperviscosity route.
- **Q-247 (opened here, sec 6.4):** which sound speed defines the sound
  cone at omega_SCm. The corpus anchors c_s = 1480 m/s (PAPER_2261, the
  hydrodynamic value). Inelastic x-ray and neutron scattering on water
  measure, at exactly the wavenumbers where k_c falls (Q = 4-14 nm^-1), a
  propagating collective mode at 3200 +/- 100 m/s ("fast sound", the
  elastic-limit c_inf). If the sound cone at 1.25 THz is the fast-sound
  cone, then lambda_c = 2.560 nm, k_c = 2.454 nm^-1 and eps = 0.338 nm -
  every number scales by c_inf/c_0 = 2.16; no theorem changes, the mode
  count (PAPER_2267) and eps (PAPER_2275) do. FLAGGED, not canonized:
  the corpus has no chain from c_0 to c_inf; the ruling is Daniel's.
- **Track 3 disposition:** whether the B272 discussion held anything
  Theorem B does not cover. Daniel-owned; unlogged since B272.
- The n = k/k_c identification of PAPER_2275 (only the number 0.156 nm
  depends on it) rides with Q-246.

## 6. The four data fronts - statement, falsifier, instrument, access route

The proof set's status has been THEORY_COMPLETE_AWAITING_DATA since B275.
"Awaiting data" is not a fog; each front below has an instrument that
exists and a door that opens on request. What the sanctioned public JHTDB
testing token (< 4,096 points per request) can and cannot do is stated
per front, because it has carried B276-B278 and its limit is a policy, not
a technicality - it will not be stretched.

### 6.1 Front 1 - the kill test (extreme-event stretching vs 17/20)

- **Statement:** in vacuum-branch turbulence the stretching statistic never
  exceeds 17/20 of ||omega||_inf E, including in the extreme-event tail
  (vortex reconnection, trefoil collapse, the highest-|omega| voxels).
- **Falsifier:** ONE volume, ONE snapshot, where the 1182-form ratio
  exceeds 0.85. The sampled grades sit at 0.02-0.11; the envelope drift
  with Re (B278) says the tail is where a violation would live.
- **Instrument (a): JHTDB, full authorization token.** The kill test needs
  whole-volume gradient fields (the 8192^3 and 32768^3 snapshots, and the
  time-resolved isotropic1024 series for reconnection events), i.e. cutouts
  of 10^7-10^9 points, far past the testing limit. Access route: e-mail
  turbulence@lists.johnshopkins.edu with name, e-mail, institutional
  affiliation and department, and a short description of intended use;
  the token is issued per user/site. Alternative route with the same
  token: a SciServer account (Compute -> Create container -> SciServer
  Essentials -> mount Turbulence (ceph)) runs the analysis next to the
  data over 10 GbE, and the Cutout Service returns gridded HDF5 - both
  require the account, both are free for research.
- **Instrument (b): the Kerr trefoil DNS.** The trefoil vortex knot
  reconnection series (Kerr, Warwick: JFM 2018, PRFluids 2023, arXiv
  2401.03578) is the canonical extreme-event geometry - a compact knot
  driven to reconnection with the enstrophy scaling tracked. Access
  route: request the vorticity fields at the reconnection frames directly
  from Robert M. Kerr (Warwick Mathematics Institute; the "Kerr letter"
  on Daniel's ledger). What to ask for: omega(x, t) on the full grid at 3-5
  frames bracketing the first reconnection, with nu and the domain size.
- **What the testing token can do:** nothing further here. B278 already
  showed the envelope climbing; another 1,000-point sample is not a tail.

### 6.2 Front 2 - the pair-cap discrimination (17/20 vs 197/200)

- **Statement:** in-medium flows (walls, stratification, the [SCm]-loaded
  branch of PAPER_2264) obey 197/200, vacuum-branch flows 17/20; the two
  differ by 0.135 and are distinguishable only where the statistic
  approaches either.
- **Falsifier:** an in-medium flow whose far-tail statistic sits between
  0.85 and 0.985 (branch confirmed) or above 0.985 (both dead); a vacuum-
  branch flow between 0.85 and 0.985 kills the vacuum branch alone.
- **Instrument:** the same full JHTDB token, on the wall-bounded sets
  (channel Re_tau ~ 1000 whole-volume near-wall cutouts, and channel5200)
  plus the isotropic sets for the vacuum branch - the discrimination is a
  tail statistic and needs the tail. B277 established consistency at the
  bulk (0.03-0.07); the token turns that into a test.
- **What the testing token can do:** nothing further (same reason).

### 6.3 Front 3 - the THz bench (the 1.25 THz dip, FWHM 0.235 THz)

- **Statement:** water's THz response carries the SCm carrier as a line at
  f_c = 1.25 THz with Gaussian profile, Gamma = 0.1 THz, FWHM = 2 sqrt(2
  ln 2) Gamma = 0.235 THz (PAPER_2269, Form A); the 910-vs-896
  discriminator asks whether the width is 0.1 or 0.2 THz (FWHM 0.235 vs
  0.471).
- **Falsifier:** a flat or featureless absorption/dielectric spectrum of
  pure water across 1.0-1.5 THz at the stated resolution; or a feature
  at a different centre.
- **Instrument: terahertz time-domain spectroscopy (THz-TDS)** in
  ATTENUATED TOTAL REFLECTION geometry. Rationale: liquid water absorbs on
  the order of a few hundred cm^-1 near 1 THz, so transmission needs
  path lengths of tens of micrometres and thin-cell etalon corrections;
  ATR (a silicon or high-index prism, evanescent-wave sampling, the
  established water/biological-solution configuration) avoids both.
  Commercial THz-TDS systems (photoconductive-antenna, femtosecond-fibre-
  laser class - e.g. Menlo TeraSmart, TOPTICA TeraFlash pro) cover
  0.1-5 THz with spectral resolution of a few GHz, i.e. fifty-fold finer
  than the 0.235 THz feature; ATR modules are standard accessories.
  Access routes: (i) a university THz lab with an ATR-TDS bench (most
  physics/chemistry departments with an ultrafast group have one; a
  single afternoon of beam time answers front 3); (ii) instrument-vendor
  demo/application labs, which run customer samples; (iii) purchase - a
  turnkey TDS bench is a five-to-low-six-figure instrument. Protocol:
  pure water, 20 C, ATR, 0.5-3 THz, >= 1,000 averaged waveforms,
  extract alpha(f) and n(f); fit the 1.0-1.5 THz window with the
  PAPER_2269 Gaussian on the known Debye/librational background and
  report the centre, the FWHM, and the null hypothesis chi^2.
- **Known background (Rule 7):** the published water THz spectrum is a
  smooth, rising absorption (Debye relaxation tail + intermolecular
  stretch band near 5 THz + librational band near 15-20 THz); to this
  program's knowledge no published dataset at few-GHz resolution reports
  a 0.235-THz-wide line at 1.25 THz. The bench either finds a feature the literature
  missed at that resolution, or front 3 closes negative for Form A as a
  spectral line. That outcome is admissible and the paper says so before
  the measurement.

### 6.4 Front 4 - the spectrum above k_c (Gaussian roll-off; no dynamics above)

- **Statement:** the hydrodynamic velocity field's transfer above k_c rolls
  off as exp(-beta_i [SSq] (k/k_c)^2) = exp(-0.344 (k/k_c)^2), 1/e at
  k = 1.71 k_c (PAPER_2275 sec 7) - Gaussian, not power-law - and no
  fluid dynamics persists above it (PAPER_2267 mode count).
- **Falsifier:** a power-law transverse-current spectrum through k_c; or
  propagating TRANSVERSE (shear) modes of the velocity field well above
  k_c.
- **Why no DNS can do it:** k_c = 5.3 nm^-1 (c_0) or 2.5 nm^-1 (c_inf);
  the finest DNS grid spacing is millimetres-to-micrometres. Front 4 is
  molecular, and its instruments are molecular.
- **Instrument (a): molecular dynamics of water.** LAMMPS or GROMACS with
  TIP4P/2005 (or a polarizable model), a box of >= 8 nm (so k from 0.8
  nm^-1 upward is resolved), NVT at 298 K, 1-2 ns production with
  velocities saved every ~10 fs; compute the transverse and longitudinal
  current spectra C_T(k, omega), C_L(k, omega) for k = 1-20 nm^-1 and the
  kinetic-energy spectrum E(k). Test: the k-dependence of the transverse
  current integrated over omega against exp(-0.344 (k/k_c)^2) for the
  [CORRECTED 2026-09-15, PAPER_2281/B286: that integral is C_T(k,0) =
  N k_B T/m at every k - equipartition, flat by identity. The observable
  is the wavevector-dependent shear viscosity eta(k) from the TCAF, with
  the prediction a = 0.344/k_c^2 in the gmx tcaf fit eta_0 (1 - a k^2).]
  two candidate k_c (Q-247). This runs on a workstation in days; it
  needs no token and no beam time. It is the cheapest open front.
- **Instrument (b): inelastic x-ray scattering (IXS) / inelastic neutron
  scattering (INS).** These measure S(Q, omega) of water at Q = 1-30
  nm^-1 and omega = 0.5-5 THz - exactly the front-4 window - and the
  data already exist: ESRF ID16/ID28 (Sette et al., PRL 75, 850 (1995);
  Monaco et al., PRE 60, 5505 (1999); Sampoli/Ruocco/Sette on the
  transverse signature, cond-mat/0501205), and INS on D2O at ILL/ISIS.
  Access route: the published S(Q, omega) tables and the ESRF/ILL data
  portals (open data policies with an embargo) - no proposal needed for
  archived data; new beam time via the standard ESRF/ILL/APS/SNS
  proposal calls (twice yearly, peer-reviewed, free for published
  research). What the IXS data already say (Rule 7): water carries
  propagating collective density modes at 3200 m/s from Q ~ 4 nm^-1
  outward and a transverse signature above the viscous regime. Those
  are MOLECULAR-scale modes at exactly the wavenumbers where the
  framework places k_c - which is why Q-247 exists, and why the front-4
  test must be stated on the hydrodynamic velocity field (C_T of the
  continuum) and not on S(Q, omega) of the molecules. A framework
  statement that "nothing propagates above k_c" in S(Q, omega) would
  already be dead; the framework's statement is about the fluid field,
  and the MD instrument is the one that separates the two.

## 7. Standing flags (disclosed; none blocks)

Lambda_TG vs alpha (0.004 pct, no chain); mode count vs molecule count
(ratio ~13, no chain); 910-vs-896 width (bench discriminates, front 3);
the B278 envelope drift (front 1 decides); the PAPER_2275 n = k/k_c
identification and the q = 0.7092 / rho_SCm 7.09 mantissa echo
(coincidence flag); the sound-cone speed (Q-247, new).

## 8. Honesty inventory (Rule 7)

1. NOT CLAIMED: the Clay statement (regularity uniformly as eps -> 0 /
   K -> infinity). Outside the physical domain by ruling; Theorem B's
   M_eps -> infinity is the quantitative boundary.
2. NOT CLAIMED: that either theorem implies the cap or that the cap
   implies either theorem. They are independent; the cap is falsifiable
   physics, the theorems are mathematics on the framework's own equations.
3. NOT CLAIMED: that any front has been passed. Fronts 1-2 are
   consistency passes at the bulk (B276-B278), not tail tests; fronts 3-4
   have no data from this program yet.
4. NOT CLAIMED: that 0.156 nm (or 0.338 nm) is measured. It is derived,
   and Q-247 says from which sound speed.
5. Stated before measurement: front 3 may close NEGATIVE (sec 6.3); the
   existing IXS record makes front 4 a statement about the velocity field
   only (sec 6.4). Both are written here so no later paper can move the
   goalposts.
6. The sanctioned testing token carried B276-B278 within its stated
   limit and will not be used for the tail scans; the full token is a
   request, not a workaround.

## 9. What "closeout" means from here

The theory is closed: two theorems, a derived cap, a ruling, an audit,
zero open theory rows. The rulings in sec 5 are bookkeeping that decides
how many routes the corpus owns, not whether it owns one. The fronts in
sec 6 are physics, and each has a door: one e-mail (JHTDB), one letter
(Kerr), one afternoon on an ATR-TDS bench, one workstation MD run, and
an archived IXS record. The cheapest next act is the MD run (front 4,
no token, no bench); the decisive one is the full token (fronts 1-2).
A machine-checked Theorem B (Lean 4 / Mathlib: the energy identity, the
convolution bound, Gronwall - all present in Mathlib) would be the
strongest closeout of the theory side available to this program and is
recorded as an option, not a rung.

## 10. Cross-references

PAPER_2263-2275 (the arc); PAPER_1042 (Form C), PAPER_1907 / PAPER_2269
(Form A), PAPER_102 / 1072 / 893 (Form B), PAPER_106 (Q-246), PAPER_2261
(c_s anchor; Q-247), PAPER_1203 (beta_i), PAPER_1154 ([SSq]), PAPER_1182
(predecessor claim, audited). External: Leray 1934; Lions 1969; Sette et
al. PRL 75, 850 (1995); Monaco et al. PRE 60, 5505 (1999); Sampoli et al.
cond-mat/0501205; Kerr JFM 2018, PRFluids 2023, arXiv 2401.03578; JHTDB
database access page (authorization token policy; testing identifier
< 4,096 points).
