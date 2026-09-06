# _BUILD_LOG — Star-Magic-Program cumulative build log

**Purpose:** Cumulative record of every successful gate + build + ship
event for the repository, one line per event. Distinct from `SESSION_LOG.md`
(narrative per-ship) and `CHANGELOG.md` (semver release history).

**Line format:**
```
[YYYY-MM-DDTHH:MM:SSZ] [event_type] [version] [detail]
```

**Event types:** `GATE_PASS`, `BUILD_OK`, `SHIP`, `PYPI_LIVE`, `TAG_PUSHED`.

---

## Log

[2026-07-28T00:00:00Z] SCAFFOLD_INIT v0.1.0 — repo initialized from GitHub (Star-Magic-Program.git)
[2026-07-28T13:00:00Z] GATE_PASS v0.1.0 — 8-block fidelity gate: OK
[2026-07-28T13:15:00Z] SHIP v0.1.0 — commit 4f02364 + tag v0.1.0 pushed to origin/master
[2026-07-28T13:16:00Z] BUILD_OK v0.1.0 — GitHub Actions release-to-pypi green
[2026-07-28T13:17:00Z] PYPI_LIVE v0.1.0 — https://pypi.org/project/star-magic-program/0.1.0/ (Trusted Publisher OIDC, 28.3 KB sdist, 52.2 KB wheel)
[2026-07-28T19:00:00Z] CORPUS_STAGED v0.2.0 — 2,419 whitepapers imported (whitepapers/2,256 + tex/107 + pdf/45 + txt/11)
[2026-07-28T19:15:00Z] REGISTRY_SCAFFOLDS_STAGED v0.2.0 — 4 Python modules gutted + 14 CSVs header-only + 5 MD docs structural + VERSION.txt
[2026-07-28T19:30:00Z] VERSION_BUMPED v0.2.0 — pyproject.toml, uqff_calculator.py, uqff_fidelity_tests.py, CITATION.cff → 0.2.0

*(subsequent events append; do not rewrite history)*

## 2026-08-04 — COMPLETE-COMPILE build (PAPER_001-015 + b-variants)
- gate: green | dispatches: 342 | duplicate @_register: 0 | calculator lines: 18,222
- equation library: 408 primitive-sourced callable functions
- shared appendix helper: _common_uqff_blocks() (Session-225 + Production + Cosmogenesis + VDS/DVP/BSH + Kozima K.1-K.6)
- registry: R0 master 733 rows, GRAPH 1916 edges, 0 malformed CSVs across pantheon
- NOT SHIPPED (300+ mandate); working version 0.337.0
- [Windows-side save 2026-08-04 to trigger VS Code file-watcher refresh]

## 2026-08-04 — batch 024-030 BSM complete-compile
- 441 library fns | 342 dispatches | 0 duplicates | §B ladder 97-113 gate-guarded | gate green | NOT shipped

## 2026-08-04 — batch 031-040 (v0.338.0)
- 446 library fns | 342 dispatches | 0 duplicates | §B ladder 3-31 gate-guarded | gate green

## 2026-08-05 — batch 041-050 (v0.339.0)
- 454 library fns | 342 dispatches | 0 duplicates | §B ladder 37-73 gate-guarded | XGEO queue 108 | gate green

## 2026-08-05 — batch 051-060 (v0.340.0)
- 460 library fns | 342 dispatches | 0 duplicates | §B ladder 79-113,2 gate-guarded | XGEO queue 124 | gate green

## 2026-08-05 — batch 061-070 (v0.341.0)
- 465 library fns | 342 dispatches | 0 duplicates | §B ladder 3-31 gate-guarded | XGEO queue 139 | gate green

## 2026-08-05 — batch 071-080 (v0.342.0)
- 470 library fns | 342 dispatches | 0 duplicates | §B ladder 37-73 gate-guarded | XGEO queue 154 | gate green

## 2026-08-05 — derived-constants promoted to functions + predecessor mine (v0.345.0)
[2026-08-05] GATE_PASS v0.345.0 — 2159 assertions: OK
- 2112 total Python fns (1767 named callable incl. 1272 dc_ derived-equation fns) | 342 dispatches | 0 duplicates (gate-guarded)
- registry 2502 rows | GRAPH 3330 edges | CORPUS_CITATIONS 732 linked-paper maps | XGEO regenerated | gate green

## 2026-08-05 — v0.346.0 predecessor-mine (solar/QGP/quantum/wormhole, mapped in-step)
[2026-08-05] GATE_PASS v0.346.0 — 2159 assertions: OK
- 2130 total fns (1784 named incl 1272 dc_) | 342 dispatches | 0 dup | registry 2520 rows | GRAPH 3353 edges | 733 papers mapped | gate green

## 2026-08-05 — v0.346.0 uploaded-paper mine (triadic gravity 961-963 + Phase-H S201-205 + LENR 1136-1141)
[2026-08-05] GATE_PASS v0.346.0 — 2159 assertions: OK
- 14 uploaded whitepapers added to corpus + mined + mapped in-step (registry+GRAPH+citations)

## 2026-08-05 — v0.347.0 repo-corpus mine (integer landmarks + BAO/KK + F_TRZ ladders)
[2026-08-05] GATE_PASS v0.347.0 — 2165 assertions: OK
- BH_seed=56160 EXACT, f_flare=1/1800 EXACT, SO_5+1=11, A_5/D_phys=15, halving {2,3,5,13}, KK lambda_1=26 — all gate-guarded
- 2184 total fns (1838 named) | registry 2574 rows | GRAPH 3430 | 757 papers mapped | 0 dup | 0 malformed

