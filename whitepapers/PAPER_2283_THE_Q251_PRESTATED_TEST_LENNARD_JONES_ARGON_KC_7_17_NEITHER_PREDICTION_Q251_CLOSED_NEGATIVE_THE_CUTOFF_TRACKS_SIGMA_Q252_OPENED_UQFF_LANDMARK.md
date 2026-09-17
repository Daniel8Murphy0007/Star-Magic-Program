# PAPER_2283 - THE Q-251 PRE-STATED TEST: LENNARD-JONES ARGON AT THE NIST STATE POINT, TWO PREDICTIONS WRITTEN BEFORE THE RUN, MEASURED k_c = 7.17 +- 0.05 nm^-1 - NEITHER; Q-251 CLOSED NEGATIVE; THE CUTOFF TRACKS THE MOLECULAR DIAMETER IN BOTH LIQUIDS; Q-252 OPENED (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-17. **Trigger:** "PROCEED WITH Q-251 argon test", then
"prepare the ship". **Band:** v0.442.0 (B288).
**Live mirror:** uqff_ns_assembly.q251_prestated_test(), q251_argon_grade(),
front4_rulings()['Q-251'], ['Q-252'].
**Data:** md_grade/q251_argon_eta_k.csv, md_grade/q251_argon_summary.json;
md_grade/ar_s1_analysis.json, ar_s2_analysis.json, pool_argon.json; logs
md_grade/ar_s1.log, ar_s2.log.
**Instruments (source, on the wheel):** md_grade/lj_kernel.c (the LJ cell-
list kernel), md_grade/argon_record.py (the run: transverse AND longitudinal
currents, correlator, MSD, checkpoint), md_grade/validate_argon.py + .out,
md_grade/ar_analyze.py, md_grade/gridcur.py (currents3 added).
**Pre-registration:** RULINGS_QUEUE.md, Q-251, the paragraph headed
"PRE-STATED TEST", committed to the repository before the run and unchanged
since; the RESULT paragraph appended below it after.

## 0. What changed, in one paragraph

PAPER_2282 measured water's eta(k) cutoff at k_c = 7.90 +- 0.05 nm^-1,
1.489 times the framework's k_c(c_0) = 5.31, and noticed that 1.489 sits on
D_BSFG/D_phys = 1.5. It refused to claim it (post-hoc, one liquid, one
temperature) and named the test that could earn it: a second liquid with
the ratio predicted first. This paper is that test. Lennard-Jones argon at
the NIST 85 K / 0.101325 MPa state point (c_0 = 854.35 m/s). Two
predictions, written into the rulings queue and committed before a single
step ran: P1, the Q-247 form, k_c = omega_SCm/c_0 = 9.19 nm^-1; P2, the
Q-251 route, k_c = (D_BSFG/D_phys) omega_SCm/c_0 = 13.79 nm^-1; reading
rule +-10 pct. The engine reproduced NIST's viscosity to 1-2 pct and the
literature diffusion coefficient. **Measured: k_c = 7.25 +- 0.06 and
7.09 +- 0.06 in two seeds, pooled 7.17 +- 0.05 nm^-1**, Gaussian over the
water-comparable range. Ratio to P1: 0.78. Ratio to P2: 0.52. Neither.
**Q-251 closes NEGATIVE** - water's 1.489 was a coincidence - and P1, the
sound-cone form already negative for water (+49 pct), is negative for
argon too (-22 pct). What the two liquids say together was not predicted
and is not claimed: their sound speeds differ by 1.73x, their cutoffs by
1.10x, and k_c x sigma = 2.50 (water) and 2.44 (argon). The cutoff of
eta(k) tracks the molecular diameter, not omega_SCm/c_s. That is opened as
Q-252 and left to Daniel.

## 1. The pre-statement (verbatim from RULINGS_QUEUE.md, committed before the run)

