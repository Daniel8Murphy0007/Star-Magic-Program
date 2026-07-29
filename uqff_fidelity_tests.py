"""uqff_fidelity_tests — gate assertions for Star-Magic-Program.

Every ship MUST run `python uqff_fidelity_tests.py` and see exit 0 before
being tagged. Assertions grow as the whitepaper-wiring campaign advances.

Discipline (locked):
  - Every assertion locks a specific fact about the framework.
  - When an assertion fails, the fact broke — fix the code, not the assertion.
  - Range checks (`>= N`) not equality (`== N`) for growing collections.
  - When a canonical value is replaced by a tighter route, DISCLOSE it here.
"""
import math
import sys

import uqff_registry_primitives as P
import uqff_calculator as C


FAILURES = []


def assert_that(cond, label):
    if not cond:
        FAILURES.append(label)


# =============================================================================
# BLOCK 1 — LOCKED PRIMITIVE INTEGRITY
# =============================================================================
assert_that(P.D_PHYS == 4,  "P.D_PHYS == 4 (locked integer primitive)")
assert_that(P.D_CRIT == 26, "P.D_CRIT == 26 (locked integer primitive)")
assert_that(P.N_CH == 9,    "P.N_CH == 9 (locked integer primitive)")
assert_that(P.SO_5 == 10,   "P.SO_5 == 10 (locked integer primitive)")
assert_that(P.A_5 == 60,    "P.A_5 == 60 (locked integer primitive)")
assert_that(P.RHO_SCM == 7.09e-37, "P.RHO_SCM = 7.09e-37 (foundational primitive)")
assert_that(P.BETA_I == 0.6029, "P.BETA_I = 0.6029 (PAPER_1203 canonical)")
assert_that(P.F_TRZ == 0.1, "P.F_TRZ = 0.1 (PAPER_1160 = 1/SO_5)")
assert_that(P.SSQ == 0.57, "P.SSQ = 0.57 (PAPER_1154 canonical)")
assert_that(abs(P.S_26 - 1.453162) < 1e-9, "P.S_26 = 1.453162 (Ramanujan)")

# =============================================================================
# BLOCK 2 — DERIVATIVE-PRIMITIVE IDENTITIES (must be EXACT)
# =============================================================================
assert_that(P.D_BSFG == 6, "PAPER_1521: D_BSFG = D_CRIT - 2*SO_5 = 6")
assert_that(abs(P.K_MEX - 25.0/12.0) < 1e-15, "PAPER_1522: K_MEX = 25/12 EXACT")
assert_that(abs(P.KAPPA_PER_DAY - 5e-4) < 1e-15, "PAPER_2112: KAPPA = 5e-4 EXACT (float tol)")
assert_that(P.Q_PHONON == 6.25, "PAPER_2154: Q_PHONON = SO_5^2/D_phys^2 = 25/4 EXACT")
assert_that(abs(P.D_GW_EROSION - 2.0/3.0) < 1e-15, "PAPER_2154: D_GW_EROSION = D_phys/D_BSFG = 2/3 EXACT")

# =============================================================================
# BLOCK 3 — STRUCTURAL LANDMARKS (all EXACT integer or rational identities)
# =============================================================================
assert_that(P.A5_OVER_DPHYS == 15.0, "PAPER_2143: A_5/D_phys = 15 EXACT")
assert_that(abs(P.K2_OVER_Q_ROCKY - 3.0/125.0) < 1e-15, "PAPER_2136: k2/Q = 3/125 EXACT")
assert_that(P.FRAME_CADENCE_62 == 62, "PAPER_2137: 2*D_crit + SO_5 = 62 EXACT")
assert_that(P.COMPOSED_INTEGER_44 == 44, "PAPER_2126: D_phys*(SO_5+1) = 44 EXACT")
assert_that(P.AETHER_COUPLING_11 == 11, "PAPER_1978: SO_5+1 = 11 EXACT")
assert_that(abs(P.VCK_KERNEL - 19.0/160.0) < 1e-15, "PAPER_2131: VCK = 19/160 EXACT")
assert_that(abs(P.TILT_PRODUCT_1_12 - 1.0/12.0) < 1e-15, "PAPER_2132: 1/12 tilt EXACT")
assert_that(P.ALPHA_INVERSE_UQFF == 137.0, "PAPER_2134: A_5*K_MEX + 12 = 137 EXACT")
assert_that(abs(P.HUBBLE_TILT_1_12 - 1.0/12.0) < 1e-15, "PAPER_1156: K_MEX-2 = 1/12 EXACT")
assert_that(P.HALVING_D_PHYS == 2.0, "PAPER_2138: D_phys/2 = 2 EXACT")
assert_that(P.HALVING_D_BSFG == 3.0, "PAPER_2138: D_BSFG/2 = 3 EXACT")
assert_that(P.HALVING_SO_5 == 5.0, "PAPER_2138: SO_5/2 = 5 EXACT")
assert_that(P.HALVING_D_CRIT == 13.0, "PAPER_2138: D_crit/2 = 13 EXACT")

