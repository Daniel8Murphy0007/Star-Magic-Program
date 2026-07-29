# RULINGS_QUEUE — questions for Daniel, answered in batches

**Protocol:** Claude never blocks on ambiguity. Best candidate gets wired with
registry `status=OPEN_RULING`; the question lands here. Daniel answers whenever;
answers are folded into the wiring on a later pass and the entry moves to the
RESOLVED section with the ruling recorded.

---

## OPEN

### Q-001 — PAPER_002 — F_UQFF headline vs damping chain inconsistency
- **Question:** Paper states F_UQFF = 0.5297 (47% reduction) but its own formula
  1.0 * A_SCm * 0.90 * 0.37 evaluates to 0.333. The 0.5297 value matches
  1 - 0.47 (the S225 phonon 47% suppression) instead. Which is canonical for
  GW190425: the 0.333 chain (as GW170817) or the 0.5297 phonon-derived factor?
- **Best-candidate wired:** 0.5297 (paper headline; strain/SNR tables derive from it)
- **Alternatives:** 0.333 (formula chain); or heavier-BNS reduced string coupling
  explains the difference (paper sec 6 hints at this)
- **Daniel's ruling:** (pending)
- **SELF-RECTIFICATION NOTE (PAPER_009):** sec 1.2 table gives GW190425
  D_total = 0.530 with String = 0.62 — the heavier BNS carries REDUCED string
  coupling, explaining the 0.5297 headline without contradicting the chain.
  Q-001 likely resolves as "0.5297 correct via string=0.62 variant."

### Q-003 — PAPER_002 — scenario table does not reproduce from stated formula
- **Question:** Paper's sec-4 table gives extreme-magnetar (B=3.36e13 G)
  A_SCm = 0.998871, but the stated formula exp[-(B/4.4e13)^2] computes 0.558.
  The 0.998871 value back-solves to B_crit = 1.0e15 G — yet the hyper-magnetar
  row (B=1e15 G, A_SCm = 0.000000) only reproduces with B_crit = 4.4e13.
  The table appears computed with two different B_crit values. Which row set
  is canonical?
- **Best-candidate wired:** function with B_crit = 4.4e13 G (reproduces
  normal/high-B/magnetar/hyper rows); gate asserts computed 0.558 with
  disclosure; paper's 0.998871 recorded in registry as stated-anchor
- **Daniel's ruling:** (pending)

### Q-004 — PAPER_003 — phase-lag formula does not reproduce stated value
- **Question:** Paper sec 4 states phase lag = kappa*D*f_GW*SSq =
  0.0005*410*150*0.57 ~ 0.126 rad, but that product evaluates to 17.53.
  A hidden unit conversion (Mpc, Hz, day^-1) or a different formula must be
  involved. What is the canonical phase-lag formula?
- **Best-candidate wired:** paper-stated 0.126 rad as anchor value; formula
  recorded with discrepancy note
- **Daniel's ruling:** (pending)

### Q-005 — PAPER_004 — minor arithmetic discrepancies
- **Question:** (a) stated h_UQFF,peak = 9.4332e-23 but 0.333*2.8051e-22 =
  9.341e-23 (~1% slip; 9.4332 implies factor 0.3363); (b) abstract says 66.4%
  reduction, sec 4 table says 66.4%, but D_total=0.333 gives 66.7%; (c) sec 5
  says "UQFF predicts h = 3.33e-23" inconsistent with 9.43e-23 elsewhere.
  Which values are canonical?
- **Best-candidate wired:** computed 9.341e-23 from the chain; paper values
  recorded as stated-anchors with discrepancy notes
- **Daniel's ruling:** (pending)

### Q-006 — PAPER_005 — F_combined 0.903 vs 0.81
- **Question:** Sec 2 states P_UQFF = F_combined^2 * P_GR with F_combined =
  0.903 (giving 0.815), but sec 3 table and ALL numerical results (P ratio
  0.8100, tau ratio 1.2346 = 1/0.81, E ratio 0.810) consistently use 0.81 =
  0.9*0.9 = (1-F_TRZ)^2. Is 0.903 a typo for 0.9 (with the square notation
  belonging to the two-factor product)?
