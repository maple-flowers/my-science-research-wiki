---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d1440e82f85676d2b3ce24ffb8efaf05_07a1a002989d11f1a98a525400f8a581
    ReservedCode1: EQm+6plYdGiv+F9TQhw9PdkY/d8YBTHudWkj+RSrxiy9owDYRXXh01qf+C4l3cNySb0FJt7pL1NG4rNw1IIWgZXIN5tGg5VCat9/ssxv5go7Et0lEHeAV139JOlIPr1GUCRbcd0gZSfaF7BEUa0ynKTjeGU8lQpUdCCyMhNJst0s+PPzJt1pbmMtjNY=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d1440e82f85676d2b3ce24ffb8efaf05_07a1a002989d11f1a98a525400f8a581
    ReservedCode2: EQm+6plYdGiv+F9TQhw9PdkY/d8YBTHudWkj+RSrxiy9owDYRXXh01qf+C4l3cNySb0FJt7pL1NG4rNw1IIWgZXIN5tGg5VCat9/ssxv5go7Et0lEHeAV139JOlIPr1GUCRbcd0gZSfaF7BEUa0ynKTjeGU8lQpUdCCyMhNJst0s+PPzJt1pbmMtjNY=
---



# 第一性原理材料设计预测 / First-Principles Material Design

> 科研范式 P01：像"纸上盖楼"一样，先在计算机里把材料"算"出来，验证它稳不稳、有没有想要的性质，再告诉实验家去哪里找。

## 👵 太奶导读

就像盖房子前先画图纸、算承重，第一性原理材料设计就是在计算机里"画"出原子怎么排布，算出这栋"原子楼"稳不稳、有没有电、有没有磁性。算出来稳、又有用，就相当于给实验科学家发了一张"藏宝图"，告诉他们去合成哪种材料、怎么调控它。这套办法不用先买材料、做实验，成本低、试错快，是近二十年材料科学的"预言家"。

## 🧭 范式概述

这个范式的核心逻辑是：**用密度泛函理论（DFT）等第一性原理方法，从原子尺度直接预测材料的结构与性质，形成"预测—验证—调控"的完整链条**。研究对象覆盖二维铁电/多铁/铁弹材料、电荷密度波、磁性金属、超导体等。总体思路是：先构造候选结构并优化，再用声子谱或从头算分子动力学（AIMD）确认动力学稳定性，接着计算目标性质（极化、能垒、磁性、超导转变温度等），最后通过应变、掺杂、层数、堆垛等自由度给出调控预言。这样设计的原因在于：二维材料家族庞大、实验合成成本高，先算后做能大幅缩小搜索空间。例如 [[../papers/dingPredictionIntrinsicTwodimensional2017a]] 系统预测了二维铁电材料家族，[[../papers/chenStrongSlidingFerroelectricity2024]] 预测了滑移铁电并给出 Rashba 自旋纹理，[[../papers/junqueraCriticalThicknessFerroelectricity2003]] 确立了铁电临界厚度这一器件极限。

## 🔁 研究流程

1. **结构建模与优化**：构造候选晶体结构，用 DFT 做几何优化，得到能量最低的原子排布。
2. **稳定性验证**：计算声子谱（无虚频）或跑 AIMD，确认结构在热力学与动力学上稳定。
3. **性质计算**：用 Berry 相位算极化、CI-NEB 算翻转/相变能垒、磁性项算磁矩与磁各向异性、Eliashberg 方程算超导转变温度。
4. **调控预测**：扫描应变、掺杂浓度、层数、堆垛方式等自由度，给出性质随调控参数的变化规律。
5. **器件预言**：将预测性质映射到器件场景（忆阻器、自旋阀、拓扑开关等），为实验提供可验证的判据。

## 🛠️ 核心方法与工具

