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
def read_temperature_csv(path) -> LiveStream:
    """Ingest a temperature-profile CSV (header `d,t`: depth in metres,
    temperature in degC — the GEUS ice-borehole database format) as a
    depth-indexed LiveStream with a TEMP channel. The catalogue's non-LAS
    entry path (v1.16.0, driven by the GISP2 prize well)."""
    import csv as _csv
    p = Path(path)
    d, t = [], []
    with p.open(newline='', encoding='utf-8') as f:
        for row in _csv.DictReader(f):
            d.append(float(row['d']))
            t.append(float(row['t']))
    from .uqff_ports import StreamChannel
    return LiveStream(name=p.stem, source_format='temperature_csv',
                      index_kind='depth', index=np.array(d, dtype=float),
                      channels={'TEMP': StreamChannel(name='TEMP', unit='DEGC',
                                                      values=np.array(t, dtype=float))},
                      meta={'format': 'GEUS d,t temperature profile'})


def read_survey_csv(path):
    """Ingest a deviation-survey CSV (NLOG-style long headers: Depth /
    TrueVertical Depth, with inclination/azimuth/offsets alongside) as a
    DeviationSurvey - MD->TVD taken DIRECTLY from the measured columns, no
    minimum-curvature reconstruction needed. The catalogue's survey-entry
    path (v1.19.0, driven by the real L06-06 trajectory)."""
    import csv as _csv
    from .uqff_deviation import DeviationSurvey
    p = Path(path)
    md, tvd = [], []
    with p.open(newline='', encoding='utf-8') as f:
        reader = _csv.DictReader(f)
        md_col = next(c for c in reader.fieldnames if c.strip().lower() in ('depth', 'md', 'md_ft'))
        tvd_col = next(c for c in reader.fieldnames
                       if 'truevertical' in c.strip().lower().replace(' ', '')
                       or c.strip().lower() in ('tvd', 'tvd_ft'))
        for row in reader:
            md.append(float(row[md_col]))
            tvd.append(float(row[tvd_col]))
    return DeviationSurvey(md_ft=md, tvd_ft=tvd, name=p.stem)


def read_core_csv(path) -> LiveStream:
    """Ingest a conventional core-analysis CSV (Volve-style header:
    DEPTH,OrigDepth,CORE_NO,SAMPLE,...) as a depth-indexed LiveStream whose
    channels are the numeric lab columns (permeability/porosity/saturations/
    grain density; blanks -> NaN). Laboratory ground truth alongside logs
    (v1.20.0, driven by the real 15/9-19 A core data)."""
    import csv as _csv
    from .uqff_ports import StreamChannel
    p = Path(path)
    with p.open(newline='', encoding='utf-8') as f:
        reader = _csv.DictReader(f)
        cols = [c for c in reader.fieldnames if c != 'DEPTH']
        depth, data = [], {c: [] for c in cols}
        for row in reader:
            depth.append(float(row['DEPTH']))
            for c in cols:
                v = (row.get(c) or '').strip()
                data[c].append(float(v) if v else np.nan)
    return LiveStream(name=p.stem, source_format='core_csv',
                      index_kind='depth', index=np.array(depth, dtype=float),
                      channels={c: StreamChannel(name=c, unit='', values=np.array(data[c]))
                                for c in cols},
                      meta={'format': 'conventional core analysis (units per provenance)'})


