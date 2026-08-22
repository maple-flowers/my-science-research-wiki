# Phase C 第五十六批身份解析报告（entities 第 1-20 页）

> 主 Agent 直接基于页面内容完成身份判定（只读，未修改任何页面）。

## 身份判定表

| # | 路径 | 身份 | 判定依据 |
| :-- | :-- | :-- | :-- |
| 1 | entities/1T-MoTe2 | short-aggregation | 无 frontmatter，2 篇论文，含别名 d1t-mote2 |
| 2 | entities/1T-NbSe2 | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 3 | entities/1T-TaS2 | short-aggregation | 无 frontmatter，4 篇论文 |
| 4 | entities/1T-TaSe2 | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 5 | entities/1T-double-prime-TMD | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 6 | entities/1t-phase | canonical | 有 frontmatter（status: mature），完整正文（太奶导读/结构概览），3 篇论文 |
| 7 | entities/2H-NbSe2 | canonical | 有 frontmatter（status: mature），完整正文（太奶导读等），2 篇论文 |
| 8 | entities/2H-TaS2 | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 9 | entities/2H-TaSe2 | short-aggregation | 无 frontmatter，4 篇论文 |
| 10 | entities/2d-acar | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 11 | entities/2h-phase | canonical | 有 frontmatter（status: mature），完整正文（太奶导读/结构概览），2 篇论文 |
| 12 | entities/3r-tmds | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 13 | entities/4d-stem | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 14 | entities/A36-low-carbon-steel | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 15 | entities/ABINIT | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 16 | entities/AFM | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 17 | entities/ALD | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 18 | entities/AM2X4-intercalation-family | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 19 | entities/AOM | short-aggregation | 无 frontmatter，仅 1 篇论文 |
| 20 | entities/AR-N-4340 | short-aggregation | 无 frontmatter，仅 1 篇论文 |

## 类别汇总

| 身份类型 | 数量 |
| :-- | :-- |
| canonical | 3（1t-phase mature、2H-NbSe2 mature、2h-phase mature） |
| short-aggregation | 17 |
| alias / ambiguous / misplaced / no-evidence | 0 |

## 问题清单

1. **跨层碰撞**：1t-phase 与 concepts/1t-phase 碰撞（已知 3 对之一，保留）
2. **规范化名称重复**：无
3. **缩写/变体**：1T-MoTe2 含别名 d1t-mote2
4. **父子概念**：1T-MoTe2/1T-NbSe2/1T-TaS2/1T-TaSe2 ⊂ 1t-phase；2H-NbSe2/2H-TaS2/2H-TaSe2 ⊂ 2h-phase；3r-tmds ⊂ TMD；AM2X4-intercalation-family ⊂ intercalation
5. **歧义词**：无
6. **跨层误放**：无
7. **无证据页**：无
8. **反链弱相关**：1T-MoTe2 ← Islam2025enhancement/guoAdvancesTwodimensionalFerroelectric2025（TMD 超导/2D 铁电，间接）；1T-NbSe2 ← nakataRobustChargedensityWave2021（1T-TaSe2/NbSe2 CDW，间接）；1T-TaS2 ← cossuStackingChargedensityWaves2024/kimObservationPhaseTransition1997/nakataRobustChargedensityWave2021/Chen2019superconductivity（CDW/STM 相变/超导，间接）；1T-TaSe2 ← nakataRobustChargedensityWave2021（CDW，间接）；1T-double-prime-TMD ← tangCombiningIntrinsicSlidinginduced2025（滑移铁电，间接）；2H-TaS2 ← kimObservationPhaseTransition1997（STM 相变，间接）；2H-TaSe2 ← Barnett2006coexistence/kimObservationPhaseTransition1997/Chen2019superconductivity/gorkovStrongElectronlatticeCoupling2012（CDW/超导，间接）；2d-acar ← Laverock2005fermi（费米面嵌套，间接）；3r-tmds ← guoAdvancesTwodimensionalFerroelectric2025（2D 铁电，间接）；4d-stem ← sunSlidingFerroelectricityTwodimensional2025（滑移铁电，间接）；A36-low-carbon-steel ← Zhang2003a（铁素体相变，间接）；ABINIT ← Li2013bonding（单层 TMD 键合，间接）；AFM ← Kumar2017microstructuring（双光子聚合，间接）；ALD ← chenHafniumBasedFerroelectricPostMoore2026（Hf 基铁电，间接）；AM2X4-intercalation-family ← zhaoRealization2DMultiferroic2024（插层 2D 多铁，间接）；AOM ← Kumar2017microstructuring（双光子聚合，间接）；AR-N-4340 ← Kumar2017microstructuring（双光子聚合，间接）

## 说明

- 本批 20 页全部位于 entities 层
- 未修改任何页面，未提交
- 下一批从 entities 第 21 页开始
