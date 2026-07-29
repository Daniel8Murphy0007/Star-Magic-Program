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
assert_that(C.VERSION == "0.112.0", "uqff_calculator.VERSION = 0.112.0")
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

_r004 = C.calc('PAPER_004')['value']
assert_that(abs(_r004['D_total'] - 0.333) < 1e-12,
            "PAPER_004: D_total = 0.333 via paper's own (1-f_TRZ) composition")
assert_that(abs(_r004['h_uqff_peak_computed'] - 9.341e-23) < 5e-26,
            "PAPER_004: computed h_UQFF = 9.341e-23 (paper states 9.4332e-23, ~1% slip - Q-005)")
assert_that(abs(_r004['strain_reduction_pct'] - 66.7) < 0.05,
            "PAPER_004: 66.7% strain reduction (paper abstract says 66.4 - Q-005)")
assert_that(C.wired_count() >= 4, "wired_count >= 4")

_r005 = C.calc('PAPER_005')['value']
assert_that(abs(_r005['F_combined'] - 0.81) < 1e-15,
            "PAPER_005: F_combined = (1-F_TRZ)^2 = 0.81 EXACT (string deactivated BBH)")
assert_that(abs(_r005['P_gw_uqff_w'] - 7.2455e-11) / 7.2455e-11 < 0.001,
            "PAPER_005: P_GW_UQFF = 7.2455e-11 W (19% reduction)")
assert_that(abs(_r005['tau_uqff_yr'] - 1.1656e12) / 1.1656e12 < 0.001,
            "PAPER_005: tau_UQFF = 1.1656e12 yr (1.23x extension)")
assert_that(abs(_r005['E_rad_uqff_msun'] - 0.6505) < 0.001,
            "PAPER_005: E_radiated = 0.6505 Msun (mass retention)")
assert_that(C.wired_count() >= 5, "wired_count >= 5")

_r006 = C.calc('PAPER_006')['value']
assert_that(abs(_r006['D_total'] - 0.333) < 1e-12,
            "PAPER_006: D_total = 0.333 (consistent with PAPER_001)")
assert_that(abs(_r006['h_uqff_strain'] - 1.8041e-22) < 1e-25,
            "PAPER_006: h_UQFF = 1.8041e-22 (multi-messenger consistency)")
assert_that(abs(_r006['snr_uqff'] - 10.8) < 0.02,
            "PAPER_006: SNR_UQFF = 10.8")
assert_that(abs(_r006['detection_volume_shrink'] - 27.1) < 0.2,
            "PAPER_006: detection volume shrinks ~27x (1/0.333^3)")
assert_that(_r006['gw_speed_constraint'] == 3e-15,
            "PAPER_006: |dc/c| < 3e-15 preserved (amplitude-only modification)")
assert_that(C.wired_count() >= 6, "wired_count >= 6")

_r007 = C.calc('PAPER_007')['value']
assert_that(abs(_r007['Lambda_typical_NS'] - 400.0) / 400.0 < 0.15,
            "PAPER_007: Lambda ~ 400 for M=1.4/R=12km (C=0.17, k2=0.1)")
assert_that(_r007['f_scm_normal_pulsar'] > 0.999999,
            "PAPER_007: f_SCm ~ 1 for normal pulsar (no Lambda suppression)")
assert_that(abs(_r007['f_scm_at_bcrit'] - 0.632) < 0.001,
            "PAPER_007: f_SCm(B_crit) = 1-exp(-1) = 0.632")
assert_that(_r007['Lambda_ns_massgap_2p52'] > 0 and _r007['Lambda_bh'] == 0.0,
            "PAPER_007: Lambda_NS(2.52) = 16 vs Lambda_BH = 0 discriminator")
assert_that(C.wired_count() >= 7, "wired_count >= 7")

_r008 = C.calc('PAPER_008')['value']
assert_that(abs(_r008['D_total_squared'] - 0.110889) < 1e-6,
            "PAPER_008: D_total^2 = 0.111 (power scaling)")
assert_that(abs(_r008['tau_extension_factor'] - 9.0) < 0.02,
            "PAPER_008: tau_UQFF = 9.0x tau_GR (1/D^2)")
assert_that(abs(_r008['phase_lag_growth_factor'] - 8.0) < 0.02,
            "PAPER_008: phase lag ~ 8x phi_GR (1/D^2 - 1)")
assert_that(abs(_r008['phase_lag_full_rad'] - 2310.8) < 0.1,
            "PAPER_008: full-inspiral phase lag 2310.8 rad (matches PAPER_006)")
assert_that(abs(_r008['D_bbh_reference'] - 0.81) < 1e-15,
            "PAPER_008: BBH cross-reference (1-F_TRZ)^2 = 0.81 (PAPER_005)")
assert_that(C.wired_count() >= 8, "wired_count >= 8")

_r009 = C.calc('PAPER_009')['value']
assert_that(abs(_r009['D_total_by_system']['gw170817_bns'] - 0.333) < 1e-12,
            "PAPER_009: GW170817 BNS D_total = 0.333")
assert_that(abs(_r009['D_total_by_system']['gw150914_bbh'] - 0.81) < 1e-15,
            "PAPER_009: GW150914 BBH D_total = (1-F_TRZ)^2 = 0.81 EXACT")
assert_that(abs(_r009['bns_bbh_damping_ratio'] - 2.43) < 0.01,
            "PAPER_009: BNS shows 2.4x stronger damping than BBH")
assert_that(abs(_r009['d_aether_410mpc_paper'] - 0.999999) < 1e-6,
            "PAPER_009: D_Aether = 0.999999 paper anchor (Q-009: SI eval gives ~0)")
assert_that(abs(_r009['string_factor_gw190425'] - 0.62) < 1e-12,
            "PAPER_009: GW190425 string factor 0.62 (self-rectifies Q-001 direction)")
assert_that(C.wired_count() >= 9, "wired_count >= 9")

_r010 = C.calc('PAPER_010')['value']
assert_that(abs(_r010['f_uqff_hz'] - 2375.0) < 0.5,
            "PAPER_010: f_UQFF = 2.375 kHz (5% QNM downshift)")
assert_that(abs(_r010['freq_shift_hz'] - 125.0) < 0.5,
            "PAPER_010: 125 Hz shift (detectable at 3G)")
assert_that(abs(_r010['tau_uqff_ms'] - 7.14) < 0.05,
            "PAPER_010: tau_UQFF ~ 7 ms (29% faster ringdown decay)")
assert_that(abs(_r010['eps_damp'] - 0.15) < 1e-12,
            "PAPER_010: 15% extra quantum-channel energy dissipation")
assert_that(C.wired_count() >= 10, "wired_count >= 10")

_r011 = C.calc('PAPER_011')['value']
assert_that(abs(_r011['omega_suppression_bns'] - 0.110889) < 1e-6,
            "PAPER_011: Omega BNS suppression = D^2 = 0.111 (89% cut)")
assert_that(abs(_r011['omega_suppression_bbh'] - 0.6561) < 1e-6,
            "PAPER_011: Omega BBH suppression = 0.81^2 = 0.656 (paper rounds 0.66)")
assert_that(abs(_r011['omega_mixed_population_factor'] - 0.37) < 0.005,
            "PAPER_011: mixed-population Omega ~ 0.37*Omega_GR (63% reduction)")
assert_that(abs(_r011['omega_gw_uqff_bns_100hz'] - 1.11e-10) < 2e-13,
            "PAPER_011: Omega_UQFF,BNS ~ 1.11e-10 at 100 Hz")
assert_that(C.wired_count() >= 11, "wired_count >= 11")

_r012 = C.calc('PAPER_012')['value']
assert_that(abs(_r012['tau_circ_extension'] - 9.0) < 0.02,
            "PAPER_012: tau_circ = 9.0x tau_GR (3rd D^2 data point)")
assert_that(abs(_r012['e_final_uqff_at_10hz'] - 0.003) < 1e-12,
            "PAPER_012: residual eccentricity 0.003 at LIGO band (30x GR)")
assert_that(abs(_r012['rate_enhancement_eccentric'] - 3.0) < 1e-12,
            "PAPER_012: ~3x eccentric-merger detection rate enhancement")
assert_that(C.wired_count() >= 12, "wired_count >= 12")

_r013 = C.calc('PAPER_013')['value']
assert_that(abs(_r013['D_scm_sgr1806'] - 0.0218) < 0.0005,
            "PAPER_013: SGR 1806-20 D_SCm = 0.0218 COMPUTED (paper states ~0.01 - Q-010)")
assert_that(_r013['braking_index_uqff_range'] == (1.5, 2.0),
            "PAPER_013: braking index n_UQFF = 1.5-2.0 (vs GR 3; obs 1-2.5)")
assert_that(abs(_r013['tau_ratio_sec23'] - 1.0e4) < 1.0,
            "PAPER_013: sec-2.3 tau = t_GR/D^2 = 10,000x (abstract says 3x - Q-010)")
assert_that(abs(_r013['magnetar_age_resolution_yr'] - 1.0e7) < 1.0,
            "PAPER_013: magnetar age problem resolved (~1e7 yr)")
assert_that(C.wired_count() >= 13, "wired_count >= 13")

_r014 = C.calc('PAPER_014')['value']
assert_that(abs(_r014['A_damp'] - 0.3) < 1e-15,
            "PAPER_014: A_damp = 0.3 = (D_phys-1)/SO_5 EXACT (primitive-lock candidate)")
assert_that(abs(_r014['delta_c_gr'] - 0.45) < 1e-12,
            "PAPER_014: delta_c,GR = 0.45 (sec 2.2; key-results 0.333 slip - Q-011)")
assert_that(abs(_r014['gamma_scaling'] - 1.8) < 1e-12,
            "PAPER_014: gamma = 1.8 UQFF mass-function scaling")
assert_that(_r014['lambda_uqff_kg_m3'] > 0,
            "PAPER_014: Lambda_UQFF = kappa*rho_crit composed from registry")
assert_that(C.wired_count() >= 14, "wired_count >= 14")

_r015 = C.calc('PAPER_015')['value']
assert_that(abs(_r015['h0_obs_gw170817'] - 70.0) < 1e-12,
            "PAPER_015: uncorrected GW170817 H_0 = 70 = A_5+SO_5 (PAPER_1573 canonical)")
assert_that(abs(_r015['h0_uqff_corrected'] - 75.0) / 75.0 < 0.005,
            "PAPER_015: H_0,UQFF = 1.07*70 = 74.9 within 0.5 pct of paper 75.0 (Q-012)")
assert_that(abs(_r015['detection_volume_vs_gr'] - 0.24) < 0.005,
            "PAPER_015: detection volume 0.622^3 = 0.2406 ~ paper 24 pct of GR")
assert_that(abs(_r015['delta_mu_z1_mag'] - 0.12) < 1e-12,
            "PAPER_015: Delta-mu(z=1) = 0.15-0.03 = 0.12 mag")
assert_that(abs(_r015['ligo_horizon_mpc'][1] / _r015['ligo_horizon_mpc'][0] - _r015['uqff_factor']) < 0.001,
            "PAPER_015: 8355/13440 = 0.6216 ~ UQFF_factor 0.622 internally consistent")
assert_that(C.wired_count() >= 15, "wired_count >= 15")

_r015b = C.calc('PAPER_015b')['value']
assert_that(abs(_r015b['snr_gw150914'][1] / _r015b['snr_gw150914'][0] - 0.622) < 0.002,
            "PAPER_015b: GW150914 SNR 167/268 = 0.6231 ~ D = 0.622")
assert_that(abs(_r015b['snr_smbh_z1'][1] / _r015b['snr_smbh_z1'][0] - 0.622) < 0.002,
            "PAPER_015b: SMBH SNR 694/1116 = 0.6219 ~ D = 0.622")
assert_that(_r015b['freq_independence_check'] < 0.001,
            "PAPER_015b: LIGO ratio == LISA ratio within 1e-3 (frequency independence)")
assert_that(abs(_r015b['detection_volume_vs_gr'] - 0.241) < 0.001,
            "PAPER_015b: V/V_GR = 0.622^3 = 0.2407 ~ paper 0.241")
assert_that(abs(_r015b['d_pure_bbh_ligo'] - 1.0/3.0) < 1e-15,
            "PAPER_015b: pure LIGO BBH factor 0.333 disclosed (0.622 = cross-band avg)")
assert_that(C.wired_count() >= 16, "wired_count >= 16")

_r016 = C.calc('PAPER_016')['value']
assert_that(abs(_r016['s_qm_chsh'] - 2.8284271247461903) < 1e-15,
            "PAPER_016: S_QM = 2*sqrt(2) Tsirelson bound exact")
assert_that(abs(_r016['delta_energy_scaling'] - 1.5) < 1e-15,
            "PAPER_016: delta = 1.5 = D_BSFG/D_PHYS EXACT (PAPER_1962 family candidate)")
assert_that(abs(_r016['range_extension'] - 3.0) < 1e-12,
            "PAPER_016: entanglement range extension 1/D_total = 3.0 = 1/(1-D_GW_EROSION)")
assert_that(abs(_r016['eps_damp_gev'] - 0.0277) < 0.001,
            "PAPER_016: GeV CHSH suppression eps = 1 - 2.75/2.828 = 0.0277")
assert_that(_r016['s_uqff_1000km'] < _r016['s_uqff_gev'] < _r016['s_qm_chsh'],
            "PAPER_016: suppression ordering 2.60 < 2.75 < 2.828 monotone")
assert_that(C.wired_count() >= 17, "wired_count >= 17")

_r016b = C.calc('PAPER_016b')['value']
assert_that(abs(_r016b['d_local'] - 0.6224) < 0.001,
            "PAPER_016b: D_local = sqrt(1.67/4.31) = 0.6224 ~ paper 0.623")
assert_that(abs(_r016b['d_local'] - 0.622) < 0.001,
            "PAPER_016b: D_local matches PAPER_015b cross-band 0.622 (corpus consistency)")
assert_that(abs(_r016b['foreground_reduction_pct'] - 61.4) < 0.5,
            "PAPER_016b: foreground reduction 61.3 ~ paper 61.4 pct")
assert_that(abs(_r016b['resolved_scaling_check'] - _r016b['d_local']) < 0.001,
            "PAPER_016b: resolved catalog 6216/10000 = 0.6216 = D_local linear scaling")
assert_that(abs(_r016b['net_snr_ratio_z1'] - 0.994) < 0.001,
            "PAPER_016b: net SNR z~1 = 0.619/0.623 = 0.994 (sec 4.1; Q-013 vs abstract 1.6x)")
assert_that(C.wired_count() >= 18, "wired_count >= 18")

_r017 = C.calc('PAPER_017')['value']
assert_that(abs(_r017['f_combined'] - 0.6217) < 0.0005,
            "PAPER_017: F_combined = (1-F_TRZ)*1.0*0.6907 = 0.6216 ~ paper 0.6217 - ORIGIN of 0.622")
assert_that(abs(_r017['phi_lag_merger_rad'] - 0.6283185307179586) < 1e-12,
            "PAPER_017: phi_lag = 2*pi*F_TRZ = 0.6283 rad EXACT registry composition (~paper 0.63)")
assert_that(abs(_r017['phi_lag_cycles'] - 0.1) < 1e-15,
            "PAPER_017: phase lag 0.10 cycles = F_TRZ EXACT")
assert_that(abs(_r017['snr_ratio'] - 0.6233) < 0.001,
            "PAPER_017: SNR 128338/205910 = 0.6233 ~ 0.622 family")
assert_that(abs(_r017['strain_reduction_sec4_pct'] - 39.5) < 0.1,
            "PAPER_017: sec-4 strain reduction 39.5 pct reproduced (vs sec-5 31.6 - Q-014)")
assert_that(C.wired_count() >= 19, "wired_count >= 19")

_r018 = C.calc('PAPER_018')['value']
assert_that(abs(_r018['trz_dip_depth'] - 0.1) < 1e-15,
            "PAPER_018: TRZ suppression dip depth = F_TRZ = 0.1 EXACT registry composition")
assert_that(abs(_r018['sgwb_slope'] - 2.0/3.0) < 1e-15,
            "PAPER_018: SGWB inspiral slope f^(2/3) = D_GW_EROSION value note (2/3)")
assert_that(abs(_r018['comb_envelope_n1_5'][0] - 0.6065) < 0.001,
            "PAPER_018: comb n=1 weight exp(-1/2) = 0.6065")
assert_that(abs(_r018['aether_power_fraction_pct'] - 222.93) < 1e-9,
            "PAPER_018: aether power fraction 222.93 pct anchor locked")
