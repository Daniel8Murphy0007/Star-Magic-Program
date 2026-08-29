"""uqff_inverse_engine - Part 3 of the subsurface surveying tool: THE
INVERSE ENGINE (measurement -> strata, with uncertainty).

v1.77.0. The direction the whole mission points: read the ground. This first
inverse composes the two layers already built and validated:

    measured borehole gravity            (the catalogue's own archives)
        -> implied density column        (K2 forward model inverted;
                                          UQFF constants g_U, G_U, R_U)
        -> posterior strata properties   (strata-join conditional priors:
                                          the library's OWN joint
                                          distributions, P(Vp | rho), ...)
        -> layer-boundary candidates     (density-step detector, disclosed
                                          threshold)

EVERY estimate carries its full chain: which constants, which prior well,
how many co-located bins support it, whether the query extrapolates beyond
the prior's observed range, and the CROSS-SITE TRANSFER assumption stated
in words (a prior learned in oceanic basalt applied to continental gneiss
is an assumption, not a fact - the engine says so on every estimate).

WHAT THIS ENGINE REFUSES TO DO
    - It never averages archives into a 'truth'.
    - It never returns an estimate without n, spread, and support.
    - It never hides that today's priors come from ONE well family; the
      posterior is exactly as provincial as the library, no more.

FALSIFIABILITY
    Run on the KTB gravity column with the 504B prior, the engine PREDICTS
    the KTB sonic column (Vp vs depth) - a log that exists in the GFZ
    archives but is NOT yet in this catalogue. Ingesting it tests the
    entire chain end-to-end. The prediction is emitted, labeled
    PREDICTION_AWAITING_DATA, and pinned; it can be wrong, which is the
    point.
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .uqff_forward_model import implied_density_gcc
from .uqff_profile_catalog import CATALOG
from . import uqff_strata_join as SJ

CROSS_SITE_NOTE = ("cross-site transfer: prior learned at '%s' applied at "
                   "'%s' - an assumption the engine discloses, not a fact")


@dataclass
class StrataEstimate:
    """One inverted interval: what the ground implies, and how sure."""
    depth_m: float
    dz_m: float
    implied_density_gcc: float
    posteriors: Dict[str, Dict] = field(default_factory=dict)
    chain: Dict[str, str] = field(default_factory=dict)


def detect_boundaries(depths: List[float], implied_rho: List[float],
                      k_sigma: float = 2.0) -> List[Dict]:
    """Layer-boundary candidates: consecutive implied-density changes
    exceeding k_sigma population sigmas (threshold disclosed in each hit).
    Candidates, not verdicts - amplitude and depth reported, nothing
    smoothed away."""
    if len(implied_rho) < 3:
        return []
    steps = [implied_rho[i] - implied_rho[i - 1] for i in range(1, len(implied_rho))]
    sd = statistics.pstdev(steps)
    if sd == 0.0:
        return []
    return [{'depth_m': depths[i + 1], 'delta_rho_gcc': steps[i],
             'n_sigma': abs(steps[i]) / sd, 'threshold_sigma': k_sigma}
            for i in range(len(steps)) if abs(steps[i]) > k_sigma * sd]


def invert_gravity_column(entry: str = 'ktb_hb_bhgm_density',
                          prior_well: str = '504b',
                          targets: tuple = ('vp', 'porosity'),
                          rho_null_gcc: float = 0.5,
                          k_sigma: float = 2.0) -> Dict:
    """The first full inversion: a measured gravity column becomes a strata
    column with uncertainty. Null stations (archive density zeros) excluded
    with the count disclosed; every posterior carries n/spread/support and
    the extrapolation flag from the prior itself."""
    st = CATALOG[entry].stream()
    z = [float(v) for v in st.index]
    grav = [float(v) for v in st.channels['GRAV'].values]
    rho_tool = [float(v) for v in st.channels['RHO'].values]
    estimates: List[StrataEstimate] = []
    excluded = 0
    for i in range(1, len(z)):
        dz = z[i] - z[i - 1]
        if dz <= 0:
            continue
        if rho_tool[i] <= rho_null_gcc or rho_tool[i - 1] <= rho_null_gcc:
            excluded += 1
            continue
        rho_imp = implied_density_gcc(grav[i] - grav[i - 1], dz)
        est = StrataEstimate(
            depth_m=z[i], dz_m=dz, implied_density_gcc=rho_imp,
            chain={
                'measurement': '%s GRAV interstation (mGal)' % entry,
                'density_inversion': 'K2 UQFF constants (uqff_forward_model)',
                'prior': 'uqff_strata_join joint table, well %s' % prior_well,
                'assumption': CROSS_SITE_NOTE % (prior_well, entry),
            })
        for t in targets:
            given = ('wet_bulk_density'
                     if 'wet_bulk_density' in SJ.WELL_GROUPS[prior_well][1] else None)
            if given is None or t not in SJ.WELL_GROUPS[prior_well][1]:
                est.posteriors[t] = {'status': 'NO_PRIOR_CHANNEL'}
                continue
            est.posteriors[t] = SJ.conditional(prior_well, t, given, rho_imp)
        estimates.append(est)

    depths = [e.depth_m for e in estimates]
    rhos = [e.implied_density_gcc for e in estimates]
    boundaries = detect_boundaries(depths, rhos, k_sigma)
    ok_vp = [e for e in estimates
             if e.posteriors.get('vp', {}).get('status') == 'OK']
    in_support = [e for e in ok_vp if not e.posteriors['vp']['extrapolation']]
    prediction = None
    if in_support:
        vps = [e.posteriors['vp']['estimate'] for e in in_support]
        prediction = {
            'status': 'PREDICTION_AWAITING_DATA',
            'predicted_property': 'Vp (m/s) column at %s' % entry,
            'n_intervals_in_prior_support': len(in_support),
            'vp_range_m_s': (min(vps), max(vps)),
            'vp_mean_m_s': statistics.mean(vps),
            'test': ('ingest the %s sonic log (exists in the source archive, '
                     'not yet catalogued) and score these estimates - the '
                     'chain is falsified if the measured column leaves the '
                     'posterior spreads' % entry),
        }
    return {
        'entry': entry, 'prior_well': prior_well,
        'n_intervals': len(estimates), 'null_intervals_excluded': excluded,
        'n_posterior_ok': len(ok_vp), 'n_in_prior_support': len(in_support),
        'boundary_candidates': boundaries,
        'falsifiable_prediction': prediction,
        'estimates': estimates,
    }
