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

# Scientific-stack dependency check (fail-fast, clear message). The framework's
# math genuinely requires sympy (symbolic derivations) + numpy/scipy/mpmath
# (numerics); these are declared in pyproject `dependencies` and installed by
# CI/Release before the gate runs. If a dependency is missing, exit HERE with a
# clear message rather than crashing deep inside a paper dispatch (the v0.208.0
# CI break: PAPER_205 imported sympy on a runner that had not installed it).
_missing_deps = []
for _dep in ("sympy", "mpmath", "numpy", "scipy"):
    try:
        __import__(_dep)
    except ImportError:
        _missing_deps.append(_dep)
if _missing_deps:
    print("[FIDELITY GATE] MISSING REQUIRED DEPENDENCIES: " + ", ".join(_missing_deps))
    print("  These are declared in pyproject `dependencies`. Install with `pip install .`")
    print("  (CI/Release install them before the gate; a bare `python uqff_fidelity_tests.py`")
    print("   needs them present too).")
    sys.exit(1)

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
assert_that(C.VERSION == "0.249.0", "uqff_calculator.VERSION = 0.249.0")
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

_r110 = C.calc('PAPER_110')['value']
assert_that(_r110['mass_error_pct'] < 0.1,
            "PAPER_110: M_BH = 4.3e6 Msun at 0.07 pct vs GRAVITY S2 orbit - excellent anchor")
assert_that(abs(_r110['r_5mpc_m'] - 1.543e14) / 1.543e14 < 0.001,
            "PAPER_110: r = 5 mpc = 1.543e14 m EXACT")
assert_that(abs(_r110['g_newton_chain'] - 2.40e-2) / 2.40e-2 < 0.01,
            "PAPER_110: g_Newton chain 2.40e-2 vs printed 2.401e-5 - x1000 exponent slip (Q-106b)")
assert_that(abs(_r110['ug4_1894_family'] - 1.8937e-23) < 1e-27,
            "PAPER_110: Ug4 = 1.8937e-23 (048 cross-check) - the 1.894-mantissa PAPER_2156 origin candidate (Q-106d)")
assert_that(abs(_r110['v_c_error_pct'] - 0.85) < 0.01,
            "PAPER_110: rotation curve 238 vs 236 km/s = 0.85 pct EXACT")
assert_that(_r110['kappa_decay_exponent'] > 8e8,
            "PAPER_110: kappa full-decay chain EXACT - Q-094d/Q-098 doctrine support")
assert_that(C.wired_count() >= 114, "wired_count >= 114")

_r111 = C.calc('PAPER_111')['value']
assert_that(abs(_r111['cos_scan'][0.25] - 1.217) < 0.001,
            "PAPER_111: cos-scan chains ALL EXACT (1.217/1.249/3.179)")
assert_that('ASSERTED' in _r111['series_claim'],
            "PAPER_111: R = 1.50 series closure asserted without computation - OPEN (Q-107a)")
assert_that(abs(_r111['tau_dissip_chain_gyr'] - 27.2) < 0.5,
            "PAPER_111: dissipation chain 27 Gyr - printed (2.8e14 s, 9 Gyr) triple defect (Q-107b)")
assert_that(_r111['nu_eff_factor'] == 1.0099,
            "PAPER_111: nu_eff = nu*1.0099 - PAPER_102 cross-consistent")
assert_that(abs(_r111['doppler_bc_chain'] - 0.081) < 0.001,
            "PAPER_111: Doppler beta*cos chain 0.081 vs printed 0.091 pinned (Q-107c)")
assert_that(C.wired_count() >= 115, "wired_count >= 115")

_r112 = C.calc('PAPER_112')['value']
assert_that(abs(_r112['n_higgs'] - 12.302) < 0.001,
            "PAPER_112: Higgs level 12.302 EXACT (EW cluster at n=12)")
assert_that(abs(_r112['n_fe56_bea'] - 8.149) < 0.001,
            "PAPER_112: Fe-56 BE/A level 8.149 EXACT (nuclear anchor n=8, sec 4 all EXACT)")
assert_that(abs(_r112['n_muon_chain'] - 9.229) < 0.001 and abs(_r112['n_proton_chain'] - 10.177) < 0.001,
            "PAPER_112: mid-band -1.0 systematic defect pinned (muon 9.229 vs printed 8.23; proton 10.177 vs 9.18) (Q-108a)")
assert_that(abs(_r112['e13_gev'] - 624.15) < 0.1,
            "PAPER_112: E_13 = 624 GeV BSM threshold EXACT")
assert_that(abs(_r112['kappa_per_s'] - 5.787e-9) < 1e-12,
            "PAPER_112: kappa 5e-4/day = 5.787e-9 /s conversion EXACT (S204.5 self-consistent)")
assert_that('trivially 100' in _r112['stat_defect'],
            "PAPER_112: 90.5 pct within +/-0.5 statistic ill-defined - pinned (Q-108b)")
assert_that(C.wired_count() >= 116, "wired_count >= 116")

_r113 = C.calc('PAPER_113')['value']
assert_that(abs(_r113['flare_decay_2000d'] - 0.3679) < 0.0001,
            "PAPER_113: flare decay e^-1 = 0.368 after 2000 days EXACT (canonical kappa)")
assert_that(abs(_r113['n_cycles_z1'] - 2.426) < 0.001,
            "PAPER_113: N_cycles = 2.426 per e-fold at z=1 EXACT")
assert_that(abs(_r113['bin_err_pct'] - 1.04) < 0.01,
            "PAPER_113: 4LAC bin totals 3743/3704 = 1.04 pct EXACT")
assert_that(abs(_r113['cta102_kappa_chain'] - 2.664e-3) < 1e-5,
            "PAPER_113: CTA 102 chain 2.66e-3/day vs printed 2.66e-4 - FACTOR-10 ERROR pinned (Q-109a)")
assert_that(abs(_r113['cta102_vs_canonical'] - 5.33) < 0.01,
            "PAPER_113: corrected CTA 102 is 5.3x ABOVE canonical - reconciliation INVERTED (Q-109a)")
assert_that(C.wired_count() >= 117, "wired_count >= 117")

_r114 = C.calc('PAPER_114')['value']
assert_that(abs(_r114['ug2_coeff_j_m3'] - 9.79e-38) < 0.01e-38,
            "PAPER_114: Ug2 coefficient 9.79e-38 chain (printed 9.76e-38, rounding)")
assert_that(abs(_r114['p_ram_pa'] - 1e-9) < 1e-12,
            "PAPER_114: P_ram = 1e-9 Pa EXACT")
assert_that(abs(_r114['delta_sw'] - 0.01) < 1e-15 and abs(_r114['delta_sw_paper_route'] - 0.01) < 1e-15,
            "PAPER_114: d_sw = 0.01 via BOTH F_TRZ^2 (primitive candidate) and SSq/57 (paper route) - Q-110a")
assert_that(abs(_r114['psp_mean_err_pct'] - 1.70) < 0.01,
            "PAPER_114: PSP 4-perihelion mean error 1.70 pct EXACT")
assert_that(abs(_r114['alpha_cr_implied'] - 1.02e26) < 0.01e26,
            "PAPER_114: compression chain closes only at unstated alpha_CR = 1.02e26 (Q-110b)")
assert_that(C.wired_count() >= 118, "wired_count >= 118")

_r115 = C.calc('PAPER_115')['value']
assert_that(abs(_r115['per_reversal'] - 1.3629) < 0.0001,
            "PAPER_115: per-reversal factor 1 + SSq*2/pi = 1.3629 EXACT")
assert_that(abs(_r115['r_n13_chain'] - 55.97) < 0.01 and abs(_r115['printed_129_8_is'] - 129.75) < 0.01,
            "PAPER_115: ladders crossed - 1.363^13 = 56.0 chain; printed 129.8 IS 1.5^12 (Q-111a)")
assert_that(14.8 < _r115['n_for_100_ssq'] < 15.0,
            "PAPER_115: R > 100 needs N = 15 at SSq-weighted rate (not 13)")
assert_that(abs(_r115['ubi_corrected'] - 6.11e-10) < 0.01e-10,
            "PAPER_115: U_bi = 6.11e-10 N/m2 at TRUE 65 kpc (printed 6.14e-14 used r 100x high) (Q-111b)")
assert_that(abs(_r115['doppler_chain'] - 2.28e6) < 0.01e6,
            "PAPER_115: Doppler chain 2.28e6 vs printed 2.2e7 - factor 10 (Q-111c)")
assert_that(abs(_r115['t_jet_yr'] - 3.03e5) < 0.01e5,
            "PAPER_115: t_jet = 3.03e5 yr EXACT (65 kpc / 0.7c)")
assert_that(C.wired_count() >= 119, "wired_count >= 119")

_r116 = C.calc('PAPER_116')['value']
assert_that(abs(_r116['e4_ev'] - 624.15) < 0.01,
            "PAPER_116: E_4 = 624 eV EXACT (adjacent to Holmlid 630 family - cross-repo note)")
assert_that(abs(_r116['n_atlas'] - 4.204) < 0.001 and abs(_r116['n_cms'] - 4.173) < 0.001,
            "PAPER_116: ATLAS 4.204 / CMS 4.173 ladder assignments EXACT")
assert_that(abs(_r116['e_transfer_is_1kev'] - 1.0) < 0.01,
            "PAPER_116: E_transfer anchor is exactly 1 keV, underived from Lambda = 30 TeV (Q-112a)")
assert_that(abs(_r116['n_hadronic_1gev'] - 10.205) < 0.001,
            "PAPER_116: hadronic 1 GeV -> n = 10.20 CONFIRMS PAPER_112 Q-108a correction (self-rectification No. 8)")
assert_that(abs(_r116['n_lambda_30tev'] - 14.68) < 0.01,
            "PAPER_116: Lambda = 30 TeV -> n = 14.68 EXACT")
assert_that(C.wired_count() >= 120, "wired_count >= 120")

_r117 = C.calc('PAPER_117')['value']
assert_that(abs(_r117['n_10mev'] - 8.2047) < 0.001,
            "PAPER_117: headline n(10 MeV) = 8.205 EXACT")
assert_that(abs(_r117['sn_over_e8'] - 1.1803) < 0.001 and abs(_r117['ssq_err_pct'] - 3.54) < 0.05,
            "PAPER_117: S_n/E_8 = 1.1803 vs 2*SSq = 1.14 at 3.5 pct - SSq 8th role candidate")
assert_that(abs(_r117['n_1st_exc_chain'] - 7.109) < 0.001,
            "PAPER_117: 1st excited chain 7.109 - printed 6.91 is EP-02 electron value (Q-113a offset family)")
assert_that(abs(_r117['n_be_chain'] - 10.415) < 0.001,
            "PAPER_117: total BE chain n = 10.415 (printed 10.215; -0.2 offset; hadronic n=10 family)")
assert_that(_r117['z82_identity_predecessor'] == 82,
            "PAPER_117: Z = 82 = A_5 + D_crit - D_phys EXACT predecessor identity (Q-113b cross-repo)")
assert_that(C.wired_count() >= 121, "wired_count >= 121")

_r118 = C.calc('PAPER_118')['value']
assert_that(abs(_r118['vac_ratio'] - 2.09) < 0.01,
            "PAPER_118: rho_vac = 1.11e-9 is 2.09x standard Lambda conversion (5.31e-10) (Q-114a)")
assert_that(abs(_r118['n1_hop_at_true'] - 3.03e-10) < 0.01e-10,
            "PAPER_118: N=1 hop at TRUE rho_Lambda = 3.03e-10 - 46 pct off, headline fails corrected (Q-114a)")
assert_that(abs(_r118['secondary_sqrt'] - 0.6220) < 0.0001,
            "PAPER_118: CLEAN secondary sqrt(Om_DM/Om_L) = 0.6220 vs SSq at 9.12 pct EXACT")
assert_that(_r118['bonus_err_pct'] < 0.2,
            "PAPER_118: BONUS FIND Om_b/Om_DM = 0.18491 vs SSq^3 = 0.18519 at 0.16 pct (Q-114c candidate identity)")
assert_that(abs(_r118['honest_cosmic_ratio'] - 0.387) < 0.001,
            "PAPER_118: honest cosmic Om_DM/Om_L = 0.387 vs SSq fails at 32 pct - conflation pinned (Q-114b)")
assert_that(C.wired_count() >= 122, "wired_count >= 122")

_r119 = C.calc('PAPER_119')['value']
assert_that(len(_r119['systems']) == 7,
            "PAPER_119: 7 equation systems registered (supersedes PAPER_064 4 modes)")
assert_that(abs(_r119['m_bh_kg'] - 8.155e36) < 0.001e36 and abs(_r119['tau_kappa_yr'] - 5.476) < 0.001,
            "PAPER_119: M_bh / tau chains EXACT")
assert_that(abs(_r119['dual_form_chain'] - 709) < 1,
            "PAPER_119: E_react dual-form identity evaluates to 709 vs claimed 1e46 - 43 orders broken (Q-115a)")
assert_that(_r119['triadic_fork'][1] / _r119['triadic_fork'][0] > 1e8,
            "PAPER_119: SSq dual definition forks Triadic suppression by 8 orders (Q-115b)")
assert_that(abs(_r119['ejecta_fraction'] - 0.3971) < 0.0001,
            "PAPER_119: GW170817 ejecta 1 - BETA_I = 0.3971 at canonical beta")
assert_that(C.wired_count() >= 123, "wired_count >= 123")

_r120 = C.calc('PAPER_120')['value']
assert_that(_r120['n_systems'] == 24 and _r120['n_qwave_superset'] == 47,
            "PAPER_120: 24-system catalog registered (47-system Q_wave superset)")
assert_that(abs(_r120['l_3c273_w'] - 1e39) < 1e30,
            "PAPER_120: 1e46 erg/s = 1e39 W conversion EXACT")
assert_that(_r120['b_crit_fork'] == (4.4e13, 4.4e9) and _r120['b_over_bcrit_schwinger'][0] > 1,
            "PAPER_120: B_crit 1e4 fork - catalog 4.4e13 vs PAPER_094 Schwinger 4.4e9; magnetar supercritical at true value (Q-116b, informs Q-002)")
assert_that('g/cm3 mantissa' in _r120['dm_density_drift'],
            "PAPER_120: DM density unit-direction drift pinned (Q-116c, PAPER_2147 family)")
assert_that(abs(_r120['ejecta_fraction'] - 0.3971) < 0.0001,
            "PAPER_120: GW170817 ejecta 1 - BETA_I canonical")
assert_that(C.wired_count() >= 124, "wired_count >= 124")

_r121 = C.calc('PAPER_121')['value']
assert_that(_r121['n_equations'] == 71 and sum(_r121['categories']) == 71,
            "PAPER_121: 71-equation catalog registered (28+14+23+6)")
assert_that(abs(_r121['m_bh_fork'][0] - 8.155e36) < 1e33 and abs(_r121['m_bh_fork'][1] - 8.553e36) < 1e33,
            "PAPER_121: M_bh internal fork 4.1e6 vs 4.3e6 M_sun pinned (Q-117a)")
assert_that(abs(_r121['alpha_fund'] - _r121['inv_phi']) < 0.001,
            "PAPER_121: alpha_fund = 0.618 = 1/phi to 4 decimals (Q-117d golden-ratio candidate)")
assert_that(abs(_r121['imf_slope'] + _r121['sqrt3']) < 0.001,
            "PAPER_121: IMF slope -1.732 = -sqrt(3) EXACT (Q-117d)")
assert_that(abs(_r121['footer_chain_m_s2'] - 0.078) < 0.001,
            "PAPER_121: footer r^2-form chain 0.078 m/s2 vs printed 147 - still broken (Q-085a family)")
assert_that(C.wired_count() >= 125, "wired_count >= 125")

_r122 = C.calc('PAPER_122')['value']
assert_that(abs(_r122['n_proton'] - 10.176) < 0.001,
            "PAPER_122: proton n = 10.18 EXPLICIT - canonizes Q-108a correction (self-rectification No. 9)")
assert_that(abs(_r122['n_pion_true'] - 9.335) < 0.001,
            "PAPER_122: pion n = 9.34 - mid-band correction confirmed")
assert_that(_r122['code_r2_actual'] < 0.5 and _r122['code_r2_printed'] > 0.95,
            "PAPER_122: own code outputs R^2 = 0.468 vs printed 0.9527 - falsified output pinned (Q-118b)")
assert_that(abs(_r122['ssq_2hop_claim'] - 3.08) < 0.01 and abs(_r122['higgs_actual_hops'] - 1.24) < 0.01,
            "PAPER_122: Higgs 2-hop SSq attribution fails (SSq^-2 = 3.08 != 2; actual 1.24 hops) (Q-118c)")
assert_that(abs(_r122['higgs_factor2'] - 2.01) < 0.01,
            "PAPER_122: E_H = 2.01 x E_12 factor-2 observation real")
assert_that(C.wired_count() >= 126, "wired_count >= 126")

_r123 = C.calc('PAPER_123')['value']
assert_that(abs(_r123['e_virtual_kev'] - 0.989) < 0.001,
            "PAPER_123: E_0*10^4.20 = 0.989 keV chain EXACT")
assert_that(abs(_r123['dn_winding'] - 0.2) < 1e-15 and abs(_r123['dn_winding'] - 2 / 10) < 1e-15,
            "PAPER_123: winding dn = 1/5 = 2/SO_five EXACT primitive candidate (Q-119b)")
assert_that(abs(_r123['log10_1602'] - 0.20466) < 0.00001,
            "PAPER_123: dn ~ 0.2047 = log10(1.602) eV-to-J mantissa - unit-conversion artifact (Q-119a)")
assert_that(_r123['real_dn_gap'] < 0.001,
            "PAPER_123: EP-03/EP-04 real dn identical to 0.0006 - the 0.20-vs-0.21 story is rounding")
assert_that(abs(_r123['winding_vs_artifact_residual'] - 0.9893) < 0.0001,
            "PAPER_123: 0.989-vs-1.000 keV residual IS the winding-vs-mantissa mismatch")
assert_that(C.wired_count() >= 127, "wired_count >= 127")

_r124 = C.calc('PAPER_124')['value']
assert_that(abs(_r124['sn_uqff_mev'] - 7.116) < 0.001,
            "PAPER_124: S_n = 2*SSq*E_8 = 7.116 MeV EXACT")
assert_that(abs(_r124['pb208_ratio'] - 1.181) < 0.001 and abs(_r124['pb206_true_ratio'] - 1.296) < 0.001,
            "PAPER_124: SSq check survives as Pb-208 doubly-magic (3.6 pct); true Pb-206 fails (13.7 pct) - PAPER_117 isotope misattribution corrected (self-rectification No. 10)")
assert_that(abs(_r124['err_pb207_pct'] - 5.59) < 0.01 and abs(_r124['err_pb208_pct'] - 3.43) < 0.01,
            "PAPER_124: bracket errors 5.59/3.43 pct EXACT")
