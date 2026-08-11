---
title: Ferroelasticity
type: concept
tags: [phase-transition, domain-wall, ferroics, 2D-materials, straintronics]
---

# Ferroelasticity in 2D Materials

**Ferroelasticity** is a physical phenomenon where a material exhibits multiple stable orientation variants in the absence of external stress, and can be switched between these variants by the application of mechanical stress. In two-dimensional (2D) systems, ferroelasticity offers a unique platform for **straintronics**—the manipulation of electronic, magnetic, and topological properties through lattice distortion.

## 1. Physical Mechanisms

### 1.1 Peierls Distortion in 1T'-TMDs
In group-VI transition metal dichalcogenides (TMDs), the high-symmetry 1T phase is often unstable towards a structural distortion known as **Peierls distortion**. This leads to the formation of the **1T' phase** (e.g., in WTe$_2$ and MoTe$_2$), characterized by metal-atom dimerization and a distorted rectangular lattice.

![Atomistic structure of 1T and 1T' phases showing the structural distortion generic to group VI MX2 monolayers.](../../raw/figures/liFerroelasticityDomainPhysics2016/fig_1_YTRF2PW6.png)
*Source: [[../../raw/note/liFerroelasticityDomainPhysics2016|Li & Li, Nat. Commun. 2016]]*

This distortion can occur along three symmetry-equivalent directions of the triangular M-atom lattice, resulting in **three orientation variants** (O1, O2, and O3).

![Three orientation variants of 1T0–MX2 monolayers derived from the triangular lattice.](../../raw/figures/liFerroelasticityDomainPhysics2016/fig_2_KHBH8L57.png)

### 1.2 Antiferroelectric-Coupled Spontaneous Strain in $\beta'$-In$_2$Se$_3$
In van der Waals $\beta'$-In$_2$Se$_3$, ferroelasticity originates from an **antiferroelectric distortion** that is intrinsically coupled to a **spontaneous strain** ($\approx 0.49\%$). Unlike 1T'-TMDs where the distortion is driven by electronic dimerization, the ferroelasticity in $\beta'$-In$_2$Se$_3$ manifests as a nanostriped superstructure.

![TEM and STEM evidence of the nanostriped superstructure and satellite diffraction in β’-In2Se3.](../../raw/figures/xuTwodimensionalFerroelasticityVan2021/fig_1_3385VJAN.png)
*Source: [[../../raw/note/xuTwodimensionalFerroelasticityVan2021|Xu et al., Nat. Commun. 2021]]*

## 2. Quantitative Energetics and Switching

### 2.1 Transition Barriers
The switching between ferroelastic variants requires overcoming a potential energy barrier. In 1T'-WTe$_2$, Nudged Elastic Band (NEB) calculations reveal a relatively low transformation barrier of **< 0.2 eV per formula unit (f.u.)**, facilitating reversible switching.

![NEB calculation of transformation barrier and the pathway for orientation switching in 1T0–WTe2.](../../raw/figures/liFerroelasticityDomainPhysics2016/fig_6_DIRK5297.png)

### 2.2 Strain-Induced Switching
Experimental validation in $\beta'$-In$_2$Se$_3$ has shown that domain variants can be controlled by uniaxial tensile strain. A switching strain of **$\le 0.5\%$** is sufficient to induce domain wall motion, while the material maintains mechanical integrity up to a yield strain of **$\approx 5.5\%$**.

![Polarized-light imaging showing reversible domain switching under vertical uniaxial tensile strain.](../../raw/figures/xuTwodimensionalFerroelasticityVan2021/fig_4_BVK6GKZN.png)

## 3. Domain Physics
Ferroelastic domains are regions of different orientation variants separated by **domain walls (DWs)**. These boundaries are categorized based on their symmetry properties:
- **W-walls:** Symmetry-fixed boundaries.
- **S-walls:** Strain-dependent boundaries that may change orientation to minimize elastic energy.

In 2D systems, these walls can exhibit distinct electronic states or even host topological phases.

![DFT-relaxed atomistic structures of domain boundaries between variants O1, O2, and O3 in 1T0–WTe2.](../../raw/figures/liFerroelasticityDomainPhysics2016/fig_7_BRNW8WQ3.png)

## 4. Multiferroicity and Intercalation Strategies
Emerging research focuses on coupling ferroelasticity/ferroelectricity with magnetic order to create **2D Multiferroics**. A promising strategy involves the intercalation of metal atoms (A) into MX$_2$ bilayers to form $AM_2X_4$ compounds. High-throughput screening has identified 21 candidates with strong magnetoelectric coupling, where the magnetic ground state can be controlled by ferroic switching.

![Structural diagram of intercalation compounds AM2X4 for multiferroic realization.](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_1_S88Q2EF3.png)
*Source: [[../../raw/note/zhaoRealization2DMultiferroic2024|Zhao et al., npj Comput. Mater. 2024]]*

| Property | Typical Value | Material System |
| :--- | :--- | :--- |
| **Spontaneous Strain** | ~3% (TMDs), 0.49% (In$_2$Se$_3$) | 1T'-MX$_2$, $\beta'$-In$_2$Se$_3$ |
| **Switching Barrier** | < 200 meV/f.u. | 1T'-WTe$_2$ |
| **Yield Strain** | ~5.5% | $\beta'$-In$_2$Se$_3$ |

## References
- [[../../raw/note/liFerroelasticityDomainPhysics2016|Li, W., & Li, J. (2016). Ferroelasticity and domain physics in two-dimensional transition metal dichalcogenide monolayers. Nature Communications, 7, 10843.]]
- [[../../raw/note/xuTwodimensionalFerroelasticityVan2021|Xu, C., et al. (2021). Two-dimensional ferroelasticity in van der Waals β’-In2Se3. Nature Communications, 12, 3600.]]
- [[../../raw/note/zhaoRealization2DMultiferroic2024|Zhao, Y., et al. (2024). Realization of 2D multiferroic with strong magnetoelectric coupling by intercalation: a first-principles high-throughput prediction. npj Computational Materials, 10, 131.]]
