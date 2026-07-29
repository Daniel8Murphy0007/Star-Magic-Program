"""uqff_calculator — Star-Magic-Program v6-style calculator, rebuilt from whitepaper truth.

DESIGN RULES (locked, non-negotiable):
  1. Line 1 imports from uqff_registry_primitives. Every canonical value flows
     from there. Never inline a numeric literal that duplicates a registry entry.
  2. Every public surface takes signature (paper_id, dataset) and returns
     {'value': X, 'formula': str, 'source': 'PAPER_N', 'residual_pct': r}.
  3. Every surface is 5-30 lines, extracted directly from a whitepaper.
  4. If a whitepaper has no closed form, mark as OPEN — do not substitute a
     classical/SM formula (Rule 4 doctrine).
  5. This file is grown ONE paper at a time. Read whitepaper → wire dispatch →
     verify residual → advance to next.

STATE at v0.1.0 (2026-07-28): scaffold only. Dispatch table is empty; the wiring
campaign starts from PAPER_001 in the first content ship (v0.2.0+).
"""
from uqff_registry_primitives import (
    # Locked primitives
    D_PHYS, D_CRIT, N_CH, SO_5, A_5, D_BSFG,
    RHO_SCM, BETA_I, F_TRZ, SSQ, S_26, OMEGA_SCM_HZ,
    PHI_RES_COUNTING, PHI_RES_RESONANCE,
    # Derivative primitives
    K_MEX, KAPPA_PER_DAY, Q_PHONON, D_GW_EROSION,
    # Composed vacuum
    RHO_UA, LAMBDA_VAC, K_SPRING,
    # Kernel constants
    G_UQFF, G_OBSERVED, C_UQFF_DERIVED, C_OBSERVED, MU_0,
    K_B_UQFF, H_UQFF_S629, HBAR_UQFF_S629, H_PLANCK_UQFF,
    L_PLANCK_UQFF, L_PLANCK_OBSERVED, PLANCK_LENGTH_M,
    PLANCK_MASS_KG, PLANCK_TIME_S,
    # Cosmology
    MPC_TO_M, H0_KM_PER_S_PER_MPC, H0_GRID, H0_OBSERVED_LOCAL,
    LAMBDA_SIMPLE, B_CRIT, T_SCM_K,
    AGE_UNIVERSE_SECONDS, RHO_CRITICAL_KG_PER_M3, RHO_LAMBDA_ENERGY_J_PER_M3,
    OMEGA_LAMBDA_UQFF, HUBBLE_TILT_1_12,
    # Observed
    M_SUN_OBSERVED, R_SUN_OBSERVED,
    # Structural landmarks
    A5_OVER_DPHYS, K2_OVER_Q_ROCKY, FRAME_CADENCE_62,
    COMPOSED_INTEGER_44, AETHER_COUPLING_11, DG_COMPOSED_INTEGER,
    VCK_KERNEL, TILT_PRODUCT_1_12, ALPHA_INVERSE_UQFF, ALPHA_FINE_STRUCTURE,
    DM_FRACTION_SOMBRERO,
    HALVING_D_PHYS, HALVING_D_BSFG, HALVING_SO_5, HALVING_D_CRIT,
    # Blackbody
    WIEN_DISPLACEMENT_B_M_K, STEFAN_BOLTZMANN_SIGMA,
    # Millennium
    HODGE_IDENTITY, POINCARE_7_12, P_VS_NP_BOUND, NAVIER_STOKES_ENSTROPHY_CAP,
    YANG_MILLS_MASS_GAP_GEV, RIEMANN_ZERO_T_10000, BSD_CREMONA_37A1,
    BH_INFO_PAGE_CURVE,
    # Particle physics
    ALPHA_S_M_Z, JARLSKOG_CP_INVARIANT, N_EFF_NEUTRINO, LAMBDA_H_HIGGS_QUARTIC,
    M_W_GEV, M_Z_GEV, M_TOP_GEV, M_HIGGS_GEV,
    M_BOTTOM_GEV, M_CHARM_GEV, M_TAU_GEV, M_MUON_GEV,
    M_STRANGE_GEV, M_ELECTRON_GEV,
    CKM_LAMBDA, CKM_A, CKM_RHOBAR, CKM_ETABAR,
    G_MINUS_2_MUON_ANOMALY, SIN_SQUARED_2_THETA_13,
    DELTA_M2_21_EV2, DELTA_M2_32_EV2,
)

VERSION = "0.12.0"