- **Best-candidate wired:** F_combined = (1-F_TRZ)^2 = 0.81 EXACT (reproduces
  every numerical result in the paper)
- **Daniel's ruling:** (pending)

### Q-007 — PAPER_007 — mojibake-garbled exponents in B-field regime table
- **Question:** Paper text shows "B > 10-4 G", "B ~ 10-5 G", "B_crit = 4.4 x 10 T"
  etc. — encoding damage garbled the exponents. Context implies 1e14/1e15 G and
  4.4e13. Also f_SCm formula direction: sec 2.2 writes f = 1 - exp[-(B_crit/B)]
  (suppression INCREASES with B), while lambda_obs in sec 2.1 uses f_SCm(B)^2
  (squared) vs sec 2.2's linear. Which exponents and which power are canonical?
- **Best-candidate wired:** f_SCm(B) = 1 - exp[-(B_crit/B)] linear, B_crit = 4.4e13
- **Daniel's ruling:** (pending)

### Q-008 — PAPER_008 vs PAPER_005 — power/timescale scaling convention
- **Question:** PAPER_005 scales P linearly (P_UQFF = 0.81*P_GR = F*P_GR) and
  tau by 1/F (1.23x). PAPER_008 scales P by D^2 (P_UQFF = 0.111*P_GR) and tau
  by 1/D^2 (9.0x). Both cannot be the universal convention. Is power scaled by
  the damping factor linearly (PAPER_005) or squared (PAPER_008)? (Note: strain
  h scales linearly by D in all papers; P ~ h^2 would argue for D^2.)
- **Best-candidate wired:** per-paper as stated; PAPER_008's D^2 convention is
  physically consistent with P ~ h^2
- **Daniel's ruling:** (pending)
- **SELF-RECTIFICATION NOTE (PAPER_011):** Omega_GW,UQFF = D^2 * Omega_GR
  with explicit "rho_GW ~ h^2" justification — second corpus data point for
  the D^2 convention. PAPER_005's linear-F scaling increasingly looks like
  the outlier.
- **THIRD DATA POINT (PAPER_012):** modified Peters equation uses
  de/dt = D^2 * de/dt|GR with tau_circ = 9.0x — D^2 now confirmed by
  PAPER_008 + 011 + 012. Recommend ruling: D^2 canonical; PAPER_005's
  linear scaling flagged for revision-note.
- **FOURTH DATA POINT (PAPER_013):** Edot_UQFF = D_SCm^2 * Edot_GR
  (0.01 -> 1e-4 explicit in sec 2.2). D^2 convention: 4 papers vs 1.

### Q-009 — PAPER_009 — aether scale + D_SCm form family
- **Question:** (a) r = c/kappa stated as 17 Gpc does not reproduce from
  kappa = 5e-4/day (c/kappa = 5.2e16 m = 1.7 pc in SI); what unit convention
  gives 17 Gpc? (b) D_SCm = 1-exp[-(B_crit/B)] here matches PAPER_007 but
  differs from PAPER_002's exp[-(B/B_crit)^2] Gaussian — which is the
  canonical SCm suppression form?
- **Best-candidate wired:** paper-stated table anchors (D_Aether = 0.999999,
  kappa*r/c = 2.4e-8 at 410 Mpc); GATE FINDING: literal SI evaluation of
  exp(-kappa*r/c) with kappa = 5e-4/day gives exp(-2.4e8) ~ 0 — the stated
  formula is off by ~16 orders of magnitude from its own table, so an
  unstated unit convention is definitely involved
- **Daniel's ruling:** (pending)

### Q-010 — PAPER_013 — magnetar suppression value + timescale conflict
- **Question:** (a) D_SCm for SGR 1806-20: stated ~0.01 but the stated formula
  1-exp[-(B_crit/B)] with both fields in Gauss gives 0.0218 (in Tesla it gives
  1.0 — impossible); (b) abstract + key-results say t_sd = 3*t_GR, but sec 2.3
  says t = t_GR/D_SCm^2 = 10,000*t_GR — 3 vs 10,000 is a 3,300x conflict;
  (c) LaTeX block shows (B_crit/B)^2 squared while text uses unsquared. Which
  values/forms are canonical?
