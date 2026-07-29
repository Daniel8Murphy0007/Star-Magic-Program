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
