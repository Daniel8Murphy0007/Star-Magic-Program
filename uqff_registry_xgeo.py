"""uqff_registry_xgeo — Cross-Geometry Derivation Campaign queue builder (XGEO).

Emits (idempotent, read-only inputs):
    UNIFIED_REGISTRY_XGEO_QUEUE.csv         cross-geometry tasks
    UNIFIED_REGISTRY_XGEO_ROUTES.csv        append-only routing ledger
    UNIFIED_REGISTRY_XGEO_EXTRACTED.csv     opaque-formula recoveries
    UNIFIED_REGISTRY_XGEO_CONFIRMATIONS.csv two-route agreement records

STATUS: v0.2.0 scaffold. No tasks queued, no routes ruled, no extractions.
The campaign begins in v0.3.0+ as each paper's dispatch is wired.

Discipline (from predecessor Star-Magic v5.86.0 R1 verdict + PAPER_1160
d26-generator chain):
    - Value-coincidence and name-token matching REJECTED as numerology.
    - Fills require published identity chains or script-verified extraction.
    - ROUTES.csv is append-only (rulings ledger, merged on regeneration).
"""
from __future__ import annotations

import csv


QUEUE_CSV = "UNIFIED_REGISTRY_XGEO_QUEUE.csv"
ROUTES_CSV = "UNIFIED_REGISTRY_XGEO_ROUTES.csv"
EXTRACTED_CSV = "UNIFIED_REGISTRY_XGEO_EXTRACTED.csv"
CONFIRMATIONS_CSV = "UNIFIED_REGISTRY_XGEO_CONFIRMATIONS.csv"


def _build_queue() -> list[tuple]:
    """Return XGEO task tuples for the queue.

    Column format: observable, domain, owner_geometry, target_geometry,
    owner_formula, owner_value, target, primary_source, primitives_used,
    route_status, route_formula, route_paper.

    v0.2.0: empty.
    """
    return []


def _load_routes_ledger() -> list[tuple]:
    """Load the append-only XGEO_ROUTES ruling ledger. v0.2.0: empty."""
    try:
        with open(ROUTES_CSV, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            return list(reader)
    except FileNotFoundError:
        return []


def _build_extracted() -> list[tuple]:
    """Return XGEO opaque-formula extractions. v0.2.0: empty."""
    return []


def _build_confirmations() -> list[tuple]:
    """Return XGEO two-route agreements. v0.2.0: empty."""
    return []


def write_queue_csv() -> None:
    with open(QUEUE_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["observable", "domain", "owner_geometry", "target_geometry",
                    "owner_formula", "owner_value", "target", "primary_source",
                    "primitives_used", "route_status", "route_formula",
                    "route_paper"])
        for row in _build_queue():
            w.writerow(row)


def write_routes_csv() -> None:
    """Append-only ledger — preserve existing rulings, add new ones."""
    existing = _load_routes_ledger()
    with open(ROUTES_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["observable", "target_geometry", "route_formula",
                    "route_paper", "status"])
        for row in existing:
            w.writerow(row)


def write_extracted_csv() -> None:
    with open(EXTRACTED_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["observable", "session_script", "extracted_formula",
                    "primitives_in_expr", "value_verified"])
        for row in _build_extracted():
            w.writerow(row)


def write_confirmations_csv() -> None:
    with open(CONFIRMATIONS_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["observable", "route_1_formula", "route_1_value",
                    "route_2_formula", "route_2_value", "target",
                    "route_1_residual_pct", "route_2_residual_pct",
                    "classification", "sources"])
        for row in _build_confirmations():
            w.writerow(row)


def main() -> None:
    write_queue_csv()
    write_routes_csv()
    write_extracted_csv()
    write_confirmations_csv()


if __name__ == "__main__":
    main()