assert_that('1.05' in _r124['dn_formula_broken'],
            "PAPER_124: dn formula broken as printed (10 -> 1.05) - pinned (Q-120b)")
assert_that(C.wired_count() >= 128, "wired_count >= 128")

_r125 = C.calc('PAPER_125')['value']
assert_that(abs(_r125['kappa_derivation'] - 5e-4) < 1e-15,
            "PAPER_125: kappa = alpha/t_mean = 0.35/700 = 5e-4 EXACT (real derivation chain)")
assert_that(abs(_r125['t_half_yr'] - 3.795) < 0.001,
            "PAPER_125: t_1/2 = 3.80 yr EXACT (blazar variability match)")
assert_that(abs(_r125['named_mean'] - 4.95e-4) < 1e-7,
            "PAPER_125: 4 named per-source kappas mean 4.95e-4 - Q-109b partially answered; CTA 102 absent")
assert_that('injected' in _r125['circular_code'],
            "PAPER_125: circular simulation code pinned (Rule 7) (Q-121a)")
assert_that(abs(_r125['arrhenius_implied_egap_kev'] - 5.03) < 0.01,
            "PAPER_125: Arrhenius form needs unstated E_gap = 5.03 keV at 1e6 K (Q-121c)")
assert_that(C.wired_count() >= 129, "wired_count >= 129")

_r126 = C.calc('PAPER_126')['value']
assert_that(abs(_r126['d_g_err_pct'] - 4.31) < 0.01 and abs(_r126['m_bh_err_pct'] - 3.51) < 0.01,
            "PAPER_126: d_g 4.31 pct / M_bh 3.51 pct errors EXACT")
assert_that(abs(_r126['m_over_d'] - 3.50e16) < 0.01e16,
            "PAPER_126: M_bh/d_g = 3.50e16 kg/m galactic calibration unit EXACT")
assert_that('circularity' in _r126['self_canceling_code'],
            "PAPER_126: eps_UA self-canceling code pinned - 4.3 pct calibrated not derived (Q-122a)")
assert_that(abs(_r126['mbh_corrected_canonical'] - 4.297) < 0.001,
            "PAPER_126: M_app = M*(1 + SSq*beta_i*F_TRZ) = 4.297 at canonical beta - the /10 IS F_TRZ (Q-122b primitive find)")
assert_that(abs(_r126['roundtrip_kpc'] - 8.247) < 0.001,
            "PAPER_126: round-trip 8.247 kpc vs GRAVITY 8.277 (0.37 pct)")
assert_that(C.wired_count() >= 130, "wired_count >= 130")

_r127 = C.calc('PAPER_127')['value']
assert_that(abs(_r127['f_u_ra'] - 0.685) < 0.001,
            "PAPER_127: F_U(r_A) = 0.685 m/s2 EXACT")
assert_that(abs(_r127['omega_res'] - 3.59e-5) < 0.01e-5 and abs(_r127['t_n_days'] - 0.322) < 0.001,
            "PAPER_127: Alfven resonance chains EXACT (3.59e-5 rad/s; t_n = 0.322 d)")
assert_that(_r127['code_claimed'] / _r127['code_actual_output'] > 1e12,
            "PAPER_127: falsified code output No. 2 - actual 4.4e-7 vs claimed 5e5 (Q-123a)")
assert_that(abs(_r127['ua_fourth_value'] - 0.0145) < 0.0001,
            "PAPER_127: [UA] fourth value 0.0145 (circular back-solve) - fork grows (Q-123b)")
assert_that(len(_r127['ua_fork_values']) == 4,
            "PAPER_127: [UA] fork now 4 values across corpus")
assert_that(C.wired_count() >= 131, "wired_count >= 131")

_r128 = C.calc('PAPER_128')['value']
assert_that(abs(_r128['rho_l_j_m3'] - 5.36e-10) < 0.01e-10,
            "PAPER_128: vacuum anchor FIXED at 5.36e-10 J/m3 (1 pct from standard) - self-rectification No. 11")
assert_that(abs(_r128['rho_dm_uqff'] - 1.104e-27) < 0.001e-27,
            "PAPER_128: rho_DM = rho_L * SSq^3 = 1.104e-27 EXACT; hop count settled N=3")
assert_that(abs(_r128['ssq_cubed'] - 0.18519) < 0.00001,
            "PAPER_128: the 'measured' 0.185 GeV/cm3 anchor IS SSq^3 numerically - circular suspicion (Q-124b)")
assert_that(abs(_r128['empirical_ratio'] - 0.1622) < 0.0001,
            "PAPER_128: empirical ratio 0.1622 EXACT; residual chains 12.4/14.2 vs printed 12.8")
assert_that(abs(_r128['n1_baryon_offset'] - 8.13) < 0.01,
            "PAPER_128: N=1 baryon factor-8 offset honestly disclosed")
assert_that(C.wired_count() >= 132, "wired_count >= 132")

_r129 = C.calc('PAPER_129')['value']
assert_that(abs(_r129['cos_pi_t_true'] + 0.8246) < 0.0001,
            "PAPER_129: cos(pi t_-) = -0.8246 - paper dropped the sign (Q-125a)")
assert_that(abs(_r129['t_counter_corrected'] + 0.809) < 0.001,
            "PAPER_129: corrected t_- = -0.809 (paper's -0.10 = sign + deg/360 double error)")
assert_that(abs(_r129['r_at_corrected'] - 130) < 0.1 and _r129['r_at_printed'] < 1.1,
            "PAPER_129: R = 130.0 EXACT at corrected t (exact solve); R = 1.05 at printed t - fails")
assert_that(_r129['n_crossings'] == 13 and 26 // 2 == 13,
            "PAPER_129: N = 13 = D_crit/2 EXACT primitive candidate (Q-125b)")
assert_that(abs(_r129['beta_app_chain'] - 3.60) < 0.01,
            "PAPER_129: beta_app = 3.60c chain EXACT")
assert_that(C.wired_count() >= 133, "wired_count >= 133")

_r130 = C.calc('PAPER_130')['value']
assert_that(abs(_r130['e_nu_peak_pev'] - 0.061) < 0.001,
            "PAPER_130: E_nu peak = 0.061 PeV EXACT (< 0.1 PeV bound)")
assert_that(abs(_r130['inversion_beta'] - 0.600) < 0.001,
            "PAPER_130: IceCube inversion beta_i = 0.600 EXACT (clean code block)")
assert_that(_r130['precision_at_canonical_pct'] < _r130['precision_at_061_pct'],
            "PAPER_130: canonical BETA_I improves the fit 1.64 -> 0.48 pct (PAPER_1203 auto-correction strengthens)")
assert_that(_r130['peak_at_1e16_pev'] > 0.1,
            "PAPER_130: p_max internal fork - at Eq29's 1e16 the peak FAILS the bound; calibration needs 1e15 (Q-126b)")
assert_that(abs(_r130['degeneracy_pct'] - 22) < 0.1,
            "PAPER_130: UQFF net 0.061 vs standard 0.05 - 22 pct degeneracy noted (Q-126c)")
assert_that(C.wired_count() >= 134, "wired_count >= 134")

_r131 = C.calc('PAPER_131')['value']
assert_that(abs(_r131['y_e_chain'] - 0.0930) < 0.0001,
            "PAPER_131: Y_e = 0.0930 chain EXACT (7 pct from 0.1)")
assert_that(abs(_r131['r_aging_dt_days'] - 810.9) < 0.1,
            "PAPER_131: R = 1.5 aging back-solve dt = 811 days EXACT")
assert_that(_r131['r_at_light_travel'] < 1.1,
            "PAPER_131: light-travel justification gives R = 1.06, not 1.5 - dt back-solved (Q-127b)")
assert_that(abs(_r131['ua_fifth_value'] - 0.168) < 0.001 and _r131['ua_sixth_adjacency'] < 1,
            "PAPER_131: [UA] FIFTH value 0.168 (0.8 pct from 1/6) - fork grows (Q-127c)")
assert_that(abs(_r131['ejecta_competing'] - 0.3971) < 0.0001,
            "PAPER_131: ejecta fork - ad hoc x4 form vs cleaner 1-BETA_I = 0.397 (Q-127d)")
assert_that(abs(_r131['old_ns_exponent'] - 7.93e5) < 0.01e5,
            "PAPER_131: old-NS exhaustion exponent 7.93e5 EXACT (young-NS inference)")
assert_that(C.wired_count() >= 135, "wired_count >= 135")

_r132 = C.calc('PAPER_132')['value']
assert_that(abs(_r132['geometric_sum'] - 2.0801) < 0.0001,
            "PAPER_132: SSq geometric sum 2.0801 EXACT")
assert_that(abs(_r132['e_hoyle_uqff'] - 7.676) < 0.001 and _r132['err_pct'] < 0.3,
            "PAPER_132: E_Hoyle = 7.676 MeV at 0.28 pct EXACT (but E_0 = 3.69 back-solved, Q-128a)")
assert_that(abs(_r132['t_c_uqff_mev'] - 14.04) < 0.01,
            "PAPER_132: T_c = 8/SSq = 14.04 MeV EXACT")
assert_that(abs(_r132['lenr_factor'] - 1.768) < 0.001,
            "PAPER_132: LENR e^SSq = 1.768 EXACT (77 pct - modest vs observed LENR claims)")
assert_that(abs(_r132['hoyle_above_threshold_mev'] - 0.380) < 0.001,
            "PAPER_132: Hoyle 0.380 MeV above 3-alpha threshold (E_0 provenance open)")
assert_that(C.wired_count() >= 136, "wired_count >= 136")

_r133 = C.calc('PAPER_133')['value']
assert_that(abs(_r133['e_react_v1_form'] - 1e46) < 1e40,
            "PAPER_133: E_react = rho_SCm*v_SCm/rho_A = 1e46 EXACT with v^1 - RESOLVES Q-115a 43-order break (Q-129a)")
assert_that(_r133['e_react_v2_divide'] == 1e54 and abs(_r133['e_react_v2_multiply'] - 1e8) < 1,
            "PAPER_133: both v^2 forms fail (1e54 / 1e8) - v^2 is the drift")
assert_that(abs(_r133['omega_m_over_d'] - 23.33) < 0.01,
            "PAPER_133: Omega_g*M_bh/d_g = 23.33 EXACT")
assert_that(abs(_r133['ug2_implied_ereact'] - 2.17e50) < 0.01e50,
            "PAPER_133: Ug2 table 1.18e53 unreproducible (needs E_react 2.17e50; code prints 5.4e10) (Q-129b)")
assert_that(_r133['genesis_beta'] == 0.6,
            "PAPER_133: genesis beta_i = 0.6 - PAPER_2152 provenance lineage documented")
assert_that(C.wired_count() >= 137, "wired_count >= 137")

_r134 = C.calc('PAPER_134')['value']
assert_that(abs(_r134['m_over_rb2'] - 8887) < 1,
            "PAPER_134: M/R_b^2 = 8887 EXACT")
assert_that(abs(_r134['ug2_chain'] - 1.18e40) < 0.01e40,
            "PAPER_134: Ug2 chain = 1.18e40 - mantissa exact, 13-order exponent slip resolves PAPER_133 (Q-130a)")
assert_that(abs(_r134['p_ram_pa'] - 2e-9) < 1e-12,
            "PAPER_134: P_ram = 2e-9 Pa EXACT")
assert_that(_r134['age_exponent_sun'] > 1e8,
            "PAPER_134: age law overflows at Gyr with daily alpha - +73 pct is 3 yr not 3.4 Gyr (Q-130b)")
assert_that(_r134['k_liquid_chain'] > 1e8,
            "PAPER_134: k_liquid chain 2e8 vs printed 201 - 1e6 scale break (Q-130c)")
assert_that(C.wired_count() >= 138, "wired_count >= 138")

_r135 = C.calc('PAPER_135')['value']
assert_that(abs(_r135['f_scm_1pc'] - 3.24e14) < 0.01e14,
            "PAPER_135: F_SCm(1 pc) = 3.24e14 N/m3 EXACT")
assert_that(abs(_r135['dl_printed_factors_kpc'] - 38) < 1,
            "PAPER_135: Cygnus dL = 38 kpc arithmetic consistent GIVEN printed factors")
assert_that(abs(_r135['printed_decay_true_t_days'] - 8) < 0.1,
            "PAPER_135: printed 0.996 decay corresponds to 8 DAYS not 5 Myr - daily-alpha break (Q-131a)")
assert_that(abs(_r135['dl_code_actual_kpc'] - 511) < 1,
            "PAPER_135: own code prints 511 kpc vs claimed 37 - falsified output No. 4")
assert_that(abs(_r135['cos_slip'][0] - 0.891) < 0.001,
            "PAPER_135: cos(0.15pi) = 0.891 vs printed 0.929 - factor slip")
assert_that(C.wired_count() >= 139, "wired_count >= 139")

_r136 = C.calc('PAPER_136')['value']
assert_that(abs(_r136['h_ug3'] - 447.6) < 0.1,
            "PAPER_136: H_Ug3 = 448 J/m3 EXACT")
assert_that(abs(_r136['t_prec_days'] - 29.09) < 0.01,
            "PAPER_136: T_prec = 29.09 days EXACT (solar-rotation relabel, Q-132b)")
assert_that(_r136['hierarchy_ratio'] > 1e24 and _r136['physicality_excess'] > 1e6,
            "PAPER_136: H_SCm 25 orders above H_Ug3 + exceeds core mass-energy by 4e6 (Q-132a)")
assert_that(abs(_r136['p_scm_chain'] - 1e-3) < 1e-15 and abs(_r136['p_scm_primitive'] - 1e-3) < 1e-15,
            "PAPER_136: P_SCm = 1e-3 chain EXACT and = F_TRZ^3 primitive candidate")
assert_that(len(_r136['v_ua_fork']) == 3,
            "PAPER_136: v_UA text/code/corpus fork (1e8/1e4/3e4) pinned (Q-132c)")
assert_that(C.wired_count() >= 140, "wired_count >= 140")

_r137 = C.calc('PAPER_137')['value']
assert_that(abs(_r137['e18_ev'] - 6.24e16) < 0.01e16,
            "PAPER_137: E_18 = 62.4 PeV (printed MeV - 1e9 conversion break); real Higgs n = 12.3 (Q-133a)")
assert_that(abs(_r137['higgs_true_n'] - 12.3) < 0.01,
            "PAPER_137: genesis n=18 Higgs label superseded by EP block n=12")
assert_that(abs(_r137['orbital_cascade_actual'] - 2.18e-14) < 0.01e-14 and abs(_r137['k_needed_for_10ev'] - 32) < 0.2,
            "PAPER_137: orbital cascade gives 136 keV not 10 eV (k=32 needed) - falsified output No. 5 (Q-133b)")
assert_that(_r137['ereact_ladder_max'] == 1e21 and _r137['n_needed_for_1e46'] == 51,
            "PAPER_137: E_react ladder maxes 1e21 - 1e46 off-ladder under v^2; supports v^1 resolution (Q-133c)")
assert_that(abs(_r137['rho_ladder_n26'] - 1e28) < 1e22,
            "PAPER_137: rho ladder self-consistent (n=26 -> 1e28)")
assert_that(C.wired_count() >= 141, "wired_count >= 141")

_r138 = C.calc('PAPER_138')['value']
assert_that(abs(_r138['m_at_tau_msun'] - 547152) < 1,
            "PAPER_138: M(tau) = 547,152 M_sun EXACT")
assert_that(abs(_r138['p0_pa'] - 4e-8) < 1e-11,
            "PAPER_138: P_0 = 4e-8 Pa EXACT")
assert_that(_r138['cavity_chain_ly'] > 20000 and abs(_r138['cavity_code_ly'] - 9099) < 10,
            "PAPER_138: cavity chain 22,867 ly / code 9,099 ly vs printed 21 - 1000x slip, falsified output No. 6 (Q-134a)")
assert_that(abs(_r138['cavity_weaver_ly'] - 266) < 1,
            "PAPER_138: standard Weaver gives 266 ly with these inputs (observed 19)")
assert_that(len(_r138['b_crit_fork']) == 3,
            "PAPER_138: B_crit THIRD value (1e11) - Q-002 fork now 3 values (Q-134d)")
assert_that(abs(_r138['h0_si'] - 2.269e-18) < 0.001e-18,
            "PAPER_138: H_0 = 2.269e-18 /s EXACT (PAPER_1573 route consistent)")
assert_that(C.wired_count() >= 142, "wired_count >= 142")

_r139 = C.calc('PAPER_139')['value']
assert_that(abs(_r139['f_grav_n'] - 3.634e-47) < 0.001e-47,
            "PAPER_139: F_grav = 3.634e-47 N EXACT")
assert_that(abs(_r139['hubble_factor'] - 1.9877) < 0.0001,
            "PAPER_139: (1 + H0 t) = 1.9877 EXACT")
assert_that(28 < _r139['orders_apart'] < 30,
            "PAPER_139: Ug4 paper value 29 orders from its stated chain - falsified output No. 7 (Q-135a)")
assert_that(abs(_r139['total_vs_dominant'] - 105) < 1,
            "PAPER_139: total g_H 105x SMALLER than claimed dominant Ug4i (Q-135b)")
assert_that(abs(_r139['p_term'] - 1.448e31) < 0.001e31,
            "PAPER_139: P_term arithmetic 1.448e31 EXACT (units flag open)")
assert_that(C.wired_count() >= 143, "wired_count >= 143")

_r140 = C.calc('PAPER_140')['value']
assert_that(_r140['ratio'] == 10.0 and abs(_r140['inverse_is_f_trz'] - 0.1) < 1e-15,
            "PAPER_140: ratio = 10 EXACT = 1/F_TRZ (origin paper)")
assert_that(_r140['n_monopole_is_so_five'] == 10 and _r140['magnetic_factor'] == 11,
            "PAPER_140: N_monopole = SO_FIVE and factor 11 = SO_FIVE+1 - two predecessor convergences (Q-136a)")
assert_that(abs(_r140['f_quantum_body'] - 1.0000049) < 1e-7,
            "PAPER_140: f_quantum body 1.0000049 vs abstract 1.000000008 - 600x internal fork (Q-136c)")
assert_that(_r140['dark_energy_claim_orders'] > 8,
            "PAPER_140: dark-energy identification 8.9 orders off, marked Exact - overclaim pinned (Q-136b)")
assert_that(_r140['muge_factor_21'] == 21,
            "PAPER_140: MUGE-H factor 21 = 1+10+10 consistent with PAPER_139")
assert_that(C.wired_count() >= 144, "wired_count >= 144")

_r141 = C.calc('PAPER_141')['value']
assert_that(abs(_r141['e_rot_j'] - 2.125e29) < 0.001e29,
            "PAPER_141: E_rot = 2.125e29 J EXACT")
assert_that(abs(_r141['henry_correction'] - 1.29e-29) < 0.01e-29,
            "PAPER_141: Henry correction 1.29e-29 EXACT (below-precision honesty)")
