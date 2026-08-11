---
project_id: P06
name: 小花闻的电压湿度传感器
zotero_collection_key: 7Z2S985G
status: 数据处理/Origin绘图阶段
local_path: E:\swan_goose\燕燕\香香\项目六：小花闻的电压湿度传感器\
---

# 项目六：小花闻的电压湿度传感器

> **物理路径**：`E:\swan_goose\燕燕\香香\项目六：小花闻的电压湿度传感器\`  
> **Zotero 文献池**：`科研项目文献池/项目六：小花闻的电压湿度传感器` (`7Z2S985G`)

---

## 1. 项目简介与背景
电压湿度传感器件的实验数据分析与光学带隙计算。采用 Tauc 法处理吸收光谱计算带隙，并利用 Origin-MCP 进行高质量科研绘图。重点关注二维材料在湿度感应过程中的电荷传输机制及其对外部环境（如水分）的响应。

## 2. 与科研 Wiki 知识库的联系
- **相关物理概念**：[[../../concepts/2D-materials|二维传感器件]]、Tauc Plot 带隙分析、库仑屏蔽效应 (Coulombic Screening)、转角电子学 (Twistronics)
- **绘图与工具**：Origin-MCP 数据处理与可视化

## 3. Zotero 参考文献池积累
- [[../../raw/note/wangScreeningEnabledChemiresistiveMoisture2025|Screening-Enabled Chemiresistive Moisture Sensing with Tetrathiafulvalene-Based Electrically Conductive Metal–Organic Frameworks]] (JACS 2025): 揭示了极性水分子通过高介电常数和氢键作用，屏蔽了载流子与电荷平衡阴离子间的库仑引力（屏蔽效应），从而释放被俘获的空穴，大幅提升电导率的本征机制。
- [[../../raw/note/Owji20212d|2D Materials Coated Fiber Optic Humidity Sensor]] (2021): 对比研究了 MoS2、MoSe2 和 G/GO 涂层。MoSe2 在低湿度 (<30% RH) 下表现最佳（空穴被吸附水分子夺取导致折射率降低），而 G/GO 在高湿度 (>80% RH) 下性能最优（载流子浓度增加导致折射率上升）。
- [[../../raw/note/duUltrasensitiveOptoelectronicBiosensor2025|Ultrasensitive optoelectronic biosensor arrays based on twisted bilayer graphene superlattice]] (NSR 2025): 利用 9.4° 扭转双层石墨烯 (tBLG) 的范霍夫奇点 (VHS) 对齐等离激元共振，实现了超灵敏检测。莫尔工程 (Moiré-engineered) 提供的介电常数调控机制为湿度传感的灵敏度提升提供了新思路。
- [[../../raw/note/Perugu2024morphology|Morphology and dielectric properties of doped multiferroics]] (2024): 详细讨论了掺杂多铁性材料中的电荷跳跃传导 (Hopping Conduction) 和介电损耗机制，有助于理解传感器在不同频率下的响应特性。
- [[../../raw/note/Chen2016electrical|Electrical and mechanical switching of ferroelectric polarization in the 70 nm BiFeO3 film]] (Sci. Rep. 2016): 探讨了 BiFeO3 中的电学与力学翻转机制（挠曲电效应），为基于铁电极化调控的湿度响应提供了物理背景。
- [[../../raw/note/xuOpticalFiberHumidity2004|Optical fiber humidity sensor based on evanescent-wave scattering]] (Opt. Lett. 2004): 介绍了基于倏逝波散射的传感机理，是本项目光纤传感架构的基础参考。
- [[../../raw/note/Lv2023humidity|Humidity sensor based on optical fiber Bragg grating with high sensitivity and fast response]]: 高灵敏度光纤光栅湿度传感器研究。
- [[../../raw/note/Shao2022humidity|In-fiber humidity sensor based on Black Phosphorus-Polyvinyl alcohol]]: 基于黑磷-聚乙烯醇的纤维内湿度传感器。

## 4. 知识积累与项目进展记录
- **2026-08-11**: 
    - **文献机制综合分析**：
        - 深入对比了 [[../../raw/note/Owji20212d|Owji et al. (2021)]] 的实验结果。明确了材料极性对湿度响应的决定性作用：G/GO 涂层在 80% RH 以上通过增加载流子密度显著提升灵敏度，适用于高湿环境；而 MoSe2 在低湿段 (<30%) 具有优势，但存在饱和问题。
        - 结合 [[../../raw/note/wangScreeningEnabledChemiresistiveMoisture2025|Wang et al. (2025)]] 的机制，识别出“水分子屏蔽电荷陷阱”是提升传导性的核心本征物理图像，应在数据处理中验证是否存在空穴释放过程。
    - **转角电子学引入**：
        - 关注 [[../../raw/note/duUltrasensitiveOptoelectronicBiosensor2025|Du et al. (2025)]] 关于 tBLG (9.4°) 的研究。计划探讨是否可通过微调二维材料的层间扭转角来优化感应界面的介电常数，从而进一步压低检测限 (LOD)。
    - **多铁性与介电特性**：
        - 参考 [[../../raw/note/Perugu2024morphology|Perugu et al. (2024)]] 关于跳跃传导的模型。本项目传感器在不同频率下的介电常数变化符合 Maxwell-Wagner 极化模型，尤其是 $Zn^{2+}$ 掺杂对电荷俘获的影响需要进一步通过 Origin-MCP 拟合分析。
    - **实验与绘图进展**：
        - 完成 Tauc 法带隙拟合，生成测试图表。后续计划利用 Origin-MCP 对不同湿度下的带隙偏移进行系统绘图，探讨介电常数变化对光学带隙的调制效应（遵循 Penn Model）。
