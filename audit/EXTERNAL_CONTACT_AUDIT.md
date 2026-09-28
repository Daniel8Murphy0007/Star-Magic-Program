# EXTERNAL CONTACT AUDIT — where has the corpus met outside data with a prediction stated first?

**Prepared for:** Daniel T. Murphy, at his request ("NOW FOR THAT AUDIT YOU MENTIONED, BEFORE I THROW ALL OF THIS AWAY"), 2026-09-17.
**Scope:** the 2,328 whitepapers in `whitepapers/`, the registry (7,141 rows), and the four NS-arc fronts, as of v0.442.0.
**Question asked:** not "does the calculator reproduce the papers" (it does — 6,115 gate assertions say so) but "where has a paper committed to a number *before* nature was asked, and what happened when nature answered."
**Method:** every table in the corpus whose header names an outside source (Observed / Experiment / PDG / Planck / NIST / Measured …) was extracted (1,267 tables in 1,161 papers). 1,064 of them are one boilerplate template; the other 205 (in 165 papers) were classified row by row against a fixed rubric by three independent readers, then 140 of the 880 classified rows (16%) were re-checked by me against the source text. All 140 matched. Every number in this report is reproducible from the scripts in this folder.

---

## 1. The verdict in one paragraph

The corpus contains exactly **four** tests in which a number was written down, committed, and then compared with data that could have come out otherwise. Two of them (fronts 1 and 2 of the NS proof set) returned "consistent, but the data cannot reach the discriminating region" — they were not able to fail. The other two (front 4 on water, Q-251 on argon) were able to fail and did: water landed 49% above the prediction, argon 22% below, and the measured cutoff tracks the molecular diameter, not the SCm carrier. Every other numerical agreement in the corpus — and there are thousands — was obtained by choosing the formula *after* the target value was known, from a vocabulary of primitives rich enough that a random number can be matched to 1% with a three-primitive product 78% of the time and to 2% almost always. That is not fraud and it is not nothing; it is curve-description, and the corpus has systematically labelled it "prediction," "EXACT," "closure," and "PASS." The honest inventory is: zero pre-stated positive results; two pre-stated negatives; a large, well-engineered, internally consistent calculator; and a set of untested forecasts for future experiments that are the only remaining falsifiable content.

---

## 2. The tier scheme used

| Tier | Meaning | What it can establish |
|---|---|---|
| **T0 — INPUT_REPRODUCED** | The "UQFF value" is the observed value, an anchor, a calibration, or a quantity defined from the observed one. | Nothing (circular). |
| **T1a — POST_HOC_PER_TARGET** | A different combination of primitives is offered for each observable in the table, chosen with the target in view. | Descriptive fit; strength depends on the look-elsewhere density (§5). |
| **T1b — POST_HOC_FIXED_FORM** | One stated form, compared with data after the fact; may still carry a fitted prefactor or exponent. | Consistency, not prediction. |
| **RANGE_ONLY** | Compared with a bound, a band, a qualitative statement, or an order of magnitude. | Non-exclusion. |
| **FORECAST_UNTESTED** | A number for an experiment not yet performed. | Falsifiable content, unrealised. |
| **NOT_A_COMPARISON** | No external value in the row. | — |
| **T2 — PRE-STATED** | The number and the pass/fail rule were committed before the data were looked at. | A real test. |
| **T3 — PRE-STATED AND PASSED** | T2 with a positive outcome. | Evidence for the framework. |

---

## 3. Part A — the boilerplate template (1,064 papers, 4,108 rows)

The table headed `Observable | UQFF Prediction | SM / Experiment | Source | Alignment` appears in **1,064** whitepapers. It is a template: **2,129** of its 4,108 rows are the same four lines (Cosmological constant Λ ×622, Proton decay rate ×617, UQFF buoyancy signature ×616, Fine-structure α ×612), and the rest are a handful of PDG constants (sin²θ_W ×143, m_H ×92, m_Z ×68, σ_T ×58 …).

Alignment column census: **PASS/Consistent 2,231**, **Testable 698**, numeric percentages **947** (of which "99.9%" ×336, "99.6%" ×162, "99.8%" ×138), "100% (exact QED input)" ×55.

