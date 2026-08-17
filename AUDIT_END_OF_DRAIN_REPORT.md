# AUDIT_END_OF_DRAIN_REPORT — The Corpus Drain Complete: PAPER_001 → PAPER_2156

**Generated:** 2026-08-16 | **Version at audit:** v0.381.0 (shipped) + audit-repair trail |
**Gate at audit:** 5,602/0 entering; repairs added in-audit (see §7) |
**Charter authority:** decision C (end-of-drain audit at corpus completion), agreed in-session and
gate-pinned since the AUDIT_1910 cadence restoration.
**Scope:** the entire campaign, PAPER_001 (v0.3.0, 2026-07-28) → PAPER_2156 (v0.381.0, 2026-08-16),
plus the 19 in-flight landmarks (PAPER_2160-2178) and 34 non-numeric keys.

---

## 1. FINAL COVERAGE CENSUS (live-computed this date)

| Metric | Value |
|---|---|
| Dispatches | **2,208** |
| Numeric papers 001-2159 | **ALL dispatched except exactly [1796, 1797, 1798, 1799]** (RESERVED placeholders — correct absence, gate-pinned) |
| Landmarks 2160-2178 | 19/19 wired |
| Non-numeric keys | 34 (b-variants, 1209 letter tiers, 376b, Phase-H pentad) |
| Execution errors across all 2,208 | **0** (342 early-era dispatches take positional `dataset`; all execute clean) |
| Index consistency | 0 wired-but-⬜ rows |
| OPEN (None-valued) dispatches | 0 at top level (all prior OPENs resolved or disclosed in-formula) |

## 2. RESIDUAL DISTRIBUTION (all 2,196 dispatches carrying a top-level residual field)

| Bin | Count | Reading |
|---|---|---|
| = 0.0 | 1,704 | MIXED BIN (honest label per AUDIT_1910 §2): true EXACT identities + structural/meta papers + suites carrying per-observable residuals inside the value dict |
| < 0.01% | 89 | precision tier |
| 0.01–0.1% | 167 | |
| 0.1–1% | 149 | |
| 1–5% | 54 | disclosed dressings |
| ≥ 5% | 33 | weakest members |
| **Median nonzero** | **0.086%** (n = 492) | |

**Worst five, disclosure-audited:** P013 117.6% (braking-index envelope — was UNDISCLOSED,
Rule 7 disclosure added in this audit), P1805 45% (disclosed), P186 39.8% (four-body structural
estimate — was UNDISCLOSED, disclosure added), P1835 34% (disclosed), P1866 28% (disclosed).
After repair: **all ≥5% members carry in-formula disclosure.**

## 3. DISCIPLINE CENSUS (machine-counted, in-formula)

FAMILY notes 231 · Rule 7/disclosure language 251 (253 after this audit's two additions) ·
prediction/falsifiability markers 97 · `_seq` renames 17 · FAMILY_RECORD rows in DUPLICATES 54
(incl. the TERMINUS_RECORD). Registry 6,618 rows; graph 12,047 edges.

## 4. FORENSIC CLOSURE: THE 9.47e-27 / 5.0e-27 DENSITY ORIGIN (PAPER_2156 open target — RESOLVED)

**Finding:** 9.47×10⁻²⁷ kg/m³ = ρ_crit = 3H₀²/8πG at **H₀ = 71.00 km/s/Mpc** (match to 0.004%).
The "unknown-origin" density that the Session-204 bulk script injected as "RHO_SCM" into 935
papers **is the SM critical density of the universe** — present in-corpus explicitly as
`RHO_CRIT = 9.47e-27 kg/m3` in PAPER_495 (Cosmic Quantum Egg) and reused by the script under
the wrong name. The companion 5.0×10⁻²⁷ corresponds to no natural H₀ (would need 51.6) and is
concluded a round-number placeholder; 9.47/5.0 = **1.894 exactly** — the drift ratio's full
ancestry: SM ρ_crit(H₀=71) ÷ round-number → "VDS ratio" → 935 papers.

**Three-layer confirmation of PAPER_2156's ruling:** the artifact was (a) SM-sourced (Rule 4
contamination at script level), (b) carried a non-canonical H₀ = 71 (vs A_5+SO_5 = 70), and
(c) correctly superseded by F_TRZ = 0.1 without retrofit. The forensic question is CLOSED;
the calculator's two knowingly-drifted anchor sites (P495-family ω_egg, P1090 anchor) already
carry PAPER_2156 flags in-comment.

## 5. THE NUMBERING MIRROR — SYSTEMATIC, MECHANISM DOCUMENTED