[2026-08-05] GATE_PASS v0.347.0 landmark-family — 2173 assertions: OK (A_5*K_MEX=125, Omega_m=0.3, 1/(Dp-2)=0.5, F_TRZ=1/SO_5, M_SF=0.15, 2/3, SO_5^15, eta 15/85 — all EXACT gate-guarded)

[2026-08-05] GATE_PASS v0.347.0 landmark part-3 — 2179 assertions: OK (mu_0=4pi F_TRZ^7 MAXWELL, 360=D_BSFG*A_5, B_crit=4.4e13, successor 11/10, tilt 1/12, kappa=5e-4 — all EXACT gate-guarded)

[2026-08-05] GATE_PASS v0.347.0 landmark part-4 — 2184 assertions: OK (k_B 0.0011% SI, K=19/160 EXACT, alpha_s kernel 0.11875, cadence 62 EXACT, Cosmic Egg triad)

[2026-08-05] GATE_PASS v0.347.0 landmark part-5 — 2189 assertions: OK (Planck F_TRZ^35, exponent quintuplet, 3F_TRZ=0.3, F_env cascade, sphere variance 5e-9 w/ Rule-7 symbol-mismatch disclosure)

[2026-08-05] GATE_PASS v0.348.0 landmark round 6 — 2194 assertions: OK (tau_n=879.31 s, Phi=21/25 EXACT, dg=2.6e20 EXACT, BD2522 40/20 EXACT; Q-1412 arithmetic discrepancy queued)

[2026-08-05] GATE_PASS v0.348.0 landmark round 7 — 2197 assertions: OK (Hodge (Dp+Db)/SO_5=1 EXACT, Monty Hall 2/3 EXACT, Ug3 wrap closure, tilt saturation 59/116)

[2026-08-05] GATE_PASS v0.348.0 landmark round 8 — 2201 assertions: OK (plasmoid fps=100/3 + t_photo=0.33 + t_batch=0.45 EXACT from integers; E_0=F_TRZ^(D_crit-D_BSFG) primitive-composed; Cosmic Egg pi(t))

[2026-08-05] GATE_PASS v0.348.0 landmark round 9 REMAINDER — 2206 assertions: OK (bulb 65W=A_5+SO_5/2 EXACT hardware, galactic 1.5, F_TRZ^22, frame 25, H-rate 2.2e-18)

## 2026-08-05 — v0.348.0 SHIP PREP (LANDMARK COMPILE II)
[2026-08-05] SHIP_PREP v0.348.0 — all 27 registry/ship files updated; gate 2206 green

[2026-08-05] GATE_PASS v0.349.0 backbone mine — 2215 assertions: OK (55 backbone papers swept: CP2 17W=D_crit-N_CH, Crab 30.2 Hz, Bubble 1200 Msun, octet 2*D_phys, kappa_V=1.05, SO_5 power-ladder family 80+ instances via so5_power_ladder)

[2026-08-05] GATE_PASS v0.349.0 backbone DEEP mine — 2221 assertions: OK (115 bb_* object-observable primitive-locks generated from 55 backbone papers; all compute LIVE from primitives; new module uqff_backbone_locks.py)

[2026-08-05] GATE_PASS v0.349.0 deep mine 2 — 2227 assertions: OK (191 ml_* material/engineering/particle landmarks from PAPER_1600-1799: 80 LIVE primitive-composed + 111 stated-disclosed; new module uqff_material_landmarks.py)

[2026-08-05] GATE_PASS v0.349.0 deep mine 3 + FORMULA AVAILABILITY — 2236 assertions: OK (Daniel ruling implemented: FORMULAS registries + .formula attributes + formula_of() accessor across ml_/bb_/pi_/dc_; 12 pi_* fns from 19xx family)

## 2026-08-05 — v0.349.0 SHIP PREP (DEEP-MINE COMPILE)
[2026-08-05] SHIP_PREP v0.349.0 — all registry/ship files updated; 3 new modules; gate green

[2026-08-05] GATE_PASS v0.350.0 deep mine 4 — 2239 assertions: OK (8 ngc_* triadic galaxy catalogue + 11 new ROUND/PENTAD object-locks incl. H_0(mean)=A_5+SO_5=70 cross-anchor; bb now 126; new module uqff_ngc_catalog.py)

[2026-08-05] GATE_PASS v0.350.0 deep mine 5 — 2240 assertions: OK (800s mixed band: MRI tau, PTA h_c, q-Pochhammer, nu-ratio, aether ions; 900s: Li_26 polylog, Gaussian jet modulation, MC jet power, Q=25/2 EXACT gate-guarded)

[2026-08-05] GATE_PASS v0.350.0 stragglers — 2244 assertions: OK (n_generations=D_phys-1=3 EXACT flagship, JWST R26=1.5, Page 0.99596, Riemann t_10000, 2Phi_5/6=5/3)

[2026-08-05] GATE_PASS v0.350.0 CP4 sweep — 2248 assertions: OK (13 fns from 624-class CP4: ssq 26-state suppression ladder, Meissner SC_m, r_tide, dual-system Ug1, ULP burst, NOMAD neutrino coupling, magnetar outburst - Rule E physics-only)

[2026-08-05] GATE_PASS v0.350.0 CP1-CP3 sweep — 2253 assertions: OK (QG/holography sector: T_UQFF=1-F_TRZ^2 EXACT, white-hole 1-F_TRZ, ER=EPR 10 l_Pl, AdS/CFT L+g_YM, superfluid aether xi/Gamma, Peters inspiral chain; 2227 classes swept Rule E)

