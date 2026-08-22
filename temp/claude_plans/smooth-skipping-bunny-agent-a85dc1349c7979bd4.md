# Plan: Update Experimental Setups Wiki

Update `E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\wiki\figures\experimental-setups.md` with new figures and tables from `raw/figures/` manifests.

## User Review Required

> [!IMPORTANT]
> I have identified 12 new figures and 4 new tables to add. This will increase the total items from 34 to 50.

- **New Figures (12)**:
  - `RecentAdvancesGrowth2025`: Fig 4 (CVD/MBE/ALD), Fig 10 (Device Fab), Fig 12 (THz Measurement), Fig 13 (XRD/ED), Fig 14 (AFM).
  - `Chen2016electrical`: Fig 5 (Photovoltaic setup).
  - `cuiIntercorrelatedInplaneOutofplane2018a`: Fig 1 (CVD Growth), Fig 2 (PFM), Fig 3 (Switching model), Fig 4 (CAFM).
  - `chenHafniumBasedFerroelectricPostMoore2026`: Fig 3 (Fab diagram), Fig 4 (FeFET/FTJ structures).
- **New Tables (4)**:
  - `Chen2016electrical`: Table 1 (PFM/c-AFM/PV parameters), Table 4 (Readout comparison).
  - `aiFerroelectricityCoexistedPorbital2022`: Table T1 (Research workflow).
  - `chenHafniumBasedFerroelectricPostMoore2026`: Table 2 (Device performance comparison).

## Proposed Changes

### Metadata Updates
- Update "收录总数" to **50**.
- Update counts to "(图: 12, 表: 33, 公式: 5)".

### File Content Additions
1. **New Section**: `## 🖼️ 示意图 (Figures)` inserted at line 10.
2. **Figure Entries**: Append 12 figure blocks with metadata tables (citekey, title, description, tags, materials, methods).
3. **Table Entries**: Append 4 table blocks to the `## 📊 数据表 (Tables)` section.

## Verification Plan

### Automated Tests
- Check markdown syntax integrity.
- Verify all `manifest.json` paths and `parent_key` consistency.

### Manual Verification
- Verify the counts match the actual number of entries in the file.
- Check that the new "Figures" section is correctly formatted with the standard emoji and heading style.