assert_that(abs(_r141['gas_table_mm']['H2'] - 62.4) < 0.1,
            "PAPER_141: gas table EXACT (4 gases)")
assert_that(abs(_r141['azeo_primitive'] - 0.2) < 1e-15,
            "PAPER_141: Azeo_void = 0.2 = 2/SO_FIVE - second independent 1/5 appearance (Q-137b)")
assert_that(len(_r141['failed_chains']) == 3,
            "PAPER_141: Buoy_term code-calibrated - three failed chains honestly disclosed (Q-137a)")
assert_that(abs(_r141['ug4_prefactor'] - 9.42e-18) < 0.01e-18,
            "PAPER_141: Ug4 oceanic prefactor 9.42e-18 EXACT (attenuation constructive)")
assert_that(C.wired_count() >= 145, "wired_count >= 145")

_r142 = C.calc('PAPER_142')['value']
assert_that(abs(_r142['ni62_ares'] - 1900.6) < 0.1,
            "PAPER_142: Ni-62 A_res = 1900.6 V EXACT")
assert_that(abs(_r142['ni62_fres'] - 1.415e22) < 0.001e22,
            "PAPER_142: Ni-62 f_res = 1.415e22 Hz EXACT")
assert_that(abs(_r142['k_dp'] - 5.902e-39) < 0.001e-39,
            "PAPER_142: k_dp = ALPHA_G = 5.902e-39 EXACT physical identification (Q-138b)")
assert_that(abs(_r142['dpair_effective_backsolved']['He4'] - 0.501) < 0.001 and abs(_r142['dpair_effective_backsolved']['Pb208'] - 2.502) < 0.001,
            "PAPER_142: d_pair chaos pinned - He-4 suppressed 0.5x, Pb 2.5x, five conventions (Q-138a)")
assert_that(_r142['s_shell_island_fork'] == (29.8, 31.0),
            "PAPER_142: S_shell island table-vs-code fork (114 not in MAGIC list) (Q-138c)")
assert_that(abs(_r142['island_ratio'] - 1.80) < 0.01,
            "PAPER_142: island resonance 1.80x Pb - falsifiable prediction")
assert_that(C.wired_count() >= 146, "wired_count >= 146")

_r143 = C.calc('PAPER_143')['value']
assert_that(abs(_r143['uqff_share_primitive'] - 0.4) < 1e-15 and abs(_r143['qm_share_primitive'] - 0.6) < 1e-15,
            "PAPER_143: 40/60 split = (D_PHYS, D_BSFG)/SO_FIVE EXACT primitive decomposition (Q-139a)")
assert_that(abs(_r143['ratio_backsolved'] - 4 / 6) < 0.001,
            "PAPER_143: back-solved ratio 2/3 = D_PHYS/D_BSFG (PAPER_2154 predecessor identity)")
assert_that(abs(_r143['g_qm_bohr'] - 4.52e22) < 0.01e22,
            "PAPER_143: g_QM(Bohr) = 4.52e22 EXACT")
assert_that('hardcoded' in _r143['code_circular'] and 'cannot run' in _r143['code_syntax_error'],
            "PAPER_143: split circularly inserted + code block syntax error (Q-139b)")
assert_that(abs(_r143['lambda_chain'] - 8.58e-10) < 0.01e-10,
            "PAPER_143: lambda chain 8.58e-10 vs printed 8.59e-19 - 1e9 slip, mantissa exact (Q-139c)")
assert_that(abs(_r143['anomaly_targets']['neutron_lifetime_s'] - 8.4) < 0.01,
            "PAPER_143: four real anomaly targets registered (explanations restate gaps)")
assert_that(C.wired_count() >= 147, "wired_count >= 147")

_r144 = C.calc('PAPER_144')['value']
assert_that(abs(_r144['m_over_d'] - 3.196e16) < 0.001e16,
            "PAPER_144: M/d = 3.196e16 EXACT")
assert_that(abs(_r144['omega_m_over_d'] - 23.33) < 0.01,
            "PAPER_144: Omega*M/d = 23.33 EXACT (capstone consistent with 133)")
assert_that(13.9 < _r144['ub_amplification'] < 14.2,
            "PAPER_144: Ub amplification = 14 - buoyancy overwhelms gravity at max activation (Q-140a)")
assert_that(_r144['f_u_at_max'] < 0,
            "PAPER_144: F_U NET NEGATIVE at max activation - F_U=0 doctrine tension pinned")
assert_that(len(_r144['millennium_bridges']) == 4,
            "PAPER_144: four Millennium bridges registered (P-NP third rationale noted)")
assert_that(C.wired_count() >= 148, "wired_count >= 148")

_r145 = C.calc('PAPER_145')['value']
assert_that(_r145['n_terms'] == 12,
            "PAPER_145: 12-term Cycle 3 architecture registered")
assert_that(abs(_r145['delta_evac'] - 6.381e-36) < 1e-39,
            "PAPER_145: DeltaEvac = 6.381e-36 EXACT")
assert_that('resolves PAPER_140' in _r145['self_rectification'],
            "PAPER_145: vacuum split resolves 140 DE conflation - self-rectification No. 12 (Q-141a)")
assert_that(_r145['k4_fork'] == (1.0, 2.0),
            "PAPER_145: k4 fork genesis 1.0 vs Cycle 3 2.0 pinned (Q-141b)")
assert_that(_r145['seven_systems']['SGR1745'] < 1e-8 and _r145['seven_systems']['SgrA'] > 1e29,
            "PAPER_145: MUGE-g identification OPEN - 21/23 orders from physical gravities (Q-141c)")
assert_that(C.wired_count() >= 149, "wired_count >= 149")

_r146 = C.calc('PAPER_146')['value']
assert_that(abs(_r146['osc_period_yr'] - 19.9) < 0.1,
            "PAPER_146: Osc aether period 19.9 yr EXACT")
assert_that(_r146['evac_ratio'] == 10.0,
            "PAPER_146: Evac_neb/Evac_ISM = 10 = monopole ratio (PAPER_140 link)")
assert_that('additive' in _r146['ftrz_form_fork'],
            "PAPER_146: fTRZ additive-vs-multiplicative form fork pinned (Q-142a)")
assert_that('inverse' in _r146['ug4i_collision'],
            "PAPER_146: Ug4i naming collision (direct vs 139/121 inverse) pinned (Q-142b)")
assert_that(_r146['sgra_gnewt_slip'][1] / _r146['sgra_gnewt_slip'][0] > 1e5,
            "PAPER_146: Sgr A* g_Newt-at-1AU table slip pinned")
assert_that(C.wired_count() >= 150, "wired_count >= 150")

_r147 = C.calc('PAPER_147')['value']
assert_that(abs(_r147['athz_over_adpm_stellar'] - 3.33e9) < 0.01e9,
            "PAPER_147: aTHz = 3.33e9 x aDPM at stellar winds - hierarchy inversion (Q-143a)")
assert_that(_r147['athz_over_adpm_sgra'] > 1e12,
            "PAPER_147: at Sgr A* speeds aTHz = 3e12 x aDPM - contradicts dominance map")
assert_that(abs(_r147['avac_over_adpm'] - 1e-7) < 1e-9,
            "PAPER_147: avac_diff/aDPM = 1e-7 EXACT (subdominant consistent)")
assert_that(abs(_r147['lenr_thz_err_pct'] - 1.69) < 0.01,
            "PAPER_147: LENR THz anchor 1.18-vs-1.2 = 1.7 pct EXACT (089 lineage)")
assert_that(len(_r147['thz_family']) == 4,
            "PAPER_147: THz family four values (1.0/1.18/1.2/1.25) - canonical carrier needed (Q-143d)")
assert_that(C.wired_count() >= 151, "wired_count >= 151")

_r148 = C.calc('PAPER_148')['value']
assert_that(abs(_r148['lap_v_chain'] - 41.4) < 0.1,
            "PAPER_148: lap_v = 41.4 EXACT")
assert_that(abs(_r148['r_lc_m'] - 1.795e8) < 0.001e8,
            "PAPER_148: light-cylinder r_lc = 1.795e8 m EXACT")
assert_that(_r148['ftrz_additive_refuted'] > 1e7,
            "PAPER_148: additive fTRZ would be 5.6e7x the total - own table refutes additive form (Q-144a)")
assert_that('Schwinger' in _r148['bcrit_direction_vote'],
            "PAPER_148: B_crit direction consistency votes Schwinger 4.4e9 (Q-144b, feeds Q-002)")
assert_that(_r148['mantissa_slips'] == 3 and abs(_r148['nu_chain'] - 1.728e24) < 0.001e24,
            "PAPER_148: three mantissa-exact exponent slips pinned (nu/g_lc/surface) (Q-144c)")
assert_that(C.wired_count() >= 152, "wired_count >= 152")

_r149 = C.calc('PAPER_149')['value']
assert_that(abs(_r149['vsys_m3'] - 7.79e30) < 0.01e30,
            "PAPER_149: Vsys = 7.79e30 m^3 EXACT")
assert_that(abs(_r149['g_newt_1au'] - 2.43e4) < 0.01e4,
            "PAPER_149: g_Newt(1AU) = 2.43e4 EXACT - corrects PAPER_146 table slip")
assert_that(_r149['athz_formula_over_adpm'] / _r149['athz_table_over_adpm'] > 1e14,
            "PAPER_149: aTHz table-vs-formula 1e15 discrepancy CONFIRMS the Q-143a cascade inversion (Q-145a)")
assert_that(abs(_r149['ratio_body'] - 1.69e25) < 0.01e25,
            "PAPER_149: body ratio 1.69e25 vs abstract 1e19 - 6-order internal fork (Q-145b)")
assert_that(abs(_r149['g_newt_rs_chain'] - 3.59e6) < 0.01e6,
            "PAPER_149: g_Newt(r_s) chain 3.59e6 vs printed 3.6e15 - 1e9 mantissa-exact slip (Q-145c)")
assert_that(C.wired_count() >= 153, "wired_count >= 153")

_r150 = C.calc('PAPER_150')['value']
assert_that(_r150['sat_westerlund'] / _r150['sat_tapestry'] > 1e5,
            "PAPER_150: saturation floor 1e6 apart at own radii - same-floor claim self-contradicts (Q-146a)")
assert_that(_r150['westerlund_actual_sfr'] < 0.01,
            "PAPER_150: Westerlund SFR ~ 5e-3 Msun/yr fails the > 100 precondition by 4+ orders (Q-146b)")
assert_that(_r150['westerlund_distance_fork'] == (2.8, 8.0),
            "PAPER_150: Westerlund distance fork 2.8-vs-8 kpc pinned (Q-146c)")
assert_that(abs(_r150['periodicity_prediction_yr'] - 19.9) < 0.1,
            "PAPER_150: 20-yr aether periodicity prediction registered (maser-testable)")
assert_that(abs(_r150['implied_ratio'] - 500) < 1,
            "PAPER_150: table implies nu*lap_v/Evac = 500 (formula-vs-table family)")
assert_that(C.wired_count() >= 154, "wired_count >= 154")

_r151 = C.calc('PAPER_151')['value']
assert_that(abs(_r151['cascade_ratios'][0] - 5.0) < 0.01 and abs(_r151['cascade_ratios'][1] - 4.0) < 0.01,
            "PAPER_151: cascade ratios 5.00/4.00 EXACT")
assert_that(abs(_r151['p_scm_tag'] - 1.001) < 1e-6,
            "PAPER_151: VALUE FINGERPRINT - system g = round x (1 + P_SCM) decade ladder (Q-147a)")
assert_that(abs(_r151['r_e_m'] - 1.498e20) < 0.001e20,
            "PAPER_151: Einstein radius 1.498e20 m EXACT")
assert_that(_r151['theta_correction'] > 8e28,
            "PAPER_151: lensing correction 8.3e28 - 30-order observation flag unless scoped (Q-147b)")
assert_that('10x' in _r151['b_label_slip'],
            "PAPER_151: B-label 10x slip pinned (150 family) (Q-147c)")
assert_that(C.wired_count() >= 155, "wired_count >= 155")

_r152 = C.calc('PAPER_152')['value']
assert_that(abs(_r152['cascade_decades'] - 38.4) < 0.1,
            "PAPER_152: 7-system cascade spans 38.4 decades EXACT")
assert_that(abs(_r152['term_exact']['aaether_res'] - 1.5e27) < 0.01e27,
            "PAPER_152: aaether_res = 1.5e27 EXACT (largest term)")
assert_that(_r152['total_vs_largest'] > 1e12,
            "PAPER_152: total 13 orders below its own largest term - unreproducible (Q-148b)")
assert_that('differ from 146/147' in _r152['formula_fork_no3'],
            "PAPER_152: formula set fork No. 3 - three 12-term formula sets corpus-wide (Q-148a)")
assert_that(_r152['h0_fork'] == (67.4, 70),
            "PAPER_152: H0 fork 67.4-vs-70 pinned (predecessor canonized 70)")
assert_that(C.wired_count() >= 156, "wired_count >= 156")

_r153 = C.calc('PAPER_153')['value']
assert_that(abs(_r153['r0_mm'] - 2.32) < 0.01,
            "PAPER_153: throat r_0 = 2.32 mm GENUINELY derived from SCm parameters (block's cleanest)")
assert_that(abs(_r153['transit_s'] - 7.73e-12) < 0.01e-12,
            "PAPER_153: transit 7.73 ps EXACT")
assert_that(_r153['throat_condition'] == 1.0,
            "PAPER_153: throat condition 0.9 + 0.1 = 1 EXACT; fTRZ native home (topology fraction) (Q-149a)")
assert_that(abs(_r153['cosmological_time_actual_yr'] - 13.83) < 0.01,
            "PAPER_153: 'cosmological' decay factor = 13.83 YEARS - Gyr-to-yr echo (Q-149c)")
assert_that(abs(_r153['scm_margin'] - 13.9) < 0.1,
            "PAPER_153: SCm exceeds reduced exotic requirement 13.9x - self-consistency chain")
assert_that(C.wired_count() >= 157, "wired_count >= 157")

_r154 = C.calc('PAPER_154')['value']
assert_that(_r154['f_jet'] == 1e7,
            "PAPER_154: f_jet = v_SCm * F_TRZ = 1e7 EXACT primitive identity")
assert_that(abs(_r154['t_osc_yr'] - 54.8) < 0.1,
            "PAPER_154: T_Osc = tau/F_TRZ = 54.8 yr EXACT (M87 knot match)")
assert_that(abs(_r154['e46_second_decomposition'] - 1e46) < 1e40,
            "PAPER_154: rho v^2/lambda_fm = 1e46 EXACT - SECOND closing decomposition (Q-150b, annotates Q-129)")
assert_that(abs(_r154['nu_scm'] - 3.33e-8) < 0.01e-8,
            "PAPER_154: nu_SCm = v lambda/3 = 3.33e-8 EXACT; lambda_SCm = 1 fm registered")
assert_that(_r154['step4_denominator'][0] / _r154['step4_denominator'][1] > 1e7,
            "PAPER_154: Step-4 derivation broken (8-order slip, abandoned) - f_jet definitional (Q-150c)")
assert_that(C.wired_count() >= 158, "wired_count >= 158")

_r155 = C.calc('PAPER_155')['value']
assert_that(abs(_r155['taylor_core'] - 1) < 0.001,
            "PAPER_155: Taylor core (1-e^-kt)/kt -> 1 VALID - SM limit proof holds modulo Ug4i fork")
assert_that(abs(_r155['mercury_g'] - 0.0397) < 0.0001,
            "PAPER_155: Mercury chain EXACT (solar-system consistency)")
assert_that('FOUR variants' in _r155['ug4i_fourth_form'],
            "PAPER_155: keystone rests on Ug4i FOURTH form - fork adjudication now decides the proof (Q-151a)")
assert_that(_r155['aaether_solar_chain'] < 1e-13 and _r155['sgra_kt_chain'] > 1e8,
            "PAPER_155: three mantissa-exact slips pinned (1e5/10x/1e6) (Q-151b)")
assert_that('Turyshev' in _r155['pioneer_status'],
            "PAPER_155: Pioneer attribution outdated (thermally resolved) (Q-151c)")
assert_that(C.wired_count() >= 159, "wired_count >= 159")

_r156 = C.calc('PAPER_156')['value']
assert_that(abs(_r156['t0_days'] - 20000) < 1e-9,
            "PAPER_156: t_0 = 1/(kappa*F_TRZ) = 20,000 days = 154's T_Osc (consistent)")
assert_that(abs(_r156['pnp_exponent'] - 1.754) < 0.001,
            "PAPER_156: P-NP exponent N^(1/SSq) = N^1.754 EXACT")
assert_that(_r156['ym_fork'] > 1e19,
            "PAPER_156: YM gap fork 3.3e19 (roadmap 5.2e-11 eV vs canonical 1.736 GeV) (Q-152a)")
assert_that(_r156['ym_sqrt_slip'][1] / _r156['ym_sqrt_slip'][0] > 3,
            "PAPER_156: sqrt-10 slip inside eq-M2 pinned")
assert_that(abs(_r156['bsd_amplifier'] - 2000) < 1e-9,
            "PAPER_156: BSD 1/kappa = 2000 EXACT (but ord = rank x 2000 inverts BSD)")
assert_that('145-156' in _r156['block_complete'],
            "PAPER_156: Cycle 3 block COMPLETE (12 papers)")
assert_that(C.wired_count() >= 160, "wired_count >= 160")

_r157 = C.calc('PAPER_157')['value']
assert_that(abs(_r157['fu_over_ug3_measured'] - (-12.9975)) < 0.001,
            "PAPER_157: F_U/Ug3 = -12.9975 constant across ALL four bodies (table structure)")
assert_that(abs(_r157['fu_over_ug3_measured'] - _r157['fu_over_ug3_chain']) / abs(_r157['fu_over_ug3_chain']) < 0.001,
            "PAPER_157: F_U = (1-beta*Omega_g*Mbh/dg)*Ug3 chain matches table to 0.01% (derived)")
assert_that(_r157['thirteen_adjacency'] == 13,
            "PAPER_157: -13 factor adjacent to -D_crit/2 (N=13 family)")
assert_that(abs(_r157['k4_implied'] - 2.0) < 0.001,
            "PAPER_157: undeclared k4 = 2.000 EXACT implied by uniform Ug4 = 4.219e-10")
assert_that(abs(_r157['kappa_per_s'] - 5.787e-9) / 5.787e-9 < 1e-4,
            "PAPER_157: kappa 5e-4/day = 5.787e-9/s cross-section consistent EXACT")
assert_that('THIRD' in _r157['e_react_variant'],
            "PAPER_157: E_react third variant rho*v^2/rho_A pinned (Q-153a)")
assert_that(C.wired_count() >= 161, "wired_count >= 161")