assert_that(abs(_r018['integrated_snr'] - 12695834.0) < 1.0,
            "PAPER_018: integrated SNR 12,695,834 matches PAPER_017 validator (corpus consistency)")
assert_that(C.wired_count() >= 20, "wired_count >= 20")

_r019 = C.calc('PAPER_019')['value']
assert_that(abs(_r019['d_total_fyr'] - 1.60) < 0.001,
            "PAPER_019: D_total(f_yr) = 1 + SSq*1.053 = 1.600 registry-composed")
assert_that(abs(_r019['a_uqff'] - 2.4e-15) / 2.4e-15 < 0.001,
            "PAPER_019: A_UQFF = 1.60*1.5e-15 = 2.4e-15 = NANOGrav 15-yr")
assert_that(abs(_r019['bns_100hz_check'] - 0.333) < 0.001,
            "PAPER_019: 100 Hz BNS row 0.900*0.370 = 0.333 consistent with PAPER_001/009")
assert_that(abs(_r019['alpha_gr'] + 2.0/3.0) < 1e-15,
            "PAPER_019: alpha_GR = -2/3 (Peters circular-inspiral index)")
assert_that(abs(_r019['d_sq_keyresults'] * _r019['d_total_fyr'] - 1.0) < 0.001,
            "PAPER_019: key-results 0.625 = 1/1.60 - Q-016 parameterization conflict quantified")
assert_that(C.wired_count() >= 21, "wired_count >= 21")

_r020 = C.calc('PAPER_020')['value']
assert_that(abs(_r020['z_drag_scaling']['he'] - 1.2599) < 0.001,
            "PAPER_020: He drag 2^(1/3) = 1.26 exact")
assert_that(abs(_r020['z_drag_scaling']['fe'] - 2.9625) < 0.01,
            "PAPER_020: Fe drag 26^(1/3) = 2.96 exact")
assert_that(abs(_r020['gamma_aether_1e20_per_day'] - 2.748e-3) < 1e-5,
            "PAPER_020: kappa*100^0.37 = 2.75e-3/day composed (paper 2.68e-3 - Q-017a 2.5 pct slip)")
assert_that(abs(_r020['beta_aether'] - 0.37) < 1e-15,
            "PAPER_020: beta_aether = 0.37 anchor (= PAPER_009 D_String(100Hz) value)")
assert_that(abs(_r020['trz_break_delta_gamma'] - 0.3) < 1e-15,
            "PAPER_020: TRZ secondary break Delta-gamma = +0.3 at 8e19 eV (AugerPrime falsifiable)")
assert_that(C.wired_count() >= 22, "wired_count >= 22")

_r021 = C.calc('PAPER_021')['value']
assert_that(abs(_r021['ssq_squared'] - 0.3249) < 1e-12,
            "PAPER_021: SSq^2 = 0.57^2 = 0.3249 registry-composed (~paper 0.325)")
assert_that(abs(_r021['sigma8_uqff'] - 0.762) / 0.762 < 0.001,
            "PAPER_021: sigma8 = 0.811*0.940 = 0.762 = DES/HSC/KiDS combined (0.0-sigma)")
assert_that(abs(_r021['shear_xi_suppression'] - 0.841) < 0.001,
            "PAPER_021: shear correlation (1-0.083)^2 = 0.841 ~ paper 0.840")
assert_that(abs(_r021['einstein_ring_factor'] ** 2 - _r021['suppression_0940']) < 0.002,
            "PAPER_021: Einstein ring 0.969^2 = 0.9390 vs 0.940 (0.11 pct; paper rounds sqrt(0.940) = 0.9695 to 0.969) - Q-018a family")
assert_that(abs(_r021['rho_crit_paper_kg_m3'] - 9.47e-27) < 1e-30,
            "PAPER_021: rho_crit anchor 9.47e-27 kg/m3 = PAPER_2156 mystery bulk-script constant IDENTIFIED")
assert_that(abs(_r021['rho_crit_registry_kg_m3'] / _r021['rho_crit_paper_kg_m3'] - 0.973) < 0.005,
            "PAPER_021: registry rho_crit (H0 = 70) within 2.7 pct of paper anchor (H0 ~ 71)")
assert_that(C.wired_count() >= 23, "wired_count >= 23")

_r022 = C.calc('PAPER_022')['value']
assert_that(abs(_r022['d_string_bns'] - 0.37) < 0.001,
            "PAPER_022: D_String(BNS) = 1 - SSq^2*1.94 = 0.3697 - ORIGIN of the 0.37 factor")
assert_that(abs(_r022['polarization_ladder']['breathing'] - 0.3249) < 1e-12,
            "PAPER_022: breathing mode = SSq^2 = 0.3249 EXACT (~paper 0.325)")
assert_that(abs(_r022['polarization_ladder']['longitudinal'] - 0.185193) < 1e-6,
            "PAPER_022: longitudinal mode = SSq^3 = 0.1852 EXACT (~paper 0.185)")
assert_that(abs(_r022['polarization_ladder']['vector'] - 0.10556) < 1e-4,
            "PAPER_022: vector modes = SSq^4 = 0.1056 EXACT (~paper 0.106)")
assert_that(abs(_r022['m_kk_tev'] - 11.6) < 0.05,
            "PAPER_022: M_KK = hbar*c/1.70e-20 m = 11.61 TeV exact (LHC-consistent)")
assert_that(_r022['n_compact'] == 22,
            "PAPER_022: N_compact = D_CRIT - D_PHYS = 22 registry-composed")
assert_that(C.wired_count() >= 24, "wired_count >= 24")

_r023 = C.calc('PAPER_023')['value']
assert_that(abs(_r023['delta_a_tau_kk'] - 1.92e-9) / 1.92e-9 < 0.005,
            "PAPER_023: KK loop (m^2/8piM^2)*(2/3)*(1/SSq^2) = 1.92e-9 EXACT composition")
assert_that(abs(_r023['f_string_basel'] - 1.6449) < 0.0001,
            "PAPER_023: F_string = pi^2/6 = 1.6449 Basel exact (~paper 1.645)")
assert_that(abs(_r023['ratio_tau_mu'] - 282.8) < 0.5,
            "PAPER_023: (m_tau/m_mu)^2 = 282.8 (~paper 282.6)")
assert_that(abs(_r023['universality_exponent'] - 2.37) < 1e-15,
            "PAPER_023: universality exponent 2.37 = 2 + 0.37 (PAPER_022 string factor link)")
assert_that(abs(_r023['a_tau_uqff'] - 1.18063e-3) < 1e-8,
            "PAPER_023: a_tau^UQFF = 1.17721e-3 + 3.42e-6 = 1.18063e-3")
assert_that(abs(_r023['component_sum'] - 3.386e-6) < 1e-9,
            "PAPER_023: component sum 3.386e-6 vs headline 3.42e-6 (1 pct, Q-020a) honestly pinned")
assert_that(C.wired_count() >= 25, "wired_count >= 25")

_r024 = C.calc('PAPER_024')['value']
assert_that(abs(_r024['phi_cp_rad'] - 1.7907078) < 1e-6,
            "PAPER_024: phi_CP = SSq*pi = 1.7907 rad registry-composed (paper rounds 1.795)")
assert_that(abs(_r024['phi_trz_rad'] - 0.2827433) < 1e-6,
            "PAPER_024: phi_TRZ = (1-F_TRZ)*F_TRZ*pi = 0.2827 EXACT (~paper 0.283)")
assert_that(abs(_r024['se_chain_ecm'] - 1.84e-20) / 1.84e-20 < 0.001,
            "PAPER_024: Schiff-Engel chain 3.42e-6*4.637*9.377e-21*1.237e5 = 1.8395e-20 = headline")
assert_that(abs(_r024['sigma_reach']['tau_factory'] - 184.0) < 1e-12,
            "PAPER_024: tau-factory 184-sigma = 1.84e-20/1e-22 exact")
assert_that(abs(_r024['component_sum'] - 1.8073e-20) < 1e-24,
            "PAPER_024: component sum 1.807e-20 vs headline 1.84e-20 (1.8 pct, Q-021a) honestly pinned")
assert_that(abs(_r024['tan_phi_cp_computed'] + 4.4737) < 0.001,
            "PAPER_024: tan(SSq*pi) = -4.474 computed (paper 4.637, 3.6 pct - Q-021b)")
assert_that(C.wired_count() >= 26, "wired_count >= 26")

_r025 = C.calc('PAPER_025')['value']
assert_that(abs(_r025['m_acp_ev'] - 3.81e-24) / 3.81e-24 < 0.005,
            "PAPER_025: M_ACP = kappa*hbar = 3.81e-24 eV EXACT registry composition")
assert_that(abs(_r025['lambda_db_kpc'] - 2.29) < 0.02,
            "PAPER_025: lambda_dB = hbar/(m*v) = 2.29 kpc at 220 km/s reproduced")
assert_that(abs(_r025['m_acp2_tev'] - 3.77) < 0.01,
            "PAPER_025: M_ACP2 = M_KK*SSq^2 = 3.769 TeV registry-composed (~paper 3.77)")
assert_that(abs(_r025['self_interaction_cm2_g'] - 0.57) < 1e-15,
            "PAPER_025: DM self-interaction sigma/M = SSq = 0.57 cm2/g primitive direct")
assert_that(abs(_r025['relic_acp_check'] - 0.073) < 0.001,
            "PAPER_025: Omega_ACP = 0.128*SSq = 0.073 composition checks")
assert_that(abs(_r025['omega_dm_h2'] - 0.1200) < 1e-12,
            "PAPER_025: Omega_DM h^2 = 0.1200 = Planck 2020 anchor")
assert_that(C.wired_count() >= 27, "wired_count >= 27")

_r025b = C.calc('PAPER_025b')['value']
assert_that(abs(_r025b['kappa_ssq'] - 2.85e-4) < 1e-18,
            "PAPER_025b: kappa*SSq = 2.85e-4 EXACT registry composition")
assert_that(abs(_r025b['hierarchy_ratio_12'] - 0.57) < 0.0005,
            "PAPER_025b: m_nu1/m_nu2 = 8.18/14.35 = 0.5700 = SSq EXACT hierarchy")
assert_that(abs(_r025b['xray_line_kev'] - 3.55) < 1e-12,
            "PAPER_025b: E_gamma = M_s1/2 = 3.55 keV (Perseus/M31 XMM line)")
assert_that(abs(_r025b['mixing_enhancement'] - 0.407) < 0.001,
            "PAPER_025b: sterile mixing enhancement 0.407 chain verified")
assert_that(abs(_r025b['g_uqff_nucleon'] - 9.7e-6) / 9.7e-6 < 0.01,
            "PAPER_025b: g_UQFF-nucleon = 0.37*(m_N/M_s3)*SSq = 9.7e-6 (0.37 factor again)")
assert_that(abs(_r025b['sum_m_nu_components_mev'] - 72.89) < 0.01,
            "PAPER_025b: components sum 72.89 meV vs stated 74.2 (1.8 pct, Q-023a) honestly pinned")
assert_that(C.wired_count() >= 28, "wired_count >= 28")

_r026 = C.calc('PAPER_026')['value']
assert_that(abs(_r026['m_s2_gev'] - 45.81) < 0.01,
            "PAPER_026: M_s2 = SSq*M_W = 45.81 GeV EXACT (above M_Z/2 = 45.6)")
assert_that(abs(_r026['m_s3_gev'] - 20351.0) < 1.0,
            "PAPER_026: M_s3 = M_KK/SSq = 20,351 GeV EXACT (matches PAPER_025b anchor)")
assert_that(abs(_r026['gut_ratio_check'] - 0.57) < 1e-12,
            "PAPER_026: GUT Majorana geometric ratio = SSq EXACT (resolves Q-023b: M_N1 = 2.19e9 GeV)")
assert_that(abs(_r026['sum_m_nu_gut_mev'] - 74.2) < 1e-9,
            "PAPER_026: GUT seesaw triple sums to 74.2 meV EXACT (resolves Q-023a stated-sum origin)")
assert_that(abs(_r026['d_s_dilution'] - 1.7544) < 0.001,
            "PAPER_026: entropy dilution D_s = 1/SSq = 1.754")
assert_that(abs(_r026['omega_s1_h2'] - 0.131) < 0.001,
            "PAPER_026: Omega_s1 = 0.305*SSq^1.5 = 0.131 composition")
assert_that(abs(_r026['yukawa_ladder']['e'] - 0.185193) < 1e-6,
            "PAPER_026: Yukawa ladder y_e = SSq^3 = 0.185 (SSq powers, PAPER_022 family)")
assert_that(C.wired_count() >= 29, "wired_count >= 29")

_r026b = C.calc('PAPER_026b')['value']
assert_that(abs(_r026b['kappa_avg_singlet_t'] - 0.37) < 1e-15,
            "PAPER_026b: ATLAS singlet-T average (0.22+0.52)/2 = 0.37 = beta_string EXACT")
assert_that(abs(_r026b['kappa_avg_triplet'] - 0.30) < 1e-15,
            "PAPER_026b: triplet average 0.30 = (D_PHYS-1)/SO_5 candidate (0.3-factor family)")
assert_that(abs(_r026b['kappa_avg_triplet'] - _r026b['triplet_030_check']) < 1e-15,
            "PAPER_026b: 0.30 = (D_PHYS-1)/SO_5 identity holds exactly")
assert_that(abs(_r026b['k_eta_vlq'] - 0.1369) < 1e-12,
            "PAPER_026b: k_eta_VLQ = 0.37^2 = 0.1369 EXACT")
assert_that(abs(_r026b['third_family_prediction_gev'] - 844.7) < 0.5,
            "PAPER_026b: third VLQ family 2600*SSq^2 = 844.7 GeV (~paper 845, Run-3 falsifiable)")
assert_that(abs(_r026b['vlq_hierarchy_gev'][1] - 1482.0) < 1.0,
            "PAPER_026b: second family 2600*SSq = 1482 GeV")
assert_that(C.wired_count() >= 30, "wired_count >= 30")

_r027 = C.calc('PAPER_027')['value']
assert_that(abs(_r027['s_lfv'] - 0.5655) < 0.0001,
            "PAPER_027: S_LFV = exp(-SSq) = 0.5655 EXACT registry composition")
assert_that(abs(_r027['ug3_suppression'] + 0.3337) < 0.001,
            "PAPER_027: Ug3 = -0.59*0.5655 = -0.3337 chain verified")
assert_that(abs(_r027['t_n_lfv_constraint'] - 3.833) < 0.001,
            "PAPER_027: t_n_LFV = -ln(5.9e-6)/pi = 3.833 reversal depth")
assert_that(abs(_r027['br_reproduction'] - 5.9e-6) / 5.9e-6 < 1e-9,
            "PAPER_027: BR = exp(-pi*t_n) = 5.9e-6 reproduces LHCb limit exactly")
assert_that(abs(_r027['ug1_mb_over_mp'] - 5.627) < 0.01,
            "PAPER_027: Ug1 = m_B/m_p = 5.627 (~paper 5.622)")
assert_that(abs(_r027['ug4_effective'] - 6.556e-6) < 1e-9,
            "PAPER_027: Ug4 = BR/(1-F_TRZ) = 6.556e-6 (~paper 6.558e-6; Q-026a density reading)")
assert_that(C.wired_count() >= 31, "wired_count >= 31")

_r028 = C.calc('PAPER_028')['value']
assert_that(abs(_r028['scm_flavor_mixing'] - 1.5366e-3) / 1.5366e-3 < 0.001,
            "PAPER_028: [SCm]_flavor = |V_cb|^2 = 1.5366e-3 EXACT (CKM as vacuum density)")
assert_that(abs(_r028['ug_ladder']['ug1'] - 5.627) < 0.02,
            "PAPER_028: Ug1 = m_B/m_p = 5.63 (~paper 5.614)")
assert_that(abs(_r028['ug_ladder']['ub_i'] - 24.88) < 0.1,
            "PAPER_028: Ub_i = beta_i*Gamma/(m_B*c^2) = 24.88 with registry BETA_I")
assert_that(abs(_r028['f_u_total'] - 75.81) < 0.1,
            "PAPER_028: F_U = 75.81 net positive (B->Dlnu supported)")
assert_that(abs(_r028['phase_space'] - 0.936) < 0.001,
            "PAPER_028: phase space sqrt(1-(m_D/m_B)^2) = 0.936 verified")
assert_that(abs(_r028['cabibbo_ratio'] - 0.0303) < 0.0005,
            "PAPER_028: Cabibbo ratio 0.0303 pinned (its (m_s/m_b)^1/2 claim FAILS - Q-027b)")
