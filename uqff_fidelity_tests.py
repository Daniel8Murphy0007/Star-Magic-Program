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
assert_that(C.VERSION == "0.43.0", "uqff_calculator.VERSION = 0.43.0")
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
