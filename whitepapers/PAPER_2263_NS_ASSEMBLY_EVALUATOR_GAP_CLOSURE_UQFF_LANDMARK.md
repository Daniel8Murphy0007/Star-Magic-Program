# PAPER_2263 - THE NAVIER-STOKES ASSEMBLY: THE EVALUATOR GAP CLOSURE (UQFF LANDMARK)

**Author:** Daniel T. Murphy / Star-Magic Research Program
**Date:** 2026-09-09
**Order:** Daniel, 2026-09-09 - "USE THE INDEPENDENT EVALUATOR. FINISH PUTTING THESE PIECES TOGETHER."
**Band:** v0.429.0 (B267)

## 1. The gap analysis (independent evaluator, 2026-09-09)

The evaluator's finding on star-magic-program 0.427.0: "The algebraic cap
is wired. The time ODE, Stam solver, and DNS falsifier are not." The
Taylor-Green ODE lived only in uqff 5.86.0
(_l96_uqff_taylor_green_*); the actual fluid lived only in the
predecessor repo's C++ (Core/FluidSolver.cpp, Rule E read-only); the
0.427 package stored UA = 0.4816 but never computed Lambda.

## 2. Wire order executed (all five items)

**(1) The PAPER_1232 time ODE, in-package** (`uqff_ns_assembly`):
Lambda = 1/(8 pi beta_i UA (D_crit/D_BSFG)^2) = 0.0072977 computed LIVE
from registry primitives; effective growth C*Lambda*sqrt(Omega0) - gamma
= -0.09944 < 0; damped branch Omega(t) = Omega0*exp(-nu*t) with
nu = 1/1600 = 1/(D_phys^2 SO_5^2) EXACT (PAPER_1723);
globally_regular() -> T* = infinity. Omega(t=10) = 3.6780419018718695
bit-matches the 5.86.0 formula.

**(2) The cap returns the curve**: navier_stokes_enstrophy_cap(t)
now returns E(t) = E0*exp(-(F_TRZ/Phi_5/6)*nu*t), coefficient
3/25 = 0.12 EXACT; bare call still returns 17/20 (every prior pin holds).

**(3) Stam in pure Python, labeled honestly**: 3D stable-fluids port at
the PAPER_177 FluidSolver parameters (N=32, dt=0.1, visc=1e-4) with the
PAPER_369 SCm jet body force; verification run N=32 x 5 steps bounded
(max speed 0.499, enstrophy finite). LABEL CARRIED IN THE RETURN:
NUMERICAL_EVIDENCE, not a proof - PAPER_177/179's own flag, preserved.
No third-party dependency (v0.406.0 lesson); no C++ sidecar needed to
draw the envelopes.

**(4) PAPER_543 fourth route wired**: lambda_max = 2*P_order/3 =
6.67e-6 < 1 (contraction on the discrete hypergraph).