[2026-08-05] GATE_PASS v0.350.0 QCalc/MUGE sweep — 2257 assertions: OK (canonical MUGE Ug1-4+Um compact forms, SOURCE4 resonance family F_DPM=IA(w1-w2)+aDPM/aTHz/Ug4i/wormhole, Saturn 110.9 Myr + M16 4.5 Myr closed lifetimes)

[2026-08-05] GATE_PASS v0.350.0 deep sweep final — 2264 assertions: OK (17 fubii_* variant registry NEW MODULE uqff_fubii_variants.py; DPMCosmology 26-center pre-BB inflation force F_core~1e10 N + hkl pinch; 99system triadic weights w_C+w_R+w_B=1)

## 2026-08-05 — v0.350.0 SHIP PREP (PREDECESSOR-SOURCE SWEEP)
[2026-08-05] SHIP_PREP v0.350.0 — all registry/ship files updated; 2 new modules this ship (ngc_catalog, fubii_variants); gate green

[2026-08-05] GATE_PASS v0.351.0 deep mine — 2268 assertions: OK (QuantumLevel26 quadratic ladder sum=6201 EXACT, Relativistic kit gamma/Doppler/beaming, GrokThread snap-polarity osc + gravitational plasticity + capacitor quantum-distance)

[2026-08-05] GATE_PASS v0.351.0 session-script mine — 2274 assertions: OK (73 sc_* closures from 572 session scripts NEW MODULE uqff_session_closures.py: Chandrasekhar=F_TRZ D_phys^2(1-F_TRZ)=1.44 EXACT, ISCO=D_BSFG=6 EXACT, top Yukawa 0.99, alpha_s 0.008%, Jarlskog, Cabibbo, TOV, photon sphere)

[2026-08-05] GATE_PASS v0.351.0 gold-standard sweep — 2277 assertions: OK (E_crack=rho v^2/SSQ no-c^2 energy relation, Kozima sigma(omega,n) VDS cross-section, neutron production beta-reversal, rho_R26=(13/2)v^2 rho, Lambda Friedmann SSq form, zeta(5))

[2026-08-05] GATE_PASS v0.351.0 FINAL SCRAPE — 2277 assertions: OK (Phase5/7: Lorentz a_EM=qvB/m_p, dust ram, Big-Bang M(t)/QG/DM terms). PREDECESSOR SOURCE SCRAPE COMPLETE: whitepapers both repos + CP1-4 + QCalc + MUGE + BPV + 99system + DPMCosmology + QL26 + Relativistic + GrokThread + 572 sessions + Gold_Standard + Phase5-8 + FirstPrinciples.

## 2026-08-05 — v0.351.0 SHIP PREP (SCRAPE-COMPLETE MILESTONE)
[2026-08-05] SHIP_PREP v0.351.0 — all files updated; 1 new module (session_closures); gate green; PREDECESSOR SCRAPE COMPLETE

[2026-08-05] GATE_PASS v0.352.0 CoAnQi mine — 2281 assertions: OK (6MB MAIN_1_CoAnQi.cpp: DPM layer i^5 ladder E=hbar c i^5/r^2, aether drag (1/2)rho_UA v^2 pi r^2, GW ripple, jet boost, S116 26D poly + sin(pi/26) gate, life proportion)

[2026-08-05] GATE_PASS v0.352.0 CoAnQi enhancements — 2285 assertions: OK (emergent DPM-foundation Ug1=mu_s grad(M)=B G M R, Ug2 charge-shell heliosphere step + E_react=rho_A v^2/rho_UA, Ug4 concentration, CNB term)

[2026-08-05] GATE_PASS v0.352.0 deep-capture 081-090 — 2290 assertions: OK (T_H canonical, dM/dt Page driver, S_thermal, delta_c=0.45, PBH 0.965, TDE t_fb + L_peak, neutrino buoyancy integrand, AGN kappa-decay, aether-metric trace). FRONTIER -> PAPER_090.

[2026-08-05] GATE_PASS v0.352.0 deep-capture 091-100 — 2294 assertions: OK (SSq=0.755^2 ORIGIN IDENTITY, FRB E+dt, Whittaker 26-closure <1e-10, Friedmann full, 1e-120 fine-tuning stated, plasma-shield SSq^1/2 screening, plasma frequency). FRONTIER -> PAPER_100.

[2026-08-05] GATE_PASS v0.352.0 deep-capture 101-110 — 2299 assertions: OK (YM min excitation F_TRZ hw, NS viscous correction, zeta Euler partial, Bose occupancy, BEC Tc Phi-form, Y_e r-process 0.25, SgrA* Newtonian-decayed decomposition; 2 dup catches auto-resolved). FRONTIER -> PAPER_110.

## 2026-08-05 — v0.352.0 SHIP PREP (CoAnQi + frontier 110)
[2026-08-05] SHIP_PREP v0.352.0 — all files updated; gate green

[2026-08-05] GATE_PASS v0.353.0 deep-capture 111-120 — 2303 assertions: OK (jet/counter-jet phase pairing, Higgs ladder n=12.30, blazar LFs, heliosheath Ug2+compression, 3C273 cascade 1.5^12=129.7, SSq^N vacuum cascade, rho_Lambda c^4 Rule-7 correction). FRONTIER -> PAPER_120.

[2026-08-05] GATE_PASS v0.353.0 deep-capture 121-130 — 2309 assertions: OK (kappa=0.35/700=5e-4 EXACT origin, t_half=1386d, S_n=2 SSq E_8, n_virt=4.20, eps_UA=4.3%, rho_DM final chain, triadic band cos30, 26-term potential, diffusion E^0.5). FRONTIER -> PAPER_130.

