---
tags: [concept, charge-density-wave, collective-excitation, raman]
title: 振幅子与相位子 / Amplitudon and Phason
type: concept
status: developing
domain: [charge-density-wave, condensed-matter-physics, lattice-dynamics]
mechanism: 电荷密度波复序参量的振幅自由度与相位自由度各自的集体振荡模式，分别对应有限频率的振幅模与无钉扎时趋于零频的相位模
related_concepts: [charge-density-wave, order-parameter, incommensurate-cdw, electron-phonon-coupling, soft-mode]
papers: [chowdhuryReviewTheoreticalComputational]
updated: 2026-08
---

# 振幅子与相位子 / Amplitudon and Phason

振幅子（amplitudon）与相位子（phason）是电荷密度波（charge density wave, CDW）序的两类集体激发模式。CDW 的序参量是一个复数量，写成"振幅 × 相位因子"的形式后，振幅与相位就成为两个独立的自由度：振幅模对应 CDW 序参量振幅的振荡，相位模对应 CDW 相位（整体滑移）的振荡。二者在拉曼光谱中表现为 CDW 的特征振动模式，是识别与刻画 CDW 相的重要谱学指纹。

## 👵 太奶导读

太奶，先说什么是**电荷密度波**（charge density wave，简称 CDW）：材料里的电子本来是均匀撒开的，到了低温会自己排成**疏密相间的垄沟**，像地里犁出来的一道垄、一道沟。

这垄沟能"抖"，而且有两种完全不同的抖法：

第一种，垄沟的位置不动，但**垄的高低在起伏**——垄一会儿堆得高、一会儿摊得平。这叫**振幅子**（amplitudon，"振幅"就是垄有多高）。要把垄堆高堆低是要费劲的，所以这种抖动有固定的频率，好比拨一根绷紧的弦，音调是定的。

第二种，垄的高低不变，但**整片垄沟一起往旁边平移**，垄挪到原来沟的位置去。这叫**相位子**（phason，"相位"就是垄沟排在哪儿）。妙处在于：只要地面平整没坑（专业叫"没有钉扎"，钉扎就是杂质像钉子一样把垄沟卡住了），整片垄沟往旁边挪一点根本不费力气——所以这种抖动的频率能低到接近零（物理上叫**戈德斯通模**，意思是"平移不花钱"的那种运动）。

分清这两种抖法为什么要紧？因为整片垄沟能不费劲地滑动，就意味着它能**驮着电荷跑**——这正是 CDW 那种奇特导电行为的根子。而实验上，科学家就是拿激光照材料、看散射出来的光变了多少频率（这叫拉曼光谱），从谱线里把这两种抖法认出来的。

## 🧩 物理实质：CDW 的集体激发

CDW 序参量可分解为振幅与相位两个自由度，其动力学分别由振幅子与相位子描述；振幅模通常具有有限频率，而相位模在无钉扎时趋于零频（Goldstone 模），是理解 CDW 动力学与输运的关键。

- **振幅子**：恢复力来自序参量振幅偏离平衡值所付出的自由能代价，因此频率有限、在拉曼谱中表现为可分辨的谱峰；接近 CDW 相变温度时振幅模软化，与[[../concepts/soft-mode|软模]]图像相通。
- **相位子**：整体相位平移不改变自由能（连续平移对称性），故为无能隙的 Goldstone 模。实际材料中杂质与公度性会将其钉扎并打开小能隙，相位子由此获得有限频率——CDW 的滑移输运阈值电场正源于此。
- 在非公度 CDW（[[../concepts/incommensurate-cdw|incommensurate CDW]]）中相位自由度更"自由"，相位子最接近理想 Goldstone 模；公度化后相位被锁定在离散取向，相位子被显著钉扎。

## 🔬 实验表征与理论计算

以 TaS₂、TaSe₂ 为代表的二维 TMD 中，DFT 结合"电子温度"方法与微压缩应力可模拟温度驱动与非公度 CDW 相变，并用于理解与预测拉曼光谱中的 CDW 特征模式（振幅模与相位模） [[../papers/chowdhuryReviewTheoreticalComputational]]。计算上，振幅模可通过沿 CDW 畸变方向的冻结声子（frozen-phonon）势能面提取；相位模因近零频、且对超胞尺寸与钉扎极其敏感，是计算上更困难的一类。

## 📚 相关论文 (Related Papers)

- [[../papers/chowdhuryReviewTheoreticalComputational]]：综述了二维材料中电荷密度波的计算方法，含 CDW 特征拉曼模式的模拟途径。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/charge-density-wave|电荷密度波]]：本条目所描述的有序态。
- [[../concepts/order-parameter|序参量]]：振幅/相位分解的出发点。
- [[../concepts/incommensurate-cdw|非公度电荷密度波]]：相位子最接近无能隙 Goldstone 模的场合。
- [[../concepts/electron-phonon-coupling|电子-声子耦合]]：决定振幅模频率与 CDW 稳定性。
- [[../concepts/soft-mode|软模]]：振幅模在相变点附近的软化行为。
- [[../entities/TaS2|TaS₂]]：CDW 集体模式的代表研究体系。
- [[../entities/TaSe2|TaSe₂]]：CDW 集体模式的代表研究体系。