def read_production_csv(path) -> LiveStream:
    """Ingest a daily production-history CSV (Volve-style header:
    DATEPRD,WELL_BORE_CODE,...) as a TIME-indexed LiveStream - the
    catalogue's first time-indexed kind (v1.21.0, driven by the real
    15/9-F-12/F-14 daily records). Index = elapsed seconds from the first
    date (86400 s cadence); channels are the per-well numeric operational
    columns, namespaced COL[well]; blanks and absent dates -> NaN. Units are
    NOT in the header - carried per the provenance data dictionary."""
    import csv as _csv
    from datetime import date as _date
    from .uqff_ports import StreamChannel
    p = Path(path)
    numeric = ('ON_STREAM_HRS', 'AVG_DOWNHOLE_PRESSURE', 'AVG_DOWNHOLE_TEMPERATURE',
               'AVG_DP_TUBING', 'AVG_ANNULUS_PRESS', 'AVG_CHOKE_SIZE_P', 'AVG_WHP_P',
               'AVG_WHT_P', 'DP_CHOKE_SIZE', 'BORE_OIL_VOL', 'BORE_GAS_VOL',
               'BORE_WAT_VOL', 'BORE_WI_VOL')
    units = {'ON_STREAM_HRS': 'h', 'AVG_DOWNHOLE_PRESSURE': 'bar',
             'AVG_DOWNHOLE_TEMPERATURE': 'degC', 'AVG_DP_TUBING': 'bar',
             'AVG_ANNULUS_PRESS': 'bar', 'AVG_CHOKE_SIZE_P': 'pct',
             'AVG_WHP_P': 'bar', 'AVG_WHT_P': 'degC', 'DP_CHOKE_SIZE': 'bar',
             'BORE_OIL_VOL': 'Sm3', 'BORE_GAS_VOL': 'Sm3', 'BORE_WAT_VOL': 'Sm3',
             'BORE_WI_VOL': 'Sm3'}
    rows = []
    with p.open(newline='', encoding='utf-8') as f:
        for row in _csv.DictReader(f):
            rows.append(row)
    if not rows:
        raise ValueError(f"production CSV {p.name}: no records")
    dates = sorted({r['DATEPRD'] for r in rows})
    wells = []
    for r in rows:
        w = r['NPD_WELL_BORE_NAME']
        if w not in wells:
            wells.append(w)
    d0 = _date.fromisoformat(dates[0])
    idx = np.array([( _date.fromisoformat(d) - d0).days * 86400.0 for d in dates])
    pos = {d: i for i, d in enumerate(dates)}
    channels = {}
    for w in wells:
        grids = {c: np.full(len(dates), np.nan) for c in numeric}
        for r in rows:
            if r['NPD_WELL_BORE_NAME'] != w:
                continue
            i = pos[r['DATEPRD']]
            for c in numeric:
                v = (r.get(c) or '').strip()
                if v:
                    grids[c][i] = float(v)
        for c in numeric:
            channels[f"{c}[{w}]"] = StreamChannel(
                name=f"{c}[{w}]", unit=units[c] + ' (per provenance dictionary)',
                values=grids[c])
    return LiveStream(name=p.stem, source_format='production_csv',
                      index_kind='time_s', index=idx, channels=channels,
                      meta={'format': 'daily production history (per-well, namespaced channels)',
                            'start_date': dates[0], 'end_date': dates[-1],
                            'wells': ';'.join(wells), 'cadence_s': '86400',
                            'units_note': 'units interpretive per provenance data dictionary, not in-file'})


