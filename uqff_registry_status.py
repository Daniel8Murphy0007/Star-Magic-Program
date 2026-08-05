"""uqff_registry_status — campaign registry census (Star-Magic-Program).

HONESTY NOTE (2026-08-03 repair):
This module previously shipped as a v0.2.0 SCAFFOLD STUB whose writer functions
emitted hardcoded "no rows wired yet" text, while the bundled report files
(UNIFIED_REGISTRY_STATUS_REPORT.md / _RESULTS_TABLE.md / _FALSIFIABILITY.md)
actually carried the *predecessor* Star-Magic R0-R5 physics results (9-primitive
-> 73-derived-constant table, 2,549-row registry). The stub therefore falsely
claimed to generate files it did not, and running it would have DELETED the
inherited physics results.

This module is now read-only and non-destructive:
  * It NEVER writes over the inherited frozen reference files
    (UNIFIED_REGISTRY_STATUS_REPORT.md, UNIFIED_REGISTRY_RESULTS_TABLE.md/.csv,
    UNIFIED_REGISTRY_FALSIFIABILITY.md, UNIFIED_REGISTRY_SCHEMA.md).
  * calculate_status_report() computes an HONEST live census of THIS repo's
    paper-wiring campaign registry (UNIFIED_REGISTRY.csv), parsed with the csv
    module (quoted comma-bearing fields handled correctly).

The campaign's authoritative wired/not-wired ledger is WHITEPAPER_INDEX.md;
this surface is a programmatic cross-check of the campaign CSV, nothing more.
"""
from __future__ import annotations

import csv
from typing import Any


REGISTRY_CSV = "UNIFIED_REGISTRY.csv"
GRAPH_CSV = "UNIFIED_REGISTRY_GRAPH.csv"
CITATIONS_CSV = "UNIFIED_REGISTRY_CORPUS_CITATIONS.csv"
XGEO_QUEUE_CSV = "UNIFIED_REGISTRY_XGEO_QUEUE.csv"
XGEO_ROUTES_CSV = "UNIFIED_REGISTRY_XGEO_ROUTES.csv"
XGEO_CONFIRMATIONS_CSV = "UNIFIED_REGISTRY_XGEO_CONFIRMATIONS.csv"


def _load_registry_rows() -> list[dict[str, Any]]:
    try:
        with open(REGISTRY_CSV, "r", encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []


def _count_data_lines(path: str) -> int:
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            n = sum(1 for _ in f)
        return max(0, n - 1)
    except FileNotFoundError:
        return 0


def calculate_status_report(dataset: dict | None = None) -> dict:
    """Honest live census of THIS repo's campaign registry (UNIFIED_REGISTRY.csv)."""
    rows = _load_registry_rows()
    statuses: dict[str, int] = {}
    papers: set[str] = set()
    for r in rows:
        st = (r.get("status") or "").strip()
        statuses[st] = statuses.get(st, 0) + 1
        src = (r.get("paper_source") or "").strip()
        if src.startswith("PAPER_"):
            papers.add(src.split()[0])
    return {
        "value": {
            "registry_rows": len(rows),
            "distinct_papers_in_registry": len(papers),
            "status_breakdown": statuses,
            "graph_edges": _count_data_lines(GRAPH_CSV),
            "corpus_citation_rows": _count_data_lines(CITATIONS_CSV),
            "xgeo_queue_tasks": _count_data_lines(XGEO_QUEUE_CSV),
            "xgeo_routes": _count_data_lines(XGEO_ROUTES_CSV),
            "xgeo_confirmations": _count_data_lines(XGEO_CONFIRMATIONS_CSV),
            "note": "campaign census; physics results table is a frozen inherited reference, not derived here",
        }
    }


if __name__ == "__main__":
    import json
    print(json.dumps(calculate_status_report()["value"], indent=2))
