# 剩余极化 / Remanent Polarization

剩余极化（remanent polarization, P_r）指**铁电体在施加电场使极化饱和后、撤去外电场时仍保持的极化值**，即铁电电滞回线（P-E 回线）在 E=0 处的截距。它是铁电性的核心定量指标，直接决定非易失存储（FeRAM、FeFET、FTJ）的读出信号与开关稳定性。P_r 的大小由本征极化、畴结构、缺陷钉扎与材料尺寸共同决定。

## 👵 太奶导读

铁电材料像一块"带电的记忆橡皮泥"：你用电把它"捏"出一个极化方向，撤掉电它还记得——这个"撤电后还记住的极化强度"就是剩余极化 P_r。P_r 越大，"记忆"越牢，存储器读起来越清楚。但如果材料里有杂质"捣乱"（缺陷钉扎），它会"记性变差"，P_r 就小了。

## 🧩 定义与测量

P_r 从**电滞回线**提取：对铁电体施加三角波电场，极化 P 随电场 E 形成回线，回线在 E=0 处的两个交点即 ±P_r。它与 [[../concepts/spontaneous-polarization|自发极化]]（无外场时本征极化 P_s）的区别在于：P_s 是理想单畴值，P_r 是实际测量值，二者之差反映**畴部分翻转、缺陷钉扎与去极化场**的损耗。

## 🔬 材料体系中的 P_r 调控

- **BiFeO₃ 薄膜的外延应变**：厚度梯度研究表明，BiFeO₃ 从高应变四方相（c/a≈1.04）弛豫到近菱形相（c/a≈1.01）时，本征极化仅变化 1.6%，所测 P_r 的微弱变化主要源于极化矢量随 c/a 比的几何旋转——揭示孤对电子铁电对外延应变的本征不敏感性（[[../papers/Kim2008effect|Kim 2008]]）。
- **自支撑 MXene 铁电**：Nb₂CTₓ 薄膜在 1000 Hz 下剩余极化 P_r = 5.12 μC/cm²，为当时自支撑 MXene 最高值，其氧空位与结构畸变同时作为忆阻开关层（[[../papers/tahirFerroelectricityNonvolatileMemristor2025|Tahir 2025]]）。
- **二维滑动铁电**：层间滑移驱动的面外极化体系，其 P_r 与层间电荷转移及翻转机制（逐层翻转、畴壁扭结）密切相关（[[../papers/zhangEmergingFrontiersTwodimensional2025|Zhang 2025]]）。
- **二维多铁异质结**：Fe₃GaTe₂/P(VDF-TrFE) 双栅异质结利用铁电聚合物逆压电效应诱导应变，室温下非易失、全电学调控磁各向异性，极化态作为存储变量（[[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025|Cai 2025]]）。

## ⚡ 翻转动力学与超快开关

P_r 的可靠读出依赖极化翻转的完整性。堆叠工程铁电（如 h-BN 双层）中，基于深度势能机器学习势的大规模模拟表明，畴壁运动可将临界翻转场降低两个数量级、实现**皮秒级翻转**，从而保障回线方度与 P_r 保持（[[../papers/heUltrafastSwitchingDynamics2024|He 2024]]）。二维多铁材料的生长与表征工具箱（CVD/PVD/MBE/ALD + STM/SHG/拉曼/太赫兹）为测量与优化 P_r 提供支撑（[[../papers/RecentAdvancesGrowth2025|Recent advances 2025]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Kim2008effect]] — Effect of epitaxial strain on ferroelectric polarization in multiferroic BiFeO3 films
- [[../papers/tahirFerroelectricityNonvolatileMemristor2025]] — Ferroelectricity and Nonvolatile Memristor Applications of Free‐Standing 2D Niobium Carbide
- [[../papers/zhangEmergingFrontiersTwodimensional2025]] — Emerging frontiers in two-dimensional sliding ferroelectrics
- [[../papers/caiFerroelectricitydrivenStrainmediatedMagnetoelectric2025]] — Ferroelectricity-driven strain-mediated magnetoelectric coupling in two-dimensional multiferroic heterostructure
- [[../papers/heUltrafastSwitchingDynamics2024]] — Ultrafast switching dynamics of the ferroelectric order in stacking-engineered ferroelectrics
- [[../papers/RecentAdvancesGrowth2025]] — Recent advances in growth, characterization, and application of two-dimensional multiferroic materials

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：P_r 是铁电回线的核心定量指标。
- [[../concepts/spontaneous-polarization|自发极化]]：P_r 的理想单畴参考值。
- [[../concepts/hysteresis|迟滞]]：P-E 回线的来源，决定 P_r 与矫顽场。
- [[../concepts/sliding-ferroelectricity|滑动铁电性]]：层间滑移体系的 P_r 与翻转机制。
- [[../concepts/multiferroicity|多铁性]]：极化作为磁电耦合的存储变量。
- [[../concepts/negative-capacitance|负电容]]：铁电 P_r 在低功耗器件中的利用。
- [[../entities/BiFeO3|BiFeO₃]]：室温多铁原型，外延应变下 P_r 行为的研究对象。
- [[../entities/Nb2CTx|Nb₂CTₓ]]：自支撑 MXene 铁电与忆阻应用。
- [[../entities/Fe3GaTe2|Fe₃GaTe₂]]：二维多铁异质结中的磁性层。
*（内容由AI生成，仅供参考）*