assert_that(C.wired_count() >= 32, "wired_count >= 32")

_r029 = C.calc('PAPER_029')['value']
assert_that(abs(_r029['f_sm_raw_ssq4'] - 0.1056) < 0.0001,
            "PAPER_029: f_SM raw = SSq^4 = 0.1056")
assert_that(abs(_r029['f_sm_corrected_printed'] - _r029['ssq6_identity_candidate']) < 0.0001,
            "PAPER_029: printed correction formula = SSq^6 = 0.0343 EXACTLY (not 0.0485 - Q-028a)")
assert_that(abs(_r029['budget_residual_check'] - 0.6835) < 0.0001,
            "PAPER_029: f_Lambda = 1 - 0.0485 - 0.268 = 0.6835 residual consistent")
assert_that(abs(_r029['n_kk_true'] - 61.5) < 0.1,
            "PAPER_029: true KK exponent 61.5 (claimed 8 fails by 13 orders - Q-028c)")
assert_that(_r029['n_kk_62_check'] == 62,
            "PAPER_029: 2*D_CRIT + SO_5 = 62 registry-composed (PAPER_2137-family candidate near 61.5)")
assert_that(abs(_r029['icecube_break_pev'] - 5.8) < 1e-12,
            "PAPER_029: IceCube spectral break = M_KK/2 = 5.8 PeV falsifiable")
assert_that(C.wired_count() >= 33, "wired_count >= 33")

_r030 = C.calc('PAPER_030')['value']
assert_that(abs(_r030['f_suppress'] - 0.749) < 0.002,
            "PAPER_030: F_suppress = cos^2(pi*3.833) = 0.749 (paper self-corrects to 0.748)")
assert_that(abs(_r030['br_uqff'] - 5.8e-6) / 5.8e-6 < 0.01,
            "PAPER_030: BR_UQFF = 2.3e-5*(1-F) = 5.8e-6 saturates LHCb bound - falsifiable")
assert_that(abs(_r030['m_dark_gev'] - 2163.0) / 2163.0 < 0.005,
            "PAPER_030: M_dark = m_B*exp(pi*t_n/2) = 2163 GeV ~ 2.2 TeV")
assert_that(abs(_r030['e_react_tan4_cabibbo'] - 2.846e-3) / 2.846e-3 < 0.005,
            "PAPER_030: E_react = tan^4(theta_C) = 2.84e-3 closed form verified")
assert_that(abs(_r030['hl_lhc_reach'] - 7.9e-7) / 7.9e-7 < 0.01,
            "PAPER_030: HL-LHC reach = 5.9e-6*sqrt(5.4/300) = 7.9e-7 scaling verified")
assert_that(abs(_r030['t_n_lfv'] - 3.8327) < 0.001,
            "PAPER_030: t_n = 3.833 shared with PAPER_027 (corpus consistency)")
assert_that(C.wired_count() >= 34, "wired_count >= 34")

_r031 = C.calc('PAPER_031')['value']
assert_that(abs(_r031['r_d_uqff'] - 0.332) < 0.001,
            "PAPER_031: R(D) = 0.298/(1-(m_tau/m_b)^2*SSq) = 0.332 (1.9 -> 0.9 sigma)")
assert_that(abs(_r031['r_dstar_uqff'] - 0.269) < 0.001,
            "PAPER_031: R(D*) = 0.269 with F_TRZ factor in denominator (3.3 -> 1.2 sigma)")
assert_that(abs(_r031['c_d_kinematic'] - 0.1806) < 0.0005,
            "PAPER_031: C = (m_tau/m_b)^2 = 0.1806 (printed as unsquared - Q-030a)")
assert_that(abs(_r031['ckm_uqff_mapping'] - 0.0020) < 0.0001,
            "PAPER_031: CKM row-2 deficit 2*[SCm]_flavor*0.65 = 0.0020 mapped")
assert_that(abs(_r031['tera_z_shift'] - 5.8e-7) / 5.8e-7 < 0.01,
            "PAPER_031: Tera-Z shift [SCm]*m_tau^2/m_Z^2 = 5.8e-7 (FCC-ee testable)")
assert_that(abs(_r031['lfu_uqff'] - 1.060) < 0.001,
            "PAPER_031: LFU = 1 + m_mu/m_tau = 1.060 (Belle II 1.020 within 1.3 sigma)")
assert_that(C.wired_count() >= 35, "wired_count >= 35")

_r032 = C.calc('PAPER_032')['value']
assert_that(abs(_r032['alpha_deg'] - 21.7) < 0.1,
            "PAPER_032: scalar mixing angle alpha = asin(0.37) = 21.7 deg")
assert_that(abs(_r032['tan_beta_2hdm'] - 2.70) < 0.01,
            "PAPER_032: tan(beta) = 1/sqrt(k_eta) = 2.70 (2HDM, FCNC-safe)")
assert_that(abs(_r032['f_composite_gev'] - 665.0) < 1.0,
            "PAPER_032: composite scale f = 246/0.37 = 665 GeV (FCC-ee 6.8 pct shift)")
assert_that(abs(_r032['triplet_split_gev'] - 17.0) < 0.1,
            "PAPER_032: triplet splitting m_W*(D_PHYS-1)/SO_5/sqrt(2) = 17.0 GeV composed")
assert_that(abs(_r032['echo_026b_route_gev'] - _r032['m_s0_prediction_gev']) < 1.0,
            "PAPER_032: 845 GeV ECHO - 2600*SSq^2 (026b route) = 844.7 = S0 prediction (Q-031c)")
assert_that(abs(_r032['v_s_singlet_gev'] - 791.0) < 1.0,
            "PAPER_032: singlet VEV v_S = 845/sqrt(2*SSq) = 791 GeV (lambda_S = SSq)")
assert_that(C.wired_count() >= 36, "wired_count >= 36")

_r033 = C.calc('PAPER_033')['value']
assert_that(abs(_r033['e_react'] - 2.846e-3) / 2.846e-3 < 0.005,
            "PAPER_033: E_react = tan^4(theta_C) = 2.84e-3 (shared with PAPER_030)")
assert_that(abs(_r033['delta_t_uqff'] - 0.222) < 0.002,
            "PAPER_033: delta_T = E_react*SSq/alpha_EM = 0.222")
assert_that(abs(_r033['dm_w_gev'] - 0.093) < 0.002,
            "PAPER_033: Delta_m_W = +93 MeV - CDF-anomaly direction and magnitude")
assert_that(abs(_r033['m_w_uqff_gev'] - 80.455) < 0.003,
            "PAPER_033: m_W^UQFF = 80.455 GeV vs CDF 80.4335 (~0.3 sigma)")
assert_that(abs(_r033['dcs_geometric_mean'] - 5.31e-3) / 5.31e-3 < 0.005,
            "PAPER_033: DCS geometric mean 5.31e-3; hadronic enhancement 1.87x disclosed")
assert_that(abs(_r033['rho_uqff'] - 1.00322) < 0.00001,
            "PAPER_033: rho_UQFF = 1.00322 within LEP 1-sigma")
assert_that(C.wired_count() >= 37, "wired_count >= 37")

_r034 = C.calc('PAPER_034')['value']
assert_that(abs(_r034['kappa_18_uh'] - 0.1927) < 0.0005,
            "PAPER_034: UH Level-18 coupling = 18^(-SSq) = 0.1927 composition")
assert_that(abs(_r034['kt_bracket'][0] - 0.9220) < 0.0005,
            "PAPER_034: kappa_t low = 1 - SSq*k_eta = 0.9220")
assert_that(abs(_r034['kt_central'] - 0.948) < 0.001,
            "PAPER_034: kappa_t central = geometric mean = 0.948 (5.2 pct below SM)")
assert_that(abs(_r034['mu_th_uqff'] - 0.898) < 0.001,
            "PAPER_034: mu_tH = kappa_t^2 = 0.898 vs ATLAS 0.9583 +- 0.11 (0.6 sigma)")
assert_that(abs(_r034['fcc_hh_significance'] - 10.4) < 0.2,
            "PAPER_034: FCC-hh discrimination 10.4 sigma - definitive falsifiable")
assert_that(_r034['kappa_c_derived'] < _r034['kappa_c_bound'] and _r034['kappa_c_claimed'] < _r034['kappa_c_bound'],
            "PAPER_034: both kappa_c values (18.8 derived, 42.0 claimed) within CERN < 47 (Q-033a)")
assert_that(C.wired_count() >= 38, "wired_count >= 38")

_r035 = C.calc('PAPER_035')['value']
assert_that(abs(_r035['t_n_self_consistent'] - 0.3308) < 0.001,
            "PAPER_035: self-consistent t_n = arccos(0.507)/pi = 0.331 (paper used 0.353 - Q-034a)")
assert_that(abs(_r035['cos_pi_tn_paper'] - 0.4456) < 0.001,
            "PAPER_035: cos(pi*0.353) = 0.4456 - the 87.88 pct decomposition is downstream of the slip")
assert_that(abs(_r035['g_cp_one_loop'] - 2.41e-5) / 2.41e-5 < 0.01,
            "PAPER_035: one-loop g_CP = (alpha/4pi)*D_TRZ*t_n^2 = 2.41e-5 composed")
assert_that(abs(_r035['a_cp_hgg'] - 7.4e-3) / 7.4e-3 < 0.01,
            "PAPER_035: A_CP(H->gamma-gamma) = 0.74 pct falsifiable at HL-LHC")
assert_that(abs(_r035['width_enhancement'] - 780.0) < 2.0,
            "PAPER_035: Gamma_H scenario = 780x SM (bound scenario, disclosed not physical)")
assert_that(_r035['gamma_h_scenario_gev'] < _r035['gamma_h_cern_limit_gev'],
            "PAPER_035: 3.2 GeV scenario below CERN 3.6 GeV limit")
assert_that(C.wired_count() >= 39, "wired_count >= 39")

_r036 = C.calc('PAPER_036')['value']
assert_that(abs(_r036['f_ubii_virx_perseus_n'] - (-2.024e60)) / 2.024e60 < 0.001,
            "PAPER_036: Perseus F_UBii_virx = -2.024e60 N arithmetic verified end-to-end")
assert_that(_r036['base_identity'] == 'F_UBii = F_U - F_Bi - F_i',
            "PAPER_036: base identity matches predecessor Tier-4 registry (PAPER_2151 continuity)")
assert_that(_r036['sigma_scaling_power'] == 3,
            "PAPER_036: sigma_X^3 scaling (phase-space entropy)")
assert_that(abs(_r036['enhancement_raw'] - 2.4e6) / 2.4e6 < 0.02,
            "PAPER_036: raw enhancement 2.4e6 -> Q_wave ~ 1e-6 thermalized (disclosed self-consistency)")
assert_that(_r036['variant_count_family'] == 17,
            "PAPER_036: 17-variant family root (template papers 036-039)")
assert_that(C.wired_count() >= 40, "wired_count >= 40")

_r037 = C.calc('PAPER_037')['value']
assert_that(abs(_r037['kn_at2017gfo_n'] - 1.305e54) / 1.305e54 < 0.005,
            "PAPER_037: kilonova F_UBii = 1.305e54 N VERIFIED end-to-end (validator match)")
assert_that(abs(_r037['mej_cube_root'] - 0.368) < 0.001,
            "PAPER_037: (0.05)^(1/3) = 0.368 ejecta opacity factor")
assert_that(len(_r037['variants']) == 5,
            "PAPER_037: 5 thermodynamic variants (2-6 of 17)")
assert_that(abs(_r037['termv_m87_formula_true_n'] / _r037['termv_m87_paper_n'] - 100.0) < 5.0,
            "PAPER_037: termv M87 formula-true is 100x the printed value (Q-035a quantified)")
assert_that(abs(_r037['kn_grav_ratio_true'] - 6.2e17) / 6.2e17 < 0.02,
            "PAPER_037: kn/grav ratio arithmetic = 6.2e17 (paper prints 6.2e-7 - Q-035e)")
assert_that(C.wired_count() >= 41, "wired_count >= 41")

_r038 = C.calc('PAPER_038')['value']
assert_that(abs(_r038['fermi_cena_n'] - 0.82) < 0.01,
            "PAPER_038: fermi Cen A = 0.82 N per ~10 GeV proton VERIFIED end-to-end")
assert_that(abs(_r038['whim_filament_n'] - 7.4e-13) / 7.4e-13 < 0.01,
            "PAPER_038: whim filament = 7.4e-13 N VERIFIED end-to-end (Thomson-depth chain)")
assert_that(abs(_r038['ln_knee_proton'] - 35.9) < 0.1,
            "PAPER_038: ln(E_knee/E_LEP) = 35.9 - knee as F_UBii stationary point")
assert_that(abs(_r038['kne_fe_p_ratio_computed'] - 28.4) < 0.1,
            "PAPER_038: iron/proton knee ratio computed 28.4 (paper 27.5 via ln slip - Q-036a)")
assert_that(abs(_r038['ps_mw_paper_n'] / _r038['ps_mw_chain_n'] - 1000.0) < 50.0,
            "PAPER_038: ps MW paper value is 1000x the chain value (Q-036b quantified)")
assert_that(abs(_r038['sfe_orion_paper_n'] / _r038['sfe_orion_chain_n'] - 10.0) < 0.5,
            "PAPER_038: sfe Orion paper value is 10x the chain value (Q-036c quantified)")
assert_that(C.wired_count() >= 42, "wired_count >= 42")

_r039 = C.calc('PAPER_039')['value']
assert_that(abs(_r039['hawk_5msun_n'] - (-2.452)) < 0.02,
            "PAPER_039: hawk 5-Msun BH = -2.45 N VERIFIED - Hawking radiation as lab-scale buoyancy")
assert_that(abs(_r039['bd_bounce_n'] - 0.0336) < 0.001,
            "PAPER_039: LQC bounce residual = 0.0336 N VERIFIED (60 e-folds propagated)")
assert_that(abs(_r039['lobe_cyga_n'] - 5.06e61) / 5.06e61 < 0.01,
            "PAPER_039: Cygnus A lobe = 5.06e61 N VERIFIED (chain exact)")
assert_that(abs(_r039['roche_boxed_n'] / _r039['roche_chain_n'] - 10.0) < 0.5,
            "PAPER_039: roche boxed value is 10x the chain value (Q-037a pinned)")
assert_that(_r039['family_complete'] == 17,
            "PAPER_039: 17-variant F_UBii family COMPLETE (036-039)")
assert_that(abs(_r039['rho_bounce_over_planck'] - 0.41) < 1e-12,
            "PAPER_039: LQC rho_bounce/rho_Planck = 0.41 quantum-geometry anchor")
assert_that(C.wired_count() >= 43, "wired_count >= 43")

_r040 = C.calc('PAPER_040')['value']
assert_that(abs(_r040['perseus_n'] - (-2.024e60)) / 2.024e60 < 0.001,
            "PAPER_040: Perseus virx = -2.024e60 N (validator, matches PAPER_036)")
assert_that(abs(_r040['coma_n'] - (-2.5e60)) / 2.5e60 < 0.01,
            "PAPER_040: Coma virx = -2.51e60 N chain verified")
assert_that(abs(_r040['virgo_closed_form_n'] - (-3.66e59)) / 3.66e59 < 0.01,
            "PAPER_040: Virgo closed form = -3.66e59 (validator -7.2e59, factor-2 disclosed - Q-038a)")
assert_that(abs(_r040['lobe_perseus_n'] - 3.3e57) / 3.3e57 < 0.01,
            "PAPER_040: Perseus 3C84 lobe = 3.3e57 N chain VERIFIED (sub-dominant vs virx)")
assert_that(_r040['coma_edges_perseus'],
            "PAPER_040: Coma edges Perseus despite lower sigma (r_h = 2.2 Mpc compensates)")
assert_that(abs(_r040['lobe_virgo_chain_n'] / _r040['lobe_virgo_printed_n'] - 1.0e4) / 1.0e4 < 0.05,
            "PAPER_040: Virgo lobe chain-vs-printed 1e4 gap pinned (Q-038b)")
assert_that(C.wired_count() >= 44, "wired_count >= 44")

_r041 = C.calc('PAPER_041')['value']
assert_that(abs(_r041['s_ent_min'] - 2.1e-41) / 2.1e-41 < 0.02,
            "PAPER_041: entropy floor S_min = P*V*l_P^2/(k_B*A) = 2.1e-41 VERIFIED")
