# BATCH 1 VERIFICATION — every ruling claim re-read against its source paper (2026-08-31)

Ordered by Daniel after catching that batch questions were built from ledger
summaries without re-reading the papers. Method: every claim in every Batch 1
question re-verified against the source paper text, with file:line citations
and independent recomputation. Verdicts below. THREE defects found — none
overturns a ruling; all are recorded and corrected.

## Verdicts, claim by claim

**B1 (Q-008, GW power scaling) — RULING STANDS; LEDGER DEFECT FOUND.**
- PAPER_008 L50-52: `P_UQFF = D^2_total x P_GR, D_total = 0.333; tau = tau_GR/D^2 = 9.0` — VERIFIED verbatim.
- PAPER_005 L62: `P_GW,UQFF = F_combined^2 x P_GW,GR, F_combined = 0.903` — **the paper states the SQUARED convention explicitly.**
- DEFECT 1: the original Q-008 ledger entry framed PAPER_005 as "scales P linearly
  (P = F*P_GR)" and my B1 question called it "the lone linear outlier." The paper
  was never linear. The D^2 ruling is UNAFFECTED — strengthened: the corpus is
  unanimous (5/5), there is no outlier. PAPER_005's L92 "Combined 0.8100 product
  of four" vs L62 F=0.903 (F^2=0.815) remains the separate open Q-006.

**B2 (Q-002, B_crit unit) — VERIFIED VERBATIM.**
- PAPER_001 L110: `B_crit = 4.4 x 10^13 T`. PAPER_002 L66: `B_crit = 4.4x10^13 G`.
- The fork is exactly as presented. Ruling (Gauss) stands.

**B3 (Q-230 family) — VERIFIED (mojibake superscripts disclosed).**
- PAPER_250 L78-80: `DPM_resonance = 2*mu_B*B0/(hbar*omega0) ~ 1.76e3` (formula + stated value verbatim; recomputation gives 1.76e18 — the 15-order drift is real).
- PAPER_250 L46/L94-95: F_LENR stated 6.17e30 with intermediate 6.17e40 (correct chain gives 6.17e49 intermediate, 6.17e39 final) — drift real.
- 2.11e208 benchmark: PAPER_250 L36/139/148 + PAPER_237 L28/41/121 — stated in both, VERIFIED.

**B4 (Q-246/248, f_super) — RULING STANDS; TWO RECORD CORRECTIONS.**
- PAPER_295 L55 + L200: `f_super = 1.411e15 Hz` — VERIFIED (twice).
- PAPER_316 L46: worked chain uses 1.411e16 — VERIFIED.
- DEFECT 2 (attribution): the ledger said 1.411e15 is stated in "PAPER_295/302,
  both bodies." PAPER_302 contains NO f_super/Cooper statement. Attribution is
  PAPER_295-only. Ruling unaffected.
- NEW FINDING: PAPER_316 L33 parameter table prints f_super = 1.411e-6 Hz —
  a THIRD internal variant (table vs chain vs canonical), recorded for the
  paper's revision trail.

**B5 (Q-216, additive terms) — VERIFIED VERBATIM.**
- PAPER_220 L59-60: the master equation adds `+ F_wind + M_mag` directly;
  L68-69 give F_wind = E_sd/(c*4pi*r^2) [Pa] and M_mag = mu0*m/(4pi*r^3) [T].
  The dimensional gap is exactly as presented. Ruling (rho x length bridge form)
  stands; Q-216b (per-domain values) remains open.

**B6 (Q-224b, Eta Carinae mass) — VERIFIED VERBATIM.**
- PAPER_237 L39: `Mass M | ~150 M_sun = 2.984e31 kg` — the 10x label/value
  mismatch is in the paper exactly as presented. Ruling (2.984e32) stands.

**B7 (Q-220, a_wind) — VERIFIED; ONE ATTRIBUTION PRECISION NOTE.**
- PAPER_227 L27 (abstract): `a_wind ~ 4e3 m/s^2`. L65-67 (sec 2): rho_fluid =
  1e-21 giving 4e12. Both VERIFIED verbatim.
- PAPER_228 L55-56 (comparative table): Tapestry 4e3 / Wd2 4e4 — VERIFIED.
- DEFECT 3 (precision): rho_fluid = 1e-12 is NOT printed in PAPER_228; it is
  the UNIQUE value forced by the table's own arithmetic (1e-21*(2e6)^2/4e3 =
  1e-12; one equation, one unknown). The ruling's physics stands; the batch
  question said "established" where "uniquely implied by the table" is exact.

## Batch 2 items (B8-B11) — source-verified BEFORE re-presentation, same session
- B8 PAPER_089 L197-198 read directly; canonical Ubi located in predecessor
  QCalc_core_uqff.py compute_Ubi_SOURCE4 (beta_i-form); solar candidate
  beta_i*(1-F_TRZ)*g_sun = 148.7 vs printed 147 (1.2%, disclosed).
- B10 k4: SOURCE4 constants table k4=1.0 verbatim; QCalc.py L618 k4=2.0;
  QCalc.py L9570 k4=1.5 ("calibrated from solar system data") — three-way fork.
- B11 aTHz: compute_aTHz_SOURCE4 read in full; normalized (fTHz/1THz) reading
  reproduces PAPER_149's table ratio 0.0034 (10*1e5/3e8 = 3.33e-3); raw-Hz
  reading gives the impossible 3.33e9 inversion.

## Standing rule (canonized this session)
No ruling question goes to Daniel without: (1) the source paper re-read, (2)
verbatim quotes with file:line citations, (3) independent recomputation of
every number in the claim. Ledger entries are leads, not evidence. This rule
is gate-pinned and appended to CLAUDE.md.