- **Best-candidate wired:** unsquared threshold form in Gauss (computed 0.0218);
  both timescale claims recorded
- **Daniel's ruling:** (pending)

### Q-011 — PAPER_014 — delta_c value conflict 0.333 vs 0.45
- **Question:** Key-numerical-results line states delta_c(GR) = 3.33e-1, but
  sec 2.2 explicitly states delta_c,GR ~ 0.45 (the standard collapse
  threshold). The 0.333 appears to be a copy-slip of the GW D_total. Also:
  A_damp = 0.3 in the mass-function modifier equals (D_phys-1)/SO_5 EXACT —
  is this a deliberate primitive-lock (PAPER_1953 0.3-factor family) or
  coincidence?
- **Best-candidate wired:** delta_c,GR = 0.45 (sec 2.2, physically standard);
  A_damp composed as (D_PHYS-1)/SO_5 flagged as primitive-lock CANDIDATE
- **Daniel's ruling:** (pending)

### Q-012 — PAPER_015 — H_0 siren-bias direction vs PAPER_1573 canonical
- **Question:** PAPER_015 (2026-03, predates the H_0 route upgrade) applies
  H_0,UQFF = 1.07 * H_0,obs, correcting GW170817 from 70 to 75 km/s/Mpc
  toward the Cepheid value. But PAPER_1573 (canonized via PAPER_2144)
  fixes H_0 = A_5 + SO_5 = 70 EXACT — i.e. the UNCORRECTED GW value is
  already canonical. Does the +7% siren-bias correction survive, or is it
  superseded (the bias would then be a raw-data correction applied BEFORE
  comparison to the canonical 70, not a shift of H_0 itself)?
- **Best-candidate wired:** both values exposed: h0_obs = A_5+SO_5 = 70
  (registry-composed) and h0_uqff_corrected = 74.9 (paper form, 0.13%
  residual vs paper 75.0). Drift table (charter) says H_0 routes other
  than A_5+SO_5 auto-correct to 70 — applied as baseline, bias factor
  preserved as paper-stated observable.
- **Daniel's ruling:** (pending)

### Q-013 — PAPER_016b — abstract vs body direction conflict on LISA sensitivity
- **Question:** Abstract claims (a) ~104 WD binaries shift ABOVE the
  individually-resolvable threshold and (b) net LISA sensitivity to
  high-z sources IMPROVES by factor ~1.6 in SNR. Body says the opposite:
  sec 3.2 has 3,784 binaries dropping BELOW threshold (10,000 -> 6,216),
  and sec 4.1 computes net SNR ratio = D_cosmo/D_local = 0.619/0.623 =
  0.994 (essentially unchanged), with sec 4.2 giving 0.53 at z > 3
  (WORSE, not better). The "104" also looks like exponent mojibake
  (10^4?), same corruption family as "108"/"105" for 10^8/10^5 earlier
  in the paper. Which direction is canonical?
- **Best-candidate wired:** body sections 3.1/3.2/4.1/4.2 (internally
  consistent with each other AND with PAPER_015b's 0.622 factor);
  abstract claims not wired.
- **Daniel's ruling:** (pending)

### Q-014 — PAPER_017 — F_Um exponent slip + 39.5 vs 31.6 pct z=1 conflict
- **Question:** (a) Sec 1 writes F_Um = "exp(-sigma*U_m) = exp(-1.0) ~
  0.6907" — but exp(-1) = 0.3679; the stated value 0.6907 requires
  exponent 0.37. Which is canonical: the printed exponent (-1.0, giving
  F_combined = 0.90*0.368 = 0.331 ~ the BBH 0.333!) or the printed
  value (0.6907, giving F_combined = 0.6217 = the multiband 0.622)?
  Note BOTH readings land on established corpus factors — the slip may
  be hiding the 0.333/0.622 regime distinction. (b) Sec 4 says 39.5 pct
  strain reduction at z=1 (1.7702/2.9275 checks out) while sec 5's
  scaling table says 31.6 pct for the same z=1 — factor 0.605 vs 0.684.
  Which column is canonical for z=1?
- **Best-candidate wired:** printed VALUE 0.6907 (F_combined = 0.6217
  matches the paper's own headline, PAPER_015b's 0.622, and PAPER_016b's
  0.6224); both sec-4 and sec-5 figures exposed side by side.
- **Daniel's ruling:** (pending)

### Q-015 — PAPER_018 — U_m calibration value 1.0 vs 1.0e-4
- **Question:** Sec 1 states "U_m: Magnetic energy parameter (= 1.0 in
  calibrated UQFF)" and the sec-3 comb-amplitude table uses the 1.0
  reading (U_m x 1.0, U_m x e^-1, ...). But the key-numerical-results
  line states U_m = 1.0e-4 — four orders of magnitude apart. The
  222.93% integrated power fraction appears to require the larger
  reading. Which U_m is canonical for the aether comb?