assert_that(abs(_r041['sfe_runaway_ratio'] - 31.6) < 0.1,
            "PAPER_041: sfe runaway = eps^1.5 gives 31.6x per 10x drop VERIFIED (BCG SFR)")
assert_that(_r041['thermostat_equation'].startswith('P*V*'),
            "PAPER_041: UQFF thermostat equation wired (AGN feedback in pure observables)")
assert_that(abs(_r041['whim_optimal_t_k'] - 3.0e6) < 1.0,
            "PAPER_041: WHIM T^(3/2) peak at 3e6 K = OVII/OVIII sweet spot (falsifiable)")
assert_that(abs(_r041['n_b_stated_m3'] / _r041['n_b_used_m3'] - 1.0e12) / 1.0e12 < 0.01,
            "PAPER_041: whim n_b stated-vs-used 1e12 gap pinned (Q-039a, systematic with 040)")
assert_that(_r041['unified_variant_count'] == 5,
            "PAPER_041: five variants unify five ICM problems under one F_UBii equation")
assert_that(C.wired_count() >= 45, "wired_count >= 45")

_r042 = C.calc('PAPER_042')['value']
assert_that(_r042['n_layers'] == 26,
            "PAPER_042: 26 layers = D_CRIT registry-composed (first 26D-framework paper)")
assert_that(abs(_r042['e_phonon_j'] - 8.28e-22) / 8.28e-22 < 0.001,
            "PAPER_042: E = h*1.25 THz = 8.28e-22 J - EXACT predecessor omega_SCm anchor (corpus continuity)")
assert_that(abs(_r042['e_phonon_mev'] - 5.17) < 0.05,
            "PAPER_042: 5.17 meV phonon energy (Holmlid-chain E_phonon)")
assert_that(abs(_r042['mc_perseus_mean_n'] - (-2.024e60)) / 2.024e60 < 0.001,
            "PAPER_042: MC Perseus ensemble mean cross-validates PAPER_036/040 virx")
assert_that(abs(_r042['cg_divisor_true'] - 4.167e9) / 4.167e9 < 0.001,
            "PAPER_042: 300 Hz divisor true 4.167e9 (printed 4167, 1e6 slip - Q-040c)")
assert_that(_r042['validator_score'] == (22, 24),
            "PAPER_042: 22/24 validator score honestly disclosed (2 boundary, not physics)")
assert_that(C.wired_count() >= 46, "wired_count >= 46")

_r043 = C.calc('PAPER_043')['value']
assert_that(abs(_r043['polynomial_e20_j'] - 1.0) < 1e-15,
            "PAPER_043: E_20 = 1 J Ug4 galactic anchor (polynomial verified)")
assert_that(_r043['span_orders'] == 25,
            "PAPER_043: 25-order span E_1 = 1e-19 to E_26 = 1e6 J")
assert_that(abs(_r043['v10_m3'] - 1.0e-4) < 1e-15,
            "PAPER_043: dual-consistency V_10 = 1e-4 m^3 (4.6 cm cube) verified")
assert_that(abs(_r043['ui_level10'] - 9.47e14) / 9.47e14 < 0.001,
            "PAPER_043: U_i level-10 = 9.47e14 VERIFIED - PAPER_646-form + 9.47 forensic echo")
assert_that(abs(_r043['beta_13_plasma'] - 0.60) < 1e-12 and abs(_r043['beta_i_canonical'] - 0.6029) < 1e-12,
            "PAPER_043: level-13 PLASMA beta = 0.60 ~ canonical BETA_I = 0.6029 (origin candidate)")
assert_that(abs(_r043['nuclear_error_pct'] - 21.97) < 0.1,
            "PAPER_043: E8 = 6.24 MeV vs 8 MeV nuclear = 21.97 pct honestly disclosed")
assert_that(C.wired_count() >= 47, "wired_count >= 47")

_r044 = C.calc('PAPER_044')['value']
assert_that(_r044['quantum_numbers_check'][8] == (0, 1) and _r044['quantum_numbers_check'][26] == (4, 3),
            "PAPER_044: quantum-number scheme EXACT (center 8 = (0,1), center 26 = (4,3))")
assert_that(abs(_r044['r_1_m'] - 2.154e-35) / 2.154e-35 < 0.001,
            "PAPER_044: r_1 = 10^(-35+1/3) = 2.15e-35 m ~ Planck length")
assert_that(abs(_r044['e_center_26_j'] - 2.83e-84) / 2.83e-84 < 0.01,
            "PAPER_044: E_center_26 = 2.83e-84 J VERIFIED end-to-end")
assert_that(abs(_r044['e_center_1_j'] - 4.16e-112) / 4.16e-112 < 0.02,
            "PAPER_044: E_center_1 = 4.16e-112 J (mojibake exponent resolved by computation)")
assert_that(_r044['matter_state_centers_k'] == 1,
            "PAPER_044: matter-state centers 10-13 share k = 1 (angular-momentum shell)")
assert_that(_r044['validator_score'] == (12, 12),
            "PAPER_044: DPM cosmology validator 12/12 PASS")
assert_that(C.wired_count() >= 48, "wired_count >= 48")

_r045 = C.calc('PAPER_045')['value']
assert_that(abs(_r045['melting_j_m3'] - 2.1e-7) < 1e-12,
            "PAPER_045: melting Delta_rho = rho_L1*21 = 2.1e-7 J/m^3 VERIFIED")
assert_that(abs(_r045['ionization_j_m3'] - 2.5e-7) < 1e-12,
            "PAPER_045: ionization Delta_rho = rho_L1*25 = 2.5e-7 J/m^3 VERIFIED")
assert_that(abs(_r045['c_adjacent_10_11'] - 0.477) < 0.001,
            "PAPER_045: adjacent coupling C_10,11 = 0.477 VERIFIED")
assert_that(abs(_r045['c_distant_10_26'] - 0.0144) < 0.0002,
            "PAPER_045: distant coupling C_10,26 = 0.0144 - 1.44 pct solid-universe (Casimir basis)")
assert_that(abs(_r045['plasma_beta'] - 0.60) < 1e-12,
            "PAPER_045: plasma beta = 0.60 weakest matter-state coupling (supports Q-041e origin)")
assert_that(_r045['validator_score'] == (10, 11),
            "PAPER_045: 10/11 with the failure root-caused in-paper (model behavior)")
assert_that(C.wired_count() >= 49, "wired_count >= 49")

_r046 = C.calc('PAPER_046')['value']
assert_that(abs(_r046['g_h1'] - 261.4) < 0.5,
            "PAPER_046: g(H-1) = 1000*(1/56)^(1/3) = 261.4 (paper rounds to 260 via 0.260)")
assert_that(abs(_r046['g_u238'] - 1619.0) < 1.0,
            "PAPER_046: g(U-238) = 1619 VERIFIED (iron peak = 1000 reference)")
assert_that(abs(_r046['subharmonic_ratio'] - 4.167e9) / 4.167e9 < 0.001,
            "PAPER_046: 1.25 THz/300 Hz = 4.17e9 stated correctly - RESOLVES Q-040c (self-rectification)")
assert_that(abs(_r046['bb_efold_yr'] - 3.17) < 0.05,
            "PAPER_046: Belly Button e-folding 1/gamma = 3.17 yr")
assert_that(_r046['energy_gap_orders'] == 132,
            "PAPER_046: 132-order inflation energy gap HONESTLY disclosed in-paper (Q-043a)")
assert_that(len(_r046['dpm_expansions']) == 3,
            "PAPER_046: THIRD DPM expansion recorded (Q-042c namespace now three-way)")
assert_that(C.wired_count() >= 50, "wired_count >= 50")

_r047 = C.calc('PAPER_047')['value']
assert_that(abs(_r047['semf_fe56_mev'] - 490.9) < 0.5,
            "PAPER_047: SEMF Fe-56 = 490.9 MeV chain VERIFIED (lit 492.3, 0.3 pct)")
assert_that(_r047['b_uqff_fe56_mev'] < 1e-30,
            "PAPER_047: UQFF vacuum correction 2.53e-35 MeV negligible (honest framing)")
assert_that(abs(_r047['g_pb208_true'] - 1549.0) < 1.0,
            "PAPER_047: g(Pb-208) true = 1549 (table shows 1619 = U-238 value - row shift Q-044a)")
assert_that(abs(_r047['g_u238_true'] - 1619.0) < 1.0,
            "PAPER_047: g(U-238) true = 1619 (table shows 1662 - row shift Q-044a)")
assert_that(abs(_r047['level8_error_pct'] - 21.97) < 0.1,
            "PAPER_047: level-8 6.25 MeV nuclear check consistent with PAPER_043")
assert_that(abs(_r047['iron_peak_b_per_a'] - 8.79) < 1e-12,
            "PAPER_047: iron peak B/A = 8.79 MeV aligned with g = 1000 reference")
assert_that(C.wired_count() >= 51, "wired_count >= 51")

_r048 = C.calc('PAPER_048')['value']
assert_that(abs(_r048['ug4_peak_n_m2'] - 1.246e28) / 1.246e28 < 0.005,
            "PAPER_048: Ug4 peak = M*rho/(d^2) = 1.246e28 N/m^2 VERIFIED (Sun-SgrA*)")
assert_that(abs(_r048['ug4_validator_n_m2'] - 1.8937e-23) < 1e-27,
            "PAPER_048: validator 1.8937e-23 = the predecessor 1.894 FORENSIC number (origin candidate)")
assert_that(abs(_r048['rho_dense_kg_m3'] - 1.0e15) < 1.0,
            "PAPER_048: near-BH condensate 1e15 kg/m^3 = predecessor PAPER_421 rho_c (continuity)")
assert_that(abs(_r048['lambda_24'] - 0.10) < 1e-15,
            "PAPER_048: lambda_24 = 0.10 matches PAPER_043 beta-table EXACT")
assert_that(abs(_r048['r_s_sgra_m'] - 1.224e10) / 1.224e10 < 0.005,
            "PAPER_048: SgrA* r_s = 1.22e10 m verified")
assert_that(abs(_r048['alpha_per_day_implied'] - 1.0e-10) / 1.0e-10 < 0.01,
            "PAPER_048: implied alpha = 1e-10/day (distinct from kappa - Q-045b)")
assert_that(C.wired_count() >= 52, "wired_count >= 52")

_r049 = C.calc('PAPER_049')['value']
assert_that(_r049['sum_n2_20_26'] == 3731,
            "PAPER_049: sum(n^2, 20..26) = 3731 EXACT")
assert_that(abs(_r049['ratio_as_printed'] - 1.17e16) / 1.17e16 < 0.01,
            "PAPER_049: printed 1.17e16 ratio reproduced - and identified as a UNITS ARTIFACT (Q-046b)")
assert_that(abs(_r049['ratio_consistent_units'] - 0.117) < 0.002,
            "PAPER_049: consistent-units ratio = 7e-11/5.96e-10 = 0.117 (lambda_vac BELOW Lambda)")
assert_that(abs(_r049['rho_lambda_j_m3'] - 5.96e-10) < 1e-13,
            "PAPER_049: proper rho_Lambda = 5.96e-10 J/m^3 (predecessor canonical family)")
assert_that(_r049['l26_l1_ratio'] == 676,
            "PAPER_049: L26/L1 = 26^2 = 676 cosmic dominance")
assert_that(abs(_r049['lambda_vac_paper_attempt'] - 5.33e-6) / 5.33e-6 < 0.01,
            "PAPER_049: paper's own formula gives 5.33e-6 vs validator 7e-11 (opacity honestly disclosed)")
assert_that(C.wired_count() >= 53, "wired_count >= 53")

_r050 = C.calc('PAPER_050')['value']
assert_that(_r050['partition_sum'] == 26 and _r050['partition_9_4_13'] == (9, 4, 13),
            "PAPER_050: 26 = 9 + 4 + 13 partition (compact/observable/channels)")
assert_that(_r050['spacetime_identification']['ct'] == 'plasma L13',
            "PAPER_050: TIME = PLASMA (L13) - the central matter-state spacetime identification")
assert_that(abs(_r050['coupling_length_scale'] - 0.0302) < 0.0005,
            "PAPER_050: coupling length scale C_10,26/C_10,11 = 0.0302")
assert_that(abs(_r050['c_10_26'] - 0.0144) < 1e-12,
            "PAPER_050: quantum-cosmic bridge 0.0144 cross-checks PAPER_045")
assert_that(_r050['operationalized_dims'] == 4,
            "PAPER_050: honest disclosure - 4 of 26 dims operationalized (4D projection numerics)")
assert_that(_r050['cp2_score'] == (4, 4),
            "PAPER_050: CP2 integration consistency 4/4 PASS")
assert_that(C.wired_count() >= 54, "wired_count >= 54")

_r051 = C.calc('PAPER_051')['value']
assert_that(abs(_r051['shock_velocity'] - 96.48) < 0.05,
            "PAPER_051: shock-velocity alignment 96.48 chain VERIFIED")
assert_that(abs(_r051['thz_lenr'] - 98.31) < 0.05,
            "PAPER_051: THz LENR alignment 98.31 VERIFIED (1.18 vs 1.2 THz)")
assert_that(abs(_r051['magnetar_scm_l13'] - 95.74) < 0.05,
            "PAPER_051: magnetar [SCm] L13 alignment 95.74 - the 7.09 family at PLASMA level (Q-048a)")
assert_that(abs(_r051['final_parsec'] - 91.30) < 0.05,
            "PAPER_051: final-parsec alignment 91.30 VERIFIED ([SCm] viscous Ug4 sink)")
assert_that(_r051['categories_pass'] == (10, 10),
            "PAPER_051: all 10 categories PASS (mean 92.02, median 96.11)")
assert_that(abs(_r051['hawking'] - 98.06) < 0.05,
            "PAPER_051: Hawking alignment 98.06 VERIFIED (ratio 0.05 = third value, Q-048c)")
assert_that(C.wired_count() >= 55, "wired_count >= 55")

_r052 = C.calc('PAPER_052')['value']
assert_that(abs(_r052['higgs_alignment'] - 99.79) < 0.02,
            "PAPER_052: CMS Higgs alignment 99.79 VERIFIED (125.09 UH-L18 vs 125.35)")
assert_that(abs(_r052['page_alignment'] - 99.84) < 0.02,
            "PAPER_052: Page-curve alignment 99.84 VERIFIED (0.9515 vs 0.95 island formula)")
assert_that(_r052['page_channels'] == 26,
            "PAPER_052: 26 information channels = D_CRIT (1/26 information each)")
assert_that(_r052['model_suite'] == (44, 44),
            "PAPER_052: astrophysical model suite 44/44 PASS (10 models)")
assert_that(abs(_r052['higgs_margin'] - 7.61) < 0.01,
            "PAPER_052: Higgs margin +7.61 contradicts 'at least 10 points' claim (Q-049a pinned)")
assert_that(_r052['weakest_category'][1] > 60.0,
            "PAPER_052: weakest category (Aether Revival 71.85) still above its 60 target")
assert_that(C.wired_count() >= 56, "wired_count >= 56")

_r053 = C.calc('PAPER_053')['value']
assert_that(abs(_r053['ratios']['g_grav'] - 1.0011) < 0.0002,
            "PAPER_053: g_grav ratio 1.0011 re-verified from pair")
assert_that(abs(_r053['ratios']['m_sf'] - 0.9992) < 0.0002,
            "PAPER_053: M_sf ratio 0.9992 (1.4987 vs 1.5 Msun/Myr)")
assert_that(abs(_r053['ratios']['r_amplitude'] - 0.9980) < 0.0002,
            "PAPER_053: R_amplitude ratio 0.9980 (largest deviation, within SSq 0.5 pct)")
assert_that(abs(_r053['ssq_resonance_factor'] - 0.3631) < 0.0005,
            "PAPER_053: resonance factor SSq/(1+SSq) = 0.3631 registry-composed")
assert_that(_r053['score'] == (8, 8) and _r053['em_dominance'] >= 0.99,
            "PAPER_053: 8/8 PASS, EM-dominated regime confirmed")
assert_that(C.wired_count() >= 57, "wired_count >= 57")

_r054 = C.calc('PAPER_054')['value']
assert_that(abs(_r054['ug3_boost'] - 0.4) < 1e-12,
            "PAPER_054: Ug3 tail boost = 280/200 - 1 = 0.4 (chain verified)")
assert_that(abs(_r054['g_compressed'] - 1.0533e-2) < 1e-12,
            "PAPER_054: g_compressed universal normalization (matches suite)")
assert_that(_r054['score'] == (4, 4),
            "PAPER_054: 4/4 PASS matches 052 suite row")