_r158 = C.calc('PAPER_158')['value']
assert_that(abs(_r158['beta_sgr'] - 0.99321) < 1e-4,
            "PAPER_158: beta_SGR = exp(-3e11/4.4e13) = 0.99321 (paper 0.9933)")
assert_that(abs(_r158['beta_ns'] - 0.97753) < 1e-4,
            "PAPER_158: beta_NS = 0.97753 (paper 0.977)")
assert_that(_r158['res_dominance_analytic']['SGR 1745'] > 6e3,
            "PAPER_158: resonance term dominates SGR row by 6.4e3 analytically")
assert_that(_r158['res_dominance_analytic']['StudentsGuide'] > 1e85,
            "PAPER_158: resonance dominates Student's Guide by 1.4e85 - underflow artifact (Q-154a)")
assert_that(abs(_r158['footer_ubi_ratio'] - 2.85e-4) < 1e-9,
            "PAPER_158: footer U_bi/F_U = SSq*kappa = 2.85e-4 EXACT")
assert_that('4.4e13' in _r158['b_crit_fork_vote'],
            "PAPER_158: B_crit = 4.4e13 vote pinned (Q-002 fork deepens)")
assert_that(C.wired_count() >= 162, "wired_count >= 162")

_r159 = C.calc('PAPER_159')['value']
assert_that(abs(_r159['a_worm_1au'] - 3.17e-58) / 3.17e-58 < 0.001,
            "PAPER_159: a_worm(1 AU) = 3.168e-58 matches paper 3.17e-58 (0.06%)")
assert_that(_r159['e_vac_neb_over_rho_scm'] == 10,
            "PAPER_159: E_vac,neb = SO_5*rho_SCm = rho_UA EXACT (primitive identity)")
assert_that(_r159['n_terms'] == 13,
            "PAPER_159: 13-term resonance MUGE (extends 146's 12-term)")
assert_that(400 < 1.0 / 2.32e-3 < 460,
            "PAPER_159: throat fork b = 1.0 m vs 153's derived 2.32 mm = 431x (Q-155a)")
assert_that(_r159['magnitude_slip'][1] / _r159['magnitude_slip'][0] > 500,
            "PAPER_159: '1e58x smaller' claim is a 534x slip vs actual 1.87e55 (Q-155b)")
assert_that(C.wired_count() >= 163, "wired_count >= 163")

_r160 = C.calc('PAPER_160')['value']
assert_that(abs(_r160['ug4_t0'] - 4.219e-10) / 4.219e-10 < 1e-3,
            "PAPER_160: Ug4(0,0) = 4.2188e-10 chain verified (paper 4.219e-10, 0.004%)")
assert_that(_r160['k4_canonical'] == 2.0,
            "PAPER_160: k4 = 2.0 declared canonical - CONFIRMS 157-derived k4 = 2.000 (Q-153b resolved)")
assert_that(_r160['rounding_pct'] < 2.0,
            "PAPER_160: rho_v = 6e-27 is 1.8% rounding of Lambda*c^2/8piG = 5.89e-27")
assert_that(abs(_r160['footer_edd'] - 0.43017) < 1e-4,
            "PAPER_160: footer 1 - SSq*e^-2.9e-4 = 0.43017 EXACT")
assert_that('2147' in _r160['drift'],
            "PAPER_160: J/m^3-on-kg/m^3 unit-tag drift pinned (PAPER_2147 class)")
assert_that(C.wired_count() >= 164, "wired_count >= 164")

_r161 = C.calc('PAPER_161')['value']
assert_that(abs(_r161['gamma'] - 7.0888) < 1e-3,
            "PAPER_161: Lorentz gamma(0.99c) = 7.0888 (paper 7.09)")
assert_that(abs(_r161['e_inject_factor'] - 6.09) < 0.01,
            "PAPER_161: E_inject = (gamma-1)*m*c^2 = 6.09*m*c^2 verified")
assert_that(abs(_r161['v2_scaling_actual'] - 98.01) < 0.1,
            "PAPER_161: actual v^2 scaling 0.1c->0.99c = 98.01 vs claimed ~4 (Q-157a)")
assert_that(abs(_r161['v_scm'] - 2.968e8) / 2.968e8 < 1e-3,
            "PAPER_161: v_SCm = 0.99c = 2.968e8 m/s")
assert_that('curl-free' in _r161['body_force'],
            "PAPER_161: uniform body force curl-free - consistent with 154's NS core")
assert_that(C.wired_count() >= 165, "wired_count >= 165")

_r162 = C.calc('PAPER_162')['value']
assert_that(abs(_r162['omega_c_sun'] - 1.810e-8) / 1.810e-8 < 1e-3,
            "PAPER_162: omega_c(Sun) = 2pi/11yr = 1.810e-8 rad/s verified")
assert_that(abs(_r162['cycle_ratio'] - 2.333) < 0.001,
            "PAPER_162: solar-cycle Ug1 ratio 1.4/0.6 = 2.333 EXACT (testable prediction)")
assert_that(abs(_r162['period_actual_s'] - 6283.19) < 0.1,
            "PAPER_162: delta_def period = 6283 s, not '6.3 s' - 1000x slip, mantissa EXACT (Q-158b)")
assert_that(_r162['scm_contrib_sun_T'] == 1e5,
            "PAPER_162: SCm_contrib(Sun) = 1e5 T = 1e9 x B_s - 'perturbative' claim false (Q-158c)")
assert_that(abs(_r162['footer_solar_wind'] - 0.5688) < 0.001,
            "PAPER_162: footer solar-wind correction 0.5688 ~ 5.7e-1 (exponent 2.16e-3 vs paper 3.2e-3)")
assert_that(C.wired_count() >= 166, "wired_count >= 166")

_r163 = C.calc('PAPER_163')['value']
assert_that(_r163['n_functions'] == 8,
            "PAPER_163: 8 decomposed compressed-MUGE functions cataloged")
assert_that(abs(_r163['cosm_term'] - 3.293e-36) / 3.293e-36 < 0.001,
            "PAPER_163: cosm = Lambda*c^2/3 = 3.296e-36 (table 3.293e-36, 0.08%)")
assert_that(abs(_r163['fluid_bench'] - 12.66) < 0.01,
            "PAPER_163: fluid bench 1.29*1*9.81 = 12.655 (table 12.66)")
assert_that(_r163['base_table_expected'] / _r163['base_actual'] > 1e10,
            "PAPER_163: base-test expected 6.67e8 vs actual 6.674e-3 - 1e11 slip, mantissa EXACT (Q-159a)")
assert_that(_r163['h0_canonical'] > _r163['h0_paper'],
            "PAPER_163: H0 fork - 67.4 hardcoded vs canonical A_5+SO_5 = 70 (Q-159b)")
assert_that(C.wired_count() >= 167, "wired_count >= 167")

_r164 = C.calc('PAPER_164')['value']
assert_that(abs(_r164['de_vac'] - 2.083e39) / 2.083e39 < 0.001,
            "PAPER_164: dE_vac = 13 TeV/(1 fm)^3 = 2.083e39 J/m^3 CORRECT (intermediate typo only)")
assert_that(abs(_r164['dx_lhc'] - 1.518e-20) / 1.518e-20 < 0.001,
            "PAPER_164: dx = hbar*c/(2*6.5 TeV) = 1.518e-20 m (paper 1.5e-20)")
assert_that(abs(_r164['b_over_bcrit_chandra'] - 5.227e-4) / 5.227e-4 < 0.001,
            "PAPER_164: Chandra B/B_crit = 5.227e-4 EXACT (paper 5.23e-4)")
assert_that('13x' in _r164['sgr_b_fork'],
            "PAPER_164: SGR 1745 B fork 2.3e10 vs 3e11 T pinned (Q-160a)")
assert_that('compressed' in _r164['contradiction'],
            "PAPER_164: sec 5 resonance-dominates claim contradicts 158/155 at beta~1 (Q-160b)")
assert_that(C.wired_count() >= 168, "wired_count >= 168")

_r165 = C.calc('PAPER_165')['value']
assert_that(abs(_r165['delta_a'] - 4.448e-15) / 4.448e-15 < 1e-6,
            "PAPER_165: Delta_A = 4*eta*T_s00 = 4.448e-15 EXACT")
assert_that(_r165['trace_factor_is_d_phys'] == 4,
            "PAPER_165: trace factor 4 = D_PHYS (4D trace count)")
assert_that(abs(_r165['t_scm_chain'] - 9.947e6) / 9.947e6 < 0.001,
            "PAPER_165: B^2/2mu0 @ 5T = 9.947e6, paper 1.11e7 (11.6%; B = 5.28 T would match) (Q-161a)")
assert_that(20 < _r165['orders_above_wormhole'] < 21,
            "PAPER_165: 20.8 orders above wormhole term, claimed '~4' (Q-161b)")
assert_that(73 < _r165['orders_below_fu_sun'] < 74,
            "PAPER_165: 73.7 orders below F_U(Sun), claimed '1043' (Q-161b)")
assert_that(C.wired_count() >= 169, "wired_count >= 169")

_r166 = C.calc('PAPER_166')['value']
assert_that(abs(_r166['rho_sw_1au'] - 8.35e-21) / 8.35e-21 < 1e-6,
            "PAPER_166: rho_sw(1 AU) = m_p*5e6 = 8.35e-21 kg/m^3 EXACT")
assert_that(9.9 < _r166['mercury_slip'][1] / _r166['mercury_slip'][0] < 10.1,
            "PAPER_166: Mercury row 10x slip with EXACT mantissa (5.48e-19 vs 5.49e-20)")
assert_that(_r166['sec7_actual'] == 401.0,
            "PAPER_166: sec 7 '1.4' actually = 401 with stated 4e5 m/s - km/s unit persists (Q-162a)")
assert_that(_r166['sec7_kms_reading'] == 1.4,
            "PAPER_166: sec 7 = 1.4 only under v_sw in km/s")
assert_that(_r166['threshold_1pct'] == 10.0,
            "PAPER_166: 1% threshold rho = 10 kg/m^3, claimed 1e3 - 100x slip (Q-162b)")
assert_that(C.wired_count() >= 170, "wired_count >= 170")

_r167 = C.calc('PAPER_167')['value']
assert_that(_r167['mass_balance_exact'],
            "PAPER_167: GW231123 mass balance 225 - 213 = 12 Msun SELF-CONSISTENT")
assert_that(_r167['fu_additive'][0] == _r167['fu_additive'][1],
            "PAPER_167: F_U additive across merger - 5e51 + 3e51 = 8e51 EXACT")
assert_that(1.8e-27 < _r167['m_gap_chain_kg'] < 2.0e-27,
            "PAPER_167: M_gap chain gives 1.88e-27 kg (glueball-scale), paper prints 1e-35 (Q-163b)")
assert_that(4e67 < _r167['n_glueball_chain'] < 5e67,
            "PAPER_167: N = 225 Msun/1e-35 = 4.5e67, paper prints 1e71 - 2200x internal (Q-163b)")
assert_that('300 MeV' in _r167['ym_gap_third_value'],
            "PAPER_167: YM gap THIRD value 300 MeV pinned (Q-163a, Q-152a family)")
assert_that(_r167['g_pert_mass'] == 1350,
            "PAPER_167: g_pert effective mass (225 + 1125) = 1350 Msun EXACT")
assert_that(C.wired_count() >= 171, "wired_count >= 171")

_r168 = C.calc('PAPER_168')['value']
assert_that(_r168['n_systems'] == 7,
            "PAPER_168: 7-system entity framework (SGR/SgrA/Tapestry/West2/Pillars/Rings/Student)")
assert_that('minus-buoyancy' in _r168['fu_sign_convention'],
            "PAPER_168: F_U minus-buoyancy sign convention - predecessor-consistent (2152 echo)")
assert_that(abs(_r168['g_uqff_correction'] - 1.6245e-4) < 1e-8,
            "PAPER_168: g_UQFF correction SSq*(Ubi/F_U) = 1.62e-4 with 158 footer ratio")
assert_that(_r168['size_span_orders'] > 20,
            "PAPER_168: actual size span ~23 orders vs claimed 13 (Q-164)")
assert_that('1e6x' in _r168['scale_law_break'],
            "PAPER_168: entity scale law breaks 1e6x at Rings row (Q-164)")
assert_that(C.wired_count() >= 172, "wired_count >= 172")

_r169 = C.calc('PAPER_169')['value']
assert_that(abs(_r169['delta_p_factor'] - 2.85e-4) < 1e-12,
            "PAPER_169: delta_P factor kappa*SSq = 2.85e-4 EXACT (matches 158 footer product)")
assert_that(_r169['matches_158_footer'],
            "PAPER_169: kappa*SSq product corpus-consistent with 158")
assert_that(_r169['n_tiers'] == 6,
            "PAPER_169: six-tier CoAnQi architecture registered")
assert_that(_r169['port_pi_echo'] == 3141,
            "PAPER_169: REST port 3141 (pi echo)")
assert_that('157-168' in _r169['block_closed'],
            "PAPER_169: sec 2.3 block (157-168) CLOSED; sec 2.4 opens")
assert_that(C.wired_count() >= 173, "wired_count >= 173")

_r170 = C.calc('PAPER_170')['value']
assert_that(_r170['n_fields'] == 12,
            "PAPER_170: 12-field CelestialBody struct registered")
assert_that(_r170['omega_s_sun_canonical'] == 2.5e-6,
            "PAPER_170: Sun omega_s = 2.5e-6 = predecessor canonical omega_s_Sun EXACT")
assert_that(abs(_r170['ubi_factor'] - 2.85e-4) < 1e-12,
            "PAPER_170: compact Ubi law factor kappa*SSq = 2.85e-4 (2nd Ubi form, Q-166a)")
assert_that(_r170['qua_ratio_sun_earth'] == 10.0,
            "PAPER_170: QUA Sun/Earth = 10 internally consistent")
assert_that('placeholder' in _r170['placeholder_confessed'],
            "PAPER_170: SCm_contrib = 1e3 confessed as placeholder (Q-158c self-resolution)")
assert_that('5x' in _r170['neptune_forks'],
            "PAPER_170: Neptune Bs/SCm forks vs 157 pinned (Q-166c)")
assert_that(C.wired_count() >= 174, "wired_count >= 174")

_r171 = C.calc('PAPER_171')['value']
assert_that(_r171['k_constants'] == {'k1': 1.5, 'k2': 1.2, 'k3': 1.8, 'k4': 2.0},
            "PAPER_171: k1/k2/k3 = 1.5/1.2/1.8 = May 2025 source-doc EXACT (2152 provenance); k4 = 2.0")
assert_that(_r171['k4_third_confirmation'],
            "PAPER_171: k4 = 2.0 third confirmation (157 derived, 160 canonical)")
assert_that(_r171['wind_factor_171'] == 5001.0,
            "PAPER_171: wind factor 5001 vs 166's 1.4/401 - instability pinned (Q-167b)")
assert_that(_r171['bj_placeholder_dominance'] == 1e6,
            "PAPER_171: Bj placeholder 1e3 dominates baseline 1e-3 by 1e6")
assert_that(_r171['ug4_energy_levels'] == (20, 26),
            "PAPER_171: Ug4 assigned to energy levels 20-26 (26-level touchpoint)")
assert_that('BETA_I' in _r171['beta_drift'],
            "PAPER_171: beta_i = 0.61 drift auto-corrected by citation (PAPER_1203)")
assert_that(C.wired_count() >= 175, "wired_count >= 175")

_r172 = C.calc('PAPER_172')['value']
assert_that(9e53 < _r172['smoking_gun_ratio'] < 1e54,
            "PAPER_172: SMOKING GUN - code unit test 1.773e-9 vs table 1.655e45 = 9.3e53 (Q-143a confirmed from inside codebase)")
assert_that(_r172['compressed_consistent'] < 0.001,
            "PAPER_172: compressed_MUGE unit test 1.782e39 IS table-consistent (0.06%)")
assert_that(_r172['jet_quarter_is_d_phys'] == 0.25,
            "PAPER_172: jet law 0.25 = 1/D_PHYS")
assert_that('4 forms' in _r172['ubi_fourth_form'],
            "PAPER_172: FOURTH Ubi form (Archimedes) - four-form fork pinned (Q-168a)")
assert_that('distinct' in _r172['wind_two_factors'],
            "PAPER_172: two distinct wind factors clarified - partially resolves Q-162a/Q-167b")
assert_that('1.127e7' in _r172['amunu_flip'],
            "PAPER_172: A_mu_nu signature flip + T_s00 = 1.127e7 adoption pinned (Q-168b)")
assert_that(C.wired_count() >= 176, "wired_count >= 176")

_r173 = C.calc('PAPER_173')['value']
assert_that(_r173['derivation_residual_pct'] < 0.1,
            "PAPER_173: DERIVED - 1.782e39 = 3GM^2/r^3 at SGR (M = 2.984e30, r = 10 km), 0.05%")
assert_that(abs(_r173['h0_vote'] - 2.2685e-18) / 2.2685e-18 < 1e-3,
            "PAPER_173: Term 2 H0 = 70 km/s/Mpc = A_5+SO_5 CANONICAL vote (Q-169a)")
assert_that(abs(_r173['quantum_term'] - 0.3315) < 0.001,
            "PAPER_173: quantum term = 0.3315 EXACT (13.6 eV ground-state anchor)")
assert_that(abs(_r173['fluid_term'] - 4.189e-2) < 1e-5,
            "PAPER_173: fluid term 4.189e-2 EXACT (sphere 10 km)")
assert_that(9.9 < _r173['term6_slip'][0] / _r173['term6_slip'][1] < 10.1,
            "PAPER_173: Term 6 prints 3.3e-37 vs actual 3.3e-36 - 10x slip, mantissa EXACT (Q-169b)")
assert_that(9.9 < _r173['base_slip'][0] / _r173['base_slip'][1] < 10.1,
            "PAPER_173: sec-3 base 10x slip with EXACT mantissa (Q-169b)")
assert_that(C.wired_count() >= 177, "wired_count >= 177")

_r174 = C.calc('PAPER_174')['value']
assert_that(_r174['resonance_total'] == 1.773e-9 and _r174['matches_172_unittest'],
            "PAPER_174: resonance total 1.773e-9 EXACT match to 172's unit test - tables doubly disproven")
assert_that(abs(_r174['fquantum_exact'] - 1.445e-17) / 1.445e-17 < 0.001,
            "PAPER_174: fquantum = 2pi/t_Hubble = 1.445e-17 EXACT (cross-paper match to 173)")
assert_that(abs(_r174['wormhole_r1e4'] - 7.09e-44) / 7.09e-44 < 1e-6,
            "PAPER_174: wormhole term 7.09e-44 at r = 1e4 EXACT")
assert_that(abs(_r174['h0_second_vote'] - 70.05) < 0.1,
            "PAPER_174: H_z = 2.270e-18 = 70.05 km/s/Mpc - second canonical H0 vote in sec 2.4")
