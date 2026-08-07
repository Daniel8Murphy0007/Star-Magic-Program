# UNIFIED_REGISTRY_FALSIFIABILITY.md — R4 per-primitive break report

**Provenance — INHERITED FROZEN REFERENCE (predecessor Star-Magic R0–R5,
PAPER_2130).** Per-primitive break analysis over the 9-primitive → 73-constant
derivation registry. **Question answered:** *if primitive X were revised, what
breaks?* This is a frozen reference from the predecessor program; it does not
describe this repo's paper-wiring campaign (`UNIFIED_REGISTRY.csv`) and is not
regenerated from it.

| Primitive | Derived constants dependent | Registry rows touched | Known canonical invariants | Gate exposure |
|---|:-:|:-:|:-:|---|
| A_5 | 0 (-) | 23 | 0 | magic-number EXACT pins |
| D_BSFG | 1 (HBAR_UQFF_S629) | 41 | 0 | canonical-value pins |
| D_crit | 3 (D_BSFG, G_UQFF, C_UQFF_DERIVED) | 43 | 0 | magic-number EXACT pins |
| D_phys | 4 (K_MEX, K_B_UQFF, HBAR_UQFF_S629, B_CRIT) | 97 | 0 | magic-number EXACT pins |
| F_TRZ | 6 (KAPPA, MU_0, K_B_UQFF, HBAR_UQFF_S629, H0_GRID, LAMBDA_SIMPLE) | 112 | 61 | U_i=2.75e-7 pin + 61-site (1+F_TRZ) family |
| K_MEX | 0 (-) | 6 | 0 | canonical-value pins |
| N_CH | 0 (-) | 16 | 0 | magic-number EXACT pins |
| Phi_res | 5 (K_MEX, K_SPRING, G_UQFF, C_UQFF_DERIVED, K_B_UQFF) | 7 | 0 | canonical-value pins |
| SO_5 | 9 (D_BSFG, F_TRZ, K_MEX, KAPPA, RHO_UA, LAMBDA_VAC, K_SPRING, LAMBDA_SIMPLE, B_CRIT) | 212 | 61 | U_i=2.75e-7 pin + 61-site (1+F_TRZ) family |
| SSq | 3 (G_UQFF, K_B_UQFF, HBAR_UQFF_S629) | 16 | 0 | canonical-value pins |
| S_26 | 0 (-) | 2 | 0 | canonical-value pins |
| beta_i | 0 (-) | 20 | 0 | canonical-value pins |
| kappa | 0 (-) | 6 | 0 | canonical-value pins |
| omega_SCm | 2 (K_SPRING, T_SCM_K) | 3 | 0 | canonical-value pins |
| rho_SCm | 2 (RHO_UA, LAMBDA_VAC) | 5 | 0 | canonical-value pins |

## Route-paper citation leverage (constant -> canonical paper -> citing whitepapers)

| Constant | Canonical route | Citing files |
|---|---|:-:|
| T_SCM_K | PAPER_1072 | 799 |
| K_SPRING | PAPER_1203 | 223 |
| LAMBDA_SIMPLE | PAPER_1156 | 179 |
| D_BSFG | PAPER_1521 | 82 |
| K_MEX | PAPER_1522 | 66 |
| G_UQFF | PAPER_593 | 32 |
| K_B_UQFF | PAPER_1209EE | 30 |
| H0_GRID | PAPER_2093 | 19 |
| C_UQFF_DERIVED | PAPER_592 | 18 |
| HBAR_UQFF_S629 | PAPER_590 | 10 |
| KAPPA | PAPER_2112 | 5 |
| MU_0 | PAPER_2108 | 5 |
| B_CRIT | PAPER_2126 | 4 |
| LAMBDA_VAC | PAPER_2120 | 3 |

## Headline

Total graph edges: 658. Every primitive participates in multiply-pinned
identities; a single-primitive revision propagates through the derived constants,
the registry rows above, the (1+F_TRZ) 61-site invariant family, and the
3,186-assertion fidelity gate simultaneously. Over-determination is the
falsifiability mechanism: wrong values cannot hide (see PAPER_2119/2126/2128).