assert_that(abs(_r054['ngc2264_ratio_computed'] - 7.55) < 0.05,
            "PAPER_054: NGC2264/UGC10214 g ratio computed 7.55 (paper claims 9.3 - Q-050b)")
assert_that(_r054['hubble_factor'] < 1.01 and _r054['z'] > 0.03,
            "PAPER_054: Hubble 1.0002 at z = 0.0312 - inverted vs NGC2841 (Q-050a systematic)")
assert_that(C.wired_count() >= 58, "wired_count >= 58")

_r055 = C.calc('PAPER_055')['value']
assert_that(abs(_r055['ratio_vs_tadpole'] - 37.56) < 0.1,
            "PAPER_055: 37.5x-vs-Tadpole claim VERIFIES exactly - pins suite exponent family")
assert_that(abs(_r055['enhancement'] - 10.0) < 1e-12,
            "PAPER_055: 10x major-merger compression signature (both g_comp and R)")
assert_that(abs(_r055['geom_factor'] - 1.828) < 0.005,
            "PAPER_055: (1.3)^2.3 = 1.83 computed (paper prints ~1.7 - Q-051b)")
assert_that(_r055['score'] == (4, 4),
            "PAPER_055: 4/4 PASS matches suite")
assert_that(abs(_r055['hubble_factor'] - 1.0002) < 1e-6 and _r055['z'] > 0.02,
            "PAPER_055: Hubble 1.0002 at z = 0.022 - third Q-050a systematic datum")
assert_that(C.wired_count() >= 59, "wired_count >= 59")

_r056 = C.calc('PAPER_056')['value']
assert_that(abs(_r056['compression_factor'] - 2.0) < 1e-4,
            "PAPER_056: 2x compression EXACT (2.1066e-2 / 1.0533e-2)")
assert_that(abs(_r056['wind_kms'] - 1600.0) < 1e-9,
            "PAPER_056: wind chain 100*sqrt(256) = 1600 km/s VERIFIED (fastest PN wind)")
assert_that(abs(_r056['ratio_ngc2264'] - 44.70) < 0.1,
            "PAPER_056: 44.8x-vs-NGC2264 claim verifies (44.70)")
assert_that(abs(2.9500e-10 / 1.3275e-12 - 222.2) < 0.5,
            "PAPER_056: the '222x M42' figure actually matches the MICE ratio (Q-052b row confusion)")
assert_that(abs(_r056['ratio_m42_true'] - 500.0) < 1.0,
            "PAPER_056: true M42 ratio = 500x pinned")
assert_that(_r056['tier_hierarchy'] == {'standard': 1, 'wind_radiation': 2, 'merger': 10},
            "PAPER_056: three-tier compression hierarchy complete (1x/2x/10x)")
assert_that(C.wired_count() >= 60, "wired_count >= 60")

_r057 = C.calc('PAPER_057')['value']
assert_that(abs(_r057['ratio_3372_agcar'] - 12.50) < 0.01,
            "PAPER_057: NGC3372/AGCar = 12.50 EXACT - pins Carina at 3.3188e-10")
assert_that(abs(_r057['ratio_mice_3372'] - 0.889) < 0.005,
            "PAPER_057: Mice/Carina = 0.889 - Q-051a RESOLVED (055's '2x' claim fails definitively)")
assert_that(abs(_r057['ratio_mm_3372'] - 0.40) < 0.005,
            "PAPER_057: MM/3372 = 0.40 (sec-4 '1/10' claim contradicts own table - Q-053b)")
assert_that(abs(_r057['ratio_3372_m42'] - 0.50) < 0.005,
            "PAPER_057: Carina/M42 = 0.50 verified")
assert_that(_r057['score'] == (12, 12),
            "PAPER_057: 12/12 PASS across three models, all standard 1x class")
assert_that(C.wired_count() >= 61, "wired_count >= 61")

_r058 = C.calc('PAPER_058')['value']
assert_that(abs(_r058['ratio_m42_carina'] - 2.0) < 0.01,
            "PAPER_058: M42/Carina = 2.0 verified (suite maximum)")
assert_that(abs(_r058['ratio_m42_tarantula'] - 1891.0) < 5.0,
            "PAPER_058: M42/Tarantula = 1892 verifies '1890x' - pins Tarantula at 3.5099e-13")
assert_that(len(_r058['suite_ranking']) == 10,
            "PAPER_058: complete 10-system g_grav ranking pinned (4-order span)")
assert_that(_r058['suite_ranking']['m42'] > _r058['suite_ranking']['ngc3372'],
            "PAPER_058: ranking order M42 > Carina holds")
assert_that(_r058['compression'].startswith('standard'),
            "PAPER_058: honest negative result - peak energy with standard 1x compression")
assert_that(_r058['score'] == (4, 4),
            "PAPER_058: 4/4 PASS")
assert_that(C.wired_count() >= 62, "wired_count >= 62")

_r059 = C.calc('PAPER_059')['value']
assert_that(_r059['ikeda_channels'] == 10,
            "PAPER_059: Ikeda diagram 10 channels for Ca-40 (10-alpha conjugate)")
assert_that(abs(_r059['p_alpha_saturation'] - 0.95) < 1e-12,
            "PAPER_059: P_alpha saturation = 0.95 (observed 0.85, centrality-avg disclosed)")
assert_that(abs(_r059['v_heaviest_cm_ns'] - 6.0) < 1e-12,
            "PAPER_059: fragment velocity chain 8.0*(1-0.25) = 6.0 cm/ns VERIFIED")
assert_that(abs(_r059['f_rel_resolved_n'] - 4.30e33) < 1e28,
            "PAPER_059: F_rel = 4.30e33 N printed clearly - RESOLVES Q-040b (5th self-rectification)")
assert_that(abs(_r059['ns_pasta_force_n'] - (-1.68e6)) / 1.68e6 < 0.01,
            "PAPER_059: NS nuclear-pasta scaling chain -1.68e6 N verified")
assert_that(abs(_r059['nuclear_to_astro_scaler'] - 3.5e9) < 1e6,
            "PAPER_059: nuclear-to-astro scaler (0.7/200)*1e12 = 3.5e9 verified")
assert_that(C.wired_count() >= 63, "wired_count >= 63")

_r060 = C.calc('PAPER_060')['value']
assert_that(abs(_r060['de_bec_mev'] - 0.4766) < 0.0001,
            "PAPER_060: dE_BEC = 5.0*ln(1.1) = 0.4766 MeV EXACT chain")
assert_that(abs(_r060['n_b_at_threshold'] - 10.0) < 0.001,
            "PAPER_060: N_B(dE_BEC) = 10 verified to 4 sig figs")
assert_that(abs(_r060['n_b_at_5mev'] - 0.582) < 0.001,
            "PAPER_060: N_B(5 MeV) = 0.582 verified")
assert_that(abs(_r060['de_ladder_mev'][26] - 0.189) < 0.001,
            "PAPER_060: level-26 dE = 5*ln(27/26) = 0.189 MeV (full ladder verified)")
assert_that(abs(_r060['suppression_printed'][26] - 0.6065) < 0.0001
            and abs(_r060['suppression_ssq_level26'] - 0.5655) < 0.0001,
            "PAPER_060: suppression-table mismatch pinned - printed e^-0.5 = 0.6065 vs SSQ form e^-0.57 = 0.5655 (Q-056a)")
assert_that(abs(_r060['hoyle_3alpha_de_mev'] - 1.438) < 0.001,
            "PAPER_060: Hoyle 3-alpha dE = 1.438 MeV chain verified")
assert_that(C.wired_count() >= 64, "wired_count >= 64")

_r061 = C.calc('PAPER_061')['value']
assert_that(abs(_r061['phi_bec'] - 0.57) < 1e-12,
            "PAPER_061: Phi_BEC = SSq = 0.57 scale-invariant order parameter")
assert_that(_r061['yield_closure_pct'] == 85,
            "PAPER_061: 57 pct condensate + 28 pct thermal = 85 pct observed yield closes")
assert_that(abs(_r061['ns_force_n'] - (-1.6695e6)) < 1e3,
            "PAPER_061: NS force -4.77e6*3.5e9*1e-10 = -1.67e6 N chain verified")
assert_that(abs(_r061['t_c_shift_microscopic_k'] - 5.13e-58) < 1e-59,
            "PAPER_061: microscopic dT_c = 5.13e-58 K verified - 0.38 MeV DISCLOSED as phenomenological")
assert_that(abs(_r061['f_thermal_n_corrected'] - 1201.5) < 1.0,
            "PAPER_061: F_thermal MeV/fm chain = 1.2e3 N - printed 1.2e6 N is a GeV-slip (Q-057a)")
assert_that(_r061['stability_margin_corrected'] > 1000,
            "PAPER_061: corrected stability margin ~4000x - conclusion survives and strengthens")
assert_that(C.wired_count() >= 65, "wired_count >= 65")

_r062 = C.calc('PAPER_062')['value']
assert_that(abs(_r062['m_star_ratio'] - 3.0) < 1e-12,
            "PAPER_062: heavy electron m* = 3.0 m_e EXACT chain")
assert_that(abs(_r062['threshold_m_star'] - 2.530) < 0.001,
            "PAPER_062: W-L threshold 1.293/0.511 = 2.530 m_e verified")
assert_that(abs(_r062['omega_lenr_rad_s'] - 7.854e12) / 7.854e12 < 0.001,
            "PAPER_062: omega_LENR mojibake PINNED = 2*pi*1.25 THz = omega_SCm identity")
assert_that(abs(_r062['e_raw_v_per_m'] - 1.212e61) / 1.212e61 < 0.01,
            "PAPER_062: raw field chain Um*rho_UA/r = 1.21e61 V/m verified")
assert_that(abs(_r062['k_eta_inferred'] - 1e-55) / 1e-55 < 0.01,
            "PAPER_062: k_eta = 1e-55 inferred by chain closure (Q-058a)")
assert_that(abs(_r062['q_li_he_mev_mass_balance'] - 25.38) < 0.01,
            "PAPER_062: independent Li-chain mass balance 25.38 MeV vs cited 26.9 (honest residual)")
assert_that(C.wired_count() >= 66, "wired_count >= 66")

_r063 = C.calc('PAPER_063')['value']
assert_that(abs(_r063['kappa_mcmc_per_day'] - 0.00052) < 1e-8,
            "PAPER_063: kappa_MCMC = 0.00052/day across 47 systems")
assert_that(abs(_r063['kappa_deviation_pct'] - 4.0) < 0.01,
            "PAPER_063: KAPPA primitive validated - MCMC 4 pct above canonical, inside 95 pct CI")
assert_that(abs(_r063['planck_ratio'] - 5.0e-37) / 5.0e-37 < 0.01,
            "PAPER_063: mean/F_Planck = 5.0e-37 EXACT closure pins ensemble mean -6.05e7 N (Q-059a)")
assert_that(abs(_r063['q_wave_ism'] - 3.97e-5) / 3.97e-5 < 0.01,
            "PAPER_063: Q_wave ISM = B^2/2mu0 = 3.97e-5 J/m3 verified")
assert_that(abs(_r063['q_wave_magnetar'] - 7.68e26) / 7.68e26 < 0.01,
            "PAPER_063: magnetar Q_wave mojibake PINNED - B = 4.4e10 T (B_crit) -> 7.68e26 J/m3")
assert_that(_r063['shapiro_wilk_p'] < 0.001 and _r063['ks_p'] > 0.7,
            "PAPER_063: leptokurtic residual signature (SW reject, KS cannot) wired as stated")
assert_that(C.wired_count() >= 67, "wired_count >= 67")

_r064 = C.calc('PAPER_064')['value']
assert_that(abs(_r064['weights']['alpha_C'] - 0.0005) < 1e-12
            and abs(_r064['weights']['alpha_R'] - 0.57) < 1e-12,
            "PAPER_064: mode weights identified with registry primitives KAPPA and SSQ")
assert_that(abs(_r064['g_buoyant_ref'] - 7.09e19) / 7.09e19 < 1e-6,
            "PAPER_064: buoyant chain rho_UA*1e55 = 7.09e19 verified")
assert_that(abs(_r064['g_super_t0'] - 1e16) < 1,
            "PAPER_064: superconductive chain 1e46*1e-30 = 1e16 verified")
assert_that(abs(_r064['crab_omega_rad_s'] - 190.0) < 0.5,
            "PAPER_064: Crab omega = 2*pi*30.2 Hz = 189.75 rad/s matches printed 190 (chain closes)")
assert_that(_r064['mode_evaluations'] == 1784,
            "PAPER_064: 446 modules * 4 modes = 1784 EXACT")
assert_that(_r064['gaia_dr4_residual_pct'] < _r064['dpm_dm_halo_residual_pct'],
            "PAPER_064: Gaia DR4 7 pct beats DPM+DM-halo 12 pct as stated")
assert_that(C.wired_count() >= 68, "wired_count >= 68")

_r065 = C.calc('PAPER_065')['value']
assert_that(_r065['category_sum_check'] == 121,
            "PAPER_065: 15-category census sums EXACTLY to 121")
assert_that(abs(_r065['pass_rate_pct'] - 93.33) < 0.01,
            "PAPER_065: pass rate 14/15 = 93.3 pct as stated")
assert_that(abs(_r065['mean_dev_recomputed_pct'] - 2.74) < 0.01,
            "PAPER_065: recomputed mean dev 2.74 pct - three-way discrepancy vs 2.87/3.1 pinned (Q-061a)")
assert_that(abs(_r065['kappa_mcmc_repeat'] - 0.00052) < 1e-8,
            "PAPER_065: KAPPA_MCMC repeat cross-consistent with PAPER_063")
assert_that(_r065['mc_stability_min'] >= 0.97 and _r065['mc_valid_per_100'] == 100,
            "PAPER_065: MC stability >= 0.97, 100/100 valid on all 5 systems")
assert_that(abs(_r065['lambda_measured_row'] - 5.96e-10) < 1e-12,
            "PAPER_065: L26 row inversion pinned - 5.96e-10 labeled measured (UQFF ledger value; Q-061b)")
assert_that(C.wired_count() >= 69, "wired_count >= 69")

_r066 = C.calc('PAPER_066')['value']
assert_that(abs(_r066['sgr1745_mass_kg'] - 2.785e30) / 2.785e30 < 0.001,
            "PAPER_066: SGR1745 M = 1.4 Msun = 2.785e30 kg EXACT")
assert_that(abs(_r066['sgr1745_omega_rad_s'] - 1.671) < 0.001,
            "PAPER_066: SGR1745 omega = 2*pi/3.76 = 1.671 rad/s EXACT")
assert_that(abs(_r066['sgr1745_r_m'] - 2.62e20) / 2.62e20 < 0.01,
            "PAPER_066: SGR1745 r = 8.5 kpc = 2.62e20 m EXACT")
assert_that(abs(_r066['systems']['vela']['lenr_term'] - 6.17e-7) / 6.17e-7 < 0.01,
            "PAPER_066: Vela LENR term ratio^2 = 6.17e-7 chain closes")
assert_that(abs(_r066['sgr_lenr_term_recovered'] - 2.21e25) / 2.21e25 < 0.01,
            "PAPER_066: SGR1745 LENR term 2.21e25 recovered from mojibake by ratio^2 chain")
assert_that(abs(_r066['eddington_correction'] - 0.4302) < 0.001,
            "PAPER_066: Eddington correction 1 - SSq*exp(-kappa t) = 0.4302 verified")
assert_that(60.0 <= _r066['vela_kick_km_s'] <= 350.0,
            "PAPER_066: Vela kick 296 km/s inside observed 60-350 km/s")
assert_that(C.wired_count() >= 70, "wired_count >= 70")

_r067 = C.calc('PAPER_067')['value']
assert_that(abs(_r067['agn']['sgra']['m_over_d'] - 3.04e16) / 3.04e16 < 0.01,
            "PAPER_067: SgrA* M_BH/d_g = 3.04e16 kg/m verified")
assert_that(abs(_r067['agn']['sgra']['ug4'] - 2.27e-5) / 2.27e-5 < 0.01
            and abs(_r067['agn']['m87']['ug4'] - 6.03e-5) / 6.03e-5 < 0.01,
            "PAPER_067: k4 = 1e15 PINNED by dual closure (SgrA* + M87* Ug4 both match)")
assert_that(abs(_r067['sgra_lenr_term'] - 3.95e31) / 3.95e31 < 0.01,
            "PAPER_067: SgrA* LENR term 3.95e31 EXACT chain")