- **DFT 与泛函**：GGA/PBE、GGA+U、HSE 杂化泛函，处理强关联与带隙问题（[[../papers/aiFerroelectricityCoexistedPorbital2022]]、[[../papers/chen3dLevelSymmetry2025]]）。
- **声子谱 / AIMD**：验证动力学稳定性（[[../papers/liMonolayerPuckeredPentagonal2022]]）。
- **Berry 相位极化**：计算铁电极化（[[../papers/chenStrongSlidingFerroelectricity2024]]）。
- **CI-NEB**：计算相变/翻转能垒（[[../papers/gaoStrainEngineeringFerroelectric2024]]）。
- **蒙特卡洛 / 微磁学**：估算居里温度、模拟斯格明子（[[../papers/wangTunableD0Topological2025b]]）。
- **DFPT + Eliashberg**：预测超导（[[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]）。

## ✅ 适用条件

- 目标体系原子数适中（通常数十至数百原子），DFT 可处理。
- 需要明确的可计算判据（极化、能垒、磁矩、声子稳定性等）。
- 有实验可验证的调控自由度（应变、掺杂、层数、堆垛）。
- 适合"先算后做"的新材料探索，尤其是二维材料家族。

## ⚠️ 局限与风险

- 泛函近似误差：GGA 低估带隙、强关联体系需 +U 或杂化泛函，参数选择影响结论。
- 预测性质与实验合成可行性脱节：算出来稳定不等于能合成出来。
- 忽略温度、缺陷、衬底、环境等真实条件，预测可能与实验偏离。
- 高通量预测结果需实验闭环验证，否则停留在"纸面预言"。

## 📚 代表论文 (Representative Papers)

- [[../papers/dingPredictionIntrinsicTwodimensional2017a]]：系统预测二维铁电材料家族，确立"预测—稳定性—极化—能垒—应用"完整链条。
- [[../papers/chenStrongSlidingFerroelectricity2024]]：预测滑移铁电并揭示 Rashba 自旋纹理，给出器件预言。
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]]：用 DFT 超胞确立铁电临界厚度，是"器件极限"类预测的典范。
- [[../papers/liMonolayerPuckeredPentagonal2022]]：预测新型五边形二维相，展示"新相预测"路线。

## 🗂️ 覆盖论文全集 (All Covered Papers)

- [[../papers/aiFerroelectricityCoexistedPorbital2022]]
- [[../papers/chen3dLevelSymmetry2025]]
- [[../papers/chenFerromagneticNonmagnetic1T2022]]
- [[../papers/chenStrongSlidingFerroelectricity2024]]
- [[../papers/cossuStackingChargedensityWaves2024]]
- [[../papers/dingPredictionIntrinsicTwodimensional2017a]]
- [[../papers/gaoStrainEngineeringFerroelectric2024]]
- [[../papers/hanTunableSlidingFerroelectricity2025]]
- [[../papers/hillWhyAreThere2000a]]
- [[../papers/junqueraCriticalThicknessFerroelectricity2003]]
- [[../papers/khazaeiNovelElectronicMagnetic2013]]
- [[../papers/krishnamurthiSpinChargeDensity2020]]
- [[../papers/lezoualchStudyChargeDensity]]
- [[../papers/Li2013bonding]]
- [[../papers/liFerroelasticityDomainPhysics2016]]
- [[../papers/liMonolayerPuckeredPentagonal2022]]
- [[../papers/miaoMagneticFerroelectricMetal2024]]
- [[../papers/shenEmergenceMultipleFerroelectric2025]]
- [[../papers/tangCombiningIntrinsicSlidinginduced2025]]
- [[../papers/wangTwodimensionalFerroelectricMetal2025]]
- [[../papers/wuNonvolatileSwitchableHalfmetallicity2024]]
- [[../papers/xunCoexistingMagnetismFerroelectric2024]]
- [[../papers/yuFerroelectricControlMagnetism2026]]
- [[../papers/zhengAnisotropicSuperconductivityTwodimensional2025]]
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]
- [[../papers/wangTunableD0Topological2025b]]
- [[../papers/zhangNonvolatileControlTopological2025]]

## 🔗 关联概念、实体与主题 (Related Concepts, Entities & Topics)

- [[../concepts/density-functional-theory|密度泛函理论]]
- [[../concepts/ferroelectricity|铁电性]]
- [[../concepts/multiferroicity|多铁性]]
- [[../concepts/sliding-ferroelectricity|滑移铁电]]
- [[../concepts/strain-engineering|应变工程]]
- [[../concepts/charge-density-wave|电荷密度波]]
- [[../entities/In2Se3|In₂Se₃]]
- [[../topics/材料模拟计算设计|材料模拟计算设计]]
- [[../topics/多铁性材料|多铁性材料]]

## 📈 生命周期日志

- **2026-08-15**: active — 提炼自 27 篇第一性原理材料设计类论文（含铁电/多铁/铁弹/超导/磁性预测）。
*（内容由AI生成，仅供参考）*