- **PAPER_001** (GW170817): LIGO O5 ringdown spectral offset R_21/R_22 = 0.144 (PAPER_1175) constrains the 66.7% strain reduction (D_total = 1 - D_GW_erosion = 1/3). Phonon peak reduction 47% (h_UQFF = h_GR*(1-0.47*Phi/S_26)) falsifiable at O5 for BNS < 40 Mpc.

- **PAPER_002** (GW190425): UQFF SNR deficit 72% (SNR_UQFF=3.6 vs obs 12.9) and mass-gap m1=2.52 Msun classification (51% BH) falsifiable at O5; hyper-magnetar B>1e15 G -> complete SCm suppression -> no kilonova (consistent with GW190425). Q-001: F_UQFF=0.5297=1-0.47 phonon route, not the 0.333 damping chain.

- **PAPER_003** (GW150914): 3x apparent-distance bias (D_app=D_true/0.333) systematically lowers GW-inferred H0 - falsifiable via EM-counterpart host distances; 0.126 rad phase-lag residuals in matched filters (O4/O5). Q-004: stated phase-lag formula kappa*D*f*SSq gives 17.53, not 0.126.

- **PAPER_004** (GW170817 chirp): phase-space distinguishability - UQFF chirp lags GR templates, detectable at Einstein Telescope; M_chirp bias >0.01 Msun for D_L<40 Mpc. Q-005: h_UQFF,peak stated 9.4332e-23 vs 0.333*2.8051e-22=9.341e-23 (~1% slip).

- **PAPER_005** (BBH energy retention): 99% mass retention (0.65 vs 0.80 Msun radiated), 23% longer merger timescale - falsifiable via ringdown remnant-mass inference. Q-006: sec2 F_combined=0.903 (P=F^2) inconsistent with 0.81 used throughout.

- **PAPER_006** (GW170817 multi-messenger): detection volume shrinks 27x (1/0.333^3) - implicit O4/O5 BNS-rate prediction; amplitude-only damping preserves |dc/c|<3e-15 (GRB 170817A delay). EM sector unmodified.

## PAPER_007 — Tidal Deformability BNS
- **Falsifier:** measured Lambda_1.4 > 800 (stiff EOS) contradicts UQFF SCm-suppressed tidal response.
- **Discriminator:** any GW-mass-gap object (2.5-3 Msun) with Lambda > 0 falsifies NS/BH Lambda_NS~16 vs Lambda_BH=0.
- **SCm hook:** B-field suppression f_SCm(B)=1-exp[-(B_crit/B)] predicts reduced Lambda for magnetar-class B; null suppression at magnetar fields falsifies Cooper-pair screening.

## PAPER_008 — Waveform Phase Evolution & Template Mismatch
- **Falsifier:** GR templates matching GW170817 with <1% residual phase over 100s inspiral falsify UQFF dphi=2310.8 rad accumulated lag.
- **Discriminator:** tau_UQFF/tau_GR = 1/D^2 = 9x inspiral-time extension; measured chirp duration consistent with pure GR falsifies D^2 power scaling.

## PAPER_008b — Full Inspiral Waveform GW170817
- **Falsifier:** peak strain ratio h_GR/h_UQFF measurably != 3.0 across 23-300 Hz falsifies D=0.333 combined damping.
- **Discriminator:** 367.8 accumulated phase-lag cycles over 100s in-band; GR-consistent cycle count falsifies vacuum damping onset.

## PAPER_009 — 4-Mechanism Damping Decomposition
- **Falsifier:** BNS/BBH damping ratio measurably != 2.4 falsifies String-sector activation asymmetry (matter present -> stronger coupling).
- **Discriminator:** D_Aether becomes significant only r>c/kappa~17 Gpc (beyond observable universe); any sub-Gpc aether damping falsifies exp(-kappa r/c).

## PAPER_009b — Aether/String/TRZ/SCm Decomposition GW150914
- **Falsifier:** GR-template distance inference matching independent EM/host-galaxy distance (not 3x biased) falsifies D=0.333 strain suppression.
- **Discriminator:** SNR 24(GR)->8.0(UQFF) near threshold; phase lag 0.126 rad + 1% amplitude ripple are direct waveform tests.