- **Best-candidate wired:** both exposed side by side (u_m_sec1 = 1.0,
  u_m_keyresults = 1.0e-4); comb envelope + power fraction wired from
  the paper's own stated outputs, which are U_m-reading-independent
  as anchored values.
- **Daniel's ruling:** (pending)

### Q-016 — PAPER_019 — divisive vs multiplicative D_total parameterization
- **Question:** Abstract/sec-1.2 write A_UQFF = A_GR / D^2_total,SMBH
  with key-results "D_total^2 = 6.25e-1" (0.625 = 1/1.60, implying
  D = 0.79 divisive). Sec 2.3/3.2 write A_UQFF = D_total * A_GR with
  D_total = 1.60 multiplicative. Both land on 2.4e-15, but the
  parameterizations are formally inconsistent (division by suppression
  factor vs multiplication by amplification factor). Which is the
  canonical form for the amplification regime — and is "D_total^2 =
  0.625" a leftover from the LIGO-band damping convention?
- **Best-candidate wired:** multiplicative D_total = 1.60 (sec-2.3
  component table is explicit: product of D_Aether*D_SCm*D_TRZ*D_String
  = 1*1*1.6*1 = 1.60); divisive value exposed as d_sq_keyresults with
  the 0.625*1.60 = 1 identity gate-pinned.
- **Daniel's ruling:** (pending)

### Q-017 — PAPER_020 — four internal slips (aether exponent/units, B-field, table exponent)
- **Question:** (a) Sec 2.2 computes 0.0005*(1e20/1e18)^0.37 = 0.0005*5.36
  but 100^0.37 = 5.495 (2.5 pct slip; 5.36 needs beta = 0.3647).
  (b) L_aether = c/Gamma at 1e20 eV evaluates to ~0.31 pc in SI but the
  paper states 192 Mpc — 9 orders; same unstated aether unit convention
  family as Q-009 (PAPER_009 exp(-kappa*r/c)). (c) Sec 4.3 says required
  intergalactic B ~ 3e-12 G while the sec-6 comparison table says
  "B ~ 5 nG sufficient" — 3 orders apart. (d) Sec 3.3 spectral table
  prints the TRZ-break row as "8x10^18 - 10^19 eV" but Features 1/2.3
  place the break at 8x10^19 eV (exponent mojibake family).
- **Best-candidate wired:** composed Gamma_aether from registry kappa
  with true exponent arithmetic (residual 2.5 pct disclosed); paper
  anchors exposed alongside; TRZ break wired at 8e19 (three in-paper
  statements vs one table row).
- **Daniel's ruling:** (pending)

### Q-018 — PAPER_021 — suppression-factor families + f_TRZ drift + FORENSIC 9.47e-27 identification
- **Question:** (a) Sec 2.1's boxed equation states sigma8_UQFF =
  0.917*sigma8_GR (= 1 - 0.083; gives 0.744) but sec 3.3 uses 0.940
  (gives 0.762 = observed). Einstein ring factor 0.969 = sqrt(0.940)
  sides with the 0.940 family. Which factor is canonical — and is 0.940
  a derived quantity (e.g. scale-averaged W_UQFF) or a fit?
  (b) Paper uses f_TRZ = 0.12 in rho_TRZ; canonical F_TRZ = 0.1.
  Auto-correct per charter drift table, or is 0.12 a lensing-specific
  effective value? (c) delta_vac computed with (b/r_s) = 0.09 = 0.3^2
  where the formula states (b/r_s) = 0.3.