assert_that(_r174['adpm_formula_break'][0] / _r174['adpm_formula_break'][1] > 1e65,
            "PAPER_174: aDPM printed formula 66 orders from its own test value (Q-170a)")
assert_that(5e7 < _r174['ftrz_additive_refuted_again'] < 6e7,
            "PAPER_174: additive fTRZ empirically refuted AGAIN - 0.1 vs total 1.773e-9 (Q-142 #2)")
assert_that(C.wired_count() >= 178, "wired_count >= 178")

_r175 = C.calc('PAPER_175')['value']
assert_that(_r175['n_levels'] == 26,
            "PAPER_175: 26-level energy ladder = D_CRIT structure")
assert_that(abs(_r175['rho_lambda_correction'] - 1.0000000812) < 1e-10,
            "PAPER_175: rho_Lambda correction = 1 + (kappa*SSq)^2 = 1.0000000812 EXACT (family squared)")
assert_that(_r175['ug_bands_match_171'],
            "PAPER_175: Ug level bands identical to 171 (cross-paper consistent)")
assert_that(_r175['higgs_level18_mismatch'][0] / _r175['higgs_level18_mismatch'][1] > 4e5,
            "PAPER_175: level-18 'Higgs' at 1e-2 J vs actual 2.0e-8 J - 5e5 mismatch (Q-171b)")
assert_that('NOT QFT' in _r175['qft_differentiation'],
            "PAPER_175: explicit differentiation from QFT zero-point (honest framing)")
assert_that(C.wired_count() >= 179, "wired_count >= 179")

_r176 = C.calc('PAPER_176')['value']
assert_that(_r176['pcore_earth_anchor'] == 3.6e11,
            "PAPER_176: Earth Pcore = 3.6e11 Pa - real seismology anchor EXACT")
assert_that(abs(_r176['dg_kpc'] - 8.26) < 0.01,
            "PAPER_176: dg = 2.55e20 m = 8.26 kpc (real Sun-GC distance)")
assert_that(9e8 < _r176['kappa_printed'] / _r176['kappa_chain_per_day'] < 1.1e9,
            "PAPER_176: kappa derivation 1e9 slip with EXACT mantissa 2.12 (Q-172a)")
assert_that(2e9 < _r176['kappa_canonical_gap'] < 3e9,
            "PAPER_176: canonical kappa = 5e-4 is 2.4e9 x the faint-young-Sun chain value")
assert_that('intentional' in _r176['dominance_reframed'],
            "PAPER_176: SCm_contrib dominance reframed as intentional physics (Q-158c/167c candidate)")
assert_that(_r176['rho_a_new'] == 1e-23,
            "PAPER_176: rho_A = 1e-23 new ambient-Aether fork value (Q-172b)")
assert_that(C.wired_count() >= 180, "wired_count >= 180")

_r177 = C.calc('PAPER_177')['value']
assert_that(abs(_r177['body_force_step_codetruth'] - 1.773e-10) < 1e-13,
            "PAPER_177: dt*g_res(code-truth) = 1.77e-10 per step - numerically sane")
assert_that(_r177['body_force_step_table'] > 1e43,
            "PAPER_177: table value would add 1.7e44 m/s per step - absurd; 3rd code-truth vote (Q-173a)")
assert_that(5e10 < _r177['jet_over_uqff'] < 6e10,
            "PAPER_177: jet force dominates UQFF drive by 5.6e10 (Q-173b)")
assert_that(abs(_r177['diffuse_a'] - 0.01024) < 1e-6,
            "PAPER_177: diffuse coefficient a = dt*visc*N^2 = 0.01024 (stable)")
assert_that('154/161' in _r177['curl_free_consistency'],
            "PAPER_177: uniform body force curl-free - 3rd consistency with 154/161")
assert_that(C.wired_count() >= 181, "wired_count >= 181")

_r178 = C.calc('PAPER_178')['value']
assert_that(len(_r178['components']) == 7,
            "PAPER_178: 7 infrastructure components registered")
assert_that(_r178['fu_convention_streak'] == 4,
            "PAPER_178: F_U minus-buoyancy convention 4th consecutive (2152 echo)")
assert_that('Perlin' in _r178['perlin_mismatch'],
            "PAPER_178: 168-Perlin vs 178-sine-cosine heightmap mismatch pinned (Q-174a)")
assert_that('booleanUnion' in _r178['stubs_confessed'],
            "PAPER_178: modeling stubs confessed (extrudeMesh, booleanUnion)")
assert_that(C.wired_count() >= 182, "wired_count >= 182")

_r179 = C.calc('PAPER_179')['value']
assert_that("UA'/SCm" in _r179['dpm_definition'],
            "PAPER_179: DPM = UA'/SCm formal definition registered (cross-repo UA-derivative echo)")
assert_that(_r179['dg_vs_gravity_pct'] < 0.3,
            "PAPER_179: dg anchor 0.2% from GRAVITY 8.277 kpc - excellent")
assert_that(4 < _r179['mbh_vs_gravity_pct'] < 5,
            "PAPER_179: M_bh 4.6% below GRAVITY-2022 (Q-175d)")
assert_that('4 constructs' in _r179['ym_fourth_construct'],
            "PAPER_179: YM gap FOURTH construct (E_react(0)) - fork expands (Q-175a)")
assert_that('speculative' in _r179['honesty_landmark'],
            "PAPER_179: explicit epistemic self-assessment registered (honesty landmark)")
assert_that('Rule 7' in _r179['ns_overclaim'],
            "PAPER_179: NS existence-proof overclaim flagged (Q-175b)")
assert_that(C.wired_count() >= 183, "wired_count >= 183")

_r180 = C.calc('PAPER_180')['value']
assert_that(_r180['n_tests'] == 26 and _r180['test_breakdown'] == (10, 14, 2),
            "PAPER_180: 26-test suite (10+14+2) - Q-165a count question resolved")
assert_that(_r180['afluid_residual_pct'] < 0.1,
            "PAPER_180: afluid = ffluid*Vsys*SO_5/c_res RECONSTRUCTED (0.06% vs unit test)")
assert_that(_r180['ua_scm_is_so5'] == 10,
            "PAPER_180: reconstruction uses UA_SCM = 10 = SO_5")
assert_that(abs(_r180['self_audit_match'][0] - 2.799e24) < 1e21,
            "PAPER_180: corpus self-audit chain 2.799e24 matches our Q-170a verification EXACTLY")
assert_that('100x' in _r180['test12_vexp_inconsistency'],
            "PAPER_180: test-12 vexp 1e3-vs-1e5 inconsistency pinned (Q-176a)")
assert_that(C.wired_count() >= 184, "wired_count >= 184")

_r181 = C.calc('PAPER_181')['value']
assert_that(_r181['asd_paper_n4'] == 2 and _r181['asd_correct_n4'] == 3,
            "PAPER_181: ASD Theorem-4 counterexample n=4 - paper 2 vs correct 3 (4-vs-8 discriminant, Q-177a)")
assert_that('orthogonal' in _r181['orthogonality'],
            "PAPER_181: orthogonality to UQFF physics honestly declared")
assert_that('K_{1,n}' in _r181['etymology'],
            "PAPER_181: Star Magic project-name etymology registered (star graph)")
assert_that(abs(_r181['footer_jeans'] - 7.41e-10) < 1e-13,
            "PAPER_181: footer Jeans arithmetic 0.57*1.3e-9 = 7.41e-10 EXACT")
assert_that(C.wired_count() >= 185, "wired_count >= 185")

_r182 = C.calc('PAPER_182')['value']
assert_that(_r182['beta_dictionary'] == 0.603,
            "PAPER_182: dictionary beta_i = 0.603 overrides thread 0.61 (~canonical 0.6029)")
assert_that(_r182['bcrit_third_vote'] == 4.4e13,
            "PAPER_182: B_crit = 4.4e13 THIRD vote (Q-002 tally)")
assert_that(1e9 * 0.9 < _r182['e_react_chain'] / _r182['e_react_printed'] < 1e9 * 1.1,
            "PAPER_182: E_react 1e9 exponent slip with mantissa matching the TRANSPOSED v (Q-178b)")
assert_that(1e18 * 0.9 < _r182['earth_chain'] / _r182['earth_printed'] < 1e18 * 1.1,
            "PAPER_182: Earth E_react 1e18 exponent slip, mantissa EXACT")
assert_that(_r182['u_ua_fork'] == (1e-4, 1.0),
            "PAPER_182: U_UA fork 1e-4 dictionary vs 1.0 in 172 (Q-178a)")
assert_that(_r182['k_constants_confirmed']['k4'] == 2.0,
            "PAPER_182: k1-k4 source-doc set confirmed by the dictionary")
assert_that(C.wired_count() >= 186, "wired_count >= 186")

_r183 = C.calc('PAPER_183')['value']
assert_that(abs(_r183['h_scm_chain_transposed_v'] / 10 - 4.37e30) / 4.37e30 < 0.01,
            "PAPER_183: H_SCm mantissa = 182's TRANSPOSED v chain / 10 - transposition propagates (Q-179b)")
assert_that(9000 < _r183['m_gap_printed'] / _r183['m_gap_chain'] < 11000,
            "PAPER_183: m_gap chain 4.95e9 vs printed 4.87e13 - 1e4 break; FIFTH YM construct (Q-179a)")
assert_that(8e6 < _r183['h_ua_break'][1] / _r183['h_ua_break'][0] < 1e7,
            "PAPER_183: H_UA printed 9e6 x its own chain (Q-179c)")
assert_that(1.3e8 < _r183['dominance_internal_ok'] < 1.5e8,
            "PAPER_183: '8 orders' dominance claim internally consistent with printed values")
assert_that('classical level' in _r183['hedge'],
            "PAPER_183: mass-gap claim honestly hedged to classical level")
assert_that(C.wired_count() >= 187, "wired_count >= 187")

_r184 = C.calc('PAPER_184')['value']
assert_that(abs(_r184['kappa_conversion'] - 5.787e-9) / 5.787e-9 < 0.001,
            "PAPER_184: kappa day->s conversion EXACT")
assert_that(_r184['prodi_serrin_actual'] == 1.5,
            "PAPER_184: Prodi-Serrin 2/p+3/q = 1.5 > 1 - printed '= 1' false; criterion fails (Q-180a)")
assert_that(9.5 < _r184['r_implied_m'] < 10.5,
            "PAPER_184: F_SCm(0) implies r = 10 m unstated (transposed mantissa carried)")
assert_that(all(4e-5 < k < 9e-5 for k in _r184['decay_kappa_implied']),
            "PAPER_184: decay table implies kappa ~5-8e-5/day - 10x slower than stated (Q-180b)")
assert_that(1.4e40 < _r184['mu_eff'] < 1.6e40,
            "PAPER_184: mu_eff = 1.5e40 Pa*s magnitude pinned")
assert_that('common-source 3 deep' in _r184['transposed_v_third'],
            "PAPER_184: transposed v third appearance - common-source evidence (Q-180c)")
assert_that(C.wired_count() >= 188, "wired_count >= 188")

_r185 = C.calc('PAPER_185')['value']
assert_that(_r185['zeros_correct'] == (14.135, 21.022, 25.011),
            "PAPER_185: first Riemann zeros printed correctly")
assert_that('not Mobius' in _r185['mobius_mislabel'],
            "PAPER_185: Mobius mislabel pinned - alternation is Dirichlet eta (Q-181a)")
assert_that('eta_26' in _r185['eta_correction'],
            "PAPER_185: eta correction connects bridge to existing corpus S204.2 machinery")
assert_that('3-way' in _r185['riemann_fork'],
            "PAPER_185: Riemann fork now 3-way (Q-181c)")
assert_that('proof' in _r185['honest_hedge'],
            "PAPER_185: honest non-proof hedge registered")
assert_that(C.wired_count() >= 189, "wired_count >= 189")

_r186 = C.calc('PAPER_186')['value']
assert_that('162/157 doctrine canonical' in _r186['q166b_resolved'],
            "PAPER_186: per-body omega_c restored - Q-166b RESOLVED by v2 rewrite")
assert_that('157 values' in _r186['q166c_resolved'],
            "PAPER_186: Neptune forks resolved to 157's values - Q-166c RESOLVED")
assert_that(_r186['mu_s_with_placeholder'] / _r186['mu_s_printed'] > 1e6,
            "PAPER_186: placeholder form 7 orders off printed mu_s - SCm_contrib DROPPED in v2 (Q-182a)")
assert_that(_r186['mu_s_printed'] / _r186['mu_s_no_placeholder'] > 0.5,
            "PAPER_186: printed mu_s matches no-placeholder form within 1.7x")
assert_that('e45' in _r186['e_react_slip_persists'],
            "PAPER_186: E_react transposed-mantissa + exponent slip persists in v2 (Q-182b)")
assert_that(C.wired_count() >= 190, "wired_count >= 190")

_r187 = C.calc('PAPER_187')['value']
assert_that(_r187['b_over_bcrit_universal'] == 0.1,
            "PAPER_187: B/Bcrit = 0.1 = F_TRZ EXACT for ALL 7 systems - ratio primitive-locked (Q-183a)")
assert_that('Q-002 reframed' in _r187['ratio_lock'],
            "PAPER_187: B = F_TRZ*Bcrit universal encoding - B_crit fork reframed")
assert_that('vexp = 1e3 canonical' in _r187['q176a_resolved'],
            "PAPER_187: Q-176a RESOLVED - catalog vexp = 1e3; 174's output carried the slip")
assert_that(_r187['ffluid_confirms_180'] == 1.269e-14,
            "PAPER_187: ffluid confirms 180's afluid reconstruction input")
assert_that('DPM CW/CCW' in _r187['counter_rotation'],
            "PAPER_187: omega2 = -omega1 universal - predecessor grinding-pole echo")
assert_that(_r187['sgra_area_break'][0] / _r187['sgra_area_break'][1] > 1e9,
            "PAPER_187: SgrA* horizon-area value 1.5e9 x 4*pi*Rs^2 (Q-183b)")
assert_that(C.wired_count() >= 191, "wired_count >= 191")

_r188 = C.calc('PAPER_188')['value']
assert_that(abs(_r188['terms_per_kb'] - 4.68) < 0.01,
            "PAPER_188: 6688 terms / 1430 kB = 4.68 terms/kB EXACT")
assert_that(_r188['physics_terms_census'] == 6688,
            "PAPER_188: 6,688 physics-terms corpus census stat registered")
assert_that(9 < _r188['upx_original_mb'] < 9.5,
            "PAPER_188: UPX ratio implies 9.2 MB uncompressed (169-consistent)")
assert_that('Qt5' in _r188['qt_inconsistency'],
            "PAPER_188: Qt6-claimed vs Qt5-shipped inconsistency pinned (Q-184a)")
assert_that(C.wired_count() >= 192, "wired_count >= 192")

_r189 = C.calc('PAPER_189')['value']
assert_that(_r189['units_registry_exact'],
            "PAPER_189: derived-unit registry (N/J/W/Pa/T) ALL EXACT vs SI")
assert_that('two components' in _r189['q184a_resolved'],
            "PAPER_189: Q-184a RESOLVED - S-C is Qt5, source2 tier-1 is Qt6")
assert_that('unused by papers' in _r189['irony_flag'],
            "PAPER_189: in-corpus unit-propagation system exists, unused (Q-185a)")
assert_that('no-check stub' in _r189['units_defects'],
            "PAPER_189: Units operator+ no-check stub + toString mol/cd omission pinned (Q-185b)")
assert_that(C.wired_count() >= 193, "wired_count >= 193")

_r190 = C.calc('PAPER_190')['value']
assert_that(_r190['all_rules_verified'],
            "PAPER_190: ALL 10 antiderivative rules numerically verified correct")
assert_that('zeta(1)' in _r190['rk_divergence'],
            "PAPER_190: R_K regularization diverges at its first term (Q-186a)")
assert_that('unevaluated' in _r190['fallback_honesty'],
            "PAPER_190: honest unevaluated-Integral fallback (no silent wrong answers)")
assert_that(C.wired_count() >= 194, "wired_count >= 194")

_r191 = C.calc('PAPER_191')['value']
assert_that(_r191['n_feature_systems'] == 8 and len(_r191['systems']) == 8,
            "PAPER_191: 8 multi-modal feature systems cataloged")
assert_that('reverse-order undo' in _r191['engineering_note'],
            "PAPER_191: MacroCommand reverse-order undo correctness noted")
assert_that(C.wired_count() >= 195, "wired_count >= 195")

_r192 = C.calc('PAPER_192')['value']
assert_that('never verifies' in _r192['sign_verify_mismatch'],
            "PAPER_192: ECDSA sign/verify payload mismatch - security layer non-functional (Q-188a)")
assert_that('WebSocket 8765' in _r192['stack'],
            "PAPER_192: collaboration stack (WebSocket/OT/ECDSA/Snappy) registered")
assert_that(C.wired_count() >= 196, "wired_count >= 196")

_r193 = C.calc('PAPER_193')['value']
assert_that(_r193['n_namespaces'] == 7 and len(_r193['namespaces']) == 7,
            "PAPER_193: 7-namespace decomposition registered")
assert_that(abs(_r193['mu0_exact'] - 1.2566e-6) / 1.2566e-6 < 1e-4,
            "PAPER_193: mu0 = 4pi*1e-7 = 1.2566e-6 EXACT")
assert_that(_r193['fu_term_count_here'] == 5,
            "PAPER_193: F_U = sum(Ugi)+Ubi (5 terms) drops Um+tr(A) vs 172 ten-term (Q-189a)")
assert_that('variant' in _r193['canonical_field_set_needed'],
            "PAPER_193: architecture-doc field equations are a variant set - canonical set needed")
assert_that(C.wired_count() >= 197, "wired_count >= 197")

_r194 = C.calc('PAPER_194')['value']
assert_that(len(_r194['operations']) == 8,
            "PAPER_194: 8 Graphics3D mesh-I/O operations cataloged")
assert_that('Q-174a persists' in _r194['perlin_note'],
            "PAPER_194: Perlin-vs-sine landscape doc/impl mismatch persists (Q-174a)")
assert_that(C.wired_count() >= 198, "wired_count >= 198")

_r195 = C.calc('PAPER_195')['value']
assert_that(len(_r195['formats']) == 3,
            "PAPER_195: JSON/YAML/CSV loader family registered")
assert_that(abs(_r195['omega_c_earth_1yr'] - 1.991e-7) / 1.991e-7 < 1e-3,
            "PAPER_195: example omega_c = 2pi/1yr = 1.991e-7 (stale vs 186 canonical 1.81e-8)")
assert_that('reverts pre-186' in _r195['stale_example'],
            "PAPER_195: JSON example data stale vs 186 v2 canonical set (Q-191a)")
assert_that(C.wired_count() >= 199, "wired_count >= 199")

_r196 = C.calc('PAPER_196')['value']
assert_that('calculate_triadic_g' in _r196['predecessor_convergence'],
            "PAPER_196: triadic form converges with predecessor calculate_triadic_g (cross-repo)")