# =============================================================================
# DISPATCH TABLE — grown one whitepaper at a time.
# Every entry maps 'PAPER_N' -> a callable (dataset) -> {value, formula, ...}
# =============================================================================
DISPATCH = {}


def _register(paper_id):
    """Decorator: registers a paper's calculator surface into DISPATCH."""
    def _wrap(fn):
        DISPATCH[paper_id] = fn
        return fn
    return _wrap


def calc(paper_id, dataset=None):
    """Primary public interface. Look up a paper's dispatch and evaluate it."""
    if paper_id not in DISPATCH:
        return {
            'value': None,
            'formula': None,
            'source': paper_id,
            'residual_pct': None,
            'status': 'OPEN_NOT_YET_WIRED',
        }
    return DISPATCH[paper_id](dataset or {})


def list_wired():
    """Return sorted list of PAPER_Ns currently wired."""
    return sorted(DISPATCH.keys(), key=lambda p: int(p.split('_')[1]))


def wired_count():
    """Return count of wired papers."""
    return len(DISPATCH)


# =============================================================================
# PAPER_N DISPATCHES — sequential wiring campaign from PAPER_001 (see CLAUDE.md)
# =============================================================================


@_register('PAPER_001')
def _paper_001(dataset):
    """GW170817 UQFF Damping Analysis (Session 1).

    BNS merger strain damping: D_total = D_Aether*D_SCm*D_TRZ*D_String.
    Headline 66.7% reduction later canonized as D_GW_EROSION = D_phys/D_BSFG
    = 2/3 EXACT (PAPER_2154 5th primitive-reduction landmark); paper chain
    (0.9*0.37 = 0.333) sits 0.10% from the primitive identity 1/3.
    """
    B_NS = 1.0e4                      # T — typical NS field, paper Table 3.1
    D_aether = 1.0                    # negligible aether coupling at 40 Mpc
    D_scm = 1.0                       # B_NS/B_CRIT = 2.27e-10 << 1
    D_trz = 1.0 - F_TRZ               # 0.9 EXACT (topological resonance zone)
    D_string = 0.37                   # paper-stated string-sector factor
    D_total = D_aether * D_scm * D_trz * D_string      # 0.333
    h_gr = 5.4176e-22                 # LIGO GR peak strain anchor (paper §3.3)
    snr_gr = 32.4                     # GR SNR anchor (paper §3.4)
    d_primitive = 1.0 - D_GW_EROSION  # 1/3 EXACT per PAPER_2154
    return {
        'value': {
            'D_aether': D_aether,
            'D_scm': D_scm,
            'D_trz': D_trz,
            'D_string': D_string,
            'D_total': D_total,
            'D_total_primitive_identity': d_primitive,
            'h_gr_strain': h_gr,
            'h_uqff_strain': D_total * h_gr,             # 1.8041e-22
            'snr_gr': snr_gr,
            'snr_uqff': D_total * snr_gr,                # 10.79
            'mismatch': 1.0 - D_total,                   # 0.667
            'B_NS_over_B_crit': B_NS / B_CRIT,           # 2.27e-10
            'chirp_mass_msun': 1.188,                    # LIGO O2 anchor
            'total_mass_msun': 2.73,                     # LIGO O2 anchor
            'distance_mpc': 40.0,                        # NGC 4993 anchor
            'grb_delay_s': 1.74,                         # GRB 170817A anchor
        },
        'formula': ('D_total = D_Aether*D_SCm*(1-F_TRZ)*D_String; '
                    'h_UQFF = D_total*h_GR; mismatch ~ D_GW_EROSION (PAPER_2154)'),
        'source': 'PAPER_001',
        'residual_pct': abs(D_total - d_primitive) / d_primitive * 100.0,  # 0.10%
    }


