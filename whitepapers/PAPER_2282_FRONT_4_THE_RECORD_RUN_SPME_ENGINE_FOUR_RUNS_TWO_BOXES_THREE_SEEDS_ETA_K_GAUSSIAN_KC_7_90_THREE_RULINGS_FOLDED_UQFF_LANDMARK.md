# PAPER_2282 - FRONT 4, THE RECORD RUN: A PARTICLE-MESH EWALD ENGINE WRITTEN FOR IT, FOUR RUNS IN TWO BOXES WITH THREE SEEDS, eta(k) OF TIP4P/2005 WATER GAUSSIAN WITH k_c = 7.90 +- 0.05 nm^-1, THE SHEAR-WAVE ONSET AT 1.0-1.4 nm^-1, THREE RULINGS FOLDED AND A FOURTH OPENED (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-17. **Trigger:** "proceed with 1 & 2" (the record run and
the rulings) and then "proceed with the next two parts as identified" (the
rulings folded; this band). **Band:** v0.441.0 (B287).
**Live mirror:** uqff_ns_assembly.front4_record_grade(), front4_rulings().
**Data:** md_grade/front4_record_eta_k.csv, md_grade/front4_record_summary.json;
per-run analyses md_grade/rec_*_analysis.json; logs md_grade/rec_*.log.
**Instruments (all on the wheel, all source):** md_grade/md_pme.py (the
SPME engine), md_grade/pair_kernel.c (C kernels), md_grade/gridcur.py (the
current transform), md_grade/ewald_ref.py (the explicit-Ewald reference),
md_grade/validate.py + validate.out, validate_gridcur.py + .out, nve_pme.py
+ .out (the validation ladder), md_grade/front4_record.py (the run),
md_grade/rec_analyze.py, rec_pool.py (the analysis).

## 0. What changed, in one paragraph

PAPER_2281 (v0.440.0) re-specified front 4 on the wavevector-dependent
shear viscosity eta(k), stated the falsifier before measuring, and measured
once: 512 molecules, a reaction-field engine, 20-fs sampling, one seed -
measured k_c 7.8 nm^-1 against the candidates 5.31 (c_0) and 2.45 (c_inf),
shape undecided. This paper is the record run that measurement called for,
under the constraint the workspace imposes (sec 7). A second engine was
written for it - smooth particle-mesh Ewald electrostatics, the pair
kernel, RATTLE and the B-spline spreading in C, the transverse currents by
an FFT momentum-density transform - and validated on a ladder that ends at
the Madelung constant of NaCl to 1e-7 and energy conservation to 1e-4
kJ/mol per molecule. Four runs: 2,197 molecules in a 4.04 nm box for 300 ps
at three seeds, and 8,000 molecules in a 6.21 nm box for 200 ps, sampled
every 4 fs, on the centre-of-mass and the atomic current. The result is the
same number every time: **eta(k) rolls off as a GAUSSIAN with measured
k_c = 7.90 +- 0.05 nm^-1** (seeds 7.89 / 7.89 / 7.94; the 6 nm box 7.93 +-
0.10), eta_0 = 0.84-0.85 mPa s against the literature 0.855, D = 2.3-2.4e-5
cm^2/s against 2.1-2.3 expected. Against the framework: c_0 gives k_c 5.31
(factor 1.49), c_inf gives 2.45 (factor 3.2, EXCLUDED); at k_c(c_0) the
measured suppression is 14 pct where PAPER_2275 L77 says 29 pct. The
6 nm box adds the shear-wave onset: C_T(k,t) is diffusive at k = 1.01 and
propagating at 1.43 nm^-1, so shear waves begin at 1.0-1.4 nm^-1 - four to
five times BELOW k_c(c_0). On the falsifier stated in PAPER_2281 sec 4,
front 4 is CLOSED NEGATIVE ON THE COEFFICIENT (the 1/e wavenumber, 13.5, lies
far from both 9.05 and 4.19) and POSITIVE ON EXISTENCE AND SHAPE (Gaussian,
not Lorentzian; on the sound-cone scale). Daniel ruled the three open
questions on this evidence (sec 6): Q-247 c_0 stands, with the provenance
of the literal 1480 m/s corrected; Q-250 eta(k) on the centre-of-mass
current is the canonical reading of transfer; Q-246 the PAPER_1042 Gaussian
tail is canonized as the high-k form. One question is OPENED, not ruled:
the measured ratio k_c/k_c(c_0) = 1.489 +- 0.010 sits on D_BSFG/D_phys =
1.5 (Q-251) - post-hoc, one liquid, one temperature, stated as an
observation and nothing more.