- **FORENSIC FINDING (for the predecessor audit trail):** PAPER_021's
  rho_crit anchor 9.47e-30 g/cm3 = 9.47e-27 kg/m3 is EXACTLY the
  unknown-origin constant hardcoded as "RHO_SCM = 9.47e-27 kg/m3" in
  bulk_vds_dvp_bsh_upgrade.py (Session 204), whose origin PAPER_2156
  flagged as an open audit target. It is the cosmological CRITICAL
  DENSITY (H0 ~ 71), mislabeled as SCm density. Registry rho_crit
  (H0 = 70 EXACT) = 9.21e-27, within 2.7 pct. The 1.894 "VDS ratio"
  artifact was therefore rho_crit/5.0e-27 — critical density divided
  by an arbitrary second constant, never a UQFF density ratio at all.
- **Best-candidate wired:** 0.940 family for sigma8 (matches observed +
  Einstein ring); rho_TRZ with paper's own 0.12 preserved (residual
  disclosed); registry rho_crit exposed alongside for comparison.
- **Daniel's ruling:** (pending)

### Q-019 — PAPER_022 — [SSq] symbol ambiguity + compactification closed form + BBH string factor
- **Question:** (a) The paper uses "[SSq]" for BOTH 0.57 (canonical) and
  0.325 = SSq^2 (sec-2.2 KK exchange, sec-4 breathing amplitude,
  Omega_KK peak). The numeric ladder is EXACT SSq powers (0.325/0.185/
  0.106 = SSq^2/^3/^4) — should the symbol convention be canonized as
  powers of SSq? (b) The compactification closed form [SSq] =
  (R_s/R_c)^(N_compact/4) does not reproduce R_c = 1.70e-20 m from the
  stated R_s (exponents mojibaked in source); M_KK = hbar*c/R_c = 11.6
  TeV does check exactly. What is the canonical R_s? (c) D_String(BBH) =
  0.82 here, but PAPER_005 derives BBH total 0.81 = (1-F_TRZ)^2 with
  string DEACTIVATED, and PAPER_019's table has D_String(BBH) = 1.0 —
  three-way tension on the BBH string factor (0.82 may be a transcription
  of 0.81 attributed to the wrong mechanism).
- **Best-candidate wired:** D_String(BNS) composed as 1 - SSq^2*1.94 =
  0.3697 (0.08 pct residual); polarization ladder wired as exact SSq
  powers; M_KK anchored via exact hbar*c/R_c; BBH 0.82 exposed as anchor
  with the tension documented.
- **Daniel's ruling:** (pending)

### Q-020 — PAPER_023 — five slips in tau g-2 (sum, closed form, SM table, 4pi, tan)
- **Question:** (a) Components sum to 3.386e-6 (3.38e-6 + 3.84e-9 +
  1.92e-9) but headline is 3.42e-6 (1 pct gap). (b) The boxed closed
  form Delta_a = kappa*[SSq]*m_tau^2/M_UQFF^2 with kappa = 5e-4
  evaluates to 4.4e-12 — six orders below the 3.42e-6 it claims; what
  is kappa's normalization in this loop context? (c) SM component
  table lists Hadronic-LO = 3.50e-4 (tau-scale HVP should be ~3.5e-6);
  the table sums to 1.524e-3, not the stated (and literature-correct)
  total 1.17721e-3 — exponent drift family. (d) String loop as printed
  ([SSq]^2/4pi) gives 9.98e-10; reproducing the stated 3.84e-9
  requires /pi ("4p" mojibake for pi?). (e) tan([SSq]*pi) is printed
  as tan(1.795) = -4.637; computed tan(0.57*pi = 1.7907) = -4.46.