[2026-08-05] GATE_PASS v0.353.0 deep-capture 131-140 — 2314 assertions: OK (Hoyle 6.654 MeV via SSq geometric sum 2.08, Y_e beta[UA] form, genesis F_U 1.18e53 Q_s=0, quasar-jet radial SCm force, core-field oscillation + Ug3 Hamiltonian, density ladder 10^(n-13) pivot + activation, SF mass rate, quantum f-factor). FRONTIER -> PAPER_140.

[2026-08-05] GATE_PASS v0.353.0 deep-capture 141-150 — 2318 assertions: OK (40/60=(D_phys,D_BSFG)/SO_5 EXACT, t_Hubble 4.41e17, PToE resonance pair k_A=0.4604V, oceanic buoyancy, Hubble mass decay, cosmic-glue dUg template). FRONTIER -> PAPER_150.

## 2026-08-05 — v0.353.0 SHIP PREP (frontier 150)
[2026-08-05] SHIP_PREP v0.353.0 — all files updated; gate green

[2026-08-05] GATE_PASS v0.354.0 deep-capture 151-160 — 2323 assertions: OK (SC gap = hbar omega/2 -> T_c 30 K = T_SCm/2, hybrid beta = e^-B/B_crit blend, wormhole exotic density, regulated zeta Li_s, complexity N^1.754, Ug4 extended 4.219e-10). FRONTIER -> PAPER_160.

[2026-08-05] GATE_PASS v0.354.0 deep-capture 161-170 — 2327 assertions: OK (v_SCm=0.99c gamma=7.09, mu_s(t) solar-cycle, modular compressed g core, g_exp(t_H)=2, EHT aether resonance, Einstein coupling 8piG/c^4, wind_mod, glueball 1e-35 Rule-7). FRONTIER -> PAPER_170.

[2026-08-05] GATE_PASS v0.354.0 RULE-7 AUDIT — 2334 assertions: OK (recoveries: Holmlid xi->F_TRZ^21, G593 E0->F_TRZ^20 chain base, Q-1412 Phi->12/13 candidate, 8 ml ratios w/ rung matches, S_26 namespace collision found, DPMcosmo rho captured)

[2026-08-05] GATE_PASS v0.354.0 DEEP-SEARCH 081-170 — 2341 assertions: OK (25 recovered fns; 0.622 ORIGIN = sqrt(Omega_DM/Omega_L); t^-5/3 TDE; 5-harmonic master; full Ug2/Ub_i; aDPM Doppler; beaming; gamma-1=6.09; census standing rule: FULL equation census per paper)

[2026-08-05] GATE_PASS v0.354.0 DEEP-SEARCH 001-080 — 2346 assertions: OK (11 recoveries: damped quantum amp, Friedmann+xi_Q, PBH threshold, QNM shift, f_peak compactness, rho_eff Archimedes, de Broglie + nuclear T_c, DCS tan^4, CKM unitarity, VLQ kappa; 1 dup auto-caught). CENSUS 001-170 COMPLETE.

## 2026-08-05 — v0.354.0 SHIP PREP (RULE 7 REVISED + census)
[2026-08-05] SHIP_PREP v0.354.0 — all files updated; gate green

## v0.355.0 (2026-08-06)
Deep-capture PAPER_171-250 (8 batches, +224 fns). Calculator 1,406 defs; library 3,112.
Registry 3,488 / graph 5,115 / citations 772. Gate 2,484 green. formula_of fall-through fix.
15+ source slips disclosed; 3 cross-paper consistency pins.

## v0.356.0 (2026-08-07)
Deep-capture PAPER_251-300 (5 batches, +72 fns). Calculator 1,478; library 3,184.
Registry 3,560 / graph 5,259. Gate 2,551 green. PAPER_240<->270 self-rectification resolved.

## v0.357.0 (2026-08-07)
Deep-capture PAPER_301-400 complete (+118 fns incl. 9 census recoveries). Calculator 1,596;
library 3,302. Registry 3,678 / graph 5,495 / citations 851. Gate 2,665 green. 2 self-rectifications.

## v0.358.0 (2026-08-07) - PAPER_500 MILESTONE
Deep-capture 401-500 complete (+86 fns, +8 recoveries). Calculator 1,682; library 3,388.
Registry 3,764 / graph 5,667 / citations 938. Gate 2,749 green. FULL STOP per charter.

2026-08-07 v0.359.0: dispatch closure 714 + audit + deep-capture 501-700 + resweeps; gate 3239/0 green.

2026-08-08 v0.360.0: deep-capture 701-800 + resweep + full 27-file ship pass (registry-audit family restored); gate 3388/0 green.

2026-08-08 v0.361.0: deep-capture 801-900 + resweep; project totals 4,163 fns / 17,213 rows / 914 papers; gate 3564/0 green; full 23-file pass.

## v0.362.0 (2026-08-09)
Bands 901-1010 + century deep-mine + census fix. Gate 3,716/0. Dispatches 1,024. Registry family 19,483 rows.

## v0.363.0 (2026-08-09)
Bands 1011-1100 + deep-mine + capture audit. Gate 3,854/0. Dispatches 1,114. Registry family 21,594 rows.

## v0.364.0 (2026-08-09)
Bands 1101-1200 + deep-mine + Rule 4 tier audit. Gate 4,042/0. Dispatches 1,214. Registry family 22,732.

