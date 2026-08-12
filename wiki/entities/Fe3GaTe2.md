---
tags: [entity]
---

# Fe3GaTe2

Fe3GaTe2 是一种备受关注的新型二维范德华（vdW）铁磁材料，其核心优势在于具备显著高于室温的居里温度（约 350-380 K）和强大的垂直磁各向异性（PMA）。作为 Fe3GeTe2 的同族改进材料，Fe3GaTe2 通过 Ga 原子的引入显著提升了磁序的稳定性，且具有良好的空气稳定性，是构建原子级平整界面的室温自旋电子学器件的理想平台。

## 物理特性与晶格结构

Fe3GaTe2 的层状结构由 Fe-Ga 合金层被 Te 原子夹持而成，每一层包含两个不等价的 Fe 位点。其铁磁性主要由 Fe 原子的 3d 电子主导。相较于同族的 [[../papers/zhangNonvolatileControlTopological2025]] 中提到的 Cr 基材料或 Fe3GeTe2，Fe3GaTe2 展现出更强的内在稳定性。在零应变状态下，其块体的磁各向异性能（MAE）约为 +2.158 meV/atom，表现出强烈的面外磁化偏好。

## “相位锁定”的磁电耦合机制

在“相位锁定性质”（Phase-Locked Properties）的框架下，Fe3GaTe2 的磁性状态与其晶格结构高度耦合。最新的实验进展表明，通过构建 Fe3GaTe2/P(VDF-TrFE) 垂直多铁异质结，可以实现对磁性的非易失性全电学调控 [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]。

该体系采用了创新的“非对称双栅极应变调控”范式：
1. **逆压电应变锁定**：底栅 P(VDF-TrFE) 受到刚性硅衬底的约束，其产生的逆压电形变被转化为面内剪切应力，并经范德华界面高效传递至 Fe3GaTe2。这种应变能够改变 Fe3GaTe2 的晶格常数 $a$ 和 $c$（应变范围约 0.4%-0.8%）。
2. **轨道重整化**：晶格畸变直接影响了 Fe 原子周围的晶体场环境，导致 $3d$ 轨道（如 $d_{z^2}$ 与 $d_{x^2-y^2}$）的能级分裂发生位移。DFT 计算证实，这种轨道重整化能够将各向异性常数 $K_1$ 调控至易磁化轴发生偏转，甚至实现面外到面内的转动 [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]。

## 应用前景

基于应变介导的“相位锁定”调控方案，Fe3GaTe2 异质结器件在功耗与速度上展现了显著优势：
- **超低功耗**：单次写入能耗仅为 0.5 aJ，远低于传统的 STT 或 SOT 方案。
- **高速切换**：响应速度达到 5 ns。
- **功能集成**：已成功演示了包括 AND、NAND、NOT 在内的可重构自旋逻辑门，以及用于模式识别的神经形态计算原型。

Fe3GaTe2 的室温特性与非易失性应变调控的结合，使其成为下一代非易失性存储、逻辑计算及存算一体架构的核心候选材料之一。

## Related Papers

- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]]
- [[../papers/zhangNonvolatileControlTopological2025]]