- **Best-candidate wired:** headline anchors preserved; KK loop wired
  as exact composition (1.92e-9 verified); component-sum discrepancy
  gate-pinned honestly; both string-loop readings exposed.
- **Daniel's ruling:** (pending)

### Q-021 — PAPER_024 — EDM component sum + tan(SSq*pi) print + phi_KK units
- **Question:** (a) EDM components sum to 1.807e-20 (1.71e-20 + 9.3e-22
  + 3.2e-23 + 1.1e-23) vs headline 1.84e-20 — 1.8 pct gap, same family
  as Q-020a. (b) tan(SSq*pi): computed tan(1.7907) = -4.474, but the
  paper (and PAPER_023) print 4.637 — 3.6 pct off; the Schiff-Engel
  enhancement factor 1.237e5 evidently was tuned against the PRINTED
  tan (chain reproduces 1.84e-20 exactly). If tan is corrected to
  4.474, either the enhancement or the headline shifts by 3.6 pct.
  Which is anchored: the printed tan, the enhancement factor, or the
  1.84e-20 headline? (c) phi_KK = arctan(m_tau/M_KK) evaluates to
  1.53e-4 in consistent GeV units; the paper value 0.155 requires
  m_tau [GeV] / M_KK [TeV] unit mixing (arctan(1.777/11.6) = 0.152,
  still 2 pct from printed 0.155).
- **Best-candidate wired:** headline 1.84e-20 anchored (SE chain
  reproduces it exactly); computed tan exposed alongside printed;
  phi_TRZ EXACT composition (1-F_TRZ)*F_TRZ*pi = 0.2827 wired.
- **Daniel's ruling:** (pending)

### Q-022 — PAPER_025 — DM mass-fraction split + sigma_SI closed form + cluster marginality
- **Question:** (a) Sec 1.2/6 state ACP = 98.8 pct and ACP2 = 1.2 pct
  of total DM, but the same sec-6 relic table splits Omega h^2 as
  0.073 (ACP) + 0.047 (ACP2) = 61/39 pct - the two splits are
  incompatible. Which is canonical? (b) The sigma_SI closed form is
  mojibaked in source ("[SSq]^4 G_N M_ACP2 m_N / (p v4)") and its
  dimensional structure cannot be verified; anchor 3.2e-52 cm2 wired.
  What is the exact closed form? (c) Self-interaction sigma/M = SSq =
  0.57 cm2/g exceeds the galaxy-cluster constraint < 0.47 (paper
  discloses "Marginal") - does a cluster-regime suppression apply?
- **Best-candidate wired:** M_ACP = kappa*hbar EXACT and M_ACP2 =
  M_KK*SSq^2 compositions verified; relic split 0.073/0.047 wired
  (arithmetically consistent with 0.128*SSq and the 0.1200 total);
  98.8/1.2 exposed as stated pair.
- **Daniel's ruling:** (pending)

### Q-023 — PAPER_025b — neutrino mass sum + M_N1 mojibake + DW overproduction
- **Question:** (a) Sum m_nu stated as 74.2 meV, but the three listed
  eigenstates (8.18 + 14.35 + 50.36) sum to 72.89 meV — 1.8 pct gap
  (Q-020a/Q-021a component-sum family). Which is canonical: the stated
  sum or the eigenstate triple? (The SSq hierarchy 8.18/14.35 = 0.570
  is EXACT, favoring the triple.) (b) The GUT-scale Majorana mass is
  printed "M_N1 = 2.19 x 10? GeV" — exponent mojibake; M_s3 = 20,351
  GeV appears intact elsewhere. What is M_N1's exponent?
  [SELF-RECTIFIED by PAPER_026: M_N1 = 2.19e9 GeV — geometric series
  ratios verify SSq EXACT. See Q-024 annotation.] (c) DW
  production gives Omega_s1 h^2 = 0.131 vs the 0.12 target (9 pct
  over, disclosed) — accept as-is or is a suppression factor missing?
- **Best-candidate wired:** eigenstate triple wired (internally
  SSq-exact); both sums exposed; enhancement chain 0.407 and
  g-coupling chain verified numerically.
