---
tags: [entity]
---

# 双层包层单模光纤 (DCSMF)

**双层包层单模光纤**（Doubly Cladding Single-Mode Fiber, DCSMF）是一种通过结构微加工实现的特种传感光纤。其核心架构基于对标准单模光纤（如 Corning SMF-28e）的包层进行选择性剥离与功能性重建。在典型的制备工艺中，光纤包层的一部分被化学腐蚀以减小直径（作为内包层），随后在腐蚀区涂覆一层具有环境响应性的敏感材料（如[[../entities/agarose|琼脂糖]]水凝胶），形成新的功能化外包层 [[../papers/XiaokangZhang2013calibrating]]。

### 结构演化与倏逝场锁定

DCSMF 的物理实质是将光导波的能量从被严密封装的纤芯中“释放”出来，使其与外界环境发生相位锁定式的相互作用。根据[[../concepts/evanescent-field-sensing|倏逝场传感]]原理，当纤芯中的基模光束在光纤中传输时，一部分电磁场会渗透进入内包层和外包层。在 DCSMF 结构中，外包层材料的折射率会随目标物理量（如相对湿度、离子浓度）的变化而动态调整。

这种折射率的变化直接调制了倏逝场的穿透深度与吸收损耗，从而将环境信息“锁定”在光功率的衰减特征中。例如，当[[../entities/agarose|琼脂糖]]涂层吸湿溶胀时，其有效折射率降低，导致光功率损耗增加 [[../papers/XiaokangZhang2013calibrating]]。

### 相位锁定属性与性能表征

DCSMF 展现出高度的非线性与分段灵敏度特征。在 [[../papers/XiaokangZhang2013calibrating]] 的研究中，基于 DCSMF 的湿度传感器在低湿段（30%–90% RH）的灵敏度为 9.47 dB/%RH，而在高湿段（90%–100% RH）跃升至 94.0 dB/%RH，展现了近 10 倍的增益提升。这种分段特性源于感湿材料在接近饱和点时物理形态的剧烈变化。

此外，DCSMF 传感器不可避免地存在[[../concepts/cross-sensitivity|交叉敏感]]现象，特别是温度与湿度的深度耦合。这种耦合使得单一的线性拟合无法准确还原环境参数。为了解决这一问题，研究者通常采用[[../concepts/lookup-table-calibration|查找表校准法]]（Lookup Table Calibration），通过构建高维校准矩阵，将离散的实验观测点映射为连续的数字地图，从而实现复杂恶劣环境下的精准反演。

### 工业现场应用

由于 DCSMF 具备极低的插入损耗（可达 -0.08 dB）和坚韧的机械保护潜力（如铜线封装），它被广泛应用于土木工程的在役监测。在[[../material/fresh-concrete|新拌混凝土]]的实时监测中，DCSMF 传感器能够成功捕捉水泥水化放热导致的温度波动以及自干燥引起的相对湿度下降过程，验证了其在复杂电解质环境下的可靠性 [[../papers/XiaokangZhang2013calibrating]]。

## Related Papers

- [[../papers/XiaokangZhang2013calibrating]]
