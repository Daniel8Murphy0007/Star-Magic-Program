# WHITEPAPER AUDIT — every paper in the corpus, read and recomputed

**Prepared for:** Daniel T. Murphy, 2026-09-17.
**Scope:** all 2,328 whitepaper `.md` files in `whitepapers/` (PAPER_001 … PAPER_2283 plus the reference/SCm/Star-Magic documents). Every file was read in full by a reader; every headline number was recomputed in Python from the paper's own stated equation and inputs. This is the second, deeper pass you asked for — not a survey.
**Companion data:** `WHITEPAPER_AUDIT_ROWS.csv` — one row per paper (paper_id, claim, claim kind, where the inputs came from, derivation status, the recomputation and whether it matched, external comparison, chain fidelity, own-content fraction, defects, verdict, line-cited evidence). `CONSTANT_DRIFT_TABLE.csv`, `EXTERNAL_CONTACT_AUDIT.md`, `THE_RECORD_WHERE_AI_FAILED.md`, and `INSTRUCTION_FIDELITY_LEDGER.md` are the earlier passes this one confirms at full corpus scale.

## Method

The 2,328 files were split into 83 batches. Each batch was read by a separate reader working from one rubric: identify the paper's headline claim; trace whether its inputs are chosen registry constants, values assumed in the text, outputs of the author's own code, a named measurement, or the target itself; recompute the headline number in Python; check for circularity (is the "prediction" also an input?); check whether any external comparison is to a real measurement made before the number was chosen or to boilerplate; check chain fidelity against your permanent rule that the DPM is first and GM/r² is last; and record every defect (lost exponents, mojibake, self-contradiction, unit errors). Verdicts were drawn from a fixed list. Nothing was softened. In parallel I ran all 2,334 wired dispatches in `uqff_calculator.py` and classified each one mechanically. The two methods agree.

## The result in one table

| Verdict | Papers | Share |
|---|---:|---:|
| SOUND — equation, inputs, recomputation and an independent comparison all hold | 13 | 0.6% |
| CALIBRATION_ONLY — the number follows from the chosen constants; agreement is by construction | 878 | 37.7% |
| DEFECTIVE — the stated result cannot be reproduced from the paper's own equation, or the paper contradicts itself | 547 | 23.5% |
| NARRATIVE — prose or symbolic, no checkable number | 288 | 12.4% |
| UNSUPPORTED — a checkable claim with no derivation and no way to reproduce it | 265 | 11.4% |
| CIRCULAR — the output is an input, or the "test" compares a value to itself / to the author's own code | 259 | 11.1% |
| STAMPED — the paper's own content is negligible; template plus a substituted number | 66 | 2.8% |
| ADMIN | 1 | — |

**Not one paper in 2,328 makes a validated, pre-stated prediction against an independent measurement.** The 13 marked SOUND (below) are honest, but none of them validates UQFF.

## What the 13 "SOUND" papers actually are

They fall in three groups, and every group is fatal to the framework's claims rather than supporting them:

- **Pure-math identities relabelled as physics** — PAPER_1508, PAPER_1700 (26! = 4.03×10²⁶), PAPER_1703 (a hyperconvergent sum). Correct arithmetic; zero physical content; no measurement involved.
- **Standard published astrophysics with the UQFF term negligible** — PAPER_1192 (Rankine–Hugoniot/Sedov shock velocity for Cas A) and PAPER_1194 (Stone–Metzger TDE rate). These reproduce because they are textbook formulas; the paper's own text says the "Aether correction" is ≤ 0.1%, i.e. UQFF contributes nothing.
- **Honest empirical tests that FAILED or came up untestable** — PAPER_2271–2273, 2277–2280 measured the framework's one sharp prediction (the η(k) stretching cap) against real JHTDB turbulence data and against a validated molecular-dynamics engine. The cap "holds" only by a 20–180× margin, which the papers themselves say means the specific value is untested. PAPER_2274 rigorously proves the predecessor's Navier–Stokes "proof" is false. And the sharpest pre-registered prediction of all — the k_c cutoff of water and argon (Q-251) — was measured and **closed negative** (PAPER_2282/2283): the cutoff tracks molecular diameter, ordinary generalized hydrodynamics, not UQFF. The one place the framework put a number on the table before the experiment, the experiment refuted it.

So the honest papers are the ones that disprove the framework or show it adds nothing; the numerous papers that "confirm" it are the ones that don't compute.

## The four failure modes, with the corpus's own words