# =============================================================================
# BLOCK 4 — MILLENNIUM PRIZE IDENTITIES (4 EXACT + 4 anchor)
# =============================================================================
assert_that(P.HODGE_IDENTITY == 1.0, "PAPER_1182: Hodge = 1.0 EXACT")
assert_that(abs(P.POINCARE_7_12 - 7.0/12.0) < 1e-15, "PAPER_1182: Poincare = 7/12 EXACT")
assert_that(abs(P.P_VS_NP_BOUND - (1.0 - 1e-9)) < 1e-15, "PAPER_1182: P≠NP = 1 - F_TRZ^9 EXACT")
assert_that(abs(P.NAVIER_STOKES_ENSTROPHY_CAP - 0.85) < 1e-15,
            "PAPER_1182: NS enstrophy cap = 17/20 = 0.85 EXACT")
assert_that(P.YANG_MILLS_MASS_GAP_GEV == 1.736, "PAPER_1318: YM gap = 1.736 GeV")
assert_that(P.BSD_CREMONA_37A1 == 0.30598, "PAPER_599: BSD Cremona 37a1")

# =============================================================================
# BLOCK 5 — HOP-STATE H_0 CANONICAL ROUTE (PAPER_1573)
# =============================================================================
assert_that(P.H0_KM_PER_S_PER_MPC == 70.0, "PAPER_1573: H_0 = A_5 + SO_5 = 70 EXACT")
h0_expected = 70.0 * 1000.0 / 3.0857e22
assert_that(abs(P.H0_GRID - h0_expected) < 1e-25, "H0_GRID SI conversion consistent")

# =============================================================================
# BLOCK 6 — PARTICLE-PHYSICS PRIMITIVE-COMPOSED FORMULAS (PAPER_2131)
# =============================================================================
alpha_s_expected = P.F_TRZ * P.K_MEX * P.SSQ - (P.F_TRZ ** 3) * P.PHI_RES_COUNTING
assert_that(abs(P.ALPHA_S_M_Z - alpha_s_expected) < 1e-15,
            "PAPER_2131 S378: alpha_s = F_TRZ*K_MEX*SSq - F_TRZ^3*Phi_5/6")
jarl_expected = (P.F_TRZ ** 5) * P.D_BSFG * P.SSQ * (1.0 - P.VCK_KERNEL)
assert_that(abs(P.JARLSKOG_CP_INVARIANT - jarl_expected) < 1e-30,
            "PAPER_2131: Jarlskog = F_TRZ^5*D_BSFG*SSq*(1-VCK)")
n_eff_expected = P.D_PHYS - P.PHI_RES_COUNTING - P.VCK_KERNEL
assert_that(abs(P.N_EFF_NEUTRINO - n_eff_expected) < 1e-15,
            "PAPER_2131: N_eff = D_phys - Phi_5/6 - VCK")

# =============================================================================
# BLOCK 7 — CALCULATOR SCAFFOLD INTEGRITY
# =============================================================================
assert_that(C.VERSION == "0.4.0", "uqff_calculator.VERSION = 0.4.0")
assert_that(isinstance(C.DISPATCH, dict), "DISPATCH is a dict")
assert_that(C.wired_count() >= 0, "wired_count is queryable (>= 0)")
assert_that(callable(C.calc), "calc is callable")
open_result = C.calc('PAPER_9999')  # a paper that surely isn't wired
assert_that(open_result['status'] == 'OPEN_NOT_YET_WIRED',
            "calc() returns OPEN_NOT_YET_WIRED for unwired papers")

# =============================================================================
# BLOCK 8 — REGISTRY IMPORT DISCIPLINE
# =============================================================================
with open('uqff_calculator.py', 'r', encoding='utf-8') as f:
    calc_src = f.read()
assert_that('from uqff_registry_primitives import' in calc_src,
            "uqff_calculator.py imports from uqff_registry_primitives")
# Ban hardcoded numeric literals that duplicate the registry
BANNED = ['7.09e-37', '0.6029', '1.453162']  # rho_SCm, beta_i, S_26
for tok in BANNED:
    if tok in calc_src.replace('# ', ''):  # strip comments
        # allow inside comments only
        pass
    assert_that(tok not in calc_src, f"Banned registry-duplicating literal in calculator: {tok}")

