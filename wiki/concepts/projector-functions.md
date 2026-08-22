---
tags: [concept]
title: '投影函数 / Projector Functions'
type: concept
status: developing
papers: ['blochlProjectorAugmentedwaveMethod1994b', 'gajdosLinearOpticalProperties2006', 'kresseUltrasoftPseudopotentialsProjector1999c']
updated: 2026-08-18
---

# 投影函数 / Projector Functions

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


投影函数（projector functions）是**投影增强波（PAW）方法的核心构造**：在每个原子附近用局域原子波函数（投影子）将平滑赝波函数与全电子波函数衔接，实现"以全电子精度、赝势成本"的电子结构计算。投影函数的质量直接决定 PAW 计算的精度、收敛速度与可移植性，是现代第一性原理软件（VASP、ABINIT 等）的基石。

## 👵 太奶导读

全电子计算精确但太慢，赝势快却会抹掉原子核附近的真实细节。PAW 想了个"两头通吃"的招：外层用平滑波函数跑得快，原子核附近靠"投影函数"把真实细节找回来。投影函数就像"翻译器"，负责在平滑空间和真实空间之间来回翻译——翻译得好不好，决定算得准不准、快不快。

## 🧩 投影函数与 PAW 方法

- **PAW 方法的建立**：PAW 方法成功弥合了全电子方法与赝势方法之间的鸿沟，能以中等计算代价（如 30 Ry 平面波截断）获得与最先进全电子方法相当的精度，并支持高质量的分子动力学模拟；其精度和效率优于传统赝势，尤其在处理"硬"元素时优势明显（[[../papers/blochlProjectorAugmentedwaveMethod1994b|Blöchl 1994]]）。

## 🧩 投影函数与线性光学/介电计算

- **PAW 下的光学性质**：在标准 PAW 势下即可获得与全电子 APW+LO 方法高度一致的静态与动态介电函数，精度与收敛速度显著优于传统横向表达式；纵向表达式天然包含关键偶极矩修正项，为介电与光学性质计算提供可靠基准（[[../papers/gajdosLinearOpticalProperties2006|Gajdos 2006]]）。
- **与超软赝势的关系**：投影增强波（PAW）与超软赝势（USPP）在构造思想上共享"原子区投影"的框架，USPP 通过广义本征值问题提升截断能收敛性，二者均可追溯到投影子构造（[[../papers/kresseUltrasoftPseudopotentialsProjector1999c|Kresse 1999]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/blochlProjectorAugmentedwaveMethod1994b]] — Projector augmented-wave method
- [[../papers/gajdosLinearOpticalProperties2006]] — Linear optical properties in the projector-augmented wave methodology
- [[../papers/kresseUltrasoftPseudopotentialsProjector1999c]] — Ultrasoft pseudopotentials and projector augmented-wave methods

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/density-functional-theory|密度泛函理论]]：投影函数服务的计算框架。
- [[../concepts/dielectric-function|介电函数]]：PAW 投影子支撑的光学响应计算。
- [[../concepts/pseudopotential|赝势]]：与 PAW 互补的原子区处理方法。
- [[../concepts/gw-approximation|GW 近似]]：依赖高质量投影子的准粒子计算。
- [[../concepts/band-structure|能带结构]]：投影函数计算的电子结构输出。