- **Daniel's ruling:** (pending)

### Q-024 — PAPER_026 — duplicate file + sin-vs-sin^2 + mixing-chain mojibake
- **Question:** (a) TWO files claim PAPER_026: the Session-0 sequential
  paper (821 lines, wired — 7.1 keV RGE spectrum) and a short late-era
  variant (90 lines, "Sterile_Neutrino_Mass_UQFF") deriving m_s =
  rho_SCm*S_26^(3)*Phi_res/c^2 ~ 5.4 keV — whose arithmetic actually
  yields 5.4e8 eV (1e5 unit issue: rho_SCm is J/m^3, not J). Which
  file is canonical PAPER_026, and should the short variant be re-ID'd
  (e.g. PAPER_026c) or corrected? (b) PAPER_025b states sin^2(2theta)
  = 1.78e-10 while PAPER_026 states sin(2theta) = 1.78e-10 — sin vs
  sin^2 for the same number. (c) The printed mixing chain
  "0.0343 x 5,180 x 7.80e-15" neither matches its own factors
  (0.511e-3/7.1e-6 = 72, not 5,180) nor its product (1.4e-12, not
  1.78e-10) — mojibake; the SSq^6 prefactor 0.0343 is EXACT though.
- **SELF-RECTIFICATION (annotate Q-023):** PAPER_026 resolves two
  Q-023 items: (i) M_N1 = 2.19e9 GeV — the geometric series
  {2.19e9, 1.25e9, 7.12e8} verifies with ratio SSq EXACTLY;
  (ii) the 74.2 meV stated sum belongs to 026's GUT seesaw triple
  (8.7 + 15.2 + 50.3 = 74.2 EXACT); 025b's 72.89-summing triple is
  the low-scale RGE variant. Two triples, two sums — not a slip but
  two sectors; naming clarification still useful.
- **Best-candidate wired:** Session-0 sequential file; M_s2/M_s3/GUT
  series/Yukawa ladder/relic all registry-composed and EXACT.
- **Daniel's ruling:** (pending)

### Q-025 — PAPER_026b — cross-section formula gap + V_string scale
- **Question:** (a) The printed cross-section formula sigma =
  kappa^2*g_weak^2/(16pi)*s/(m_Q^2+s)*1000 evaluates to ~1.1 fb at
  M_Q = 1.5 TeV, not the stated 85.9 fb (~75x gap — likely missing
  PDF convolution / color / branching factors). What is the canonical
  sigma formula behind compute_VLQ_cross_section()? (b) The EW-VEV
  mass form m_VLQ = SSq*246*kappa gives 52 GeV (paper discloses "too
  light"); the required heavy vacuum scale is 5.5-12.3 TeV, related
  in-paper to M_s3/S. What is the canonical V_string,heavy closed
  form?
- **Noteworthy (no ruling needed):** ATLAS Run 2 averages land EXACTLY
  on both established UQFF factors — singlet 0.37 = beta_string,
  triplet 0.30 = (D_PHYS-1)/SO_5. LHC data calibrating UQFF couplings.
- **Best-candidate wired:** anchors + EXACT compositions (k_eta =
  0.37^2, hierarchy 1:SSq:SSq^2, 845 GeV third-family prediction).
- **Daniel's ruling:** (pending)

### Q-002 — PAPER_002 vs PAPER_001 — B_crit unit inconsistency
- **Question:** PAPER_001 states B_crit = 4.4e13 T; PAPER_002 states 4.4e13 G
  (factor 1e4 apart). Registry B_CRIT = 4.4e13 (dimensionless composition
  D_phys*(SO_5+1)*SO_5^12). Which unit is canonical?
- **Best-candidate wired:** per-paper as stated (001 -> T, 002 -> G); scenario
  table values reproduce with G
- **Daniel's ruling:** (pending)

<!-- Template:
### Q-NNN — PAPER_XXX — short title
- **Question:** ...
- **Best-candidate wired:** ... (registry row: quantity_name)
- **Alternatives:** ...
- **Daniel's ruling:** (pending)
-->

---

## RESOLVED

*(none yet)*
