# Plan: Rewrite `topological-defects.md`

## Goal
Integrate scientific findings from recent research (sliding ferroelectricity, moire patterns, topological domain boundaries, and geometric frustration) into the `wiki/concepts/topological-defects.md` file. Ensure proper wiki linking and image referencing.

## Steps
1.  **Draft the new content structure**:
    *   Overview of topological defects in ferroics.
    *   **Classification**:
        *   Polar structures (Skyrmions, Vortices, Merons) + Geometric Frustration findings (Nahas 2016).
        *   1D Defects: Ripplocations in sliding ferroelectricity (Wu 2021).
        *   Topological Domain Boundaries (TDBs) in Quantum Spin Hall Insulators (Pedramrazi 2019).
    *   **Mechanisms**:
        *   Switching in sliding ferroelectrics via ripplocation movement (collective vs. isolated barrier).
        *   Ferroelastic manipulation of domain boundaries in 2D TMDs.
    *   **Bibliography & Links**: Ensure all citations and internal wiki links are correct.
2.  **Verify Image Paths**:
    *   Nahas 2016: `../../raw/figures/nahasFrustrationSelfOrderingTopological2016/fig_2_8IYT2TMA.png` (Self-ordered vortex array).
    *   Wu 2021: `../../raw/figures/wuSlidingFerroelectricity2D2021a/fig_1_37UWP3F7.png` (Sliding/Moire mechanism).
    *   Pedramrazi 2019: `../../raw/figures/pedramraziManipulatingTopologicalDomain2019/fig_1_K7BJPPZ4.png` (Domain boundaries).
3.  **Execute the rewrite**: Use the `Write` tool to overwrite the file.

## Constraints
*   Use standard markdown image syntax: `![Title](../../raw/figures/CiteKey/filename.png)`.
*   Maintain existing category/tags metadata.
*   Ensure internal links use the `[[../../raw/note/CiteKey|Title]]` or `[[concept-name|Display Name]]` format.