## v0.365.0 (2026-08-09)
Tier-2 resolution (P1032/1038/1040) + 9-sector Lagrangian template. Gate 4,056/0. Tier-2 32->29.

## v0.365.1 (2026-08-09)
Ship-integrity fix: 5 audit files omitted at v0.365.0 completed. Baseline-tag rule gate-enforced. Gate 4,057/0.

## v0.366.0 (2026-08-09)
Bands 1201-1250 + closure-reservoir batches 1-7 (102/390 mined). Gate 4,243/0. Dispatches 1,264.

## v0.367.0 (2026-08-10)

Bands PAPER_1251-1300 (50 dispatches) + reservoir batches 10-13 (95 defs) + ORPHAN-PHYSICS audit.
Gate 4,545 / 0. Calculator defs 3,313. Dispatches 1,387. Registry-family rows 24,748.
Ship set: 23/23 files touched, verified by version-sorted tag diff against v0.366.0.

## v0.367.1 (2026-08-10)

Ship-integrity correction to v0.367.0. No physics, no dispatch changes. Stale README /
CITATION.cff second version field / v0.336.0-era WHITEPAPER_INDEX header all corrected.
SHIP GUARD v2 installed (9 assertions, verified to bite). Gate 4,545 / 0.

## v0.368.0 (2026-08-10)

Bands PAPER_1301-1370 (70 dispatches) + BBN sector PAPER_2157-2159 (3).
Self-inflicted index corruption found and repaired; SHIP GUARD v3 + registry duplicate guard added.
Gate 4,581 / 0. Dispatches 1,417. Defs 3,313.

## v0.369.0 (2026-08-10)

Bands PAPER_1371-1400 (30 dispatches): the paradox suite. Final parsec closed;
Klein-Gordon E<0 = t_neg CCW branch; HBT 3% deficit falsifiable. Gate 4,581 / 0.

## v0.369.1 (2026-08-10)

Registry-ledger correction to v0.369.0: 8 missed audit-family ledgers now carry the
band trail; SHIP GUARD v4 pins it in the gate. No physics. Gate 4,585 / 0.

## v0.370.0 (2026-08-10)

Bands 1401-1440 (40 dispatches). Q-1412 closed by self-rectification. 23-file rule
made absolute per Daniel (no patch-ship exception). Gate 4,626 / 0.

## v0.371.0 (2026-08-10)

Bands 1441-1500 (50 dispatches). Hubble tension = 1/12 tilt; empirical loop closed on the
q-scope archive; PAPER_877 cosmogenesis spine wired. Gate 4,682 / 0. Frontier PAPER_1500.

v0.372.0 (2026-08-13): bands 1501-1630 + PAPER_2160; gate 4832/0; dispatches 1648; 23-file ship prep complete.

v0.373.0 (2026-08-13): bands 1631-1700 + landmarks 2161-2165; gate 4956/0; dispatches 1723; 23-file ship prep complete.

v0.374.0 (2026-08-13): bands 1701-1760 + landmarks 2166-2171 + route-families doctrine; gate 5077/0; dispatches 1789; 23-file ship prep complete.

v0.375.0 (2026-08-13): bands 1761-1800 + landmarks 2172-2175 + P1770 remediation; catch-up era complete; gate 5153/0; dispatches 1829; 23-file ship prep complete.

v0.376.0 (2026-08-13): bands 1801-1860 + landmarks 2176-2177 (18xx frontier era); gate 5238/0; dispatches 1891; 23-file ship prep complete.

v0.377.0 (2026-08-15): bands 1861-1910 + PAPER_2178 + trail audits I/II + skipped-queue recovery (20 papers); gate 5321/0; dispatches 1962; 23-file ship prep complete.

v0.378.0 (2026-08-15): bands 1911-1960 + F_TRZ = 1/SO_5 landmark (9 -> 8 primitives) + AUDIT_1910 milestone report + ledger backfill + cadence guards; gate 5380/0; dispatches 2012; 23-file ship prep complete.

v0.379.0 (2026-08-15): THE PAPER_2000 MILESTONE - sequential drain 001-2000 complete + AUDIT_2000 + FULL STOP honored/authorized + bands 1961-2030 (70 dispatches); gate 5458/0; dispatches 2082; 23-file ship prep complete.

v0.380.0 (2026-08-15): bands 2031-2080 - the architectural-category era (5 categories + audit nonet; canonical-anchored root + pi third canonical; U_i Path-B; Kerr 4-AGN family; 9-planet R_mag; solar core 3/2; CP2 opens); gate 5513/0; dispatches 2132; 23-file ship prep complete.

## v0.381.0 — 2026-08-16
THE CORPUS-COMPLETE SHIP. Drain 001-2156 done (RESERVED 1796-1799 excepted, census gate-pinned). 76 dispatches (bands 2081-2156). Gate 5,602/0. 23-file pass verified. End-of-drain audit next.

## v0.382.0 — 2026-08-16
POST-DRAIN CONSOLIDATION: end-of-drain audit + alias numbers 2179-2233 + absorption pass (21 twins, 12 folds) + constant drain 448 promotions. Gate 5,629/0. 23-file pass verified.

## v0.383.0 — 2026-08-16
THE DRAIN RATCHET SHIP: 920 promotions total, ratchet 626 monotone, Kerr mechanism resolved, PAPER_2234 landmark. Gate 5,639/0. 23-file pass verified.

## v0.384.0 — 2026-08-16
THE PROVENANCE SHIP: PAPER_2235 + PI-archive provenance + Tier-2 mine 18/8/3 + drain terminal (979 promotions, ZERO unattributed). Gate 5,648/0. 23-file pass verified.