## 1. The engine (md_grade/md_pme.py, pair_kernel.c, gridcur.py)

The B286b engine (md_engine.py) used reaction-field electrostatics, the
one caveat PAPER_2281 sec 7 listed against its own measurement. For the
record the electrostatics are smooth particle-mesh Ewald (Essmann et al.
1995): real space erfc(alpha r)/r with alpha = 3.5 nm^-1 on every charge
pair of different molecules within a SITE cutoff of 0.9 nm (erfc(3.15) =
8e-6), reciprocal space by order-4 cardinal B-spline charge spreading on a
0.1 nm grid, FFT, the Euler-spline factors b(m), and force gathering by
the B-spline derivatives; self term; intramolecular exclusion correction
-q_a q_b erf(alpha r)/r on the three charge pairs of each molecule (their
forces lie along the constraints and are removed by RATTLE, but they are
carried so that F = -grad E exactly). Lennard-Jones on oxygen with the
energy shift at the cutoff. The model is TIP4P/2005 unchanged from B286b
(Abascal & Vega 2005; virtual-site weight 0.131938; RATTLE on three
distance constraints). The pair kernel runs a molecule cell list on the
oxygens with a prelist radius rc + 0.2 nm (the two site offsets of 0.096 nm
each), tabulates erfc(alpha r)/r and its force factor at 2e-5 nm with
linear interpolation (maximum relative error 6.2e-8, checked in C), and is
OpenMP-parallel with per-thread force buffers. RATTLE positions and
velocities are in C per molecule. The transverse currents j_T(k,t) =
sum_i m_i (v_i . e) exp(i k.r_i) are computed for a chosen set of k-vectors
by spreading the momentum density m_i v_i with the same order-4 B-splines,
one FFT per component, and reading the selected grid modes deconvolved by
b(m) - all k at once, exact up to aliasing from |k'| >= 2 pi/h - |k|.

## 2. The validation ladder (md_grade/validate.out, validate_gridcur.out, nve_pme.out)

1. Madelung constant of NaCl from the same Ewald formulas on a 4x4x4 point
   lattice: 1.747565 (literature 1.747565; relative error 1.2e-7).
2. Real space + LJ + exclusion, C kernel vs the numpy reference
   (ewald_ref.py, all-pairs minimum image): dE = 1.2e-4 kJ/mol in 22,692
   (the table); LJ and exclusion identical to all printed digits.
3. Reciprocal space, SPME vs the direct k-sum to |n| <= 16: 3.1e-3
   relative at order 4, 0.10 nm (1.6e-3 at 0.08 nm; 2.8e-4 at order 6) -
   the accuracy class of a production MD code at its default settings.
4. Forces vs -grad E of the engine's own energy by central differences
   (h = 1e-5 nm) on five oxygens and two hydrogens: agreement to 3e-8
   relative (0.03 kJ/mol/nm absolute of 1,000).
5. NVE at 2,197 molecules after 8 ps of equilibration: total energy
   drift -0.0001 kJ/mol per molecule over 2 ps at 2 fs (std 0.0008);
   -0.0005 at 1 fs. The B286b engine gave -0.006 at 2 fs.
6. Potential energy -47.1 to -47.3 kJ/mol per molecule across the runs
   (the model: -47.4). Equipartition of the sampled currents:
   C_T(k,0)/(N k_B T M) = 0.99-1.03 in every shell, both boxes.