@_register('PAPER_002')
def _paper_002(dataset):
    """GW190425 Mass Gap Interpretation (Session 0).

    Heaviest known BNS (3.64 Msun); m1 = 2.52 Msun overlaps the 2.5-5 Msun
    mass gap. SCm suppression is a threshold phenomenon:
    A_SCm(B) = exp[-(B/B_crit)^2], complete only at B >~ 1e15 G.
    OPEN_RULING Q-001: paper states F_UQFF = 0.5297 but its own chain
    1*A_SCm*0.9*0.37 = 0.333; 0.5297 ~ 1-0.47 matches the S225 phonon 47%
    suppression instead. Wired best-candidate: paper-stated headline values.
    """
    import math as _m
    B_crit_G = 4.4e13                 # G here (PAPER_001 used T) — OPEN_RULING Q-002

    def a_scm(B_gauss):
        return _m.exp(-((B_gauss / B_crit_G) ** 2))

    scenarios = {                     # paper sec 4 five-field-scenario table
        'normal_pulsar_1e8G': a_scm(1.0e8),
        'high_b_pulsar_6.95e9G': a_scm(6.95e9),
        'magnetar_4.83e11G': a_scm(4.83e11),
        'extreme_magnetar_3.36e13G': a_scm(3.36e13),   # 0.998871 paper
        'hyper_magnetar_1e15G': a_scm(1.0e15),         # 0.0 paper
    }
    F_uqff = 0.5297                   # paper-stated headline (OPEN_RULING Q-001)
    h_gr = 1.702e-23                  # GR peak strain anchor (paper sec 3)
    return {
        'value': {
            'F_uqff': F_uqff,
            'amplitude_reduction_pct': (1.0 - F_uqff) * 100.0,   # 47.0
            'h_gr_strain': h_gr,
            'h_uqff_strain': 1.067e-23,                          # paper sec 3
            'snr_observed': 12.9,
            'snr_uqff': 3.6,
            'A_scm_scenarios': scenarios,
            'p_ns': 0.49,                                        # paper sec 5
            'p_bh': 0.51,
            'bh_factor': 0.6217,
            'ns_factor_mean': 0.5836,
            'chirp_mass_msun': 1.44,                             # LIGO anchor
            'm1_msun': 2.52,                                     # mass-gap component
            'm2_msun': 1.12,
            'total_mass_msun': 3.64,
            'distance_mpc': 159.0,
        },
        'formula': ('F = A_aether*A_SCm(B)*A_TRZ*A_string; '
                    'A_SCm(B) = exp[-(B/B_crit)^2]'),
        'source': 'PAPER_002',
        'residual_pct': None,          # pending Q-001 ruling
        'status': 'OPEN_RULING',
    }


@_register('PAPER_003')
def _paper_003(dataset):
    """GW150914 UQFF vs LIGO Strain Comparison (Session 0).

    First BBH detection. Same universal 0.333 chain as PAPER_001 (no magnetic
    suppression for BBH). New observables: 3x apparent-distance bias (direct
    Hubble-inference impact) and propagation phase lag.
    OPEN_RULING Q-004: stated phase-lag formula kappa*D*f*SSq evaluates to
    17.53 with the given numbers, not the paper's 0.126 rad.
    """
    D_aether = 1.0
    D_scm = 1.0                        # BBH: no B-field, no SCm suppression
    D_trz = 1.0 - F_TRZ                # 0.9 EXACT
    D_string = 0.37
    D_total = D_aether * D_scm * D_trz * D_string       # 0.333 universal BBH
    h_gr_peak = 1.2499e-21             # semi-analytic GR peak (paper sec 3.1)
    d_true_mpc = 410.0                 # LIGO anchor
    return {
        'value': {
            'D_total': D_total,
            'h_gr_peak': h_gr_peak,
            'h_uqff_peak': D_total * h_gr_peak,          # 4.1622e-22
            'snr_gr': 24.0,
            'snr_uqff': D_total * 24.0,                  # 8.0
            'distance_true_mpc': d_true_mpc,
            'distance_apparent_mpc': d_true_mpc / D_total,   # 1231 Mpc
            'distance_bias_factor': 1.0 / D_total,           # 3.0x
            'phase_lag_rad': 0.126,                      # paper-stated (Q-004)
            'ripple_amplitude_pct': 1.0,                 # paper sec 4
            'm1_msun': 36.0,                             # LIGO anchor
            'm2_msun': 29.0,
            'total_mass_msun': 65.0,
            'chirp_mass_msun': 28.3,
        },
        'formula': ('D_total = 1*1*(1-F_TRZ)*0.37 (universal BBH); '
                    'D_apparent = D_true/D_total; phase lag kappa*D*f*SSq (Q-004)'),
        'source': 'PAPER_003',
        'residual_pct': abs(D_total - (1.0 - D_GW_EROSION)) / (1.0 - D_GW_EROSION) * 100.0,
        'status': 'OPEN_RULING',
    }