## PAPER_010 — Post-Merger Oscillations & Remnant Mass
- **Falsifier:** 3G-detector post-merger peak matching GR 2.5 kHz (no 125 Hz downshift) falsifies UQFF QNM coherence correction.
- **Discriminator:** ringdown decay 29% faster (10ms->7ms) + 15% extra radiated energy -> lighter remnant; GR-consistent ringdown falsifies quantum dissipation channel.

## PAPER_001 — COMPLETE compile (Kozima-LENR + cosmogenesis added)
- **Kozima K.1-K.6 falsifier:** SCm-modulated neutron cross-section sigma_n^SCm peaking off omega_SCm=1.25 THz falsifies phonon-resonant LENR coupling.
- **Cosmogenesis falsifier:** NS-sector E-L EOM del^2 phi-(4piG rho/c^2)phi+Omega d_t phi=0 must hold at equilibrium; nonzero residual at r_hz falsifies the linkage chain.

## PAPER_010b-015 batch (complete-compile)
- **PAPER_011 (SGWB):** measured Omega_GW consistent with pure GR (no D^2=0.111 BNS suppression) falsifies energy~h^2 scaling.
- **PAPER_012 (eccentric):** LIGO-band residual eccentricity < 1e-4 (not 0.003) falsifies 1/D^2 circularization extension.
- **PAPER_013 (magnetar):** braking index n=3 (not 1.5-2.0) across magnetars falsifies D_SCm^2 spin-down suppression.
- **PAPER_014 (PBH):** PBH abundance matching GR delta_c=0.45 without SCm mass-function modifier falsifies UQFF formation channel.
- **PAPER_015 (GW cosmology):** standard-siren H0 = local H0 (no 1.07 bias) falsifies frequency-dependent propagation damping.
- **b-papers 010b-014b:** GW150914 damping!=0.6691, LISA/EMRI f_ISCO deviations from c^3/(6^1.5 pi G M(1+z)) falsify respective closures.

## PAPER_015b-023 batch (complete-compile)
- PAPER_016: CHSH S>2sqrt2 or no energy-dependent decoherence falsifies damping-mediated entanglement decay.
- PAPER_017: standard-siren phase lag != 2pi F_TRZ=0.628 rad falsifies F_combined=0.622 decomposition.
- PAPER_018: LISA noise with no n*f_U harmonic comb / no F_TRZ dip falsifies aether noise spectrum.
- PAPER_019: PTA amplitude without sub-uHz TRZ resonance inversion (D>1) falsifies A_UQFF=1.60*A_GR.
- PAPER_020: UHECR with no Z^(1/3) drag / no 8e19 eV TRZ break falsifies aether transport.
- PAPER_021: sigma_8 with no rho_TRZ=SSq^2 f_TRZ rho_crit suppression falsifies lensing correction.
- PAPER_022: D_String != 1-SSq^2 N_eff, or no 11.6 TeV KK mode at FCC-hh, falsifies compactification.
- PAPER_023: tau g-2 Delta_a != +3.42e-6, or KK loop != (m^2/8pi M_KK^2)(2/3)(1/SSq^2), falsifies BSM closure.

## PAPER_015b-023 REDO — paper-specific §B DVP ladder
- Each paper carries its OWN §B.2 dipole-vortex prime (resonant p>26): 015b=53, 016/016b=59, 017=61, 018=67,
  019=71, 020=73, 021=79, 022=83, 023=89 (n_channel 16/26..24/26). Generic PAPER_001 value (p=3) was a corner-cut;
  now corrected. A measured vacuum-topology resonance at a different prime index falsifies the per-system §B assignment.

## PAPER_024-030 batch (BSM, complete-compile)
- PAPER_024: tau EDM != 1.84e-20 e.cm, or phi_CP != SSq*pi, falsifies DPM CP-violation.
- PAPER_025: DM direct-detection above sigma_SI 3.2e-52 cm^2, or ACP mass != kappa*hbar, falsifies dual candidate.
- PAPER_026: sterile M_s2 != SSq*M_W=45.81 GeV falsifies vacuum mass-generation ladder.
- PAPER_027: LFV BR != exp(-pi|t_n|) temporal-reversal form falsifies DPM suppression.
- PAPER_028: |V_cb| decoupled from Higgs coupling falsifies CKM-as-vacuum-density link.
- PAPER_029: cosmic budget f_SM != SSq^n falsifies 100%-theory partition.
- PAPER_030: dark-mediator BR without cos^2(pi t_n) suppression falsifies mediator channel.
- §B DVP ladder 024-030: 97/101/101/103/103/103/107/109/113/2 (paper-specific, gate-guarded).

