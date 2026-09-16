# PAPER_2281 - FRONT 4 RE-SPECIFIED: THE TEST AS WRITTEN WAS AN EQUIPARTITION IDENTITY - THE WAVEVECTOR-DEPENDENT SHEAR VISCOSITY eta(k) AS THE OBSERVABLE, THE PREDICTION a = 0.344/k_c^2 FOR THE STANDARD TCAF FIT, AND THE INSTRUMENT ON THE WHEEL (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-15. **Trigger:** "proceed with recommendations" - front 4,
the MD run, named the cheapest open front the day v0.439.0 shipped.
**Band:** v0.440.0 (B286).
**Live mirror:** uqff_ns_assembly.front4_specification() (the prediction),
uqff_ns_assembly.front4_grade_eta_k() (the harness, GRADED - sec 5b).
**Instrument:** md_grade/md_engine.py + front4_run.py + front4_analyze.py (the
program's own numpy MD, run for this paper; data md_grade/front4_eta_k.csv);
md_grade/front4_tcaf.py (OpenMM route, on the wheel, not run).
**Ruling opened:** Q-250.

## 0. What changed, in one paragraph

Front 4 was to be run today. It was not, because the run would have been
worthless: the test PAPER_2276 sec 6.4 specified - "the k-dependence of
the transverse current integrated over omega against exp(-0.344
(k/k_c)^2)" - is, for any classical fluid in equilibrium, the integral
over all frequencies of the transverse current spectrum, which is the
equal-time correlation C_T(k, t = 0) = <|j_T(k)|^2> = N k_B T / m at
EVERY wavenumber. Velocities are uncorrelated with positions in the
canonical ensemble; the quantity is flat in k by identity. A molecular-
dynamics run would have returned a flat line, the Gaussian roll-off would
have "failed", and nothing about the framework's claim would have been
tested. This paper (i) names that defect (Rule 7 - the program's own
specification, not the data); (ii) states the observable the claim is
actually about, the wavevector-dependent shear viscosity eta(k) from the
transverse-current autocorrelation, which is standard in molecular
simulation (Palmer 1994; Hess 2002; the GROMACS tool gmx tcaf) and IS the
fluid's transverse-momentum transfer at wavenumber k; (iii) derives what
the framework predicts for it - the full shape eta(k)/eta_0 = exp(-0.344
(k/k_c)^2) and, for the standard small-k fit eta(k) = eta_0 (1 - a k^2)
that gmx tcaf prints, the coefficient a = 0.344/k_c^2 = 0.0122 nm^2 (c_0)
or 0.0570 nm^2 (c_inf) - a number a stock tool reports; (iv) states the
falsifier before measurement; (v) puts the instrument on the wheel; and
(vi) opens Q-250: whether eta(k) is the canonical reading of "transfer".
The public-package index is unreachable from the program's cloud
workspace (HTTP 403), so the run itself waits on either an OpenMM wheel
dropped into wheels/ or a run on Daniel's machine. Front 4 is now
correctly posed - and, the same day, MEASURED (sec 5b): a purpose-built
numpy MD of TIP4P/2005 (512 molecules, 240 ps, validated on force-energy
consistency, energy conservation and the model's potential energy)
returns eta(k)/eta_0 flat to k ~ 6 nm^-1 then rolling off to 1/e at
13.3 nm^-1 - a measured Gaussian k_c of 7.8 nm^-1. That is the c_0
scale (5.31; factor 1.47) and excludes c_inf (2.45; factor 3.2), but it
is NOT a precision match of exp(-0.344 (k/k_c)^2) at either candidate,
and the shape (Gaussian vs Lorentzian) is undecided at this statistical
quality. Front 4's honest state: the roll-off exists, sits on the
hydrodynamic-sound-cone scale, and disfavours fast sound (bearing on
Q-247); the framework's exact coefficient is not confirmed.

## 1. The defect (Rule 7 first)

For N particles with velocities v_i and positions r_i, the transverse
current at wavevector k is j_T(k, t) = sum_i m v_i,perp(t) exp(i k.r_i(t)).
Its spectrum C_T(k, omega) is the Fourier transform of C_T(k, t) =
<j_T(k, t) j_T*(k, 0)>, and integrating C_T(k, omega) over all omega
returns C_T(k, t = 0) = <|j_T(k, 0)|^2> = sum_i m^2 <v_i,perp^2> = N m k_B T
(the cross terms vanish because equilibrium velocities are independent of
positions and of each other). This holds for every k, every classical
model, every temperature. The "integrated transverse current" is not a
dynamical quantity at all; it is the equipartition theorem. PAPER_2276
sec 6.4 asked the MD to compare it with a Gaussian in k. That comparison
was guaranteed to fail and guaranteed to mean nothing. The defect is in
the specification, found before the instrument was built; it is recorded
here so that the front is graded on a real observable.

## 2. The claim, and the observable that carries it

Theorem B (PAPER_2275 sec 7) and the front-4 statement (PAPER_2276
sec 6.4) say: the hydrodynamic velocity field's TRANSFER above k_c rolls
off as m(k) = exp(-beta_i [SSq] (k/k_c)^2) = exp(-0.344 (k/k_c)^2),
Gaussian, with no fluid dynamics persisting above it. "Transfer" of what
by the fluid at wavenumber k? Of transverse momentum - that is what a
shear stress is. The quantity that measures how much transverse momentum
the fluid transfers at wavenumber k is the wavevector-dependent shear
viscosity eta(k), defined through the transverse-current autocorrelation:
in the hydrodynamic limit C_T(k, t)/C_T(k, 0) = exp(-(eta/rho) k^2 t), and
at finite k the same decay defines eta(k) (Palmer, Phys. Rev. E 49, 359
(1994)); the GROMACS implementation (gmx tcaf; Hess, J. Chem. Phys. 116,
209 (2002)) fits each C_T(k, t) to f(t) = exp(-v)(cosh Wv + sinh Wv / W),
v = -t/2tau, W = sqrt(1 - 4 tau eta k^2/rho), one (tau, eta) per k-shell,
and extrapolates eta(k) = eta_0 (1 - a k^2) to k = 0. eta(k) is known to
fall with k toward zero (TIP4P water at 292 K, Condensed Matter Physics
2005; SPC/SPC/E, Hess 2002) - it is the quantity whose k-dependence
expresses "how far down in scale the fluid still transfers momentum as a
fluid". It is the observable the claim is about, and it is one that a
stock tool prints.

## 3. The prediction

With eta(k)/eta_0 = exp(-0.344 (k/k_c)^2):

| candidate (Q-247) | c_s (m/s) | lambda_c (nm) | k_c (nm^-1) | a = 0.344/k_c^2 (nm^2) | k at 1/2 (nm^-1) | k at 1/e (nm^-1) |
|---|---|---|---|---|---|---|
| c_0 (hydrodynamic, PAPER_2261) | 1480 | 1.184 | 5.307 | 0.0122 | 7.54 | 9.05 |
| c_inf (IXS fast sound, Q-247) | 3200 | 2.560 | 2.454 | 0.0570 | 3.49 | 4.19 |

The small-k form is the expansion of the Gaussian: exp(-0.344 (k/k_c)^2)
= 1 - 0.344 (k/k_c)^2 + ..., so the coefficient gmx tcaf fits IS the
framework's number, and a single MD run at box sizes of 4-8 nm (smallest k
1.6-0.8 nm^-1, where the expansion is accurate to a few percent) reads it
off. The full shape separates the Gaussian from the Lorentzian-in-k^2 form
1/(1 + a k^2) that MD analyses sometimes use: identical to second order,
diverging near k ~ k_c where the Gaussian falls faster. The ratio of the
two candidate a-values is (c_inf/c_0)^2 = 4.67; they cannot both fit.

## 4. The falsifier, stated before measurement

A measured eta(k)/eta_0 for water (TIP4P/2005, 298 K) whose 1/e
wavenumber lies far from both 9.05 and 4.19 nm^-1, or whose shape is
clearly Lorentzian rather than Gaussian through k ~ k_c, closes front 4
NEGATIVE for the identification "transfer = eta(k)" - and Q-250 (sec 6)
asks whether that identification is the canonical one, so that a negative
result is read as either a failed prediction or a wrong observable, and
not silently as neither. A measured a within the scatter of either
candidate's value is a pass for that candidate and a discrimination
between c_0 and c_inf - which would also settle Q-247 from the fluid side.
Nothing about Theorem B's mathematics depends on the outcome; the number
k_c and the placement of the Gaussian form do.

## 5. The instrument (on the wheel; not yet run)

md_grade/front4_tcaf.py: OpenMM, TIP4P/2005 (Abascal & Vega 2005
parameters written as a force-field XML; rigid, PME, 0.9 nm cutoff),
cubic box (4 nm to check the pipeline, 5-8 nm for the record), 298 K,
100 ps equilibration, 400+ ps production, j_T(k, t) accumulated on the fly
for every integer k-shell up to |n| = 16 (k up to ~20 nm^-1 in a 5 nm
box), C_T(k, t) to 20 ps lag, the gmx tcaf fit per shell, eta_0 and a
from the three smallest shells, CSV out. The harness
front4_grade_eta_k() reads the CSV, computes the rms residual against the
Gaussian at both k_c, the measured 1/e wavenumber, and names the nearer
candidate. Runtime: hours per 100 ps on a few CPU cores; a GPU platform
is 20-50x faster. Any GROMACS run of the same box with gmx tcaf is an
equivalent instrument. The program's cloud workspace cannot reach the
package index (HTTP 403 on every package), so the run waits on an OpenMM
wheel in wheels/ (cp311, manylinux_2_28, glibc 2.39 present) or a run on
Daniel's machine - both take the same script.


## 5b. The measurement (same day; the program's own MD engine)

The package index being unreachable, the instrument was written from
scratch: md_grade/md_engine.py, a rigid TIP4P/2005 water MD in numpy -
RATTLE on three distance constraints per molecule, the M site as a
virtual site with its force redistributed, O-O Lennard-Jones and
reaction-field Coulomb (eps_rf = infinity) with a SITE-based 0.9 nm
cutoff (a first version with a molecule-based cutoff heated at +1.5
kJ/mol per molecule per 2 ps, timestep-independent - the reaction-field
force at the group boundary is ~50 kJ/mol/nm, not zero; the site cutoff,
where V and F both vanish at r_c, conserves energy to -0.006 kJ/mol per
molecule over 2 ps at 2 fs), velocity Verlet at 2 fs. Validation before
any eta: forces equal -grad E to machine precision by finite differences
(atom and molecule level); potential energy -47.5 kJ/mol per molecule
against the model's published -47.4; temperature 298 K held by a weak
Berendsen thermostat (tau 5 ps). Box: 512 molecules, L = 2.486 nm,
k_min = 2.53 nm^-1, 40 ps equilibration, 240 ps production, j_T(k, t)
sampled every 20 fs for 369 k-vectors in 26 shells to k = 13.8 nm^-1.
eta(k) by the Green-Kubo integral rho / (k^2 int_0^8ps C_T/C_T(0) dt)
(primary; errors from four 60 ps blocks); the gmx-tcaf-form fit is also
reported and is biased low by ~3x in the oscillatory shear-wave regime at
these k (disclosed; it gives the same trend).

| k (nm^-1) | 2.53 | 3.58 | 4.38 | 5.06 | 5.65 | 6.19 | 7.15 | 7.58 | 8.38 | 9.46 | 10.4 | 11.0 | 12.6 | 13.6 | 13.8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| eta(k) mPa s | 1.42+-0.17 | 1.04+-0.04 | 1.15+-0.14 | 0.86+-0.04 | 0.91+-0.04 | 0.86+-0.03 | 0.67+-0.07 | 0.83+-0.02 | 0.69+-0.03 | 0.61+-0.01 | 0.57+-0.01 | 0.47+-0.01 | 0.44+-0.01 | 0.37+-0.01 | 0.37+-0.01 |

eta_0 (Gaussian extrapolation) = 1.05 mPa s against the model's published
0.855 (reaction-field electrostatics and the small box account for the
order of the difference; the validation is the order and the trend, not
the third digit). The roll-off: eta/eta_0 is ~1 to k ~ 6 nm^-1, 0.6 at
9.5, 0.37 (1/e) at 13.3-13.4 nm^-1. Weighted log-linear Gaussian fit:
b = 0.0056 nm^2, MEASURED k_c = 7.8 nm^-1. Against the candidates:

| candidate | predicted k_c | predicted 1/e | measured / predicted k_c | reading |
|---|---|---|---|---|
| c_0 (1480 m/s) | 5.31 | 9.05 | 1.47 | same scale, not a precision match |
| c_inf (3200 m/s) | 2.45 | 4.19 | 3.18 | excluded |

Shape: the weighted log-linear fit prefers the Gaussian (rms 0.050 vs
Lorentzian 0.065); an error-weighted nonlinear fit of the same points
prefers the Lorentzian (0.068 vs 0.097). Undecided at this quality; a
longer run in a larger box decides it. The second estimator (gmx-form
fit) gives measured k_c = 4.4 nm^-1 - the c_0 candidate sits between the
two estimators' values, which is the honest width of the result.

READING. The claim's observable exists and behaves as the claim's
direction requires: the fluid's transverse-momentum transfer rolls off
at a few nm^-1, and the scale is the sound-cone scale of c_0 - not the
fast-sound scale of c_inf, which is excluded by a factor three (this is
the first fluid-side evidence bearing on Q-247, and it points to
c_0 = 1480 m/s). The framework's exact form exp(-0.344 (k/k_c)^2) with
k_c = 5.31 is NOT confirmed: the measured scale is 1.47x larger in k (a
factor 2.2 in the coefficient b), outside any error bar here. Per the
falsifier of sec 4, stated before measurement, this is NOT a pass; it
is a same-scale, wrong-coefficient result that either (a) closes the
identification transfer = eta(k) negative at the exact-coefficient
level, or (b) says the coefficient beta_i [SSq] = 0.344 is not the
number that multiplies (k/k_c)^2 in eta(k) - Q-250 decides which, and a
larger, longer run (8 nm, 1-2 ns, PME) sharpens the factor 1.47 before
either is written into a theorem.

## 6. Ruling Q-250 (Daniel's)

Which observable canonizes "the hydrodynamic velocity field's transfer
above k_c"? (a) eta(k) from the TCAF - proposed here, standard, tool-
supported, the natural meaning of momentum transfer; (b) the transverse
dispersion / damping of C_T(k, omega) - the onset and decay of propagating
shear waves, the IXS "transverse signature"; (c) a coarse-grained field
spectrum - kernel-dependent, not recommended. The instrument computes (a)
and stores C_T(k, t) so (b) can be read from the same run; the paper that
grades the data will grade whichever Daniel canonizes, and (a) unless he
says otherwise.

## 7. Honesty inventory (Rule 7)

1. The defect was the program's own (PAPER_2276 sec 6.4); it is named
   here in full and the front is re-posed before any data.
2. Data: one run, one box, one seed, 240 ps, reaction field not PME,
   eta_0 20 pct above the model's published value. The result is the
   scale (c_0, not c_inf) and the direction; the coefficient 0.344 is
   NOT confirmed (measured scale 1.47x in k); the shape is undecided.
   Front 4 is neither passed nor closed - it is measured once, honestly.
3. Published a for water was not obtained (full texts unreachable); this
   run's own a is 0.0056 nm^2 at the Gaussian reading. The diffusion
   coefficient was not reliably extracted (single-origin MSD without
   system-drift removal) and is not used for validation; E/N, force-energy
   consistency and energy conservation are.
4. eta(k) as "transfer" is a proposal (Q-250), stated as such; the
   prediction table is exact for that reading.
5. The OpenMM script on the wheel (front4_tcaf.py) was NOT the instrument
   used; the numpy engine was, and every line of it ships with this band.
   The record run should still be 1-2 ns in an 8 nm box with PME.
   Estimator dependence (Green-Kubo integral vs gmx-form fit: k_c 7.8 vs
   4.4) is disclosed as the width of the result.
6. Not claimed: anything about fronts 1-3 (unchanged); that the equi-
   partition observation is new to physics (it is elementary; what is new
   is that the program's test had rested on it).

## 8. Cross-references

PAPER_2276 (index; sec 6.4 corrected here), PAPER_2275 (Theorem B sec 7,
the roll-off), PAPER_2267 (k_c, the mode count), PAPER_2261 (c_0),
Q-247 (c_inf), PAPER_1042 (the Gaussian tail), PAPER_2270 (proof set).
External: Palmer PRE 49, 359 (1994); Hess JCP 116, 209 (2002); gmx tcaf.
