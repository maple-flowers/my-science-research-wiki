---
tags: [concept]
title: 'tight-binding'
type: concept
status: developing
papers: ['Barnett2006coexistence', 'CastroNeto2001charge', 'Inosov2008fermi', 'Johannes2008fermi', 'Makogon2012wave', 'hallEnvironmentalControlCharge', 'hillWhyAreThere2000a', 'monkhorstSpecialPointsBrillouinzone1976', 'nicholsonUniaxialStraininducedPhase2021']
updated: 2026-08-18
---

# tight-binding

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


紧束缚模型（tight-binding model）是一种以原子轨道为基矢构造固体电子哈密顿量的半经验量子方法：电子被近似局域在原子附近，通过轨道间"跳跃"（hopping）积分描述成键，从而在实空间中直观刻画能带、磁性、电荷有序等物性，是凝聚态理论最常用的模型工具之一。

## 👵 太奶导读

太奶啊，紧束缚模型就像"给每个原子发一张房卡"：电子平时待在自家原子房间（轨道）里，偶尔偷偷溜到邻居家（跳跃），溜得越勤，就越像金属。把这张"串门地图"（跳跃积分）代进量子力学公式，就能算出材料能带长什么样。很多漂亮的物理——电荷密度波的"波浪"、超导的配对、拓扑边界态——都能用这个简单模型讲清楚。

## 🧩 核心内容与机制 (Core Content)

- **模型框架**：以布洛赫和/或局域轨道为基，哈密顿量由在位能 ε 与跳跃积分 t 决定；单带/多带、自旋轨道耦合可在框架内系统加入。
- **能带与费米面**：紧束缚给出解析或半解析能带色散，可定量讨论费米面形状与嵌套（nesting）——嵌套是 CDW 与自旋密度波失稳的关键。
- **与 DFT 的联系**：紧束缚参数可取自第一性原理拟合（如 Wannier 函数、DFTB），使模型兼具物理直观与定量精度。
- **应用场景**：TMD 中 CDW 与超导共存、2H-NbSe₂ 层间堆叠效应、拓扑半金属相变（[[../papers/nicholsonUniaxialStraininducedPhase2021]]）等。
- **方法地位**：介于全电子 DFT 与纯唯象模型之间，是理解"为什么"的桥梁，也构成 [[../concepts/dftb|DFTB]] 等半经验方法的基础。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/band-structure|能带结构]]：紧束缚的直接输出。
- [[../concepts/charge-density-wave|电荷密度波]]：费米面嵌套驱动的电子序。
- [[../concepts/dftb|dftb]]：基于紧束缚思想的半经验量子方法。
- [[../entities/DFTB+|DFTB+]]：SCC-DFTB 计算软件。

## 📚 相关论文 (Related Papers)

- [[../papers/Barnett2006coexistence]] — Coexistence of Gapless Excitations and Commensurate Charge-Density Wave in the 2H Transition Metal Dichalcogenides
- [[../papers/CastroNeto2001charge]] — Charge Density Wave, Superconductivity, and Anomalous Metallic Behavior in 2D Transition Metal Dichalcogenides
- [[../papers/Inosov2008fermi]] — Fermi surface nesting in several transition metal dichalcogenides
- [[../papers/Johannes2008fermi]] — Fermi surface nesting and the origin of charge density waves in metals
- [[../papers/Makogon2012wave]] — Spin-charge-density wave in a rounded-square Fermi surface for ultracold atoms
- [[../papers/hallEnvironmentalControlCharge]] — Environmental Control of Charge Density Wave Order in Monolayer 2H-TaS₂
- [[../papers/hillWhyAreThere2000a]] — Why Are There so Few Magnetic Ferroelectrics?
- [[../papers/monkhorstSpecialPointsBrillouinzone1976]] — Special points for Brillouin-zone integrations
- [[../papers/nicholsonUniaxialStraininducedPhase2021]] — Uniaxial strain-induced phase transition in the 2D topological semimetal IrTe2