@_register('PAPER_004')
def _paper_004(dataset):
    """GW170817 BNS Chirp Phase Evolution — GR vs UQFF (Session 0).

    35-300 Hz chirp window (0.2 s, 200 samples). The paper's own formula
    explicitly writes h_UQFF = D_aether*D_SCm*(1-f_TRZ)*D_string*h_GR —
    corpus-internal confirmation of the (1-F_TRZ) primitive composition.
    Q-005: paper's stated h_UQFF,peak 9.4332e-23 differs ~1% from
    0.333*2.8051e-22 = 9.341e-23 (arithmetic slip).
    """
    D_total = 1.0 * 1.0 * (1.0 - F_TRZ) * 0.37       # 0.333 (paper's own form)
    h_gr_peak = 2.8051e-22            # PN chirp formula at ~300 Hz (paper sec 2)
    h_obs = 1.0e-22                   # LIGO observed strain anchor
    return {
        'value': {
            'D_total': D_total,
            'h_gr_peak': h_gr_peak,
            'h_uqff_peak_computed': D_total * h_gr_peak,     # 9.341e-23
            'h_uqff_peak_paper': 9.4332e-23,                 # stated (Q-005)
            'strain_reduction_pct': (1.0 - D_total) * 100.0, # 66.7 (paper says 66.4)
            'gr_residual_vs_obs_pct': 5.0,                   # paper sec 2
            'uqff_mismatch_vs_obs_pct': 66.7,                # paper sec 4
            'chirp_mass_msun': 1.188,
            'distance_mpc': 40.0,
            'freq_range_hz': (35.0, 300.0),
            'chirp_duration_s': 0.2,
            'n_samples': 200,
        },
        'formula': ('h_UQFF = D_aether*D_SCm*(1-f_TRZ)*D_string*h_GR '
                    '(paper sec 3 — explicit (1-f_TRZ) composition)'),
        'source': 'PAPER_004',
        'residual_pct': abs(D_total * h_gr_peak - 9.4332e-23) / 9.4332e-23 * 100.0,
        'status': 'OPEN_RULING',
    }


@_register('PAPER_005')
def _paper_005(dataset):
    """BH Merger Energy Retention (Session 0). GW150914-like BBH 36+29 Msun.

    BBH chain variant: string DEACTIVATED (1.0), B-factor 0.9, TRZ 0.9 →
    combined 0.81 = (1-F_TRZ)^2 primitive composition. Power/energy/timescale
    all consistently scale by 0.81 (P ratio 0.8100, tau ratio 1/0.81 = 1.2346,
    E ratio 0.810). Q-006: sec 2 states F_combined = 0.903 with P = F^2*P_GR
    (0.815), inconsistent with the 0.81 used throughout.
    """
    F_combined = (1.0 - F_TRZ) ** 2       # 0.81 EXACT — B-factor * TRZ
    P_gw_gr = 8.9451e-11                  # W, paper sec 2
    tau_gr_yr = 9.4417e11
    E_rad_gr_msun = 0.8031
    M_tot = 65.0
    return {
        'value': {
            'F_combined': F_combined,                        # 0.81
            'P_gw_gr_w': P_gw_gr,
            'P_gw_uqff_w': F_combined * P_gw_gr,             # 7.2455e-11
            'power_reduction_pct': (1.0 - F_combined) * 100, # 19.0
            'tau_gr_yr': tau_gr_yr,
            'tau_uqff_yr': tau_gr_yr / F_combined,           # 1.1656e12
            'tau_extension_factor': 1.0 / F_combined,        # 1.2346
            'E_rad_gr_msun': E_rad_gr_msun,
            'E_rad_uqff_msun': F_combined * E_rad_gr_msun,   # 0.6505
            'remnant_gr_msun': M_tot - E_rad_gr_msun,        # 64.197
            'remnant_uqff_msun': M_tot - F_combined * E_rad_gr_msun,  # 64.350
            'mass_retention_uqff_pct': (M_tot - F_combined * E_rad_gr_msun) / M_tot * 100,
            'm1_msun': 36.0, 'm2_msun': 29.0, 'distance_mpc': 410.0,
        },
        'formula': ('F_combined = (1-F_TRZ)^2 = 0.81 (string deactivated for BBH); '
                    'P/tau/E all scale by 0.81 (Q-006: sec-2 states 0.903)'),
        'source': 'PAPER_005',
        'residual_pct': abs(F_combined * P_gw_gr - 7.2455e-11) / 7.2455e-11 * 100.0,
        'status': 'OPEN_RULING',
    }


