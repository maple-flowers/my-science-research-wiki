---
tags: [concept, first-principles, magnetism, 2D-materials]
title: 冻结磁振子法 / Frozen Magnon Method
type: concept
status: mature
domain: [first-principles, magnetism, magnonics, multiferroicity]
mechanism: 第一性原理中构造螺旋自旋结构并计算总能 E(q) 随自旋波矢 q 的变化，拟合海森堡交换参数进而重建磁振子色散的方法
related_concepts: [spin-wave, density-functional-theory, exchange-interaction, helical-magnetism, spin-spiral, magnetoelectric-coupling, heisenberg-model]
papers: [gaoGiantChiralMagnetoelectric2024a]
updated: 2026-08
---

# 冻结磁振子法 / Frozen Magnon Method

冻结磁振子法（frozen magnon method）是**第一性原理（DFT）计算磁振子色散与交换参数的标准方法**：通过在超胞中构造具有固定波矢 $\mathbf{q}$ 的螺旋（或摆线）自旋结构——即"冻结"一个特定磁振子模式的实空间构型——计算体系总能 $E(\mathbf{q})$，再从 $E(\mathbf{q})$ 与海森堡模型的对应关系拟合交换积分 $J_{ij}$，最终重建完整磁振子色散 $\omega(\mathbf{q})$。该方法无需含时响应，广泛用于磁性材料、二维磁体与螺旋多铁的第一性原理研究。

## 👵 太奶导读

太奶啊，要算一块磁体里"磁针波纹"（自旋波）的传播速度，科学家有个笨办法：先把磁针摆成一个固定的螺旋花纹（这就是"冻结"一个波纹），用超级计算机算出这种摆法要多少能量；换个更密的螺旋再算一次。把这些能量连成一条曲线，就能推出磁针之间的"拉力"（交换作用），波纹多快就能算出来了。这叫"冻结磁振子法"。

## 🧩 核心内容与机制 (Core Content)

- **基本流程**：① 构造螺旋自旋结构 $\mathbf{S}_i = (\cos\mathbf{q}\cdot\mathbf{r}_i,\ \sin\mathbf{q}\cdot\mathbf{r}_i,\ 0)$；② DFT 计算不同 $\mathbf{q}$ 的总能 $E(\mathbf{q})$；③ 将 $E(\mathbf{q})$ 映射到海森堡模型 $H = -\sum_{ij}J_{ij}\mathbf{S}_i\cdot\mathbf{S}_j$ 拟合 $J_{ij}$；④ 由傅里叶变换得到磁振子色散。
- **关键近似**：假定磁矩大小恒定（绝热近似），只保留交换项；自旋轨道耦合相关效应需单独处理。
- **在螺旋多铁中的应用**：对螺旋 vdW 多铁（如 [[../entities/NiI2|NiI2]]）计算螺旋磁结构能量与磁振子/电磁振子激发，定量刻画手性磁电关联的大小与起源（[[../papers/gaoGiantChiralMagnetoelectric2024a]]）。
- **与实验衔接**：计算色散可与非弹性中子散射、太赫兹/拉曼光谱对比，验证交换参数与磁各向异性。

## 📊 方法速览

| 步骤 | 内容 | 输入/输出 |
|------|------|-----------|
| 1 | 构造螺旋自旋超胞 | 波矢 $\mathbf{q}$、螺旋轴取向 |
| 2 | DFT 总能计算 | $E(\mathbf{q})$ 能量面 |
| 3 | 海森堡映射 | 交换积分 $J_{ij}$ |
| 4 | 色散重建 | $\omega(\mathbf{q})$、交换刚度 $D$ |

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/spin-wave|自旋波]]：磁振子色散的宏观对象。
- [[../concepts/density-functional-theory|密度泛函理论]]：方法的基础框架。
- [[../concepts/exchange-interaction|交换相互作用]]：被拟合的物理量。
- [[../concepts/helical-magnetism|螺旋磁序]]：螺旋结构的物理背景。
- [[../concepts/spin-spiral|自旋螺旋]]：冻结磁振子的实空间构型。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：螺旋多铁的应用场景。
- [[../concepts/heisenberg-model|海森堡模型]]：参数映射的目标模型。
- [[../entities/NiI2|NiI2]]：典型螺旋 vdW 多铁材料。

## 📚 相关论文 (Related Papers)

- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：在手性螺旋多铁中结合第一性原理磁振子计算与 THz 光谱，刻画巨手性磁电振荡。

## 🏷️ 专业名词别名

- `frozen-magnon-approach`（concepts）
- `螺旋自旋总能面法`（concepts）