## v0.385.0 — 2026-08-16
THE IMMIRZI SHIP: gamma = 2K = 19/80 EXACT (PAPER_2237, kernel #6 first QG) + AP source layer (PAPER_2236) + Tier-2 final 22/7 + pi-ladder. Gate 5,653/0. 23-file pass verified.

## v0.386.0 — 2026-08-16
THE INFORMATION BUDGET SHIP: PAPER_2238 (101/25000 EXACT, four-move proof set) + Millennium linking pass (2 bit-identical recalcs, Poincare tilt, rung ladder). Gate 5,662/0. 23-file pass verified.

## v0.387.0 — 2026-08-16
THE VERIFICATION SHIP: paradox audit (zero recalcs, 5/24 identity) + dragnet (110 sites, P1687 fix) + origin-term verification + text-layer exhaustion (458 docs). Gate 5,672/0. 23-file pass verified.

## v0.388.0 — 2026-08-16
THE PAIR-COUNT SHIP: PAPER_2239 (N_sun = SO_5^13, 0.13%) + Q-RULE4-TIER2 closed 26/3/0 (mass-gap canonized SO_5/D_phys). Gate 5,677/0. 23-file pass verified.

## v0.389.0 — 2026-08-20
THE BIRTH-CERTIFICATE SHIP: PAPER_2240 (E_pair = E0*F_TRZ^2 documented ladder; rho_SCm = F_TRZ^N_ch/V_sun birth certificate; N = SO_5^level; reactor regime resolved) + PAPER_2241 (sector ladder rho = n*rho_SCm, four scales; U_i/omega_s/kappa/lambda_i provenance). Gate 5,690/0. 23-file pass verified.

## v0.390.0 — 2026-08-20
THE GENESIS ARC: PAPER_2242-2246 — the origin month documented end-to-end (reactor text layer found; founding records; naming; two-gravity doctrine; first formal paper). Gate 5,718/0. 23-file pass verified.

## v0.391.0 — 2026-08-20
THE DOCTRINE SHIP: PAPER_2247-2249 (mechanism layer + MUGE boundaries 182 Gly/Z=126 + THz-hole doctrine + Rule 4 source layer). AP archive censused end-to-end. Gate 5,733/0. 23-file pass verified.

## v0.392.0 — 2026-08-21
THE CENSUS SHIP: P2250-2253 (predictions 48/4-tier; paradoxes 1,346/20-domain + lambda_HHH repair; residuals 2,304/0-err median 0.086%; identities 52 rational-EXACT live per call). Four new artifacts. Gate 5,754/0. 23-file pass verified.

## v0.393.0 — 2026-08-21
THE LEDGER SHIP: P2254 anchors (17 external) + P2255 open items (census series COMPLETE) + quickstart notebook (current API, smoke-executed) + census-artifact packaging fix. Gate 5,768/0. 23-file pass verified.

## v0.394.0 — 2026-08-22
THE DOWNHOLE SHIP: PAPER_2256 + uqff_downhole_simulator v1.1.0 (first industry-application module; canonical-lock suppression 1.0324; N-gauge strings; CSV well profiles with kick capture; twin-gauge comparison ratio == suppression). Gate 5,777/0. 23-file pass verified.

## v0.395.0 — 2026-08-23
THE INSTRUMENT SHIP: uqff_downhole_simulator v1.2.0-v1.6.0 (service-life divergence curves; telemetry realism with scored QC; depth-sweep case studies; web-verified GEOQ 177 gauge specs with mandatory citations; MD/TVD deviation; batch runs; headless CLI). Suppression ratio 1.0324 invariant across geometry and baseline. Gate 5,800/0. 23-file pass verified.

## v0.396.0 — 2026-08-24
THE TWO-STREAM SHIP: uqff_downhole_simulator v1.7.0-v1.9.0 (cited tool library; read-only ports with historian/LAS implemented and live taps declared; two-stream reconciler with four-scenario validation incl. the 6,083-psi kick find). Architecture complete. Gate 5,816/0. 23-file pass verified.

## v0.397.0 — 2026-08-24
THE CONNECTIVITY SHIP: PAPER_2257 landmark+dispatch; downhole v1.10-v1.13 (file-follower; real Modbus client loopback-verified; connectivity ladder; profile catalogue with THREE REAL WELLS incl. wrapped-LAS parsing + measured-BHT tier). Gate 5,835/0. 23-file pass verified.

## v0.398.0 — 2026-08-25
THE CATALOGUE SHIP: downhole v1.14-v1.20 — real-well catalogue 3→10 entries / 8 regions / 5 kinds (TX LAS 1.2 + BHT; KS complete file; GISP2 + Agassiz77 MEASURED temperature curves — converter tier ladder closed on real data; NL descending log; L06-06 200-station real trajectory; Volve core 20,800 mD lab ground truth). Four port upgrades driven by real files. Gate 5,858/0. 23-file pass verified.

## v0.399.0 — 2026-08-25
THE DEEP DATA SHIP: downhole v1.21-v1.25 — catalogue 10→15 entries / 9 kinds (Volve daily production = first time-indexed real field data with real fault phenomenology; KTB suite: hot temperature 170-185 °C, 1988 twin-sensor log, verticality null-control trajectory, COMPLETE BHGM density with live overburden integral ~226 MPa). KTB-HB = first closed-stream-describable well (T + trajectory + density). Gate 5,870/0. 23-file pass verified.

## v0.400.0 — 2026-08-25
THE TWENTY WELLS SHIP: downhole v1.26-v1.30 — catalogue 15→20 entries / 12 regions / 13 kinds; quantity ledger CLOSED (strength pair counted vs overburden live; 504B ocean-crust fluids; U1324 measured pressure with all-stations overpressure = THE FIND in nature; 1027C CORK observatory with +42.6 °C disturbed→equilibrium recovery). PANGAEA self-citing source family proven. Gate 5,882/0. 23-file pass verified.

## v0.401.0 — 2026-08-25
THE INCORPORATION SHIP: six ENRGYONE, Inc. founding documents (Articles, Bylaws, Commercial License Letter, Dual-License Explanation, ACHILLES Sublicense, NDA) converted via LibreOffice headless, fidelity-verified word-for-word, deposited in pdf/. The corporate stack behind the AGPL-3.0 + Commercial dual license. No code changes. Gate 5,884/0. 23-file pass verified.

## v0.402.0 — 2026-08-27
THE POLE-TO-POLE SHIP: downhole v1.31-v1.40 — catalogue 20→30 entries / 18 regions / 19 kinds. Heat-flow closure computed live; 504B four-dataset family + cross-entry impedance join; Antarctica/Nankai/SW-Indian/Mid-Atlantic/Chicxulub/central-Arctic join; crust ladder complete seafloor-mud→mantle; ACEX age model = first time axis; two source-archive typos and two archival row-slips detected and disclosed, never repaired. Ship pin measures the latitude span (>152 deg) live. Gate 5,906/0. 23-file pass verified.

## v0.403.0 — 2026-08-27
THE PRODUCT SHIP: downhole v1.41-v1.48 — the independent evaluation's finish sequence executed 1-5 (modbus unified, well assembler, measured-well engine defaults, operator surface, 55-check in-package acceptance suite) = FINISHED OFFLINE PRODUCT by the evaluation's own criterion; field tier 6a gamma/lithology, 6b mixed toolstrings + in-engine rating block, 8 bench-test protocol with four-verdict self-labeled analysis. Remaining: step 7 only (site details). Gate 5,924/0. Acceptance 55/55. 23-file pass verified.

## v0.403.0-remanufacture — 2026-08-27
CI red on all runners: numpy>=2.0 removed np.trapz; assembler overburden now uses np.trapezoid (1.x fallback); PORTABILITY GUARD 2 pin + standing removed-alias-sweep rule. Stale TRACKED sdist staging tree star_magic_program-0.402.0/ identified (mounted-FS delete block; gitignored; Daniel removes on Windows). Same version per Daniel (tag preserved; PyPI untouched). Gate 5,925/0. Acceptance 55/55.

## v0.404.0 — 2026-08-28
THE FORTY WELLS SHIP: downhole v1.49–v1.58, catalogue entries 31–40 (census 40/28/29). Subduction end-to-end (JFAST record-depth slow-slip, Hikurangi rate-state + reader dedupe with 504B nitrate recovery, Costa Rica 212 °C envelopes, Barbados Pc−Po difference proof, Mariana mantle-wedge fingerprint) + hydrate hazard + first isotopes + two lakes + coral U-Th (54/54 decay-identity closure). 20 catalog data-files added to the wheel. Gate 5,949/0. Acceptance 55/55. 23-file pass verified.

## v0.405.0 — 2026-08-28
THE FIFTY WELLS SHIP (MILESTONE): downhole v1.59–v1.68, catalogue entries 41–50 (census 50/37/39).
First license refusal on record (NC-SA), petroleum-fluids triad complete (where/what/origin),
Mohr-Coulomb cohesion intercept, first LIFE (Peru radiotracer rates), Fram Strait EXACT TOC partition,
and the fiftieth entry ANCIENT AIR: EPICA Dome C CO₂ 611–799 kyr (171.6 ppmv record low; 247/247 below
preindustrial 280). SHIP GUARD v7 canonized (catalog↔data-files mechanical closure). 20 catalog
data-files added to the wheel. Gate 5,973/0. Acceptance 55/55. 23-file pass verified.

## v0.406.0 — 2026-08-29
THE SURVEYING TOOL SHIP: downhole v1.69–v1.77 = Parts 1–3 of the subsurface surveying tool
(Earth Model 29 sites / K2 gravity kernel KTB 0.9968 / K1 ladder 7 EXACT / inverse engine +
falsifiable KTB Vp prediction). Entry #51 (third runnable well), private operator tier (Retama,
cross-checksummed 181/181), SHIP GUARD v7, acceptance 55→75. Gate 5,993/0. 23-file pass verified.