@_register('PAPER_006')
def _paper_006(dataset):
    """Multi-Messenger GW170817 — Kilonova + UQFF Predictions (Session 0).

    Full-inspiral simulation (3,677 cycles, 23-300 Hz, 100 s) + per-messenger
    UQFF predictions. Consistent with PAPER_001's chain (no new
    inconsistencies): amplitude-only modification, GW speed preserved,
    EM sector unmodified. Detection volume shrinks by 1/D_total^3 ~ 27x.
    """
    D_total = 1.0 * 1.0 * (1.0 - F_TRZ) * 0.37       # 0.333 (same as PAPER_001)
    h_gr = 5.4176e-22
    return {
        'value': {
            'D_total': D_total,
            'h_uqff_strain': D_total * h_gr,             # 1.8041e-22
            'snr_gr': 32.4,
            'snr_uqff': D_total * 32.4,                  # 10.8
            'gw_speed_constraint': 3e-15,                # |dc/c| preserved by UQFF
            'grb_delay_s': 1.74,                         # unmodified by UQFF
            'kilonova_ejecta_msun': (0.04, 0.05),        # unmodified by UQFF
            'total_cycles': 3677,                        # full inspiral sim
            'max_phase_lag_rad': 2310.8,                 # 367.8 cycles
            'max_phase_lag_cycles': 367.8,
            'detection_volume_shrink': 1.0 / D_total**3, # ~27x
            'B_ns_t': 1.0e4,
            'chirp_mass_msun': 1.188,
            'distance_mpc': 40.0,
        },
        'formula': ('h_UQFF = D_total*h_GR (amplitude-only; c_GW = c preserved); '
                    'V_detect scales 1/D_total^3 ~ 27x shrink'),
        'source': 'PAPER_006',
        'residual_pct': abs(D_total - (1.0 - D_GW_EROSION)) / (1.0 - D_GW_EROSION) * 100.0,
    }


@_register('PAPER_007')
def _paper_007(dataset):
    """Tidal Deformability Constraints from BNS Mergers (Session 143).

    Lambda = (2/3)*k2*(R/M)^5; UQFF adds B-field suppression
    f_SCm(B) = 1 - exp[-(B_crit/B)]: f->1 for B<<B_crit (no suppression),
    f->0 for B>>B_crit (full suppression). NS/BH discriminator at the
    GW190425 mass gap: Lambda_NS(2.52 Msun) ~ 16 vs Lambda_BH = 0.
    Q-007: paper text carries mojibake-garbled exponents (B regimes,
    B_crit unit) — values wired from context-consistent readings.
    """
    import math as _m
    B_crit = 4.4e13                   # B_crit anchor (unit T vs G — Q-002/Q-007)

    def f_scm(B):
        return 1.0 - _m.exp(-(B_crit / B))

    k2 = 0.09                         # typical NS Love number (reproduces Lambda~400)
    C = 0.172                         # compactness GM/(Rc^2) for M=1.4 Msun, R=12 km
    Lambda_typical = (2.0 / 3.0) * k2 * (1.0 / C) ** 5
    return {
        'value': {
            'Lambda_gw170817_range': (190.0, 600.0),     # LIGO 90% credible
            'Lambda_1p4_upper': 800.0,                   # LIGO constraint
            'Lambda_typical_NS': Lambda_typical,         # ~400 at C=0.17
            'Lambda_ns_massgap_2p52': 16.0,              # paper: NS/BH discriminator
            'Lambda_bh': 0.0,                            # BH has zero tidal deformability
            'f_scm_normal_pulsar': f_scm(1.0e4),         # B=1e8 G = 1e4 T -> ~1.0
            'f_scm_at_bcrit': f_scm(B_crit),             # 1-exp(-1) = 0.632
            'compactness_typical': C,
            'k2_typical': k2,
            'm1_msun': 1.46, 'm2_msun': 1.27,            # GW170817 posteriors
        },
        'formula': ('Lambda = (2/3)*k2*(R/M)^5; lambda_UQFF = lambda_GR*f_SCm(B); '
                    'f_SCm(B) = 1 - exp[-(B_crit/B)]'),
        'source': 'PAPER_007',
        'residual_pct': abs(Lambda_typical - 400.0) / 400.0 * 100.0,
        'status': 'OPEN_RULING',
    }


