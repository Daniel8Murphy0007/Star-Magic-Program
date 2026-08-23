"""uqff_downhole_simulator — the UQFF Downhole HPHT Quartz-Gauge Simulator.

The star-magic-program's first packaged industry-application module: a
deep-well (TD ~20,300 ft) six-gauge quartz P/T string with UQFF-stabilized
drift, transient events, live animation (matplotlib / optional PyQt6), and
CSV export.

Provenance: ported 2026-08-22 (Daniel GO) from the 22Aug2026 Grok thread
template (grok_cce7a73b); canonical primitives locked, template tuning knobs
renamed to engineering trims per the knob ruling. See README.md and
PAPER_2256.

Quick use (headless):
    from uqff_downhole_simulator import UQFFDownholeEngine, SimulatorConfig
    e = UQFFDownholeEngine()
    for _ in range(100): e.step()
    print(e.summary()); e.export_csv("run.csv")

Demos (need a display):
    python -m uqff_downhole_simulator.matplotlib_demo
    python -m uqff_downhole_simulator.qt6_downhole_app   (pip install PyQt6)
"""

from .uqff_quartz_hpht_extension import (
    calculate_quartz_transducer_hpht_UQFF,
    canonical_suppression,
    conventional_drift,
    drift_comparison,
    UQFF_AVAILABLE,
)
from .uqff_downhole_engine import (
    Sensor,
    SimulatorConfig,
    UQFFDownholeEngine,
    WellProfile,
    load_well_profile_csv,
    make_sensor_string,
    DEFAULT_TD_FT,
    DEFAULT_SENSOR_DEPTHS_FT,
)

__version__ = "1.1.0"
__all__ = [
    "calculate_quartz_transducer_hpht_UQFF", "canonical_suppression",
    "conventional_drift", "drift_comparison",
    "UQFF_AVAILABLE", "Sensor", "SimulatorConfig", "UQFFDownholeEngine",
    "WellProfile", "load_well_profile_csv", "make_sensor_string",
    "DEFAULT_TD_FT", "DEFAULT_SENSOR_DEPTHS_FT",
]
