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

VERSION = "0.4.0"

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