@_register('PAPER_008')
def _paper_008(dataset):
    """UQFF Waveform Phase Evolution and Template Mismatch (Session 143).

    Power scales as D_total^2 here: P_UQFF = D^2 * P_GR, giving inspiral
    extension tau_UQFF = tau_GR / D^2 = 9.0x and phase-lag growth
    dphi ~ (1/D^2 - 1) * phi_GR ~ 8x. Full 100 s GW170817 inspiral:
    dphi = 2310.8 rad = 367.8 cycles (consistent with PAPER_006).
    Q-008: power convention differs from PAPER_005 (P scaled by F linearly
    there, by D^2 here; tau by 1/F vs 1/D^2).
    """
    D_total = (1.0 - F_TRZ) * 0.37        # 0.333 BNS chain
    D_sq = D_total ** 2                    # 0.111
    return {
        'value': {
            'D_total': D_total,
            'D_total_squared': D_sq,                       # 0.111
            'tau_extension_factor': 1.0 / D_sq,            # 9.02x
            'phase_lag_growth_factor': 1.0 / D_sq - 1.0,   # 8.02x phi_GR
            'phase_lag_full_rad': 2310.8,                  # 100s inspiral anchor
            'phase_lag_full_cycles': 367.8,
            'mismatch': 1.0 - D_total,                     # 0.667
            'snr_uqff': D_total * 32.4,                    # 10.8
            'D_bbh_reference': (1.0 - F_TRZ) ** 2,         # 0.81 (PAPER_005 x-ref)
            'template_phase_sensitivity': '1% phase error at merger -> 50% SNR loss',
        },
        'formula': ('P_UQFF = D_total^2*P_GR; tau_UQFF = tau_GR/D^2 = 9x; '
                    'dphi ~ 8*phi_GR (Q-008: power convention vs PAPER_005)'),
        'source': 'PAPER_008',
        'residual_pct': abs(1.0 / D_sq - 9.0) / 9.0 * 100.0,   # 9.018 vs paper "9.0"
        'status': 'OPEN_RULING',
    }


@_register('PAPER_009')
def _paper_009(dataset):
    """Damping Mechanism Decomposition (Session 143) — the 4-mechanism synthesis.

    D_total = D_Aether * D_SCm * D_TRZ * D_String per-system:
      GW170817 BNS 0.333 (String 0.37 primary), GW190425 BNS 0.530
      (String 0.62 — SELF-RECTIFIES Q-001: heavier BNS has reduced string
      coupling), GW150914 BBH 0.81 (TRZ only; string deactivated).
    D_Aether = exp(-kappa*r/c) ~ 1 for all observed events (significant only
    beyond observable universe). D_SCm = 1 - exp[-(B_crit/B)] (same form as
    PAPER_007; differs from PAPER_002's Gaussian — feeds Q-002/Q-007).
    Q-009: aether-scale r = c/kappa stated as 17 Gpc does not reproduce
    from kappa = 5e-4/day without an unstated unit convention.
    """
    systems = {
        'gw170817_bns': (1.0 - F_TRZ) * 0.37,          # 0.333
        'gw190425_bns': 0.530,                          # paper: string 0.62 variant
        'gw150914_bbh': (1.0 - F_TRZ) ** 2,             # 0.81 (TRZ+B-factor, PAPER_005)
    }
    return {
        'value': {
            'D_total_by_system': systems,
            'bns_bbh_damping_ratio': systems['gw150914_bbh'] / systems['gw170817_bns'],  # 2.43
            'string_factor_gw170817': 0.37,
            'string_factor_gw190425': 0.62,             # heavier-BNS reduced coupling
            'd_trz': 1.0 - F_TRZ,                       # 0.9 EXACT
            'd_aether_410mpc_paper': 0.999999,          # paper table anchor (Q-009:
            'kappa_r_over_c_410mpc_paper': 2.4e-8,      #  SI evaluation gives exp(-2.4e8)
                                                        #  ~ 0 — formula irreproducible)
            'trz_resonance_hz': 100.0,                  # paper sec 1.3
            'string_dominance_above_hz': 200.0,
            'scm_activation_threshold_note': 'sharp at B ~ 3-5e14 G (mojibake exponents)',
        },
        'formula': ('D_total = exp(-kappa*r/c) * [1-exp(-(B_crit/B))] * (1-F_TRZ) * D_string; '
                    'per-system String: BNS-light 0.37, BNS-heavy 0.62, BBH deactivated'),
        'source': 'PAPER_009',
        'residual_pct': abs(systems['gw150914_bbh'] / systems['gw170817_bns'] - 2.4) / 2.4 * 100.0,
        'status': 'OPEN_RULING',
    }