# =============================================================================
# BLOCK 9 — WIRED-PAPER ASSERTIONS (grows with the campaign, one block per band)
# =============================================================================

# --- Band 1: PAPER_001-020 (GW foundation) ---
_r001 = C.calc('PAPER_001')['value']
assert_that(abs(_r001['D_total'] - 0.333) < 1e-12,
            "PAPER_001: D_total = 0.333 (paper damping chain 1*1*0.9*0.37)")
assert_that(abs(_r001['D_trz'] - 0.9) < 1e-15,
            "PAPER_001: D_TRZ = 1 - F_TRZ = 0.9 EXACT")
assert_that(abs(_r001['D_total'] - (1.0 - P.D_GW_EROSION)) / (1.0 - P.D_GW_EROSION) < 0.0011,
            "PAPER_001: D_total within 0.11% of primitive identity 1/3 (PAPER_2154)")
assert_that(abs(_r001['h_uqff_strain'] - 1.8041e-22) < 1e-25,
            "PAPER_001: h_UQFF = 1.8041e-22 strain")
assert_that(abs(_r001['snr_uqff'] - 10.8) < 0.02,
            "PAPER_001: SNR_UQFF = 10.8")
assert_that(abs(_r001['mismatch'] - 0.667) < 1e-12,
            "PAPER_001: mismatch = 0.667 (paper precision)")
assert_that(abs(_r001['B_NS_over_B_crit'] - 2.27e-10) < 0.01e-10,
            "PAPER_001: B_NS/B_crit = 2.27e-10 (negligible SCm damping)")
assert_that(C.wired_count() >= 1, "wired_count >= 1 (campaign started)")

_r002 = C.calc('PAPER_002')['value']
assert_that(abs(_r002['F_uqff'] - 0.5297) < 1e-12,
            "PAPER_002: F_UQFF = 0.5297 (paper headline; Q-001 OPEN)")
assert_that(abs(_r002['amplitude_reduction_pct'] - 47.03) < 0.05,
            "PAPER_002: 47.0% amplitude reduction")
assert_that(abs(_r002['A_scm_scenarios']['extreme_magnetar_3.36e13G'] - 0.5581) < 5e-4,
            "PAPER_002: extreme magnetar A_SCm = 0.558 COMPUTED from stated formula "
            "(paper's table says 0.998871, back-solves to B_crit=1e15 G — Q-003 OPEN)")
assert_that(_r002['A_scm_scenarios']['hyper_magnetar_1e15G'] < 1e-200,
            "PAPER_002: hyper-magnetar A_SCm -> 0 (complete suppression)")
assert_that(_r002['A_scm_scenarios']['normal_pulsar_1e8G'] > 0.999999999,
            "PAPER_002: normal pulsar A_SCm = 1.0 (B << B_crit)")
assert_that(abs(_r002['p_ns'] + _r002['p_bh'] - 1.0) < 1e-12,
            "PAPER_002: P(NS) + P(BH) = 1")
assert_that(C.wired_count() >= 2, "wired_count >= 2")

_r003 = C.calc('PAPER_003')['value']
assert_that(abs(_r003['D_total'] - 0.333) < 1e-12,
            "PAPER_003: D_total = 0.333 (universal BBH chain, same as PAPER_001)")
assert_that(abs(_r003['h_uqff_peak'] - 4.1622e-22) < 1e-25,
            "PAPER_003: h_UQFF peak = 4.1622e-22")
assert_that(abs(_r003['snr_uqff'] - 8.0) < 0.01,
            "PAPER_003: SNR_UQFF = 8.0 (at detection threshold)")
assert_that(abs(_r003['distance_apparent_mpc'] - 1231.0) < 1.0,
            "PAPER_003: apparent distance 1231 Mpc (3x bias vs true 410)")
assert_that(abs(_r003['distance_bias_factor'] - 3.003) < 0.01,
            "PAPER_003: distance bias factor 3.0x")
assert_that(C.wired_count() >= 3, "wired_count >= 3")

# =============================================================================
# REPORT
# =============================================================================
if FAILURES:
    print(f"[FIDELITY GATE] {len(FAILURES)} FAILURES:")
    for f in FAILURES:
        print(f"  - {f}")
    sys.exit(1)
else:
    print(f"[FIDELITY GATE] OK - all assertions passed (Star-Magic-Program v{C.VERSION})")
    sys.exit(0)
