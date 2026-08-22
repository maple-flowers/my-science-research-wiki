# Phase C 第二批身份解析报告（第 51-100 页）

- 仓库：`E:\swan_goose\宝宝\笔记库\sgg\科研Wiki`（分支 `feature/wiki-synthesis-expansion`）
- 范围：`wiki/concepts` 与 `wiki/entities` 按字母序第 51-100 页（起始 `concepts/anisotropic-superconductivity`）
- 模式：只读分析，未修改任何页面，未提交
- 保护集合：与 Phase A/B 一致（concepts 下 dirac-semimetal/exciplex/fluorescence-quantum-yield/pl-quenching/stokes-shift/thermochromism；entities 下 2H-NbSe2/CoFe2O4/Cr2O3/GaSe；tools/audit_wiki_pages.py untracked），本批无并发修改

## 一、每页身份判定表

| # | 路径 | 身份 | 判定依据（一句话） |
|---|------|------|------|
| 51 | concepts/anisotropic-superconductivity | short-aggregation | 有效独立概念（各向异性超导），仅 1 篇论文反链（zheng2025 kagome Cu3(CO)6），无正文 |
| 52 | concepts/anomalous-hall-effect | canonical | developing，完整正文+太奶导读+结构概览+物理机制+关联（berry-curvature/quantum-anomalous-hall-effect 等），4 篇论文 |
| 53 | concepts/antiferroelectricity | short-aggregation | 有效独立概念（反铁电），5 篇论文反链，无正文 |
| 54 | concepts/antiferromagnetism | short-aggregation | 有效独立概念（反铁磁），6 篇论文反链，无正文 |
| 55 | concepts/antiferrotoroidic-order | short-aggregation | 有效独立概念（反铁环矩序），仅 1 篇论文（nahas2016），相关性需核实 |
| 56 | concepts/antiparallel-polarization-stacking | short-aggregation | 有效独立概念（反平行极化堆垛，滑移铁电子概念），仅 1 篇论文（cui2018a In2Se3） |
| 57 | concepts/antivortex | short-aggregation | 有效独立概念（反涡旋，极性拓扑），3 篇论文反链 |
| 58 | entities/AOM | short-aggregation | 具体器件（声光调制器 acousto-optic modulator，TPP 系统激光选通），身份明确，仅 1 篇论文 |
| 59 | entities/AR-N-4340 | short-aggregation | 具体材料（Allresist 负性光刻胶），身份明确，仅 1 篇论文 |
| 60 | entities/ARPES | short-aggregation | 测量技术（角分辨光电子能谱），身份明确，3 篇论文；别名标注含 arpes/ARPES 大小写变体（Windows 下同文件） |
| 61 | concepts/arrhenius-deviation | short-aggregation | 有效独立概念（Arrhenius 偏离），仅 1 篇论文（Mińkowski2021 扩散模拟），相关性需核实 |
| 62 | concepts/aspect-ratio | short-aggregation | 有效独立概念（纵横比），仅 1 篇论文（Kumar2017 TPP），弱相关 |
| 63 | concepts/atmospheric-window | short-aggregation | 有效独立概念（大气窗口，红外探测子概念），仅 1 篇论文（Srinivasan1989） |
| 64 | concepts/atomistic-order-parameter | short-aggregation | 有效独立概念（原子级序参量），仅 1 篇论文（yang2021 rippling ferroic） |
| 65 | entities/Au | short-aggregation | 具体材料（金），身份明确，2 篇论文；别名 gold 指向不存在的页面（悬空） |
| 66 | concepts/augmentation-charge | short-aggregation | 有效独立概念（PAW 增强电荷），2 篇论文（kresse1999 直接相关、tang2025 弱相关） |
| 67 | concepts/augmentation-region | short-aggregation | 有效独立概念（PAW 增强区），仅 1 篇论文（blochl1994） |
| 68 | entities/austenite | short-aggregation | 具体材料相（奥氏体），身份明确，仅 1 篇论文（Zhang2002b 铁素体模拟） |
| 69 | concepts/avalanche-dynamics | short-aggregation | 有效独立概念（雪崩动力学，畴翻转子概念），仅 1 篇论文（yang2021） |
| 70 | concepts/avoided-crossing | short-aggregation | 有效独立概念（避免交叉），仅 1 篇论文（ivanovski1994 Hall 振荡），弱相关 |
| 71 | concepts/axicon | misplaced 候选 | 锥透镜为具体光学器件，按"器件应在 entities"应迁移；论文 frontmatter 归为 concept，存在争议，先标记 |
| 72 | entities/b-AsP | short-aggregation | 具体材料（黑砷磷 black arsenic phosphorus），身份明确，仅 1 篇论文 |
| 73 | entities/BA2PbCl4 | short-aggregation | 具体材料（二维钙钛矿），身份明确，仅 1 篇论文 |
| 74 | entities/Ba3VO4-2 | short-aggregation | 具体材料（Ba3(VO4)2 钒酸钡，slug 为下标转义变体），身份明确，仅 1 篇论文 |
| 75 | concepts/bad-metal | short-aggregation | 有效独立概念（坏金属），仅 1 篇论文（Koley2020 TMD CDW 综述） |
| 76 | concepts/bader-analysis | short-aggregation | 有效独立概念（Bader 电荷分析，DFT 后处理方法），2 篇论文，被 density-functional-theory 引用 |
| 77 | entities/bader-code | short-aggregation | 具体软件（Bader 分析程序），身份明确，仅 1 篇论文；与 concepts/bader-analysis 为方法-软件父子关系 |
| 78 | concepts/bamboo-like-N-CNTs | misplaced | 具体材料/结构（竹节状 N 掺杂碳纳米管），与 entities 版同 slug 跨层碰撞（Phase A 已知），内容几乎相同，应归并至 entities |
| 79 | entities/bamboo-like-N-CNTs | short-aggregation | 具体材料/结构，身份明确，仅 1 篇论文（Wei2021）；为跨层碰撞的规范侧 |
| 80 | concepts/band-alignment | canonical | mature，完整正文+太奶导读+结构概览+三种对齐类型分类+关联（band-offset/schottky-barrier 等），4 篇论文 |
| 81 | concepts/band-bending | short-aggregation | 有效独立概念（能带弯曲），仅 1 篇论文（amini2024 NiI2 多铁），弱相关 |
| 82 | concepts/band-folding | short-aggregation | 有效独立概念（能带折叠），仅 1 篇论文（yanagizawa2023 TiTe2 CDW） |
| 83 | concepts/band-gap | short-aggregation | 有效独立概念（带隙），仅 1 篇论文（Ismail2015 ZnO 湿度传感器综述），弱相关 |
| 84 | concepts/band-offset | canonical | mature，完整正文+太奶导读+结构概览+物理机制与计算+关联（band-alignment/schottky-barrier 等），2 篇论文 |
| 85 | concepts/band-pass-filter | misplaced 候选 | 带通滤波器为具体器件，按"器件应在 entities"应迁移；论文 frontmatter 归为 concept，存在争议，先标记 |
| 86 | concepts/band-structure | short-aggregation | 有效独立概念（能带结构），2 篇论文 |
| 87 | concepts/bandwidth-control | short-aggregation | 有效独立概念（带宽控制），仅 1 篇论文（nakata2021 1T-TaSe2/NbSe2 CDW） |
| 88 | concepts/bandwidth-controlled-mott-transition | short-aggregation | 有效独立概念（带宽控制的 Mott 转变），仅 1 篇论文（nakata2021）；为 bandwidth-control 的子概念 |
| 89 | entities/BAs | short-aggregation | 具体材料（砷化硼 boron arsenide），身份明确，仅 1 篇论文 |
| 90 | entities/BaSrTiO3 | short-aggregation | 具体材料（钛酸锶钡），身份明确，仅 1 篇论文 |
| 91 | entities/BaTiO3 | short-aggregation | 具体材料（钛酸钡，经典铁电材料），身份明确，15 篇论文但无正文/导读/关联，未扩展 |
| 92 | entities/BBO-crystal | short-aggregation | 具体材料（β-BaB2O4 偏硼酸钡晶体），身份明确，仅 1 篇论文 |
| 93 | concepts/bcc-structure | short-aggregation | 有效独立概念（体心立方结构），仅 1 篇论文（Zhang2019a Ti 纳米颗粒 MD） |
| 94 | entities/BCPC | short-aggregation | 具体材料（有机持久机械发光材料），身份明确，仅 1 篇论文（Xie2024） |
| 95 | entities/BCPSO | short-aggregation | 具体材料（有机持久机械发光材料），身份明确，仅 1 篇论文（Xie2024）；与 BCPC 同族 |
| 96 | concepts/beam-shaping | short-aggregation | 有效独立概念（光束整形），2 篇论文 |
| 97 | concepts/bec-bcs-crossover | short-aggregation | 有效独立概念（BEC-BCS 渡越），仅 1 篇论文（Islam2025 TMD 超流密度） |
| 98 | concepts/bedt-ttf | misplaced | BEDT-TTF 为具体分子（有机电荷转移盐给体），按"具体材料应在 entities"应迁移 |
| 99 | concepts/behler-parrinello-nnp | short-aggregation | 有效独立概念（Behler-Parrinello 神经网络势，计算方法），仅 1 篇论文（Mińkowski2021） |
| 100 | concepts/bending-induced-kink | short-aggregation | 有效独立概念（弯曲诱导扭结，滑移铁电子概念），仅 1 篇论文（he2025） |

