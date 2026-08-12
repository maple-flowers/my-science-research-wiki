---
tags: [concept]
---

# 轴锥镜 (Axicon)

The term "axicon" (轴锥镜) describes a specialized conical optical element primarily used to transform a Gaussian laser beam into a non-diffracting Bessel beam or a ring-shaped intensity distribution in the far field. In the context of micro-optics and laser materials processing, axicons are increasingly fabricated using **two-photon polymerization (2PP)** due to its ability to create precise, arbitrary 3D surface profiles that overcome the limitations of traditional bulky optical components.

### Technical Principles and Beam Shaping

A physical axicon consists of a conical surface defined by a base angle $\alpha$ and a refractive index $n$. When a Gaussian beam passes through this element, the rays are refracted toward the optical axis at a constant angle $\gamma = (n-1)\alpha$, leading to the interference of rays that generates a **Bessel beam**. This beam is characterized by a central main lobe that maintains a constant diameter over a finite propagation distance (the non-diffracting zone) and is described by a zero-order Bessel function $J_0$ [[../papers/Unknown2025diffractive]].

In digital micro-optics, the axicon function is often implemented as a **Computer-Generated Hologram (CGH)**. The phase profile is calculated using an axicon term $\phi(r) = -k \sin\gamma \cdot r$, where $k$ is the wavenumber. For generating **high-order Bessel beams**, a spiral phase term $m\theta$ (where $m$ is the topological charge) is added, introducing **Orbital Angular Momentum (OAM)** and resulting in a ring-shaped intensity profile rather than a central peak [[../papers/Jia2023polymerization]].

### Micro-fabrication via Two-Photon Polymerization

The 2PP technique enables the fabrication of axicons with sub-micron resolution by inducing non-linear absorption within photoresists (e.g., **SU-8**, **SZ-2080**, or **FemtoBond-4B**). 
- **Architecture**: Axicons can be fabricated as solid 3D structures or as thin **Diffractive Optical Elements (DOEs)**. Millimeter-scale DOEs (up to 3.5 mm diameter) have been achieved by employing **stitching** algorithms to overcome the limited field of view of high-NA objectives [[../papers/Unknown2025diffractive]].
- **Phase Modulation**: The height $h$ of the polymerized structure is linked to the required phase shift $\Delta\phi$ by $h = \lambda \Delta\phi / [2\pi(n-n_0)]$. The choice of material, such as the organic-inorganic hybrid resist FemtoBond-4B, determines the refractive index (e.g., $n=1.55$ at 800 nm) and the structural height required for specific phase shifts. For example, a $6\pi$ modulation depth at 800 nm requires a height of approximately 4.4 $\mu$m [[../papers/Unknown2025diffractive]].
- **Discretization and Staircase Effect**: Since 2PP is a layer-by-layer process, the smooth conical surface is approximated by discrete steps. This "staircase effect" can introduce higher-order diffraction artifacts, but using a layer thickness of $\sim$100 nm significantly suppresses these artifacts while maintaining acceptable fabrication times [[../papers/Unknown2025diffractive]].

### Phase-Locked Properties and Applications

Axicon-generated beams exhibit unique properties central to advanced manufacturing and structural control:
- **Electronic Coupling and Polymerization**: In 2PP, the intensity distribution of the Bessel beam directly dictates the cross-linking density and energy deposition within the polymer. The high-order Bessel beam's ring-like profile allows for the rapid fabrication of micro-tubes in a single exposure. However, phase aberrations in the optical system can distort the "phase-locked" ideal beam shape, leading to uneven energy deposition and mechanical collapse of the structures due to unbalanced polymerization shrinkage stress [[../papers/Jia2023polymerization]].
- **Adaptive Optics and Correction**: To maintain structural integrity, **Spatial Light Modulators (SLM)** are used for **aberration correction**. Techniques such as multi-channel interferometric wavefront sensing can compensate for system aberrations (often $>4\pi$), restoring the uniform circularity and non-diffracting trajectory of the beam, which is crucial for high-quality micro-tube arrays [[../papers/Jia2023polymerization]].
- **High-Power Robustness**: 2PP-fabricated polymer axicons have demonstrated remarkable **laser damage thresholds**, withstanding peak power densities up to 24.8 GW/cm². The hybrid nature of these materials bridges the gap between polymer flexibility and inorganic durability, especially when post-processed via annealing or ALD coating [[../papers/Unknown2025diffractive]].

## Related Papers

- [[../papers/Jia2023polymerization]]
- [[../papers/Wang2023ultracompact]]
- [[../papers/Unknown2025diffractive]]