## PAPER_031-040 batch (BSM flavor/EW/Higgs + F_UBii buoyancy)
- 031: R(D)!=R_SM/(1-(m_tau/m_b)^2 SSq) falsifies flavor-anomaly resolution.
- 032: no extended scalar (VLQ mass) / tan_beta!=1/sqrt(k_eta) falsifies BSM scalar sector.
- 033: m_W shift opposite CDF direction, or delta_T!=E_react SSq/alpha, falsifies oblique corrections.
- 034: kappa_t outside [0.922,0.974] at FCC-hh falsifies Level-18 field.
- 035: Higgs A_CP not cos(pi t_n) form falsifies CP phase prediction.
- 036-040: F_UBii=F_U-F_Bi-F_i sigma^3 scaling; cluster force not ~sigma^3 r_h falsifies buoyancy variant family.
- §B DVP ladder 031-040: 3,5,7,11,13,17,19,23,29,31 (paper-specific, gate-guarded).

## PAPER_041-050 batch (26-level framework / DPM manifold / nuclear / vacuum)
- 042: 26-layer gravity superposition not spanning 61 orders (Planck->Hubble) falsifies compressed-gravity.
- 043: energy hierarchy != 10^(n-20) J falsifies 26-level polynomial spine.
- 044: 26-center radii != 10^(-35+i/3) (r_1!=Planck) falsifies pre-BB manifold.
- 045: matter-state transition energies not ordered rho_L1(2n+1) falsifies phase quartet.
- 046/047: nuclear coupling != 1000(A/56)^(1/3), or Fe-56 not the g=1000 iron peak, falsifies core triad.
- 048: Ug4 BH pressure != M rho_vac/(d^2 E_LEP) falsifies vacuum-pressure form.
- 049: three-component vacuum sum not = observed residual Lambda falsifies Yin-Yang cancellation.
- §B DVP ladder 041-050: 37,41,43,47,53,59,61,67,71,73 (paper-specific, gate-guarded).

## PAPER_051-060 batch (cross-validation / astrophysical models / alpha-BEC)
- 051/052: UQFF cross-validation mean alignment < 90% against 2024/2025 arXiv falsifies the prediction suite.
- 053-058: compression hierarchy 1x/2x/10x (standard/wind/merger) not matched by shock velocities falsifies taxonomy.
- 055: major-merger compression != (1+overlap)^2.3 falsifies halo-overlap spike.
- 056: PN wind v != v_esc*sqrt(Ug2/g) falsifies radiation-pressure wind.
- 059: alpha-BEC P != 0.10+0.85(E*-1)/8 falsifies formation probability.
- 060: alpha multiplicity != 1/(exp(dE/kT)-1) with single T_BEC=5 MeV falsifies BE occupancy.
- §B DVP ladder 051-060: 79,83,89,97,101,103,107,109,113,2 (paper-specific, gate-guarded).

## PAPER_061-070 batch (nuclear-BEC / LENR / ensemble / operational modes / astro)
- 062: W-L heavy-electron m*<2.53 m_e (no e+p->n) falsifies neutron-catalysis; omega_LENR!=2pi*1.25THz falsifies SCm-phonon identity.
- 064: g_UQFF weights != {KAPPA, SSq, [UA], H_SCm} falsifies 4-mode superposition.
- 066/069: magnetar LENR term != (omega_SCm/omega_0)^2 falsifies resonance coupling.
- 067: AGN Ug4 not k4 rho_SCm(M_BH/d) falsifies vacuum concentration.
- 070: destroyed-planet ripping radius != (GM/omega^2)^(1/3) falsifies Kepler debris-disk chain.
- §B DVP ladder 061-070: 3,5,7,11,13,17,19,23,29,31 (paper-specific, gate-guarded).