## 二、类别汇总

| 类别 | 数量 | 页面 |
|------|------|------|
| canonical | 3 | anomalous-hall-effect、band-alignment、band-offset |
| short-aggregation | 43 | 其余身份明确但仅论文列表的页面 |
| alias | 0 | 本批无独立别名页（ARPES 大小写变体在 Windows 下为同一文件） |
| ambiguous | 0 | 本批无歧义词（AOM 在本库上下文中唯一指向声光调制器） |
| misplaced | 3 | concepts/bamboo-like-N-CNTs、concepts/bedt-ttf、concepts/axicon（候选） |
| misplaced 候选 | 2 | concepts/axicon、concepts/band-pass-filter（论文归为 concept，存在争议） |
| no-evidence | 0 | 本批所有页面均有至少 1 篇论文反链 |

注：axicon 与 band-pass-filter 计入 misplaced 候选（2 页），与明确 misplaced 的 bamboo-like-N-CNTs、bedt-ttf 分开统计。若将候选计入 misplaced，则 misplaced 共 4 页。

## 三、问题清单

### 1. 同 slug 跨层碰撞
- **bamboo-like-N-CNTs（concepts + entities）**：Phase A 已知 3 对碰撞之一，本批确认。两页内容几乎相同（同一篇论文 Wei2021，仅论文描述略有差异）。竹节状 N 掺杂碳纳米管为具体材料/结构，规范侧应为 entities；concepts 版为重复/误放，建议 Phase G 归并。
- **无新增碰撞**。

