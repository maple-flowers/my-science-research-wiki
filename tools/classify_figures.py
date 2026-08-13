#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Classify all figure entries into 9 top-level categories by keyword matching.
Refined v2: better DFT/computational handling, fixed false positives."""
import json, re, sys
from collections import defaultdict, Counter

sys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8', closefd=False)

# 9 top-level categories with keywords (Chinese + English)
# Priority order: mathematical-models > experimental-setups > electronic-devices >
# vibrational-spectra > optical-spectra > electronic-bands > domain-walls >
# heterostructures-stacking > crystal-structures
CATEGORIES = [
    {
        "slug": "mathematical-models",
        "name": "理论模型",
        "keywords": [
            # formulas/equations (theoretical, not data fitting)
            "公式", "方程", "表达式", "解析解", "哈密顿", "hamiltonian",
            "理论模型", "数学模型", "理论框架", "理论计算",
            # computational methods
            "DFT", "第一性原理", "密度泛函", "计算方法", "收敛性",
            "k点", "k网格", "k-space", "布里渊区", "自洽",
            "数值模拟", "分子动力学", "蒙特卡洛", "Monte Carlo",
            "相场", "有限元", "模拟结果", "计算结果",
            "费曼图", "微扰论", "微扰",
            # DFT energy/force results
            "吸附能", "表面能", "总能量", "能量-温度", "能量随",
            "力的收敛", "受力", "Mulliken", "布居",
            "孤子", "soliton", "概率演化",
            # theoretical phase diagrams / models
            "理论相图", "模型计算", "理论预测",
            "EAM势", "对势", "势能",
            "机器学习势", "DP模型", "神经网络势",
            "平均能量", "熔化温度",
            "形核", "过冷度",
        ],
        "exclude": [
            "测量系统框图", "实验装置", "系统示意图",
            "校准曲线",
        ],
    },
    {
        "slug": "experimental-setups",
        "name": "器件与实验装置",
        "keywords": [
            # experimental setups
            "实验装置", "测量系统", "测量装置", "实验系统", "测试系统",
            "系统框图", "系统示意图", "光路图", "光路示意", "表征光路",
            "实验流程", "制备流程", "合成流程", "工艺流程", "实验步骤",
            "装置示意", "装置图", "设备示意",
            "setup", "apparatus",
            # characterization instruments / methods
            "SEM", "TEM", "AFM", "PFM", "XRD", "XPS", "EDS", "EDX",
            "显微镜", "谱仪", "衍射仪",
            "电镜", "扫描电镜", "透射电镜",
            "中子衍射", "FullProf", "精修", "Rietveld",
            # measurement setups
            "测量平台", "测试平台",
            "湿度腔", "真空腔", "反应腔", "腔体",
            "反应釜", "管式炉", "生长装置",
            "3D打印", "打印装置", "光固化",
            "光束相机", "4-f系统", "4f系统",
            # data plots from measurements
            "校准曲线", "对比表", "误差表", "数据表",
            "测量结果对比", "性能对比",
        ],
        "exclude": [],
    },
    {
        "slug": "electronic-devices",
        "name": "器件与实验装置",
        "keywords": [
            "器件", "晶体管", "transistor", "FET", "MOSFET",
            "存储器", "memory", "阻变", "RRAM", "忆阻",
            "传感器", "sensor", "探测器", "detector",
            "二极管", "diode", "LED", "发光二极管",
            "太阳能电池", "solar cell", "电池",
            "电极", "电极结构", "栅极", "源极", "漏极",
            "I-V特性", "I-V 曲线", "I-V曲线", "电流-电压", "输出特性", "转移特性",
            "开关比", "开关特性",
            "电路", "电路图", "等效电路",
            "电容器", "电容结构",
            "湿度传感器", "气体传感器", "压力传感器",
            "存储", "写入", "读取", "擦除",
            "器件结构", "器件示意",
            "灵敏度", "响应时间", "恢复时间",
            "循环伏安", "伏安",
        ],
        "exclude": [],
    },
    {
        "slug": "vibrational-spectra",
        "name": "能带结构与光谱",
        "keywords": [
            "声子", "phonon", "振动模", "vibrational mode",
            "拉曼", "Raman", "红外", "FTIR",
            "振动谱", "声子谱", "拉曼光谱", "红外光谱",
            "振动频率", "振动模式",
            "红外吸收", "拉曼散射", "拉曼峰",
            "极化振动", "光学声子", "声学声子",
            "介电函数", "介电谱",
        ],
        "exclude": [],
    },
    {
        "slug": "optical-spectra",
        "name": "能带结构与光谱",
        "keywords": [
            "吸收光谱", "吸收谱", "absorption", "吸收率",
            "透射光谱", "透射谱", "transmission",
            "反射光谱", "反射谱", "reflectance",
            "发光光谱", "发射光谱", "荧光光谱", "光致发光", "PL",
            "荧光", "磷光", "荧光发射",
            "光吸收", "光发射",
            "SHG", "二次谐波", "倍频",
            "光学常数", "折射率", "消光系数",
            "紫外", "UV", "可见光",
            "激子", "exciton",
            "发光强度", "发光峰",
            "solvatochrom", "溶剂化变色",
            "上转换", "upconversion",
            "圆二色", "CD光谱",
            "椭圆偏振", "椭偏",
            "发光照片", "发光图像",
            "量子产率", "荧光寿命", "衰减曲线", "时间分辨",
            "EPR", "ESR", "电子顺磁共振",
            "衍射光学", "DOE", "全息", "CGH",
            "远场", "光束剖面", "光束 profile",
        ],
        "exclude": [
            "声子", "拉曼", "红外光谱", "介电",
        ],
    },
    {
        "slug": "electronic-bands",
        "name": "能带结构与光谱",
        "keywords": [
            "能带", "band structure", "band structure",
            "态密度", "DOS", "PDOS", "density of states",
            "费米面", "Fermi surface", "费米能级", "Fermi level",
            "费米", "Fermi",
            "ARPES", "角分辨光电子",
            "能带结构", "电子结构", "electronic structure",
            "价带", "导带", "带隙", "band gap", "bandgap",
            "色散曲线", "能带图",
            "电荷密度", "电荷分布", "电子密度",
            "差分电荷密度", "电荷转移",
            "波函数", "轨道", "orbital",
            "自旋", "spin", "磁矩",
            "CDW", "电荷密度波",
            "投影态密度",
            "Fermi contours",
            "自能", "self-energy",
            "磁化率", "susceptibility", "磁电阻", "磁阻",
            "霍尔", "Hall",
            "电阻率", "电阻随温度",
            "超导", "superconduct",
            "BCS",
            "DMFT",
            "HOMO", "LUMO", "能隙",
            "电荷磁化率",
        ],
        "exclude": [],
    },
    {
        "slug": "domain-walls",
        "name": "结构与原子构型",
        "keywords": [
            "畴", "domain", "畴壁", "domain wall",
            "铁电畴", "磁畴", "电畴",
            "极化翻转", "极化分布", "极化方向",
            "畴结构", "畴图",
            "极化-电场", "电滞回线", "P-E回线", "蝴蝶回线",
            "铁电", "ferroelectric",
            "压电", "piezoelectric", "压电响应",
            "翻转", "switching",
        ],
        "exclude": [
            "能带", "态密度",
        ],
    },
    {
        "slug": "heterostructures-stacking",
        "name": "结构与原子构型",
        "keywords": [
            "异质结", "heterostructure", "heterojunction",
            "堆叠", "stacking", "堆垛",
            "范德华", "van der Waals", "vdW", "vdWH",
            "双层", "bilayer", "多层", "multilayer",
            "莫尔", "moiré", "moire", "莫尔条纹",
            "界面", "interface", "界面结构",
            "超晶格", "superlattice",
            "层间", "interlayer",
            "转角", "twist", "扭转角",
            "异质结构", "异质界面",
        ],
        "exclude": [],
    },
    {
        "slug": "crystal-structures",
        "name": "结构与原子构型",
        "keywords": [
            "晶体结构", "crystal structure", "晶格", "lattice",
            "原子结构", "原子排布", "atomic structure", "原子构型",
            "单胞", "unit cell", "原胞",
            "晶面", "crystal plane", "晶向",
            "空间群", "space group",
            "结构示意", "结构图",
            "键长", "键角", "bond length", "bond angle",
            "配位", "coordination",
            "多面体", "polyhedra", "八面体", "四面体",
            "晶体", "crystal",
            "相变", "phase transition", "相图", "phase diagram",
            "结构相变",
            "XRD", "X射线衍射", "衍射图", "衍射峰",
            "晶体取向", "织构",
            "分子结构", "molecular structure",
            "分子构型", "构象", "conformation",
            "晶体形貌", "形貌", "morphology",
            "晶粒", "grain",
            "缺陷", "defect", "空位", "vacancy", "位错", "dislocation",
            "掺杂", "doping", "掺杂位置",
            "球棍模型", "结构模型",
            "投影结构", "俯视图",
            "原子位置", "原子坐标",
            "吸附位置",
            "原子对",
        ],
        "exclude": [],
    },
]


# Manual overrides for entries that keyword matching can't handle
# Key: (paper, alt_substring) -> new_slug
MANUAL_OVERRIDES = {
    # 2019optical: humidity-voltage data plots are sensor performance
    ("2019optical", "图6 剥离长度3 cm"): "electronic-devices",
    # Johannes2008fermi: susceptibility in q-space -> electronic-bands
    ("Johannes2008fermi", "图1 理想 1D Peierls"): "electronic-bands",
    # Wang2023ultracompact: optical beam engineering -> optical-spectra
    ("Wang2023ultracompact", "图4 整体高度误差"): "optical-spectra",
    ("Wang2023ultracompact", "图6 不同m,q偶MG"): "optical-spectra",
    ("Wang2023ultracompact", "图10 螺旋MG"): "optical-spectra",
    # Wu2021: computational conformations table -> mathematical-models
    ("Wu2021", "表1：22个稳定构型"): "mathematical-models",
    # bhowal: polar metal structure -> crystal-structures
    ("bhowalPolarMetalsPrinciples2023b", "图5 几何极性金属"): "crystal-structures",
    # cheong: multiferroics review decorative images -> domain-walls
    ("cheongMultiferroicsMagneticTwist2007a", "文中图27"): "domain-walls",
    ("cheongMultiferroicsMagneticTwist2007a", "题图/版式横幅"): "domain-walls",
    # forner: soliton dynamics -> mathematical-models
    ("fornerQuantumTemperatureEffects1993", "图9 同图8"): "mathematical-models",
    # kresse MD: molecular dynamics results -> mathematical-models
    ("kresseInitiomoleculardynamicsSimulationLiquidmetalamorphoussemiconductor1994", "图4 不同温度下均方位移"): "mathematical-models",
    ("kresseInitiomoleculardynamicsSimulationLiquidmetalamorphoussemiconductor1994", "图9 扩散系数"): "mathematical-models",
    # kresse PAW: computational method table -> mathematical-models
    ("kresseUltrasoftPseudopotentialsProjector1999c", "PAW 数据集"): "mathematical-models",
    # perdew: exchange-correlation formulas -> mathematical-models
    ("perdewGeneralizedGradientApproximation1996a", "eq7"): "mathematical-models",
    ("perdewGeneralizedGradientApproximation1996a", "eq14"): "mathematical-models",
    # shu: NLO material comparison -> optical-spectra
    ("shuTwoDimensionalBlackArsenic2020", "表2 不同 NLO"): "optical-spectra",
    # tan: magnetic charge visualization -> electronic-bands
    ("tanRevealingEmergentMagnetic2024", "图3 反（正）磁场线"): "electronic-bands",
    # xue: memory device performance/architecture -> electronic-devices
    ("xueEmergingNonvolatileMemories2011", "SLC/MLC STT-RAM"): "electronic-devices",
    ("xueEmergingNonvolatileMemories2011", "PCM/DRAM 混合主存"): "electronic-devices",
    # yang: strain engineering method -> experimental-setups
    ("yangStrainEngineeringTwodimensional2021", "图1 柔性基底应变"): "experimental-setups",
    # Sahin: theoretical cross-sections -> mathematical-models
    ("Şahin2009probe", "截面随末态轻子"): "mathematical-models",
    ("Şahin2009probe", "对能量标度"): "mathematical-models",
    ("Şahin2009probe", "表3：相应条件"): "mathematical-models",
    # --- Verified against the papers' own hand-written figure notes ---
    # Doroodmand 图1 is an apparatus schematic (glass chamber, LED, camera,
    # IR source, reference hygrometer) — a setup, not a memory/transistor device.
    ("Doroodmand2017conjugated", "图1 湿度光学传感器装置示意图"): "experimental-setups",
    # Wernet 图1/图2 are O K-edge XAS/XRS absorption spectra, not structures.
    ("wernetSpectroscopicCharacterizationMicroscopic2005", "图1 气相/液面/超临界"): "optical-spectra",
    ("wernetSpectroscopicCharacterizationMicroscopic2005", "图2 超临界水与冰的扩展K边谱"): "optical-spectra",
    # --- Humidity-sensor response data ---
    ("Owji20212d", "RDA-RH核心曲线"): "electronic-devices",
    ("Owji20212d", "方差分析"): "electronic-devices",
    ("Tobeiha2025optical", "图4 暗态下"): "electronic-devices",
    # --- Structural / dielectric parameter tables ---
    ("Perugu2024morphology", "Table 1 structural parameters"): "crystal-structures",
    ("Perugu2024morphology", "Table 2 dielectric parameters"): "electronic-devices",
    # --- Geometry of nanotube rings ---
    ("Wei2021", "直径差与面积比"): "crystal-structures",
    # --- PAW partial-wave construction parameters ---
    ("blochlProjectorAugmentedwaveMethod1994b", "表I PS分波构造参数"): "mathematical-models",
    # --- Strain tensors (formulas) ---
    ("gaoStrainEngineeringFerroelectric2024", "2D应变矩阵形式"): "mathematical-models",
    ("gaoStrainEngineeringFerroelectric2024", "η21转变应变张量"): "mathematical-models",
    ("gaoStrainEngineeringFerroelectric2024", "η31转变应变张量"): "mathematical-models",
    # --- MLIP-predicted Tc / coercive field ---
    ("kaurRecentAdvancesTheoretical2025a", "DREAM/Allegro MLIP"): "mathematical-models",
    # --- Magnetoelectric coupling formulas ---
    ("mostovoyMultiferroicsDifferentRoutes2024", "独立双磁序耦合"): "mathematical-models",
    ("mostovoyMultiferroicsDifferentRoutes2024", "无场螺旋态"): "mathematical-models",
    # --- PBE functional benchmarks ---
    ("perdewGeneralizedGradientApproximation1996a", "图1 增强因子对比"): "mathematical-models",
    ("perdewGeneralizedGradientApproximation1996a", "表I 原子化能"): "mathematical-models",
    # --- MXene etching methods table ---
    ("zahraCriticalAnalysisFerroelectric2025", "表1"): "experimental-setups",
    # --- Exfoliation metric formula ---
    ("zhongHighthroughputExfoliationMultiferroic2025", "Eq.4 两相平均原子位移"): "mathematical-models",
}

# Fix specific misclassifications
MISCLASS_FIXES = {
    # Tobeiha2025optical 图6: optical-humidity coupling data, not electronic-bands
    ("Tobeiha2025optical", "图6 光-湿耦合"): "electronic-devices",
    # RecentAdvancesGrowth2025 图15: applications overview, not mathematical-models
    ("RecentAdvancesGrowth2025", "图15 二维多铁应用"): "electronic-devices",
    # RecentAdvancesGrowth2025 图8: growth + multiferroic, crystal-structures
    ("RecentAdvancesGrowth2025", "图8 PVD生长"): "crystal-structures",
    # Nakanishi2009full 图1 能级图: energy level diagram -> electronic-bands
    ("Nakanishi2009full", "图1 能级图"): "electronic-bands",
    # Nakanishi 图2-4: the paper's own wiki summary states these are 数学模型类
    # (probability formulas, time-domain wavefunctions) — not CDW transport.
    ("Nakanishi2009full", "图2 双光子波函数频谱"): "mathematical-models",
    ("Nakanishi2009full", "图3 时域波函数"): "mathematical-models",
    ("Nakanishi2009full", "图4 概率函数对比"): "mathematical-models",
}


# Audit-driven corrections (from read-only classification audit, ~40 confirmed misclassifications)
# These take precedence over keyword matching.
AUDIT_FIXES = {
    # --- Bader analysis: algorithm/method papers, not band structure ---
    ("tangGridbasedBaderAnalysis2009", "图1 在网法中被限制在网格点上"): "mathematical-models",
    ("tangGridbasedBaderAnalysis2009", "图5 水分子O–H之间Bader分割面"): "mathematical-models",
    ("tangGridbasedBaderAnalysis2009", "图7 水分子旋转45"): "mathematical-models",
    ("tangGridbasedBaderAnalysis2009", "图8 氧原子Bader电荷随分子旋转角"): "mathematical-models",
    # --- PAW method formulas ---
    ("kresseUltrasoftPseudopotentialsProjector1999c", "PAW 线性变换"): "mathematical-models",
    ("kresseUltrasoftPseudopotentialsProjector1999c", "PAW 电荷密度分解"): "mathematical-models",
    # --- Phenomenological magnetoelectric formulas (电极 false positive) ---
    ("mostovoyMultiferroicsDifferentRoutes2024", "Onsager 倒易"): "mathematical-models",
    ("mostovoyMultiferroicsDifferentRoutes2024", "逆 DM 微观键偶极"): "mathematical-models",
    ("mostovoyMultiferroicsDifferentRoutes2024", "Lifshitz 不变量耦合"): "mathematical-models",
    # --- Classical mean-field magnetism theory curves ---
    ("vanvleckSurveyTheoryFerromagnetism1945", "图2 镍在居里点附近放大"): "mathematical-models",
    ("vanvleckSurveyTheoryFerromagnetism1945", "图6 反铁磁体"): "mathematical-models",
    # --- Conceptual models ---
    ("Chen2019superconductivity", "图3 非均匀超导渗流"): "mathematical-models",
    ("fiebigEvolutionMultiferroics2016", "图1 四种多铁性机制"): "mathematical-models",
    ("bhowalPolarMetalsPrinciples2023b", "图1 极性金属"): "mathematical-models",
    ("bhowalPolarMetalsPrinciples2023b", "图4 本征铁电体与赝本征铁电体"): "mathematical-models",
    ("fengFerroelectricityMultiferroicityTwodimensional2020", "图2 Berry 相位法计算的极化"): "mathematical-models",
    # --- Sliding / stacking (not domain walls) ---
    ("bhowalPolarMetalsPrinciples2023b", "图7 铁电金属 WTe"): "heterostructures-stacking",
    ("chenStrongSlidingFerroelectricity2024", "图0 TOC"): "heterostructures-stacking",
    # --- Strain engineering techniques = experimental setups ---
    ("pengStrainEngineering2D2020", "图7 均匀单轴应变加载技术"): "experimental-setups",
    ("pengStrainEngineering2D2020", "图9 非均匀局部应变技术"): "experimental-setups",
    # --- Diffraction / structural characterization = crystal-structures ---
    ("RecentAdvancesGrowth2025", "图12 NiI"): "crystal-structures",
    ("gongAbsenceCriticalThickness2023", "图1 不同厚度 PTO/STO 超晶格"): "crystal-structures",
    ("niuDirectVisualizationLargeScale2021", "图3 双轴倾转电子衍射"): "crystal-structures",
    ("Johannes2008fermi", "图8 Na 原子链弛豫后形成之字形"): "crystal-structures",
    ("Li2013bonding", "表II 六种MX2两方向"): "crystal-structures",
    ("Li2013bonding", "图5 杨氏模量"): "crystal-structures",
    # --- AFM morphology = experimental setups ---
    ("RecentAdvancesGrowth2025", "图14 少层NiI"): "experimental-setups",
    # --- Phonon dispersion = vibrational, not electronic bands ---
    ("lezoualchStudyChargeDensity", "1T-VSe"): "vibrational-spectra",
    # --- Optical spectra wrongly sent to vibrational / crystal ---
    ("gajdosLinearOpticalProperties2006", "介电函数虚部"): "optical-spectra",
    ("shuTwoDimensionalBlackArsenic2020", "图4 开孔 Z 扫描"): "optical-spectra",
    ("shuTwoDimensionalBlackArsenic2020", "表1 不同波长下"): "optical-spectra",
    ("WRZYSZCZYNSKI2010initiators", "图1 双光子辐射吸收机理"): "optical-spectra",
    ("Wang2023ultracompact", "图7 不同m,q偶MG光束实测横向光强"): "optical-spectra",
    ("Wang2023ultracompact", "图8 偶MG光束"): "optical-spectra",
    ("Wang2023ultracompact", "图9 不同m,q螺旋MG光束"): "optical-spectra",
    # --- Memory devices (翻转/堆叠 false positives) ---
    ("xueEmergingNonvolatileMemories2011", "MLC STT-RAM 缓存写能耗"): "electronic-devices",
    ("xueEmergingNonvolatileMemories2011", "3D NUCA"): "electronic-devices",
    # --- Catalysis free-energy diagrams = theory ---
    ("wangTwodimensionalFerroelectricMetal2025", "ORR"): "mathematical-models",
    ("wangTwodimensionalFerroelectricMetal2025", "OER"): "mathematical-models",
    ("zahraCriticalAnalysisFerroelectric2025", "图1"): "mathematical-models",
}


def classify_entry(entry):
    """Classify a single figure entry. Returns (slug, confidence, matched_keywords)."""
    alt = entry.get("alt", "")
    desc = entry.get("desc", "")
    feat = entry.get("feat", "")
    text = f"{alt} {desc} {feat}"
    paper = entry.get("paper", "")

    # Audit fixes have highest precedence
    for (p, substr), slug in AUDIT_FIXES.items():
        if p == paper and substr in alt:
            return slug, 100, [("audit", "fix")]

    # Check manual overrides first
    for (p, substr), slug in MANUAL_OVERRIDES.items():
        if p == paper and substr in alt:
            return slug, 100, [("manual", "override")]

    # Check misclass fixes
    for (p, substr), slug in MISCLASS_FIXES.items():
        if p == paper and substr in alt:
            return slug, 100, [("manual", "fix")]

    results = []
    for cat in CATEGORIES:
        # Check excludes first
        excluded = False
        for ex in cat["exclude"]:
            if ex in text:
                excluded = True
                break
        if excluded:
            continue

        # Count keyword matches (weighted: alt > desc > feat)
        matches = []
        for kw in cat["keywords"]:
            if kw in alt:
                matches.append(("alt", kw))
            elif kw in desc:
                matches.append(("desc", kw))
            elif kw in feat:
                matches.append(("feat", kw))

        if matches:
            # Weight: alt=3, desc=2, feat=1
            score = sum(3 if loc == "alt" else 2 if loc == "desc" else 1 for loc, _ in matches)
            results.append((cat["slug"], score, matches))

    if not results:
        return None, 0, []

    # Sort by score descending
    results.sort(key=lambda x: x[1], reverse=True)
    return results[0][0], results[0][1], results[0][2]


def main():
    with open("tools/figure_entries_full.json", "r", encoding="utf-8") as f:
        entries = json.load(f)

    print(f"Total entries: {len(entries)}")

    # Classify all entries
    distribution = Counter()
    unclassified = []
    classified = []
    changes = []
    no_change = 0

    for entry in entries:
        slug, score, matches = classify_entry(entry)
        entry["new_slug"] = slug
        entry["score"] = score
        entry["matched_keywords"] = [kw for _, kw in matches]

        if slug is None:
            unclassified.append(entry)
        else:
            distribution[slug] += 1
            classified.append(entry)
            if entry.get("current_slug") and entry["current_slug"] != slug:
                changes.append(entry)
            elif entry.get("current_slug") == slug:
                no_change += 1

    print(f"\n=== Classification Distribution ===")
    for slug, count in distribution.most_common():
        print(f"  {slug}: {count}")

    print(f"\n=== Summary ===")
    print(f"  Classified: {len(classified)}")
    print(f"  Unclassified: {len(unclassified)}")
    print(f"  Changed: {len(changes)}")
    print(f"  No change: {no_change}")

    # Show unclassified entries
    print(f"\n=== Unclassified ({len(unclassified)}) ===")
    for e in unclassified:
        print(f"  [{e['paper']}] {e['alt'][:70]}")
        if e.get('desc'):
            print(f"    desc: {e.get('desc', '')[:90]}")

    # Show categories that need splitting (>60)
    print(f"\n=== Categories needing split (>60) ===")
    for slug, count in distribution.most_common():
        if count > 60:
            print(f"  {slug}: {count} entries")

    # Show changes (current vs new)
    print(f"\n=== Classification Changes (first 40) ===")
    for e in changes[:40]:
        print(f"  [{e['paper']}] {e['alt'][:50]}")
        print(f"    {e.get('current_slug', 'None')} -> {e['new_slug']} (kw: {e['matched_keywords'][:3]})")

    # Save classified data
    with open("tools/figure_classified.json", "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    print(f"\nSaved to tools/figure_classified.json")


if __name__ == "__main__":
    main()