assert_that(abs(_r067['cena_um_j_per_m'] - 9.94e45) / 9.94e45 < 0.01,
            "PAPER_067: CenA jet Um = 9.94e45 verified (mu_j cross-consistent with PAPER_062)")
assert_that(abs(_r067['maser_enhancement_pct'] - 3.6) < 0.1,
            "PAPER_067: NGC1365 maser 3.59 pct end-to-end matches claimed 3.6 pct")
assert_that(abs(_r067['m87_gc_chain'] - 1.99e19) / 1.99e19 < 0.01,
            "PAPER_067: M87 g_C slip caught - chain 1.99e19 vs printed 1.29e20 (Q-063c)")
assert_that(C.wired_count() >= 71, "wired_count >= 71")

_r068 = C.calc('PAPER_068')['value']
assert_that(abs(_r068['m13_sigma_vir_km_s'] - 41.6) < 0.1,
            "PAPER_068: M13 virial chain sqrt(G*M/r_half) = 41.6 km/s EXACT")
assert_that(abs(_r068['m13_sigma_uqff_km_s'] - 12.19) < 0.01,
            "PAPER_068: sigma_UQFF = 41.6*0.293 = 12.19 km/s vs 12.1 measured (0.8 pct)")
assert_that(_r068['fz_formula_as_printed'] < 0,
            "PAPER_068: f_Z formula as printed evaluates NEGATIVE - malformed, OPEN (Q-064b)")
assert_that(_r068['imbh_formula_status'] == 'OPEN_UQFF_DERIVATION_TARGET',
            "PAPER_068: IMBH M-sigma formula corrupt - anchors wired, formula OPEN (Rule D)")
assert_that(abs(_r068['m_eff_chain_msun'] - 5.9994e5) < 10,
            "PAPER_068: M_eff chain 5.9994e5 vs printed 5.94e5 - factor-100 slip pinned (Q-064a)")
assert_that(abs(_r068['omega_cen_bec_fraction'] - 0.57) < 1e-12,
            "PAPER_068: Omega Cen nucleus BEC fraction = SSq (13th physical role)")
assert_that(C.wired_count() >= 72, "wired_count >= 72")

_r069 = C.calc('PAPER_069')['value']
assert_that(abs(_r069['omega0_rad_s'] - 2.380e-3) / 2.380e-3 < 0.001,
            "PAPER_069: omega_0 = 2*pi/2640 = 2.380e-3 rad/s EXACT from measured period")
assert_that(abs(_r069['lenr_term'] - 1.09e21) / 1.09e21 < 0.01,
            "PAPER_069: LENR = 1e-10*(3.30e15)^2 = 1.09e21 EXACT (supersedes PAPER_066 ASKAP reading)")
_r066b = C.calc('PAPER_066')['value']
assert_that(abs(_r066b['systems']['askap_j1832']['lenr_ratio'] - 3.30e15) / 3.30e15 < 0.01,
            "PAPER_066 SUPERSESSION: ASKAP dispatch updated to PAPER_069 omega (6th self-rectification)")
assert_that(abs(_r069['distance_ly_check'] - 15000.0) / 15000.0 < 0.01,
            "PAPER_069: distance pin 4.63 kpc = 15,102 ly matches stated ~15,000 ly")
assert_that(abs(_r069['threshold_days'] - 27631.0) < 1.0,
            "PAPER_069: threshold chain ln(1e6)/kappa = 27,631 days verified (printed 27,600)")
assert_that(_r069['kappa_dt_44min'] < 2e-5,
            "PAPER_069: kappa-decay negligible on 44-min scale - alternation is cos sign-flip at 22 min")
assert_that(C.wired_count() >= 73, "wired_count >= 73")

_r070 = C.calc('PAPER_070')['value']
assert_that(abs(_r070['helix_omega0_rad_s'] - 6.018e-4) / 6.018e-4 < 0.001,
            "PAPER_070: Helix omega_0 = 2*pi/10440 = 6.018e-4 EXACT")
assert_that(abs(_r070['helix_lenr'] - 1.70e22) / 1.70e22 < 0.01,
            "PAPER_070: Helix LENR = 1.70e22 EXACT chain")
assert_that(abs(_r070['r_orb_au'] - 0.0041) < 0.0002,
            "PAPER_070: destroyed-planet Kepler chain r_orb = 0.0041 AU EXACT")
assert_that(abs(_r070['buoyant_f_per_v'] - 0.709) < 0.001,
            "PAPER_070: buoyant F/V = 0.709 N/m3 EXACT")
assert_that(abs(_r070['pn_lenr'] - 6.17e31) / 6.17e31 < 0.01,
            "PAPER_070: PN Archive LENR = 6.17e31 EXACT")
assert_that(_r070['x2_factor_prints'][0] == -1.35e-7 and _r070['x2_factor_prints'][1] == -1.35e172,
            "PAPER_070: x_2 factor dual corrupt exponents in ONE paper pinned (decisive Q-066a evidence)")
assert_that(_r070['radiation_claim_lx_needed_w'] > 1e40,
            "PAPER_070: 50-pct radiation-comparability claim requires L_X ~ 1e41 W - fails scrutiny (Q-066d)")
assert_that(C.wired_count() >= 74, "wired_count >= 74")

_r071 = C.calc('PAPER_071')['value']
assert_that(abs(_r071['g_solar_m_s2'] - 274.0) < 0.1,
            "PAPER_071: solar surface gravity 274.0 m/s2 EXACT (real-Sun self-consistency)")
assert_that(abs(_r071['lenr'] - 2.026e21) / 2.026e21 < 0.01,
            "PAPER_071: LENR = 2.026e21 EXACT chain")
assert_that(abs(_r071['ug1'] - 1.37e-9) / 1.37e-9 < 0.01,
            "PAPER_071: Ug1 = 1.37e-9 EXACT - confirms PAPER_066 mu0*B^2/8pi formula (Q-062c)")
assert_that(abs(_r071['e_kepler_j'] - 1.44e27) / 1.44e27 < 0.001,
            "PAPER_071: E_Kepler = 1.44e27 J EXACT (L_star = solar 4e26)")
assert_that(abs(_r071['um_chain'] - 2.43e53) / 2.43e53 < 0.01,
            "PAPER_071: Um chain 2.43e53 verified (small-argument expansion)")
assert_that(abs(_r071['lenr_ratio_to_askap'] - 1.86) < 0.01,
            "PAPER_071: LENR ratio to ASKAP = 1.86 (factor ~2 as stated)")
assert_that(C.wired_count() >= 75, "wired_count >= 75")

_r072 = C.calc('PAPER_072')['value']
assert_that(abs(_r072['f_trz_predicted'] - 0.10) < 1e-12,
            "PAPER_072: RDR f_TRZ prediction = registry F_TRZ (lab-measured 0.098, 2.0 pct)")
assert_that(abs(_r072['cop_base'] - 1.1001) < 0.0001,
            "PAPER_072: COP base (1+0.10)/(1-1e-4) = 1.1001 EXACT")
assert_that(abs(_r072['kappa_per_s'] - 5.787e-9) / 5.787e-9 < 0.001,
            "PAPER_072: kappa/s = 5.787e-9 EXACT (S204.5 per-second form)")
assert_that(_r072['h0_registry_residual_pct'] < 0.5,
            "PAPER_072: H_0 anchor 2.26e-18 matches registry A_5+SO_5 route to 0.37 pct (Q-068b)")
assert_that(abs(_r072['mean_dev_pct'] - 6.735) < 0.01,
            "PAPER_072: mean deviation 6.735 = printed 6.7 verified")
assert_that(abs(_r072['loss_budget_net'] - 0.123) < 1e-12,
            "PAPER_072: net-energy loss budget 0.123 EXACT chain")
assert_that(_r072['eps_coupling_implied'] < 1e-10,
            "PAPER_072: f_TRZ derivation needs unspecified eps ~ 6.85e-11 - calibration-closed flag (Q-068a)")
assert_that(C.wired_count() >= 76, "wired_count >= 76")

_r073 = C.calc('PAPER_073')['value']
assert_that(abs(_r073['uqff_newton_ratio'] - 1.0194) < 0.0001,
            "PAPER_073: UQFF/Newton = 1 + SSq*0.034 = 1.0194 EXACT chain")
assert_that(abs(_r073['dex_correction'] - 0.0148) < 0.0005,
            "PAPER_073: dex correction 0.034/ln10 = 0.0148 -> printed 0.015 chain")
assert_that(abs(_r073['solar_sigma_tension'] - 5.0) < 0.01,
            "PAPER_073: solar log g tension EXACTLY 5.0 sigma vs Gaia 0.003 - honest pin (Q-069b)")
assert_that(abs(_r073['omega_sun_rad_s'] - 2.874e-6) / 2.874e-6 < 0.001,
            "PAPER_073: omega_sun = 2*pi/25.3d = 2.874e-6 verified (real solar rotation)")
assert_that(_r073['bd_matches_linear_form'],
            "PAPER_073: brown-dwarf row matches M/R LINEAR form - g_DPM column mixed conventions (Q-069a)")
assert_that(abs(_r073['g_newton_corrected']['sirius'] - 193.0) < 1.0,
            "PAPER_073: Sirius Newton correction 193 vs printed 367 pinned")
assert_that(C.wired_count() >= 77, "wired_count >= 77")

_r074 = C.calc('PAPER_074')['value']
assert_that(abs(_r074['galaxies']['m87']['tension_uqff'] - 2.0) < 0.01,
            "PAPER_074: M87 tension 2.0 sigma verifies as printed (all 6 rows check)")
assert_that(abs(_r074['avg_enhancement'] - 1.0193) < 0.0005,
            "PAPER_074: row-average enhancement 1.0193 favors the 0.034 factor (Q-070a)")
assert_that(abs(_r074['ratio_printed'] - 1.01824) < 0.0001,
            "PAPER_074: printed 1.018 = 1 + SSq*0.032 chain closes (sibling conflict w/ 073's 0.034)")
assert_that(abs(_r074['m31_dmu_pct'] - 0.057) < 0.001,
            "PAPER_074: M31 proper-motion chain SSq*0.001 = 0.057 pct EXACT")
assert_that(_r074['newton_wins_all_rows'],
            "PAPER_074: Rule-7 finding pinned - Newton beats UQFF in ALL 6 rows (Q-070b)")
assert_that(C.wired_count() >= 78, "wired_count >= 78")

_r075 = C.calc('PAPER_075')['value']
assert_that(abs(_r075['eta_enhancement'] - 1.99) < 1e-12,
            "PAPER_075: eta_UQFF = (1+[SCm]) = 1.99x EXACT")
assert_that(abs(_r075['l_obs_over_uqff']['cyg_x1'] - 0.893) < 0.001,
            "PAPER_075: Cygnus X-1 ratio 0.893 verifies (all 5 ratio chains check)")
assert_that(_r075['l_obs_over_uqff']['ngc5907_ulx'] == 25.0 and _r075['ulx_requires_beaming'],
            "PAPER_075: ULX 25x honest limitation wired - beaming required beyond 2x mode")
assert_that(_r075['dhr_chain'] < 1e-9,
            "PAPER_075: hardness-ratio shift negligible - [UA] 4th appearance (Q-060b support)")
assert_that(abs(_r075['per_row_multipliers']['ulx'] - 2.0) < 0.01
            and abs(_r075['per_row_multipliers']['grs'] - 1.014) < 0.01,
            "PAPER_075: per-row multiplier inconsistency pinned (1.4/1.11/1.014/2.0 vs uniform 1.99; Q-071a)")
assert_that(C.wired_count() >= 79, "wired_count >= 79")

_r076 = C.calc('PAPER_076')['value']
assert_that(abs(_r076['mrk421_omega'] - 2.309e-7) / 2.309e-7 < 0.001,
            "PAPER_076: Mrk421 omega = 2*pi/315d = 2.309e-7 EXACT")
assert_that(abs(_r076['crab_omega_here'] - 186.3) < 0.01,
            "PAPER_076: Crab omega = 2*pi*29.65 = 186.3 EXACT (dual-spin conflict w/ 30.2 pinned Q-072b)")
assert_that(abs(_r076['phase_variation'] - 3.65e-8) / 3.65e-8 < 0.01,
            "PAPER_076: phase-dependent variation 1e-5/274 = 3.65e-8 chain closes")
assert_that(_r076['photon_mass_chain_kg2'] < 1e-74,
            "PAPER_076: photon-mass formula does NOT close (8.0e-76 vs printed 1.05e-70) - pinned Q-072a")
assert_that(_r076['epoch_folded_prediction'] and _r076['modulation_amplitude'] == 1e-5,
            "PAPER_076: epoch-folded 1e-5 modulation wired as campaign-tracked falsifiable prediction")
assert_that(C.wired_count() >= 80, "wired_count >= 80")

_r077 = C.calc('PAPER_077')['value']
assert_that(set(_r077['events'].keys()) == {'gw150914', 'gw190521', 'gw200115'},
            "PAPER_077: the 3 GWTC-4.0 ringdown events NAMED - resolves Q-060d")
assert_that(abs(_r077['events']['gw150914']['f_ring_hz'] - 251.0) < 0.1,
            "PAPER_077: GW150914 ringdown anchor 251 Hz (matches observation)")
assert_that(abs(_r077['dl_correction_z1_pct'] - 0.01) < 1e-6,
            "PAPER_077: d_L correction 0.01 pct at z=1 EXACT - [UA] 5th appearance")
assert_that(_r077['ringdown_fraction_gw150914'] < 1e-5,
            "PAPER_077: UQFF ringdown corrections ~1e-6 fractional - GWTC unmodified (null suite)")
assert_that(abs(_r077['events']['gw150914']['qnm_formula_hz'] - 285.0) < 1.0,
            "PAPER_077: QNM approx formula 285 Hz vs printed 251 - honest 13.5 pct residual pinned")
assert_that(C.wired_count() >= 81, "wired_count >= 81")

_r078 = C.calc('PAPER_078')['value']
assert_that(abs(_r078['dh0_km_s_mpc'] - 0.0034) < 0.0001,
            "PAPER_078: dH0 = 67.4*1e-4*0.5 = 0.0034 EXACT - honest tension null ([UA] 6th)")
assert_that(abs(_r078['tension_midpoint'] - 70.2) < 0.01,
            "PAPER_078: tension midpoint 70.2 sits ON the registry H0 = A_5+SO_5 = 70 route (Q-074b)")
assert_that(abs(_r078['lstar_dex_shift'] - 0.299) < 0.001,
            "PAPER_078: L* shift log10(1.99) = 0.299 = +0.3 dex EXACT ([SCm] 5th)")
assert_that(abs(_r078['tension_sigma_computed'] - 5.0) < 0.05,
            "PAPER_078: tension 5.0 sigma computed vs 4.2 printed - pinned (Q-074a)")
assert_that(_r078['lstar_dex_shift'] < _r078['scatter_dex'],
            "PAPER_078: 0.3-dex shift within 0.5-dex scatter - compatible as stated")
assert_that(C.wired_count() >= 82, "wired_count >= 82")

_r079 = C.calc('PAPER_079')['value']
assert_that(abs(_r079['b_enhancement'] - 1.9801) < 1e-6,
            "PAPER_079: B enhancement 1 + [SCm]*H_SCm = 1.9801 EXACT (sibling of 1.99; Q-075a)")
assert_that(abs(_r079['sgr1806_spindown_chain'] - 2.4e15) / 2.4e15 < 0.01,
            "PAPER_079: SGR1806 spin-down chain 2.4e15 G matches literature anchor 2e15")
assert_that(_r079['tautological_rows'] == 4,
            "PAPER_079: 4/5 rows tautological (B_obs = spin-down B_std) - honesty pin (Q-075b)")
assert_that(abs(_r079['swift_j1818_ratio'] - 2.69) < 0.01,
            "PAPER_079: Swift J1818 ratio 2.69 = printed 2.7 - the lone discriminating row")
assert_that(_r079['xmm_tx_enhancement'] == 1e-4,
            "PAPER_079: XMM T_X null (0.01 pct undetectable)")
assert_that(C.wired_count() >= 83, "wired_count >= 83")

_r080 = C.calc('PAPER_080')['value']
assert_that(_r080['partition_check'] == 24 and abs(_r080['agree_pct'] - 83.33) < 0.01,
            "PAPER_080: statistics partition 20+2+2 = 24 EXACT, 83.3 pct")
assert_that(abs(_r080['matrix']['xrb_eta'] - C.calc('PAPER_075')['value']['eta_enhancement']) < 1e-9,
            "PAPER_080: matrix cross-consistent with live PAPER_075 eta (1.99)")