def read_ktb_dat(path) -> LiveStream:
    """Ingest a KTB Information System temperature-log file ('!'-comment
    header + space-separated DEPT TMP3 HTEN MRES rows) as a depth-indexed
    LiveStream - the catalogue's first HOT-regime temperature dialect
    (v1.22.0, driven by the real KTB-HB hlog246). Header lines are carried
    into meta (well name, log date, time-since-circulation fields - the
    disturbed-log disclosure lives in the data itself)."""
    import re as _re
    p = Path(path)
    hdr, rows, cols = [], [], []
    col_re = _re.compile(r'^!\s+\d+\s+"(\w+)\s[^"]*"\s+F\d*\s+(\S+)')
    with p.open(encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line.strip():
                continue
            if line.lstrip().startswith('!'):
                hdr.append(line)
                m = col_re.match(line.strip())
                if m:
                    cols.append((m.group(1), m.group(2)))
                continue
            parts = line.split()
            if cols and len(parts) == len(cols):
                try:
                    rows.append([float(x) for x in parts])
                except ValueError:
                    continue
    if not cols:
        raise ValueError(f"KTB log {p.name}: no column-definition block in header")
    if not rows:
        raise ValueError(f"KTB log {p.name}: no data rows")
    import numpy as _np
    arr = _np.array(rows, dtype=float)
    meta = {'format': 'KTB Information System temperature log (disturbed mud-temperature log, per provenance)'}
    val_re = {'well': _re.compile(r'"WN\s+UNAL\s+.*?\s{3,}(\S[^"]*)"'),
              'log_date': _re.compile(r'"DATE\s+UNAL\s+.*?\s{3,}(\S[^"]*)"'),
              'time_logger_at_bottom': _re.compile(r'"TLAB\s+UNAL\s+Time Logger At Bottom\s{3,}(\S[^"]*)"'),
              'time_circulation_stopped': _re.compile(r'"TCS\s+UNAL\s+Time Circulation Stopped\s{3,}(\S[^"]*)"')}
    for h in hdr:
        for key, rx in val_re.items():
            m = rx.search(h)
            if m and key not in meta:
                meta[key] = m.group(1).strip()
    from .uqff_ports import StreamChannel
    return LiveStream(name=p.stem, source_format='ktb_dat',
                      index_kind='depth', index=arr[:, 0],
                      channels={n: StreamChannel(name=n, unit=u, values=arr[:, i + 1])
                                for i, (n, u) in enumerate(cols[1:], start=0)},
                      meta=meta)


def read_ktb_table(path) -> LiveStream:
    """Ingest a KTB Information System TYPED table ('!'-header declaring
    F/C/I columns, e.g. the rock-mechanics compressive-strength tables) as a
    depth-indexed LiveStream (v1.26.0, driven by the real VB core-strength
    file). Numeric (F/I) columns become channels; C-typed string columns
    stay verbatim in the file (ROCK TYPE is carried as per-sample quality
    on the strength channel). Rendering-collapsed tabs make some short rows
    ambiguous: a trailing decimal token is assigned by DECLARED TYPE (an I2
    dip cannot hold a decimal); a trailing integer token that could be
    either column is REFUSED - NaN + a quality flag with the raw token."""
    import re as _re
    p = Path(path)
    col_re = _re.compile(r'^!\s+\d+\s+"([^"]+)"\s+([FCI])\d*\s*(\S*)')
    tok_re = _re.compile(r'"[^"]*"|\S+')
    cols, rows = [], []
    with p.open(encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line.strip():
                continue
            if line.lstrip().startswith('!'):
                m = col_re.match(line.strip())
                if m:
                    cols.append((m.group(1).replace(' ', '_'), m.group(2), m.group(3)))
                continue
            toks = tok_re.findall(line)
            if len(toks) >= 6:
                rows.append(toks)
    if not cols or not rows:
        raise ValueError(f"KTB table {p.name}: no typed column block or no rows")
    import numpy as _np
    n = len(rows)
    names = [c[0] for c in cols]
    num_idx = [i for i, c in enumerate(cols) if c[1] in ('F', 'I')]
    grids = {names[i]: _np.full(n, _np.nan) for i in num_idx if i > 0}
    depth = _np.full(n, _np.nan)
    rock = ['' for _ in range(n)]
    flags = ['' for _ in range(n)]
    rock_col = next((i for i, c in enumerate(cols) if 'ROCK' in c[0]), None)
    for r, toks in enumerate(rows):
        if len(toks) == len(cols):
            assign = list(enumerate(toks))
        else:
            assign = list(enumerate(toks[:6]))
            trail = toks[6:]
            if len(trail) == 1:
                if '.' in trail[0]:
                    assign.append((6, trail[0]))
                else:
                    flags[r] = f"AMBIGUOUS_TRAILING:{trail[0]}"
        for ci, tok in assign:
            name, typ = cols[ci][0], cols[ci][1]
            if ci == 0:
                depth[r] = float(tok)
            elif typ in ('F', 'I'):
                v = tok.strip().strip('"')
                if v:
                    grids[name][r] = float(v)
            elif ci == rock_col:
                rock[r] = tok.strip('"')
    from .uqff_ports import StreamChannel
    channels = {}
    for i in num_idx:
        if i == 0:
            continue
        name, unit = names[i], cols[i][2]
        q = rock if 'STRENGTH' in name else (flags if name == 'E_MODUL' else None)
        channels[name] = StreamChannel(name=name, unit=unit, values=grids[name],
                                       quality=list(q) if q else None)
    return LiveStream(name=p.stem, source_format='ktb_table',
                      index_kind='depth', index=depth, channels=channels,
                      meta={'format': 'KTB typed table (rock mechanics); string columns verbatim in file',
                            'ambiguous_rows_refused': str(sum(1 for x in flags if x))})


def read_pangaea_txt(path) -> LiveStream:
    """Ingest a PANGAEA machine-readable textfile export (self-describing
    '/* DATA DESCRIPTION */' header + tab-separated matrix) as a
    depth-indexed LiveStream (v1.28.0, driven by the real ODP 504B borehole
    -fluid dataset). The header's citation, license and coordinates go to
    meta; numeric columns become channels (units parsed from '[...]');
    short rows pad to NaN; the first non-numeric column rides as per-sample
    quality on the first channel."""
    import re as _re
    p = Path(path)
    text = p.open(encoding='utf-8').read()
    if not text.startswith('/* DATA DESCRIPTION'):
        raise ValueError(f"{p.name}: not a PANGAEA textfile export")
    head, _, body = text.partition('*/')
    meta = {'format': 'PANGAEA textfile export (self-describing header verbatim in file)'}
    m = _re.search(r'Citation:\t([^\n]+)', head)
    if m:
        meta['citation'] = m.group(1).strip().rstrip(',')
    m = _re.search(r'License:\t([^\n]+)', head)
    if m:
        meta['license'] = m.group(1).strip()
    m = _re.search(r'LATITUDE:\s*(-?[\d.]+)\s*\*\s*LONGITUDE:\s*(-?[\d.]+)', head)
    if m:
        meta['latitude'], meta['longitude'] = m.group(1), m.group(2)
    m = _re.search(r'ELEVATION:\s*(-?[\d.]+)', head)
    if m:
        meta['elevation_m'] = m.group(1)
    lines = [l for l in body.split('\n') if l.strip()]
    headers = lines[0].split('\t')
    rows = [l.split('\t') for l in lines[1:]]
    import numpy as _np
    depth_i = next((i for i, h in enumerate(headers) if h.lower().startswith('depth')), None)
    if depth_i is None:
        raise ValueError(f"{p.name}: no Depth column")
    def val(r, i):
        v = r[i].strip() if i < len(r) else ''
        try:
            return float(v) if v else _np.nan
        except ValueError:
            return None
    depth = _np.array([val(r, depth_i) for r in rows], dtype=float)
    from .uqff_ports import StreamChannel
    channels = {}
    label_col = None
    for i, h in enumerate(headers):
        if i == depth_i:
            continue
        vals = [val(r, i) for r in rows]
        if any(v is None for v in vals):
            if label_col is None:
                label_col = [r[i].strip() if i < len(r) else '' for r in rows]
            continue
        mu = _re.search(r'\[([^\]]+)\]', h)
        name = _re.sub(r'\s*\[[^\]]+\]', '', h).strip()
        channels[name] = StreamChannel(name=name, unit=(mu.group(1) if mu else ''),
                                       values=_np.array(vals, dtype=float))
    if label_col and channels:
        first = next(iter(channels))
        channels[first].quality = label_col
    return LiveStream(name=p.stem, source_format='pangaea_txt',
                      index_kind='depth', index=depth, channels=channels, meta=meta)


def _csv_kind(path: Path) -> str:
    """Distinguish catalogue CSV kinds by header: 'd,t' = temperature profile;
    survey headers = deviation survey; DEPTH,OrigDepth,CORE_NO = core analysis;
    DATEPRD,WELL_BORE_CODE = daily production history (time-indexed)."""
    with path.open(encoding='utf-8') as f:
        header = f.readline().strip().lower()
    if header.startswith('d,t'):
        return 'temperature'
    if header.startswith('depth,origdepth,core_no'):
        return 'core'
    if header.startswith('dateprd,well_bore_code'):
        return 'production'
    if 'depth' in header and ('truevertical' in header.replace(' ', '') or 'tvd' in header):
        return 'survey'
    raise ValueError(f"catalogue CSV {path.name}: unrecognized header kind")


@dataclass(frozen=True)
class CatalogEntry:
    name: str
    las_path: Path
    provenance: dict

    def stream(self) -> LiveStream:
        if self.las_path.suffix.lower() == '.txt':
            return read_pangaea_txt(self.las_path)
        if self.las_path.suffix.lower() == '.dat':
            import re as _re
            with self.las_path.open(encoding='utf-8') as _f:
                _head = _f.read(4000)
            if _re.search(r'^!\s+\d+\s+"[^"]*"\s+C\d*', _head, _re.M):
                return read_ktb_table(self.las_path)
            return read_ktb_dat(self.las_path)
        if self.las_path.suffix.lower() == '.csv':
            kind = _csv_kind(self.las_path)
            if kind == 'survey':
                raise ValueError(f"{self.name} is a DEVIATION SURVEY entry - "
                                 "use .survey() (it is a trajectory, not a log stream)")
            if kind == 'core':
                return read_core_csv(self.las_path)
            if kind == 'production':
                return read_production_csv(self.las_path)
            return read_temperature_csv(self.las_path)
        return read_las(self.las_path)

    def survey(self):
        if self.las_path.suffix.lower() == '.dat':
            st = read_ktb_dat(self.las_path)
            if 'TVD' not in st.channels:
                raise ValueError(f"{self.name} is not a trajectory entry (no TVD channel)")
            from .uqff_deviation import DeviationSurvey
            return DeviationSurvey(md_ft=[float(x) for x in st.index],
                                   tvd_ft=[float(x) for x in st.channels['TVD'].values],
                                   name=self.name)
        if self.las_path.suffix.lower() != '.csv' or _csv_kind(self.las_path) != 'survey':
            raise ValueError(f"{self.name} is not a survey entry")
        return read_survey_csv(self.las_path)


def _load_catalog() -> Dict[str, CatalogEntry]:
    out: Dict[str, CatalogEntry] = {}
    if not _CATALOG_DIR.is_dir():
        return out
    files = sorted(list(_CATALOG_DIR.glob('*.las')) + list(_CATALOG_DIR.glob('*.dat'))
                   + list(_CATALOG_DIR.glob('*.txt'))
                   + [p for p in _CATALOG_DIR.glob('*.csv') if not p.name.endswith('.provenance.json')])
    for las in files:
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
