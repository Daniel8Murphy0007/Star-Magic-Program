# CHANGELOG — Star-Magic-Program

All notable changes to this project are documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.29.0] — 2026-07-29 — BAND 1: PAPER_026b

### Added
- **PAPER_026b dispatch** (Vector-Like Quarks): ATLAS Run 2
  (arXiv:2506.15515) coupling averages land EXACTLY on established UQFF
  factors — singlet-T (0.22+0.52)/2 = 0.37 = beta_string; triplet
  (0.14+0.46)/2 = 0.30 = (D_PHYS-1)/SO_5 (0.3-factor family, identity
  gate-pinned). k_eta_VLQ = 0.37^2 = 0.1369 EXACT (Ug2/Ug4 coupling).
  VLQ hierarchy 1 : SSq : SSq^2 predicts a THIRD FAMILY at 845 GeV —
  untested, Run-3 discoverable (falsifiable). sigma(1.5 TeV) = 85.9 fb
  anchored. OPEN_RULING Q-025 (printed sigma formula evaluates ~1.1 fb,
  75x gap — canonical formula ruling; V_string,heavy 5.5-12.3 TeV scale
  ruling; EW-VEV 52-GeV form disclosed too light in-paper).
- Gate: 228 assertions, 0 failures. Registry: 88 rows / 169 edges / 30 ledgers.

---

## [0.28.0] — 2026-07-29 — BAND 1: PAPER_026

### Added
- **PAPER_026 dispatch** (Sterile Neutrino Mass Generation): complete
  zero-free-parameter sterile spectrum. M_s2 = SSq*M_W = 45.81 GeV
  EXACT (just above M_Z/2); M_s3 = M_KK/SSq = 20,351 GeV EXACT; GUT
  Majorana series {2.19e9, 1.25e9, 7.12e8} GeV geometric in SSq
  (ratios verify EXACTLY); Yukawa ladder y_a = SSq^(4-a); entropy
  dilution D_s = 1/SSq; Omega_s1 = 0.305*SSq^1.5 = 0.131;
  leptogenesis eta_B = 6.1e-10 (0.3% of Planck); 0vbb m_bb = 12.3 meV
  (CUPID-1T). OPEN_RULING Q-024 (duplicate PAPER_026 file with 5.4 keV
  variant + 1e5 unit issue; sin-vs-sin^2 for 1.78e-10; mixing-chain
  mojibake).
