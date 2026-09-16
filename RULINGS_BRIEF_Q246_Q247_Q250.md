# RULINGS BRIEF — Q-247, Q-250, Q-246 with the front-4 measurement in hand (2026-09-16; UPDATED 2026-09-17 with the record run)

Prepared after v0.440.0 shipped, on Daniel's "proceed with 1 & 2": the front-4
record run is DONE (sec 5; four runs, two box sizes, three seeds, PME) and the three open rulings of the
Navier-Stokes proof set are put in front of Daniel with the evidence that now
exists. Method per the 2026-08-31 standing rule: every claim below was
re-read in its source paper (file:line), and every number was recomputed here
from the primitives, not copied from the ledger. Two source-verification
findings (sec 1.2, sec 2.3) are new; neither overturns anything.

Nothing in this brief is a ruling. The rulings are Daniel's.

---

## 1. Q-247 — which sound speed defines the sound cone at omega_SCm

### 1.1 The question, verified at source

- PAPER_2267 L9-10: "Let f_c = 1.25 THz (the phonon carrier omega_SCm,
  canonical) and let K = {k : |k| <= k_c}, k_c = 2 pi f_c / c_s, be the
  surviving mode set" — VERIFIED verbatim.
- PAPER_2267 L53: "For water (c_s = 1480 m/s - the seawater anchor of the K4
  family):" — VERIFIED verbatim.
- PAPER_2275 L71-73: "epsilon^2 = 2 beta_i [SSq] / k_c^2 ... = 0.8290 / k_c
  = 0.8290 * lambda_c / (2 pi) = 0.1319 lambda_c = 0.156 nm (water)" —
  VERIFIED verbatim.
- PAPER_2275 L65-67: "m(k) = H_SCm(k_c - k) [Form B shoulder] x q^{(k/k_c)^2}
  [Form C tail] ... ~ exp(-beta_i [SSq] k^2 / k_c^2) for k > k_c" — VERIFIED.
