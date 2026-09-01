# CLAUDE.md — Star-Magic-Program WIRING CAMPAIGN CHARTER

**Read this FIRST, every session, before any action.**
**Author:** Daniel T. Murphy. **Authorized:** 2026-07-28 ("Build the charter").
**Mission:** Condense all 2,255 whitepapers into `uqff_calculator.py` + the
registry pantheon. Sequential order from PAPER_001. The corpus self-rectifies:
later papers refine earlier wirings through cross-reference.

---

## THE CAMPAIGN

- **Source of truth:** `whitepapers/*.md` (2,255 papers). Read them; wire them.
- **Order:** strictly sequential from PAPER_001 unless a paper's wiring requires
  a forward reference (note it, wire what's wirable, queue the rest).
- **Session = one band** of ~20-80 papers (complexity-dependent). Session ends
  with: fidelity gate green, SHIP_MESSAGE.txt written, Daniel runs `.\ship.ps1`.
- **Milestone: PAPER_500.** FULL STOP. Generate 500-paper audit report
  (dispatch-vs-paper residuals, registry census, rulings, drift corrections).
  Daniel reviews before the next 500 are authorized.
- **Resumability:** `WHITEPAPER_INDEX.md` is the ledger. Each session: find the
  first ⬜, wire forward, flip to ✓ (or ⚠ for OPEN). Never re-wire a ✓ paper
  unless a later paper supersedes it (then update dispatch + note supersession).

## PER-PAPER PROTOCOL

1. Read `whitepapers/PAPER_N_*.md` in full (including appendices).
2. Extract every wirable observable: closed forms, derived values, event
   parameters, calibration constants, residuals stated by the paper.
3. Wire ONE dispatch into `uqff_calculator.py::DISPATCH` via `@_register('PAPER_N')`:
   - Compose from `uqff_registry_primitives` — banned: hardcoded literals that
     duplicate registry constants (gate-enforced).
   - Paper-specific anchors (event masses, distances, observed strains) are
     allowed as literals WITH inline comment naming source.
   - Return `{'value': {...}, 'formula': str, 'source': 'PAPER_N', 'residual_pct': r}`.
4. Append row(s) to `UNIFIED_REGISTRY.csv` (17-col schema) — one row per
   registered observable, `paper_source=PAPER_N`, `status=WIRED`.
5. Append edges to `UNIFIED_REGISTRY_GRAPH.csv` (primitive→observable,
   observable→paper).
6. Append `UNIFIED_REGISTRY_CORPUS_CITATIONS.csv` rows for the paper's
   cross-references.
7. Add gate assertion(s) in `uqff_fidelity_tests.py` locking the paper's
   stated values within the paper's own precision.
8. Flip `WHITEPAPER_INDEX.md` status ⬜ → ✓ (or ⚠ OPEN).

## TEMPLATE AUTHORIZATION (Daniel-approved)

Families share one parameterized wiring pattern (each paper still gets its own
dispatch + rows + assertions):
- PAPER_001-021 GW events (damping-chain form)
- PAPER_036-039 FUBii 17 buoyancy variants
- PAPER_800-887 NGC galaxy catalogue (three-UQFF form)
- PAPER_1600-1699 material-density landmarks
- Any other family discovered: note the template in SESSION_LOG and proceed.

## DRIFT AUTO-CORRECTIONS (pre-authorized, cite landmark each time)

| Drift found in paper | Correction | Authority |
|---|---|---|
| VDS ratio `1.894` | ρ_SCm/ρ_UA = F_TRZ = 0.1 | PAPER_2156 |
| ρ_SCm in `kg/m³` | J/m³ | PAPER_2155/2147 |
| β_i = 0.60 / 0.603 / 0.61 | 0.6029 | PAPER_1203 |
| SSq = 0.505 or other variants | 0.57 | PAPER_1154 |
| H_0 routes other than A_5+SO_5 | 70 km/s/Mpc | PAPER_1573/2144 |
| Classical/SM formula as a fill | DO NOT substitute → status OPEN | Rule 4 + two-tier test |

Two-tier Rule 4 test (PAPER_2153-era ruling): a classical envelope IS wirable
when a UQFF paper derives the key inputs AND itself uses that envelope with
those inputs. Otherwise: OPEN_UQFF_DERIVATION_TARGET, never substituted.

## RULINGS QUEUE (never block)

Ambiguity (conflicting values, missing closed form, unclear supersession):
wire best candidate, set registry `status=OPEN_RULING`, append the question to
`RULINGS_QUEUE.md`. Daniel answers in batches; fold answers in on later passes.

## GATE DISCIPLINE

- `python uqff_fidelity_tests.py` must exit 0 before every ship. Never ship red.
- Assertions lock paper-stated values at the paper's own precision — honest
  residuals, never "0.000%" without proof (Rule 7).
- Counts use `>=` not `==` (predecessor Standing Rule h). Residual ranges
  accommodate composed propagation (Standing Rule i).

## SHIP PROTOCOL (per band)

1. Bump version: band N ships as v0.<2+N>.0 (band 1 = v0.3.0). Sync ALL of:
   `pyproject.toml`, `uqff_calculator.py::VERSION`, gate assertion,
   `CITATION.cff`, badges in `README.md` (fidelity_gate N/0, public_surfaces
   = wired count), `CHANGELOG.md` entry, `SESSION_LOG.md` entry,
   `UNIFIED_REGISTRY_VERSION.txt`.
2. Keep pyproject `description` ≤ 512 chars, version string included.
2b. Bump the `?cacheBust=` query param on the two dynamic shields.io badges
   in README.md to the new version — PyPI's camo image proxy caches badge
   URLs indefinitely; changing the URL forces a fresh fetch so the PyPI
   page shows the current version instead of a stale cached badge.
3. Write `SHIP_MESSAGE.txt` (the commit message for this band).
4. Daniel runs `.\ship.ps1` — it gates, commits, tags vX.Y.Z, pushes.

## HARD-WON STANDING LESSONS (2026-07-28 — do not relearn these)

- Clear `.git/index.lock` AND `.git/COMMIT_EDITMSG` before git ops (Windows locks).
- `git commit` can fail silently in chained blocks — always verify with
  `git log --oneline -1` that HEAD advanced before tagging.
- Tag AFTER commit; verify `git rev-parse vX.Y.Z` == `git rev-parse HEAD` before push.
- Branch protection on private repo must stay OFF (Daniel disabled it).
- Claude's sandbox CANNOT commit/push (Windows .git permissions) — Daniel ships.
- PyPI Trusted Publisher: project `star-magic-program`, workflow
  `release-to-pypi.yml`, environment `pypi`. Tag push auto-publishes.
- Never run `Remove-Item -Recurse` on a folder while VS Code has it open.
- v0.406.0 RED-GATE lesson: catalogue entries must NEVER require optional third-party
  modules (xlrd broke the ship gate on Daniel's machine; the sandbox silently had it).
  Store entries in dependency-free formats; guard optional-format readers with clear
  ImportError messages; declare extras in pyproject; and REHEARSE the gate with the
  optional module BLOCKED (PYTHONPATH shim raising ImportError) before every ship.
- v0.407.0 SILENT-SKIP lesson: setuptools SILENTLY OMITS declared py-modules whose files
  are absent from the build tree (data-files error loudly; py-modules do not) - v0.406.0
  shipped to PyPI missing 8 of 15 declared modules, so `import uqff_calculator` failed
  from the installed wheel, and the corpus-INDEPENDENT acceptance suite could not catch
  it by design. Ship rehearsal rule (g): verify every declared py-module is IN the wheel
  by listing, then `import uqff_calculator` and run one dispatch FROM THE INSTALLED WHEEL
  in an empty cwd. The /tmp build copy must be driven BY the pyproject py-modules list,
  never by a hand-remembered file list.

## PERMANENT RULES (from v0.1.0, unchanged)

- **Rule A:** Registry primitives are the single source of truth for canonical values.
- **Rule B:** One dispatch per whitepaper; no dispatch without a whitepaper.
- **Rule D:** OPEN over SM — never substitute a classical formula for a missing
  UQFF derivation (subject to the two-tier test above).
- **Rule E:** Predecessor repo (github.com/Daniel8Murphy0007/Star-Magic) is
  READ-ONLY reference. Never commit there. It contains 4+ prior calculator
  attempts — study them for physics content only, never port their code.

## SELF-RECTIFICATION DOCTRINE (Daniel's design intent)

Elements wired slightly off early WILL resolve as the corpus compiles — papers
carry extensive cross-references, and later landmarks canonize earlier
empirical values (e.g., PAPER_001's 0.333 → PAPER_2154's 1−D_phys/D_BSFG).
When a later paper supersedes an earlier wiring: update the dispatch, keep the
old value in the registry row's history via a supersession note, tighten the
gate assertion, log it in SESSION_LOG. Convergence is the goal, not first-pass
perfection.

## HARD-WON STANDING LESSON (2026-08-31): SOURCE-VERIFIED RULINGS ONLY

Daniel's catch, verbatim context: batch ruling questions were being built from
RULINGS_QUEUE summaries without re-reading the papers, and one summary had
mischaracterized PAPER_005 (called it the "linear outlier" when its L62 states
the squared convention). RULE: no ruling question goes to Daniel without (1)
re-reading the source paper, (2) verbatim quotes with file:line citations,
(3) independent recomputation of every number in the claim. Ledger entries
are leads, not evidence. Full audit pattern: BATCH_1_VERIFICATION.md.

## HARD-WON STANDING LESSON (2026-08-31): THE FULL-WHEEL RULE

Daniel's ruling, verbatim: "EVERY SHIP SHOULD BE ON THE WHEEL." The
v0.394.0-v0.408.0 publication split happened because the ship-integrity
guard verified git-side completeness and the wheel guard verified
declared-module completeness, and NO GUARD tied repo contents to the wheel
manifest - fifteen versions of green gates while the registry, rulings
ledger, whitepapers, commercial docs, and incorporation PDFs never reached
PyPI. RULE: the data-files manifest is GENERATED (generate_wheel_manifest.py,
run at every ship prep), never hand-curated; SHIP GUARD v8 enforces
repo<->wheel coverage; the only exclusions are structural (py-modules,
package dir) and confidentiality (untracked operator tier). Guard the SEAM
between guards: any property enforced on two sides separately is unenforced
in the middle.