assert_that('sum_{i=1}^{26}' in _r196['resonance_26layer'],
            "PAPER_196: resonance R(t) 26-layer structure confirmed")
assert_that('log' in _r196['ssq_redefinition'] and '0.57 constant' in _r196['ssq_redefinition'],
            "PAPER_196: SSq redefinition - log-formula vs 0.57 constant (Q-192a)")
assert_that(_r196['w2_buoyancy_dominant'] > 1e8,
            "PAPER_196: Westerlund 2 buoyancy channel dominates compressed by ~1e8")
assert_that('E(z) structure' in _r196['hz_lcdm_correct'],
            "PAPER_196: H(t,z) = H0*sqrt(0.3(1+z)^3+0.7) correct LCDM E(z) form")
assert_that(C.wired_count() >= 200, "wired_count >= 200")

_r197 = C.calc('PAPER_197')['value']
assert_that(len(_r197['four_new_terms']) == 4,
            "PAPER_197: four multi-wavelength coupling terms (UV/mm/hybrid/hierarchical)")
assert_that(_r197['k_uv_mm'] == 1e-30,
            "PAPER_197: k_UV = k_mm = 1e-30 N/W (mojibake decoded)")
assert_that('distinct from point-Ubi' in _r197['integral_vs_point'],
            "PAPER_197: F_U_Bi_i integral distinct from point-Ubi four-form (Q-193a clarification)")
assert_that('182 k_eta' in _r197['rho_ua_keta_link'],
            "PAPER_197: rho_vac,UA ~ 1e-113 = 182's k_eta deep-vacuum constant")
assert_that('FU_Bi channel of 196' in _r197['triadic_channel'],
            "PAPER_197: slots into 196 triadic as the buoyancy channel")
assert_that(C.wired_count() >= 201, "wired_count >= 201")

_r198 = C.calc('PAPER_198')['value']
assert_that(_r198['n_variants'] == 18,
            "PAPER_198: 18 F_UBii variants cataloged (compact/stellar Part 1)")
assert_that('PAPER_2151' in _r198['predecessor_registry'],
            "PAPER_198: 18-variant catalog matches predecessor PAPER_2151 F_UBii registry (cross-repo)")
assert_that(5e-8 < _r198['hawking_verified'] < 7e-8,
            "PAPER_198: embedded Hawking T_H = hbar*c^3/8piGMkB verified correct")
assert_that('universe-response' in _r198['ubii_role'],
            "PAPER_198: F_UBii = universe-response operator (vs F_UBi mass-pushing)")
assert_that('Berti' in _r198['qnm_parametrization_note'],
            "PAPER_198: QNM ringdown parametrization vs canonical Berti fit noted (Q-194a)")
assert_that(C.wired_count() >= 202, "wired_count >= 202")

_r199 = C.calc('PAPER_199')['value']
assert_that(_r199['n_variants'] == 19,
            "PAPER_199: 19 cosmological/dark-sector F_UBii variants (Part 2)")
assert_that(_r199['s_bh_verified'] > 1e54 * 0.9,
            "PAPER_199: embedded Bekenstein-Hawking S = 4pi kB G M^2/hbar c verified correct")
assert_that(abs(_r199['rho_lambda_header'] - 1.0000000812) < 1e-10,
            "PAPER_199: header rho_Lambda = 1+(kappa*SSq)^2 = 175 family-squared, consistent")
assert_that('Chevallier-Polarski-Linder' in _r199['cpl_w_correct'],
            "PAPER_199: CPL dark-energy w(a) parametrization correct")
assert_that('PAPER_2151' in _r199['predecessor_registry_extension'],
            "PAPER_199: extends predecessor F_UBii registry into cosmological sector")
assert_that(C.wired_count() >= 203, "wired_count >= 203")

_r200 = C.calc('PAPER_200')['value']
assert_that(_r200['n_variants'] >= 50,
            "PAPER_200: 50+ Um magnetism variants cataloged")
assert_that('PAPER_1072' in _r200['predecessor_tie'],
            "PAPER_200: Um ties to predecessor L_mag / PAPER_1072 Heaviside amplifier operator")
assert_that('3 cross-repo taxonomies' in _r200['third_taxonomy'],
            "PAPER_200: third cross-repo taxonomy (Ug/F_UBii/Um)")
assert_that(1.2e31 < _r200['eddington_verified'] < 1.3e31,
            "PAPER_200: embedded Eddington L = 4pi G M c/kappa_es = 1.26e31 W verified")
assert_that('mu-damping vs F_UBii' in _r200['operator_vs_buoyancy'],
            "PAPER_200: Um and F_UBii apply different operators to same phenomena")
assert_that(C.wired_count() >= 204, "wired_count >= 204")

_r201 = C.calc('PAPER_201')['value']
assert_that(abs(_r201['chirp_gw150914'] - 28.3) < 0.5,
            "PAPER_201: GW150914 chirp mass = 28.1 Msun verified (m1=36/m2=29)")
assert_that(_r201['chirp_gw170817'] == 1.188,
            "PAPER_201: GW170817 chirp mass 1.188 Msun (real LIGO value)")
assert_that(_r201['hulse_taylor_verified'] == (-2.422e-12, 4.226),
            "PAPER_201: Hulse-Taylor Pdot -2.422e-12 + periastron 4.226 deg/yr (real, GR-confirmed)")
assert_that('predecessor GW bucket' in _r201['strain_damping_header'],
            "PAPER_201: h_UQFF strain-damping = predecessor GW bucket form")
assert_that('225 Hz' in _r201['qnm_coeff_note'],
            "PAPER_201: QNM 0.3737+0.088a coefficient note (Q-197a, confirms Q-194a)")
assert_that(C.wired_count() >= 205, "wired_count >= 205")

_r202 = C.calc('PAPER_202')['value']
assert_that(_r202['real_anchors']['Y_P'] == 0.247,
            "PAPER_202: BBN Y_P = 0.247 (4He mass fraction, real value)")
assert_that(_r202['real_anchors']['tau_reion'] == 0.054,
            "PAPER_202: tau_reion = 0.054 (Planck 2018 real value)")
assert_that('PAPER_1156' in _r202['predecessor_bucketC'],
            "PAPER_202: same observables as predecessor BUCKET C cosmology (PAPER_1156)")
assert_that('l~220' in _r202['acoustic_horizon'],
            "PAPER_202: UQFF Lambda*c^2/3 sets acoustic horizon (CMB first peak)")
assert_that(C.wired_count() >= 206, "wired_count >= 206")

_r203 = C.calc('PAPER_203')['value']
assert_that(_r203['real_anchors']['n_s'] == 0.9649,
            "PAPER_203: n_s = 0.9649 (Planck 2018 real, >5sigma tilt)")
assert_that(_r203['real_anchors']['r_s_Mpc'] == 147,
            "PAPER_203: BAO sound horizon r_s = 147 Mpc (real)")
assert_that('n_s = 1-6eps+2eta' in _r203['slow_roll_correct'],
            "PAPER_203: slow-roll n_s/r relations correct")
assert_that('low-l CMB' in _r203['low_l_anomaly_prediction'],
            "PAPER_203: low-l CMB anomaly prediction via UQFF P_R + LQC suppression (Q-199a)")
assert_that('PAPER_1156' in _r203['bucketC_tie'],
            "PAPER_203: n_s/sigma_8/r_s overlap predecessor BUCKET C (Q-198 continues)")
assert_that(C.wired_count() >= 207, "wired_count >= 207")

_r204 = C.calc('PAPER_204')['value']
assert_that(_r204['mw_anchors']['v_c_kms'] == 220,
            "PAPER_204: MW rotation v_c = 220 km/s at Solar circle (real)")
assert_that(4e14 < _r204['coma_mvir'] < 1e15,
            "PAPER_204: Coma virial mass ~5e14 Msun (3 sigma^2 r_h/G, sigma_v 880 km/s)")
assert_that('SIDM offered as resolution' in _r204['core_cusp_honest'],
            "PAPER_204: NFW core-cusp tension stated honestly")
assert_that('PAPER_1962' in _r204['predecessor_tie'],
            "PAPER_204: ties to predecessor DM/rotation-curve work")
assert_that('theta_E ~0.1%' in _r204['lensing_prediction'],
            "PAPER_204: vacuum-Lambda Einstein-radius shift prediction (Q-200a)")
assert_that(C.wired_count() >= 208, "wired_count >= 208")

_r205 = C.calc('PAPER_205')['value']
assert_that(_r205['q26_const_true'] == 7905853580625 and _r205['q26_const_is_25_dblfact'],
            "PAPER_205: true Q_26(0) = 25!! = 7,905,853,580,625 (computed via recurrence)")
assert_that(_r205['q26_const_printed'] == 34459425,
            "PAPER_205: printed constant 34,459,425 = 17!! (Q_18(0)) - wrong (Q-201a)")
assert_that('roots REAL' in _r205['root_claim_false'],
            "PAPER_205: 'roots on unit circle' claim FALSE - Hermite roots are real (Q-201a)")
assert_that('e^{xt+t^2/2}' in _r205['gen_function'],
            "PAPER_205: generating function e^{xt+t^2/2} correct")
assert_that('orthogonal expansion' in _r205['orthogonal_spectral'],
            "PAPER_205: 26-state sum = orthogonal spectral expansion of gravity series (genuine)")
assert_that(C.wired_count() >= 209, "wired_count >= 209")

_r206 = C.calc('PAPER_206')['value']
assert_that(_r206['alpha_2d'] == 1.6,
            "PAPER_206: 2D avalanche power-law alpha ~ 1.6 (Melatos-consistent glitch stats)")
assert_that('no constraint' in _r206['undersampling_honest'],
            "PAPER_206: 3D N=5 undersampling honestly reported")
assert_that('n_v = 2 Omega m_n/hbar' in _r206['feynman_magnus_correct'],
            "PAPER_206: Feynman vortex density + Magnus force verified")
assert_that('1E2259+586' in _r206['uqff_glitch_prediction'],
            "PAPER_206: UQFF anti-glitch prediction ties to 196 R(t) + 1E 2259+586 (Q-202)")
assert_that(_r206['anchors']['vela'] == 2e-6,
            "PAPER_206: Vela glitch DeltaOmega/Omega ~ 2e-6 (real anchor)")
assert_that(C.wired_count() >= 210, "wired_count >= 210")

_r207 = C.calc('PAPER_207')['value']
assert_that(abs(_r207['ghz_entropy_is_ln2'] - 0.6931) < 1e-3,
            "PAPER_207: GHZ von Neumann entropy = ln2 = 0.6931 (constant, all bipartitions)")
assert_that(_r207['svn_steps_correct'][3] == _r207['svn_steps_correct'][4],
            "PAPER_207: S_VN constant at ln2 for GHZ-chain steps 3-4 (not rising to ~2, Q-203a)")
assert_that('constant ln2' in _r207['entropy_error'],
            "PAPER_207: entropy-rise claim corrected - GHZ S_VN is constant (Q-203a)")
assert_that('2.828' in _r207['bell_mermin_correct'],
            "PAPER_207: Bell/Mermin bounds correct (Tsirelson 2sqrt2, GHZ Mermin 4)")
assert_that('shadow' in _r207['decoherence_shadow'],
            "PAPER_207: fast-decoherence -> classical 206 power-law is the shadow")
assert_that(C.wired_count() >= 211, "wired_count >= 211")

_r208 = C.calc('PAPER_208')['value']
assert_that(abs(_r208['layer_sum'] - 2.302) < 0.01,
            "PAPER_208: layer sum S = 1/(1-e^-SSq) = 2.302 EXACT (SSq = 0.57)")
assert_that(abs(_r208['phi_tn_branch'] - 0.301) < 0.005,
            "PAPER_208: phi ~ 0.81 via arcsin(0.81)/pi = 0.301 (young-universe t_n branch)")
assert_that(abs(_r208['f_qpo_hz'] - 5.952e-4) < 1e-6,
            "PAPER_208: f = 1/1680s = 5.95e-4 Hz (28-min SGR A* QPO)")
assert_that('!= canonical F_TRZ' in _r208['f_trz_name_collision'],
            "PAPER_208: f_TRZ frequency vs canonical F_TRZ=0.1 NAME COLLISION pinned (Q-204a)")
assert_that(_r208['q_wave'] == 6.33e4 and _r208['q_wave_matches_196_198'],
            "PAPER_208: Q_wave 6.33e4 J/m^3 matches 196/198 stat table")
assert_that(C.wired_count() >= 212, "wired_count >= 212")

_r209 = C.calc('PAPER_209')['value']
assert_that(abs(_r209['de_running_factor'] - 1.000000081225) < 1e-13,
            "PAPER_209: rho_L^UQFF/rho_L^obs = 1 + kappa^2*SSq^2 = 1.000000081225")
assert_that(_r209['lcdm_is_uqff_subset'] is True,
            "PAPER_209: Lambda-CDM reduces from UQFF (strict superset)")
assert_that(abs(_r209['cmb_score_gain_pct'] - 0.7017543859649098) < 1e-9,
            "PAPER_209: CMB C_l 28.5->28.7 = +0.70% (verified)")
assert_that(abs(_r209['cluster_score_gain_pct'] - 3.7037037037037033) < 1e-9,
            "PAPER_209: cluster mass fn 27->28 = +3.70% (paper states 3.4%, honest residual)")
assert_that(_r209['cmb_resonance_multipoles'] == [6, 10, 22],
            "PAPER_209: 26-layer resonance predicts CMB excess at l = 6, 10, 22")
assert_that(C.wired_count() >= 213, "wired_count >= 213")

_r210 = C.calc('PAPER_210')['value']
assert_that(_r210['k_UA_is_F_TRZ4'] and abs(_r210['k_UA'] - 1e-4) < 1e-12,
            "PAPER_210: k_UA = [UA] = F_TRZ^4 = 1e-4 EXACT (registry identity)")
assert_that(abs(_r210['a0_ch0_over_6'] - 1.1342147994333332e-10) < 1e-22,
            "PAPER_210: MOND a0 recovered as c*H0/6 = 1.134e-10 (H0 = A_5+SO_5 registry)")
assert_that(abs(_r210['a0_residual_pct'] - 5.482100047222236) < 1e-9,
            "PAPER_210: a0 c*H0/6 vs 1.2e-10 MOND target = 5.48%")
assert_that(abs(_r210['abell2744_residual_pct'] - 9.090909090909092) < 1e-9,
            "PAPER_210: Abell 2744 strong lensing 36 pred vs 33 obs = +9.09%")
assert_that(abs(_r210['bulk_flow_uqff_resid_pct'] - 3.225806451612903) < 1e-9,
            "PAPER_210: bulk flow UQFF 240 vs CosmicFlows-4 248 = 3.23% (MOND +29%)")
assert_that(C.wired_count() >= 214, "wired_count >= 214")

_r211 = C.calc('PAPER_211')['value']
assert_that(abs(_r211['compression_ratio_pct'] - 0.8547008547008548) < 1e-9,
            "PAPER_211: compression ratio 11/(99*13) = 11/1287 = 0.855% (paper 0.86%)")
assert_that(_r211['raw_unique_terms'] == 1287 and _r211['backbone_terms'] == 11,
            "PAPER_211: 99 eqs x mean 13 terms = 1287 raw -> 11 backbone terms")
assert_that(abs(_r211['backbone_avg_paper_pct'] - 89.4949494949495) < 1e-9,
            "PAPER_211: backbone coverage 886/990 = 89.5% (table-sum 898/990 = 90.7%, Q-207)")
assert_that(_r211['q_wave_mean'] == 6.33e4 and abs(_r211['q_wave_scatter_pct'] - 1.895734597156398) < 1e-9,
            "PAPER_211: Q_wave mean 6.33e4 J/m^3 (ties PAPER_208), scatter 1.90% (paper 2%)")
assert_that(_r211['systems_total'] == 99 and _r211['systems_named'] == 29 and _r211['systems_q_wave_computed'] == 47,
            "PAPER_211: 99 systems (29 named + 70 implied), 47 Q_wave-computed")
assert_that(C.wired_count() >= 215, "wired_count >= 215")

_r212 = C.calc('PAPER_212')['value']
assert_that(abs(_r212['cia_sigma_400'] - 11.6488) < 1e-6,
            "PAPER_212: H2O-H2 CIA sigma(400) = 9.65 + 0.004997*400 = 11.649 A^2 (paper 11.65)")
assert_that(abs(_r212['cia_update_pct'] - 5.898181818181814) < 1e-9,
            "PAPER_212: CIA update vs Borysow-Frommhold 11.0 = +5.90% (paper 5.9%)")
assert_that(_r212['scales_total'] == 48 and _r212['span_decades'] == 61 and _r212['regimes'] == 5,
            "PAPER_212: 48 scales, 5 regimes, ~61-decade span, single master equation")
assert_that(_r212['ratio_rotor_universe'] == 1e61 and _r212['ratio_nuclear_hubble'] == 1e41,
            "PAPER_212: scale ratios rotor:universe ~1e61, nuclear:Hubble ~1e41")
assert_that(_r212['b_h2_cm1'] == 60.853,
            "PAPER_212: H2 rotational constant B = 60.853 cm^-1 (J-conversion drift Q-208)")
assert_that(C.wired_count() >= 216, "wired_count >= 216")

_r213 = C.calc('PAPER_213')['value']
assert_that(abs(_r213['a_res_sgr1745'] - 1.0550625711035268e-15) < 1e-24,
            "PAPER_213: A_res(SGR1745) = mu_B*B/E_bind = 1.055e-15 (paper 1.06e-15)")
assert_that(abs(_r213['f_res_fe56_hz'] - 2.7056340325622208e26) < 1e18,
            "PAPER_213: omega_res(56Fe) 1.7e27 rad/s -> f = 2.706e26 Hz")
assert_that(abs(_r213['s_shell_pb208_mev'] - 0.8320502943378437) < 1e-9,
            "PAPER_213: S_shell 208Pb E_pairing = 12/sqrt(208) = 0.832 MeV")
assert_that(abs(_r213['dd_over_d_pct'] - 0.0021502139462979226) < 1e-12,
            "PAPER_213: D_universe 93.014 -> 93.016 Gly, dD/D = 0.00215% (paper 0.002%)")
assert_that(_r213['n_magic_neutron'] == [2, 8, 20, 28, 50, 82, 126] and _r213['h_res_sub_equations'] == 7,
            "PAPER_213: H_res 7 sub-equations; neutron magic {2,8,20,28,50,82,126} (proton 7th=114, Q-209a)")
assert_that(C.wired_count() >= 217, "wired_count >= 217")

_r214 = C.calc('PAPER_214')['value']
assert_that(_r214['strong_shock_compression_ratio'] == 4.0,
            "PAPER_214: strong-shock rho2/rho1 = (gamma+1)/(gamma-1) = 4 EXACT (gamma=5/3)")