### 2. 规范化名称重复（语义相同名词）
- **bader-analysis（concepts）vs bader-code（entities）**：非重复，为方法-软件合理分层（Bader 分析算法 vs 其软件实现），建议保留父子关系。
- **bandwidth-control vs bandwidth-controlled-mott-transition**：父子关系（后者为前者在 Mott 转变中的特例），非重复。
- **BCPC vs BCPSO**：同族不同材料（同一篇 Xie2024 的两种有机机械发光材料），非重复。
- **arpes / ARPES**：ARPES.md 别名标注含 `arpes`（concepts）、`arpes`（entities）、`ARPES`（entities）；Windows 文件系统不区分大小写，entities/arpes 与 entities/ARPES 为同一物理文件，非真实重复，但别名标注中 `arpes`（concepts）指向不存在的 concepts/arpes 页。

### 3. 缩写/全称与拼写变体
- AOM = acousto-optic modulator（声光调制器），本库唯一含义。
- ARPES = angle-resolved photoemission spectroscopy（角分辨光电子能谱），存在 arpes/ARPES 大小写变体标注。
- AR-N-4340 = Allresist 负性光刻胶（产品名）。
- Au = gold（金），**别名 gold 指向不存在的 entities/gold 页（悬空别名）**。
- BAs = boron arsenide（砷化硼）。
- BBO = beta-barium borate（β-BaB2O4 偏硼酸钡）。
- BEDT-TTF = bis(ethylenedithio)tetrathiafulvalene（bedt-ttf 页）。
- Ba3VO4-2 = Ba3(VO4)2（下标转义变体，slug 中 `-2` 表示下标 2）。
- b-AsP = black arsenic phosphorus（黑砷磷）。
- bcc = body-centered cubic（体心立方）。
- BCPC / BCPSO = 有机机械发光材料缩写（全称待从 Xie2024 核实）。
- bader-code = Bader 分析软件（Henkelman 组 grid-based 算法）。

