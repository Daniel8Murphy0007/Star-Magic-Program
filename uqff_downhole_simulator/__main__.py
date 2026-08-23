"""Headless CLI for the UQFF Downhole Simulator (v1.6.0 extension).

    python -m uqff_downhole_simulator run          --steps 200 --out run.csv
    python -m uqff_downhole_simulator service-life --years 5 --out curves.csv
    python -m uqff_downhole_simulator telemetry    --hours 24 --seed 11 --out field.csv
    python -m uqff_downhole_simulator case-study   --td 25000 --out case.md

Shared options (all subcommands): --gauges N, --td FT, --profile CSV,
--spec PRESET|JSON, --kickoff FT --inclination DEG (deviation).
No display needed anywhere; every subcommand writes a file and prints a
one-line summary.
"""

from __future__ import annotations

import argparse
import json
import sys


def _add_well_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--td", type=float, default=None, help="total depth (MD), ft")
    p.add_argument("--gauges", type=int, default=None, help="number of gauges (evenly spaced)")
    p.add_argument("--profile", type=str, default=None, help="well profile CSV (depth_ft,pressure_psi,temp_F; TVD-indexed)")
    p.add_argument("--spec", type=str, default=None, help="gauge spec: preset name or a datasheet JSON path")
    p.add_argument("--kickoff", type=float, default=None, help="deviation: kickoff MD, ft")
    p.add_argument("--inclination", type=float, default=None, help="deviation: tangent inclination, deg from vertical")


def _build_config(a):
    from . import (SimulatorConfig, load_well_profile_csv, make_sensor_string,
                   GAUGE_SPECS, load_gauge_spec_json, DEFAULT_TD_FT)
    from .uqff_deviation import DeviationSurvey
    td = a.td if a.td is not None else DEFAULT_TD_FT
    kw = {"td_ft": td}
    if a.gauges is not None:
        kw["sensor_depths_ft"] = make_sensor_string(a.gauges, td_ft=td)
    if a.profile:
        kw["profile"] = load_well_profile_csv(a.profile)
    if a.spec:
        kw["gauge_spec"] = (GAUGE_SPECS[a.spec] if a.spec in GAUGE_SPECS
                            else load_gauge_spec_json(a.spec))
    if a.kickoff is not None or a.inclination is not None:
        if a.kickoff is None or a.inclination is None:
            raise SystemExit("--kickoff and --inclination must be given together")
        kw["deviation"] = DeviationSurvey.from_kickoff(a.kickoff, a.inclination, td)
    return SimulatorConfig(**kw)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="uqff_downhole_simulator",
                                 description="UQFF Downhole Simulator - headless CLI")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run", help="run the engine, export the P/T history CSV")
    _add_well_args(p_run)
    p_run.add_argument("--steps", type=int, default=200)
    p_run.add_argument("--out", type=str, default="uqff_downhole_run.csv")

    p_sl = sub.add_parser("service-life", help="accumulate twin-leg drift, export divergence curves")
    _add_well_args(p_sl)
    p_sl.add_argument("--years", type=float, default=5.0)
    p_sl.add_argument("--recal", type=float, default=None, help="recalibration interval, years")
    p_sl.add_argument("--seed", type=int, default=None)
    p_sl.add_argument("--out", type=str, default="uqff_service_life.csv")

    p_tm = sub.add_parser("telemetry", help="field-telemetry acquisition, export historian CSV")
    _add_well_args(p_tm)
    p_tm.add_argument("--hours", type=float, default=24.0)
    p_tm.add_argument("--seed", type=int, default=None)
    p_tm.add_argument("--out", type=str, default="uqff_telemetry.csv")

    p_cs = sub.add_parser("case-study", help="depth sweep, write the one-page markdown case")
    _add_well_args(p_cs)
    p_cs.add_argument("--points", type=int, default=12)
    p_cs.add_argument("--name", type=str, default="case-study well")
    p_cs.add_argument("--horizon", type=float, default=5.0)
    p_cs.add_argument("--out", type=str, default="uqff_downhole_case_study.md")

    a = ap.parse_args(argv)

    from . import (UQFFDownholeEngine, ServiceLifeConfig, ServiceLifeSimulator,
                   TelemetryConfig, TelemetryRecorder, CaseStudyConfig,
                   case_study, write_markdown, GAUGE_SPECS, load_gauge_spec_json,
                   load_well_profile_csv, DEFAULT_TD_FT)

    if a.cmd == "run":
        eng = UQFFDownholeEngine(_build_config(a))
        for _ in range(a.steps):
            eng.step()
        out = eng.export_csv(a.out)
        s = eng.summary()
        print(f"run: {s['sensors']} gauges x {a.steps} steps -> {out} "
              f"(avg drift {s['avg_drift_pct']} %FS/yr, suppression {s['canonical_suppression_at_unity_trims']})")
    elif a.cmd == "service-life":
        eng = UQFFDownholeEngine(_build_config(a))
        cfg = ServiceLifeConfig(years=a.years, recalibration_interval_years=a.recal, seed=a.seed)
        sim = ServiceLifeSimulator(engine=eng, config=cfg).run()
        out = sim.export_csv(a.out)
        d = sim.divergence_summary()
        print(f"service-life: {a.years:g} yr -> {out} "
              f"(sep {d['predicted_separation_rate_psi_yr']} psi/yr, ratio pred {d['predicted_ratio_suppression']})")
    elif a.cmd == "telemetry":
        eng = UQFFDownholeEngine(_build_config(a))
        rec = TelemetryRecorder(engine=eng, config=TelemetryConfig(duration_hours=a.hours, seed=a.seed)).run()
        out = rec.export_csv(a.out)
        s = rec.telemetry_summary()
        print(f"telemetry: {s['samples']} samples -> {out} "
              f"(uptime {s['uptime_pct']}%, stuck P/R {s['stuck_score']['precision']}/{s['stuck_score']['recall']})")
    elif a.cmd == "case-study":
        from .uqff_deviation import DeviationSurvey
        td = a.td if a.td is not None else DEFAULT_TD_FT
        kw = {"td_ft": td, "n_depth_points": a.points, "well_name": a.name, "horizon_years": a.horizon}
        if a.profile:
            kw["profile"] = load_well_profile_csv(a.profile)
        if a.spec:
            kw["gauge_spec"] = (GAUGE_SPECS[a.spec] if a.spec in GAUGE_SPECS
                                else load_gauge_spec_json(a.spec))
        if a.kickoff is not None and a.inclination is not None:
            kw["deviation"] = DeviationSurvey.from_kickoff(a.kickoff, a.inclination, td)
        out = write_markdown(case_study(CaseStudyConfig(**kw)), a.out)
        print(f"case-study: -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
