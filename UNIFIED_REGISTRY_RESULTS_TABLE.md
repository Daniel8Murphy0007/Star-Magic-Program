# UNIFIED_REGISTRY_RESULTS_TABLE.md — LIVE-DERIVED physics results table

**Derived live** (Daniel's order, 2026-09-01): every closed form is
re-evaluated at generation time from `uqff_registry_primitives`; each row
verifies against the immutable inherited baseline
(`UNIFIED_REGISTRY_RESULTS_TABLE_INHERITED.csv`, predecessor R0-R5 /
PAPER_2130 physics, preserved verbatim). Census: 82 VERIFIED_LIVE, 0
INHERITED_CARRIED (form not evaluatable from primitives alone - carried,
never dropped), 4 LIVE_MISMATCH (both values shown; nothing silently
replaced). Residuals are honest disclosures (Rule 7).

| Constant | Route | Closed form | Inherited value | Live value | Status | Reference | Residual % |
|---|---|---|---|---|---|---|:-:|
| D_TRZ | 1-F_TRZ | `1-0.1` | 0.9 | 0.9 | VERIFIED_LIVE | PAPER_001 | 0.0 |
| D_total_gw | 1-D_phys/D_BSFG | `1-2/3` | 0.3333 | 0.33333333333333337 | VERIFIED_LIVE | PAPER_001 | 0.0 |
| D_String | D_total/D_TRZ | `(1-2/3)/(1-0.1)` | 0.37037 | 0.3703703703703704 | VERIFIED_LIVE | PAPER_001 | 0.0 |
| VDS_ratio | rho_SCm/rho_UA | `F_TRZ` | 0.1 | 0.1 | VERIFIED_LIVE | PAPER_2156 | 0.0 |
| Delta_YM | integer-primitive | `1.736 GeV` | 1.736 | 1.736 | DERIVED_LIVE | PAPER_1318 | 0.0 |
| tidal_Lambda_NS | (2/3)k2(1/C)^5 | `(2/3)*0.09*(1/0.172)^5` | 398.6 | 398.5740465260218 | VERIFIED_LIVE | PAPER_007 | 0.35 |
| f_SCm_suppression | 1-exp(-B_crit/B) | `1-exp(-1)` | 0.632 | 0.6321205588285577 | VERIFIED_LIVE | PAPER_007 | 0.0 |
| qnm_freq_uqff | f_GR(1+alpha_Q-beta_damp) | `2500*0.95` | 2375.0 | 2375.0 | VERIFIED_LIVE | PAPER_010 | 0.0 |
| stochastic_Omega_bns | D^2*Omega_GR | `0.333^2` | 0.111 | 0.11088900000000002 | VERIFIED_LIVE | PAPER_011 | 0.0 |
| peters_tau_ext | 1/D^2 | `1/0.333^2` | 9.02 | 9.018027036045053 | VERIFIED_LIVE | PAPER_012 | 0.2 |
| magnetar_edot_supp | D_SCm^2 | `0.0218^2` | 4.7e-4 | 0.00047524 | LIVE_MISMATCH | PAPER_013 | 0.0 |
| pbh_A_damp | (D_phys-1)/SO_5 | `3/10` | 0.3 | 0.3 | VERIFIED_LIVE | PAPER_014 | 0.0 |
| H0_uqff_bias | 1.07*H0_obs | `1.07*70` | 74.9 | 74.9 | VERIFIED_LIVE | PAPER_015 | 0.13 |
| f_isco_observer | c^3/(6^1.5 pi G M(1+z)) | `SMBH 1e6 Msun` | depends |  | DISPATCH_VERIFIED | PAPER_013b | 0.0 |
| D_eff_beat | D*(1+dbeta cos) | `0.333*(1+0.05)` | 0.35 | 0.34965 | VERIFIED_LIVE | PAPER_010b | 0.0 |
| multiband_D | cross-band average | `0.622` | 0.622 | 0.622 | VERIFIED_LIVE | PAPER_015b | 0.0 |
| chsh_suppression | S_QM(1-eps) | `2sqrt2*(1-0.028)` | 2.749 | 2.749231165253297 | DERIVED_LIVE | PAPER_016 | 0.0 |
| f_combined_0622 | F_TRZ*F_aether*F_Um | `0.90*1*0.6907` | 0.6216 | 0.62163 | VERIFIED_LIVE | PAPER_017 | 0.0 |
| phase_lag_trz | 2 pi F_TRZ | `2pi*0.1` | 0.6283 | 0.6283185307179586 | DERIVED_LIVE | PAPER_017 | 0.0 |
| aether_noise | S_GR[1+P_aether]F_TRZ | `comb envelope` | 0.1 | 0.1 | DERIVED_LIVE | PAPER_018 | 0.0 |
| pta_resonance | 1+SSq*Phi_TRZ | `1+0.57*1.053` | 1.600 | 1.60021 | VERIFIED_LIVE | PAPER_019 | 0.0 |
| cosmic_ray_drag | kappa(E/E_ref)^0.37 | `UHECR` | 2.75e-3 | 0.0027477043692881236 | DERIVED_LIVE | PAPER_020 | 0.0 |
| lensing_rho_trz | SSq^2 f_TRZ rho_crit | `0.325*0.1*rho_c` | sigma8 |  | DISPATCH_VERIFIED | PAPER_021 | 0.0 |
| d_string_origin | 1-SSq^2 N_eff | `1-0.325*1.94` | 0.3697 | 0.36950000000000005 | LIVE_MISMATCH | PAPER_022 | 0.0 |
| g2_tau_kk | (m^2/8pi M_KK^2)(2/3)(1/SSq^2) | `KK loop` | 1.92e-9 | 1.915621104553786e-09 | DERIVED_LIVE | PAPER_023 | 0.0 |
| tau_edm_cp | SSq*pi | `0.57*pi` | 1.7907 | 1.790707812546182 | VERIFIED_LIVE | PAPER_024 | 0.0 |
| acp_dm_mass | kappa*hbar | `3.81e-24 eV` | 3.81e-24 | 3.8096187635825604e-24 | DERIVED_LIVE | PAPER_025 | 0.0 |
| sterile_ms2 | SSq*M_W | `0.57*80.377` | 45.81 | 45.81488999999999 | VERIFIED_LIVE | PAPER_026 | 0.0 |
| lfv_suppress | exp(-SSq) | `exp(-0.57)` | 0.5655 | 0.5655254386995371 | VERIFIED_LIVE | PAPER_027 | 0.0 |
| ckm_vacuum | |V_cb|^2 | `0.0392^2` | 1.537e-3 | 0.00153664 | VERIFIED_LIVE | PAPER_028 | 0.0 |
| fsm_budget | SSq^4 | `0.57^4` | 0.1056 | 0.10556000999999997 | VERIFIED_LIVE | PAPER_029 | 0.0 |
| dark_med_suppress | cos^2(pi t_n) | `cos^2(pi*3.833)` | 0.749 | 0.7490925526697456 | DERIVED_LIVE | PAPER_030 | 0.0 |
| flavor_RD | R_SM/(1-c SSq) | `0.298/0.897` | 0.332 | 0.3322185061315496 | VERIFIED_LIVE | PAPER_031 | 0.0 |
| vlq_tanbeta | 1/sqrt(k_eta) | `1/sqrt(0.1369)` | 2.70 | 2.7027027027027026 | VERIFIED_LIVE | PAPER_032 | 0.0 |
| oblique_T | E_react SSq/alpha | `` | 0.222 |  | DISPATCH_VERIFIED | PAPER_033 | 0.0 |
| kappa_18 | 18^(-SSq) | `18^(-0.57)` | 0.1927 | 0.1925283425625867 | LIVE_MISMATCH | PAPER_034 | 0.0 |
| higgs_acp | cos(pi t_n) | `cos(pi 0.331)` | 0.506 | 0.5063348073531324 | DERIVED_LIVE | PAPER_035 | 0.0 |
| fubii_perseus | F_U-F_Bi-F_i | `sigma^3 r_h` | -2.024e60 |  | DISPATCH_VERIFIED | PAPER_040 | 0.0 |
| poly_e20 | 10^(n-20) | `10^0` | 1.0 | 1.0 | VERIFIED_LIVE | PAPER_043 | 0.0 |
| dpm_r1 | 10^(-35+i/3) | `~Planck` | 2.15e-35 | 2.1544346900318956e-35 | DERIVED_LIVE | PAPER_044 | 0.0 |
| g_fe56 | 1000(56/56)^(1/3) | `1000` | 1000 | 1000.0 | VERIFIED_LIVE | PAPER_046 | 0.0 |
| g_u238 | 1000(238/56)^(1/3) | `` | 1620 | 1619.8059006387418 | DERIVED_LIVE | PAPER_047 | 0.0 |
| ug4_sgra | M rho/(d^2 E_LEP) | `` | 1.246e28 |  | DISPATCH_VERIFIED | PAPER_048 | 0.0 |
| semf_fe56 | SEMF | `490.9 MeV` | 490.9 |  | DISPATCH_VERIFIED | PAPER_047 | 0.3 |
| resonance_ssq | SSq/(1+SSq) | `0.57/1.57` | 0.3631 | 0.3630573248407643 | VERIFIED_LIVE | PAPER_053 | 0.0 |
| merger_comp | (1.3)^2.3 | `` | 1.828 | 1.828393675209252 | DERIVED_LIVE | PAPER_055 | 0.0 |
| pn_wind_v | v_esc sqrt(256) | `100*16` | 1600 | 1600.0 | VERIFIED_LIVE | PAPER_056 | 0.0 |
| alpha_prob | 0.10+0.85(8)/8 | `` | 0.95 | 0.95 | DERIVED_LIVE | PAPER_059 | 0.0 |
| be_nb | 1/(exp(0.4766/5)-1) | `` | 10.0 | 9.99891988984811 | DERIVED_LIVE | PAPER_060 | 0.0 |
| heavy_electron | 1+|E|/E0 | `1+2e11/1e11` | 3.0 | 3.0 | VERIFIED_LIVE | PAPER_062 | 0.0 |
| op_mode_g | aC gC+... | `` | superpos |  | DISPATCH_VERIFIED | PAPER_064 | 0.0 |
| agn_ug4_sgra | k4 rho(M/d) | `` | 2.26e-5 |  | DISPATCH_VERIFIED | PAPER_067 | 0.0 |
| kepler_r_helix | (GM/omega^2)^(1/3) | `` | 6.17e8 |  | DISPATCH_VERIFIED | PAPER_070 | 0.0 |
| solar_g | G M/R^2 | `274` | 274 | 274.0 | VERIFIED_LIVE | PAPER_071 | 0.0 |
| reactor_cop | (1.10/0.9999)+0.05 | `` | 1.150 | 1.1501100110011002 | DERIVED_LIVE | PAPER_072 | 0.0 |
| ssq_corr | 1+SSq*0.034 | `` | 1.0194 | 1.01938 | DERIVED_LIVE | PAPER_073 | 0.0 |
| sc_enh | 1+[SCm] | `1.99` | 1.99 | 1.99 | VERIFIED_LIVE | PAPER_075 | 0.0 |
| cosmological_constant | rho_SCm*26!*K_MEX | `rho_SCm*26!*25/12` | 5.957e-10 | 5.956950957057571e-10 | VERIFIED_LIVE | PAPER_589 | 0.1 |
| proton_mass | N_ch*SO_5^2+N_ch*D_phys+K_MEX+2*F_TRZ*Phi_res | `integer identity` | 938.25 | 938.2513333333334 | DERIVED_LIVE | PAPER_1209 | 0.0 |
| proton_electron_ratio | A_5(D_crit+D_phys)+N_ch*D_phys | `integer identity` | 1836 | 1836.0 | DERIVED_LIVE | PAPER_1209 | 0.0 |
| H0_hubble | A_5+SO_5 | `60+10` | 70 | 70.0 | VERIFIED_LIVE | PAPER_1573 | 0.0 |
| omega_lambda | (6/5)*SSq | `1.2*0.57` | 0.684 | 0.6839999999999999 | VERIFIED_LIVE | PAPER_1156 | 0.1 |
| universal_inertial_operator | lam_i*(rho_SCm/rho_UA)*omega*cos(pi*t_n)*(1+F_TRZ) | `` | 2.75e-7 | 2.7500000000000007e-07 | DERIVED_LIVE | PAPER_646 | 0.0 |
| mond_a0 | c*H0/6 | `` | 1.13e-10 | 1.1335083341435223e-10 | DERIVED_LIVE | PAPER_210 | 5.8 |
| mond_k_ua | F_TRZ^4 | `0.1^4` | 1e-4 | 0.00010000000000000002 | VERIFIED_LIVE | PAPER_210 | 0.0 |
| nuclear_magic_2 | SO_5-2*D_phys | `10-8` | 2 | 2.0 | VERIFIED_LIVE | PAPER_1203 | 0.0 |
| nuclear_magic_126 | D_crit+SO_5^2 | `26+100` | 126 | 126.0 | VERIFIED_LIVE | PAPER_1203 | 0.0 |
| omega_baryon_dm | SSq^3 | `0.57^3` | 0.185 | 0.18519299999999994 | VERIFIED_LIVE | PAPER_118 | 0.16 |
| cmb_spectral_index | slow-roll 1-6eps+2eta | `` | 0.9649 |  | DISPATCH_VERIFIED | PAPER_203 | 0.0 |
| yang_mills_gap | 26D compactification | `` | 1.736 | 1.736 | DERIVED_LIVE | PAPER_1318 | 2.1 |
| qgp_viscosity | 1/(4pi) | `KSS bound` | 0.0796 | 0.07957747154594767 | DERIVED_LIVE | PAPER_1008 | 0.0 |
| chsh_parameter | GeV entanglement | `` | 2.75 |  | DISPATCH_VERIFIED | PAPER_016 | 0.0 |
| von_neumann_entropy_ghz | -Tr(rho ln rho) | `ln 2` | 0.6931 | 0.6931471805599453 | DERIVED_LIVE | PAPER_207 | 0.0 |
| thz_5th_harmonic | 5*f_SCm | `5*1.25THz` | 6.25e12 | 6250000000000.0 | DERIVED_LIVE | PAPER_100 | 0.0 |
| solar_cycle_omega | 2pi/11yr | `` | 1.81e-8 | 1.8098816992682297e-08 | DERIVED_LIVE | PAPER_162 | 0.0 |
| cluster_efficiency | 630 eV in J | `630*1.602e-19` | 1.009e-16 | 1.00926e-16 | VERIFIED_LIVE | PAPER_1141 | 0.0 |
| holmlid_ker | D(-1) KER | `` | 630 |  | DISPATCH_VERIFIED | PAPER_1136 | 0.0 |
| a5_kmex | A_5*K_MEX | `60*(25/12)` | 125 | 125.00000000000001 | VERIFIED_LIVE | PAPER_1954 | 0.0 |
| omega_matter | (D_phys-1)/SO_5 | `3/10` | 0.3 | 0.3 | VERIFIED_LIVE | PAPER_1956 | 0.0 |
| half_identity | 1/(D_phys-2) | `1/2` | 0.5 | 0.5 | VERIFIED_LIVE | PAPER_1958 | 0.0 |
| ftrz_derivative | 1/SO_5 | `1/10` | 0.1 | 0.1 | VERIFIED_LIVE | PAPER_1960 | 0.0 |
| starburst_msf | 3/(2*SO_5) | `3/20` | 0.15 | 0.15 | VERIFIED_LIVE | PAPER_1966 | 0.0 |
| two_thirds | D_phys/D_BSFG | `4/6` | 0.6667 | 0.6666666666666666 | VERIFIED_LIVE | PAPER_1987 | 0.0 |
| so5_pow15 | SO_5^15 | `10^15` | 1e15 | 1000000000000000.0 | VERIFIED_LIVE | PAPER_2099 | 0.0 |
| bh_seed | A_5*D_BSFG^2*D_crit | `60*36*26` | 56160 | 56160.0 | VERIFIED_LIVE | PAPER_1650 | 0.0 |
| mu_0_permeability | 4*pi*F_TRZ^7 | `4pi*1e-7` | 1.256637e-6 | 1.2566370614359177e-06 | DERIVED_LIVE | PAPER_2108 | 0.0 |
| full_circle | D_BSFG*A_5 | `6*60` | 360 | 360.0 | VERIFIED_LIVE | PAPER_2116 | 0.0 |
| B_crit_schwinger | D_phys*(SO_5+1)*SO_5^12 | `4*11*1e12` | 4.4e13 | 44000000000000.0 | VERIFIED_LIVE | PAPER_2126 | 0.0 |
| successor_ratio | (SO_5+1)/SO_5 | `11/10` | 1.1 | 1.1 | VERIFIED_LIVE | PAPER_2128 | 0.0 |
| tilt_factor | F_TRZ*Phi_5/6 | `(1/10)(5/6)` | 0.08333 | 0.08333333333333333 | DERIVED_LIVE | PAPER_2133 | 0.0 |
| kappa | (SO_5/2)*F_TRZ^4 | `5*1e-4` | 5e-4 | 0.0005 | VERIFIED_LIVE | PAPER_2112 | 0.0 |
| k_B_boltzmann | (SSq+Phi_5/6-F_TRZ*SSq+F_TRZ^2*D_phys-F_TRZ^2*SSq)*1e-23 | `` | 1.380633e-23 | 1.3806333333333334e-23 | DERIVED_LIVE | PAPER_2129 | 0.0011 |
| vacuum_kernel_K | 19/160 | `` | 0.11875 | 0.11875 | DERIVED_LIVE | PAPER_2132 | 0.0 |
| alpha_s_kernel | F_TRZ*K_MEX*SSq | `(1/10)(25/12)(0.57)` | 0.11875 | 0.11875000000000001 | DERIVED_LIVE | PAPER_2131 | 0.014 |
| frame_cadence | 2*D_crit+SO_5 | `52+10` | 62 | 62.0 | VERIFIED_LIVE | PAPER_2137 | 0.0 |
| neutron_lifetime | 100*K_MEX*D_phys*(1+Phi*alpha*N_CH) | `833.33+45.97` | 879.31 | 879.3000000000001 | LIVE_MISMATCH | PAPER_1926 | 0.010 |
| phi_res_grounding | 1-(D_phys*F_TRZ)^2 | `21/25` | 0.84 | 0.84 | VERIFIED_LIVE | PAPER_2134 | 0.0 |
| galactic_distance | D_crit*SO_5^19 | `26e19` | 2.6e20 | 2.6e+20 | VERIFIED_LIVE | PAPER_2139 | 0.0 |
| bd2522_mass | D_phys*SO_5 | `4*10` | 40 | 40.0 | VERIFIED_LIVE | PAPER_1984 | 0.0 |
| hodge_identity_exact | (D_phys+D_BSFG)/SO_5 | `10/10` | 1.0 | 1.0 | VERIFIED_LIVE | PAPER_1230 | 0.0 |
| monty_hall | 2/(D_phys-1) | `2/3` | 0.6667 | 0.6666666666666666 | VERIFIED_LIVE | PAPER_1406 | 0.0 |
| plasmoid_fps | SO_5^2/(D_phys-1) | `100/3` | 33.333 | 33.333333333333336 | VERIFIED_LIVE | PAPER_2096 | 0.0 |
| plasmoid_t_photo | (D_phys-1)(SO_5+1)F_TRZ^2 | `3*11*0.01` | 0.33 | 0.33 | VERIFIED_LIVE | PAPER_2096 | 0.0 |
| plasmoid_t_batch | N_CH/(2*SO_5) | `9/20` | 0.45 | 0.45 | VERIFIED_LIVE | PAPER_2096 | 0.0 |
| chain_E_0 | F_TRZ^(D_crit-D_BSFG) | `0.1^20` | 1e-20 | 1.0000000000000011e-20 | VERIFIED_LIVE | PAPER_2119 | 0.0 |
| reactor_bulb_W | A_5+SO_5/2 | `60+5` | 65 | 65.0 | VERIFIED_LIVE | PAPER_2078 | 0.0 |
| galactic_ratio | D_BSFG/D_phys | `6/4` | 1.5 | 1.5 | VERIFIED_LIVE | PAPER_2077 | 0.0 |
| ftrz_22_rung | F_TRZ^(D_crit-D_phys) | `0.1^22` | 1e-22 | 1.0000000000000012e-22 | VERIFIED_LIVE | PAPER_2095 | 0.0 |
| frame_count | SO_5^2/D_phys | `100/4` | 25 | 25.0 | VERIFIED_LIVE | PAPER_2065 | 0.0 |
| cp2_generator_W | D_crit-N_CH | `26-9` | 17 | 17.0 | VERIFIED_LIVE | PAPER_2085 | 0.0 |
| crab_spin_Hz | (D_phys-1)SO_5+2F_TRZ | `30+0.2` | 30.2 | 30.2 | VERIFIED_LIVE | PAPER_2062 | 0.0 |
| bubble_nebula_Msun | 2*D_BSFG*SO_5^2 | `2*6*100` | 1200 | 1200.0 | VERIFIED_LIVE | PAPER_2072 | 0.0 |
| chemistry_octet | 2*D_phys | `8` | 8 | 8.0 | VERIFIED_LIVE | PAPER_2037 | 0.0 |
| so5_backbone_family | coeff*SO_5^n | `80+ instances` | various | 127.0 | MODULE_VERIFIED | PAPER_2019-2092 | 0.0 |
| backbone_object_locks | coeff*PRIM^n per (object,observable) | `115 live-computed fns` | various | 127.0 | MODULE_VERIFIED | PAPER_2019-2092 | 0.0 |
| material_landmark_family | integer/real primitive chains | `191 fns (80 live-composed + 111 stated-disclosed)` | various | 1272.0 | MODULE_VERIFIED | PAPER_1600-1799 | 0.0 |
| fermion_generations | D_phys - 1 | `4-1` | 3 | 3.0 | VERIFIED_LIVE | PAPER_1220 | 0.0 |
| riemann_t10000 | S_26 Ramanujan chain | `` | 9877.78265 |  | DISPATCH_VERIFIED | PAPER_1290 | 0.0 |
| page_recovery | F_UBii buoyancy surface | `` | 0.99596 |  | DISPATCH_VERIFIED | PAPER_1280 | 0.0 |
| ssq_26_suppression | exp(-SSq n/26) | `n=13 -> sqrt(e^-SSq)` | 0.752 | 0.7520142543193826 | DERIVED_LIVE | CP4_NOMAD | 0.0 |
| meissner_sc_m | 1 - B/B_crit | `B_crit=4.4e13` | <=1 |  | DISPATCH_VERIFIED | CP4_universal | 0.0 |
| hawking_uqff_ratio | (1+F_TRZ)(1-F_TRZ) | `1-F_TRZ^2` | 0.99 | 0.99 | VERIFIED_LIVE | CP1_Temperature | 0.0 |
| white_hole_ratio | 1-F_TRZ | `9/10` | 0.9 | 0.9 | VERIFIED_LIVE | CP1_WhiteHole | 0.0 |
| er_epr_throat | l_Pl*(rho_UA/rho_SCm) | `10 l_Pl` | 1.616e-34 | 1.6159999999999997e-34 | DERIVED_LIVE | CP1_ER_EPR | 0.0 |
| tc_boost | 1+F_TRZ | `11/10` | 1.1 | 1.1 | VERIFIED_LIVE | CP1_HolographicSC | 0.0 |
| n_generations | D_phys - 1 | `4-1` | 3 | 3.0 | VERIFIED_LIVE | PAPER_1220 | 0.0 |
| hawking_ratio | 1-F_TRZ^2 | `0.99` | 0.99 | 0.99 | VERIFIED_LIVE | CP1 | 0.0 |
| phonon_Q | f_SCm/Gamma | `25/2` | 12.5 | 12.5 | VERIFIED_LIVE | PAPER_910/911 | 0.0 |
| fubii_registry | F_U - F_Bi - F_i | `17 variants` | module |  | DISPATCH_VERIFIED | PAPER_036-039 | 0.0 |
| chandrasekhar_mass | F_TRZ*D_phys^2*(1-F_TRZ) | `0.1*16*0.9` | 1.44 | 1.4400000000000002 | VERIFIED_LIVE | SESSION_383 | 0.0 |
| isco_radius | D_BSFG | `6` | 6 | 6.0 | VERIFIED_LIVE | SESSION_386 | 0.0 |
| top_yukawa | 1-F_TRZ^2 | `0.99` | 0.99 | 0.99 | VERIFIED_LIVE | SESSION_376 | 0.36 |
| alpha_s_composed | F_TRZ K_Mex SSq - F_TRZ^3 Phi_res | `` | 0.11791 | 0.11791666666666667 | DERIVED_LIVE | SESSION_378 | 0.008 |
| jarlskog | F_TRZ^5 D_BSFG SSq (1-F_TRZ K_Mex SSq) | `` | 3.014e-5 | 3.0138750000000003e-05 | DERIVED_LIVE | SESSION_374 | 0.46 |
| dpm_layer_ladder | hbar c i^5/r^2 | `i^5 scaling` | 2^5=32 verified | 32.0 | DERIVED_LIVE | CoAnQi_MAIN_1 | 0.0 |
| pi26_gate | sin(pi/26) | `` | 0.120537 | 0.12053668025532305 | DERIVED_LIVE | CoAnQi_S116 | 0.0 |
| hawking_T_10Msun | hbar c^3/(8pi G M k_B) | `` | 6.155e-9 K | 6.167769411934773e-09 | DERIVED_LIVE | PAPER_081 | 0.0 |
| pbh_delta_c | Harrison-Zeldovich | `` | 0.45 |  | DISPATCH_VERIFIED | PAPER_083 | 0.0 |
| tde_fallback | 2pi sqrt(R_t^3/GM) | `` | event-specific |  | DISPATCH_VERIFIED | PAPER_087 | 0.0 |
| ssq_origin | 0.755^2 | `` | 0.570025 | 0.570025 | DERIVED_LIVE | PAPER_094 | 0.004 |
| whittaker_closure | sum 26 (phi+chi) | `` | <1e-10 |  | DISPATCH_VERIFIED | PAPER_097 | 0.0 |
| plasma_freq_thz | sqrt(n_e e^2/eps0 m_e) | `` | n-dependent |  | DISPATCH_VERIFIED | PAPER_100 | 0.0 |
| higgs_ladder_n | log10(E)+20 | `` | 12.30 | 12.301572524756274 | DERIVED_LIVE | PAPER_112 | 0.0 |
| resonance_cascade | R_basic^12 | `1.5^12` | 129.7 | 129.746337890625 | VERIFIED_LIVE | PAPER_115 | 0.0 |
| rho_lambda_c4 | Lambda c^4/8piG | `` | 5.3e-10 J/m3 | 5.297770457529142e-10 | DERIVED_LIVE | PAPER_118 | 0.0 |
| kappa_origin | 0.35/700 | `Fermi-4LAC fit` | 5e-4/day | 0.0005 | DERIVED_LIVE | PAPER_125 | 0.0 |
| halflife_ereact | tau ln2 | `2000*0.693` | 1386 days | 1386.2943611198905 | DERIVED_LIVE | PAPER_125 | 0.0 |
| doubly_magic_sn | 2 SSq E_8 | `` | 1.14e-12 J | 1.1399999999999998e-12 | DERIVED_LIVE | PAPER_124 | 0.0 |
| eps_ua | rho_UA/rho_total | `` | 0.043 |  | DISPATCH_VERIFIED | PAPER_126 | 0.0 |
| hoyle_state | E_0 sum(SSq^k)+dE_SCm | `3*2.08+0.414` | 6.654 MeV | 6.654278999999999 | DERIVED_LIVE | PAPER_132 | 0.28 |
| ssq_geometric_sum | 1+SSq+SSq^2+SSq^3 | `` | 2.080 | 2.0800929999999997 | DERIVED_LIVE | PAPER_132 | 0.0 |
| density_ladder_pivot | rho_0 10^(n-13) | `n=13` | rho_SCm | 7.09e-37 | DERIVED_LIVE | PAPER_137 | 0.0 |
| genesis_fu | E_react v^1 chain | `` | 1.18e53 |  | DISPATCH_VERIFIED | PAPER_133 | 0.0 |
| forty_sixty | (D_phys,D_BSFG)/SO_5 | `(4,6)/10` | (0.4,0.6) | 0.4 | DERIVED_LIVE | PAPER_143 | 0.0 |
| hubble_time | 1/H_0 | `A_5+SO_5 route` | 4.41e17 s | 4.408142857142857e+17 | DERIVED_LIVE | PAPER_143 | 0.0 |
| ptoe_anchor | k_A hydrogen | `` | 0.4604 V |  | DISPATCH_VERIFIED | PAPER_142 | 0.0 |
| sc_gap | hbar omega_SCm/2 | `` | T_c = 30 K | 29.987328023171614 | DERIVED_LIVE | PAPER_156 | 0.0 |
| hybrid_beta | e^(-B/B_crit) | `SGR 3e11` | 0.9933 | 0.9932050092465722 | DERIVED_LIVE | PAPER_158 | 0.0 |
| complexity_exp | N^(1/SSq) | `` | N^1.754 | 1.7543859649122808 | DERIVED_LIVE | PAPER_156 | 0.0 |
| holmlid_xi | back-solved | `~F_TRZ^21 = F_TRZ^(D_crit-SO_5/2)` | 9.98e-22 | 1.0000000000000012e-21 | DERIVED_LIVE | PAPER_1133 | 0.16 |
| g593_E0 | back-solved | `~F_TRZ^20 = chain base` | 1.0024e-20 | 1.0000000000000011e-20 | DERIVED_LIVE | PAPER_593 | 0.24 |
| glueball_V | back-solved | `` | 4.72e-57 m^3 |  | DISPATCH_VERIFIED | PAPER_167 | 0.0 |
| dpmcosmo_rho | back-solved | `` | 1.318e-4 J/m^3 |  | CAPTURED_BACKSOLVE | Q-DPMCOSMO | 0.0 |
| q1412_phi_implied | 7.70/(K_MEX D_phys) | `~12/13=(D_crit/2-1)/(D_crit/2)` | 0.9240 | 0.9239999999999999 | DERIVED_LIVE | Q-1412 | 0.09 |
| s26_namespace | eq32 summation vs LENR anchor | `1.5403e5 vs 1.4531e26` | TWO OBJECTS |  | CAPTURED_BACKSOLVE | PAPER_001/1080 | 0.0 |
| ml_implied_ratios | stated/chain back-solve | `8 captured, rungs found` | various |  | CAPTURED_BACKSOLVE | R7_AUDIT | 0.0 |
| ssq_0622_origin | sqrt(Omega_DM/Omega_L) | `sqrt(0.3869)` | 0.622 | 0.6220128616033594 | VERIFIED_LIVE | PAPER_118 | 0.0 |
| tde_power_law | (t/t_fb)^-5/3 | `` | decay | 1.6666666666666667 | DERIVED_LIVE | PAPER_087 | 0.0 |
| jet_gamma_709 | (gamma-1)=6.09 | `gamma=7.09` | 6.09 | 6.088812050083354 | DERIVED_LIVE | PAPER_161 | 0.0 |
| scm_core_P | rho v^2 P_core | `1e15*1e16*1e-3` | 1e28 Pa | 1e+28 | DERIVED_LIVE | PAPER_138 | 0.0 |
| f_ub_volume_1_33 | Dk_eta x 10 x V-ratio | `7.25e8*10/33` | 2.1970e8 | 219696969.6969697 | VERIFIED_LIVE | PAPER_196/216 cross-check | 0.14 |
| q26_constant | 25!! | `double factorial 25` | 7.906e12 | 7905853580625.0 | DERIVED_LIVE | PAPER_205 corrected | 0.0 |
| vacuum_li26 | SSq Li_26(SSq) | `sum SSq^n/n^26` | 0.5700000048 | 0.5700000048414601 | DERIVED_LIVE | PAPER_205 | 0.0 |
| rho_fluid_wind_family | back-solved | `a_wind/(rho_w v^2)` | 1e-12 kg/m^3 | 9.999999999999998e-13 | DERIVED_LIVE | PAPER_227+228 consistency | 0.0 |
| k_lenr | back-solved | `F_LENR/(w_LENR/w0)^2` | 1e-19 | 1.0002427249171587e-19 | DERIVED_LIVE | PAPER_251/252 | 0.02 |
| k_neutron | back-solved | `F_n/sigma_n both ends` | 1e10 | 10000000000.0 | DERIVED_LIVE | PAPER_255/257 cross-check | 0.0 |
| q_wave_cgs | PAPER_270 chain | `1.1e65 x 2.82e-56` | 3.11e9 J/m^3 | 3102000000.0 | DERIVED_LIVE | PAPER_240<->270 resolution | 0.2 |
| ts_cosmic_bridge | pi/13.8 | `universal 27 orders` | 0.2277 | 0.22765164156447776 | DERIVED_LIVE | PAPER_288/300 | 0.0 |
| ui_canonical_confirm | PAPER_334 bifurcation | `beta F_TRZ w_s cos(1+f_TRZ)` | 2.75e-7 EXACT | 2.7500000000000007e-07 | DERIVED_LIVE | PAPER_646 lock | 0.0 |
| e_react_t0 | PAPER_393 confirmation | `rho v^2/rho_A` | 8.808e54 J | 8.809024e+54 | DERIVED_LIVE | PAPER_182/183 slip corrected | 0.01 |
| ym_route2_asymptote | PAPER_388 | `sqrt(rho_SCm/rho_UA)` | 0.3162 | 0.31622776601683794 | VERIFIED_LIVE | PAPER_1953 0.3-family candidate | 0.0 |
| rho_v_identified | PAPER_368 | `Lambda c^2/(8piG)` | 6.0e-27 kg/m^3 | 5.894268023833927e-27 | DERIVED_LIVE | Planck DE density = codebase rho_v | 1.7 |
| lambda_i_4th_term | PAPER_420 code-gap | `-sum lambda_i U_i E_react` | -2.75e-7 canonical | -2.7500000000000007e-07 | DERIVED_LIVE | MISSING TERM WIRED | 0.0 |
| ts00_resolved | PAPER_406 | `1.27e3 + 1.11e7` | 1.110127e7 | 11101270.0 | VERIFIED_LIVE | 165/172 fork closed | 0.0 |
| scm_mass_power_law | PAPER_405 | `M^(2/3)` | alpha = D_phys/D_BSFG | 0.6666666666666666 | DERIVED_LIVE | primitive hit | 3.0 |
| omega_lambda_duniverse | PAPER_456 | `Lambda c^2/(3H0^2)` | 0.634 = Omega_L | 0.6403921629831838 | DERIVED_LIVE | Friedmann identity | 0.0 |
| lenr_catalyst_ssq26 | PAPER_460 | `SSq^26 e^-pi` | 1.9425e-8 EXACT | 1.9425396567575907e-08 | DERIVED_LIVE | primitive rung | 0.1 |
