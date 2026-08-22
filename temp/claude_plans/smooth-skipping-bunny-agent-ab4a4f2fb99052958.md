# Magnetoelectric Coupling Concept Page Update Plan

Update the magnetoelectric coupling concept page to include recent advancements in 2D materials, sliding ferroelectricity, and strain-mediated coupling based on research notes in the repository.

## User Requirements
- Integrate findings from `raw/note/` (sliding ferroelectricity, moiré, switching, etc.).
- Update mechanisms and materials sections.
- Ensure correct link formatting: `[[../../raw/note/CiteKey|Title]]`.
- Rewrite the file directly.

## Proposed Changes

### 1. Update Definition & Significance
- Keep the core definition.
- Emphasize the shift towards 2D van der Waals (vdW) systems and ultra-low energy consumption (sub-aJ level).

### 2. Restructure "Implementation Routes" (实现路线)
- **Traditional Routes**: Maintain brief mention of Single-phase (Type I/II) and Bulk Composites.
- **New 2D/vdW Routes**:
    - **Strain-mediated vdW Heterostructures**: Using organic ferroelectrics (e.g., P(VDF-TrFE)) to control magnetic anisotropy in 2D ferromagnets (e.g., Fe3GaTe2) at room temperature.
    - **Sliding Ferroelectricity**: Interlayer sliding in vdW materials (e.g., HgI2, WTe2) generating switchable polarization that couples to spin textures (Rashba effect).
    - **Intercalation Induced Multiferroicity**: Superlattice strategy (AM2X4) for strong coupling and topological magnetic structures (Skyrmions).

### 3. Update "Related Notes" (本库相关)
- Retain existing foundational citations.
- Add new key notes:
    - [[../../raw/note/feiFerroelectricSwitchingTwodimensional2018a|Ferroelectric switching of a two-dimensional metal]]
    - [[../../raw/note/chenStrongSlidingFerroelectricity2024|Strong Sliding Ferroelectricity and Its Coupling to Rashba Spin Texture in 2D HgI2]]
    - [[../../raw/note/zhaoRealization2DMultiferroic2024|Realization of 2D multiferroic with strong magnetoelectric coupling by intercalation: a first-principles high-throughput prediction]]
    - [[../../raw/note/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025|Ferroelectricity-driven Strain-mediated Magnetoelectric Coupling in 2D Fe3GaTe2/P(VDF-TrFE) Heterostructure]]

## Implementation Details
- Ensure standard Markdown syntax for images if applicable (though currently focusing on text and links).
- Verify all relative paths to notes are correct.
