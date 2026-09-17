# md_grade — the front-4 instruments (B286b, B287) and the Q-251 argon test (B288)

Everything here is source and data; nothing is compiled on the wheel.

| file | role |
|---|---|
| `md_engine.py` | B286b: rigid TIP4P/2005 water MD in numpy, reaction-field electrostatics (site cutoff). The first measurement's engine. |
| `front4_run.py`, `front4_analyze.py` | B286b run and analysis (`front4_eta_k.csv`, `front4_main_analysis.json`, `front4_main_run.log`, `front4_nve_check.txt`). |
| `front4_tcaf.py` | The OpenMM route (never run here - package index unreachable); kept as the gmx-tcaf-comparable script. |
| `md_pme.py` | B287: the SPME engine (`WaterPME`, `PME`); subclasses `md_engine.Water`. |
| `pair_kernel.c` | B287: C kernels - real-space pairs (cell list, erfc table), RATTLE, SPME spread/gather, exact currents. Build: `gcc -O3 -march=native -fopenmp -shared -fPIC -o pair_kernel.so pair_kernel.c -lm` |
| `gridcur.py` | B287: transverse currents for a set of k-vectors by B-spline/FFT momentum-density transform. |
| `ewald_ref.py` | B287: explicit-Ewald reference (direct k-sum) used to validate the C kernel and the SPME. |
| `validate.py` -> `validate.out` | The validation ladder: Madelung (NaCl), C vs numpy, SPME vs direct, forces vs finite differences, timings. |
| `validate_gridcur.py` -> `validate_gridcur.out` | FFT currents vs the exact sum, by k band. |
| `nve_pme.py` -> `nve_pme.out` | Energy conservation at 2,197 molecules. |
| `front4_record.py` | The record run: equilibration, k-shell selection, on-the-fly autocorrelator in blocks, multi-origin MSD subset, checkpoint/restart. `python front4_record.py <n_side> <ps> <tag> [--seed N] [--restart]` |
| `rec_analyze.py`, `rec_pool.py` | Per-run analysis (eta(k) per shell on COM and atomic currents, block errors, Gaussian/Lorentzian fits, shear-wave onset, D) and seed pooling. |
| `rec_B13s1{1,2,3}_analysis.json`, `rec_C20_analysis.json`, `pool_B13.json`, `rec_*.log` | The four runs' analyses and logs. |
| `front4_record_eta_k.csv`, `front4_record_summary.json` | What the harness (`uqff_ns_assembly.front4_record_grade`) grades. |
| `lj_kernel.c` | B288: Lennard-Jones cell-list kernel (energy-shifted 12-6, OpenMP). Build: `gcc -O3 -march=native -fopenmp -shared -fPIC -o lj_kernel.so lj_kernel.c -lm` |
| `argon_record.py` | B288: the Q-251 argon run - velocity Verlet, transverse + longitudinal currents (`gridcur.currents3`), correlator, MSD, checkpoint/restart. Needs `pair_kernel.so` built too (gridcur's spreader). |
| `validate_argon.py` -> `validate_argon.out` | Kernel vs numpy, forces vs finite differences, equilibration, NVE at 4,096 atoms. |
| `ar_analyze.py` | Per-run analysis: eta(k) per shell, Gaussian/Lorentzian fits, longitudinal dispersion, D, the P1/P2 ratios. |
| `ar_s1_analysis.json/.txt`, `ar_s2_analysis.json/.txt`, `pool_argon.json`, `ar_s1.log`, `ar_s2.log` | The two seeds and their pooling. |
| `q251_argon_eta_k.csv`, `q251_argon_summary.json` | What the harness (`uqff_ns_assembly.q251_argon_grade`) grades against the pre-stated P1 / P2. |

The raw correlator archives (`rec_*.npz`, 90-110 MB each) are not on the
wheel; every number in the JSONs and the CSV is regenerable from the
scripts above with the seeds given in the logs.
