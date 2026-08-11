---
2	tags: [entity, material, multiferroic]
3	category: [D02, Z01]
4	---
5	
6	# 铋铁氧体 / Bismuth Ferrite (BiFeO3, BFO)
7	
8	**BiFeO3 (BFO)** 是多铁性材料研究领域的“旗舰”材料，也是目前唯一在室温下同时具备强铁电性（$T_C \approx 1103\text{ K}$）和反铁磁性 ($T_N \approx 643\text{ K}$) 的单相材料。由于其高转变温度和显著的磁电耦合效应，BFO 在非易失性存储器、自旋电子器件和多功能传感器中具有巨大的应用潜力。
9	
10	## 1. 结构与多铁性机制
11	BiFeO3 属于典型的 **Type-I 多铁性材料**，其铁电性和磁性起源于不同的子晶格：
12	- **铁电性起源**：由 $Bi^{3+}$ 离子的 $6s^2$ 孤对电子（Lone-pair）驱动的结构畸变产生，极化方向沿伪立方体的 $[111]_c$ 方向，室温极化强度可达 $\sim 100\text{ \mu C/cm^2}$ [[../papers/fiebigEvolutionMultiferroics2016]]。
13	- **磁性起源**：由 $Fe^{3+}$ 离子间的超交换相互作用产生，表现为 G 型反铁磁序。在块体中，受二次非齐次交换作用驱动，会形成波长约 **$62\text{ nm}$** 的[[../concepts/spin-spiral|自旋螺旋调制结构]]（Cycloidal spin structure），这通常会抵消宏观净磁矩 [[../papers/rameshMultiferroicsProgressProspects2007]]。
14	
15	## 2. 尺寸效应与纳米多铁性
16	当材料尺寸减小至纳米尺度时，BFO 展现出与块体显著不同的物理行为 [[../papers/Goswami2011multiferroic]]：
17	- **螺旋序抑制**：当粒径小于 **$62\text{ nm}$** 时，自旋螺旋结构受到抑制，释放出显著的净磁化强度（$\sim 0.4\text{ \mu_B/Fe}$）。
18	- **增强磁电耦合**：实验证实约 **$22\text{ nm}$** 的 BFO 纳米颗粒中仍存在强磁电耦合。极化在 $T_N$ 处出现约 **$30\%$** 的异常跃升，且在 $5\text{ T}$ 磁场下被抑制约 **$7\%$**。
19	- **机制中介**：耦合通过 [[../concepts/dzyaloshinskii-moriya-interaction|DM 相互作用]] 介导，增强的磁有序通过调控[[../concepts/oxygen-octahedron-rotation|氧八面体旋转]]来改变铁电离子的偏心位移。
20	
21	## 3. 应变工程与相竞争
22	在薄膜形态下，外延应变（Epitaxial strain）是调控 BFO 物理特性的重要手段 [[../papers/martinThinfilmFerroelectricMaterials2016]]：
23	- **R-T 相竞争**：施加大的压缩应变可使 BFO 从菱方相（R-like, $c/a \approx 1.01$）转变为“超级四方相”（T-like, $c/a \approx 1.25$）。
24	- **混合相界面**：在特定应变下，R 相和 T 相纳米级共存，形成具有巨大电致形变响应（$\sim 5\%$）的混合相区域，类似于准同型相界（MPB）效应。
25	
26	## 4. 畴壁物理与输运特性
27	BFO 的铁电畴壁展现出与其绝缘块体截然不同的局域导电性：
28	- **导电畴壁**：$71^\circ$ 和 $109^\circ$ 畴壁表现出显著的电导增强。
29	- **磁电调控**：通过交叉场（Cross-field）控制，利用电场翻转铁电极化可带动反铁磁轴旋转，实现“电写磁读” [[../papers/liMagnetoelectricDomainsCrossfield2008a]]。
30	
31	## 5. 二维单层特性 (2D Monolayer Properties)
32	根据 2025 年高通量剥离研究 [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]，BFO 在二维极限下的性能预测如下：
33	- **剥离能 ($E_{exf}$)**：约为 **$0.109\text{ eV/\text{\AA}}^2$**，符合非范德华剥离判据。
34	- **转变温度**：单层 $T_N \approx 280\text{ K}$，接近室温。
35	- **相锁定调控**：在应变驱动下可实现 **$Pc \text{ (AFM)} \to P4mm \text{ (FM)}$** 的相变，伴随带隙从 $3.31\text{ eV}$ 减小至 $0.60\text{ eV}$。
36	
37	## 6. 主要物性参数
38	| 参数名称 | 典型数值 | 备注 |
39	| :--- | :--- | :--- |
40	| **转变温度 ($T_C$)** | $1103\text{ K}$ | 强铁电性 |
41	| **转变温度 ($T_N$)** | $643\text{ K}$ | G 型反铁磁 |
42	| **自发极化 ($P_s$)** | $\sim 100\text{ \mu C/cm}^2$ | 沿 $[111]_c$ 方向 |
43	| **螺旋周期** | $\sim 62\text{ nm}$ | 决定纳米尺寸效应 |
44	| **材料类别** | 钙钛矿氧化物 | [[../projects/project-2-mn-multiferroics|Project-2]] 标杆材料 |
45	
46	## 7. 本库相关代表性论文
47	- [[../papers/zhongHighthroughputExfoliationMultiferroic2025]]：高通量筛选下的二维 BFO 单层性能预测。
48	- [[../papers/Goswami2011multiferroic]]：实验证实纳米尺度 BFO 中的强磁电耦合。
49	- [[../papers/hanPolarTopologicalMaterials2025]]：BFO 体系中的极性拓扑结构综述。
50	- [[../papers/fiebigEvolutionMultiferroics2016]]：多铁性材料发展史与机制综述。
51	- [[../papers/rameshMultiferroicsProgressProspects2007]]：BFO 薄膜与器件应用前景。
52	- [[../papers/martinThinfilmFerroelectricMaterials2016]]：功能氧化物薄膜中的应变工程。
53	
54	## 8. 关联概念与实体
55	- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
56	- [[../concepts/magnetoelectric-coupling|磁电耦合 Magnetoelectric Coupling]]
57	- [[../concepts/spin-spiral|自旋螺旋 Spin Spiral]]
58	- [[../entities/Bi2Fe4O9|Bi2Fe4O9]] (常见杂质相)
59	- [[../entities/LaMnO3|锰酸镧 LaMnO3]] (原型对照)
60	- [[../entities/YMnO3|锰酸钇 YMnO3]] (几何多铁对比)
61	