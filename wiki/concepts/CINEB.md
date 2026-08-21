---
tags: [concept]
title: '爬坡弹性带 / Climbing Image Nudged Elastic Band (CI-NEB)'
type: concept
status: developing
papers: ['shenEmergenceMultipleFerroelectric2025', 'fengFerroelectricityMultiferroicityTwodimensional2020', 'chenFerromagneticNonmagnetic1T2022']
updated: 2026-08-18
---

# 爬坡弹性带 / Climbing Image Nudged Elastic Band (CI-NEB)

爬坡弹性带（CI-NEB）是**用于寻找化学反应或相变过程中最小能量路径（MEP）与鞍点（过渡态）的过渡态搜索方法**。它在弹性带（NEB）方法基础上，让能量最高的镜像沿路径方向"爬坡"精确收敛到鞍点，从而获得可靠的势垒高度，是评估铁电翻转、层间滑移、相变能垒等的标准计算工具。

## 👵 太奶导读

想从山这边的山谷走到山那边的山谷，哪条路最省力？CI-NEB 就是在能量"地形图"上放一串珠子（镜像构型），让它们用弹簧连起来，再让最高处的珠子自己"爬"到山脊顶点。这样就能测出"翻山"到底要花多少力气——对应物理上就是翻转铁电、滑移层间需要跨过的能量壁垒。

## 🧩 CI-NEB 与铁电翻转势垒

- **滑移铁电低势垒**：多层黑磷在 N≥3 时通过非对称层间堆叠产生滑移铁电，不同极化态之间可通过能垒低于 100 meV 的层间滑移相互转换，这类低势垒路径正是过渡态搜索方法（如 NEB/CI-NEB）量化评估的对象（[[../papers/shenEmergenceMultipleFerroelectric2025|Shen 2025]]）。
- **面外极化翻转**：二维铁电 Sc₂P₂Se₆ 单层的面外极化（3.09 μC/cm²）翻转需跨过由层内离子位移决定的势垒，翻转路径的刻画依赖过渡态方法（[[../papers/fengFerroelectricityMultiferroicityTwodimensional2020|Feng 2020]]）。

## 🧩 相变与 CDW 转变路径

- **CDW 态间转换**：TMD 1T′ 相的铁磁与非磁 CDW 态之间可被电荷掺杂驱动发生可逆相变，并产生高达 12.17% 的结构应变，其转变路径与势垒同样可由过渡态搜索方法定量研究（[[../papers/chenFerromagneticNonmagnetic1T2022|Chen 2022]]）。
- **计算一致性**：此类能量路径计算通常与密度泛函理论（DFT）结合，见 [[../concepts/density-functional-theory|密度泛函理论]]。

## 📚 相关论文 (Related Papers)

- [[../papers/chenFerromagneticNonmagnetic1T2022]] — Ferromagnetic and nonmagnetic 1T′ CDW states in TMDs
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]] — Ferroelectricity and multiferroicity in 2D Sc₂P₂Se₆ and ScCrP₂Se₆ monolayers
- [[../papers/shenEmergenceMultipleFerroelectric2025]] — Emergence of multiple ferroelectric states in multilayer black phosphorus

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/nudged-elastic-band|弹性带方法]]：CI-NEB 的基座方法。
- [[../concepts/ferroelectricity|铁电性]]：翻转势垒的评估对象。
- [[../concepts/sliding-ferroelectricity|滑动铁电]]：低势垒层间滑移型铁电。
- [[../concepts/phase-transition|相变]]：能量路径研究的物理背景。
- [[../concepts/charge-density-wave|电荷密度波]]：CDW 态转变的路径研究。
- [[../concepts/density-functional-theory|密度泛函理论]]：势垒计算的底层方法。
- [[../entities/black-phosphorus|黑磷]]：多层滑移铁电研究体系。
- [[../entities/Sc2P2Se6|Sc₂P₂Se₆]]：二维铁电翻转平台。
*（内容由AI生成，仅供参考）*