@_register('PAPER_010')
def _paper_010(dataset):
    """Post-Merger Oscillations and Remnant Mass (Session 0).

    QNM modifications for the BNS remnant:
      f_UQFF = f_GR*(1 + alpha_Q - beta_damp) ~ 0.95*f_GR (5% downshift;
        2.5 kHz -> 2.375 kHz, 125 Hz shift detectable at 3G sensitivity)
      tau_UQFF = tau_GR/(1 + gamma_damp) ~ 0.71*tau_GR (29% faster decay;
        10 ms -> ~7 ms) with gamma_damp ~ 0.4 at 2.5 kHz
      E_rad_UQFF = E_rad_GR*(1 + eps_damp), eps_damp ~ 0.15 (15% extra
        quantum-channel dissipation) -> lighter remnant
    Note: eps_damp INCREASES radiated energy here while PAPER_005 DECREASES
    it for BBH — different mechanisms (QNM ringdown vs inspiral), not
    contradiction; ranges are paper-stated envelopes.
    """
    f_gr_hz = 2.5e3                    # typical BNS post-merger peak
    tau_gr_ms = 10.0
    gamma_damp = 0.4                   # at ~2.5 kHz
    eps_damp = 0.15
    m1, m2 = 1.4, 1.4                  # comparison case
    e_rad_gr_msun = 0.05               # typical GR radiated (comparison case)
    return {
        'value': {
            'f_uqff_over_f_gr': 0.95,
            'f_gr_hz': f_gr_hz,
            'f_uqff_hz': 0.95 * f_gr_hz,               # 2375 Hz
            'freq_shift_hz': 0.05 * f_gr_hz,           # 125 Hz
            'tau_ratio': 1.0 / (1.0 + gamma_damp),     # 0.714
            'tau_gr_ms': tau_gr_ms,
            'tau_uqff_ms': tau_gr_ms / (1.0 + gamma_damp),   # 7.14 ms
            'eps_damp': eps_damp,
            'e_rad_uqff_msun': e_rad_gr_msun * (1.0 + eps_damp),
            'remnant_uqff_msun': m1 + m2 - e_rad_gr_msun * (1.0 + eps_damp),
            'alpha_q_range': (0.02, 0.05),
            'beta_damp_range': (0.03, 0.08),
        },
        'formula': ('f_UQFF = 0.95*f_GR; tau_UQFF = tau_GR/(1+0.4) = 0.71*tau_GR; '
                    'E_rad_UQFF = (1+0.15)*E_rad_GR'),
        'source': 'PAPER_010',
        'residual_pct': abs(1.0 / 1.4 - 0.71) / 0.71 * 100.0,   # 0.60% (0.714 vs stated 0.71)
    }


@_register('PAPER_011')
def _paper_011(dataset):
    """Stochastic GW Background in UQFF (Session 0).

    Omega_GW,UQFF = D_total^2 * Omega_GW,GR (energy ~ h^2 — CORROBORATES
    Q-008's D^2 convention, second corpus data point). Per-population:
    BNS 0.111 (89% cut), BBH 0.81^2 ~ 0.66 (34% cut). Mixed population
    (50/40/10 BNS/BBH/NSBH): Omega_UQFF ~ 0.37*Omega_GR (63% reduction).
    Detection delayed 2028 -> 2032-2035; LISA slope discriminates.
    """
    D_bns = (1.0 - F_TRZ) * 0.37                  # 0.333
    D_bbh = (1.0 - F_TRZ) ** 2                     # 0.81
    omega_gr_100hz = 1.0e-9                        # GR anchor at 100 Hz
    f_bns, f_bbh, f_nsbh = 0.5, 0.4, 0.1           # population fractions
    nsbh_factor = 0.5                              # paper-stated NSBH suppression
    omega_mix = f_bns * D_bns**2 + f_bbh * D_bbh**2 + f_nsbh * nsbh_factor
    return {
        'value': {
            'omega_suppression_bns': D_bns**2,             # 0.111
            'omega_suppression_bbh': D_bbh**2,             # 0.656
            'omega_gw_gr_100hz': omega_gr_100hz,
            'omega_gw_uqff_bns_100hz': D_bns**2 * omega_gr_100hz,   # 1.11e-10
            'omega_mixed_population_factor': omega_mix,    # ~0.37
            'sgwb_reduction_pct': (1.0 - omega_mix) * 100, # ~63
            'detection_delay': '2028 (GR) -> 2032-2035 (UQFF)',
            'trz_dip_at_hz': 100.0,
            'population_fractions': (f_bns, f_bbh, f_nsbh),
        },
        'formula': ('Omega_UQFF = D_total^2 * Omega_GR (energy ~ h^2, corroborates '
                    'Q-008 D^2 convention); mixed 0.5*0.111 + 0.4*0.656 + 0.1*0.5 ~ 0.37'),
        'source': 'PAPER_011',
        'residual_pct': abs(omega_mix - 0.37) / 0.37 * 100.0,
    }


