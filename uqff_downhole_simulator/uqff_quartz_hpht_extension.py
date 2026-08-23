"""uqff_quartz_hpht_extension — the physics layer of the UQFF Downhole Simulator.

Ported to the star-magic-program repo from the 22Aug2026 Grok thread template
(grok_cce7a73b, watermarked source; see README.md provenance) on Daniel's GO
(2026-08-22) with the KNOB RULING applied:

  * The CANONICAL primitives enter the UQFF suppression composition at their
    LOCKED values via the live `uqff_calculator` module (K_MEX = 25/12,
    Phi_res = 0.84, F_TRZ = 0.1, U_i = 2.75e-7 via u_i_canonical_646).
  * The template's adjustable "K_MEX"/"Phi_res" sliders (0.95-1.35 / 0.80-0.98)
    are RENAMED to honest engineering-trim factors: `k_structural_trim` and
    `phi_coupling_trim` (default 1.0) — instrument-tuning gains, NOT primitives.

Classification (PAPER_2149 Hybrid-Form doctrine): DERIVED_HYBRID — an
industry-observed quartz baseline dressed by a UQFF suppression composition.
Industry anchors carry inline source comments per the charter's anchor rule.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# UQFF binding (current API), with graceful fallback per the template design
# ---------------------------------------------------------------------------
UQFF_AVAILABLE = False
_K_MEX = 25.0 / 12.0        # canonical fallback (PAPER_1522)
_PHI_RES = 0.84             # canonical fallback (resonance variant, PAPER_2134/2159)
_F_TRZ = 0.1                # canonical fallback (PAPER_1160)
_U_I = 2.75e-7              # canonical fallback (PAPER_646)

try:
    import uqff_calculator as _u
    UQFF_AVAILABLE = True
except ImportError:  # running outside the repo without the package installed
    import os as _os
    import sys as _sys
    _parent = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
    if _parent not in _sys.path:
        _sys.path.insert(0, _parent)
    try:
        import uqff_calculator as _u
        UQFF_AVAILABLE = True
    except ImportError:
        _u = None

if UQFF_AVAILABLE:
    _K_MEX = float(_u.K_MEX)                    # 25/12 EXACT
    _PHI_RES = float(_u.PHI_RES_RESONANCE)      # 0.84
    _F_TRZ = float(_u.F_TRZ)                    # 1/10 EXACT
    try:
        _U_I = float(_u.u_i_canonical_646())    # 2.75e-7 (PAPER_646, live)
    except Exception:
        pass


def canonical_suppression(k_structural_trim: float = 1.0,
                          phi_coupling_trim: float = 1.0) -> float:
    """The UQFF drift-suppression composition, canonical primitives locked.

    Template lineage (22Aug2026 thread): suppression = vacuum * structural *
    resonance. The three dressings' coefficients are the template's engineering
    fit (DERIVED_HYBRID); the primitive INPUTS are canonical and immutable.
    Trims are external instrument gains, applied multiplicatively and
    disclosed as such.
    """
    vacuum_stab = 0.58 + 0.32 * (1.0 - _F_TRZ)          # rho_SCm/rho_UA = F_TRZ (canonical)
    structural = 0.52 + 0.38 * _K_MEX                   # K_MEX = 25/12 (canonical)
    resonance = 0.68 + 0.27 * _PHI_RES                  # Phi_res = 0.84 (canonical)
    return vacuum_stab * structural * resonance * float(k_structural_trim) * float(phi_coupling_trim)


def calculate_quartz_transducer_hpht_UQFF(depth_m: float,
                                          temp_c: float,
                                          pressure_psi: float,
                                          k_structural_trim: float = 1.0,
                                          phi_coupling_trim: float = 1.0) -> dict:
    """Physics-informed quartz HPHT drift model (UQFF-stabilized).

    Returns the template's rich dictionary shape, current-API values.
    Anchors (inline, per charter): 0.215 %FS/yr typical good-quartz baseline
    (industry spec class); 150 C thermal knee / 15,000 psi pressure knee with
    exponents 1.15 / 0.9 (template engineering fit); clip band 0.035-0.48 %FS/yr
    (physical plausibility bounds, template).
    """
    thermal_stress = max(0.0, (temp_c - 150.0) / 80.0) ** 1.15        # anchor: 150 C knee (industry)
    pressure_stress = max(0.0, (pressure_psi - 15000.0) / 5000.0) ** 0.9  # anchor: 15 kpsi knee (industry)

    suppression = canonical_suppression(k_structural_trim, phi_coupling_trim)

    base_drift = 0.215   # anchor: %FS/yr typical good-quartz baseline (industry)
    drift = base_drift * (1.0 + 0.55 * thermal_stress + 0.35 * pressure_stress) / suppression
    drift = min(max(drift, 0.035), 0.48)   # clip band (template plausibility bounds)

    expected_temp_c = 15.0 + (depth_m / 1000.0) * 29.5   # anchor: ~29.5 C/km geothermal gradient
    hydrostatic_psi = depth_m * 3.28084 * 0.465          # anchor: 0.465 psi/ft gradient

    return {
        "value": {
            "drift_pct": round(drift, 4),
            "stability_factor": round(base_drift / drift, 3),
            "suppression": round(suppression, 4),
            "rho_SCm_over_rho_UA": _F_TRZ,
            "U_i": _U_I,
            "K_MEX_canonical": _K_MEX,
            "Phi_res_canonical": _PHI_RES,
            "k_structural_trim": float(k_structural_trim),
            "phi_coupling_trim": float(phi_coupling_trim),
            "expected_temp_c": round(expected_temp_c, 1),
            "hydrostatic_psi": round(hydrostatic_psi, 0),
            "uqff_live": UQFF_AVAILABLE,
        },
        "classification": "DERIVED_HYBRID (PAPER_2149): industry baseline x canonical-UQFF suppression",
        "notes": "star-magic-program port of the 22Aug2026 QCALCGEOM template; knob ruling applied",
    }


def conventional_drift(temp_c: float, pressure_psi: float) -> float:
    """Conventional-gauge drift: SAME industry baseline and stress dressing,
    NO UQFF suppression (suppression = 1). The comparison-mode reference leg.
    """
    thermal_stress = max(0.0, (temp_c - 150.0) / 80.0) ** 1.15
    pressure_stress = max(0.0, (pressure_psi - 15000.0) / 5000.0) ** 0.9
    base_drift = 0.215   # anchor: same industry baseline as the UQFF leg
    drift = base_drift * (1.0 + 0.55 * thermal_stress + 0.35 * pressure_stress)
    return min(max(drift, 0.035), 0.48)


def drift_comparison(depth_m: float, temp_c: float, pressure_psi: float,
                     k_structural_trim: float = 1.0,
                     phi_coupling_trim: float = 1.0) -> dict:
    """Twin-gauge comparison at matched T/P: UQFF-stabilized vs conventional.

    The module's substantive testable claim (PAPER_2256 sec 5): away from the
    clip band, the conventional/UQFF drift ratio EQUALS the suppression
    composition — 1.0324 at unity trims. This function is the simulation side
    of the quartz bench test (PAPER_2250 LABORATORY tier).
    """
    uq = calculate_quartz_transducer_hpht_UQFF(
        depth_m, temp_c, pressure_psi, k_structural_trim, phi_coupling_trim)
    conv = conventional_drift(temp_c, pressure_psi)
    uqd = uq["value"]["drift_pct"]
    sup = uq["value"]["suppression"]
    return {
        "uqff_drift_pct": uqd,
        "conventional_drift_pct": round(conv, 4),
        "measured_ratio": round(conv / uqd, 4) if uqd > 0 else None,
        "predicted_ratio_suppression": sup,
        "clip_active": bool(conv >= 0.48 or uqd <= 0.035),
        "note": "measured_ratio == suppression exactly when neither leg clips",
    }
