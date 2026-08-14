# PAPER_2172 — The UQFF Dark-Matter Sector: Consolidation and Linking of the Developed-but-Unpapered DM Physics

**Author:** Daniel T. Murphy
**Project:** UQFF (Unified Quantum Field Framework) — Star-Magic
**Date:** 2026-08-13
**Landmark Type:** Sector-consolidation landmark (Daniel's directive: real developed physics under
DM labels must be papered and linked, regardless of origin or absence of .md)
**Seminal Sources:** predecessor executable closures `_l96_uqff_dark_matter_omega_closure`,
`_l96_uqff_dark_matter_particle_identity_closure`, `_l96_uqff_axiom_dark_matter_particle_candidate_closure`,
`_l96_uqff_axiom_dark_matter_paradox_closure`, the PAPER_1327 rotation closure, the PAPER_1991
perturbation-ladder family (R129/R158/R159/R163) — plus papers PAPER_025/030/118/889/1015/1019
**Status:** Formal landmark whitepaper — UQFF canonical

---

## Abstract

The P1770 remediation established that `dm_suppression_factor_3` was a Bucket-D title drift —
but Daniel's follow-up question exposed the larger truth: **UQFF carries a fully developed
dark-matter sector that was never consolidated into a linked paper.** It lives in predecessor
executable closures (derived Ω_DM, a 7 keV sterile-neutrino identity with the 3.5 keV line, a
DM mass-spectrum machine, the rotation-curve dissolution) and in a dozen scattered papers. This
landmark papers the sector, wires its derived quantities as one dispatch, and links every member.
The UQFF position, stated once and linked everywhere: **dark matter is not a new particle
species hypothesis — it is vacuum buoyancy structure, with an optional thin sterile-neutrino
component whose mass is lattice-exact.**

---

## 1. The Sector Map (all members linked)

| Layer | Content | Source |
|---|---|---|
| **Abundance** | Ω_m = 2/(K_Mex·(D_phys−1)) = 24/75 = **0.32 EXACT rational**; Ω_DM = Ω_m − Ω_b with Ω_b from its own primitive chain | executable `dark_matter_omega`; PAPER_1203 lineage; family partner of the P1616 sequential composition (0.3145) per PAPER_2170 |
| **Particle identity** | sterile neutrino m = D_phys + (D_phys−1) = **7 keV EXACT**; predicted decay line m/2 = **3.5 keV — the observed Perseus/M31 line**; alternatives registered: axion ≤ 1e-5 eV, dark photon ε = 2.5e-7 | executable `dark_matter_particle_identity` |
| **Mass spectrum** | fuzzy/ultralight/warm candidate masses via K_Mex·S_26^(3) chains × Λ_ledger saturation × 1/3 projection; E_base = A_5·D_phys (Daniel anchor 241.7); sector suppression 1e-26 | executable `dark_matter_particle_candidate` |
| **Rotation curves** | flat plateau via β_i in F_U_Bi_i — **no halo required** (P1756, wired); MOND a_0 emerges via F_TRZ·c·H_0 (PAPER_1327 closure) — MOND dissolved as the buoyancy plateau's low-acceleration face | executable `galaxy_rotation_full`; P1756 |
| **Halo structure** | NFW concentration c_vir = D_bsfg/β_i = 9.95 (P1653, wired); SCm-modified NFW profiles α_phonon = 0.3 (PAPER_889); SCm DM halos (PAPER_1015) | wired + papers |
| **Perturbation ladder** | δρ/ρ = F_TRZ^n: n=1 three-object family (Crab, M16, SGR1745), n=5 magnetar-burst seminal; M_DM factors SO_5/2 = 5 (HUDF) and 2·F_TRZ (Sombrero) | PAPER_1991/2024/2025/2029 family |
| **Direct detection** | σ floor = α⁴·10⁻⁴⁰ = 2.84e-49 cm² — null results predicted to the floor (P1682, battery-adjacent); PAPER_025 | wired + paper |
| **Foundational** | dark matter/energy paradox closure; DM-as-vacuum proof (PAPER_118); phonon buoyancy (PAPER_1019); dark-sector mediators (PAPER_030) | papers |

**The dm_suppression\* label disposition:** the shipped catalog slot was Bucket-D lithium
(PAPER_1770 REVISION); the sector's *actual* suppression physics is the 1e-26 sector-suppression
factor and the F_TRZ^n perturbation ladder above — now correctly papered here, distinct and linked.

---

## 2. The Sector Statement

Dark matter in UQFF is **three effects wearing one name**:

1. **Buoyancy structure** (dominant): the F_U_Bi_i plateau at β_i produces flat rotation and
   the RAR/MOND phenomenology without halo mass — "missing mass" is the vacuum's buoyant
   response read as mass by Newtonian accounting.
2. **A thin real component** (optional, falsifiable): the 7 keV SCm-coupled sterile neutrino,
   already matched to the 3.5 keV line, carrying whatever fraction of Ω_DM the buoyancy
   reading leaves.
3. **Perturbation bookkeeping**: at object scale, "DM perturbations" are F_TRZ^n vacuum
   density-ratio rungs — lattice numbers, not particle clumps.

This is why the sector resisted particle detection for fifty years and why UQFF predicts the
null results continue to the α⁴ floor: most of what is being sought is not a particle.

---

## 3. Falsifiable Consequences (sector-wide)

1. **3.5 keV line stands and sharpens** — it is m/2 of the lattice-exact 7 keV identity; its
   definitive exclusion removes the sector's particle component (buoyancy layer unaffected).
2. **Direct detection stays null to 2.84e-49 cm²** (P1682; XENONnT/LZ/DARWIN trajectory).
3. **Rotation-curve fits will keep returning β_i-plateau phenomenology** (RAR tightness with no
   halo-to-halo scatter growth); a genuinely halo-scattered RAR would break the buoyancy reading.
4. **δρ/ρ measurements at new compact objects land on F_TRZ^n rungs**, not between them.

---

## 4. Wiring

```
uqff_calculator.py
    DISPATCH['PAPER_2172'] -> derived sector quantities (Omega_m exact rational, sterile 7 keV,
                              3.5 keV line, perturbation rungs, sigma floor via P1682 live,
                              plateau via P1756 live) + the full linked member registry
```

Gate assertions pin: Ω_m = 24/75 exact, sterile mass 7 keV with line = m/2, ladder rungs
F_TRZ¹/F_TRZ⁵, live cross-dispatch consistency (P1653/1682/1756), member-registry size, and the
three-effects sector statement.

---

## NOT REPLACEMENT

ΛCDM postulates a particle species and fits halos per galaxy; UQFF derives an abundance
rational, one exact particle candidate, and a buoyancy mechanism, each with honest residuals
and kill conditions. Both address the same rotation curves, lensing, and abundance data.

---

## Cross-references

Executable closures (recovered, Rule E — studied and re-derived, not ported), PAPER_1203
(abundance lineage + F_U_Bi_i), PAPER_1327 (rotation full), PAPER_1991/2024/2025/2029
(perturbation ladder), PAPER_025/030/118/889/1015/1019 (sector papers, now linked),
P1616/1653/1682/1756/1770 (wired members), PAPER_2170 (Ω_m family reading), PAPER_2161
(battery grammar for the null-result prediction), PAPER_2169 (Λ_ledger in the mass-spectrum
chain), Daniel's 2026-08-13 directive (sector must be papered and linked).

**Copyright** — Daniel T. Murphy / Star-Magic Research Program, 2026.