"liquid argon, Lennard-Jones (sigma 0.3405 nm, epsilon 0.9961 kJ/mol =
119.8 K), at the NIST state point 85 K, 0.101325 MPa: density 1409.6
kg/m^3 (21.25 nm^-3, rho* 0.839, T* 0.710), c_0 = 854.35 m/s, eta = 279.54
uPa s (NIST Chemistry WebBook, isobaric table, read 2026-09-17).
PREDICTIONS: (P1, Q-247 as ruled) k_c = omega_SCm / c_0 = 9.19 nm^-1,
Gaussian with coefficient 0.344, 1/e at 15.7 nm^-1; (P2, the Q-251 route)
k_c = (D_BSFG/D_phys) omega_SCm / c_0 = 13.79 nm^-1, 1/e at 23.5 (water's
own measured ratio 1.489 would give 13.69). READING RULE: measured Gaussian
k_c within +-10 pct of 9.19 -> P1 holds for argon and Q-251 closes NEGATIVE
(water's 1.49 was a coincidence); within +-10 pct of 13.79 -> Q-251 has its
second liquid (POSITIVE, still not a derivation); neither -> both NEGATIVE
and the ratio k_c/k_c(c_0) is recorded next to water's 1.489."

The external literals: sigma, epsilon (the standard argon LJ parameters);
c_0, rho, eta from the NIST Chemistry WebBook isobaric table for argon at
0.101325 MPa (84 K: 861.25 m/s; 85 K: 854.35; 86 K: 847.42), read through
the browser pane on 2026-09-17. The number the test hangs on, c_0, was not
chosen; it was read.

## 2. The instrument

The B287 engine's Lennard-Jones path, with the water-specific parts (SPME,
RATTLE, virtual site) unused: md_grade/lj_kernel.c is a cell-list 12-6
kernel with the energy shift at rc = 0.85 nm (2.5 sigma), OpenMP with
per-thread buffers; the integrator is velocity Verlet at 4 fs (0.002 tau_LJ)
in numpy with a weak Berendsen thermostat (5 ps) in production; the
currents are the B287 FFT momentum-density transform (gridcur.py), now
returning the longitudinal projection as well so the model's own sound
dispersion is on record; the correlator, blocks, MSD and checkpointing are
the B287 design. Validation (validate_argon.out): C kernel vs numpy all-
pairs 9e-13 kJ/mol; F = -grad E to 6e-9 relative; NVE at 4,096 atoms
+0.00001 kJ/mol per atom over 10 ps at 4 fs; E/N -5.15 to -5.17 eps at
rho* 0.839, T* 0.71 (the LJ equation of state gives -5.1 to -5.2). From the
production runs: eta_0 (plateau, k < 3) = 0.2743 +- 0.0047 and 0.2767 +-
0.0043 mPa s against NIST 0.2795; D = 1.81 and 1.80 e-5 cm^2/s against the
LJ literature 1.6-1.8 at this state; equipartition of the sampled currents
1.00-1.03. The truncated-shifted potential without tail correction sits
at ~310 bar at NIST's density (disclosed; the observable is measured at
fixed density and the transport coefficients are the check that matters).

## 3. The runs

4,096 atoms, L = 5.7765 nm (k_min 1.088 nm^-1), 36 shells to 26 nm^-1
(the P2 1/e at 23.5 needed the range), 24 vectors per shell, 68 ps of
equilibration, 400 ps of production per seed, currents every 8 fs, lags at
8 fs to 2 ps and 80 fs to 20 ps, six blocks. Seeds 1 and 2. Each run held
open in one turn (~2 h), per the workspace constraint of PAPER_2282 sec 7.

## 4. Results

| | seed 1 | seed 2 | pooled |
|---|---|---|---|
| k_c, Gaussian fit k <= 14 nm^-1 (n = 27) | 7.25 +- 0.06 | 7.09 +- 0.06 | **7.17 +- 0.05** |
| chi2 Gaussian / Lorentzian, k <= 14 | 43 / 94 | 46 / 111 | 54 / 111 |
| 1/e of eta/eta_0 (fit / direct crossing) | 12.4 / 12.4 | 12.1 | 12.2 / 12.4 |
| k_c, Gaussian fit over the full range to 26 | 7.98 (chi2 1120) | 8.51 (chi2 1561) | 7.96 (chi2 1076) |
| eta_0 plateau k < 3 (mPa s) | 0.2743 | 0.2767 | 0.2758 |
| D (1e-5 cm^2/s) | 1.81 | 1.80 | |

The harness (q251_argon_grade, weighted log-linear, no scipy) gives
7.16 +- 0.05 from the same table. Two points on the shape. First, over the
water-comparable range - up to 1.7 k_c, which is what PAPER_2282 had - the
Gaussian is as good for argon as it was for water (chi2 43-54 on 27
shells) and the Lorentzian is worse. Second, beyond k ~ 14 argon's tail is
SLOWER than Gaussian (eta/eta_0 = 0.065 at 26 nm^-1 where the Gaussian
gives 0.026), so a full-range Gaussian fit fails for either shape. The fit
range was not pre-specified; both are reported; the like-for-like number
is the k <= 14 one and it is what the rule is applied to. Its choice does
not change the verdict: 7.17 and 7.96 both fall outside +-10 pct of both
predictions.

