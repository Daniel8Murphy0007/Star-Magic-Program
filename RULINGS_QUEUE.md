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
