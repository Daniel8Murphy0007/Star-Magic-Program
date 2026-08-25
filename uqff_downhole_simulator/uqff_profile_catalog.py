"""uqff_profile_catalog — the well-profile catalogue (v1.12.0 extension).

Daniel GO 2026-08-24: build a catalogue of well profiles from public
geophysical databases, so the closed stream can run on REAL wells instead of
one synthetic sample. Three parts:

  1. `PROFILE_SOURCES` — the machine-readable table of public databases
     (what each offers, direct entry points, license, access barriers stated
     honestly: several serve only ZIPs or need registration, which this
     environment cannot fetch — those are documented pull-it-yourself paths).
  2. `CATALOG` — shipped entries. Every entry has a MANDATORY provenance
     sidecar (.provenance.json) naming the source database, well, URL,
     license, fetch date, and coverage. First real entry:
     **Equinor Volve well 15/9-19 SR** (verbatim excerpt, CC/Equinor open
     licence, disclosed coverage) — real third-party well-log data flowing
     the las2 port end-to-end.
  3. `las_to_profile()` — the converter: a LAS LiveStream becomes the
     engine's profile CSV (depth_ft,pressure_psi,temp_F). Where the log
     carries no temperature/pressure curves (most composites do not), the
     converter fills them from DECLARED gradients and stamps the output
     `derivation: DERIVED_GRADIENTS` — a profile built from a real
     trajectory with derived conditions is useful and honest ONLY when
     labeled (Rule 7); measured-curve conversion is used automatically when
     the curves exist.

Headless-safe: numpy + stdlib.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

import numpy as np

from .uqff_ports import LiveStream, read_las

_CATALOG_DIR = Path(__file__).parent / "catalog"

# Temperature/pressure curve mnemonics accepted as MEASURED (LAS conventions)
_TEMP_MNEMONICS = ('TEMP', 'TEMPERATURE', 'BHT', 'WTEP', 'MRT', 'DTEMP', 'TMP')
_PRES_MNEMONICS = ('PRES', 'PRESSURE', 'WPRE', 'BHP', 'PFOR')

M_TO_FT = 3.28084


# ---------------------------------------------------------------------------
# 1) The public-source table (honest access notes)
# ---------------------------------------------------------------------------
PROFILE_SOURCES: Dict[str, dict] = {
    'kgs': {
        'name': 'Kansas Geological Survey LAS database',
        'url': 'https://www.kgs.ku.edu/Magellan/Logs/',
        'offers': '21,000+ digital wireline logs (LAS), free, no registration',
        'license': 'public state archive',
        'access': 'individual downloads are ZIPPED via the search app; yearly bulk ZIPs; download and unzip locally, then ingest via las2'},
    'volve': {
        'name': 'Equinor Volve open dataset',
        'url': 'https://www.equinor.com/energy/volve-data-sharing',
        'offers': 'complete real North Sea field: logs, surveys, production (~40,000 files)',
        'license': 'Equinor Open Data Licence (attribution)',
        'access': 'registration required for the full archive; some files publicly redistributed (see catalogue entry volve_15_9_19_sr_excerpt)'},
    'gdr_forge': {
        'name': 'DOE Geothermal Data Repository - Utah FORGE',
        'url': 'https://gdr.openei.org/submissions/1326',
        'offers': 'REAL downhole T/P logs (wells 58-32, 56-32, 78-32; June 2021 update), drilling data, surveys; DOI 10.15121/1812334',
        'license': 'CC BY 4.0',
        'access': 'T/P logs served as ZIPs (server marks all files octet-stream); download and unzip locally, then ingest the contained .las/.csv'},
    'nlog': {
        'name': 'NLOG (Netherlands Oil and Gas portal)',
        'url': 'https://www.nlog.nl/en',
        'offers': 'thousands of onshore/offshore wells: logs, deviation, production',
        'license': 'open by mandate',
        'access': 'per-well downloads; formats vary'},
    'state_regulators': {
        'name': 'US state regulators (TX RRC, ND NDIC, OK OCC, CO ECMC, WY OGCC)',
        'url': 'https://www.rrc.texas.gov/ (and peers)',
        'offers': 'well files: directional surveys, pressure tests, BHT reports',
        'license': 'public regulatory archives',
        'access': 'per-state portals; mostly PDF/scans plus some digital data'},
    'offshore_national': {
        'name': 'BOEM/BSEE (US offshore), UK NSTA NDR, Australia NOPIMS',
        'url': 'https://www.data.boem.gov/ ; https://ndr.nstauthority.co.uk/ ; https://nopims.disr.gov.au/',
        'offers': 'national open repositories: surveys, logs, completions',
        'license': 'open national archives',
        'access': 'portal downloads; registration varies'},
}


# ---------------------------------------------------------------------------
# 2) The shipped catalogue (provenance mandatory)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class CatalogEntry:
    name: str
    las_path: Path
    provenance: dict

    def stream(self) -> LiveStream:
        return read_las(self.las_path)


def _load_catalog() -> Dict[str, CatalogEntry]:
    out: Dict[str, CatalogEntry] = {}
    if not _CATALOG_DIR.is_dir():
        return out
    for las in sorted(_CATALOG_DIR.glob('*.las')):
        prov_path = las.with_suffix('.provenance.json')
        if not prov_path.exists():
            raise ValueError(f"catalogue entry {las.name} has NO provenance sidecar - "
                             "an uncited catalogue entry is not a catalogue entry (Rule 7)")
        with prov_path.open(encoding='utf-8') as f:
            prov = json.load(f)
        for req in ('source_database', 'source_url', 'license', 'fetch_date', 'coverage'):
            if not prov.get(req):
                raise ValueError(f"catalogue entry {las.name}: provenance missing '{req}'")
        out[las.stem] = CatalogEntry(name=las.stem, las_path=las, provenance=prov)
    return out


CATALOG: Dict[str, CatalogEntry] = _load_catalog()


# ---------------------------------------------------------------------------
# 3) The converter
# ---------------------------------------------------------------------------
def las_to_profile(stream_or_path, out_csv=None,
                   depth_unit: str = 'm',
                   surface_temp_F: float = 75.0,               # anchor: template surface ambient
                   temp_gradient_F_per_ft: float = 0.018,      # anchor: template geothermal gradient
                   surface_pressure_psi: float = 14.7,         # anchor: 1 atm
                   pressure_gradient_psi_per_ft: float = 0.465 # anchor: industry hydrostatic
                   ) -> dict:
    """Convert a LAS stream (or path) to the engine's profile CSV format
    (depth_ft,pressure_psi,temp_F).

    MEASURED path: when the LAS carries temperature/pressure curves (matched
    on standard mnemonics) they are used, unit-converted, and the result is
    stamped `derivation: MEASURED_CURVES`.

    DERIVED path (most composite logs): no T/P curves exist - the REAL depth
    stations are kept and conditions are filled from the DECLARED gradients,
    stamped `derivation: DERIVED_GRADIENTS`. Useful for geometry-true
    simulation; honest only because it says so (Rule 7).
    """
    stream = stream_or_path if isinstance(stream_or_path, LiveStream) else read_las(stream_or_path)
    if stream.index_kind != 'depth':
        raise ValueError("las_to_profile needs a depth-indexed stream")
    depths = np.asarray(stream.index, dtype=float)
    ok = ~np.isnan(depths)
    depths_ft = depths[ok] * (M_TO_FT if depth_unit.lower().startswith('m') else 1.0)

    temp_ch = next((c for m in _TEMP_MNEMONICS for c in stream.channels if c.upper().startswith(m)), None)
    pres_ch = next((c for m in _PRES_MNEMONICS for c in stream.channels if c.upper().startswith(m)), None)

    # Real header anchors (v1.13.0, from the Kennetcook #2 catalogue well):
    # a measured BHT + TD in the LAS ~P section gives a REAL two-point thermal
    # profile - stronger than pure gradients, weaker than a full curve, and
    # labeled as exactly that.
    bht_F = td_ft = None
    if stream.meta.get('BHT'):
        try:
            bht = float(stream.meta['BHT'])
            bht_F = bht * 9.0 / 5.0 + 32.0 if stream.meta.get('BHT_UNIT', '').upper().startswith('DEGC') else bht
            td_m = float(stream.meta.get('TDL') or stream.meta.get('TDD') or 0.0)
            td_ft = td_m * (M_TO_FT if depth_unit.lower().startswith('m') else 1.0) or None
        except (ValueError, TypeError):
            bht_F = td_ft = None

    if temp_ch or pres_ch:
        derivation = 'MEASURED_CURVES'
        t_vals = stream.channels[temp_ch].values[ok] if temp_ch else None
        p_vals = stream.channels[pres_ch].values[ok] if pres_ch else None
        if t_vals is not None and stream.channels[temp_ch].unit.upper().startswith('DEGC'):
            t_vals = t_vals * 9.0 / 5.0 + 32.0
        temp_F = (t_vals if t_vals is not None
                  else surface_temp_F + depths_ft * temp_gradient_F_per_ft)
        pres_psi = (p_vals if p_vals is not None
                    else surface_pressure_psi + depths_ft * pressure_gradient_psi_per_ft)
    elif bht_F is not None and td_ft:
        derivation = 'DERIVED_FROM_MEASURED_BHT'
        temp_F = surface_temp_F + (bht_F - surface_temp_F) * (depths_ft / td_ft)
        pres_psi = surface_pressure_psi + depths_ft * pressure_gradient_psi_per_ft
    else:
        derivation = 'DERIVED_GRADIENTS'
        temp_F = surface_temp_F + depths_ft * temp_gradient_F_per_ft
        pres_psi = surface_pressure_psi + depths_ft * pressure_gradient_psi_per_ft

    rows = [(float(d), float(p), float(t)) for d, p, t in zip(depths_ft, pres_psi, temp_F)
            if not (np.isnan(p) or np.isnan(t))]
    result = {
        'stations': len(rows),
        'depth_range_ft': [round(rows[0][0], 1), round(rows[-1][0], 1)] if rows else None,
        'derivation': derivation,
        'temperature_curve_used': temp_ch,
        'pressure_curve_used': pres_ch,
        'source_stream': stream.name,
        'note': ('REAL depth stations; T/P filled from DECLARED gradients - labeled, not measured'
                 if derivation == 'DERIVED_GRADIENTS' else
                 'measured curves converted; gaps dropped'),
    }
    if out_csv is not None:
        p = Path(out_csv)
        with p.open('w', encoding='utf-8', newline='') as f:
            f.write('depth_ft,pressure_psi,temp_F\n')
            for d, pr, t in rows:
                f.write(f'{d:.1f},{pr:.1f},{t:.1f}\n')
        result['csv'] = str(p)
    return result