Six confirmed pairs — 2093 (H₀ ladder route), 2094 (Λ pure-primitive), 2112 (κ reduction),
2125 (Two-Kernel), 2129 (Φ_5/6 sector rule), 2130 (Unified Registry Program) — carry the same
physics at the same paper number in both repos, against one counterexample (2118). Bands
2131-2156 resolved the mechanism: **the two repos share one whitepaper lineage** — this corpus's
2131-2156 ARE the predecessor CLAUDE.md's key-papers table and 2026-07 audit-arc appends,
verbatim. The mirror is not coincidence but common ancestry; the counterexample (2118) marks
where the lineages forked. No further action required; recorded as settled corpus history.

## 6. ROUTE-FAMILY CROSSING REVIEW (PAPER_2170 doctrine, exercised at scale)

54 FAMILY_RECORD rows reviewed by class: tilt two-route (K_Mex−2 vs F_TRZ·Φ_5/6 — both EXACT,
crossing = 0, coexist), Schwinger three-route (P2013/P2071/P2126), H₀ family (CLOSED with
supersession, P2144), Λ two-route (dual-manifestation per P2153 — physics, not defect),
d_n batteries (A4-protected), plus per-band seq/crossing records. **Verdict: the doctrine held**
— no family was silently reconciled, no crossing was averaged away, and the two closures that
did occur (H₀, 7.09-identity) came from corpus papers, not session judgment.

## 7. WHAT THIS AUDIT CAUGHT AND REPAIRED (the systemic finding)

1. **LEDGER-COVERAGE guard was substring-based** — incidental mentions of a paper key in other
   rows' fields masked missing rows. 4 registry rows (P437/642/1039/1071) and 25 citations rows
   (proof-set era 1133-1236) existed as mentions but not as rows. **Repaired** (LEDGER_REPAIR-
   marked) and the **guard tightened to column-anchored parsing** with zero-padding fallback.
2. **Two undisclosed worst-tier residuals** (P013 117.6%, P186 39.8%) — Rule 7 disclosures
   added in-formula.
3. Systemic continuity: every structural failure in campaign history (v0.358.0 partial
   protocol, the missed milestone stops, and now substring-matched guards) is the same species —
   **a verification that checks a weaker proxy than the thing it certifies.** The repair pattern
   is likewise constant: strengthen the check to measure the real thing, live.

## 8. RULINGS LEDGER FINAL STATE

53 sections; 38 carry RESOLVED/DISSOLVED/CLOSED markers (39 with §4's forensic closure).
Open non-blocking, all queued with owners: Kerr F_TRZ-coefficient mechanism; category-regime
correlation; π-canonical dedicated landmark; Schwinger two-route reconciliation; design-choice
locking scope; build-intermediate deletion (Daniel's call); rare-earth A≈165; cuprate layers;
CGM tower; P1900 factor origin; Ug4 bridge; ℓ_n = D_phys·T_n; n/(D_phys−1) extensions; P2134
DPM pair-count estimator (OPEN build target); PAPER_2147's 13.4% ρ_Λ Interpretation A-vs-B
(distinguishing experiment). None silently filled (Rule D honored corpus-wide).

## 9. CAMPAIGN TOTALS (charter retrospective)

- **20 days**, v0.3.0 → v0.381.0, ~80 shipped releases, PAPER_001 → PAPER_2156 strictly
  sequential with in-flight landmark authoring (2160-2178).
- Milestone audits: AUDIT_500 → (lapse, Daniel-caught) → AUDIT_1910 → AUDIT_2000 (FULL STOP,
  Daniel-authorized continuation) → **this report**. Cadence obligations: all discharged.
- Honesty machinery: 253 in-formula disclosures, 17 `_seq` renames, 54 family records,
  2 OPEN-then-resolved values, banned-literal guard with multiple live catches, 4 in-corpus
  retraction/withdrawal honorings, one walkback wired as its own disposition (P2145).
- Prediction battery: 30 programs / 56 members, A4-dated; 3 predictions converted to
  postdictions in-campaign (exponent-21, slot-9 quenching, magnetar lobes 2/2); live
  falsifiers standing (4U 0142+61; DM morphology dichotomy; SMBH flare grid; JWST/Roman
  40-lens 1.0881; ν=5/2 shot noise; next-kilonova 5-day peak; H₀ → 70 window).
- **Every structural failure was caught by an audit; three of five audit triggers were Daniel.**
  The closing state inverts that ratio's lesson: the checks that now stand measure the real
  quantities live, so the next lapse cannot stay invisible.

## 10. DISPOSITION

The charter's mission — "condense all 2,255 whitepapers into `uqff_calculator.py` + the
registry pantheon" — is **complete for the numeric corpus**, with the census, the terminus,
and this audit's repairs all gate-pinned. Remaining work is by-request only: open-item
derivation sessions (§8), the build-intermediate deletion decision, and any future landmark
authoring. The corpus self-rectification doctrine performed as designed: later papers
corrected earlier wirings 6 times (P1908, Tier-II anchor, P2144 H₀, P2145 walkback, P2154
FWHM, P2156 ratio) with zero manual physics interventions.

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.