What these rows are: Λ is compared against Λ_Planck with the UQFF value *being* the Planck value or 6/5·SSq = 0.684 vs Ω_Λ = 0.685; α is "Ug1 dipole coupling — PASS" with no number; proton decay is a bound; the buoyancy signature is "not yet measured — Testable". **None of the 4,108 template rows is a test.** They are a compliance stamp (the "G6 SM Anchor Gate") and should be read as such. Tier: T0 / RANGE_ONLY / FORECAST_UNTESTED throughout. Script: `template_census.py`.

---

## 4. Part B — the 205 genuine comparison tables (165 papers, 880 rows)

Full row-level classification: `EXTERNAL_CONTACT_AUDIT_ROWS.csv` (909 lines: 880 rows plus 29 whole-table entries). Rubric: `rubric.txt`.

| Class | Rows | Share of comparisons |
|---|---|---|
| POST_HOC_PER_TARGET (T1a) | **287** | 34% |
| RANGE_ONLY | 234 | 28% |
| POST_HOC_FIXED_FORM (T1b) | 155 | 18% |
| FORECAST_UNTESTED | 97 | 12% |
| INPUT_REPRODUCED (T0) | 74 | 9% |
| NOT_A_COMPARISON | 62 (29 whole tables + 33 rows) | — |
| **PRE-STATED (T2)** | **4** (fronts 1, 2, 4; Q-251 — §6) | <0.5% |
| **PRE-STATED AND PASSED (T3)** | **0** | 0% |

Findings that recur across the 165 papers (each with file:line in the CSV):

**Identical-digit "predictions" (82 rows flagged).** The UQFF value equals the observed value to every printed digit. Examples: PAPER_021 L254 s8 = 0.762 vs 0.762±0.012; PAPER_027 L303 two LFV branching ratios equal to the LHCb *bounds* to all digits, each with its own exponent (3.833, 3.900); PAPER_028 L408 |V_cb| "Exact" — where [SCm]_flavor is *defined* as |V_cb|²; PAPER_1181 L73 r_p = 0.8409 fm "exact" with exponent D_phys·D_phys+β chosen for that row, m_e = 0.5110 "exact" from a bare fitted exponent 10^−0.293; PAPER_1209HH L11 top/bottom/charm/tau/muon/strange/electron masses all printed identical to observed yet assigned nonzero residuals (0.5%, 1.0%, 1.6% …); PAPER_1165 L76 β_2, β_3, β_4 "0.000%" against values that are the framework's own parameters; PAPER_1919 L247 muon g−2 "EXACT" for 2.298e-9 while PAPER_1858 L19 reports the same 2.298e-9 at 8.44% off the same measurement.

**Per-target formula selection (287 rows).** The clearest cases are the suites: PAPER_1181 (29 rows, a different primitive product per constant, exponents such as 122 and D_phys·D_phys+β chosen per row), PAPER_1858 (23 g-factors), PAPER_1866 (16), PAPER_1861 (14 hadron masses), PAPER_1859 (12), PAPER_1863 (12 superconductors: LaH₁₀ gets `T_base·(K_MEX+D_phys)·SSq·(1+F_TRZ)²·K_MEX/(K_MEX+F_TRZ)`, H₃S gets `T_base·(K_MEX+SO_5·SSq/K_MEX)·SSq·(1+F_TRZ)²`), PAPER_1846 (12 lifespans). The same primitive combination F_TRZ²·SSq·Φ_res/K_MEX = 2.298×10⁻³ serves as |ε_K| (PAPER_1849, 3.15%) and, multiplied by F_TRZ⁷·SO_5, as Δa_μ (PAPER_1919). Section 5 quantifies what such agreement is worth.

**Misses reported as passes (21 rows flagged).** PAPER_025 L134 σ/m = 0.57 vs bound < 0.47, "Marginal"; PAPER_1184 L57 Perseus L_X off by a factor 170, "cooling-flow boost"; PAPER_1187 L45 M87 Ṁ 20–80 vs ≲0.1 M☉/yr, "within isobaric ceiling"; PAPER_1185 L51 GW150914 strain 3× low, ✓; PAPER_1839 L38 deep-sleep Φ 0.208 vs 0.24–0.31, ✓; PAPER_1835 L44 angular precision 35% off, "within range"; PAPER_1921 L133 M33 f_DM 0.80 vs 0.85–0.90, "12% high"; PAPER_072/065 RDR-004 18% deviation, "ACCEPTABLE"; PAPER_1889 protein folding Villin three orders of magnitude off, starred.