### 4. 父子概念关系
- bandwidth-controlled-mott-transition ⊂ bandwidth-control
- band-offset ⊂ band-alignment（band-offset 为 band-alignment 的定量参数，两页已互链）
- augmentation-charge ⊂ augmentation-region（PAW 增强区内的增强电荷）
- bader-analysis（方法）↔ bader-code（软件实现）
- antiparallel-polarization-stacking ⊂ sliding-ferroelectricity（反平行极化堆垛）
- bending-induced-kink ⊂ sliding-ferroelectricity（弯曲诱导扭结）
- antivortex ⊂ polar-topological（反涡旋）
- bec-bcs-crossover ⊂ superconductivity（BEC-BCS 渡越）
- avalanche-dynamics ⊂ domain-switching（雪崩动力学）
- avoided-crossing ⊂ band-structure（避免交叉）
- atmospheric-window ⊂ infrared-detection（大气窗口）
- band-pass-filter ⊂ infrared-detection（带通滤波器）
- antiferrotoroidic-order 与 antiferroelectricity / antiferromagnetism 相关（反铁环矩序，独立概念）

### 5. 歧义词
- 本批无明确歧义词。AOM 在本库上下文中唯一指向声光调制器（TPP 系统激光选通器件），身份明确，不标 ambiguous。

### 6. 跨层误放
- **concepts/bedt-ttf**：BEDT-TTF 为具体分子（有机电荷转移盐给体），应在 entities。
- **concepts/bamboo-like-N-CNTs**：具体材料/结构，应在 entities（且与 entities 版重复）。
- **concepts/axicon（候选）**：锥透镜为具体光学器件，应在 entities；但论文 frontmatter 归为 concept，存在争议，先标记待 Phase G 确认。
- **concepts/band-pass-filter（候选）**：带通滤波器为具体器件，应在 entities；论文 frontmatter 归为 concept，存在争议，先标记待 Phase G 确认。

### 7. 无证据页
- 本批无完全无证据页（所有页面均有至少 1 篇论文反链）。

### 8. 论文反链误聚合/弱相关
- **band-gap ← Ismail2015humidity**：弱相关（ZnO 湿度传感器综述，band-gap 非核心主题）。
- **avoided-crossing ← ivanovskiOscillationStructureHall1994**：弱相关（Hall 电流振荡，avoided-crossing 非核心）。
- **band-bending ← aminiAtomicscaleVisualizationMultiferroicity2024**：弱相关（NiI2 多铁，band-bending 非核心）。
- **aspect-ratio ← Kumar2017microstructuring**：弱相关（TPP 论文，aspect-ratio 为通用工艺参数）。
- **augmentation-charge ← tangMultiferroicityTwodimensionalVan2025**：弱相关（多铁论文，augmentation-charge 非核心）。
- **arrhenius-deviation ← Mińkowski2021cation**：需核实（扩散模拟，Arrhenius 偏离是否为核心讨论）。
- **antiferrotoroidic-order ← nahasFrustrationSelfOrderingTopological2016**：需核实（铁电拓扑缺陷，反铁环矩序是否被明确讨论）。

## 四、与第一批对比

- 第一批：canonical 5 / short-aggregation 42 / alias 1 / ambiguous 1 / no-evidence 1。
- 本批：canonical 3 / short-aggregation 43 / misplaced 3（+候选 2）/ alias 0 / ambiguous 0 / no-evidence 0。
- 本批新增 misplaced 类别（bedt-ttf、bamboo-like-N-CNTs concepts 版、axicon/band-pass-filter 候选），为第一批未出现的身份类型。
- 跨层碰撞无新增（bamboo-like-N-CNTs 为 Phase A 已知）。
- 基线数据与 Phase A 一致，本批无新增 broken link / raw 违规链接。

## 五、后续批次提示

- 下一批应从第 101 页开始（按字母序，concepts/entities 合并排序）。
- Phase G 需处理的身份簇：bedt-ttf、bamboo-like-N-CNTs（concepts 版）、axicon、band-pass-filter 的跨层迁移确认。
- 悬空别名：entities/Au 的 `gold` 别名、entities/ARPES 的 `arpes`（concepts）别名，需在别名/消歧阶段修复或删除标注。