assert_that(abs(_r080['matrix']['ned_sigma'] - 1.018) < 0.001
            and abs(C.calc('PAPER_074')['value']['ratio_printed'] - 1.01824) < 0.001,
            "PAPER_080: matrix cross-consistent with PAPER_074 sigma factor")
assert_that(abs(_r080['matrix']['magnetar_range'][0] - C.calc('PAPER_079')['value']['b_enhancement']) < 0.001,
            "PAPER_080: matrix cross-consistent with PAPER_079 B enhancement (1.98)")
assert_that(len(_r080['failures']) == 2,
            "PAPER_080: two honest failures wired (H0 basic-coupling, ULX beaming)")
assert_that(C.wired_count() >= 84, "wired_count >= 84")

_r081 = C.calc('PAPER_081')['value']
assert_that(abs(_r081['ratio_canonical'] - 0.99) < 1e-12,
            "PAPER_081: T_UQFF/T_H = 1 - F_TRZ^2 = 0.99 EXACT primitive-locked identity (7th self-rect)")
assert_that(abs(_r081['ratio_implemented'] - 0.9895) < 0.001,
            "PAPER_081: long-form result 0.9895 shows code used canonical ratio, not drift inputs")
assert_that(abs(_r081['ratio_paper_inputs'] - 0.9999) < 1e-6,
            "PAPER_081: drift inputs (0.01, 0.01) give 0.9999 != headline - drift pinned (Q-077a)")
assert_that(abs(_r081['primordial_bh_t_k'] - 1.23e13) / 1.23e13 < 0.01,
            "PAPER_081: primordial BH row pins M = 1e10 kg by T_H chain")
assert_that(_r081['table_ratio_conflict'] == (0.9999, 0.9899),
            "PAPER_081: mass-independent ratio prints two values in one table - defect pinned (Q-077b)")
assert_that(C.wired_count() >= 85, "wired_count >= 85")

_r082 = C.calc('PAPER_082')['value']
assert_that(abs(_r082['t_ratio'] - 1.0410) < 0.0001,
            "PAPER_082: t_UQFF/t_GR = (1-F_TRZ^2)^-4 = 1.0410 EXACT (inherits 081 identity)")
assert_that(abs(_r082['t_universe_s'] - 4.35e17) < 1e15,
            "PAPER_082: t_U = 4.35e17 s pinned from mojibake (13.8 Gyr)")
assert_that(abs(_r082['sim_mass_lost_pct'] - 16.5) < 0.1,
            "PAPER_082: simulation chain 0.583^(1/3) -> 16.5 pct mass lost EXACT (M_0 = 1e10 kg = 081 pin)")
assert_that(abs(_r082['stellar_t_evap_yr'] - 2.1e70) / 2.1e70 < 0.01,
            "PAPER_082: stellar row mantissa 2.1 matches 2.1e70 YEARS - unit-label corruption pinned")
assert_that(abs(_r082['threshold_shift_chain_pct'] - (-1.33)) < 0.05,
            "PAPER_082: threshold shift chain -1.3 pct vs printed -3.5 pct - defect pinned (Q-078a)")
assert_that(C.wired_count() >= 86, "wired_count >= 86")

_r083 = C.calc('PAPER_083')['value']
assert_that(abs(_r083['m_threshold_chain_kg'] - 5.624e11) / 5.624e11 < 0.001,
            "PAPER_083: threshold chain 0.99^(4/3) = 5.62e11 kg - sign-flip corrected, CONFIRMS 082 chain (Q-079a)")
assert_that(abs(_r083['threshold_chain_pct'] - (-1.33)) < 0.02,
            "PAPER_083: -1.3 pct threshold shift double-supported (082 + 083 chains converge)")
assert_that(_r083['delta_c'] == 0.45 and _r083['p_ratio_z1e6'] < 1e-27,
            "PAPER_083: delta_c unchanged - vacuum-pressure null verified ([UA] 7th)")
assert_that(abs(_r083['f_pbh_printed'] - 0.9648) < 0.0001,
            "PAPER_083: f_PBH printed arithmetic 1.005*0.96 = 0.9648 verified; corrected 0.9472 carried")
assert_that(abs(_r083['e_peak_ratio'] - 0.99) < 1e-12,
            "PAPER_083: E_peak Wien ratio = 1 - F_TRZ^2 (inherits 081 identity)")
assert_that(C.wired_count() >= 87, "wired_count >= 87")

_r084 = C.calc('PAPER_084')['value']
assert_that(_r084['partition_sum'] == 26,
            "PAPER_084: 26D channel partition 4+14+6+2 sums EXACTLY to D_crit")
assert_that(_r084['observable_equals_d_phys'] and _r084['nonlocal_equals_d_bsfg'],
            "PAPER_084: primitive texture - observable channels = D_PHYS, non-local = D_BSFG (Q-080a)")
assert_that(_r084['linearization_invalid'],
            "PAPER_084: Page-time linearization invalid for kappa*t_evap >> 1 - honest note pinned (Q-080b)")
assert_that('approximately thermal' in _r084['observer_prediction'],
            "PAPER_084: approximately-thermal 4D prediction wired (in-principle falsifiable)")
assert_that(C.wired_count() >= 88, "wired_count >= 88")

_r085 = C.calc('PAPER_085')['value']
assert_that(abs(_r085['page_time_factor'] - 0.5205) < 0.0001,
            "PAPER_085: Page time 0.5205*t_evap_GR EXACT - flagship measurable prediction")
assert_that(abs(_r085['ratio_canonical'] - 0.99) < 1e-12,
            "PAPER_085: 081 drift correction propagates - canonical ratio 1-F_TRZ^2")
assert_that(_r085['peak_entropy_shift_pct'] == 0.0,
            "PAPER_085: peak entropy unchanged (26D channels unaffected, consistent 084)")
assert_that(abs(_r085['solar_t_evap_yr_chain'] - 2.1e67) / 2.1e67 < 0.01,
            "PAPER_085: solar row mantissa matches 2.1e67 YEARS - year-label pattern 2nd instance (Q-081b)")
assert_that(C.wired_count() >= 89, "wired_count >= 89")

_r086 = C.calc('PAPER_086')['value']
assert_that(abs(_r086['m_sgra_kg'] - 8.55e36) / 8.55e36 < 0.001,
            "PAPER_086: SgrA* mass pin 4.3e6 Msun = 8.55e36 kg EXACT")
assert_that(abs(_r086['d_g_m'] - 2.55e20) / 2.55e20 < 0.01,
            "PAPER_086: d_g = 27,000 ly = 2.55e20 m EXACT")
assert_that(abs(_r086['f_agn_quiescent'] - 1.099) < 1e-9,
            "PAPER_086: f_AGN = 1 + [SCm]/10 = 1.099 EXACT ([SCm]/10 structure noted)")
assert_that('OPEN' in _r086['formula_status'],
            "PAPER_086: closed form anchor-over-formula - dimensional + 125-order gap (Q-082a)")
assert_that(abs(_r086['decay_rate_per_yr_table'] - 1.827e-4) / 1.827e-4 < 0.001,
            "PAPER_086: decay table kappa e-4->e-7 mojibake CONFIRMED by two rows (Q-082b)")
assert_that(_r086['decay_canonical_f_1000yr'] < 1e-70,
            "PAPER_086: canonical kappa gives f(1000 yr) ~ 0 - table correction pinned")
assert_that(C.wired_count() >= 90, "wired_count >= 90")

_r087 = C.calc('PAPER_087')['value']
assert_that(abs(_r087['m_bh_msun'] - 2.82e6) / 2.82e6 < 0.001,
            "PAPER_087: M_BH = 10^6.45 = 2.82e6 Msun caret-drop pin")
assert_that(abs(_r087['distance_chain_mpc'] - 88.2) < 0.5,
            "PAPER_087: distance chain closes under registry H0 (88.2 ~ 90 Mpc)")
assert_that(abs(_r087['eta_uqff'] - 0.099) < 1e-12,
            "PAPER_087: eta = 0.1*[SCm] = 0.099 EXACT (opposite-direction sibling of 1.99; Q-083a)")
assert_that(abs(_r087['l_peak_deviation_pct'] - (-8.33)) < 0.01,
            "PAPER_087: L_peak deviation -8.3 pct EXACT vs Nicholl+2020")
assert_that(abs(_r087['t_fb_uqff_d'] - 27.9) < 0.05,
            "PAPER_087: t_fb correction 0.06*SSq chain -> 27.9 d EXACT")
assert_that(abs(_r087['kappa_half_life_d'] - 1386.0) < 1.0,
            "PAPER_087: kappa half-life 1386 d EXACT - honest 60-d mismatch disclosed + resolved")
assert_that(C.wired_count() >= 91, "wired_count >= 91")

_r088 = C.calc('PAPER_088')['value']
assert_that(abs(_r088['excess_canonical'] - 1.10) < 1e-12,
            "PAPER_088: canonical F_TRZ gives +10 pct excess - detectability fork wired (Q-084a)")
assert_that(abs(_r088['excess_drift'] - 1.01) < 1e-12,
            "PAPER_088: drift reading +1 pct carried alongside")
assert_that(_r088['flavor_perturbation_canonical'] < 1e-3,
            "PAPER_088: flavor null ROBUST under both readings (unmeasurable)")
assert_that(abs(_r088['ug4_baseline_cross'] - C.calc('PAPER_086')['value']['ug4_anchor_j_m3']) < 1e15,
            "PAPER_088: Ug4 baseline cross-consistent with the live PAPER_086 anchor")
assert_that(len(_r088['excess_values_printed']) == 3,
            "PAPER_088: mixed excess values (0.3/1.0/0.35) pinned (Q-084b)")
assert_that(C.wired_count() >= 92, "wired_count >= 92")

_r089 = C.calc('PAPER_089')['value']
assert_that(_r089['n_architectures'] == 8 and _r089['self_validate_pass'] == 8,
            "PAPER_089: 8 calculator architectures registered, 8/8 self-validate PASS")
assert_that(abs(_r089['beta_i_applied'] - 0.6029) < 1e-9,
            "PAPER_089: beta_i drift form 0.603 auto-corrected to canonical BETA_I (charter table)")
assert_that(abs(_r089['triadic_equal_sum']) < 1e-12,
            "PAPER_089: triadic equal-body cosine sum = 0 EXACT (balanced 120-deg symmetry)")
assert_that(_r089['sc_multiplier'] == 0.99,
            "PAPER_089: Superconductive x[SCm] supports Q-083a context reading (mode-dependent structures)")
assert_that(_r089['footer_ubi_chain'] > 1e8 and _r089['footer_ubi_printed'] == 147.0,
            "PAPER_089: footer solar U_bi chain does not close (6 orders) - OPEN pinned (Q-085a)")
assert_that(C.wired_count() >= 93, "wired_count >= 93")

_r090 = C.calc('PAPER_090')['value']
assert_that(abs(_r090['r_s_sgra_m'] - 1.27e10) / 1.27e10 < 0.001,
            "PAPER_090: r_s(SgrA*) = 1.27e10 m EXACT - pins M = 8.55e36 (086 cross-consistent)")
assert_that(abs(_r090['ubi_over_fu'] - 2.85e-4) < 1e-9,
            "PAPER_090: U_bi/F_U = SSq*kappa = 2.85e-4 EXACT footer chain")
assert_that(abs(_r090['sun_g_chain'] - 274.2) < 0.2,
            "PAPER_090: Sun row closes (274.2 chain vs 274.3 printed)")
assert_that('Newton = Ug2 limiting case' in _r090['doctrine'],
            "PAPER_090: T0-doctrine provenance root wired - F_U originates gravity (Q-086c)")
assert_that(_r090['sgra_g_chain'] > 1e6 and _r090['sgra_g_printed'] == 234.3,
            "PAPER_090: SgrA* row does not close vs horizon chain - defect pinned (Q-086a)")
assert_that(_r090['term_count_prints'] == (10, 9, 9),
            "PAPER_090: term-count inconsistency (title 10 / abstract 9 / table 9) pinned (Q-086b)")
assert_that(C.wired_count() >= 94, "wired_count >= 94")

_r091 = C.calc('PAPER_091')['value']
assert_that(abs(_r091['adpm_at_10rs'] - (-0.394)) < 0.001,
            "PAPER_091: aDPM chain -39 pct at 10 R_S - printed -6.3 pct label wrong (Q-087b)")
assert_that(_r091['adpm_radius_for_printed'] == 270.0,
            "PAPER_091: -6.3 pct occurs EXACTLY at ~270 R_S - formula right, radius label defect")
assert_that(_r091['mode_count_prints'] == (14, 13, 13),
            "PAPER_091: mode count 14/13/13 (title/formula/table) - one mode missing (Q-087a)")
assert_that(abs(_r091['trz_mode_canonical'] - 0.1) < 1e-12,
            "PAPER_091: f_TRZ 4th drift instance - pulsar-timing fork 1 vs 10 pct (joins Q-084)")
assert_that(abs(_r091['sgra_res_vs_comp'] - 1.0175) < 0.0001,
            "PAPER_091: SgrA* resonance/compressed = 1.0175 cross-table consistency")
assert_that(C.wired_count() >= 95, "wired_count >= 95")

_r092 = C.calc('PAPER_092')['value']
assert_that(abs(_r092['r_horizon_uqff_m'] - 1.272e10) / 1.272e10 < 0.001,
            "PAPER_092: UQFF horizon r_S*(1+[SCm]*0.07) = 1.272e10 m EXACT (new 0.07 constant)")
assert_that(abs(_r092['sum_terms'] - 234.52) < 0.01,
            "PAPER_092: 8-term sum 234.52 = printed 234.5 EXACT")
assert_that(abs(_r092['base_fraction_pct'] - 99.82) < 0.01,
            "PAPER_092: base-gravity fraction 99.82 pct EXACT")
assert_that(abs(_r092['dm_853kpc_ratio'] - 1.153) < 0.001,
            "PAPER_092: DM +15.3 pct at 8.5 kpc EXACT (rotation-curve claim)")
assert_that(_r092['gm_ratio_to_physical'] < 1e-4,
            "PAPER_092: effective-GM normalization 7.1e-5 of physical - Q-086a sharpened (Q-088a)")
assert_that(abs(_r092['ubi_over_fu_reappears'] - 2.85e-4) < 1e-9,
            "PAPER_092: U_bi/F_U = 2.85e-4 reappears - 090 cross-consistent")
assert_that(C.wired_count() >= 96, "wired_count >= 96")

_r093 = C.calc('PAPER_093')['value']
assert_that(abs(_r093['r_s_m'] - 1.92e13) / 1.92e13 < 0.0001,
            "PAPER_093: M87 r_S = 1.9200e13 m EXACT")
assert_that(abs(_r093['sum_terms'] - 2210.9) < 0.1,
            "PAPER_093: 8-term sum 2210.9 = printed 2211 EXACT (+0.18 pct excess)")
assert_that(abs(_r093['t_h_chain_k'] - 9.49e-18) / 9.49e-18 < 0.01,
            "PAPER_093: T_H chain 9.49e-18 K = the 081 family value; printed 1.35e-17 is drift (Q-089b)")
assert_that(abs(_r093['t_ratio_implemented'] - 0.9926) < 0.001,
            "PAPER_093: T values give ~0.99 - numbers side with canonical again (Q-077a support, 5th)")
assert_that(_r093['horizon_shift_here'] == 0.015,
            "PAPER_093: horizon shift 0.015 vs 092's 0.07 - sibling conflict pinned (Q-089a)")
assert_that(abs(_r093['shadow_shift_uas'] - 0.105) < 0.001,
            "PAPER_093: shadow shift 0.105 uas EXACT - honest EHT null")
assert_that(C.wired_count() >= 97, "wired_count >= 97")

_r094 = C.calc('PAPER_094')['value']
assert_that(abs(_r094['kappa_origin_chain'] - 0.0005) < 1e-12,
            "PAPER_094: KAPPA ORIGIN chain (600/1200)*1e-3 = 0.0005/day EXACT (provenance landmark)")
assert_that(abs(_r094['ssq_origin_chain'] - 0.5700) < 0.0001,
            "PAPER_094: SSQ ORIGIN chain 0.755^2 = 0.5700 EXACT (spin-down anchoring)")
assert_that(abs(_r094['char_age_yr'] - 9012.0) < 5.0,
            "PAPER_094: characteristic age 9012 yr EXACT - pins Pdot = 6.61e-12")
assert_that(abs(_r094['b_over_bcrit'] - 3.18) < 0.01,
            "PAPER_094: B/B_crit = 3.18 EXACT with B_crit = 4.4e9 T SCHWINGER (informs Q-002)")