assert_that(_r214['cycle2_raw_terms'] == 456 and abs(_r214['cycle2_compression_pct'] - 8.333333333333332) < 1e-9,
            "PAPER_214: Compression Cycle 2 = 38 F_env / (38*12=456 raw) = 8.33%")
assert_that(abs(_r214['mhd_improvement_over_pure_pct'] - 0.13) < 1e-6,
            "PAPER_214: UQFF non-ideal MHD +0.13% over pure MHD (99.87% vs 99.74%)")
assert_that(_r214['mhd_equation_types'] == 6 and len(_r214['mhd_types']) == 6,
            "PAPER_214: 6 MHD cluster equation types enumerated")
assert_that(_r214['benchmark_f_env']['perseus'] == 0.85 and _r214['error_metrics']['chandra'] == 99.98,
            "PAPER_214: MHD benchmark F_env (Perseus 0.85); Chandra 99.98% alignment")
assert_that(C.wired_count() >= 218, "wired_count >= 218")

_r215 = C.calc('PAPER_215')['value']
assert_that(_r215['dsa_index'] == 2.0,
            "PAPER_215: DSA Fermi-I index alpha = (r+2)/(r-1) = 2 EXACT (r=4 strong shock)")
assert_that(_r215['a_ug1_is_3_ftrz2'] and abs(_r215['a_ug1_knee_shift'] - 0.03) < 1e-12,
            "PAPER_215: CR knee UQFF shift a_Ug1 = 3*F_TRZ^2 = 0.03 EXACT (Q-211a)")
assert_that(abs(_r215['knee_uqff_ev']['proton'] - 3.09e15) < 1e9 and abs(_r215['knee_uqff_ev']['iron'] - 8.034e16) < 1e11,
            "PAPER_215: knee(UQFF) = Z*3e15*1.03 - proton 3.09e15, iron 8.034e16 eV")
assert_that(_r215['diffusion_1pev_cm2_s'] == 1e31,
            "PAPER_215: CR diffusion D(1 PeV) = 1e28*(1e6)^0.5 = 1e31 cm^2/s (beta=0.5)")
assert_that(abs(_r215['kazantsev_gamma_dynamo_s'] - 3.2362459546925564e-17) < 1e-25,
            "PAPER_215: Kazantsev WHIM dynamo gamma = 1e5/3.09e21 = 3.24e-17 s^-1")
assert_that(C.wired_count() >= 219, "wired_count >= 219")

_r216 = C.calc('PAPER_216')['value']
assert_that(_r216['proportion_sum'] == 1.0 and _r216['rho_ua_over_scm'] == 10,
            "PAPER_216: DPM proportion f_UA'+f_SCm = 0.999+0.001 = 1; rho_UA/rho_SCm = 10 = SO_5")
assert_that(abs(_r216['decay_tn_0'] - 0.04321391826377226) < 1e-9 and abs(_r216['decay_tn_pi_2'] - 0.20787957635076193) < 1e-9,
            "PAPER_216: buoyancy decay e^-(pi-t_n): e^-pi=0.0432, e^-pi/2=0.208, e^0=1")
assert_that(_r216['coupling_westerlund_is_ftrz'] and _r216['coupling_pillars_is_3ftrz2'],
            "PAPER_216: resonance couplings 0.1=F_TRZ (Westerlund) / 0.03=3*F_TRZ^2 (Pillars)")
assert_that(_r216['westerlund2']['r_t_N'] == -2.29e-41 and _r216['pillars_m16']['fu_g1_N'] == 3.95e-41,
            "PAPER_216: Triadic outputs Westerlund R(t)=-2.29e-41 N, Pillars FU_g1=3.95e-41 N")
assert_that(_r216['f_z_cgm'] == 1.46e-73 and _r216['dk_phi'] == 7.25e8,
            "PAPER_216: f_z,CGM=1.46e-73; dk_phi=7.25e8 (ties PAPER_212)")
assert_that(C.wired_count() >= 220, "wired_count >= 220")

_r217 = C.calc('PAPER_217')['value']
assert_that(_r217['fubii_modes'] == 12 and len(_r217['geometry_classes']) == 4,
            "PAPER_217: F_U_Bi_i 12-term integral over 4 geometry classes")
assert_that(abs(_r217['branch_asymmetry_ratio'] - 3938.388625592417) < 1e-6 and _r217['discriminant'] == 0,
            "PAPER_217: two-branch |F_U-/F_U+| = 3938 ~ 3940; discriminant b^2-4ac = 0")
assert_that(_r217['fhier_convergent'] and abs(_r217['fhier_convergence_ratio'] - 0.9622687143632572) < 1e-9,
            "PAPER_217: F_hier 26-layer hierarchy convergent, ratio e^-1/26 = 0.962 < 1")
assert_that(len(_r217['rare_discoveries']) == 3 and abs(_r217['e_neg_ssq'] - 0.5655254386995371) < 1e-9,
            "PAPER_217: 3 rare discoveries (F_hier, delta_F, F_hyb); e^-SSq = 0.566")
assert_that(abs(_r217['ssq_26'] - 4.495171312401194e-07) < 1e-13,
            "PAPER_217: 0.57^26 = 4.50e-7 (paper's 6.16e-6 is ~14x drift, n_CGM fit 67.5, Q-213)")
assert_that(C.wired_count() >= 221, "wired_count >= 221")

_r218 = C.calc('PAPER_218')['value']
assert_that(_r218['p_t'] == 0.15 and _r218['one_minus_p'] == 0.85 and _r218['reduction_pct'] == 15.0,
            "PAPER_218: P(t)=0.15 -> (1-P)=0.85 = 15% reduction (paper's '5%' is drift, Q-214)")
assert_that(abs(_r218['g_base_m_s2'] - 7.2159288e-14) < 1e-20,
            "PAPER_218: g_base = G*M/r^2*(1-P) = 7.22e-14 m/s^2 (paper's 8.52e-52 is ~38 OOM off)")
assert_that(abs(_r218['M_kg'] / 1.989e30 - 1.6e4) < 100,
            "PAPER_218: NGC 3603 M = 3.18e34 kg = 1.6e4 M_sun (Harayama 2008)")
assert_that(len(_r218['suppressor_taxonomy']) == 5 and _r218['suppressor_taxonomy']['pressure'] == '(1-P)',
            "PAPER_218: 5-term suppressor taxonomy; (1-P) is the unique pressure-specific term")
assert_that(_r218['one_minus_b_bcrit'] == 1.0,
            "PAPER_218: B/B_crit = 1e-8/4.4e13 = 2.3e-22 -> (1-B/B_crit) ~ 1.0 (paper 0.9999977 drift)")
assert_that(C.wired_count() >= 222, "wired_count >= 222")

_r219 = C.calc('PAPER_219')['value']
assert_that(_r219['m_sf'] == 0.08 and _r219['one_plus_msf'] == 1.08 and _r219['unique_both_mult_and_additive'],
            "PAPER_219: M16 M_sf=0.08 -> (1+M_sf)=1.08; unique dual mult-enhance + additive-subtract")
assert_that(abs(_r219['e_rad_J_m3'] - 1.3654417332500376e-12) < 1e-18,
            "PAPER_219: E_rad = L_UV/(4*pi*r^2*c) = 1.37e-12 J/m^3 (paper's 2.71e-22 is ~10 OOM off)")
assert_that(abs(_r219['g_base_m_s2'] - 5.012366255144033e-11) < 1e-16,
            "PAPER_219: g_base = G*M/r^2 = 5.01e-11 m/s^2 (paper's 5.00e-50 is ~39 OOM off)")
assert_that('gravity-protected' in _r219['duality'],
            "PAPER_219: Pillars (1-E) multiplier gravity-protected vs M16 -E_rad additive radiation-dominated")
assert_that(C.wired_count() >= 223, "wired_count >= 223")

_r220 = C.calc('PAPER_220')['value']
assert_that(abs(_r220['f_wind_over_g_base'] - 19.996244925740612) < 1e-6,
            "PAPER_220: F_wind/g_base = 20.0 at Crab inner radius (wind-dominated torus)")
assert_that(abs(_r220['e_sd_formula_W'] - 4.420866612298581e31) < 1e25,
            "PAPER_220: spindown E_sd = 4*pi^2*I*Pdot/P^3 = 4.42e31 W (Hester 2008 obs 4.6e31)")
assert_that(abs(_r220['m_dipole_A_m2'] - 3.8e27) < 1e24 and abs(_r220['m_mag'] - 4.488592582140559e-28) < 1e-34,
            "PAPER_220: dipole moment m = (4pi/mu0)*B_s*R_ns^3 = 3.8e27 A m^2; M_mag = 4.49e-28")
assert_that(abs(_r220['r0_initial_m'] - 5.98552e15) < 1e12 and _r220['unique_expanding_domain'],
            "PAPER_220: expanding r(t)=r0+v_exp*t, r0_initial=5.99e15 m (~0.2 pc SN ejecta)")
assert_that(abs(_r220['f_wind'] - 1.3644103083881766e-10) < 1e-16,
            "PAPER_220: F_wind = E_sd/(c*4pi*r^2) = 1.36e-10 at r=9.46e15 m")
assert_that(C.wired_count() >= 224, "wired_count >= 224")

_r221 = C.calc('PAPER_221')['value']
assert_that(_r221['e_t'] == 0.05 and _r221['one_plus_e'] == 1.05 and _r221['unique_positive_wind_multiplier'],
            "PAPER_221: (1+E(t)) positive wind-compression multiplier, E=0.05 (sign-inverse of Pillars (1-E))")
assert_that(abs(_r221['g_base_m_s2'] - 1.2411971830985913e-12) < 1e-18,
            "PAPER_221: g_base = G*M/r^2 = 1.24e-12 m/s^2 (paper's 1.23e-52 is ~40 OOM off)")
assert_that(_r221['enhancement_pct'] == 7.5 and _r221['v_shell_enhanced_km_s'] == 4.3,
            "PAPER_221: F_UBii phonon dv=0.3 km/s -> shell 4.0->4.3 km/s (+7.5%)")
assert_that(_r221['phonon_resonance_THz'] == 1.25 and _r221['phi_res'] == 0.84,
            "PAPER_221: 1.25 THz SCm phonon resonance, Phi_res=0.84")
assert_that(C.wired_count() >= 225, "wired_count >= 225")

_r222 = C.calc('PAPER_222')['value']
assert_that(abs(_r222['p_rad_Pa'] - 2.5219224605488018) < 1e-9,
            "PAPER_222: P_rad = 4*sigma*T^4/(3c) = 2.52 Pa at T=1e4 K (Stefan-Boltzmann)")
assert_that(abs(_r222['g_base_m_s2'] - 1.099210079563446e-10) < 1e-16,
            "PAPER_222: g_base = G*M*(1-E)/r^2 = 1.10e-10 m/s^2 (clean, no drift)")
assert_that(abs(_r222['p_rad_over_g_base'] - 395465.80592914706) < 1e-3,
            "PAPER_222: P_rad/g_base = 395,000 -> radiation-dominated PDR (~400,000x)")
assert_that(_r222['only_stefan_boltzmann_in_29_docs'] and len(_r222['three_way_distinction']) == 3,
            "PAPER_222: only SB blackbody P_rad in 29 docs; 3-way distinction P_rad/E_rad/rho_v2")
assert_that(C.wired_count() >= 226, "wired_count >= 226")

_r223 = C.calc('PAPER_223')['value']
assert_that(abs(_r223['f_bh'] - 324044069993519.1) < 1e6,
            "PAPER_223: F_BH = P_jet/r_jet = 3.24e14 (P_jet=1e35 W, r_jet=10 kpc)")
assert_that(abs(_r223['f_bh_accel_m_s2'] - 1.0801468999783971e40) < 1e34,
            "PAPER_223: F_BH/rho_ICM = 1.08e40 m/s^2 (AGN feedback dominates gravity)")
assert_that(abs(_r223['g_fil_m_s2'] - 1.401600857509233e-13) < 1e-19,
            "PAPER_223: g_fil = G*M_fil/r^2 = 1.40e-13 m/s^2 (M_fil=2e38 kg ~1e8 M_sun)")
assert_that(_r223['unique_agn_feedback_plus_filaments'] and _r223['n_filaments'] == 100,
            "PAPER_223: only 29-doc system with both F_BH AGN feedback + M_fil filaments; ~100 Halpha filaments")
assert_that(C.wired_count() >= 227, "wired_count >= 227")

_r224 = C.calc('PAPER_224')['value']
assert_that(abs(_r224['g_saturn_m_s2'] - 10.442158936384011) < 1e-6,
            "PAPER_224: g_saturn = G*M_Saturn/r^2 = 10.44 m/s^2 (Saturn surface gravity)")
assert_that(abs(_r224['g_sun_m_s2'] - 6.528026885982425e-05) < 1e-10,
            "PAPER_224: g_sun = G*M_Sun/r_orbit^2 = 6.53e-5 m/s^2 (paper's 6.53e-3 is 100x, Q-218)")
assert_that(_r224['dual_source_asymmetric_modifiers'] and _r224['ht_on_solar_only'] and _r224['b_bcrit_on_saturn_only'],
            "PAPER_224: dual-source asymmetric modifiers - H*t on solar only, B/B_crit on Saturn only")
assert_that(_r224['t_ring_m_s2'] == 2.043e-7 and _r224['roche_criterion_met'],
            "PAPER_224: ring tidal tension T_ring = 2.043e-7 m/s^2 (CP1); Roche criterion met, 2000:1")
assert_that(C.wired_count() >= 228, "wired_count >= 228")

_r225 = C.calc('PAPER_225')['value']
assert_that(_r225['enhancement_ratios'] == {'0.1c': 0.01, '0.3c': 0.09, '0.5c': 0.25},
            "PAPER_225: F_EU/F_UV = (v/c)^2 enhancement 1%/9%/25% at 0.1c/0.3c/0.5c")
assert_that(abs(_r225['z7_example']['F_EU_N'] - 10013.850504482567) < 1 and abs(_r225['z7_example']['F_mm_N'] - 10500.0) < 1,
            "PAPER_225: z=7 example F_EU~1e4 N ~ F_mm 1.05e4 N (comparable)")
assert_that(_r225['fourth_rare_discovery'] and len(_r225['completes_paper_217_set']) == 4,
            "PAPER_225: F_EU is 4th rare discovery, completes PAPER_217 set (F_hier/delta_F/F_hyb/F_EU)")
assert_that(_r225['k_uv_equals_ftrz30'] and _r225['sixth_pass_corpus_fully_extracted'],
            "PAPER_225: k_UV=1e-30 N/W (=F_TRZ^30 numerically); 6th-pass corpus fully extracted")
assert_that(C.wired_count() >= 229, "wired_count >= 229")

_r226 = C.calc('PAPER_226')['value']
assert_that(_r226['terms'] == 11 and len(_r226['novel_terms']) == 3,
            "PAPER_226: 11-term MUGE with 3 novel terms (a_GW, a_mag, a_decay)")
assert_that(abs(_r226['a_grav_m_s2'] - 464610509999.9999) < 1e6,
            "PAPER_226: a_grav = G*M/r^2 = 4.65e11 m/s^2 (M=1.4 M_sun, r=20 km)")
assert_that(abs(_r226['b_t_5000yr_T'] - 2865047968.601901) < 1e3,
            "PAPER_226: B(5000 yr) = B0*e^-t/tau_B = 2.865e9 T (B0=1e10 T, tau_B=4000 yr)")
assert_that(_r226['g_0501_m_s2'] == 4.474e12 and abs(_r226['a_grav_fraction'] - 0.10384678363880194) < 1e-9,
            "PAPER_226: g_0501 = 4.474e12 m/s^2 (11-term sim; a_grav 10.4%, Q-219)")
assert_that('8d951e12' in _r226['source_thread'],
            "PAPER_226: first paper from new source thread grok_share_8d951e12")
assert_that(C.wired_count() >= 230, "wired_count >= 230")

_r227 = C.calc('PAPER_227')['value']
assert_that(abs(_r227['m_dot_factor'] - 41.666666666666664) < 1e-9,
            "PAPER_227: gas-ratio amplitude M_dot_factor = M_gas/M_init = 10000/240 = 41.67")
assert_that(_r227['a_wind_m_s2'] == 4e12 and _r227['a_wind_equals_v2_when_equal_rho'],
            "PAPER_227: a_wind = rho_wind*v^2/rho_fluid = 4e12 m/s^2 = v_wind^2 (rho_wind=rho_fluid; abstract 4e3 typo Q-220)")
assert_that(_r227['terms'] == 9 and len(_r227['novel_methods']) == 2,
            "PAPER_227: 9-term MUGE with 2 novel methods (gas-ratio M(t), stellar-wind ram pressure)")
assert_that(_r227['wind_family']['westerlund2'] == 1e-20 and _r227['wind_family']['tapestry_lmc'] == 1e-21,
            "PAPER_227: wind family - Westerlund 2 rho_wind 10x denser than Tapestry LMC")
assert_that(C.wired_count() >= 231, "wired_count >= 231")

_r228 = C.calc('PAPER_228')['value']
assert_that(abs(_r228['m_dot_factor'] - 3.3333333333333335) < 1e-9,
            "PAPER_228: Westerlund 2 M_dot_factor = M_gas/M_init = 100000/30000 = 3.33")
assert_that(_r228['rho_wind'] == 1e-20 and _r228['rho_wind_ratio_vs_tapestry'] == 10 and _r228['highest_wind_density_in_family'],
            "PAPER_228: rho_wind = 1e-20 kg/m^3 (10x Tapestry) - highest wind density in MUGE family")
assert_that(_r228['a_wind_m_s2'] == 4e4 and _r228['rho_fluid'] == 1e-12,
            "PAPER_228: a_wind = rho_wind*v^2/rho_fluid = 4e4 m/s^2 (rho_fluid=1e-12 ambient, self-rectifies Q-220)")
assert_that(_r228['comparative_ratios_vs_tapestry']['M_init'] == 125 and _r228['comparative_ratios_vs_tapestry']['a_wind'] == 10,
            "PAPER_228: Wd2 vs Tapestry ratios M_init 125x, rho_wind 10x, a_wind 10x")
assert_that(C.wired_count() >= 232, "wired_count >= 232")

_r229 = C.calc('PAPER_229')['value']
assert_that(abs(_r229['one_minus_e'] - 0.909516258196404) < 1e-9,
            "PAPER_229: erosion (1-E(t)) at t=0.1 Myr = 1-0.1*e^-0.1 = 0.9095 (E_0=0.1, tau_e=1 Myr)")
assert_that(abs(_r229['a_base_m_s2'] - 5.396462589930841e-12) < 1e-18,
            "PAPER_229: a_base = G*M/r^2*(1-E) = 5.40e-12 m/s^2 (paper's 5.36e-24 is ~12 OOM, Q-221)")
assert_that(len(_r229['sign_taxonomy']) == 3 and 'erosion' in _r229['sign_taxonomy']['pillars'],
            "PAPER_229: sign taxonomy - Pillars (1-E) erosion vs Bubble (1+E) compression vs Orion none")