7. FFT currents vs the exact sum over 216 random k-vectors on the 4 nm
   box: 1.8e-6 relative at k < 3 nm^-1, 5.8e-5 at 3-6, 3.4e-4 at 6-9,
   1.4e-3 at 9-12, 3.5e-3 rms (9.8e-3 max) at 12-14.5. The filter is the
   same at every time step, so the normalized autocorrelation is affected
   at the square of these numbers.
8. Transport, from the production runs themselves: eta_0 = 0.836 (4 nm,
   pooled), 0.850 +- 0.023 (6 nm plateau, k < 2.6) against the literature
   0.855 mPa s; D from the multi-origin centre-of-mass MSD (2,000
   molecules, lags 5-40 ps) = 2.33 / 2.42 / 2.38 / 2.38 e-5 cm^2/s against
   2.1-2.3 expected for TIP4P/2005 at 298 K (uncorrected for box size).

## 3. The runs (md_grade/rec_*.log)

All at 298 K (Berendsen, 5 ps), 2 fs, 40 ps equilibration (0.5 fs and
1 fs soft start, then 20 ps at 0.2 ps coupling and 20 ps at 1 ps), then
production with the currents sampled every 2 steps = 4 fs on both the
atomic (3N) and centre-of-mass (N) currents, for every k-vector in the
selected shells (up to 40 per shell), accumulated on the fly into an
autocorrelator at 4-fs lags to 0.8 ps and 40-fs lags to 10 ps, in six
blocks. eta(k) = rho / (k^2 int_0^8ps C_T(k,t)/C_T(k,0) dt) per shell;
errors from the blocks; for the pooled 4 nm result, block error and
seed-to-seed scatter in quadrature.

| run | molecules | L (nm) | k_min (nm^-1) | shells | length | seed |
|---|---|---|---|---|---|---|
| B13s11 | 2,197 | 4.0395 | 1.555 | 28 to 14.0 | 300 ps | 11 |
| B13s12 | 2,197 | 4.0395 | 1.555 | 28 | 300 ps | 12 |
| B13s13 | 2,197 | 4.0395 | 1.555 | 28 | 300 ps | 13 |
| C20 | 8,000 | 6.2147 | 1.011 | 31 to 13.9 | 200 ps | 21 |

The 20-fs sampling of B286b was marginal above k ~ 5 nm^-1, where the
correlation time is 20-80 fs; it is disclosed as a limitation of that
first measurement and is not present here.

## 4. Results

### 4.1 eta(k), the Gaussian, and k_c

| run / pool | k_c (COM current) | k_c (atomic) | chi2 Gaussian / Lorentzian | eta_0 (mPa s) |
|---|---|---|---|---|
| B13s11 | 7.89 +- 0.06 | 8.00 +- 0.06 | 53 / 142 (n = 28) | 0.837 |
| B13s12 | 7.89 +- 0.07 | 8.00 +- 0.07 | 58 / 83 | 0.838 |
| B13s13 | 7.94 +- 0.06 | 8.04 +- 0.07 | 56 / 136 | 0.832 |
| B pooled | **7.90 +- 0.05** (seed scatter 0.02) | 8.02 +- 0.05 | 33 / 192 | 0.836 |
| C20 | **7.93 +- 0.10** | 8.01 +- 0.10 | 71 / 104 (n = 31) | 0.829; plateau 0.850 +- 0.023 |
| B286b (v0.440.0, RF) | 7.80 | - | undecided | 1.05 |

The harness (front4_record_grade, pure arithmetic, weighted log-linear
fits) reproduces the scipy fits: 7.89 +- 0.05 and 7.92 +- 0.10, atomic
8.01 and 8.00, chi2 34 / 197 and 71 / 108. Gaussian b = 0.00550 nm^2;
1/e at 13.5 nm^-1. The centre-of-mass and atomic currents agree to 1e-3
at k < 4 nm^-1 and separate slowly above (1.5 pct in k_c).

### 4.2 Against the candidates

