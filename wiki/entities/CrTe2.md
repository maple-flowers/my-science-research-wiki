---
2	tags: [entity, material, multiferroic, TMD, 2D, magnetism, ferroelectricity]
3	category: [D01, Z02]
4	---
5	
6	# 二碲化铬 / Chromium Telluride (CrTe2)
7	
8	**二碲化铬 (CrTe2)** 是一种具有高度调控潜力的范德华（vdW）层状过渡金属硫族化合物（TMD）。它是目前二维凝聚态物理研究的旗舰体系，作为首个被实验证实具有**室温、空气稳定性**的本征二维多铁金属材料，被广泛用于研究磁电耦合的“电写磁读”逻辑 [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]。
9	
10	## 1. 核心物理特性
11	
12	### 1.1 铁电金属佯谬的解决
13	不同于传统铁电体必须是绝缘体以防止极化被自由载流子屏蔽，CrTe2 表现出**面内金属性与面外铁电性**共存：
14	- **空间分离机制**：传导电子主要局域在 MX2 层内平面运动，而极化偶极矩由层间（纵向）不对称电荷分布产生，有效避免了极化屏蔽 [[../papers/zhaoRealization2DMultiferroic2024]]。
15	- **金属性铁电判据**：表现出非易失性的极化翻转迟滞回线，同时具备良好的电荷输运能力。
16	
17	### 1.2 层依赖磁性与室温多铁性
18	CrTe2 的磁基态受层厚和层间耦合强力调制 [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：
19	- **单层 (z-AFM)**：基态为锯齿状反铁磁序（Zigzag-AFM），宏观净磁矩抵消。
20	- **双层 (Multiferroic)**：呈现 **FM/AFM 异质叠加** 结构（顶层 FM，底层 AFM）。产生约 **$2.44\text{ \mu_B/Cr}$** 的净磁矩。
21	- **居里温度 ($T_C$)**：室温稳定，测量值约为 **$300\text{ K}$**。
22	
23	### 1.3 极化机制：层间电荷转移
24	其铁电性起源于 **层间电荷转移 (Interlayer Charge Transfer)** 而非简单的原子滑移：
25	- **驱动力**：FM 层与 z-AFM 层之间存在静电势差（$\sim 0.1\text{ eV}$）。
26	- **极化强度 ($P_{out}$)**：产生约 **$3.0\text{ pC/m}$** 的面外自发极化，显著强于传统滑动铁电体（如 $h\text{-}BN$） [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]。
27	
28	## 2. 磁电耦合应用：电写磁读
29	CrTe2 演示了高集成度的非易失性功能控制：
30	- **全电学控磁**：通过施加外电压（矫顽电压 $1\text{--}2\text{ V}$）翻转铁电极化，可同步改变层间电荷分布，进而诱导 FM/AFM 磁序的可逆切换。
31	- **斯格明子调控**：在 CrTe2 基异质结中，极化翻转可有效调控 Dzyaloshinskii-Moriya 相互作用 (DMI)，实现对**磁斯格明子 (Skyrmions)** 的全电学操控 [[../papers/zhaoRealization2DMultiferroic2024]]。
32	
33	## 3. 主要物性参数
34	| 参数名称 | 典型数值 | 备注 |
35	| :--- | :--- | :--- |
36	| **转变温度 ($T_C$)** | $\sim 300\text{ K}$ | 室温多铁性 |
37	| **面外极化 ($P_{out}$)** | $\sim 3.0\text{ pC/m}$ | 高于滑移铁电机制 |
38	| **磁矩 (Net)** | $2.44\text{ \mu_B/Cr}$ | 双层 FM/AFM 态 |
39	| **环境稳定性** | 空气稳定 | 暴露大气两周仍具活性 |
40	| **材料类别** | 磁性 TMDs | 多铁金属旗舰材料 |
41	
42	## 4. 本库相关代表性论文
43	- [[../papers/tianRoomtemperatureTwodimensionalMultiferroic2026]]：Nature Materials 2026，实验证实室温空气稳定的二维多铁金属。
44	- [[../papers/zhaoRealization2DMultiferroic2024]]：综述了 CrTe2 类材料在插层超晶格与斯格明子控制中的优势。
45	- [[../papers/miaoMagneticFerroelectricMetal2024]]：讨论了 TMDs 中金属性与极性共存的理论边界。
46	
47	## 5. 关联概念与实体
48	- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
49	- [[../concepts/interlayer-charge-transfer|层间电荷转移 Interlayer Charge Transfer]]
50	- [[../entities/WTe2|二碲化钨 WTe2]] (同族铁电金属对比)
51	- [[../entities/MnBi2Te4|MnBi2Te4]] (磁性拓扑对比)
52	- [[../projects/project-2-mn-multiferroics|Project-2]] (磁性调控参考)
53	