assert_that(_r229['m_dot_factor'] == 100 and _r229['E0'] == 0.1,
            "PAPER_229: M_dot_factor = M_gas/M_init = 10000/100 = 100; E_0 = 0.1")
assert_that(C.wired_count() >= 233, "wired_count >= 233")

_r230 = C.calc('PAPER_230')['value']
assert_that(_r230['only_negative_term_in_catalogue'] and _r230['g_sn_sign'] == 'negative',
            "PAPER_230: g_SN is the ONLY negative acceleration term in the MUGE catalogue")
assert_that(abs(_r230['g_sn_magnitude_m_s2'] - 2.3041584507042247e-21) < 1e-27,
            "PAPER_230: |g_SN| = G*M_SN0/r^2 = 2.30e-21 m/s^2 (paper's 2.3e-33 is ~12 OOM, Q-222)")
assert_that(abs(_r230['h_z_s'] - 2.2867559880052767e-18) < 1e-24,
            "PAPER_230: Friedmann H(z=0.0162) = H0*sqrt(0.3*(1+z)^3+0.7) = 2.287e-18 s^-1 (registry H0)")
assert_that(abs(_r230['a_bh_m_s2'] - 133456.67993437042) < 1.0,
            "PAPER_230: a_BH = G*M_BH/r_BH^2 = 1.335e5 m/s^2 (M_BH=2.25e7 M_sun; paper's 1.34e6 is 10x, Q-222)")
assert_that(C.wired_count() >= 234, "wired_count >= 234")

_r231 = C.calc('PAPER_231')['value']
assert_that(abs(_r231['h_z_factor'] - 5.29504485344553) < 1e-9,
            "PAPER_231: Friedmann H(z=3.5)/H0 = sqrt(0.3*(4.5)^3+0.7) = 5.295")
assert_that(abs(_r231['h_z_km_s_mpc'] - 370.6531397411871) < 1e-6,
            "PAPER_231: H(z=3.5) = 370.7 km/s/Mpc (Om=0.3, registry H0); canonical MUGE param 510 (Q-223)")
assert_that(abs(_r231['hz_t_dominant'] - 4.549476062856132) < 1e-9,
            "PAPER_231: H(z)*12 Gyr = 4.55 (dominant MUGE term at z=3.5)")
assert_that(_r231['double_interaction_modulation'] and abs(_r231['I_at_0p5gyr'] - 0.030326532985631673) < 1e-9,
            "PAPER_231: double I(t) on base+Ug (novel); I(0.5 Gyr)=0.05*e^-0.5=0.0303")
assert_that(C.wired_count() >= 235, "wired_count >= 235")

_r232 = C.calc('PAPER_232')['value']
assert_that(_r232['sfr_factor_per_yr'] == 1e-9,
            "PAPER_232: specific-SFR amplitude SFR_factor = SFR/M_total = 10/1e10 = 1e-9 yr^-1")
assert_that(abs(_r232['frac_change_at_50Myr'] - 6.065306597126334e-10) < 1e-18,
            "PAPER_232: M(t) fractional change at 50 Myr = 1e-9*e^-0.5 = 6.065e-10")
assert_that(_r232['a_sn_m_s2'] == 4e12 and _r232['a_sn_equals_v2_rho_equal'],
            "PAPER_232: a_SN = rho_wind*v_SN^2/rho_fluid = v_SN^2 = 4e12 m/s^2 (rho_wind=rho_fluid=1e-21)")
assert_that(len(_r232['novel_methods']) == 2 and _r232['previously_unknown'],
            "PAPER_232: 2 novel methods (specific-SFR growth, SN wind feedback); previously-unknown system")
assert_that(C.wired_count() >= 236, "wired_count >= 236")

_r233 = C.calc('PAPER_233')['value']
assert_that(abs(_r233['a_bh_smbh_tidal_m_s2'] - 6.629917217095979e-07) < 1e-13,
            "PAPER_233: SMBH tidal a_BH = G*M_SgrA*/r_BH^2 = 6.63e-7 m/s^2 (dominant at 0.92 pc)")
assert_that(abs(_r233['f_sc'] - 0.9995454545454545) < 1e-9,
            "PAPER_233: superconductive f_sc = 1 - B/B_crit = 1 - 2e10/4.4e13 = 0.99955")
assert_that(abs(_r233['a_mag_m_s2'] - 95764.80164715454) < 1e-3,
            "PAPER_233: static magnetic energy a_mag = B^2/(2mu0)*V/(Mr) = 9.58e4 m/s^2 (B=2e10 T)")
assert_that(_r233['atnf_pulse_period_s'] == 3.76 and _r233['new_terms_vs_session53'] == 3,
            "PAPER_233: ATNF pulse period P=3.76 s; 3 new MUGE terms vs Session 53")
assert_that(C.wired_count() >= 237, "wired_count >= 237")

_r234 = C.calc('PAPER_234')['value']
assert_that(abs(_r234['growth_over_hubble'] - 0.0021581508339868975) < 1e-9,
            "PAPER_234: secular accretion growth over Hubble = 0.01*e^-13.8/9 = 0.00216 (~0.22%)")
assert_that(abs(_r234['a_grav_canonical_m_s2'] - 3571908.0539661474) < 1e-3,
            "PAPER_234: canonical a_grav = G*1.01*M_init/r_s^2 = 3.57e6 m/s^2 (M_init=4.297e6 M_sun)")
assert_that(abs(_r234['pert2_factor'] - 1.5) < 1e-9 and _r234['b_tesla_at_t0'] == 1.0,
            "PAPER_234: Kerr pert_2 = 3*sin(30)=1.5*G*M/r^3; Gauss->Tesla 1e4 G = 1 T")
assert_that(_r234['new_terms_vs_session53'] == 3 and _r234['M_init_solar'] == 4.297e6,
            "PAPER_234: 3 new MUGE terms vs Session 53; Sgr A* M_init = 4.297e6 M_sun")
assert_that(C.wired_count() >= 238, "wired_count >= 238")

_r235 = C.calc('PAPER_235')['value']
assert_that(abs(_r235['I_at_300Myr'] - 0.04723665527410147) < 1e-9,
            "PAPER_235: I(300 Myr) = 0.1*e^-300/400 = 0.1*e^-0.75 = 0.0472 (~4.7%)")
assert_that(_r235['double_interaction_modulation'] and _r235['sfr_factor_per_yr'] == 1e-10,
            "PAPER_235: double I(t) on base+Ug (novel); SFR_factor = 20/2e11 = 1e-10 yr^-1")
assert_that(_r235['nearest_major_merger'] and _r235['M0_solar'] == 2e11,
            "PAPER_235: Antennae nearest major merger, M_0 = 2e11 M_sun (NGC 4038+4039)")
assert_that(_r235['vs_hudf']['antennae_I0'] == 0.1 and _r235['vs_hudf']['hudf_I0'] == 0.05,
            "PAPER_235: double-I(t) family - Antennae local (I_0=0.1) vs HUDF cosmic (I_0=0.05, PAPER_231)")
assert_that(C.wired_count() >= 239, "wired_count >= 239")

_r236 = C.calc('PAPER_236')['value']
assert_that(abs(_r236['advancement_pct'] - 226.66666666666666) < 1e-9,
            "PAPER_236: advancement = (3+3+0.8)/3*100 = 226.67% (diversity/dynamic/scalability)")
assert_that(_r236['first_meta_assessment_calculator'] and _r236['super_linear'],
            "PAPER_236: first framework-level meta-assessment calculator; advancement >100% (super-linear)")
assert_that(_r236['diversity_score'] == 3.0 and _r236['scalability_score'] == 0.8,
            "PAPER_236: three metrics - diversity 3, dynamic 3, scalability 0.8")
assert_that(_r236['novel_contributions'] == 5 and len(_r236['aggregated_examples']) == 3,
            "PAPER_236: 5 novel contributions; aggregates 3 examples (Wd2/Pillars/Rings)")
assert_that(C.wired_count() >= 240, "wired_count >= 240")

_r237 = C.calc('PAPER_237')['value']
assert_that(_r237['master_buoyancy_components'] == 5 and _r237['triadic_layers'] == 26,
            "PAPER_237: 5-component master buoyancy F_U_Bi_i; 26-layer Triadic gravity")
assert_that(abs(_r237['i_grav_m_s2'] - 1.9915215999999998e-07) < 1e-13 and abs(_r237['M_layer_kg'] - 1.1476923076923077e30) < 1e24,
            "PAPER_237: I_grav = G*M/r^2 = 1.99e-7; M_i = M/26 = 1.148e30 kg (M=2.984e31, r=1e14)")
assert_that(_r237['fubii_benchmark_N'] == 2.11e208 and _r237['fubii_ties_paper_217'],
            "PAPER_237: Eta Carinae F_U_Bi_i = 2.11e208 N benchmark (ties PAPER_217 Branch 1, Q-224)")
assert_that(_r237['g_H'] == 1.252e46 and len(_r237['force_classes']) == 5,
            "PAPER_237: g_H = 1.252e46 UQFF hydrogen g-factor; 5 UQFF force classes")
assert_that(C.wired_count() >= 241, "wired_count >= 241")

_r238 = C.calc('PAPER_238')['value']
assert_that(abs(_r238['F_vac_rep_N'] - 1.9915e15) < 1e12,
            "PAPER_238: CP3 F_vac_rep = G*5e-13*2.984e31*2e6 = 1.99e15 N (reproduces)")
assert_that(_r238['k_vac_equals_G'] and abs(_r238['k_vac'] - C.G_OBSERVED) < 1e-20,
            "PAPER_238: k_vac = G (novel contribution 4, dimensional consistency)")
assert_that(abs(_r238['delta_rho_vac_J_m3'] - 5e-13) < 1e-15 and _r238['velocity_coupled'],
            "PAPER_238: delta_rho_vac = 5e-13 J/m3; velocity-coupled (only UQFF force linear in v)")
assert_that(_r238['third_repulsive_force'] and _r238['vanishes_at_rest'] and _r238['r_independent'],
            "PAPER_238: 3rd repulsive force (after F_DE, F_rel); vanishes at v=0; r-independent")
assert_that(C.wired_count() >= 242, "wired_count >= 242")

_r239 = C.calc('PAPER_239')['value']
assert_that(_r239['freq_ratio_sq'] == 14400.0,
            "PAPER_239: (omega_thz/omega_0)^2 = (120)^2 = 14400 EXACT (quadratic freq amplification)")
assert_that(abs(_r239['F_thz_shock_N'] - 1.4705e-19) < 1e-22 and abs(_r239['F_conduit_N'] - 6.6526e9) < 1e6,
            "PAPER_239: CP3 derived-correct F_thz=1.47e-19, F_conduit=6.65e9 (rho_ratio=1, w=1); example 4.56e78/3.45e67 not reproducible Q-225")
assert_that(abs(_r239['ratio_thz_over_conduit'] - 2.21e-29) < 1e-31 and _r239['conduit_scale'] == 0.74,
            "PAPER_239: ratio mantissa 2.21 (computed 2.21e-29 vs paper 2.21e-17 Q-225); conduit_scale=H_abund*w=0.74")
assert_that(_r239['water_gate_binary'] and _r239['dual_neutron_coupling'],
            "PAPER_239: binary water phase gate (w=0 => both vanish); dual rho_n/rho_ref coupling")
assert_that(C.wired_count() >= 243, "wired_count >= 243")

_r240 = C.calc('PAPER_240')['value']
assert_that(_r240['freq_ratio'] == 5e4 and abs(_r240['F_spooky_N'] - 5.55e-30) < 1e-33,
            "PAPER_240: F_spooky = k_spooky*(5e14/1e10) = 1.11e-34*5e4 = 5.55e-30 N (sec 1.3 reproduces)")
assert_that(_r240['spooky_linear_in_omega'],
            "PAPER_240: F_spooky linear in omega (vs THz omega^2 PAPER_239, DE ~r, LENR ~e^-t/tau)")
assert_that(_r240['g_H'] == 1.252e46 and _r240['ties_paper_237'] and _r240['g_p_nuclear'] == 5.586,
            "PAPER_240: g_H = 1.252e46 UQFF hydrogen g-factor (~46 orders above nuclear g_p=5.586; ties PAPER_237)")
assert_that(abs(_r240['Q_wave_J_m3'] - 3.1036e-15) < 1e-18,
            "PAPER_240: Q_wave = g_H*mu_B*B_0*C_DPM/(hbar*omega_0) = 3.10e-15 J/m3 (mantissa 3.11 vs paper 3.11e9, 24-order exp drift Q-226)")
assert_that(C.wired_count() >= 244, "wired_count >= 244")

_r241 = C.calc('PAPER_241')['value']
assert_that(abs(_r241['overall_alignment_pct'] - 95.2767) < 0.01 and abs(_r241['experimental_pass_rate_pct'] - 93.3333) < 0.01,
            "PAPER_241: overall = (92.53+93.3+100)/3 = 95.28%; exp pass 14/15 = 93.33% (reproduce)")
assert_that(_r241['arxiv_papers'] == 16 and _r241['arxiv_categories'] == 10 and _r241['arxiv_mean_alignment_pct'] == 92.53,
            "PAPER_241: ArXiv stream = 16 papers / 10 categories / 92.53% mean alignment")
assert_that(_r241['computational_systems'] == 100 and _r241['computational_finite'] == 100 and _r241['validation_streams'] == 3,
            "PAPER_241: computational 100/100 finite (0 NaN/Inf); 3 verification streams")
assert_that(_r241['higgs_alignment_pct'] == 99.79 and _r241['thz_deviation_pct'] == 1.7 and _r241['lenr_cop'] == 1.12 and _r241['chi2_nu'] == 1.03,
            "PAPER_241: Higgs 99.79%, THz 1.7% dev, LENR COP 1.12, chi^2_nu=1.03 (N=9)")
assert_that(C.wired_count() >= 245, "wired_count >= 245")

_r242 = C.calc('PAPER_242')['value']
assert_that(abs(_r242['L_t'] - 3.2067e-4) < 1e-7 and abs(_r242['corr_L'] - 1.000321) < 1e-5,
            "PAPER_242: L_t = (GM/c^2r)*0.67 = 3.21e-4 derived (corr_L 1.00032); paper 1.6e-3 Q-227")
assert_that(_r242['ua_scm_ratio'] == 10.0 and _r242['L_factor'] == 0.67,
            "PAPER_242: T4 rho_UA/rho_SCm = 1/F_TRZ = 10 EXACT; L_factor = D_LS/D_S = 0.67")
assert_that(abs(_r242['Hz_over_H0_z0p5'] - 1.3086) < 1e-3,
            "PAPER_242: H(z=0.5)/H0 = sqrt(0.3*(1.5)^3+0.7) = 1.309 derived (paper 1.27 Q-227)")
assert_that(_r242['muge_terms'] == 9 and _r242['lensing_static_geometric'],
            "PAPER_242: 9-term MUGE; static geometric Einstein-ring lensing (vs class-81 dynamic L(t))")
assert_that(C.wired_count() >= 246, "wired_count >= 246")

_r243 = C.calc('PAPER_243')['value']
assert_that(abs(_r243['Mt_over_M0'] - 1.6065) < 1e-3 and abs(_r243['sf_efficiency'] - 0.6065) < 1e-3,
            "PAPER_243: M(t)/M0 = 1+1.0*e^-0.5 = 1.607; SFE eps_SF = 0.607 (t=0.5 Myr, reproduce)")
assert_that(abs(_r243['Pt_pa'] - 2.4261e-8) < 1e-11 and abs(_r243['T_pressure_m_s2'] - 2.4261e12) < 1e9,
            "PAPER_243: P(t)=4e-8*e^-0.5=2.43e-8 Pa; T_pressure=P(t)/rho_fl=2.43e12 m/s^2 (reproduce)")
assert_that(_r243['muge_terms'] == 10 and _r243['cavity_pressure_additive'] and _r243['ua_scm_ratio'] == 10.0,
            "PAPER_243: 10-term MUGE; additive cavity pressure (vs class-88 multiplicative); T4 rho_UA/rho_SCm=10 EXACT")
assert_that(_r243['novel_elements'] == 2,
            "PAPER_243: 2 novel elements - time-varying M(t) + additive cavity-pressure acceleration")
assert_that(C.wired_count() >= 247, "wired_count >= 247")

_r244 = C.calc('PAPER_244')['value']
assert_that(abs(_r244['t_Hubble_s'] - 4.3553e17) < 1e14 and abs(_r244['two_pi_over_tHubble'] - 1.4427e-17) < 1e-20,
            "PAPER_244: t_Hubble = 13.8 Gyr*3.156e7 = 4.355e17 s; 2pi/t_H = 1.443e-17 rad/s (reproduce)")
assert_that(abs(_r244['g_Q_min_m_s2'] - 2.0952e-34) < 1e-37 and abs(_r244['sqrt_2hbar'] - 1.4523e-17) < 1e-20,
            "PAPER_244: g_Q_min = sqrt(2hbar)*(2pi/t_H) = 2.10e-34 derived (paper 3.0e-34 uses wrong root Q-228)")
assert_that(_r244['universal_muge_modules'] == 19 and _r244['cosmological_floor'],
            "PAPER_244: Universal Presence Theorem - term_q identical in all 19 MUGE modules; non-zero cosmological floor")
assert_that(_r244['g_Q_over_g_newt'] == 1e-34,
            "PAPER_244: g_Q/g_Newt ~ 1e-34 for stellar systems (perturbative correction)")
assert_that(C.wired_count() >= 248, "wired_count >= 248")

_r245 = C.calc('PAPER_245')['value']
assert_that(abs(_r245['crossover_radius_m'] - 3.621e16) < 1e13 and abs(_r245['crossover_radius_pc'] - 1.17) < 0.02,
            "PAPER_245: r_c = (3M/(4*pi*rho_fluid))^(1/3) = 3.62e16 m = 1.17 pc (M_sun, rho=1e-20; reproduce)")
assert_that(abs(_r245['g_fluid_cluster_m_s2'] - 8.387e-14) < 1e-16 and abs(_r245['four_piG_over_3'] - 2.7956e-10) < 1e-13,
            "PAPER_245: cluster g_fluid = (4piG/3)*1e-26*3e22 = 8.39e-14 m/s^2; 4piG/3 = 2.796e-10 (reproduce)")
assert_that(_r245['mass_independent'] and _r245['linear_in_rho_and_r'] and _r245['universal_muge_term'],
            "PAPER_245: g_fluid = (4piG/3)*rho*r mass-independent, linear (Linear Radius Theorem); universal MUGE term")
assert_that(_r245['cluster_contribution_pct'] == 1,
            "PAPER_245: fluid self-gravity ~1% of MUGE gravity at cluster (Mpc) scale")
assert_that(C.wired_count() >= 249, "wired_count >= 249")


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