@_register('PAPER_012')
def _paper_012(dataset):
    """Eccentric Binary Circularization (Session 143).

    Modified Peters equation: de/dt|UQFF = D_total^2 * de/dt|GR, so
    tau_circ extends by 1/D^2 = 9.0x — THIRD corpus data point for the
    Q-008 D^2 convention (with PAPER_008, PAPER_011). Residual
    eccentricity at LIGO band: e_f = 0.003 (vs GR < 1e-4, 30x higher),
    producing 2f/3f/4f harmonic structure with relative amplitude ~ e.
    Rate enhancement ~3x for detectable eccentric mergers.
    """
    D_bns = (1.0 - F_TRZ) * 0.37                   # 0.333
    tau_extension = 1.0 / D_bns**2                  # 9.02x
    return {
        'value': {
            'tau_circ_extension': tau_extension,           # 9.0x
            'e_final_uqff_at_10hz': 0.003,                 # paper sec 3.2
            'e_final_gr_at_10hz': 1e-4,                    # GR upper bound
            'eccentricity_enhancement': 30.0,              # 0.003/1e-4
            'rate_enhancement_eccentric': 3.0,             # paper sec 4
            'harmonic_amplitude_ratio': 0.003,             # ~ e at 2f/3f/4f
            'e0_reference': 0.01,
        },
        'formula': ('de/dt|UQFF = D_total^2 * de/dt|GR (modified Peters); '
                    'tau_circ = 9.0x tau_GR — 3rd D^2 data point (Q-008)'),
        'source': 'PAPER_012',
        'residual_pct': abs(tau_extension - 9.0) / 9.0 * 100.0,
    }


@_register('PAPER_013')
def _paper_013(dataset):
    """Magnetar Spin-Down in UQFF (Session 143) — the kappa calibration paper.

    SCm suppression of magnetic dipole radiation: D_SCm(B) = 1-exp[-(B_crit/B)]
    (threshold form; reproduces SGR 1806-20 D_SCm ~ 0.01-0.02 only with both
    fields in GAUSS — Q-010 extends the B_crit unit family Q-002/007/009).
    Edot_UQFF = D_SCm^2 * Edot_GR = 1e-4 (FOURTH D^2 corpus data point).
    Braking index n_UQFF = 1.5-2.0 vs GR n=3; observed magnetars n ~ 1-2.5 —
    UQFF resolves the magnetar age problem.
    Q-010: abstract says t_sd = 3*t_GR but sec 2.3 says t = t_GR/D^2 = 10,000x.
    """
    import math as _m
    B_crit_G = 4.4e13                  # Gauss reading (Q-010)
    B_sgr1806_G = 2.0e15               # SGR 1806-20 surface field

    D_scm = 1.0 - _m.exp(-(B_crit_G / B_sgr1806_G))   # 0.0218 (paper states ~0.01)
    return {
        'value': {
            'D_scm_sgr1806': D_scm,                       # 0.0218 computed
            'D_scm_paper_stated': 0.01,
            'edot_suppression': D_scm**2,                  # ~4.7e-4 (paper: 1e-4 from D=0.01)
            'braking_index_uqff_range': (1.5, 2.0),
            'braking_index_gr': 3.0,
            'braking_index_observed_range': (1.0, 2.5),
            'tau_ratio_abstract': 3.0,                     # Q-010 conflict
            'tau_ratio_sec23': 1.0e4,                      # t_GR/D^2 with D=0.01
            'magnetar_age_resolution_yr': 1.0e7,
            'sgr1806_period_s': 7.5,
            'n_known_magnetars': 23,
        },
        'formula': ('D_SCm(B) = 1-exp[-(B_crit/B)]; Edot_UQFF = D_SCm^2*Edot_GR '
                    '(4th D^2 data point); n_UQFF = 2 - dlnD/dlnOmega ~ 1.5-2.0'),
        'source': 'PAPER_013',
        'residual_pct': abs(D_scm - 0.01) / 0.01 * 100.0,   # 118% vs paper ~0.01 (Q-010)
        'status': 'OPEN_RULING',
    }