**1. Calibration dressed as derivation (878 papers, 38%).** The dominant pattern: a known value is decomposed into a product of the chosen primitives (D_phys=4, D_BSFG=6, D_crit=26, A_5=60, SO_5=10, F_TRZ=0.1, [SSq]=0.57, K_MEX=25/12, β_i=0.6029, Φ_res=0.84), then labelled "EXACT, zero free parameters." Because SO_5=10 and F_TRZ=1/10 by definition, any power of ten locks automatically — several papers say so outright. PAPER_2046 (L92): "SO_5 = 10 as a decimal scaling constant." PAPER_1990: "This is definitional, not empirical … any power-of-10 value automatically satisfies the ladder." PAPER_1181 (§9) describes the actual method: "an algebraic search over integer-and-rational combinations of the eleven locked primitives until a closed form was found within published experimental error bars." PAPER_1209JJ ships the search script itself (`_uqff_program.py --search --max-terms 5 --tol 0.0003`). The framework's foundational constant is calibrated the same way: ρ_SCm × 26! × K_MEX = 5.957×10⁻¹⁰ reproduces the dark-energy density exactly because ρ_SCm was set so it would (PAPER_2067, PAPER_2240 concede this), and that "match" is separately admitted to be ~12.8% off the real Planck value, the 0.117% figure having been measured against a fabricated "Planck 2024" citation (PAPER_2147/2148).

**2. Numbers that don't come from their own equations (547 papers, 24%).** Recomputation fails, usually by many orders of magnitude, with the digits kept and the exponent lost. Representative: PAPER_086 Ug4 stated 3.35×10²² J/m³, its own formula gives 1.5×10⁻¹⁰³ (125 orders); the whole "1.053×10⁻³" MUGE family (PAPER_705–710, 759–802) prints one mantissa for objects whose masses differ by 40 orders; PAPER_1005 carries an erratum admitting the famous "1.736 GeV Yang–Mills mass gap" was a hardcoded magic number with no derivation that propagated to ~610 corpus locations; PAPER_1109's "630 eV" Holmlid result is off by 21 orders (E_phonon × S26 = 7.5×10²³ eV, not 751). Many "PASS" and "0.00%" labels sit on top of these.

**3. Circularity (259 papers, 11%).** The prediction is fed in as an input. PAPER_1239 "predicts" the NANOGrav strain by taking the observed 2.4×10⁻¹⁵ and multiplying by 1.0344. PAPER_1704 derives [SSq] from Ω_Λ while PAPER_1696 derives Ω_Λ from [SSq] ("reciprocal closure"). PAPER_1096's flagship "closure holds to 1e-10 across 11 domains" is a tautology because the second term is defined as the total minus the first. The Holmlid papers define a factor ξ ≡ 630eV/(E_phonon·S26·Φ) and then "derive" 630 eV.

**4. Your ontology rule, broken at scale.** 448 papers begin their master equation with GM/r² (or Schwarzschild 2GM/c², or a mass-primary M/r² relabelled "DPM mass gradient") — a direct violation of "THE DPM IS FIRST. GM/r² IS LAST … If any equation begins with GM/r² it is WRONG." Of those 448, only 90 are even calibration-consistent; 206 are also defective. Just 212 papers in the whole corpus honor DPM-first, and most of those have no dynamics to test.

## Where the external comparisons actually point

Of 2,328 papers, 912 compare to nothing, 757 to a named source only after the fact, 431 to the author's own other papers or code, 186 to boilerplate tables. Only 25 even attempt a comparison to a pre-stated named measurement — and **all 25 resolve to DEFECTIVE (9), CIRCULAR (6), CALIBRATION_ONLY (8), NARRATIVE (1) or UNSUPPORTED (1). Zero hold.** This is the same result the external-contact audit reached on the 909 comparison lines and the four T2 tests, now confirmed paper by paper across the entire corpus.

## The one encouraging thing, and it is not the physics

The most recent papers (PAPER_2144–2283) are where the framework finally tests itself against real data with a validated engine and pre-registered predictions — and they are the most honest documents in the corpus. They retract the water coincidence, prove a predecessor's Millennium "proof" false, document that 22 of 38 "predictions" were the measured value times a ~0.1% fudge (PAPER_2149), and find the JHTDB caps untestable. That machinery — a real MD engine, data you didn't choose, a number committed before the run — is the only part of the 21 months that did science. It returned a negative result. That is worth more than the 1,207 papers that returned "EXACT," because it is true.

## Bottom line

Read in full and recomputed, the corpus is 0.6% sound (and that 0.6% is math identities, textbook astrophysics, or your own falsification tests), 38% calibration by construction, and 61% either non-reproducible, circular, unsupported, or empty template. The pattern is uniform from PAPER_001 to PAPER_2283 and the tools said so themselves in dozens of errata and honest-assessment sections that were then overridden. The framework's numbers were fit to their targets or fail their own equations; the one prediction it made before an experiment, the experiment refuted. Nothing here is a defect in your ideas as ideas — it is a record of what the AI tools built on top of them.
