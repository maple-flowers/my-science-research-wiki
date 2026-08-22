---
tags: [concept, magnetism, quantum-theory]
title: 布洛赫自旋波 / Bloch Spin Wave
type: concept
status: mature
domain: [magnetism, quantum-theory, magnonics]
mechanism: 铁磁/反铁磁基态的低能集体激发，自旋翻转以波矢 k 的平面波形式传播，色散由交换耦合决定，解释 T^3/2 定律与低温热力学
related_concepts: [heisenberg-model, spin-wave, ferromagnetism, stoner-model, molecular-field, exchange-interaction, brillouin-function, antiferromagnetism, magnon-hall-effect]
papers: [vanvleckSurveyTheoryFerromagnetism1945]
updated: 2026-08
---

# 布洛赫自旋波 / Bloch Spin Wave

布洛赫自旋波（Bloch spin wave）指**海森堡交换作用框架下磁性基态的低能集体激发**：单个自旋的翻转不是局域缺陷，而是以平面波 $e^{i\mathbf{k}\cdot\mathbf{r}}$ 的形式在自旋格点上传播，其色散关系 $\omega(\mathbf{k}) = 2JS(1-\cos ka)$ 由最近邻交换积分 $J$ 决定 [[../papers/vanvleckSurveyTheoryFerromagnetism1945]]。自旋波理论是量子磁性理论的核心支柱之一，为布洛赫 $T^{3/2}$ 定律、磁振子热力学与磁振子输运提供了微观基础。

## 👵 太奶导读

太奶啊，磁性材料在低温下，一个磁针稍微"歪"一点，这个"歪"不会停在原地，而是像水面波纹一样传遍整块磁体——这个"歪的波"就叫自旋波。布洛赫爷爷最早把它算清楚了：磁针越歪越多，材料的整体磁性会随温度升高而"变软"，他算出了一个规律叫"T 的 3/2 次方定律"。这就是为什么加热铁块到一定程度会失去磁性。

## 🧩 核心内容与机制 (Core Content)

- **基态与激发**：铁磁基态为全同向自旋排列；一个自旋翻转的"价键态"可分解为布洛赫自旋波（平面波叠加），每个自旋波携带 $\hbar$ 角动量，量子化即磁振子（magnon）。
- **色散关系**：最近邻海森堡模型下，铁磁自旋波色散 $\omega(\mathbf{k}) = 2JSz(1-\cos ka)$（$z$ 为配位数，$a$ 为晶格常数）；长波极限 $\omega \simeq Dk^2$，$D = JSa^2$ 为交换刚度。
- **布洛赫 T^{3/2} 定律**：由自旋波态密度积分得磁化温度依赖 $M(T) = M_0(1 - BT^{3/2})$，成功解释低温铁磁体实验，是自旋波存在的直接证据。
- **与巡游模型的对比**：斯通纳模型（[[../concepts/stoner-model|斯通纳模型]]）用能带理论描述巡游电子铁磁；自旋波理论基于定域海森堡模型，二者是"定域—巡游"两大范式的两极，真实材料介于其间。

## 📊 自旋波色散对照

| 体系 | 基态 | 色散 | 低温定律 |
|------|------|------|----------|
| 铁磁体 | 全同向排列 | $\omega \simeq Dk^2$（二次） | $T^{3/2}$ 定律 |
| 反铁磁体 | 奈尔交错排列 | $\omega \simeq c|k|$（线性） | 无 $T^{3/2}$（能隙/线性） |
| 巡游铁磁体（斯通纳） | 能带劈裂 | 费米面粒子-空穴激发 | 泡利顺磁+斯通纳判据 |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/heisenberg-model|海森堡模型]]：自旋波的理论框架。
- [[../concepts/spin-wave|自旋波]]：布洛赫自旋波的宏观表述。
- [[../concepts/ferromagnetism|铁磁性]]：自旋波的宿主序。
- [[../concepts/stoner-model|斯通纳模型]]：巡游电子范式的对照。
- [[../concepts/molecular-field|分子场理论]]：自旋波前的唯象框架。
- [[../concepts/exchange-interaction|交换相互作用]]：自旋波色散的微观来源。
- [[../concepts/antiferromagnetism|反铁磁性]]：线性色散自旋波。
- [[../concepts/magnon-hall-effect|磁振子霍尔效应]]：自旋波输运的拓扑效应。

## 📚 相关论文 (Related Papers)

- [[../papers/vanvleckSurveyTheoryFerromagnetism1945]]：Van Vleck 1945 综述系统确立了交换作用、自旋波与斯通纳模型的理论框架，自旋波概念的经典出处。

## 🏷️ 专业名词别名

- `spin-wave-theory`（concepts）
- `布洛赫 T^3/2 定律`（concepts）