- **SELF-RECTIFICATION — first ruling items closed by corpus:**
  PAPER_026 resolves Q-023a (74.2 meV = GUT triple 8.7+15.2+50.3 EXACT;
  025b's triple is the low-scale RGE variant — two sectors, two sums)
  and Q-023b (M_N1 = 2.19e9 GeV via exact SSq-series consistency).
- Gate: 221 assertions, 0 failures. Registry: 85 rows / 162 edges / 29 ledgers.

---

## [0.27.0] — 2026-07-29 — BAND 1: PAPER_025b

### Added
- **PAPER_025b dispatch** (Neutrino Polarizability): sterile M_s1 =
  7.1 keV (Aether RGE fixed point) -> E_gamma = 3.55 keV consistent
  with the unidentified Perseus/M31 XMM line; sin^2(2theta) = 1.78e-10
  under the XMM constraint. EXACT SSq hierarchy: m_nu1/m_nu2 =
  8.18/14.35 = 0.570 and M_N2/M_N1 = SSq; kappa*SSq = 2.85e-4 registry
  composition; sterile mixing enhancement 0.407 chain verified;
  g_UQFF-nucleon = 0.37*(m_N/M_s3)*SSq = 9.7e-6 (0.37 string factor
  again); polarizability bound a_nu < 1e-32 cm^3 (next-gen CEvNS).
  OPEN_RULING Q-023 (mass-sum 74.2 vs 72.89 meV; M_N1 exponent
  mojibake; DW overproduction 0.131 vs 0.12).
- Gate: 214 assertions, 0 failures. Registry: 82 rows / 154 edges / 28 ledgers.

---

## [0.26.0] — 2026-07-29 — BAND 1: PAPER_025

### Added
- **PAPER_025 dispatch** (Dark Matter Direct Detection): two zero-free-
  parameter DM candidates. ACP ultra-light: M_ACP = kappa*hbar =
  3.81e-24 eV EXACT registry composition, lambda_dB = 2.29 kpc
  reproduced, fuzzy DM solves core-cusp; ACP2 heavy: M_ACP2 = M_KK *
  SSq^2 = 3.77 TeV registry-composed, sigma_SI = 3.2e-52 cm2 (1e4 below
  LZ — all direct-detection nulls explained). Self-interaction sigma/M
  = SSq = 0.57 cm2/g primitive direct; relic Omega h^2 = 0.1200 =
  Planck 2020 with Omega_ACP = 0.128*SSq = 0.073 composition verified.
  OPEN_RULING Q-022 (98.8/1.2 vs 61/39 mass split; sigma_SI closed form
  mojibake; cluster-constraint marginality).
- Gate: 207 assertions, 0 failures. Registry: 79 rows / 147 edges / 27 ledgers.

---

## [0.25.0] — 2026-07-29 — BAND 1: PAPER_024

### Added
- **PAPER_024 dispatch** (Tau Electric Dipole Moment): d_tau = 1.84e-20
  e.cm — zero-free-parameter BSM prediction. phi_CP = SSq*pi = 1.7907
  rad registry-composed (near-maximal CP violation, leptogenesis-
  favorable, NOT the CKM phase); phi_TRZ = (1-F_TRZ)*F_TRZ*pi = 0.2827
  EXACT composition (discovered during wiring); Schiff-Engel chain
  reproduces the headline exactly; tau-factory reach 184-sigma
  (= 1.84e-20/1e-22 exact); FCC-ee 10-sigma. OPEN_RULING Q-021
  (component sum 1.8% under headline; tan(SSq*pi) computed -4.474 vs
  printed 4.637 with SE enhancement tuned to the print; phi_KK
  GeV/TeV unit mixing).
- Gate: 200 assertions, 0 failures. Registry: 76 rows / 140 edges / 26 ledgers.

---

## [0.24.0] — 2026-07-29 — BAND 1: PAPER_023 — BSM DOMAIN OPENS

### Added
- **PAPER_023 dispatch** (Tau Anomalous Magnetic Moment g-2): first
  Beyond-Standard-Model domain paper. Delta_a_tau^UQFF = +3.42e-6
  (aether loop dominant), a_tau^UQFF = 1.18063e-3, M_UQFF = 14.3 TeV
  consistent with PAPER_022's M_KK = 11.6 TeV. EXACT compositions:
  KK loop = (m_tau^2/(8pi*M_KK^2))*(2/3)*(1/SSq^2) = 1.92e-9;
  F_string = pi^2/6 Basel; (m_tau/m_mu)^2 = 282.8. Universality-
  breaking exponent 2.37 = 2 + 0.37 — the PAPER_022 string factor as
  an anomalous dimension. Tau-factory 3.4-sigma falsifiable target.
  OPEN_RULING Q-020: 5 slips (component sum 1 pct; closed-form kappa
  normalization 6 orders; SM-table Hadronic-LO exponent drift; 4pi-vs-pi
  in string loop; tan(SSq*pi) value).
- Gate: 193 assertions, 0 failures. Registry: 73 rows / 133 edges / 25 ledgers.

---

## [0.23.0] — 2026-07-29 — BAND 1: PAPER_022

### Added
- **PAPER_022 dispatch** (String Compactification Signatures): ORIGIN of
  the 0.37 string factor — D_String(BNS) = 1 - SSq^2*N_eff = 1 -
  0.3249*1.94 = 0.3697 (consumed by PAPER_001/009/020, now registry-
  composed). Extra GW polarization amplitudes are EXACT SSq powers:
  breathing SSq^2 = 0.325, longitudinal SSq^3 = 0.185, vector SSq^4 =
  0.106 (ET/SKA falsifiable; 32.5% HD contamination). M_KK = hbar*c/R_c
  = 11.6 TeV exact at R_c = 1.70e-20 m (all LHC limits satisfied);
  N_compact = D_crit - D_phys = 22 registry-composed. KK SGWB peak
  3.25e-10 at 1e-4 Hz; spectral break at 1e-8 Hz PTA-LISA unique.
  OPEN_RULING Q-019 ([SSq] symbol means both 0.57 and SSq^2;
  compactification closed form vs R_c; BBH string factor 0.82/0.81/1.0
  three-way tension).
- Gate: 186 assertions, 0 failures. Registry: 70 rows / 125 edges / 24 ledgers.

---

## [0.22.0] — 2026-07-29 — BAND 1: PAPER_021 — GW TEMPLATE FAMILY 001-021 COMPLETE

### Added
- **PAPER_021 dispatch** (Gravitational Lensing Corrections): sigma8
  tension resolved — f_vac(z=0.5) = 0.083 -> sigma8 = 0.811*0.940 =
  0.762 = DES/HSC/KiDS combined (0.0-sigma); rho_TRZ = SSq^2*f_TRZ*
  rho_crit with SSq^2 = 0.3249 registry-composed; shear (1-0.083)^2 =
  0.841; GW lensing magnification deficit 2.4% + unique 0.003 rad phase
  shift (ET-falsifiable ~2 yr). OPEN_RULING Q-018 (0.917-vs-0.940
  factor families; paper f_TRZ = 0.12 vs canonical 0.1; b/r_s slip).
- **FORENSIC IDENTIFICATION (predecessor audit closure):** PAPER_021's
  rho_crit anchor 9.47e-27 kg/m3 is EXACTLY the unknown-origin constant
  the predecessor's bulk_vds_dvp_bsh_upgrade.py hardcoded as "RHO_SCM"
  (PAPER_2156 open audit target). It is the cosmological critical
  density (H0 ~ 71) mislabeled as SCm density; the 1.894 "VDS ratio"
  artifact was rho_crit/5.0e-27, never a UQFF density ratio. Registry
  rho_crit (H0 = 70 EXACT) = 9.21e-27, within 2.7%.
- **GW template family PAPER_001-021 COMPLETE** (23 dispatches incl.
  015b/016b): all Session-0 GW/multi-band/PTA/UHECR/lensing papers wired.
- Gate: 179 assertions, 0 failures. Registry: 67 rows / 117 edges / 23 ledgers.

### Fixed
- Gate caught over-tight Einstein-ring tolerance (0.969^2 = 0.9390 vs
  0.940 is 0.11%, not <0.1%); assertion corrected with honest numbers.

---

## [0.21.0] — 2026-07-29 — BAND 1: PAPER_020

### Added
- **PAPER_020 dispatch** (Cosmic Ray Propagation): UHECR transport with
  Gamma_aether(E) = kappa*(E/E_ref)^0.37 registry-composed (0.37 = the
  PAPER_009 D_String(100 Hz) value); charge-dependent drag Z^(1/3)
  (He 1.26 / Fe 2.96 exact); TRZ scattering peak at 8e19 eV -> secondary
  spectral break Delta-gamma = +0.3 (AugerPrime-falsifiable 2026-28);
  GZK 3.7% sharper; Cen A 14% anisotropy via TRZ filament alignment
  (A_TRZ = 0.42) without extreme B fields. Same kappa/SSq across 22
  decades of energy (GW nHz -> 1e20 eV). OPEN_RULING Q-017: 4 internal
  slips — 100^0.37 arithmetic (2.5%), L_aether SI-vs-paper 9 orders
  (Q-009 aether-unit family), B-field 3e-12 G vs 5 nG, TRZ-break table
  exponent 8e18 vs 8e19.
- Gate: 172 assertions, 0 failures. Registry: 64 rows / 110 edges / 22 ledgers.

---

## [0.20.0] — 2026-07-29 — BAND 1: PAPER_019

### Added
- **PAPER_019 dispatch** (Pulsar Timing Array Anomalies): TRZ RESONANCE
  INVERSION — the same vacuum mechanism that damps at LIGO frequencies
  amplifies below ~1 uHz. D_TRZ(f) = 1 + SSq*Phi_TRZ(f) registry-
  composed; D_total(f_yr = 31.7 nHz) = 1 + 0.57*1.053 = 1.600;
  A_UQFF = 1.60*1.5e-15 = 2.4e-15 = NANOGrav 15-yr from STANDARD SMBH
  merger rates (no exotic populations); alpha_eff = -0.757 falsifiable
  tilt; Hellings-Downs preserved; 100 Hz BNS row 0.900*0.370 = 0.333
  cross-checks PAPER_001/009. OPEN_RULING Q-016 (abstract divisive
  A_GR/D^2 with D^2 = 0.625 = 1/1.60 vs sec-3.2 multiplicative D = 1.60;
  identity 0.625*1.60 = 1 gate-pinned).
- Gate: 166 assertions, 0 failures. Registry: 61 rows / 104 edges / 21 ledgers.

---

## [0.19.0] — 2026-07-29 — BAND 1: PAPER_018

### Added
- **PAPER_018 dispatch** (Aether Noise Spectrum for LISA): S_UQFF =
  S_GR*[1+P_aether]*F_TRZ(f); harmonic comb at n*0.99 mHz with exp(-n/2)
  envelope (no astrophysical analogue — smoking-gun); TRZ suppression
  dip depth = F_TRZ = 0.1 EXACT registry composition at ~5 mHz; aether
  power fraction 222.93% of GR SGWB; integrated SNR 12,695,834 — same
  validator figure as PAPER_017 (corpus consistency). OPEN_RULING Q-015
  (U_m = 1.0 sec-1 vs 1.0e-4 key-results, four orders apart).
- Gate: 160 assertions, 0 failures. Registry: 58 rows / 97 edges / 20 ledgers.

---

## [0.18.0] — 2026-07-29 — BAND 1: PAPER_017

### Added
- **PAPER_017 dispatch** (Redshift Corrections z=1, LISA): decomposes the
  ORIGIN of the 0.622 factor — F_combined = (1-F_TRZ)*F_aether*F_Um =
  0.90*1.0*0.6907 = 0.6217; merger phase lag = 2*pi*F_TRZ = 0.6283 rad
  EXACT registry composition (= 0.10 cycles = F_TRZ); SNR ratio 0.6233;
  flat 31-32% reduction z=0.5-2 (aether-negligible regime).
  OPEN_RULING Q-014: (a) F_Um printed "exp(-1.0) ~ 0.6907" but
  exp(-1) = 0.368 — remarkably, exponent reading gives F_combined =
  0.331 ~ the BBH 0.333 while value reading gives 0.622 — the slip may
  hide the regime split; (b) sec-4 39.5% vs sec-5 31.6% at same z=1.
- Gate: 154 assertions, 0 failures. Registry: 55 rows / 91 edges / 19 ledgers.

---

## [0.17.0] — 2026-07-29 — BAND 1: PAPER_016b

### Added
- **PAPER_016b dispatch** (White Dwarf Binary Foreground Reduction):
  LISA mHz confusion foreground P_UQFF = D_local^2 * P_GR (1.67e-41 vs
  4.31e-41, 61.4% reduction); D_local = sqrt-derived 0.6224 — corpus
  consistency with PAPER_015b's cross-band 0.622; resolved catalog
  10,000 -> 6,216 = exact linear-D scaling; net SNR z~1 = 0.994.
  OPEN_RULING Q-013 (abstract claims 1.6x SNR improvement + binaries
  shifting ABOVE threshold; body computes 0.994 net + 3,784 dropping
  BELOW — body wired, abstract not).
- Gate: 148 assertions, 0 failures. Registry: 52 rows / 84 edges / 18 ledgers.

### Fixed
- **Calculator file order** — PAPER_015/015b/016 dispatch blocks had been
  inserted above the interface instead of after PAPER_014 (wrong anchor;
  registration unaffected). All 18 dispatches now in strict paper
  sequence in the file.

---

## [0.16.0] — 2026-07-29 — BAND 1: PAPER_016

### Added
- **PAPER_016 dispatch** (Quantum Entanglement Nonlocal Correlations):
  gamma_damp = kappa*(E/E_ref) registry-composed; CHSH suppression
  S_UQFF = 2.75 at GeV (vs Tsirelson 2*sqrt(2)), 2.60 at L>1000 km;
  entanglement range extension 1/D_total = 3.0 = 1/(1-D_GW_EROSION);
  tau_dec ~ 50 s satellite-scale falsifiable prediction. PRIMITIVE-LOCK
  CANDIDATE: energy-scaling delta = 1.5 = D_BSFG/D_PHYS EXACT
  (PAPER_1962 3/2 cross-scale family). CLEAN wiring.
- Gate: 142 assertions, 0 failures. Registry: 49 rows / 78 edges / 17 ledgers.

---

## [0.15.0] — 2026-07-29 — BAND 1: PAPER_015b

### Added
- **PAPER_015b dispatch** (Multiband LISA+LIGO Synergy): D = 0.622
  FREQUENCY-INDEPENDENT across mHz and 100 Hz bands — coherent cross-band
  suppression as the vacuum-propagation hallmark. SNR 268->167 (GW150914)
  and 1116->694 (SMBH z~1) both exactly 0.622; horizons 13440->8355 Mpc /
  140.8->87.5 Gpc; volume 24% GR. Paper itself discloses 0.622 =
  cross-band average of pure-BBH 0.333 — self-documents the factor
  relation flagged at PAPER_015. CLEAN wiring (abstract "0.522" slip
  noted in registry, sec-4 form wired).
- Gate: 136 assertions, 0 failures. Registry: 46 rows / 71 edges / 16 ledgers.

---

## [0.14.0] — 2026-07-29 — BAND 1: PAPER_015

### Added
- **PAPER_015 dispatch** (Cosmological Implications of Modified GW
  Propagation): Gamma_UQFF(f,z) damping law with discriminator exponents
  alpha=-0.7 / beta=0.8 (vs Horndeski/extra-dim/mod-grav); standard-siren
  H_0 bias 1.07x; detection volume 0.622^3 = 24% of GR (internally
  consistent LIGO horizon 8355/13440, cross-checks PAPER_011 mixed
  population). OPEN_RULING Q-012: paper "corrects" GW170817 H_0 70 -> 75,
  but PAPER_1573 canonizes 70 = A_5+SO_5 EXACT — the uncorrected value.
  Baseline wired registry-composed as A_5+SO_5.
- Gate: 130 assertions, 0 failures. Registry: 44 rows / 67 edges / 15 ledgers.

---

## [0.13.0] — 2026-07-29 — BAND 1: PAPER_014

### Added
- **PAPER_014 dispatch** (Primordial Black Holes): modified Friedmann with
  Lambda_UQFF = kappa*rho_crit (registry-composed from KAPPA_PER_DAY and
  RHO_CRITICAL); critical overdensity 0.45*(1-alpha_Q+beta_damp);
  mass-function A_damp = 0.3 = (D_phys-1)/SO_5 EXACT — primitive-lock
  CANDIDATE flagged (PAPER_1953 0.3-factor family). OPEN_RULING Q-011
  (delta_c 0.333 vs 0.45 copy-slip).
- Gate: 124 assertions, 0 failures. Registry: 41 rows / 61 edges / 14 ledgers.

---

## [0.12.0] — 2026-07-29 — BAND 1: PAPER_013

### Added
- **PAPER_013 dispatch** (Magnetar Spin-Down — the kappa calibration paper):
  D_SCm(B) threshold suppression (99% for SGR 1806-20); braking index
  n_UQFF = 1.5-2.0 matches observed 1-2.5 (GR predicts 3); magnetar age
  problem resolved (~1e7 yr). OPEN_RULING Q-010 (D_SCm 0.01 vs computed
  0.0218; abstract 3x vs sec-2.3 10,000x timescale; squared-vs-linear form).
- **Q-008 FOURTH data point** — Edot = D_SCm^2 * Edot_GR explicit.
  D^2 convention: 4 corpus papers vs 1 outlier.
- Gate: 119 assertions, 0 failures. Registry: 38 rows / 54 edges / 13 ledgers.

---

## [0.11.0] — 2026-07-29 — BAND 1: PAPER_012

### Added
- **PAPER_012 dispatch** (Eccentric Binary Circularization): modified
  Peters de/dt = D^2 * de/dt|GR; tau_circ 9.0x extension; residual
  e = 0.003 at LIGO band (30x GR); ~3x eccentric-merger rate. CLEAN.
- **Q-008 third data point** — D^2 convention now confirmed by
  PAPER_008 + 011 + 012; ruling recommendation: D^2 canonical.
- **Badge cacheBust fix** — PyPI camo proxy caches badge URLs forever;
  dynamic badges now carry ?cacheBust=<version> per ship (CLAUDE.md 2b).
- Gate: 114 assertions, 0 failures. Registry: 35 rows / 49 edges / 12 ledgers.

---

## [0.10.0] — 2026-07-29 — BAND 1: PAPER_011

### Added
- **PAPER_011 dispatch** (Stochastic GW Background): Omega_UQFF = D^2 *
  Omega_GR (rho_GW ~ h^2); BNS suppression 0.111 (89%), BBH 0.656 (34%),
  mixed population 0.37x (63% SGWB reduction); detection delayed
  2028 -> 2032-2035; LISA slope discriminator. CLEAN wiring.
- Q-008 SELF-RECTIFICATION: PAPER_011 is the second corpus data point for
  the D^2 power convention — PAPER_005's linear-F increasingly the outlier.
- Gate: 110 assertions, 0 failures. Registry: 33 rows / 46 edges / 11 ledgers.

---

## [0.9.0] — 2026-07-29 — BAND 1: PAPER_010

### Added
- **PAPER_010 dispatch** (Post-Merger Oscillations + Remnant Mass):
  QNM frequency downshift f_UQFF = 0.95*f_GR (2.5 -> 2.375 kHz, 125 Hz
  detectable at 3G); ringdown decay 29% faster (tau ~7 ms, gamma=0.4);
  15% extra quantum-channel dissipation -> lighter remnant. CLEAN wiring
  (internally consistent paper, no new rulings).
- Gate: 105 assertions, 0 failures. Registry: 31 rows / 43 edges / 10 ledgers.

---

## [0.8.0] — 2026-07-29 — BAND 1: PAPER_009

### Added
- **PAPER_009 dispatch** (Damping Mechanism Decomposition, Session 143):
  4-mechanism synthesis (Aether/SCm/TRZ/String) with per-system table.
  GW190425 string factor 0.62 — SELF-RECTIFICATION evidence for Q-001
  (heavier BNS carries reduced string coupling; 0.5297 headline consistent).
  BNS/BBH damping ratio 2.43x. OPEN_RULING Q-009: gate found the aether
  formula exp(-kappa*r/c) evaluates ~0 in SI — 16 orders from the paper's
  own table (0.999999) — unstated unit convention involved.
- Gate: 100 assertions, 0 failures. Registry: 28 rows / 40 edges / 9 ledgers.

---

## [0.7.0] — 2026-07-29 — BAND 1: PAPER_008

### Added
- **PAPER_008 dispatch** (Waveform Phase Evolution + Template Mismatch,
  Session 143): P_UQFF = D_total^2 * P_GR; inspiral extension 9.0x;
  phase-lag growth ~8x phi_GR; full-inspiral 2310.8 rad cross-checks
  PAPER_006. OPEN_RULING Q-008 (power convention: linear F in PAPER_005
  vs D^2 here; D^2 physically consistent with P ~ h^2).
- Gate: 94 assertions, 0 failures. Registry: 25 rows / 35 edges / 8 ledgers.

---

## [0.6.0] — 2026-07-29 — BAND 1: PAPER_007

### Added
- **PAPER_007 dispatch** (BNS Tidal Deformability, Session 143):
  Lambda = (2/3)*k2*(R/M)^5 (~400 for M=1.4/R=12km); UQFF suppression
  f_SCm(B) = 1 - exp[-(B_crit/B)]; mass-gap NS/BH discriminator
  Lambda_NS(2.52) = 16 vs Lambda_BH = 0. OPEN_RULING Q-007 (mojibake
  exponents + linear-vs-squared f_SCm power).
- Gate: 88 assertions, 0 failures. Registry: 23 rows / 32 edges / 7 ledgers.

### Fixed
- Corrects the prior claim that PAPER_007 was absent from the corpus —
  it exists (Tidal_Deformability_Constraints_BNS_UQFF) and is now wired
  in proper sequence.

---

## [0.5.0] — 2026-07-29 — BAND 1 CONTINUES: PAPER_004..PAPER_006

### Added
- **PAPER_004 dispatch** (GW170817 chirp): paper's own explicit (1-f_TRZ)
  composition — corpus-internal confirmation of primitive form. OPEN_RULING Q-005.
- **PAPER_005 dispatch** (BBH energy retention): F = (1-F_TRZ)^2 = 0.81
  EXACT, string deactivated for BBH; P/tau/E scale consistently. OPEN_RULING Q-006.
- **PAPER_006 dispatch** (multi-messenger): c_GW = c preserved, kilonova
  unmodified, detection volume 27x shrink. Clean.
- Gate Block 9 extended: 83 assertions total, 0 failures.
- Registry pantheon: 20 rows, 28 edges, 6 citation ledgers.

### Changed
- Version 0.4.0 → 0.5.0; badges fidelity_gate 83/0, public_surfaces 6.
- WHITEPAPER_INDEX: 004/005 → ⚠, 006 → ✓.

---

## [0.4.0] — 2026-07-28 — BAND 1 CONTINUES: PAPER_002 + PAPER_003

### Added
- **PAPER_002 dispatch** (GW190425 Mass Gap): A_SCm(B) threshold function,
  5-scenario field table, mass-gap classification P(BH)=0.51. OPEN_RULING.
- **PAPER_003 dispatch** (GW150914 BBH): universal 0.333 chain, 3.0x
  apparent-distance bias, phase-lag anchor. OPEN_RULING.
- **RULINGS_QUEUE Q-001..Q-004** — gate-discovered paper-internal
  inconsistencies (F_UQFF headline vs chain; B_crit units T vs G;
  scenario table reproduction; phase-lag formula evaluation).
- Gate Block 9 extended: 68 assertions total, 0 failures.
- Registry pantheon: UNIFIED_REGISTRY 10 rows, GRAPH 18 edges,
  CORPUS_CITATIONS 3 ledgers.

### Changed
- Version 0.3.1 → 0.4.0; badges fidelity_gate 68/0, public_surfaces 3.
- WHITEPAPER_INDEX: PAPER_002/003 → ⚠ OPEN_RULING.

---

## [0.3.0] — 2026-07-28 — WIRING CAMPAIGN START

### Added
- **CLAUDE.md** — campaign charter: sequential wiring from PAPER_001, band
  structure, per-paper protocol, template authorizations, drift auto-corrections,
  rulings queue, gate discipline, ship protocol, standing lessons.
- **ship.ps1** — one-command band ship (gate → commit → tag-verify → push).
- **RULINGS_QUEUE.md** — never-block ambiguity protocol.
- **First wired dispatch: PAPER_001** (GW170817 UQFF Damping Analysis):
  - D_total composed from registry primitives (F_TRZ, D_GW_EROSION, B_CRIT)
  - 16 observables returned; honest 0.10% residual vs 1/3 primitive identity
  - 8 gate assertions (Block 9 opened)
  - +4 UNIFIED_REGISTRY.csv rows, +7 GRAPH edges, +1 CORPUS_CITATIONS row
  - WHITEPAPER_INDEX: PAPER_001 ⬜ → ✓

### Changed
- Version 0.2.2 → 0.3.0; badges fidelity_gate 55/0, public_surfaces 1.

---

## [0.2.2] — 2026-07-28 — BADGE PATCH

### Added
- **Documentation Status badge** — the 7th badge from predecessor Star-Magic pattern.
  v0.2.1 tag on PyPI accidentally landed with only 6 badges; v0.2.2 adds
  the missing `Documentation Status` shield pointing at
  `star-magic-program` on readthedocs.org.

### Changed
- SESSION_LOG.md — badge descriptions expanded with source/link details.
- Version bumps 0.2.1 → 0.2.2 (pyproject/calc/gate/citation).

### Unchanged
- All physics content, corpus, registry scaffolds, calculator DISPATCH.

---

## [0.2.1] — 2026-07-28 — README BADGES

### Added
- 7 README badges rendered by shields.io (visible on PyPI + GitHub):
  - `pypi` (dynamic version), `python` (dynamic version support),
  - `License AGPL-3.0 + Commercial`,
  - `Fidelity Gate passing`,
  - `Whitepapers 2,255`,
  - `Public Surfaces 0` (updates as calculator gets wired),
  - `CI` (dynamic status from GitHub Actions).

### Changed
- Version bumps 0.2.0 → 0.2.1 (pyproject.toml, uqff_calculator.py, uqff_fidelity_tests.py, CITATION.cff).

### Unchanged
- Whitepaper corpus, registry scaffolds, calculator DISPATCH, fidelity gate blocks 1-8 — all identical to v0.2.0.

---

## [0.2.0] — 2026-07-28 — CORPUS + REGISTRY SCAFFOLDING

### Added

- **Whitepaper corpus (2,419 files)** imported from predecessor
  `github.com/Daniel8Murphy0007/Star-Magic` v5.86.0, reorganized:
  - `whitepapers/` — 2,255 `.md` files + 1 `.bak`
  - `pdf/` — 45 `.pdf` files
  - `tex/` — 107 `.tex` files
  - `txt/` — 11 `.txt` files
- **R3 Unified Registry Pantheon scaffolds** (all empty per clean-start discipline):
  - 4 Python regen modules: `uqff_registry_status.py`, `uqff_registry_graph.py`,
    `uqff_registry_xgeo.py`, `registry_generator.py` — signatures + docstrings + `pass`
  - 14 CSV registries with header rows only
  - 5 MD registry docs with structural section headers
  - `UNIFIED_REGISTRY_VERSION.txt` — v0.2.0 marker
- `CHANGELOG.md` — this file, release-history log
- `WHITEPAPER_INDEX.md` — living index of all whitepapers with wired/not-wired status
- `_BUILD_LOG.md` — cumulative build log

### Changed

- `pyproject.toml` version 0.1.0 → 0.2.0, description updated for corpus+pantheon
- `uqff_calculator.py` VERSION 0.1.0 → 0.2.0
- `uqff_fidelity_tests.py` version-lock assertion updated to 0.2.0
- `CITATION.cff` version 0.1.0 → 0.2.0
- `SESSION_LOG.md` — v0.2.0 entry appended

### Unchanged (deliberately preserved from v0.1.0)

- `uqff_registry_primitives.py` — 96 canonical constants
- `uqff_calculator.py::DISPATCH = {}` — empty; grown by v0.3.0+ wiring
- Fidelity gate blocks 1–7 (block 8 banned-literal check unchanged)
- All 15 v0.1.0 scaffold files (LICENSE, NOTICE, README, etc.)

### Discipline notes

- **No predecessor CSV data preserved.** 7,688 rows of predecessor
  registry state discarded. Every future row must come from a fresh
  paper reading with gate-verified residual.
- **Rules A–E** from v0.1.0 remain locked (registry-single-source-of-truth,
  one-dispatch-per-whitepaper, one-paper-at-a-time growth, OPEN-over-SM,
  predecessor-read-only).

---

## [0.1.0] — 2026-07-28 — SCAFFOLD (initial ship)

### Added

- Fresh-repo systematic rebuild scaffold for the UQFF calculator.
- `uqff_registry_primitives.py` — 96 canonical constants carried verbatim
  from predecessor Star-Magic v5.86.0 R5 baseline.
- `uqff_calculator.py` — 79-line skeleton, empty `DISPATCH = {}`,
  public `calc(paper_id, dataset)` interface.
- `uqff_fidelity_tests.py` — 8-block fidelity gate.
- Dual license: AGPL-3.0-or-later OR LicenseRef-StarMagic-Commercial.
- `README.md`, `CITATION.cff`, `NOTICE`, `COMMERCIAL.md`, `SESSION_LOG.md`.
- CI + release-to-pypi workflows (GitHub Actions + PyPI Trusted Publisher).
- `.gitignore`, `.gitattributes`, `LICENSE-MIT-INITIAL.txt` (archived repo-init license).

### Predecessor delta at time of v0.1.0

| Metric | Predecessor (v5.86.0) | v0.1.0 |
|---|---:|---:|
| Total canonical-state lines | 441,167 | 1,142 |
| Redundant hardcoded literals | 3,352 | 0 |
| Files importing registry | 4 of 23 | 3 of 3 |
| Duplicate primitive definitions | 20 primitives × 2-10 files | 0 |
| Calculator size | 73,629 lines | 79 lines |

---

## Unreleased — v0.3.0+ (planned)

**First wiring batch**: 46 UQFF_LANDMARK papers as the structural spine.
Each paper: one dispatch to `uqff_calculator.py::DISPATCH`, one row to
`UNIFIED_REGISTRY.csv`, one gate assertion. See SESSION_LOG for order.

---

*Every entry above is append-only. History does not get rewritten.*
