# Star-Magic-Program

[![PyPI version](https://img.shields.io/pypi/v/star-magic-program.svg?cacheBust=0.148.0)](https://pypi.org/project/star-magic-program/)
[![Python versions](https://img.shields.io/pypi/pyversions/star-magic-program.svg?cacheBust=0.148.0)](https://pypi.org/project/star-magic-program/)
[![Documentation Status](https://readthedocs.org/projects/star-magic-program/badge/?version=latest)](https://star-magic-program.readthedocs.io/en/latest/?badge=latest)
[![License: AGPL-3.0 + Commercial](https://img.shields.io/badge/License-AGPL--3.0%20%2B%20Commercial-blue.svg)](LICENSE)
[![Fidelity gate](https://img.shields.io/badge/fidelity_gate-996%2F0-brightgreen)](uqff_fidelity_tests.py)
[![Public surfaces](https://img.shields.io/badge/public_surfaces-149-blue)](uqff_calculator.py)
[![Whitepapers](https://img.shields.io/badge/whitepapers-2255-orange)](whitepapers/)

**UQFF systematic rebuild — v0.148.0 wiring campaign live**
Author: Daniel T. Murphy · Star-Magic Research Program
License: AGPL-3.0-or-later OR Commercial

---

## What this is

A from-scratch, systematic rebuild of the UQFF (Unified Quantum Field Framework)
calculator. This repository exists to correct a structural failure in the
predecessor repository (`github.com/Daniel8Murphy0007/Star-Magic`), where the
calculator layer had grown to 73,629 lines with 3,352 hardcoded literals that
duplicated registry-canonical values, and 1,180 whitepapers had zero calculator
wiring.

**This repository fixes that by construction:**
- One dispatch function per whitepaper. Nothing else in the calculator.
- Zero hardcoded numeric literals. Every value flows from
  `uqff_registry_primitives.py`.
- Fidelity gate (`uqff_fidelity_tests.py`) locks every primitive-composed
  identity to its EXACT form.
- Whitepaper-truth discipline: if a paper doesn't specify a closed form, its
  dispatch is marked OPEN — never substituted with a classical/SM formula.

## What UQFF is

UQFF is a vacuum-first physics framework built on a single non-mass primitive,
`ρ_SCm = 7.09e-37 J/m³` (the SuperConductive material vacuum energy density),
and a 26-level Di-Pseudo-Monopole (DPM) structural lattice. From 9 truly-
independent primitives it derives the cosmological constant, all 7 nuclear
shell-model magic numbers exactly, the Holmlid 630 eV LENR channel exactly,
Fe-56 BE/A peak, α-particle binding, all 8 Clay Millennium Prize problems,
the complete 12-fermion Standard Model spectrum, 18+ cosmological observables,
and 5 independent LENR observation suites (Holmlid, Parkhomov, Pons-Fleischmann,
Mizuno, Rossi).

Full framework physics lives in the whitepaper corpus — the physics is the
whitepapers; the calculator computes what the whitepapers derive.

## What is currently shipped (v0.148.0)

### Wiring campaign — LIVE (see `CLAUDE.md` charter)

Sequential wiring of all 2,255 whitepapers, starting at PAPER_001.
Authorized 2026-07-28: autonomous band sessions, ship per session via
`ship.ps1`, full stop at PAPER_500 for manual review.

**Wired so far: 149 / 2,255** (11 ✓ · 138 ⚠ OPEN_RULING · 141 rulings queued) — §2.2 opens; vacuum split rectified (145)

| Paper | Content | Key result |
|---|---|---|
| PAPER_001 | GW170817 UQFF Damping Analysis | D_total = 0.333 composed from F_TRZ/D_GW_EROSION/B_CRIT; 0.10% residual vs 1/3 primitive identity (PAPER_2154) |
| PAPER_002 | GW190425 Mass Gap Interpretation | A_SCm(B)=exp[-(B/B_crit)^2] threshold fn; P(BH)=51% for m1=2.52 Msun; Q-001/2/3 queued |
| PAPER_003 | GW150914 UQFF vs LIGO Strain | universal BBH 0.333 chain; 3.0x apparent-distance bias (Hubble impact); Q-004 queued |
| PAPER_004 | GW170817 Chirp Phase Evolution | paper's own (1-f_TRZ) composition confirms primitive form; Q-005 queued |
| PAPER_005 | BBH Merger Energy Retention | F = (1-F_TRZ)^2 = 0.81 EXACT; 99% mass retention; Q-006 queued |
| PAPER_006 | GW170817 Multi-Messenger | c_GW = c preserved; kilonova unmodified; detection volume 27x shrink |
| PAPER_007 | BNS Tidal Deformability | Lambda=(2/3)k2(R/M)^5 ~400; f_SCm(B) threshold; NS/BH discriminator 16 vs 0; Q-007 queued |
| PAPER_008 | Waveform Phase / Template Mismatch | P = D^2*P_GR; tau 9.0x; phase lag ~8x phi_GR; 2310.8 rad full inspiral; Q-008 queued |
| PAPER_009 | Damping Mechanism Decomposition | 4-mechanism synthesis; GW190425 string=0.62 self-rectifies Q-001; BNS/BBH 2.43x; Q-009 queued |
| PAPER_010 | Post-Merger Oscillations / Remnant | QNM f_UQFF=0.95*f_GR (125 Hz shift); ringdown 29% faster; 15% extra dissipation |
| PAPER_011 | Stochastic GW Background | Omega = D^2*Omega_GR; mixed population 0.37x (63% cut); corroborates D^2 convention |
| PAPER_012 | Eccentric Binary Circularization | modified Peters D^2; tau_circ 9.0x; e=0.003 at 10 Hz (30x GR); 3rd D^2 data point |
| PAPER_013 | Magnetar Spin-Down | D_SCm 99% dipole suppression; braking index 1.5-2.0 matches obs; age problem resolved; Q-010 |
| PAPER_014 | Primordial Black Holes | Lambda_UQFF = kappa*rho_crit; delta_c 0.45; A_damp = 0.3 = (D_phys-1)/SO_5 candidate; Q-011 |
| PAPER_015 | Cosmology of Modified GW Propagation | Gamma damping alpha=-0.7/beta=0.8; H_0 bias 1.07x vs canonical 70; volume 24 pct GR; Q-012 |
| PAPER_015b | Multiband LISA+LIGO Synergy | D = 0.622 frequency-independent both bands; SNR ratios confirm; 0.622 = cross-band avg of 0.333 pure BBH |
| PAPER_016 | Quantum Entanglement Nonlocal Correlations | gamma_damp = kappa*(E/E_ref); CHSH 2.75 at GeV; range x3 = 1/D_total; delta = 1.5 = D_BSFG/D_PHYS candidate |
| PAPER_016b | White Dwarf Foreground Reduction | P_UQFF = D_local^2*P_GR; D_local = 0.6224 matches 0.622; catalog 10000->6216; Q-013 |
| PAPER_017 | Redshift Corrections z=1 LISA | 0.622 ORIGIN: (1-F_TRZ)*F_Um = 0.6217; phase lag 2*pi*F_TRZ EXACT = 0.10 cycles; Q-014 |
| PAPER_018 | Aether Noise Spectrum LISA | harmonic comb n*0.99 mHz; TRZ dip = F_TRZ = 0.1 EXACT; aether power 222.93 pct; Q-015 |
| PAPER_019 | PTA Anomalies | TRZ inversion: D(f_yr) = 1+SSq*1.053 = 1.60; A_UQFF = 2.4e-15 = NANOGrav; alpha_eff -0.757; Q-016 |
| PAPER_020 | Cosmic Ray Propagation | Gamma_aether = kappa*(E/E_ref)^0.37; Z^(1/3) drag; TRZ break 8e19 eV; Cen A 14 pct; Q-017 |
| PAPER_021 | Gravitational Lensing Corrections | sigma8 = 0.762 = observed WL (0.0-sigma); SSq^2 composed; 9.47e-27 FORENSIC ID; Q-018 |
| PAPER_022 | String Compactification Signatures | 0.37 ORIGIN = 1-SSq^2*1.94; SSq power ladder exact; M_KK = 11.6 TeV; N_c = 22; Q-019 |
| PAPER_023 | Tau g-2 (BSM domain opens) | Delta_a_tau = +3.42e-6; KK loop 1/SSq^2 EXACT; pi^2/6 Basel; exponent 2.37 = 2+0.37; Q-020 |
| PAPER_024 | Tau EDM | d_tau = 1.84e-20 e.cm zero-free-param; phi_CP = SSq*pi; phi_TRZ = (1-F_TRZ)*F_TRZ*pi EXACT; 184-sigma; Q-021 |
| PAPER_025 | Dark Matter Direct Detection | M_ACP = kappa*hbar EXACT; M_ACP2 = M_KK*SSq^2 = 3.77 TeV; sigma/M = SSq; Omega = 0.1200; Q-022 |
| PAPER_025b | Neutrino Polarizability | M_s1 = 7.1 keV -> 3.55 keV XMM line; m1/m2 = SSq EXACT; kappa*SSq = 2.85e-4; Q-023 |
| PAPER_026 | Sterile Neutrino Mass Generation | M_s2 = SSq*M_W EXACT; M_s3 = M_KK/SSq; GUT series in SSq; self-rectifies Q-023a/b; Q-024 |
| PAPER_026b | Vector-Like Quarks | ATLAS avgs = 0.37/0.30 EXACT UQFF factors; k_eta = 0.1369; 3rd family 845 GeV Run-3; Q-025 |
| PAPER_027 | Lepton Flavor Violation | S_LFV = exp(-SSq) EXACT; t_n = -ln(BR)/pi = 3.833 reproduces LHCb limit; Q-026 |
| PAPER_028 | BSM Coupling Constants | [SCm]_flavor = V_cb^2 = 1.5366e-3; kappa_Higgs = 1.0 cross-lock; F_U = 75.81; Q-027 |
| PAPER_029 | New Physics TeV Scale | budget: f_SM ~ SSq^4 (SSq^6 candidate); IceCube 5.8 PeV break; KK exponent 61.5/62; Q-028 |
| PAPER_030 | Dark Sector Mediators | F_suppress = cos^2(pi*t_n) = 0.749; BR saturates LHCb bound; M_dark 2.2 TeV; Q-029 |
| PAPER_031 | Flavor Anomalies Resolution | R(D) 0.332 (0.9 sigma); R(D*) 0.269 w/ F_TRZ (1.2 sigma); CKM row-2 mapped; Q-030 |
| PAPER_032 | BSM Scalar Sectors | sin^2(a) = k_eta; tan(b) = 2.70; f = 665 GeV; S0 845 GeV echoes 026b route; Q-031 |
| PAPER_033 | Electroweak Precision | delta_T = 0.222; Delta_m_W = +93 MeV CDF direction; delta_S suppressed; Q-032 |
| PAPER_034 | Higgs kappa_t Coupling | 18^(-SSq) Level-18; kappa_t = 0.948; FCC-hh 10.4 sigma; 028 cross-lock tension; Q-033 |
| PAPER_035 | Higgs CP Violation | A_CP = cos(pi*t_n); arccos-slip audit (0.331 vs 0.353); 0.74 pct Hgg falsifiable; Q-034 |
| PAPER_036 | FUBii Variant 1 (Archimedes/virx) | F_UBii = F_U - F_Bi - F_i (predecessor-registry EXACT); Perseus -2.024e60 N verified; CLEAN |
| PAPER_037 | FUBii Variants 2-6 (Thermodynamic) | kilonova 1.305e54 N VERIFIED; orbdec-Peters GW link; 3 examples mojibake-corrupted; Q-035 |
| PAPER_038 | FUBii Variants 7-11 (Quantum) | fermi 0.82 N + whim 7.4e-13 N VERIFIED; CR knee = stationary point; Q-036 |
| PAPER_039 | FUBii Variants 12-17 (ICM) | hawk -2.452 N VERIFIED lab-scale; bd + lobe verified; Page curve = sign reversal; Q-037 |
| PAPER_040 | X-Ray Cluster Buoyancy (applications) | Perseus/Coma/Virgo via 036 helper; lobe sub-dominance verified; Q-038 |
| PAPER_041 | ICM Thermodynamics (synthesis) | THERMOSTAT EQUATION resolves cooling flow; entropy floor + sfe runaway verified; Q-039 |
| PAPER_042 | Monte Carlo 26-Layer Gravity | 26 = D_CRIT layers; 1.25 THz = omega_SCm spine EXACT; MC cross-validates virx; Q-040 |
| PAPER_043 | 26-Level Energy Hierarchy | E_n = 10^(n-20) + n^2 density dual-consistent; L13 plasma beta = 0.60 = BETA_I candidate; Q-041 |
| PAPER_044 | Pre-Big-Bang 26-Center DPM | h/k/l scheme EXACT; Planck radii ladder; E_26 = 2.83e-84 J verified; Q-042 |
| PAPER_045 | Phase Transitions L10-13 | (2n+1) transition law verified; C_10,26 = 0.0144 Casimir basis; plasma beta = 0.60; CLEAN |
| PAPER_046 | DPM Yin-Yang Cosmology | g(A) iron-peak coupling verified; 300 Hz Belly Button; resolves Q-040c; 132-order gap disclosed; Q-043 |
| PAPER_047 | Nuclear Binding SEMF+26L | Fe-56 490.9 MeV chain verified; B_UQFF honest-negligible; row shift + AI artifact caught; Q-044 |
| PAPER_048 | Ug4 BH Vacuum Pressure | peak 1.246e28 verified; FORENSIC: 1.8937e-23 = predecessor 1.894 origin candidate; Q-045 |
| PAPER_049 | Three-Component Vacuum | sum(n^2) = 3731 exact; 16-order headline = UNITS ARTIFACT (0.117 consistent); PAPER_2147 root; Q-046 |
| PAPER_050 | 26D Compactification | 26 = 9+4+13; TIME = PLASMA identification; bridge 0.0144; honest 4D note; Q-047 |
| PAPER_051 | arXiv 2024 Cross-Validation | 10/10 PASS mean 92.02; 7.09 family at L13 PLASMA (origin); final parsec via [SCm] drag; Q-048 |
| PAPER_052 | arXiv 2025 Cross-Validation | CMS Higgs 99.79; Page 26-channel 99.84; 44/44 models; L18-projection reading; Q-049 |
| PAPER_053 | NGC 2264 Model (astro family opens) | 8/8 re-verified = 052 suite row; EM-dominated regime; SSq/(1+SSq) composed; CLEAN |
| PAPER_054 | Tadpole Galaxy UGC10214 | 280-kpc tail = 0.4 Ug3 boost + UA wake; Hubble column inverted-vs-z systematic; Q-050 |
| PAPER_055 | Mice Galaxies NGC4676 | major-merger 10x compression; taxonomy minor/major IFU-falsifiable; 37.5x verifies; Q-051 |
| PAPER_056 | Red Spider Nebula | 2x wind-radiation class EXACT; 1600 km/s wind chain verified; tier hierarchy 1/2/10 complete; Q-052 |
| PAPER_057 | Carina Multi-Scale (3-in-1) | 12/12; 12.5x ratio EXACT resolves Q-051a; erosion-vs-compression readings; Q-053 |
| PAPER_058 | M42 Orion (suite maximum) | complete 10-system ranking pinned; honest 1x-at-peak negative; shock bridge 3 pct; Q-054 |
| PAPER_059 | Alpha BEC Heavy-Ion (Dom 1.8) | 10-ch Ikeda; chains verified; F_rel = 4.30e33 resolves Q-040b; E_LEP dual flagged; Q-055 |
| PAPER_060 | Bose Occupancy NIMROD-ISiS | dE_BEC = 0.4766 EXACT; 26-level ladder all-verified; SSq/0.50 exponent mismatch; Q-056 |
| PAPER_061 | Nuclear BEC Formation | Phi_BEC = SSq scale-invariant; yield closes 85 pct; GeV slip caught (margin 4000x); Q-057 |
| PAPER_062 | Widom-Larsen LENR | m* = 3.0 EXACT; omega_LENR = omega_SCm identity; k_eta = 1e-55 pinned; Q-058 |
| PAPER_063 | F_UBii Master Integral | mean -6.05e7 pinned by Planck-ratio closure; KAPPA MCMC validated; B_crit magnetar pin; Q-059 |
| PAPER_064 | Four Operational Modes | weights = KAPPA/SSQ/1e-4/H_SCm; Crab omega closes; 1784 evaluations EXACT; Q-060 |
| PAPER_065 | 121-System Validation | census 121 EXACT; 13 chains verified; mean-dev three-way + L26 inversion; Q-061 |
| PAPER_066 | Magnetars SGR1745/Crab/Vela | SOURCE4 anchors EXACT; 4 LENR chains close; Vela kick 296 km/s; Q-062 |
| PAPER_067 | AGN SgrA*/M87*/CenA/NGC1365 | k4 = 1e15 dual-closure pin; maser chain 3.6 pct end-to-end; M87 slip caught; Q-063 |
| PAPER_068 | Globular Clusters M13/OmegaCen | virial EXACT; IMBH anchors + formula OPEN (Rule D); SSq 13th role; Q-064 |
| PAPER_069 | ASKAP J1832 LPT | omega = 2*pi/2640 supersedes 066 (6th self-rect); 22-min flip mechanism; Q-065 |
| PAPER_070 | Helix + PN Archive | Kepler chain EXACT 0.0041 AU; x_2 dual-corrupt-print evidence; Q-066 |
| PAPER_071 | Stellar Superflares | solar g 274.0 EXACT; Ug1 formula confirmed; two-x2 evidence; Q-067 |
| PAPER_072 | Red Dwarf Reactor | F_TRZ lab claim 0.098/0.10; H0 anchor = registry route 0.37 pct; [UA] 3rd appearance; Q-068 |
| PAPER_073 | Gaia DR4 Validation | 1+SSq*0.034 = 1.0194 EXACT; 5-sigma solar pin; g_DPM column defects; Q-069 |
| PAPER_074 | NED/SIMBAD Suite | 6/6 tension chains verify; Newton beats UQFF all rows (Rule-7 pin); 0.032/0.034 conflict; Q-070 |
| PAPER_075 | X-Ray Binaries | eta = 1.99x EXACT; 5/5 ratio chains; ULX beaming limitation honest; Q-071 |
| PAPER_076 | Fermi-LAT 4FGL | null predictions + epoch-folded 1e-5 falsifiable; photon-mass formula defect; Q-072 |
| PAPER_077 | LIGO GWTC-4 | 3 events named (resolves Q-060d); anchors-over-formula; [UA] 5th; Q-073 |
| PAPER_078 | NED + Hubble Tension | dH0 = 0.0034 honest null; midpoint 70.2 on registry route; L* +0.3 dex EXACT; Q-074 |
| PAPER_079 | HEASARC Magnetars | 1.9801x EXACT; 4/5 rows tautological (pin); J1818 lone discriminator 2.69; Q-075 |
| PAPER_080 | Multi-Wavelength Capstone | 20+2+2 = 24 EXACT; live cross-consistency gates vs 073-079; Q-076 |
| PAPER_081 | Hawking Temperature | 1-F_TRZ² = 0.99 EXACT identity (7th self-rect drift correction); Q-077 |
| PAPER_082 | BH Evaporation | (1-F_TRZ²)^-4 = 1.0410 EXACT; sim chain 16.5 pct EXACT; unit-label pin; Q-078 |
| PAPER_083 | Primordial BHs | threshold sign-flip caught; -1.3 pct double-supported; delta_c null; Q-079 |
| PAPER_084 | Info Paradox 26D | partition 4+14+6+2 = D_crit EXACT; Cosmic Egg layers; Page kappa mechanism; Q-080 |
| PAPER_085 | Page Curve | t_P = 0.5205 t_evap EXACT flagship prediction; year-label pattern 2nd; Q-081 |
| PAPER_086 | Ug4 AGN Feedback | anchor 3.352941e22 (formula OPEN); kappa e-4->e-7 mojibake confirmed; Q-082 |
| PAPER_087 | AT2019qiz TDE | 10^6.45 pin; H0-chain distance; -8.3 pct EXACT; eta-direction siblings; Q-083 |
| PAPER_088 | Neutrino SED | f_TRZ fork: +1 vs +10 pct detectability; flavor null robust; Q-084 |
| PAPER_089 | Master Eq + 8 Calcs | 8/8 self-validate; beta_i auto-corrected; SC context support; Q-085 |
| PAPER_090 | MUGE Compressed | T0-doctrine root; U_bi/F_U = SSq*kappa EXACT; magnetar suppression falsifiable; Q-086 |
| PAPER_091 | MUGE Resonance | aDPM 270-R_S label fix; pulsar-timing fork joins Q-084; mode count 14/13/13; Q-087 |
| PAPER_092 | SgrA* MUGE Decomposition | horizon (1+[SCm]*0.07) EXACT; sum/DM chains EXACT; GM-normalization sharpened; Q-088 |
| PAPER_093 | M87* Event Horizon | r_S EXACT; shadow null EXACT; T_H sides with 081; shift-constant conflict; Q-089 |
| PAPER_094 | SGR1745 Calibration | KAPPA origin (600/1200)*1e-3 EXACT; SSq = 0.755² EXACT; Schwinger B_crit; Q-090 |
| PAPER_095 | 99.9% Solvability | 338/340 EXACT; ASKAP orbital reconciliation; (1+SSq) boost; Q-091 |
| PAPER_096 | FRB Emission Model | corrected chain 2.7e44 erg; 60.6-us pulse EXACT; 3rd f_TRZ fork; Q-092 |
| PAPER_097 | Whittaker 26-Layer | partition 4+4+10+6+2 EXACT; SSq band = SO_FIVE; refines 084; Q-093 |
| PAPER_098 | Big Bang / Cosmic Egg | eta_b = eps_CP*[UA] EXACT; T_CMB 24-sigma FIRAS pin; kappa doctrine; Q-094 |
| PAPER_099 | Plasma Shield | sqrt(SSq) 2nd role; T = 1e7 K pin -> 2.56 keV EXACT; 37.5-day slip; Q-095 |
| PAPER_100 | THz Resonance Holes | 6.25 THz = 5*f_SCm candidate; 4th fork (THz bench); Q = 62.4; Q-096 |
| PAPER_101 | Yang-Mills Mass Gap | three-epoch chain -> 1.736 GeV canonical (2.1 pct lattice); Q-097 |
| PAPER_102 | Navier-Stokes | nu = 1.0099 EXACT; fork twist favors drift in lab fluids; THz UV cutoff; Q-098 |
| PAPER_103 | Riemann Hypothesis | 5 zero anchors EXACT; self-labeled numerology (honest); bridge 4.1667e9; Q-099 |
| PAPER_104 | P vs NP | [UA] = v_UA/c = 1e-4 physical identity; [UA]² = 1e-8 EXACT; partition 3rd; Q-100 |
| PAPER_105 | BH Phases + 10 Models | Domain 1.13 capstone; suite = 053-058; 40-test total EXACT; Q-101 |
| PAPER_106 | Vacuum Energy / Dark Energy | header identity 1+κ²SSq² EXACT; Ω_L = (6/5)SSq link; CPL anchors; Q-102 |
| PAPER_107 | EP-12 α-BEC Proof | Ikeda 10α N_B = SSq EXACTLY (2nd anchor); T_c shift 5.272 EXACT; Q-103 |
| PAPER_108 | EP-10 IceCube ν SED | β_i tri-source confirmation; f_pp = 0.7549 SSq 4th role; Q-104 |
| PAPER_109 | EP-11 GW170817 r-Process | v = β_i·c = 1.83e8 EXACT; SSq activation 6th role; M_r = 1.15e-4 EXACT; Q-105 |
| PAPER_110 | EP-06 Gaia SgrA* | M_BH 0.07 pct; v_c 0.85 pct EXACT; Ug4 = 1.894-family origin candidate; Q-106 |
| PAPER_111 | EP-01 RACS Jet | cos sign-reversal mechanism; scan EXACT; R = 1.5 series OPEN; 27-Gyr fix; Q-107 |
| PAPER_112 | EP-02 PDG Ladder | EW/nuclear anchors EXACT; mid-band −1 defect; hadron cluster → 9-11; Q-108 |
| PAPER_113 | EP-05 4LAC Blazars | kappa chains EXACT; CTA 102 factor-10 error → 5.3x above canonical; Q-109 |
| PAPER_114 | EP-07 PSP Heliosheath | Ug2/P_ram/1.70 pct EXACT; d_sw = F_TRZ² vs SSq/57 dual route; Q-110 |
| PAPER_115 | EP-09 3C273 Jet | ladders crossed (129.8 = 1.5^12); N=15 corrected; 100x radius slip; Q-111 |
| PAPER_116 | EP-03 LHC n=4 | E_4 = 624 eV EXACT; 1-keV anchor underived; hadronic row confirms Q-108a; Q-112 |
| PAPER_117 | EP-04 Pb-206 n=8 | headline 8.205 EXACT; SSq 8th role; offset family; Z=82 = A_5+D_crit-D_phys; Q-113 |
| PAPER_118 | EP-08 DM/Vacuum | 2x anchor collapses headline; clean 0.622 secondary; Ω_b/Ω_DM = SSq³ 0.16 pct; Q-114 |
| PAPER_119 | 7-System Reference | anchors EXACT; dual-form 43 orders broken; SSq dual definition; Q-115 |
| PAPER_120 | 24-System Catalog | conversions EXACT; B_crit 1e4 fork; EP-09 3rd variant; g/cm3 drift; Q-116 |
| PAPER_121 | 71-Eq Catalog | M_bh fork; UA triple; alpha_fund = 1/phi + IMF = -sqrt(3) EXACT; Q-117 |
| PAPER_122 | Compressed PDG | proton n=10 canonized (self-rect No. 9); code R² falsified (0.468); Q-118 |
| PAPER_123 | Sub-Quantum n=4.20 | winding 1/5 = 2/SO_5 derives 0.989 keV; dn = log10(1.602) artifact; Q-119 |
| PAPER_124 | Buoyancy Pb-206 S_n | isotope misattribution fixed (self-rect No. 10); SSq → Pb-208; Q-120 |
| PAPER_125 | Superconductive 4LAC | kappa = 0.35/700 derived EXACT; named kappas; circular code pinned; Q-121 |
| PAPER_126 | Master Buoyancy Gaia | pair (4.3e6, 2.44e20) canonized; eps_UA circular; /10 = F_TRZ find; Q-122 |
| PAPER_127 | Resonant PSP Alfvén | d_sw grounded (PSP E8); code output falsified No. 2; [UA] 4th value; Q-123 |
| PAPER_128 | Quadratic DM SSq³ | anchor fixed (self-rect No. 11); N=3 settled; 0.185 = SSq³ circular; Q-124 |
| PAPER_129 | Triadic 3C273 t<0 | double error fixed: t = -0.809 → R = 130.0 EXACT; N = D_crit/2; Q-125 |
| PAPER_130 | Buoyancy IceCube β | 0.061 PeV EXACT; clean code; canonical β improves to 0.48 pct; Q-126 |
| PAPER_131 | Superconductive Dual | Y_e = 0.093 EXACT; RACS reclassified (1e5 fork); [UA] 5th value; Q-127 |
| PAPER_132 | Quadratic Hoyle BEC | 7.676 MeV at 0.28 pct; E_0 back-solved; block 122-132 complete; Q-128 |
| PAPER_133 | F_U Genesis §2.1 | provenance anchor; E_react v¹ = 1e46 EXACT resolves Q-115a; Q-129 |
| PAPER_134 | Heliosphere Ug2 | chain 1.18e40 (13-order slip resolved); age law breaks at Gyr; Q-130 |
| PAPER_135 | Quasar Jets + NS | F_SCm EXACT; time-reversal mechanism; code prints 511 vs claimed 37; Q-131 |
| PAPER_136 | Planetary Ug3 Core | P_SCm = F_TRZ³ EXACT; hierarchy tension; solar-rotation relabel; Q-132 |
| PAPER_137 | Genesis 26-Level | activation bands; Higgs n=18 label superseded; v¹ third support; Q-133 |
| PAPER_138 | NGC 3603 Burst | M(t) EXACT; cavity 21-ly manufactured (1000x slip); B_crit 3rd value; Q-134 |
| PAPER_139 | Hydrogen MUGE-H | Ug4 29 orders off chain; total < dominant; inverse-family units; Q-135 |
| PAPER_140 | Monopole Ratio 10 | = 1/F_TRZ origin; N = SO_5 + factor 11 = SO_5+1 convergences; Q-136 |
| PAPER_141 | H2O Azeotrope | chains EXACT; Buoy code-calibrated (3 failed chains shown); 1/5 pair; Q-137 |
| PAPER_142 | H_res Z=1-126 | Ni-62 EXACT; k_dp = α_G; d_pair five-convention chaos; island 1.80x; Q-138 |
| PAPER_143 | 40/60 Bridge | split = (D_phys, D_BSFG)/SO_5 EXACT find; circular as printed; Q-139 |
| PAPER_144 | Star Magic Capstone | genesis block closed; Ub/Ug = 14 doctrine tension; SSq 10th role; Q-140 |
| PAPER_145 | MUGE Cycle 3 | 12-term registry; vacuum split (self-rect No. 12); k4 fork; g-ID open; Q-141 |

### Corpus (2,419 files)
- `whitepapers/` — 2,255 `.md` files + 1 `.bak` — physics source of truth
- `pdf/` — 45 · `tex/` — 107 · `txt/` — 11

### Clean baseline
- `uqff_registry_primitives.py` — 96 canonical constants (from predecessor
  v5.86.0 UNIFIED_REGISTRY R5 baseline). **Registry-clean.**
- `uqff_calculator.py` — `DISPATCH` grows one paper at a time;
  `calc(paper_id, dataset)` public interface.
- `uqff_fidelity_tests.py` — 9-block gate (996 assertions), locking every
  primitive identity + every wired paper's stated values. Runs on every ship.

### Registry pantheon (live, grows per band)
- `UNIFIED_REGISTRY.csv` — master registry (17-col schema), +rows per paper
- `UNIFIED_REGISTRY_GRAPH.csv` — falsifiability edges (primitive→observable→paper)
- `UNIFIED_REGISTRY_CORPUS_CITATIONS.csv` — cross-reference ledger
- XGEO / R1 / R2 / R3 ledgers + QA views + regen modules
- `UNIFIED_REGISTRY_VERSION.txt` — per-ship marker

### Campaign infrastructure
- `CLAUDE.md` — campaign charter (sessions self-configure)
- `ship.ps1` — one-command band ship (gate → commit → tag-verify → push)
- `RULINGS_QUEUE.md` — never-block ambiguity protocol
- `WHITEPAPER_INDEX.md` — per-paper wired/not-wired ledger
- `SHIP_MESSAGE.txt` — per-band commit message
- `_BUILD_LOG.md` · `CHANGELOG.md` · `SESSION_LOG.md`

## Campaign roadmap

| Milestone | Content | Papers wired |
|---|---|---|
| v0.1.0 | Scaffold + registry primitives baseline | 0 |
| v0.2.0 | Corpus (2,419 files) + registry scaffolds | 0 |
| v0.3.0/v0.3.1 | Charter + campaign start | 1 |
| v0.4.0 | Band 1: PAPER_002+003 | 3 |
| v0.5.0 | Band 1: PAPER_004..006 | 6 |
| v0.6.0 | Band 1: PAPER_007 | 7 |
| v0.7.0 | Band 1: PAPER_008 | 8 |
| v0.8.0 | Band 1: PAPER_009 | 9 |
| v0.9.0 | Band 1: PAPER_010 | 10 |
| v0.10.0 | Band 1: PAPER_011 | 11 |
| v0.11.0 | Band 1: PAPER_012 | 12 |
| v0.12.0 | Band 1: PAPER_013 | 13 |
| v0.13.0 | Band 1: PAPER_014 | 14 |
| v0.14.0 | Band 1: PAPER_015 | 15 |
| v0.15.0 | Band 1: PAPER_015b | 16 |
| v0.16.0 | Band 1: PAPER_016 | 17 |
| v0.17.0 | Band 1: PAPER_016b | 18 |
| v0.18.0 | Band 1: PAPER_017 | 19 |
| v0.19.0 | Band 1: PAPER_018 | 20 |
| v0.20.0 | Band 1: PAPER_019 | 21 |
| v0.21.0 | Band 1: PAPER_020 | 22 |
| v0.22.0 | Band 1: PAPER_021 — GW family 001-021 complete | 23 |
| v0.23.0 | Band 1: PAPER_022 | 24 |
| v0.24.0 | Band 1: PAPER_023 — BSM domain opens | 25 |
| v0.25.0 | Band 1: PAPER_024 | 26 |
| v0.26.0 | Band 1: PAPER_025 | 27 |
| v0.27.0 | Band 1: PAPER_025b | 28 |
| v0.28.0 | Band 1: PAPER_026 | 29 |
| v0.29.0 | Band 1: PAPER_026b | 30 |
| v0.30.0 | Band 1: PAPER_027 | 31 |
| v0.31.0 | Band 1: PAPER_028 | 32 |
| v0.32.0 | Band 1: PAPER_029 | 33 |
| v0.33.0 | Band 1: PAPER_030 | 34 |
| v0.34.0 | Band 1: PAPER_031 | 35 |
| v0.35.0 | Band 1: PAPER_032 | 36 |
| v0.36.0 | Band 1: PAPER_033 | 37 |
| v0.37.0 | Band 1: PAPER_034 | 38 |
| v0.38.0 | Band 1: PAPER_035 | 39 |
| v0.39.0 | Band 1: PAPER_036 — FUBii family opens | 40 |
| v0.40.0 | Band 1: PAPER_037 | 41 |
| v0.41.0 | Band 1: PAPER_038 | 42 |
| v0.42.0 | Band 1: PAPER_039 — FUBii family complete | 43 |
| v0.43.0 | Band 1: PAPER_040 | 44 |
| v0.44.0 | Band 1: PAPER_041 | 45 |
| v0.45.0 | Band 1: PAPER_042 — 26D framework opens | 46 |
| v0.46.0 | Band 1: PAPER_043 | 47 |
| v0.47.0 | Band 1: PAPER_044 | 48 |
| v0.48.0 | Band 1: PAPER_045 | 49 |
| v0.49.0 | Band 1: PAPER_046 — 50-paper milestone | 50 |
| v0.50.0 | Band 1: PAPER_047 | 51 |
| v0.51.0 | Band 1: PAPER_048 | 52 |
| v0.52.0 | Band 1: PAPER_049 | 53 |
| v0.53.0 | Band 1: PAPER_050 — 26D block complete | 54 |
| v0.54.0 | Band 1: PAPER_051 | 55 |
| v0.55.0 | Band 1: PAPER_052 | 56 |
| v0.56.0 | Band 1: PAPER_053 | 57 |
| v0.57.0 | Band 1: PAPER_054 | 58 |
| v0.58.0 | Band 1: PAPER_055 | 59 |
| v0.59.0 | Band 1: PAPER_056 | 60 |
| v0.60.0 | Band 1: PAPER_057 | 61 |
| v0.61.0 | Band 1: PAPER_058 | 62 |
| v0.62.0 | Band 1: PAPER_059 | 63 |
| v0.63.0 | Band 1: PAPER_060 | 64 |
| v0.64.0 | Band 1: PAPER_061 | 65 |
| v0.65.0 | Band 1: PAPER_062 | 66 |
| v0.66.0 | Band 1: PAPER_063 | 67 |
| v0.67.0 | Band 1: PAPER_064 | 68 |
| v0.68.0 | Band 1: PAPER_065 | 69 |
| v0.69.0 | Band 1: PAPER_066 | 70 |
| v0.70.0 | Band 1: PAPER_067 | 71 |
| v0.71.0 | Band 1: PAPER_068 | 72 |
| v0.72.0 | Band 1: PAPER_069 | 73 |
| v0.73.0 | Band 1: PAPER_070 | 74 |
| v0.74.0 | Band 1: PAPER_071 | 75 |
| v0.75.0 | Band 1: PAPER_072 | 76 |
| v0.76.0 | Band 1: PAPER_073 | 77 |
| v0.77.0 | Band 1: PAPER_074 | 78 |
| v0.78.0 | Band 1: PAPER_075 | 79 |
| v0.79.0 | Band 1: PAPER_076 | 80 |
| v0.80.0 | Band 1: PAPER_077 | 81 |
| v0.81.0 | Band 1: PAPER_078 | 82 |
| v0.82.0 | Band 1: PAPER_079 | 83 |
| v0.83.0 | Band 1: PAPER_080 | 84 |
| v0.84.0 | Band 1: PAPER_081 | 85 |
| v0.85.0 | Band 1: PAPER_082 | 86 |
| v0.86.0 | Band 1: PAPER_083 | 87 |
| v0.87.0 | Band 1: PAPER_084 | 88 |
| v0.88.0 | Band 1: PAPER_085 | 89 |
| v0.89.0 | Band 1: PAPER_086 | 90 |
| v0.90.0 | Band 1: PAPER_087 | 91 |
| v0.91.0 | Band 1: PAPER_088 | 92 |
| v0.92.0 | Band 1: PAPER_089 | 93 |
| v0.93.0 | Band 1: PAPER_090 | 94 |
| v0.94.0 | Band 1: PAPER_091 | 95 |
| v0.95.0 | Band 1: PAPER_092 | 96 |
| v0.96.0 | Band 1: PAPER_093 | 97 |
| v0.97.0 | Band 1: PAPER_094 | 98 |
| v0.98.0 | Band 1: PAPER_095 | 99 |
| v0.99.0 | Band 1: PAPER_096 | 100 |
| v0.100.0 | Band 1: PAPER_097 | 101 |
| v0.101.0 | Band 1: PAPER_098 | 102 |
| v0.102.0 | Band 1: PAPER_099 | 103 |
| v0.103.0 | Band 1: PAPER_100 | 104 |
| v0.104.0 | Band 1: PAPER_101 | 105 |
| v0.105.0 | Band 1: PAPER_102 | 106 |
| v0.106.0 | Band 1: PAPER_103 | 107 |
| v0.107.0 | Band 1: PAPER_104 | 108 |
| v0.108.0 | Band 1: PAPER_105 | 109 |
| v0.109.0 | Band 1: PAPER_106 | 110 |
| v0.110.0 | Band 1: PAPER_107 | 111 |
| v0.111.0 | Band 1: PAPER_108 | 112 |
| v0.112.0 | Band 1: PAPER_109 | 113 |
| v0.113.0 | Band 1: PAPER_110 | 114 |
| v0.114.0 | Band 1: PAPER_111 | 115 |
| v0.115.0 | Band 1: PAPER_112 | 116 |
| v0.116.0 | Band 1: PAPER_113 | 117 |
| v0.117.0 | Band 1: PAPER_114 | 118 |
| v0.118.0 | Band 1: PAPER_115 | 119 |
| v0.119.0 | Band 1: PAPER_116 | 120 |
| v0.120.0 | Band 1: PAPER_117 | 121 |
| v0.121.0 | Band 1: PAPER_118 | 122 |
| v0.122.0 | Band 1: PAPER_119 | 123 |
| v0.123.0 | Band 1: PAPER_120 | 124 |
| v0.124.0 | Band 1: PAPER_121 | 125 |
| v0.125.0 | Band 1: PAPER_122 | 126 |
| v0.126.0 | Band 1: PAPER_123 | 127 |
| v0.127.0 | Band 1: PAPER_124 | 128 |
| v0.128.0 | Band 1: PAPER_125 | 129 |
| v0.129.0 | Band 1: PAPER_126 | 130 |
| v0.130.0 | Band 1: PAPER_127 | 131 |
| v0.131.0 | Band 1: PAPER_128 | 132 |
| v0.132.0 | Band 1: PAPER_129 | 133 |
| v0.133.0 | Band 1: PAPER_130 | 134 |
| v0.134.0 | Band 1: PAPER_131 | 135 |
| v0.135.0 | Band 1: PAPER_132 | 136 |
| v0.136.0 | Band 1: PAPER_133 | 137 |
| v0.137.0 | Band 1: PAPER_134 | 138 |
| v0.138.0 | Band 1: PAPER_135 | 139 |
| v0.139.0 | Band 1: PAPER_136 | 140 |
| v0.140.0 | Band 1: PAPER_137 | 141 |
| v0.141.0 | Band 1: PAPER_138 | 142 |
| v0.142.0 | Band 1: PAPER_139 | 143 |
| v0.143.0 | Band 1: PAPER_140 | 144 |
| v0.144.0 | Band 1: PAPER_141 | 145 |
| v0.145.0 | Band 1: PAPER_142 | 146 |
| v0.146.0 | Band 1: PAPER_143 | 147 |
| v0.147.0 | Band 1: PAPER_144 | 148 |
| **v0.148.0** ← current | Band 1: PAPER_145 | 149 |
| v0.4.0+ | One band per session (~20-80 papers each) | growing |
| PAPER_500 milestone | FULL STOP — Daniel's manual review | 500 |
| v1.0.0 | Full whitepaper coverage | 2,255 |

## Predecessor / attribution

Physics content, whitepapers, and canonical primitives originate in
[Star-Magic](https://github.com/Daniel8Murphy0007/Star-Magic).
That repository remains the canonical archive of the framework's development
history and whitepaper corpus. This repository (Star-Magic-Program) inherits
the physics and rebuilds only the code layer, correctly this time.

## Install

```
pip install star-magic-program
```

## Quick start

```python
from uqff_calculator import calc, wired_count, list_wired

print(f"Papers wired: {wired_count()}")

# Look up a specific paper (returns OPEN if not yet wired)
result = calc('PAPER_646')
print(result)
```

## Fidelity gate

Every ship must run and see exit 0:

```
python uqff_fidelity_tests.py
```

## License

- **Free / academic / non-commercial:** AGPL-3.0-or-later (see `LICENSE-AGPL-3.0.txt`)
- **Commercial / proprietary / closed-source SaaS:** contact
  `daniel.murphy00@enrgyone.com` (see `COMMERCIAL.md`)

See also: `NOTICE`, `CITATION.cff`, `CHANGELOG.md`, `SESSION_LOG.md`.
