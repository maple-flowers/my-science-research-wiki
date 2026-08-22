# Plan: Rewrite Sliding Ferroelectricity Concept Page

I need to update `wiki/concepts/sliding-ferroelectricity.md` to integrate recent research findings, specifically focusing on mechanisms (ripplocations), new materials (HgI2, FGT), and new phenomena (super-paraelectricity).

## User Requirements
- Integrate findings from `raw/note/` (sliding ferroelectricity, moire, switching, etc.).
- Ensure links `[[../../raw/note/CiteKey|Title]]` are correct.
- Rewrite `wiki/concepts/sliding-ferroelectricity.md` directly.
- **Security Constraint**: Use standard markdown image syntax with relative paths: `![caption](../../raw/figures/{citekey}/{filename})`.

## Integrated Content Points
1.  **HgI2/HgBr2**: Strong sliding ferroelectricity (~0.16 μC/cm²) and Rashba spin texture control (`chenStrongSlidingFerroelectricity2024`).
2.  **Fe3GeTe2 (FGT)**: Coexistence of ferromagnetism, metallicity, and switchable polarization via sliding (`miaoMagneticFerroelectricMetal2024`).
3.  **h-BN Dynamics**: Domain wall motion reducing switching fields by 100x, ps-scale switching, and Moiré super-paraelectricity vs. defect pinning (`heUltrafastSwitchingDynamics2024`).
4.  **Ripplocations**: Topological defects (buckled dislocations) acting as high-mobility domain walls (`wuSlidingFerroelectricity2D2021a`).
5.  **Terminology**: Use "Stacking-engineered Ferroelectrics" alongside "Sliding Ferroelectricity".

## Proposed Structure
1.  **Header**: Tags and Category.
2.  **Definition**: Updated with symmetry and stacking concepts.
3.  **Physical Origin**: Charge transfer mechanism and symmetry breaking.
4.  **Key Mechanisms & Dynamics**:
    - Ripplocations (Wu 2021).
    - Domain Wall Motion & Ultrafast Switching (He 2024).
5.  **Moiré Superlattices & Super-paraelectricity**:
    - Moire-induced domain patterns.
    - Super-paraelectric behavior (He 2024).
6.  **Materials & Properties**:
    - Group by type (Insulators, Metals/Magnetics).
    - Include HgI2 and FGT details.
7.  **Slidetronics & Multiferroicity**: Rashba coupling and multiferroic integration.
8.  **Internal References**: Updated list of notes.

## Execution Steps
1.  [X] Explore and read relevant notes.
2.  [X] Verify figure paths and manifests.
3.  [ ] Draft the final content.
4.  [ ] Write to `wiki/concepts/sliding-ferroelectricity.md`.
