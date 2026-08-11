---
title: Berry Phase
type: concept
tags: [topology, polarization, quantum-mechanics, ferroelectricity]
---

# Berry Phase (Geometric Phase)

The **Berry phase**, named after Sir Michael Berry, is a geometric phase acquired by a quantum system during a cyclic adiabatic evolution. Unlike the dynamic phase, which depends on the duration of the process and the energy of the state, the Berry phase depends solely on the path taken in the parameter space.

In the context of condensed matter physics, the parameter space is usually the **Brillouin Zone (BZ)**, and the Berry phase is fundamental to understanding topological insulators, the anomalous Hall effect, and the modern theory of polarization.

## 1. Theoretical Definition

### Berry Connection and Curvature
For a Bloch state $|u_{n\mathbf{k}}\rangle$ (the cell-periodic part of the wave function), the **Berry connection** $\mathbf{A}_n(\mathbf{k})$ (also called Berry vector potential) is defined as:
$$\mathbf{A}_n(\mathbf{k}) = i \langle u_{n\mathbf{k}} | \nabla_{\mathbf{k}} | u_{n\mathbf{k}} \rangle$$

The **Berry curvature** $\mathbf{\Omega}_n(\mathbf{k})$ is the "magnetic field" in $\mathbf{k}$-space, defined as the curl of the connection:
$$\mathbf{\Omega}_n(\mathbf{k}) = \nabla_{\mathbf{k}} \times \mathbf{A}_n(\mathbf{k})$$

### The Berry Phase
The Berry phase $\gamma_n$ acquired by an electron in band $n$ traversing a closed loop $C$ in the BZ is:
$$\gamma_n = \oint_C \mathbf{A}_n(\mathbf{k}) \cdot d\mathbf{k}$$

## 2. Modern Theory of Polarization (MTP)

The most significant application of the Berry phase in materials science is the **Modern Theory of Polarization**, established by [[../../raw/note/king-smithTheoryPolarizationCrystalline1993|King-Smith and Vanderbilt (1993)]]. Before this theory, polarization in crystals was ill-defined because it depended on the choice of the unit cell.

King-Smith and Vanderbilt showed that the change in electronic polarization $\Delta \mathbf{P}_{el}$ between two states (e.g., a centrosymmetric reference state and a ferroelectric state) is proportional to the Berry phase of the valence bands:
$$\Delta \mathbf{P}_{el} = \frac{ife}{8\pi^3} \sum_n \int_{BZ} d\mathbf{k} \langle u_{n\mathbf{k}} | \nabla_{\mathbf{k}} | u_{n\mathbf{k}} \rangle$$

### The Polarization Quantum
Polarization is not a single-valued vector but a **lattice of values** separated by the "polarization quantum":
$$\mathbf{P} = \mathbf{P}_{0} + \frac{e\mathbf{R}}{V}$$
where $\mathbf{R}$ is a lattice vector, $e$ is the electron charge, and $V$ is the unit cell volume.

## 3. Physical Interpretation: Wannier Centers

The Berry phase has a direct real-space interpretation through **Wannier functions**. The center of a Wannier function (WCC) for a given band is determined by the Berry phase integrated over the Brillouin Zone:
$$\bar{\mathbf{r}}_n = \frac{V}{(2\pi)^3} \int_{BZ} \mathbf{A}_n(\mathbf{k}) d\mathbf{k}$$
The total electronic polarization is essentially the sum of the displacements of these Wannier centers relative to the ionic positions. In ferroelectric switching, the spontaneous polarization arises from the collective shift of these charge centers.

## 4. Berry Phase in 2D Materials

In modern 2D materials research, Berry phase calculations are the standard method for determining spontaneous polarization in first-principles studies (DFT).

### In2Se3 and III2-VI3 Materials
[[../../raw/note/dingPredictionIntrinsicTwodimensional2017a|Ding et al. (2017)]] utilized the Berry phase method to predict intrinsic 2D ferroelectricity in $\text{In}_2\text{Se}_3$. They demonstrated that the non-centrosymmetric arrangement of atoms in the quintuple layers leads to a robust out-of-plane and in-plane polarization, which is switchable and persists at room temperature.

### 2D Multiferroics via Intercalation
Recent high-throughput studies, such as the work by [[../../raw/note/zhaoRealization2DMultiferroic2024|Zhao et al. (2024)]], have applied Berry phase calculations to screen for multiferroic materials in intercalated $\text{AM}_2\text{X}_4$ superlattices.

![Structure of T-AM2X4 and H-AM2X4](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_1_S88Q2EF3.png)
*Fig 1. Structural diagrams of intercalated 2D materials where Berry phase calculations are used to determine polarization states [[../../raw/note/zhaoRealization2DMultiferroic2024|Zhao2024]].*

![High-throughput screening flowchart](../../raw/figures/zhaoRealization2DMultiferroic2024/fig_2_7QNUMABJ.png)
*Fig 2. Flowchart of high-throughput screening using first-principles calculations to identify ferroic materials [[../../raw/note/zhaoRealization2DMultiferroic2024|Zhao2024]].*

Key findings in these 2D systems include:
- **Strong Magnetoelectric Coupling**: The Berry phase-derived polarization can be coupled to magnetic order, allowing for electrical control of magnetism.
- **Out-of-plane Polarization**: The broken inversion symmetry in intercalated bilayers (like $\text{T-PdZr}_2\text{Se}_4$) results in a significant $P_{out}$ (calculated in pC/m for 2D systems).

## 5. Related Concepts
- [[topology|Topological Invariants]] (e.g., Chern numbers are integrals of Berry curvature)
- [[wannier-functions|Wannier Functions]]
- [[ferroelectricity|Ferroelectricity in 2D]]
- [[anomalous-hall-effect|Anomalous Hall Effect]]