## PAPER_071-080 batch (superflare / reactor / database cross-validation)
- 071: solar g != G M/R^2=274 falsifies self-consistency landmark; Ug1 magnetic != g mu0 B^2/8pi falsifies form.
- 072: red-dwarf reactor f_TRZ != 0.10 or COP != (1+f_TRZ)/(1-Omega_g)+d_SCm falsifies TRZ primitive.
- 073/074: astrometric correction != 1+SSq*coeff falsifies Gaia/NED cross-validation.
- 075/079: SC-mode enhancement != 1+[SCm]=1.99 falsifies eta_Edd / B_field multiplier.
- 078: H0 tension correction H0*[UA]*0.5=0.0034 (honest null) - UQFF does NOT resolve tension via [UA].
- §B DVP ladder 071-080: 37,41,43,47,53,59,61,67,71,73 (paper-specific, gate-guarded).


---

## LIVE CAMPAIGN FALSIFIABLE PREDICTIONS — v0.345.0 (this repo)

Mined this ship as individually-callable, primitive-sourced functions — each falsifiable against observation:
- **H_0 = A_5 + SO_5 = 70 km/s/Mpc** (PAPER_1573): next-gen JWST/Roman/LSST central value lands at/near 70; falsified if outside 68.5-71.5.
- **m_p/m_e = A_5(D_crit+D_phys)+N_ch·D_phys = 1836** (PAPER_1209): integer identity; any precision drift from 1836.15 stresses the primitive lattice.
- **Ω_b/Ω_DM = SSq³ = 0.185** (PAPER_118): falsified if the ratio departs measurably from 0.185.
- **MOND a₀ = c·H₀/6** (PAPER_210): ties the MOND scale to H_0; falsified if a₀ and H_0 decouple.
- **k_UA = F_TRZ⁴ = 1e-4 EXACT** (PAPER_210): deep-MOND interpolation coupling; falsified by any non-1e-4 measurement.


## v0.346.0 falsifiable additions
- **eta/s = 1/(4pi) = 0.0796** (PAPER_1008): QGP shear-viscosity KSS bound; falsified if measured eta/s drops below 1/4pi.
- **CHSH = 2.75 at GeV** (PAPER_016): falsified if high-energy Bell tests cap at the classical bound 2.
- **6.25 THz = 5*f_SCm** (PAPER_100): 5th-harmonic phonon line; falsified if no SO_5-fold resonance appears at 6.25 THz.
- **T_Osc = tau/F_TRZ = 54.8 yr** (PAPER_154): SCm oscillation period; falsified by a different measured NS-jet oscillation period.


## v0.347.0 landmark falsifiable additions
- **mu_0 = 4 pi F_TRZ^7** (PAPER_2108): pre-2019-SI mu_0 was defined 4pi e-7 exactly; UQFF derives the same from F_TRZ^7 — falsified if post-redefinition measured mu_0 drifts from 4pi F_TRZ^7 beyond alpha-measurement uncertainty.
- **k_B primitive composition** (PAPER_2129): 0.0011%% residual vs SI-exact; falsified if a tighter primitive route cannot close the residual.
- **alpha_s(M_Z) = F_TRZ K_MEX SSq = 0.11875** (PAPER_2131): falsified if world-average alpha_s departs 0.014%% band.
- **B_crit = 4.4e13 T** (PAPER_2126): Schwinger critical field integer identity; magnetar B-field ceiling test.
- **Omega_m = 0.3 EXACT** (PAPER_1956): falsified if CMB+LSS converge away from 0.300.


## v0.348.0 landmark falsifiable additions
- **tau_n = 879.31 s** (PAPER_1926): within current beam/bottle measurements (879.4 +/- 0.6); falsified if the
  beam-bottle discrepancy resolves away from 879.31.
- **Phi_res = 21/25 EXACT** (PAPER_2134): Phi_res is derived, not free; any fit requiring Phi != 0.84 falsifies.
- **Plasmoid timings** (PAPER_2096): reactor camera/photo/batch observables = integer identities; falsified by
  recalibrated hardware measurements departing 100/3 fps, 0.33 s, 0.45 s.
- **dg = 2.6e20 m** (PAPER_2139): Sgr A* distance identity vs VLBI parallax (~2.55e20 m); watch the residual.