## v0.407.0 — 2026-08-29
THE SCORED PREDICTION SHIP: entry #52 judges the first strata prediction (REFUTED +10%,
diagnosis = pre-disclosed assumption) -> family priors correct it (6,231 vs 6,228) ->
Prediction V2 pinned. PAPER_2258 landmark self-verifying (2,254/2,309). Honest renderer +
ENRGYONE commercial package. Gate 5,993 -> 6,003 (crossed 6,000). Acceptance 79. Full pass.

## v0.408.0 — 2026-08-31 (entry added at v0.410.0 prep)
THE RULED BATCH SHIP: surveying tool Parts 4-7 + differentiator (v1.81-1.85);
campaign resumed; RULINGS_BATCH_1 answered + folded same day (8 papers RULED).
Gate 6,003 -> 6,017. Acceptance 89.

## v0.409.0 — 2026-08-31 — FIRST FULL-WHEEL PUBLICATION
Manifest generated from repo contents (~2,540 data-files), SHIP GUARD v8,
Batch-1 verification, Batch 2 fold. Upgraded by v0.410.0 (registry closure,
live results table, band trails, history entries).

## v0.410.0 — 2026-09-01 — THE FULL-WHEEL UPGRADED / SECOND PRODUCT PUBLICATION
THE FULL-WHEEL SHIP: Daniel's rule ("EVERY SHIP SHOULD BE ON THE WHEEL") closes
the fifteen-version publication split — manifest generated from repo contents
(generate_wheel_manifest.py, ~2,540 data-files incl. whitepapers corpus,
registry family, rulings ledger, commercial + incorporation docs), catalog
moved to package-data (installs inside the package on every layout), SHIP
GUARD v8 (repo<->wheel closure) + v7 superseded. Plus the banked trust arc:
BATCH_1_VERIFICATION (all seven rulings stand; three record defects corrected)
and RULINGS_BATCH_2 (eight rulings; PAPER_063 mean REVERSED e7 -> -6.05e217 N;
[UA]=1e-4 canonized). Registry family updated for Batch 2 (16 row edits +
canonization row + 3 graph edges + citations). Gate 6,003 -> 6,025 across the
band. Wheel 22.3 MB / 2,706 members.

