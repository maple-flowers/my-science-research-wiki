---
tags: [concept]
---

# Arrhenius Deviation (非阿伦尼乌斯行为)

**Arrhenius Deviation** (or non-Arrhenius behavior) refers to the phenomenon where the temperature dependence of a transport property—such as the diffusion coefficient ($D$) or reaction rate—deviates from the linear relationship expected in a $\ln(D)$ vs. $1/T$ Arrhenius plot. In crystalline solids, this curvature typically signifies that the transport process is not governed by a single, static activation energy barrier, but rather by the coexistence of multiple parallel mechanisms with distinct activation energies.

## Physical Origin and Mechanisms

The presence of non-Arrhenius behavior is a hallmark of complexity in the potential energy surface (PES) of a material. According to the study of cation interstitial diffusion in **PbTe** and **CdTe** [[../papers/Mińkowski2021cation]], the deviation arises from two primary atomic-scale mechanisms:

1.  **Direct Hops**: The interstitial atom moves directly between adjacent interstitial sites. This is the "classical" diffusion path often assumed in static calculations.
2.  **Interstitial-Exchange Mechanism**: The interstitial atom "kicks out" a lattice atom, taking its site, while the displaced lattice atom becomes the new interstitial. This coordinated, multi-atom process often has a different activation energy and a longer effective displacement per event.

In the case of PbTe (Rocksalt structure), the exchange mechanism has a significantly lower activation energy ($E_{ex} \approx 224\text{--}309$ meV) compared to direct hops ($E_{hop} \approx 461\text{--}564$ meV). As temperature increases, the relative contribution of these two pathways shifts, leading to the observed "bending" in the Arrhenius plot.

## Phase-Locked Properties and Structural Context

The deviation is deeply tied to the **Phase-Locked Properties** of the crystal lattice:

-   **Crystal Structure**: The symmetry of the lattice determines the availability and degeneracy of these paths. In **PbTe**'s rocksalt lattice, the exchange mechanism is the dominant transport mode. In **CdTe**'s zinc-blende lattice, although direct hops between $T_a$ and $T_c$ interstitial sites are more frequent due to lower barriers, the exchange mechanism remains critical because its single-step displacement is roughly twice as long as a hop.
-   **Electronic Coupling**: The transition between mechanisms is driven by the dynamic electronic coupling between the interstitial and the surrounding lattice. In modern computational physics, **Neural Network Potentials (NNP)** are used to "lock" the high-dimensional electronic structure information (derived from DFT) into a force field, allowing for long-time MD simulations that can capture these rare exchange events that static Nudged Elastic Band (NEB) methods might overlook.
-   **Mathematical Formulation**: The total diffusion coefficient is modeled as a sum of two Arrhenius terms:
    $$D(T) = D_0^{hop} \exp\left(-\frac{E_{hop}}{k_BT}\right) + D_0^{ex} \exp\left(-\frac{E_{ex}}{k_BT}\right)$$
    This dual-exponential behavior is the fundamental mathematical reason for the curvature in the logarithmic representation.

## Research Significance

Understanding Arrhenius deviations is crucial for predicting the morphological evolution of heterostructures, such as the transformation of PbTe/CdTe layers into quantum dots. The "exchange" mechanism provides a micro-level explanation for how atoms can migrate across interfaces and facilitate the lattice reconstruction required for such phase transitions.

## Related Papers

- [[../papers/Mińkowski2021cation]] — Detailed study using NNP-MD to reveal the jump-exchange dual mechanism in IV-VI and II-VI semiconductors.