## v0.349.0 deep-mine falsifiable additions
- **Object primitive-locks (115)**: each bb_* is a falsifiable claim that the object observable equals a pure
  primitive power (e.g. B(Crab) = SO_5^-8 T); improved measurements departing the lock falsify per-object.
- **Material landmarks (191)**: engineering/biology constants as primitive chains (aluminum 2700 EXACT,
  blood pH 7.4 EXACT, DNA 10.5); any revised standard value breaking the chain falsifies that identity.
- **Sgr A* JWST 2025 flare = 1/1800 Hz** (pi_ir_flare_frequency): live JWST cadence data tests the triple-integer.


## v0.350.0 falsifiable additions
- **T_UQFF/T_H = 1 - F_TRZ^2 = 0.99** (CP1): Hawking-temperature deficit of exactly 1%; testable against analogue-gravity Hawking experiments.
- **n_generations = D_phys - 1 = 3** (PAPER_1220): a 4th fermion generation at any energy falsifies the identity.
- **exp(-SSq n/26) ladder** (CP4): 26-state suppression; NOMAD n=13 sqrt-identity + ALICE n=18 multiplicity test it at colliders.
- **Saturn ring lifetime 110.9 Myr** (QCalc ODE): Cassini-era erosion-rate extrapolations test the closed lifetime.


## v0.351.0 falsifiable additions (scrape-complete)
- **Chandrasekhar = F_TRZ D_phys^2 (1-F_TRZ) = 1.44 Msun EXACT**: any WD-mass revision off 1.44 falsifies the triple-primitive identity.
- **ISCO = D_BSFG = 6 r_g**: EHT/X-ray ISCO measurements departing 6 r_g (Schwarzschild) falsify.
- **top Yukawa y_t = 1 - F_TRZ^2 = 0.99**: PDG 0.9936; tighter m_t/v measurements test the 0.36% band.
- **alpha_s = F_TRZ K_Mex SSq - F_TRZ^3 Phi_res = 0.11791**: 0.008% vs world average; lattice tightening tests it.


## v0.352.0 falsifiable additions
- **SgrA* Newtonian-decayed** (PAPER_110): stellar-orbit precession around Sgr A* must be fully explained by
  Ug4+MUGE; any residual requiring an undecayed Newtonian core falsifies the kappa-decay.
- **DPM i^5 layer ladder** (CoAnQi): layer-resolved DPM energies must scale as i^5; spectroscopy of layered
  systems departing i^5 falsifies.
- **SSq = 0.755^2** (PAPER_094): if 0.755 proves non-decomposable, SSq remains primitive; if it decomposes,
  the 9-primitive count drops again.


## v0.353.0 falsifiable additions
- **kappa dual-route** (PAPER_125/2112): observational 0.35/700 must remain consistent with (SO_5/2)F_TRZ^4;
  any blazar-population decay refit departing 5e-4/day breaks the convergence.
- **Hoyle via SSq sum** (PAPER_132): the 7.654 MeV state (minus 1 MeV offset) as E_0*2.080+0.414; improved
  alpha-BEC calculations test the geometric-sum route.
- **40/60 split** (PAPER_143): hydrogen ground-state decompositions must apportion 40% MUGE / 60% quantum.
- **Density-ladder activation** (PAPER_137): Ug terms switch at rho thresholds 10^(n-13); astrophysical systems
  crossing thresholds should show term onset/offset.


## v0.356.0 falsifiable additions
- **0.622 = sqrt(Omega_DM/Omega_Lambda)** (PAPER_118): ties the GW cross-band damping to Planck densities;
  falsified if D_cross-band and the density ratio diverge.
- **xi_Holmlid = F_TRZ^(D_crit-SO_5/2)** (R7 capture): the 630 eV chain is now fully primitive; falsified
  if refined KER measurements break the F_TRZ^21 normalization.
- **T_c(SC gap) = 30 K = T_SCm/2** (PAPER_156): SCm superconductive transition at half the activation
  temperature; lab-testable in SCm-analogue systems.
- **QNM shift [1+alpha_Q-beta_damp]** (PAPER_010): LIGO O5 ringdown spectroscopy tests the band.