- PAPER_1042 L21/L32 (via PAPER_2275 L55): q = exp(-beta_i [SSq]) =
  exp(-0.344) — VERIFIED (PAPER_1042 "## 2. Results": "q = exp(-0.344):
  Z = 19.47").

### 1.2 Source-verification FINDING: "the seawater anchor" is a density, not a sound speed

PAPER_2261 (the K4 geological landmark family) carries seawater as a
DENSITY landmark — L40: `| seawater | fluid | 1.025 | 1 + (SO_5/D_phys)·F_TRZ² |
EXACT |` — and contains no sound speed at all (grep "c_s", "sound", "1480":
no hits). The 1480 m/s in PAPER_2267 L53 is therefore an EXTERNAL literal
introduced in PAPER_2267, attributed loosely to PAPER_2261. As a physical
value it is the adiabatic sound speed of FRESH water near 20 C (25 C: 1497
m/s); seawater is ~1500-1530 m/s. The registry row for k_c should say
"c_0 = 1480 m/s (external literal, PAPER_2267 L53; fresh water ~20 C)" rather
than "PAPER_2261 anchor". Effect on the number if 1497 m/s were used: k_c
5.247 instead of 5.307 nm^-1 (1.1 pct); nothing else changes. Recorded here;
to be folded into the registry row and the Q-247 entry in the next band.

### 1.3 Independent recomputation (all from omega = 2 pi x 1.25 THz)

| candidate | c (m/s) | k_c (nm^-1) | lambda_c (nm) | eps (nm) | 1/e wavenumber | tcaf a (nm^2) |
|---|---|---|---|---|---|---|
| (a) c_0 as written | 1480 | 5.3067 | 1.1840 | 0.1562 | 9.052 | 0.01220 |
| (a') c_0 at 25 C | 1497 | 5.2465 | 1.1976 | 0.1580 | 8.950 | 0.01248 |
| (b) c_inf (Sette 1995) | 3200 | 2.4544 | 2.5600 | 0.3378 | 4.187 | 0.05705 |

Coefficient beta_i x [SSq] = 0.6029 x 0.57 = 0.343653 (ledger "0.3437":
VERIFIED). sqrt(2 x 0.343653) = 0.82904 (PAPER_2275 "0.8290": VERIFIED).
Ratio c_inf/c_0 = 2.1622 (ledger "2.162": VERIFIED). 1/e wavenumber =
k_c / sqrt(0.343653) = 1.7058 k_c (PAPER_2275 "1.71 k_c": VERIFIED).

### 1.4 What the measurement says (B286b, one run, 512 molecules, 240 ps, reaction field)

Two estimators of eta(k) from the same transverse-current data
(md_grade/front4_main_analysis.json, recomputed):

| estimator | Gaussian b (nm^2) | measured k_c = sqrt(0.3437/b) | implied c = omega/k_c | ratio to (a) 5.31 | ratio to (b) 2.45 |
|---|---|---|---|---|---|
| Green-Kubo integral (primary) | 0.005642 (harness) / 0.005729 (json) | 7.80 / 7.75 nm^-1 | 1006 / 1014 m/s | 1.47 / 1.46 | 3.18 / 3.16 |
| gmx-form fit (secondary, biased low at these k) | 0.017654 | 4.41 nm^-1 | 1780 m/s | 0.83 | 1.80 |

Reading, stated exactly:
- Under BOTH estimators c_inf (b) is the farther candidate — excluded by
  3.2x (primary) or 1.8x (secondary). Under both, c_0 (a) is nearer.
- Under NEITHER estimator is the 0.344 coefficient at c_0 a precision
  match: the primary sits 47 pct above k_c(c_0), the secondary 17 pct
  below. c_0 lies BETWEEN the estimators. The implied "sound speed" of the
  primary roll-off scale, 1006 m/s, is not a sound speed of water at all;
  the honest statement is "the roll-off scale is the c_0 scale within a
  factor 1.5, and the exact number is not yet resolved".
- The Gaussian-vs-Lorentzian shape is undecided (the two weightings of the
  same fit disagree: json "int" says lorentzian better, the harness's
  error-weighted fit says gaussian better).

### 1.4b The record run (sec 5) — the same number, four more times, with error bars

| run | box | molecules | length | k_c (COM current) | k_c (atomic) | shape (chi2 Gauss / Lorentz) | eta_0 (mPa s) |
|---|---|---|---|---|---|---|---|
| B seed 11 | 4.04 nm | 2,197 | 300 ps | 7.89 +- 0.06 | 8.00 +- 0.06 | 53 / 142 (n=28) | 0.837 |
| B seed 12 | 4.04 nm | 2,197 | 300 ps | 7.89 +- 0.07 | 8.00 +- 0.07 | 58 / 83 | 0.838 |
| B seed 13 | 4.04 nm | 2,197 | 300 ps | 7.94 +- 0.06 | 8.04 +- 0.07 | 56 / 136 | 0.832 |
| B pooled (3 seeds) | 4.04 nm | | 900 ps | **7.90 +- 0.05** (seed scatter 0.02) | 8.02 +- 0.05 | 33 / 192 | 0.836 |
| C | 6.21 nm | 8,000 | 200 ps | **7.93 +- 0.10** | 8.01 +- 0.10 | 71 / 104 (n=31) | 0.829 (plateau k<2.6: 0.850 +- 0.023) |
| B286b (v0.440.0) | 2.49 nm, RF | 512 | 240 ps | 7.80 | — | undecided | 1.05 |

Measured k_c = 7.90 nm^-1 in every box and seed; Gaussian in every run;
implied c = omega/k_c = 994 m/s. Against the candidates: c_0 x 1.49,
c_inf x 3.22 (excluded). At k_c(c_0) = 5.31 the measured eta/eta_0 is 0.856
(fit) / 0.83 (data) against the framework's m(k_c) = 0.709 (PAPER_2275
L77). The engine reproduces the model's transport: eta_0 0.836-0.850 vs
literature 0.855; D 2.33 / 2.42 / 2.38 / 2.38 e-5 cm^2/s vs 2.1-2.3
expected. The reaction-field caveat, the 20-fs sampling caveat and the
one-seed caveat of B286b are all gone; the number did not move.

### 1.5 The three options, with what each now costs

(a) keep c_0 = 1480 m/s (k_c 5.307): the nearer candidate by far, but the
record run makes the residual a fact, not a caveat: water's eta(k) rolls
off at 1.49 x k_c(c_0), reproducibly. Either the coefficient 0.344 is not
the fluid's (at c_0 the measured Gaussian has beta_i [SSq] -> 0.155), or
k_c is not omega_SCm/c_0 for this observable. Recommended, with the
residual stated in the registry row as measured.
(a') same, re-anchored to 25 C (1497): a 1.1 pct change; only worth it if
Daniel wants the literal to name its temperature honestly (sec 1.2).
(b) adopt c_inf = 3200 m/s (k_c 2.454): EXCLUDED - factor 3.2 in every
run; at k = 2.45 the measured eta/eta_0 is 0.97 against a predicted 0.709.
(c) a corpus route from c_0 to c_inf: none found in the sweep (B281);
none found since.

---

## 2. Q-250 — is eta(k) the canonical reading of "the hydrodynamic velocity field's transfer above k_c"

### 2.1 Verified at source

- PAPER_2276 sec 6.4 (as shipped in v0.437.0) specified "the transverse
  current integrated over omega" — that integral is C_T(k, t=0) = N k_B T / m
  at every k (equipartition). PAPER_2281 sec 1 states the identity; PAPER_2276
  now carries the dated correction. VERIFIED.
- PAPER_2281 sec 3-4 (B286): eta(k) from the transverse-current
  autocorrelation, eta(k) = rho / (k^2 int_0^inf C_T(k,t)/C_T(k,0) dt)
  (generalized hydrodynamics; Palmer 1994; Hess 2002; the gmx tcaf
  observable), prediction eta(k)/eta_0 = exp(-0.344 (k/k_c)^2). VERIFIED.

### 2.2 What eta(k) is, and what the alternative (b) is

eta(k) is the k-dependent shear viscosity: the linear-response coefficient
relating transverse momentum current to the transverse velocity gradient at
wavevector k. It is THE quantity the words "momentum transfer above k_c"
map onto in generalized hydrodynamics, which is why B286 proposed it.
Alternative (b), the transverse dispersion: at low k the transverse current
decays diffusively (C_T ~ exp(-eta k^2 t / rho)); above an onset wavenumber
k_T the liquid supports propagating shear waves and C_T(k,t) oscillates.
The onset k_T is a second, independent number that the same data supply. A
framework cutoff at k_c could be read as either "eta(k) rolls off at k_c"
or "shear waves begin at k_c"; they need not coincide. MEASURED (sec 5,
6.21 nm box): C_T(k,t) is diffusive (no negative lobe: minimum -0.03 +-
0.03) at k = 1.01 nm^-1 and propagating (minimum -0.094 +- 0.018, 5 sigma)
at k = 1.43 - the shear-wave onset k_T lies between 1.0 and 1.4 nm^-1, a
factor 4-5 BELOW k_c(c_0) and below k_c(c_inf) too. Reading (b) would
therefore fail front 4 outright for both candidates; reading (a), eta(k),
gives the c_0 scale within 1.5. The two readings are not interchangeable.

### 2.3 Source-verification FINDING: a sub-question the queue does not yet carry — ATOMS or MOLECULES

The transverse current can be built from the atomic velocities
(j = sum over all atoms of m_i v_i e^{ik.r_i}; gmx tcaf does this on the
selected group) or from the molecular centres of mass (the molecular
hydrodynamic momentum density). At k <= 3 nm^-1 they agree; at k ~ 10-14
nm^-1 (k x r_OH ~ 1) the atomic current carries the librational motion of
the hydrogens, which is not viscous momentum transport. The B286b run used
the atomic current. The record run recorded BOTH at every k: k_c 7.90
(COM) vs 8.02 (atomic) - a 1.5 pct difference, at the edge of the error
bars; the two currents agree to 1e-3 at k < 4 and separate slowly above.
The ruling does not hinge on it. Recommendation: the molecular
(centre-of-mass) current is the hydrodynamic variable the claim is about;
the atomic one is reported alongside as the gmx-comparable number.

### 2.4 Recommendation

eta(k) as canonical (as PAPER_2281 sec 4 states), on the centre-of-mass
current, with the shear-wave onset k_T reported next to it from the same
run as the (b) reading — so that if Daniel later prefers (b) the grade is
re-stated without a new run. (c), a kernel-smoothed velocity-field
spectrum, remains not recommended: it measures the kernel.

The queue's "Also needed: the MD run itself" paragraph is now stale (the
run exists: md_grade/); to be struck in the next band.

---

## 3. Q-246 — the high-k exponents (a, beta) vs the 5/2 threshold, and why front 4 bears on it

- PAPER_106 L98-99: `?_damp(k) = ?_0 (k/k_Q)^a` and
  `F_UQFF(k) = 1/(1 + (k/k_Q)^ß)` — VERIFIED verbatim; neither exponent is
  given a number anywhere in PAPER_106 (grep "exponent": only L183
  "? = 1.8 (scaling exponent)", a different quantity). VERIFIED.
- The threshold: ||grad rho||_2^2 ~ int k^2 F(k)^2 k^2 dk ~ int k^{4-2 beta}
  dk converges at infinity iff 4 - 2 beta < -1, i.e. beta > 5/2. RECOMPUTED,
  holds.

The link to front 4 that was not in the queue: the SHAPE test. PAPER_106's
suppression factor with beta = 2 is exactly the Lorentzian 1/(1 + c k^2) that
the front-4 analysis fits as the alternative to the Gaussian. If the record
run finds the roll-off Gaussian, that is evidence for option (b) of Q-246
(canonize the PAPER_1042 Gaussian tail as THE high-k form; both Leray
conditions automatic). If it finds a Lorentzian, that is the PAPER_106 form
with beta = 2 < 5/2 — which does not touch Theorem B (which rests on the
Gaussian mollifier of PAPER_2275 sec 3 regardless), but would mean the
measured fluid does NOT follow the form Theorem B's mollifier is built on,
and Q-246 (a) would need beta fixed above 5/2 by some other route. The
caveat of sec 2.2 applies: eta(k) is a transport coefficient, F_UQFF(k) a
field multiplier; the identification between them is part of what Q-250
decides. The record run DECIDED it: Gaussian in all four runs (pooled 3-seed chi2
33 vs 192; 6 nm box 71 vs 104). The evidence favours Q-246 option (b),
canonizing the PAPER_1042 Gaussian tail as the high-k form - subject to
the identification caveat above, which is Q-250's.

Track 3 is CLOSED on the Gaussian form (PAPER_2275; registry theorem_b_row);
nothing here reopens it.

---

## 4. Summary table for the ruling session

| ruling | evidence now | what the record run adds | recommendation on the evidence |
|---|---|---|---|
| Q-247 sound speed | k_c = 7.90 +- 0.05 nm^-1 in 4 runs / 2 boxes / 3 seeds; c_0 x 1.49; c_inf x 3.22 EXCLUDED; implied c 994 m/s | done | (a) c_0, with the 1.49 residual recorded as measured; literal's provenance corrected (sec 1.2) |
| Q-250 observable | eta(k): Gaussian, c_0 scale. Shear-wave onset k_T = 1.0-1.4 nm^-1: below BOTH candidates | done | eta(k) canonical on the centre-of-mass current (atomic differs 1.5 pct); k_T reported - reading (b) fails both candidates |
| Q-246 exponents | Gaussian decided (chi2 33 vs 192) | done | (b) canonize the PAPER_1042 Gaussian tail, under the Q-250 identification |

---

## 5. The record run (DONE 2026-09-17)

Engine: md_pme (rigid TIP4P/2005; SPME order 4, grid 0.1 nm, alpha 3.5 nm^-1,
real-space cutoff 0.9 nm; C pair kernel with cell list and a 2e-5 nm erfc
table (max error 6e-8); RATTLE in C). Validation before launch: Madelung
constant of NaCl from the Ewald sum 1.747565 (literature 1.747565); C real
space vs numpy reference to 1.2e-4 kJ/mol in 22,692; SPME reciprocal vs
direct k-sum 3e-3 relative (order 4, 0.1 nm); forces = -grad E to 3e-8
relative by finite differences; NVE at 2197 molecules, 2 fs: dE/N = -0.0001
kJ/mol over 2 ps (the reaction-field engine gave -0.006); E_pot/N -47.1 to
-47.2. Currents by B-spline/FFT momentum-density transform, validated
against the exact sum (3.5e-3 rms at k = 12-14.5 nm^-1, 6e-5 at k < 6);
sampled every 4 fs (the B286b run sampled every 20 fs, which is marginal
above k ~ 5 nm^-1 where the correlation time is 20-80 fs - a limitation of
the first measurement disclosed here); on-the-fly autocorrelator to 10 ps
(4 fs resolution to 0.8 ps, 40 fs beyond) in six blocks; eta(k) by the
Green-Kubo integral to 8 ps; errors from the blocks, and from the seeds.

Runs (all 298 K, 2 fs, weak Berendsen 5 ps, 40 ps equilibration): B =
2,197 molecules, L 4.040 nm, k_min 1.555, 28 shells to 14 nm^-1, 300 ps,
seeds 11 / 12 / 13; C = 8,000 molecules, L 6.215 nm, k_min 1.011, 31 shells,
200 ps. The 8 nm / 1 ns spec of PAPER_2281 was NOT run: the cloud
workspace suspends between turns, so a run only advances while a turn is
held open, and 8 nm costs 0.7 s per step - Daniel chose the 4 nm seeds
plus the 6 nm box (ruling 2026-09-16). Results: sec 1.4b, sec 2.2, sec 3.
Not claimed: the plateau below k = 1.0 nm^-1; the value of k_T to better
than "between 1.0 and 1.4"; anything about real water beyond what
TIP4P/2005 at 298 K says.
