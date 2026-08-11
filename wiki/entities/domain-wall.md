---
tags: [entity, domain-wall, ferroic, topological, sliding-ferroelectricity, strain-engineering]
category: [D02, Z01]
---

# 畴壁 / Domain Wall (DW)

**畴壁** 是分隔不同铁性畴（如极化取向不同的铁电畴、磁化取向不同的铁磁畴、或自发应变不同的铁弹畴）的界面拓扑缺陷。在二维材料及纳米复合体系中，畴壁展现出不同于体相的奇特物理态，是**畴壁电子学 (Domain Wall Electronics)** 的核心研究对象。

## 1. 滑动铁电中的超快动力学
在范德华双层体系（如 [[h-BN]]、[[TMDs]]）中，畴壁性质受层间超低滑移势垒与面内强共价键刚度共同支配 [[../papers/heUltrafastSwitchingDynamics2024]]：
- **超宽畴壁**：由于层间相互作用极弱，双层 h-BN 的畴壁宽度极广，可达 **$10\text{--}40\text{ nm}$**。
    - **0° 壁**：表现为布洛赫型（Bloch-type）极化织构，宽度约 $9.7\text{ nm}$。
    - **90° 壁**：表现为奈尔型（Néel-type）特征，伴随显著的面外屈曲（Buckling），宽度约 $40.7\text{ nm}$。
- **皮秒级开关**：畴壁运动介导的极化翻转场（$\sim 0.026\text{ V/nm}$）比均匀翻转场低两个数量级。在电场驱动下速度可达 **$6000\text{ m/s}$**，翻转时间仅约 $15\text{ ps}$。
- **缺陷钉扎**：氮空位（$V_N$）等点缺陷对畴壁产生约 **$50\text{ meV}$** 的钉扎能，是实验中铁电回滞的微观起源。

## 2. 应变工程调控
应变是精准操纵二维多铁材料（如 $\beta'\text{-In}_2\text{Se}_3$）畴结构的关键自由度 [[../papers/gaoStrainEngineeringFerroelectric2024]]：
- **畴壁构型切换**：应力方向与畴壁线的夹角决定了畴壁的演化。垂直于 180° 畴壁施加 $4\%$ 的拉伸应变可将其转变为 60° 畴壁。
- **势垒消失机制**：应变不仅改变变体稳定性，还能显著降低相变势垒（$2\%$ 应变下势垒趋于零），触发自发的铁电-铁弹相变。

## 3. 金属性界面与拓扑功能
- **导电畴壁**：在某些二维体系中（如 [[BiFeO3]]、[[WTe2]]），畴壁处表现出显著优于畴内的电导率。在 Weyl 半金属 $T_d\text{-MoTe}_2$ 中，极化畴壁处存在高阶拓扑铰链态驱动的增强电导 [[../papers/huangPolarPhaseDomain2019]]。
- **磁电耦合锚点**：在二维多铁金属 [[CrTe2]] 中，铁电畴壁的移动可同步牵引磁畴界，实现“电写磁读”功能 [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]。

## 4. 关键物理模型
- **一维弹性模型**：畴壁宽度 $w \propto \sqrt{\lambda/ \Delta}$，其中 $\lambda$ 为面内刚度，$\Delta$ 为单位长度翻转势垒。范德华材料的低势垒和高刚度共同导致了其巨畴壁特征。
- **挫折与自组装**：几何挫折可诱导铁电涡旋/反涡旋阵列的自发形成，挫折指数 $f \approx 3.1\text{--}4.0$ [[../papers/nahasFrustrationSelfOrderingTopological2016]]。

## 5. 本库相关代表性论文
- [[../papers/heUltrafastSwitchingDynamics2024]]：揭示滑动铁电中的超宽畴壁与皮秒级动力学。
- [[../papers/gaoStrainEngineeringFerroelectric2024]]：论证应变对 $\beta'\text{-In}_2\text{Se}_3$ 畴壁类型的调控规律。
- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：双层 CrTe2 中的多铁畴壁电磁联动。
- [[../papers/nahasFrustrationSelfOrderingTopological2016]]：铁电拓扑缺陷的自组装与挫折效应。

## 6. 关联概念
- [[../concepts/sliding-ferroelectricity|滑动铁电性 Sliding Ferroelectricity]]
- [[../concepts/strain-engineering|应变工程 Strain Engineering]]
- [[../concepts/topological-defects|拓扑缺陷 Topological Defects]]
- [[deep-potential|机器学习势 Deep Potential]]