**Sources that are not measurements (T0 disguised).** PAPER_068 L66 "measured" f_Z from ROMULUS25 (a simulation); PAPER_065 L104 "measured" values of Layer-13 and Layer-26 [SCm] (internal quantities); PAPER_1169 L137 four "measured prefactors" at 0.0833±0.0004 which are fits *of the UQFF form itself* to archival light curves; PAPER_072 RDR/QSC rows (reactor COP, THz amplitude) with no provenance at all, repeated in three papers; PAPER_1181 L73 S294 "observed" neutron non-β branching 1.121% inferred from the beam–bottle gap, not measured.

**Anchors and calibrations labelled as predictions.** H₀ = A_5+SO_5 = 70 (PAPER_1573) sits between Planck 67.4 and SH0ES 73.0 and is then used both ways (PAPER_1181 L208 derives 67.19 and 72.79 from it via √(13/12)); N_eff = 3.046 "match"; T_BEC "calibration 5.0 MeV ✓"; V_cb "PDG anchor 100% ✓" (PAPER_494).

**Internal inconsistencies between papers.** LFU R = 1.020 (PAPER_028 L303) and 1.000 (L408); Σm_ν = 74.2 meV (PAPER_026 L231/L327) and 0.0764 eV (L293); η_B two variants (GUT/TeV) in the same table; Δm²₃₁ observed 2.51e-3 in one row and 2.453e-3 in another; Λ compared once against Planck 2018 (0.002%) and once against Planck+DESI 2025 (2.2%) with the same prediction.

---

## 5. Part C — what a 1% match is worth: the look-elsewhere density

Script: `look_elsewhere.py`. Primitives used: D_PHYS=4, SO_5=10, D_CRIT=26, D_BSFG=6, A_5=60, β_i=0.6029, F_TRZ=0.1, SSq=0.57, K_MEX=25/12, Φ_res=5/6 and 0.84 (both are used in the corpus).

**Restricted vocabulary** — products of at most three primitives with exponents ±1, no prefactors, no sums (narrower than any suite in the corpus actually uses): **1,050 distinct numbers**. For a random target drawn log-uniformly in [0.01, 100]:

| Tolerance | Fraction of random targets matched |
|---|---|
| 0.5% | 56% |
| 1% | 78% |
| 2% | 97% |
| 5% | 100% |

**Corpus vocabulary** — up to three primitives with exponents ±1, ±2, one prefactor from {1, 2, ½, 3, ⅓, π, 4π, √2, e}, optional square root (still no sums, though the corpus uses sums freely, e.g. `2·(K_MEX+SSq)·(1+F_TRZ·SSq)`): **117,982 distinct numbers, ~23,000 per decade**. Every random target in [10⁻³, 10³] is matched to **0.1%**.

Consequence: a residual of 0.5%–5% between a per-target primitive formula and a known constant carries **no information** about the framework. The 287 T1a rows and most of the 155 T1b rows are expected at their observed hit rates under the null hypothesis that the primitives are unrelated to the observables. The only way such a formula becomes evidence is if it is written down *before* the target is known — which brings us to §6.

Note on the primitives themselves (Part D): the four integers (4, 10, 26, 60) are combinatorial; F_TRZ = 1/SO_5 and K_MEX = Φ_res·SO_5/D_phys are derived from them; SSq = 0.57 is a Star-Magic.txt Chapter-18 calibration constant whose three post-hoc "derivations" in PAPER_1154 land at +0.34%, −10.5% and −2.0% (the paper calls this "unique"); Φ_res takes two values (5/6 in 72 papers, 0.84 in 121 papers), i.e. it is chosen per sector; ω_SCm = 2π·1.25 THz is asserted from PAPER_003 onward without derivation; and β_i = 0.6029 — the CLAUDE.md drift table forces every paper onto this value citing PAPER_1203 — **does not appear in PAPER_1203** (which has 0.603 and 0.65). The four-digit value first appears in **PAPER_1156 L332**, where it is the value that makes `SO_5·SSq·β_i/(D_phys·D_crit)` reproduce r_d·H₀/c from Planck+eBOSS to 0.0093%; the shift from 0.603 to 0.6029 is 0.017%, larger than the residual claimed. β_i was tuned to one cosmological datum and then canonised. Of the nine "independent primitives," then, three real numbers (SSq, β_i, Φ_res) are fitted or sector-selected, and the THz carrier is postulated.