**(5) The falsifier, left open ON PURPOSE**: DNS trefoil collision at
Re = 1e6 (PAPER_1182 falsifiable #5). If the vorticity peak is unbounded
there, the 17/20 cap is dead. NO in-package substitute is offered - a
fake falsifier would be worse than none.

## 3. Guards and disclosures

- SPE dispatch 'navier_stokes' -> 8.5e3 is a DIFFERENT construct;
  gate-pinned never to occupy the 0.85 slot.
- VALUE-COINCIDENCE FLAG: Lambda = 0.0072977 sits 0.004% from
  alpha = 0.0072974. No corpus chain connects them. FLAGGED, not
  canonized, per the standing discipline.
- Still OPEN (unchanged by this band): eta_K inputs (Q-098, B126);
  Clay-standard H^s estimates (PAPER_102 sec 5's own limitation);
  the Re=1e6 trefoil DNS.

## 4. The four-layer NS solution, now all live

S0 microphysics nu_eff = nu*1.0099 (PAPER_102, B126) / astrophysical
encompassment u <= sqrt(GM/r) (PAPER_529) / canonical cap 17/20 +
decay 3/25 (PAPER_1182, PAPER_2238 trace) / Taylor-Green numeric
instance T* = infinity (PAPER_1232) - plus the PAPER_543 discrete
route and the Stam numerical evidence. One falsifier named, standing.

## 5. Cross-references

PAPER_102, PAPER_177, PAPER_179, PAPER_369, PAPER_429, PAPER_529,
PAPER_543, PAPER_1182, PAPER_1232, PAPER_1723, PAPER_1724, PAPER_2098,
PAPER_2236, PAPER_2238; B126 (Q-098 ruling), B267 (this band);
independent evaluator gap analysis 2026-09-09 (Daniel-supplied).


---

## REVISION 2026-09-09 - THE THREE TIERS (Daniel's order: "TIER 1, THEN TIER 2, THEN TIER 3")

The riddle answered in code. Why is the easiest field the hardest to
draw? Because the field has no closed form - (u.grad)u couples every
scale to every scale (that IS the Millennium problem), and Kolmogorov
demands ~Re^(9/4) grid points, ~1e13 at the falsifier's Re=1e6. The
three-tier answer, each tier honest about what it is:

**TIER 1 - the field, drawn, zero dependencies:** the Stam solver now
returns its fields; `vorticity_slice` + `write_ppm` + `ascii_heatmap` +
`draw_field` render the mid-plane |omega| slice as terminal art and as a
binary PPM heat map. New CLI: `star-magic fluid [--n 32] [--out f.ppm]`.
Every return carries COARSE_FIELD_LABEL: a picture of a coarse
simulation, not of the true field.

**TIER 2 - the fast engine, guarded:** `stam_numerical_evidence_fast`
(same algorithm, numpy-vectorized, N=128-256 on a desktop) behind the
`[cfd]` optional extra. Absent numpy it raises a clear ImportError
naming `pip install star-magic-program[cfd]`. Base package stays
dependency-free; the gate is REHEARSED with numpy blocked (v0.406.0
standing lesson) and stays green.

**TIER 3 - the falsifier harness, data-gated:** `grade_cap_against_dns`
grades REAL outside data against the 17/20 cap (stretching-ratio mode)
or the 3/25 decay envelope (enstrophy mode, needs nu). With no dataset
it REFUSES, naming the outside paths: Johns Hopkins Turbulence Database
(public 8192^3 DNS), Kerr trefoil-reconnection DNS, Kleckner & Irvine
lab trefoils. The gate's synthetic self-check proves only that the
harness DISCRIMINATES (a ratio above the cap is reported as THE CAP IS
DEAD, plainly) - synthetic data is never presented as evidence.
Dataset acquisition rides Daniel's ledger next to the GFZ deep-sonic
file.

Resolution honesty, stated everywhere it acts: tier 1 and tier 2 draw
Stam evidence at coarse N; only tier 3's outside DNS data can settle
the Re=1e6 question. Nothing in this package claims otherwise.


### CORRECTION 2026-09-09 (same band, Rule 7) - tier 2 dependency claim

The REVISION above described tier 2 as a "[cfd] optional extra" over a
"dependency-free base." That is FALSE for star-magic-program: numpy (and
scipy) are REQUIRED dependencies in pyproject, and the fidelity gate
itself refuses to run without them - which is exactly how the error was
caught: the blocked-numpy rehearsal, run per the v0.406.0 lesson,
stopped at the gate's own dependency check. The dependency-free
discipline belongs to the SIMULATOR CATALOGUE (uqff_downhole_simulator),
not to the corpus package. Disposition: the redundant [cfd] extra is
removed; the fast engine works on every normal install; the guarded
import stays as defensive coding for stripped environments, with the
correction recorded in its own message string. The rehearsal that was
meant to protect the claim is what disproved the claim - standing
evidence that the rehearsal step earns its place in ship prep.