| candidate | k_c predicted | measured / predicted | eta/eta_0 at that k_c: measured (fit) vs PAPER_2275 m(k_c) | reading |
|---|---|---|---|---|
| c_0 = 1480 m/s | 5.307 | 1.49 | 0.856 vs 0.709 | same scale, NOT a precision match |
| c_inf = 3200 m/s | 2.454 | 3.22 | 0.967 vs 0.709 | EXCLUDED |

Implied "sound speed" of the measured roll-off scale: omega_SCm/k_c = 994
m/s - not a sound speed of water. The coefficient that WOULD fit at c_0 is
beta_i [SSq] -> 0.155 instead of 0.344; the k_c that fits at 0.344 is 7.90.

### 4.3 The shear-wave onset (6.21 nm box)

| k (nm^-1) | C_T minimum | error | reading |
|---|---|---|---|
| 1.011 | -0.030 | 0.028 | diffusive (consistent with no negative lobe) |
| 1.430 | -0.094 | 0.018 | propagating (5 sigma) |
| 1.751 | -0.167 | 0.011 | propagating |
| 2.26-5.4 | -0.20 to -0.26 | <= 0.008 | fully developed shear waves |

Shear waves begin between 1.0 and 1.4 nm^-1: below k_c(c_inf) = 2.45 and
four to five times below k_c(c_0) = 5.31. The "onset" reading of transfer
(Q-250 alternative (b)) would therefore fail front 4 for BOTH candidates,
where the eta(k) reading gives the c_0 scale within 1.5. The two readings
are not interchangeable; this is the fact Q-250 was ruled on.

## 5. The falsifier applied (PAPER_2281 sec 4, verbatim: "A measured eta(k)/eta_0 ... whose 1/e wavenumber lies far from both 9.05 and 4.19 nm^-1, or whose shape is clearly Lorentzian rather than Gaussian through k ~ k_c, closes front 4 NEGATIVE for the identification 'transfer = eta(k)' ... A measured a within the scatter of either candidate's value is a pass for that candidate")