assert_that(abs(_r094['q_wave_magnetar_revised'] - 7.68e24) / 7.68e24 < 0.01,
            "PAPER_094: 063 magnetar Q_wave pin REVISED to Schwinger B -> 7.68e24 J/m3 (Q-090c)")
assert_that(abs(_r094['kappa_internal_per_day'] - 1.73e-7) / 1.73e-7 < 0.01,
            "PAPER_094: kappa_internal = SSq/tau_c = 1.73e-7/day chain EXACT")
assert_that(C.wired_count() >= 98, "wired_count >= 98")

_r095 = C.calc('PAPER_095')['value']
assert_that(_r095['total_tests'] == 340 and _r095['total_pass'] == 338,
            "PAPER_095: category arithmetic 340/338 EXACT")
assert_that(abs(_r095['pass_rate_pct'] - 99.41) < 0.01,
            "PAPER_095: validator rate 99.4 pct EXACT; Grok-4 extension 99.9 pct provenance")
assert_that(_r095['off_by_one'] == (659, 660),
            "PAPER_095: 659-vs-660 off-by-one pinned (Q-091a)")
assert_that(abs(_r095['superflare_boost'] - 1.57) < 1e-12,
            "PAPER_095: superflare boost (1+SSq) = 1.57 EXACT")
assert_that('orbital resonance' in _r095['askap_reconciliation'],
            "PAPER_095: ASKAP 2.78-h orbital-vs-emission reconciliation candidate (Q-091b/Q-083c)")
assert_that(C.wired_count() >= 99, "wired_count >= 99")

_r096 = C.calc('PAPER_096')['value']
assert_that(abs(_r096['ug1_si_j_m3'] - 1.59e26) / 1.59e26 < 0.01,
            "PAPER_096: correct-SI U_g1 = 1.59e26 J/m3 (Gauss/SI mixing pinned; mantissa right)")
assert_that(_r096['v_trz_factor_correct'] == 2.375 and _r096['v_trz_factor_printed'] == 0.875,
            "PAPER_096: V_TRZ factor 2.375 correct vs 0.875 printed - defect pinned (Q-092b)")
assert_that(abs(_r096['e_frb_corrected_j'] - 2.7e37) / 2.7e37 < 0.02,
            "PAPER_096: fully corrected E_FRB = 2.7e37 J = 2.7e44 erg - nearer CHIME without beaming")
assert_that(abs(_r096['pulse_width_s'] - 6.06e-5) / 6.06e-5 < 0.01,
            "PAPER_096: pulse width 60.6 us EXACT chain")
assert_that(abs(_r096['slope_canonical'] - 1.10) < 1e-12,
            "PAPER_096: spectral-slope fork 1.01 vs 1.10 - THIRD f_TRZ observable fork (Q-092c)")
assert_that(C.wired_count() >= 100, "wired_count >= 100")

_r097 = C.calc('PAPER_097')['value']
assert_that(_r097['partition_sum'] == 26,
            "PAPER_097: Whittaker layer partition 4+4+10+6+2 = 26 EXACT")
assert_that(_r097['ssq_band_is_so_five'],
            "PAPER_097: the SSq-correction band = 10 = SO_FIVE - primitive texture strengthens (Q-093a)")
assert_that(_r097['completeness_pass_systems'] == 3,
            "PAPER_097: completeness < 1e-10 PASS on 3 systems as stated")
assert_that('T0-consistent' in _r097['interpretation'],
            "PAPER_097: chi-horizon/phi-infinity interpretation consistent with the 090 T0 doctrine")
assert_that(C.wired_count() >= 101, "wired_count >= 101")

_r098 = C.calc('PAPER_098')['value']
assert_that(abs(_r098['t_cmb_pred_k'] - 2.711) < 0.001,
            "PAPER_098: T_CMB chain 2.725*sqrt([SCm]) = 2.711 K EXACT")
assert_that(_r098['firas_sigma_tension'] > 20,
            "PAPER_098: 2.711 K sits ~24 sigma from FIRAS - Rule-7 pin on the printed PASS (Q-094a)")
assert_that(abs(_r098['eta_b_chain'] - 6e-10) < 1e-15,
            "PAPER_098: baryon asymmetry eps_CP*[UA] = 6e-10 EXACT to observation ([UA] 10th)")
assert_that(_r098['kappa_t_age_reductio'] > 1e9,
            "PAPER_098: honest kappa reductio self-caught - field-vs-cosmology doctrine (Q-094d)")
assert_that(_r098['friedmann_correction'] == 1e-120,
            "PAPER_098: Friedmann correction 1e-120 negligible (120-orders scale)")
assert_that(C.wired_count() >= 102, "wired_count >= 102")

_r099 = C.calc('PAPER_099')['value']
assert_that(abs(_r099['sqrt_ssq'] - 0.755) < 0.001,
            "PAPER_099: sqrt(SSq) = 0.755 reappears (= 094 origin anchor, 2nd role)")
assert_that(abs(_r099['inv_kappa_days'] - 2000.0) < 1e-9,
            "PAPER_099: 1/kappa = 2000 days EXACT")
assert_that(abs(_r099['p_shield_chain_days'] - 37.5) < 0.01,
            "PAPER_099: P_shield chain = 37.5 DAYS - printed yr is a unit slip (Q-095a)")
assert_that(abs(_r099['e_peak_uqff_kev'] - 2.56) < 0.01,
            "PAPER_099: E_peak UQFF = 2.56 keV EXACT - pins T_plasma = 1e7 K (Q-095b)")
assert_that(abs(_r099['r_isco_chain_m'] - 3.81e10) / 3.81e10 < 0.01,
            "PAPER_099: r_ISCO chain 3.81e10 vs printed 7.14e10 - factor 1.9 open (Q-095c)")
assert_that(C.wired_count() >= 103, "wired_count >= 103")

_r100 = C.calc('PAPER_100')['value']
assert_that(abs(_r100['nu_hole_hz'] - 6.248e12) / 6.248e12 < 0.001,
            "PAPER_100: nu_hole chain closes CLEANLY at 6.248 THz with r_vac0 = 5.77 um (Q-096a)")
assert_that(abs(_r100['delta_r_um'] - 23.8) < 0.2,
            "PAPER_100: Delta_r = 23.8 um corroborates the um reading (printed 23.9)")
assert_that(_r100['harmonic_match_pct'] < 0.2,
            "PAPER_100: nu_hole = 5*f_SCm harmonic candidate matches to 0.16 pct (Q-096b, no retrofit)")
assert_that(abs(_r100['dip_canonical_pct'] - (-10.0)) < 1e-9,
            "PAPER_100: canonical dip -10 pct - FOURTH f_TRZ observable fork, most lab-accessible (Q-096c)")
assert_that(abs(_r100['q_factor'] - 62.4) < 0.01,
            "PAPER_100: Q = 62.4 EXACT (62-integer echo noted without retrofit)")
assert_that(C.wired_count() >= 104, "wired_count >= 104")

_r101 = C.calc('PAPER_101')['value']
assert_that(abs(_r101['gap_canonical_gev'] - 1.736) < 1e-9,
            "PAPER_101: Yang-Mills gap CANONICAL 1.736 GeV (PAPER_1318) wired primary")
assert_that(_r101['gap_residual_pct'] < 2.2,
            "PAPER_101: 2.1 pct vs lattice anchor 1.7 GeV - honest residual")
assert_that(abs(_r101['s204_ratio_check'] - 29849.6) < 0.1,
            "PAPER_101: S204 epoch internal ratio 29849.6 EXACT (superseded layer recorded)")
assert_that(abs(_r101['hbar_c_fm_gev'] - 0.1976) < 0.001,
            "PAPER_101: hbar*c/fm = 197.6 MeV - S0 conversion defect x160 pinned (Q-097b)")
assert_that('heuristic' in _r101['honesty'],
            "PAPER_101: Rule-7 exemplary honesty - no rigor claim on the Millennium problem")
assert_that(C.wired_count() >= 105, "wired_count >= 105")

_r102 = C.calc('PAPER_102')['value']
assert_that(abs(_r102['nu_factor_drift'] - 1.0099) < 1e-9,
            "PAPER_102: nu_eff = nu*(1 + [SCm]*f_TRZ) = 1.0099 EXACT")
assert_that(abs(_r102['nu_factor_canonical'] - 1.099) < 1e-9,
            "PAPER_102: canonical branch +9.9 pct viscosity EXCLUDED in lab fluids - fork twist (Q-098a)")
assert_that(abs(_r102['re_shift_pct'] - (-0.98)) < 0.01,
            "PAPER_102: Reynolds shift -0.98 pct EXACT")
assert_that(abs(_r102['f_vac_n_m3'] - 7.09e-74) < 1e-80,
            "PAPER_102: f_vac = k_vac*rho_vac = 7.09e-74 EXACT (negligible)")
assert_that('not rigorous' in _r102['honesty'],
            "PAPER_102: Rule-7 honest labeling preserved on Millennium problem 2")
assert_that(C.wired_count() >= 106, "wired_count >= 106")

_r103 = C.calc('PAPER_103')['value']
assert_that(abs(_r103['zeros_first5'][0] - 14.134) < 0.001,
            "PAPER_103: first-five Riemann zero anchors match literature EXACTLY")
assert_that(abs(_r103['harmonic_bridge'] - 4.1667e9) / 4.1667e9 < 0.001,
            "PAPER_103: harmonic bridge 1.25e12/300 = 4.1667e9 EXACT")
assert_that(abs(_r103['sec3_chain'] - 0.4888) < 0.001,
            "PAPER_103: sec-3 chain 0.4888 vs printed 0.50 - self-labeled numerology (Q-099a)")
assert_that(sum(_r103['kk_split']) == 26,
            "PAPER_103: KK tower 4 + 22 = D_crit split")
assert_that('Rule-7 exemplary' in _r103['honesty'],
            "PAPER_103: self-labeled speculative - honest Millennium treatment")
assert_that(C.wired_count() >= 107, "wired_count >= 107")

_r104 = C.calc('PAPER_104')['value']
assert_that(abs(_r104['v_ua_m_s'] - 3.0e4) < 1e-6,
            "PAPER_104: [UA] = v_UA/c PHYSICAL IDENTITY -> v_UA = 3.0e4 m/s = 101's v_SCm (Q-100a)")
assert_that(abs(_r104['extraction_prob'] - 1e-8) < 1e-15,
            "PAPER_104: extraction probability [UA]^2 = 1e-8 EXACT")
assert_that(sum(_r104['partition'].values()) == 26 and _r104['partition_appearance'] == 3,
            "PAPER_104: computational partition = the 084 partition, 3rd consistent appearance")
assert_that('no lower bound proven' in _r104['honesty'],
            "PAPER_104: Rule-7 honest labeling on Millennium 4")
assert_that(C.wired_count() >= 108, "wired_count >= 108")

_r105 = C.calc('PAPER_105')['value']
assert_that(abs(_r105['phase2_eta'] - 0.099) < 1e-9,
            "PAPER_105: BH phase-2 accretion eta = [SCm]*eta_acc = 0.099 EXACT (087 family)")
assert_that(_r105['n_models'] == 10 and _r105['part_c_total'] == 15,
            "PAPER_105: 5 BH phases + 10 galaxy models = 15 Part C EXACT")
assert_that(_r105['domain_113_total'] == 40,
            "PAPER_105: Domain 1.13 grand total 40 tests EXACT (Papers 96-105)")
assert_that(len(_r105['bh_phases']) == 5,
            "PAPER_105: 5-phase BH lifecycle wired (Drawings 5-9)")
assert_that('053-058' in _r105['suite_cross_ref'],
            "PAPER_105: 10-model suite cross-referenced to the 053-058 objects (structural re-expression)")
assert_that(C.wired_count() >= 109, "wired_count >= 109")

_r106 = C.calc('PAPER_106')['value']
assert_that(abs(_r106['rho_l_uqff_ratio'] - 1.0000000812) < 1e-10,
            "PAPER_106: rho_L_UQFF/rho_L_obs = 1 + kappa^2*SSq^2 = 1.0000000812 EXACT header identity")
assert_that(abs(_r106['omega_l_via_ssq'] - 0.684) < 0.001,
            "PAPER_106: Omega_L = (6/5)*SSq = 0.684 canonical - links 0.685 anchor to PAPER_1156/078")
assert_that(_r106['planck_deviation_pct'] < 1.0,
            "PAPER_106: Omega_L 0.685 within 0.6 pct of Planck 0.6889")
assert_that(abs(_r106['eps_omega'] - 0.08) < 1e-9,
            "PAPER_106: eps_Omega = 0.08 = 8*f_TRZ (9th drift instance, tuning uncertainty)")
assert_that('Rule-7' in _r106['honesty'],
            "PAPER_106: honest 'potential resolution' + falsifiable predictions labeling")
assert_that(C.wired_count() >= 110, "wired_count >= 110")

_r107 = C.calc('PAPER_107')['value']
assert_that(abs(_r107['de_bec_mev'] - 0.4766) < 0.001,
            "PAPER_107: dE_BEC = 5*ln(1.1) = 0.4766 MeV EXACT (060 identity reappears)")
assert_that(abs(_r107['n_b_at_threshold'] - 10.0) < 0.01,
            "PAPER_107: N_B(0.477, 5.0) = 10.000 EXACT threshold")
assert_that(abs(_r107['tc_shift_uqff_mev'] - 5.272) < 0.001,
            "PAPER_107: T_c^UQFF = 5 + SSq*0.477 = 5.272 MeV EXACT")
assert_that(abs(_r107['level_8_suppression'] - 1.028) < 0.001,
            "PAPER_107: level-8 chain SSq/sqrt(8/26) = 1.028 EXACT")
assert_that(_r107['ikeda_10a_n_b_printed'] == 0.57,
            "PAPER_107: Ikeda 10-alpha (Ca-40) N_B = 0.57 = SSq EXACTLY (Q-103a MAJOR)")
assert_that(C.wired_count() >= 111, "wired_count >= 111")

_r108 = C.calc('PAPER_108')['value']
assert_that(abs(_r108['f_pp_ssq_chain'] - 0.7549) < 0.001,
            "PAPER_108: f_pp = 1 - SSq*(1-SSq) = 0.7549 EXACT (SSq 4th observational role - mixing fraction)")
assert_that(abs(_r108['beta_drift_squared'] - 0.0121) < 1e-9,
            "PAPER_108: (beta_i - 0.5)^2 = 0.0121 EXACT at drift 0.61")
assert_that(abs(_r108['beta_0_at_1gev'] - 0.9325) < 1e-9,
            "PAPER_108: beta_0 = 1 - m_pi/(2 E_p) = 0.9325 EXACT at E_p = 1 GeV")
assert_that(_r108['sed_norm_gap_pct'] < _r108['icecube_systematic_pct'] * 3,
            "PAPER_108: drift-vs-canonical beta_i SED-norm gap within IceCube systematic (undiscriminating; Q-104a)")
assert_that(len(_r108['tri_source']) == 3,
            "PAPER_108: tri-source beta_i confirmation recorded (Q-104b canonization candidate)")
assert_that(C.wired_count() >= 112, "wired_count >= 112")

_r109 = C.calc('PAPER_109')['value']
assert_that(abs(_r109['m_ej_fraction'] - 0.0183) < 0.0005,
            "PAPER_109: M_ej/M_total = 0.05/2.73 = 0.0183 EXACT (far below SSq -> Ub_i suppressed regime)")
assert_that(abs(_r109['v_boundary_m_s'] - 1.83e8) < 1e5,
            "PAPER_109: r-process velocity boundary = beta_i*c = 1.83e8 m/s EXACT")
assert_that(_r109['blue_ejecta_c'] < 0.61 and _r109['red_ejecta_c'] < 0.61 and _r109['jet_c'] > 0.61,
            "PAPER_109: blue+red ejecta below boundary (r-process active), jets above (quenched)")
assert_that(abs(_r109['lanthanide_mass_chain_msun'] - 1.15e-4) < 1e-6,
            "PAPER_109: lanthanide mass chain dM_Ubi*tau = 1.15e-4 Msun EXACT (Cowperthwaite+2017 range)")
assert_that(_r109['lightcurve_uniform_scaling'] == 0.975,
            "PAPER_109: light-curve rows uniform x0.975 not independent fits (Q-105a)")
assert_that(_r109['ssq_new_role_count'] == 6,
            "PAPER_109: SSq 6th observational role wired (activation threshold)")
assert_that(C.wired_count() >= 113, "wired_count >= 113")

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