---

## 6. Part E — the four pre-stated tests (the entire T2 list)

| Test | Where stated | Prediction committed | Outcome | Tier |
|---|---|---|---|---|
| Front 1 — the kill test | PAPER_2276 §6.1 | Stretching ratio never exceeds 17/20 = 0.85 in vacuum-branch turbulence | JHTDB isotropic samples sit at 0.02–0.11. Consistent; the tail where a violation would live was never reached (needs whole-volume token). **Could not fail.** | T2, non-discriminating |
| Front 2 — pair-cap discrimination | PAPER_2276 §6.2, PAPER_2279, PAPER_2280 | In-medium 197/200 vs vacuum 17/20 | Channel Re_τ 1000 and 5200: bulk 0.03–0.07, no trend; "DISCRIMINATED by neither" (PAPER_2279 L141). **Could not fail.** | T2, non-discriminating |
| Front 4 — η(k) cutoff in water | PAPER_2281 (re-specified), PAPER_2282 | k_c = ω_SCm/c_s: 5.31 nm⁻¹ (c₀) or 2.45 (c_∞); Gaussian roll-off | Record run (SPME, 3 seeds, 2 boxes): **k_c = 7.90 ± 0.05 nm⁻¹** — +49% vs c₀, ×3.2 vs c_∞. Existence and Gaussian shape positive; coefficient **CLOSED NEGATIVE**. | T2, **failed** |
| Q-251 — argon | RULINGS_QUEUE Q-251 (committed before the run), PAPER_2283 | Water/argon k_c ratio = 1.489 (P1) or D_BSFG/D_phys = 1.5 (P2); NIST c₀ 854.35 m/s | Measured k_c = 7.17 ± 0.05 nm⁻¹; ratio 1.10 → P1 0.78, P2 0.52: **NEITHER, CLOSED NEGATIVE.** k_c·σ = 2.50 (water) / 2.44 (argon): the cutoff tracks σ, not ω_SCm. | T2, **failed** |
| Front 3 — THz bench | PAPER_2276 §6.3 | Water absorption line at 1.25 THz, FWHM 0.235 THz | Not performed (needs THz-TDS ATR). | FORECAST |

These four are the only places in 2,328 papers where the number was on the table before the data were. The two that could discriminate did, against the framework. Note the positive residue honestly: front 4 *did* find a Gaussian η(k) roll-off with a finite cutoff in both fluids, which is real physics (and not new: generalized-hydrodynamics studies of simple liquids have long found η(k) falling off on the scale of the inverse molecular diameter, which is what k_c·σ ≈ 2.5 in both fluids says). The measurement is good; the attribution to the SCm carrier is what failed.

What is *not* on this list, and why: PAPER_1169 ("Numerical Confrontation P1–P5 With Archival Data") fits a prefactor of the UQFF form to archival light curves and reports the fit equals 0.0833 — that is a fit, T1b. PAPER_2161 ("Near-Term Falsifiability Battery") and PAPER_1174 ("P6–P10") state kill criteria for future experiments — genuine T2 statements, but untested (§7). PAPER_1181 L244 lists eleven falsifiers, all future.

---

## 7. Part F — the untested forecasts (97 rows): the remaining falsifiable content

These are the only claims that can still turn into T3. Grouped by when a result could exist:

**Already measurable or being measured now (a result could be obtained within the year):**
- Muon g−2: Δa_μ = 2.5065×10⁻⁹ with "drift > 0.3σ kills" (PAPER_1181 L244 #9) — but the framework also carries 2.298×10⁻⁹ (PAPER_1858/1919). Fermilab's final result is published; pick one value first, then compare.
- w_DE = −1 exactly, no time variation; |1+w| > 0.02 kills (PAPER_1181 #11, PAPER_1174 P7). DESI DR2 is out. This is a live test — and it is also exactly ΛCDM, so a pass does not distinguish UQFF.
- Neutron non-β branching 1.140%; outside [1.0%, 1.3%] kills (PAPER_2161 #4, PAPER_1181 #4).
- BR(μ→eγ) = 1.27×10⁻¹³ vs MEG-II (bound 4.2×10⁻¹³); exclusion below 1.0×10⁻¹³ kills (PAPER_2161 #3).
- Sub-mm Yukawa L_KK 20–90 µm (PAPER_1174 P6, PAPER_1173) vs torsion-balance bounds already at > 48–56 µm.
- σ₈/S₈ residual 0.04% at the √26 ratio; > 1σ tension kills (PAPER_1181 #10) — Euclid/DESI.
- Front 3 THz line at 1.25 THz, FWHM 0.235 THz (PAPER_2276) — a bench measurement, no collaboration needed.

**Future facilities (2027–2050):** JWST Δμ(z=6) = +0.015 mag; LISA Ω_GW(0.37 mHz) = 2×10⁻¹³; IceCube-Gen2 g ≤ 0.185; sterile M_s1 = 7.1 keV line at 3.55 keV with 2.6 eV width (XRISM); m_ββ = 12.3 meV (CUPID-1T); τ g−2 and EDM at Belle II/FCC-ee/CLIC; κ_λ = 1.0 EXACT at HL-LHC; VLQ cross-sections; Li-7 and ⁶Li/⁷Li at ELT.

Several of these forecasts coincide with the Standard Model / ΛCDM expectation (w = −1, κ_λ = 1, Y_p depletion exactly zero, N_eff 3.046), so a pass would not be evidence *for* UQFF, only a non-failure.

---

## 8. Verdict and options

**What the 13 months built, honestly stated:**
1. A calculator that reproduces 2,279 papers' stated numbers to their stated precision, with a 6,115-assertion gate, a generated wheel manifest, a tag-chain guard, and a rulings ledger. This is real engineering and it is what made §6 possible: the negatives are clean *because* the discipline existed.
2. A working SPME water engine and LJ argon engine with a validated Green–Kubo η(k) pipeline (Madelung 1.2×10⁻⁷, NVE drift 10⁻⁴, η₀ within 2% of literature, D within 2%) — publishable methods in their own right, independent of UQFF.
3. Two clean pre-registered negative results on the framework's one sharp, distinctive claim.
4. Zero pre-registered positive results.
5. ~440 post-hoc numerical agreements (T1a+T1b) that §5 shows are expected by chance at the observed hit rates, plus ~230 non-exclusions against bounds, plus 4,108 template rows that are not tests.

**On "not salvageable":** the *framework's* central claim (the 1.25 THz carrier setting fluid cutoffs) has been tested and has failed; the *numerological* content (primitive products matching constants) has no evidential weight and cannot acquire any retroactively. What remains falsifiable is §7, and about half of it can be checked against data that already exists. That is the honest test of whether anything is salvageable: pick the three or four §7 items that are decidable now (Δa_μ — after choosing one value; w_DE from DESI DR2; neutron BR; L_KK vs the existing torsion bounds), write the pass/fail rule in RULINGS_QUEUE *before* looking, and grade them. If they fail too, the record is complete and closing the project is the correct scientific outcome, not a waste — a documented negative with the tooling to reproduce it is worth more than 2,000 unfalsifiable agreements. If any passes with a value that differs from the SM/ΛCDM expectation, that is the first T3 in the corpus and the thing to build on.

**What I would not do:** ship another band of T1a papers; re-derive β_i, SSq or Φ_res to recover the water/argon coefficient (that is the per-target selection of §4 applied to the one test that was clean); or re-open front 4 under Q-252 without first ruling whether a "different object" reading is a prediction or an accommodation.

---

## Appendix — files in this folder

- `EXTERNAL_CONTACT_AUDIT_ROWS.csv` — 909 lines; columns `paper|table_line|quantity|uqff_value|external_value|external_source_named|residual_as_stated|class|evidence`.
- `rubric.txt` — the classification rubric given to each reader.
- `look_elsewhere.py` — §5 computation (runs in seconds, no dependencies).
- `template_census.py` — §3 census of the boilerplate table.
- `spotcheck.txt` — the 140 sampled rows with the matching source lines.

Standing rules observed: no version bump, no new band, no rulings folded; Q-252 remains Daniel-gated. Nothing in this audit changes any dispatch, registry row, or gate assertion.
