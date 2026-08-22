# Plan: Rewrite machine-learning-potential.md with advanced research findings

This plan outlines the steps to rewrite the Machine Learning Interatomic Potentials (MLIP) concept page by integrating specific findings from recent research notes on sliding ferroelectricity and moiré systems.

## Proposed Changes

### 1. Structure and Content Enhancement
- **Introduction**: Briefly define MLIP and its role in bridging the gap between DFT accuracy and large-scale simulation.
- **Physical Advantages**:
    - Highlight the $O(N)$ linear scaling and DFT-level precision.
    - Mention the phonon dispersion and DOS accuracy.
    - Discuss the DP-Gen active learning scheme.
- **Advanced Applications in Sliding Ferroelectricity** (Deep Integration):
    - **Ultrafast Dynamics (He 2024)**: Discuss the discovery of 6000 m/s domain wall speeds and ~15 ps switching in h-BN. Introduce "super-paraelectricity".
    - **Mechanical Bending & Kinks (He 2025)**: Detail the mechanical switching mechanism. Explain how the competition between bending energy and stacking energy leads to irreversible topological kinks (31° Néel and 57° Ising walls).
    - **Multi-state Storage (Tang 2025)**: Describe "composite ferroelectricity" where intrinsic distortions and sliding effects combine to create 6-state or 10-state systems.
- **Figures**: Insert relevant figures from the verified paths in `raw/figures/`.

### 2. Implementation Details
- Use `[[../../raw/note/CiteKey|Title]]` for all citations.
- Follow the required image syntax: `![Caption](../../raw/figures/{citekey}/{filename})`.
- Maintain a professional, academic tone.

## Task List
1. Create a temporary draft of the new content.
2. Review the draft against the research notes to ensure precision in numbers (e.g., velocities, energy barriers).
3. Overwrite the existing `wiki\concepts\machine-learning-potential.md` with the new content.

## Verification
- Check all internal links.
- Verify image paths.
- Ensure the Markdown formatting is clean.
