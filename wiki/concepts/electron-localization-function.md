---
tags: [concept, DFT, electron-structure]
category: [Z01]
---

# 电子局域函数 / Electron Localization Function (ELF)

**电子局域函数**（ELF）是描述多电子体系中电子局域化程度的无量纲标量场，取值范围 0-1。ELF = 1 表示电子完全局域（如核附近），ELF = 0.5 表示电子气行为（自由电子），ELF → 0 表示电子离域。ELF 是分析化学键类型、孤对电子和电荷转移的有力工具。

## 核心内容

### 分析应用
- **化学键判据**：共价键在键轴中点 ELF 高，离子键在两原子间 ELF 低。
- **孤对电子**：ELF 可视化孤对电子分布，用于判断分子的反应活性位点。
- **电荷转移**：通过 ELF 差分图分析铁电极化过程中的电荷重新分布。

### 与 Bader 分析互补
- ELF 关注电子局域化程度，Bader 分析关注电荷分配，两者互补使用。

## Related Papers

- [[../papers/tangGridbasedBaderAnalysis2009]]：Bader 分析与 ELF 的网格化方法
- [[../papers/xuTunableFerroelectricTopological2022]]：铁电-拓扑相变中的 ELF 分析

## 关联概念与实体

- [[../concepts/bader-charge-analysis|Bader 电荷分析]]
- [[../concepts/electron-localization|电子局域化]]
- [[../entities/bader-code|Bader 电荷分析程序]]