## v0.411.0 — 2026-09-01 — THE CONSOLIDATED FULL-WHEEL PUBLICATION
v0.409.0 + v0.410.0 condensed into one complete self-contained release: full
wheel (generated manifest, SHIP GUARD v8, package-data catalog), trust arc
(Batch-1 verification, Batch-2 fold incl. PAPER_063 e217 + [UA] canonized,
registry closure), live results table (82 VERIFIED_LIVE / 4 slips disclosed),
band trails gate-enforced. Gate 6,029/0. Acceptance 89/89.

## v0.412.0 — 2026-09-01 — THE FRONT DOOR SHIP (Qt)
star-magic CLI (calc/gate/well/docs/gui) + uqff_paths + installed-layout gate
(PROVEN green from site-packages, empty cwd) + LIVE-vs-INHERITED honesty flags
in plain terminal + Qt shell (Papers/Wells/Gate/Export/Geology) + full repo
mirror on wheel + list_wired alias-safe. Gate 6,031/0. Acceptance 89/89.

## v0.413.0 — 2026-09-01 — THE USER MANUAL SHIP
CLI-first Quick start (5 steps, no Python); headless-first doctrine
documented; stale dual-census KILLED (one number, one source); star-magic
export + quickstart + real well help. Gate 6,033/0. Acceptance 89/89.

## v0.414.0 — 2026-09-01 — THE DISSOLUTION SHIP
RULINGS Batches 3-4 folded (16 rulings) + 8 single deep dives dissolved
into primitive locks (B18/B20/B22/B25/B31/Q-110b/D_SCm/Q-216b) +
PAPER_2259 rung-12 conjugate-pair bridge landmark authored + wired.
Gate 6,045/0. Acceptance 89/89. Registry 6,820. Backlog 236 -> 224 + 1.

## 2026-09-03 — POST-SHIP CORRECTION: v0.413.0 tag-chain gap (Daniel's catch)
v0.414.0 shipped clean; v0.413.0 turned out never committed/tagged/published
(silent ship failure). Content verified inside v0.414.0 (full wheel). Records
corrected (CHANGELOG history note, version-history naming: THE USER MANUAL
BAND - PREPARED; PUBLISHED INSIDE v0.414.0). SHIP GUARD v9 added: tag-chain
continuity - every ledger version except current prep must have a git tag;
authorized gap v0.413.0 on record. ship.ps1 hardened: pre-flight ledger/tag
check + post-push remote-tag verification. Gate 6,046/0.

## v0.415.0 — 2026-09-03 — THE TAG-CHAIN SHIP
SHIP GUARD v9 (ledger/tag-chain continuity, v0.413.0 authorized gap on
record) + ship.ps1 pre-flight chain check and post-push remote-tag
verification + honest history naming. Physics untouched. Gate 6,046/0.
Acceptance 89/89.

## v0.415.1 — 2026-09-03 — THE TAG-CHAIN SHIP (CI-FIXED)
v0.415.0 tag went RED in both workflows: guard v9 assumed tag history, but
Actions shallow checkouts fetch no tags. Guard now skips at zero visible
tags, enforces on real checkouts. v0.415.0 = tagged, not published,
superseded. Gate 6,046/0.

## v0.415.2 — 2026-09-03 — THE TAG-CHAIN SHIP (ALL-CONTEXTS-FIXED)
Second v9 blindspot: tag-push checkouts carry exactly ONE tag, so the
zero-tags skip never fired in the release workflow. Guard now skips when
GITHUB_ACTIONS is set or <100 tags visible; enforces on full checkouts.
Verified in four contexts. v0.415.0/.1 tagged-unpublished-superseded.
Gate 6,046/0.

## v0.416.0 — 2026-09-04 — THE ORIGIN POINTS SHIP
Batches 5-8 + B57: 41 rulings folded under the recalculate-first method;
rho_crit forensic closure; Cabibbo dual closures; S330 flavor physics;
PAPER_026c re-ID. Gate 6,051/0. Acceptance 89/89. Registry 6,856.
Backlog 224 -> 191 + 1.

## v0.417.0 — 2026-09-04 — THE FIFTH SECTOR SHIP
Post-ship audit fixes + Batches 9-11 (23 rulings): R91 5th sector
fulfilled, both PAPER_2156 forensics closed, root-era units fix, rung
taxonomy growth, omega identity. Gate 6,055/0. Acceptance 89/89.
Registry 6,880. Backlog 191 -> 167 + 1.