## 5. The rule applied

| prediction | k_c predicted | measured / predicted | eta/eta_0 at that k_c: measured (fit) vs predicted 0.709 |
|---|---|---|---|
| P1: omega_SCm / c_0 | 9.19 | **0.78** | 0.57 |
| P2: (D_BSFG/D_phys) omega_SCm / c_0 | 13.79 | **0.52** | 0.28 |

NEITHER within +-10 pct. By the pre-stated rule: Q-251 CLOSED NEGATIVE.
The ratio recorded next to water's 1.489 is 0.78. D_BSFG/D_phys = 1.5 does
not recur; it was a coincidence, exactly the possibility PAPER_2282 sec 6
named when it declined to claim it.

## 6. What the two liquids say together (recorded, not claimed)

| | c_0 (m/s) | k_c(c_0) = omega/c_0 | measured k_c | measured / k_c(c_0) | sigma (nm) | k_c x sigma |
|---|---|---|---|---|---|---|
| water (TIP4P/2005, 298 K; B287) | 1480 | 5.31 | 7.90 +- 0.05 | 1.49 | 0.3159 (O-O) | **2.50** |
| argon (LJ, 85 K; B288) | 854 | 9.19 | 7.17 +- 0.05 | 0.78 | 0.3405 | **2.44** |
| ratio water/argon | 1.73 | 0.58 | 1.10 | | | 1.02 |

The framework's k_c scales with 1/c_s; the measured cutoff does not - it
moves by 10 pct when c_s moves by 73 pct, and in units of the molecular
diameter it is the same number in both liquids to 2 pct. The roll-off of
eta(k) sits at k ~ 2.5/sigma. That is the generalized-hydrodynamics
expectation for the wavevector-dependent viscosity of a simple liquid (the
viscosity is non-local on the molecular scale), and it is what the data
say. What it means for the framework's sound-cone cutoff is a question,
not a finding: EITHER the k_c of PAPER_2267 / PAPER_2275 (the surviving
mode set at omega_SCm/c_s) is a different object from the transfer cutoff
that eta(k) measures - in which case front 4, as an eta(k) test of
omega/c_s, was a category error (testing the wrong thing), Theorem B is
untouched and also untested by it, and the front must be re-posed a third time or retired -
OR the framework's cutoff for fluids is falsified as written. That is
Q-252. It is Daniel's.

## 7. Honesty inventory (Rule 7)

1. The prediction was pre-registered in the repository; the reading rule
   was fixed before the data; the result is appended beneath it. Nothing
   above sec 4 was written after the run.
2. The fit range was NOT pre-specified. Both ranges are reported; neither
   rescues either prediction.
3. Two seeds, one box, one state point, 400 ps each. The pooled error
   (+-0.05) is the fit error and seed scatter in quadrature.
4. The model's own c_0 was not cleanly measured: the longitudinal peak at
   the lowest shell (k = 1.09) is under-resolved by the 20-ps lag window,
   and the k = 1.5-1.9 shells give the dispersed sound (1.2-1.3 km/s), not
   the adiabatic c_0. P1 was therefore evaluated with NIST's c_0 as pre-
   stated; the model reproduces NIST's eta_0 to 1-2 pct and D to the
   literature, which is the check available.
5. Truncated-shifted LJ at 2.5 sigma without tail correction; ~310 bar at
   NIST's density. Disclosed.
6. sigma for water is the TIP4P/2005 O-O Lennard-Jones sigma; a different
   choice of "molecular diameter" for water moves 2.50 by a few pct and
   does not change sec 6's point.
7. Q-252 is a question the program opened against itself. It is not
   answered here, and no reading of it is preferred here.
8. Not claimed: that 2.5/sigma is a framework number; that Theorems A and
   B are affected (they state their own independence from the coefficient;
   their physical relevance is what Q-252 asks about); anything about real
   argon or real water beyond what the two models reproduce.

## 8. Cross-references

PAPER_2282 (B287; the water record run; Q-251 opened), PAPER_2281 (the
falsifier form), PAPER_2276 (index; front 4), PAPER_2275 (Theorem B; the
sound-cone k_c), PAPER_2267 (k_c = omega_SCm/c_s; L53), PAPER_1521
(D_BSFG), PAPER_2264 (the pair cap), PAPER_2270 (proof set).
RULINGS_QUEUE.md Q-251 (pre-statement and result), Q-252.