The measured 1/e wavenumber is 13.5 nm^-1 - far from both. The shape is
Gaussian, not Lorentzian, in every run. No candidate's coefficient is
within the scatter. Therefore, with Q-250 ruled (the observable is the
right one), the exact-coefficient prediction exp(-0.344 (k/k_c)^2) with
k_c = omega_SCm/c_s is NEGATIVE at both candidates: **front 4 is CLOSED
NEGATIVE ON THE COEFFICIENT** - a failed prediction, not a wrong
observable, as sec 4 of PAPER_2281 required the reading to be one or the
other and not silently neither. What SURVIVES, positively: the roll-off
exists; it is Gaussian (the PAPER_1042 form, not the PAPER_106 beta = 2
form); its scale is the sound-cone scale within a factor 1.5; and it
excludes the fast-sound candidate. What is NEGATIVE is the number 0.344 at
k_c = 5.31 for this fluid. Theorem A and Theorem B are unaffected (their
mathematics never depended on the fluid's coefficient; PAPER_2275 sec 3);
the number 0.156 nm inherits the same factor 1.49 if eta(k) is taken as
the mollifier's own width (the Q-250 identification), which it is NOT
claimed to be here.

## 6. The rulings (Daniel, 2026-09-17, on RULINGS_BRIEF_Q246_Q247_Q250.md)

Ruled by "proceed with the next two parts as identified" over the brief's
recommendation table, each on the evidence line beside it:

- **Q-247 RULED: c_0.** k_c = omega_SCm/c_0 = 5.307 nm^-1 stands; c_inf
  rejected (excluded by 3.2 in every run). The residual 1.489 is recorded
  in the registry row as a measured fact. PROVENANCE CORRECTED: the
  literal 1480 m/s entered the corpus at PAPER_2267 L53 as an external
  value (the adiabatic sound speed of fresh water near 20 C; 1497 at
  25 C); PAPER_2261 carries seawater as a DENSITY landmark only (L40) and
  no sound speed - the "seawater anchor" attribution is withdrawn in
  uqff_ns_assembly (C_S_WATER_M_S, galerkin_mode_count) and the registry.
- **Q-250 RULED: eta(k) on the centre-of-mass current.** The atomic
  current (gmx tcaf's group) is reported alongside; the shear-wave onset
  k_T is reported alongside as reading (b). The "Also needed: the MD run
  itself" paragraph of the queue entry is struck - the run exists.
- **Q-246 RULED: option (b).** The PAPER_1042 Gaussian tail q^{n^2} is
  canonized as THE high-k form for fluid modes (the beta -> infinity
  member of the PAPER_106 family; both Leray conditions automatic). The
  identification n = k/k_c (PAPER_2275 sec 6) stays flagged as before;
  only the number 0.156 nm depends on it.
- **Q-251 OPENED (not ruled):** k_c(measured)/k_c(c_0) = 1.489 +- 0.010
  (fit) / +- 0.004 (seeds), against D_BSFG/D_phys = 6/4 = 1.5. A route
  would read k_c(fluid) = (D_BSFG/D_phys) omega_SCm/c_0 = 7.96 nm^-1. It
  is post-hoc, one parameter, one liquid, one temperature; a pre-stated
  test needs a second liquid or a temperature series. Recorded as an
  observation. NOT claimed: that the ratio is 1.5; that the corpus derives
  it; the coefficient 0.344 at 7.96.

## 7. Honesty inventory (Rule 7)

1. The 8 nm / 1 ns spec written in PAPER_2281 sec 5b was NOT run. The
   cloud workspace suspends between turns, so a run advances only while a
   turn is held open; at 0.7 s per step the 8 nm box needed days of held
   turns. Daniel chose (2026-09-16) the 4 nm seeds plus the 6 nm box. The
   plateau below k = 1.0 nm^-1 is therefore not sampled; the 6 nm box's
   k < 2.6 plateau (0.850 +- 0.023) stands in for it.
2. One box size per seed set; 200-300 ps per run; Berendsen thermostat
   (weak, 5 ps) during production - the standard caveats, disclosed.
3. TIP4P/2005 is a model of water, not water. Its eta_0 and D are
   reproduced to 2-5 pct, which is what the model itself achieves against
   experiment; nothing here is claimed about real water beyond that.
4. The SPME reciprocal accuracy is 3e-3 relative at the settings used -
   a production-code default, not a spectroscopic one. The force/energy
   consistency (3e-8) and conservation (1e-4) are what the dynamics needs.
5. The shear-wave onset is a BRACKET (1.0-1.4 nm^-1) from two shells with
   3 and 6 vectors; a finer bracket needs a larger box.
6. The Gaussian-vs-Lorentzian decision is a two-parameter comparison on
   28-31 shells with error bars; a Lorentzian is excluded, a third shape
   is not tested.
7. The atomic and centre-of-mass currents differ by 1.5 pct in k_c; Q-250
   chose the latter. Had it chosen the former the number would be 8.02.
8. Q-251's 1.5 is post-hoc. It is written down because the doctrine is to
   write such things down and rule on them later, not because it is
   believed.
9. Not claimed: front 4 "passed"; that fronts 1-3 changed; the value of
   0.156 nm; that eta(k) is the mollifier; the diffusion coefficient to
   better than 5 pct; anything about the 8 nm plateau.

## 8. Cross-references

PAPER_2281 (B286, the re-specification and first measurement; the
falsifier of sec 4 applied here), PAPER_2276 (index; front 4), PAPER_2275
(Theorem B; the Gaussian tail; m(k_c) = 0.709 at L77), PAPER_2267 (k_c =
omega_SCm/c_s; L53 the literal 1480), PAPER_2261 (the K4 density
landmarks; seawater 1.025 at L40 - no sound speed), PAPER_1042 (the
Gaussian phonon partition, now canonized), PAPER_106 (the beta-form
suppression, now the excluded alternative), PAPER_2264 (the pair cap),
PAPER_2270 (proof set). RULINGS_BRIEF_Q246_Q247_Q250.md (the brief ruled
on).
