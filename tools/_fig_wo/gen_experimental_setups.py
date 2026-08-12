#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate experimental-setups subpages and hub from work order."""
import json, sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

BASE = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki'
FIG_DIR = f'{BASE}/wiki/figures'

with open(f'{BASE}/tools/_fig_wo/experimental-setups.json', encoding='utf-8') as f:
    all_entries = json.load(f)

EXCLUDE = {'Şahin2009probe', 'fornerQuantumTemperatureEffects1993'}
entries = [e for e in all_entries if e['citekey'] not in EXCLUDE]

with open(f'{BASE}/wiki/figures/experimental-setups.md', encoding='utf-8') as f:
    current_page = f.read()

existing_paths = set(re.findall(r'!\[.*?\]\((.*?)\)', current_page))

# ─── Categories ───
GROWTH = {'RecentAdvancesGrowth2025'}
PROBE = {
    'Jin2015studying','Kumar2017microstructuring','guanRecentProgressTwoDimensional2020',
    'hanPolarTopologicalMaterials2025','kimObservationPhaseTransition1997',
    'pedramraziManipulatingTopologicalDomain2019','cossuStackingChargedensityWaves2024',
    'majumdarInterplayChargeDensity2020','tanRevealingEmergentMagnetic2024',
    'Goswami2011multiferroic','Perugu2024morphology',
}
OPTICAL_FIBER = {
    '2019optical','Doroodmand2017conjugated','Tobeiha2025optical','Wang2023ultracompact',
    'XiaokangZhang2013calibrating','Yarai2005optical','duUltrasensitiveOptoelectronicBiosensor2025',
    'Owji20212d','shuTwoDimensionalBlackArsenic2020',
}
SPECTROSCOPY = {
    'Unknown2003charge','Wixtrom2011electrical','Zhang2002b','Zhang2003a',
    'xuTwodimensionalFerroelasticityVan2021','Zhang2019a',
    'martinThinfilmFerroelectricMaterials2016','neumayerCompetingPolarPhases2025',
    'petkovStructureIntercalatedCs2002','wangScreeningEnabledChemiresistiveMoisture2025',
    'songEvidenceSinglelayerVan2022','kresseUltrasoftPseudopotentialsProjector1999c',
    'perdewGeneralizedGradientApproximation1996a','shishkinImplementationPerformanceFrequencydependentGWmethod2006',
    'tangGridbasedBaderAnalysis2009','Nakanishi2009full','Wei2021',
    'zhaoRealization2DMultiferroic2024','cheongMultiferroicsMagneticTwist2007a',
    'naguib25thAnniversaryArticle2013a',
}
DEVICES = {
    'chenHafniumBasedFerroelectricPostMoore2026','xueEmergingNonvolatileMemories2011',
    'sunSlidingFerroelectricityTwodimensional2025','yangStrainEngineeringTwodimensional2021',
    'Unknown2025diffractive',
}

def cat(ck):
    if ck in GROWTH: return 'growth'
    if ck in PROBE: return 'probe'
    if ck in OPTICAL_FIBER: return 'optical'
    if ck in SPECTROSCOPY: return 'spectroscopy'
    if ck in DEVICES: return 'devices'
    return None

new_entries = [e for e in entries if e['path'] not in existing_paths]

# ─── helpers ───
def derive_desc(alt, fn):
    desc = re.sub(r'^图\S+\s*', '', alt).strip()
    if fn.startswith('eq_') or fn.startswith('tab_'):
        desc = alt.strip()
    return desc

def fmt_entry(e, idx):
    fn = e['filename']
    alt_raw = e['alt']
    if fn.startswith('eq_'):
        label, alt = "公式", alt_raw
    elif fn.startswith('tab_'):
        label, alt = "表", alt_raw
    else:
        label = "图"
        alt = alt_raw
        if not alt.startswith('图') and not alt.startswith('ED'):
            alt = f"图{alt}"
    path, citekey = e['path'], e['citekey']
    desc = derive_desc(alt, fn)
    return "\n".join([
        f"### {idx}. {alt}", "", desc, "",
        f"![{label}：{alt}]({path})",
        f"*   **来源**：[[../papers/{citekey}]]", "",
    ])

def count_h3(content):
    return len(re.findall(r'^### \d+\.', content, re.MULTILINE))

# ─── Extract sections using line-based approach ───
lines = current_page.split('\n')

# Find line indices for each H2 section
h2_line_indices = {}
for i, line in enumerate(lines):
    if line.startswith('## '):
        h2_line_indices[line] = i

# Find the boundary sections
formulas_line = None
related_line = None
for line, idx in h2_line_indices.items():
    if '物理公式' in line: formulas_line = (line, idx)
    if '相关概念' in line: related_line = (line, idx)

# Extract section text by line range
def get_section(h2_name):
    start_idx = h2_line_indices.get(h2_name)
    if start_idx is None:
        return ""
    # Find next H2 after this one
    next_idx = None
    for line, idx in sorted(h2_line_indices.items(), key=lambda x: x[1]):
        if idx > start_idx:
            next_idx = idx
            break
    if next_idx is None:
        next_idx = len(lines)
    section_lines = lines[start_idx:next_idx]
    return '\n'.join(section_lines)

growth_existing = get_section('## 🧪 生长、合成与高通量筛选 (Growth, Synthesis & Screening)')
probe_existing = get_section('## 🔬 探针显微与局域电学表征 (Probe Microscopy & Local Characterization)')
spectro_existing = get_section('## 📡 谱学、衍射与宏观表征 (Spectroscopy, Diffraction & Macroscopic Probes)')
devices_existing = get_section('## 🔧 器件制备流程与架构 (Device Fabrication & Architectures)')
formulas_existing = '\n'.join(lines[formulas_line[1]:related_line[1]]) if formulas_line and related_line else ""
related_existing = '\n'.join(lines[related_line[1]:]) if related_line else ""

existing_growth_h3 = count_h3(growth_existing)
existing_probe_h3 = count_h3(probe_existing)
existing_spectro_h3 = count_h3(spectro_existing)
existing_devices_h3 = count_h3(devices_existing)

growth_new = [e for e in new_entries if cat(e['citekey']) == 'growth']
probe_new = [e for e in new_entries if cat(e['citekey']) == 'probe']
optical_new = [e for e in new_entries if cat(e['citekey']) == 'optical']
spectro_new = [e for e in new_entries if cat(e['citekey']) == 'spectroscopy']
dev_new = [e for e in new_entries if cat(e['citekey']) == 'devices']

probe_total = existing_probe_h3 + len(probe_new)
spectro_total = existing_spectro_h3 + len(spectro_new)
devices_total = existing_devices_h3 + len(dev_new)
growth_total = existing_growth_h3 + len(growth_new)
optical_total = len(optical_new)

print(f"Existing H3: growth={existing_growth_h3}, probe={existing_probe_h3}, spectro={existing_spectro_h3}, devices={existing_devices_h3}")
print(f"New: growth={len(growth_new)}, probe={len(probe_new)}, optical={len(optical_new)}, spectro={len(spectro_new)}, devices={len(dev_new)}")
print(f"Subpage totals: growth={growth_total}, probe={probe_total}, spectro={spectro_total}, devices={devices_total}, optical={optical_total}")

# ─── Probe subpage ───
probe_new_content = "\n".join(fmt_entry(e, existing_probe_h3 + 1 + i) for i, e in enumerate(probe_new))
probe_sub = f"""# 探针显微与局域表征 (Probe Microscopy & Local Characterization)

> 收录 PFM、AFM、CAFM、STM、MFM、KPFM 等探针显微表征手段在二维铁电/多铁材料中的成像与应用，包括畴结构可视化、极化翻转动力学、局域电导测绘以及磁性畴的磁光成像。

[[科研Wiki/wiki/figures/experimental-setups|← 返回实验装置索引]]

---

{probe_existing}

{probe_new_content}

---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/scanning-tunneling-microscopy|扫描隧道显微镜 (STM)]]、[[../concepts/ferroelectric-domain-imaging|铁电畴成像]]、[[../concepts/ferroelectric-domain|铁电畴]]、[[../concepts/domain-wall-motion|畴壁运动]]、[[../concepts/flexoelectricity|挠曲电效应]]、[[../concepts/magnetic-optical-imaging|磁光成像]]

**相关材料/实体**：[[../entities/BiFeO3|BiFeO₃]]、[[../entities/NiI2|NiI₂]]、[[../entities/In2Se3|In₂Se₃]]、[[../entities/Cr2S3|Cr₂S₃]]、[[../entities/alpha-Fe2O3|α-Fe₂O₃]]、[[../entities/h-BN|h-BN]]、[[../entities/WTe2|WTe₂]]
"""

# ─── Optical & Fiber subpage ───
optical_new_content = "\n".join(fmt_entry(e, 1 + i) for i, e in enumerate(optical_new))
optical_sub = f"""# 光学、光纤与化学传感 (Optical, Fiber & Chemical Sensing)

> 收录光纤传感器、光学湿度/气体/生物传感器、激光微纳加工（飞秒 TPP）、光电流成像、等离激元耦合等光学表征与传感平台的装置示意、测试数据与性能对比。

[[科研Wiki/wiki/figures/experimental-setups|← 返回实验装置索引]]

---

## 💡 光学与光纤传感 (Optical & Fiber Sensing)

{optical_new_content}

---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/optical-fiber-sensor|光纤传感器]]、[[../concepts/humidity-sensing|湿度传感]]、[[../concepts/evanescent-wave|倏逝波]]、[[../concepts/biosensor|生物传感器]]、[[../concepts/chemiresistor|化学电阻传感器]]、[[../concepts/intensity-modulation|光强调制]]

**相关材料/实体**：[[../entities/polymer-optical-fiber|聚合物光纤]]、[[../entities/graphene-oxide|氧化石墨烯]]、[[../entities/MoS2|MoS₂]]、[[../entities/MoSe2|MoSe₂]]、[[../entities/TiO2-SiO2|TiO₂-SiO₂ 光纤]]、[[../entities/FTO|FTO 导电玻璃]]
"""

# ─── Spectroscopy subpage ───
spectro_new_content = "\n".join(fmt_entry(e, existing_spectro_h3 + 1 + i) for i, e in enumerate(spectro_new))
spectro_sub = f"""# 谱学、衍射与宏观表征 (Spectroscopy, Diffraction & Macroscopic Probes)

> 收录 XRD、TEM、中子衍射、XPS、EPR、磁光成像、太赫兹光谱等宏观谱学与衍射表征手段的实验装置、数据图谱及物理解释，涵盖结构精修、相纯度确认、磁性结构测定与电输运测量等关键环节。

[[科研Wiki/wiki/figures/experimental-setups|← 返回实验装置索引]]

---

{spectro_existing}

{spectro_new_content}

---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/x-ray-diffraction|X 射线衍射 (XRD)]]、[[../concepts/neutron-diffraction|中子衍射]]、[[../concepts/magnetic-optical-imaging|磁光成像]]、[[../concepts/electron-paramagnetic-resonance|电子顺磁共振 (EPR)]]、[[../concepts/density-functional-theory|密度泛函理论 (DFT)]]、[[../concepts/martensitic-transformation|马氏体相变]]、[[../concepts/commensurate-cdw|公度电荷密度波]]

**相关材料/实体**：[[../entities/alpha-Fe2O3|α-Fe₂O₃]]、[[../entities/BaTiO3|BaTiO₃]]、[[../entities/PbTiO3|PbTiO₃]]、[[../entities/PZT|PZT]]、[[../entities/Ti3C2Tx|Ti₃C₂Tₓ MXene]]、[[../entities/black-phosphorus|黑磷]]
"""

# ─── Devices subpage ───
dev_new_content = "\n".join(fmt_entry(e, existing_devices_h3 + 1 + i) for i, e in enumerate(dev_new))
devices_sub = f"""# 器件制备流程与架构 (Device Fabrication & Architectures)

> 收录铁电/多铁材料的器件制备工艺流程、存储器件架构（FeFET、FTJ、FeRAM、STT-RAM）、二维材料异质结堆叠、以及微纳加工（光刻、刻蚀、转移）等器件制造相关的图表。

[[科研Wiki/wiki/figures/experimental-setups|← 返回实验装置索引]]

---

{devices_existing}

{dev_new_content}

---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/nonvolatile-memory|非易失存储]]、[[../concepts/in-memory-computing|存内计算]]、[[../concepts/synaptic-plasticity|突触可塑性]]、[[../concepts/microfabrication|微纳加工]]、[[../concepts/cmos-compatibility|CMOS 兼容性]]

**相关材料/实体**：[[../entities/FeFET|FeFET]]、[[../entities/FeRAM|FeRAM]]、[[../entities/FTJ|铁电隧道结]]、[[../entities/HZO|HZO (铪锆氧)]]、[[../entities/CrI3|CrI₃]]、[[../entities/MoS2|MoS₂]]、[[../entities/Ti3C2Tx|Ti₃C₂Tₓ]]
"""

# ─── Growth subpage ───
growth_new_content = "\n".join(fmt_entry(e, existing_growth_h3 + 1 + i) for i, e in enumerate(growth_new))
growth_sub = f"""# 生长、合成与高通量筛选 (Growth, Synthesis & Screening)

> 收录 CVD、MBE、ALD、CVT 等二维材料生长合成装置示意图、高通量 DFT 筛选流程、以及材料制备方法对比表。重点聚焦铁电/多铁二维范德华材料的可控制备路线。

[[科研Wiki/wiki/figures/experimental-setups|← 返回实验装置索引]]

---

{growth_existing}

{growth_new_content}

---

## 🔗 相关概念与实体 (Related Concepts & Entities)

**核心概念**：[[../concepts/chemical-vapor-deposition|化学气相沉积 (CVD)]]、[[../concepts/high-throughput-screening|高通量筛选]]、[[../concepts/slidetronics|滑移电子学]]、[[../concepts/density-functional-theory|密度泛函理论 (DFT)]]、[[../concepts/exfoliation|机械剥离]]

**相关材料/实体**：[[../entities/Cr2S3|Cr₂S₃]]、[[../entities/In2Se3|In₂Se₃]]、[[../entities/NiI2|NiI₂]]、[[../entities/CuCrP2S6|CuCrP₂S₆]]、[[../entities/h-BN|h-BN]]、[[../entities/MoS2|MoS₂]]
"""

# ─── Hub page ───
hub_content = f"""# 实验测试与测量装置 (Experimental Setups & Measurements)

> 收录二维铁电/多铁材料研究中的生长合成装置、PFM/AFM/CAFM 等探针显微表征平台、THz/XRD/TEM 等谱学与衍射手段，光学与光纤传感器，以及器件制备流程与器件架构相关的图表和关键公式。

[[科研Wiki/wiki/figures/_index|← 返回总索引]]

---

> **📂 子页面导航**：实验装置图像已按主题拆分为 5 个子页面，点击下表快速跳转：
>
> | 子页面 | 主题 | 条目数 |
> |--------|------|--------|
> | [[experimental-setups-growth-synthesis\|🧪 生长、合成与高通量筛选]] | CVD/MBE/ALD 生长、高通量筛选、材料制备方法 | {growth_total} |
> | [[experimental-setups-probe-microscopy\|🔬 探针显微与局域表征]] | PFM/AFM/CAFM/STM/MFM 等纳米尺度成像 | {probe_total} |
> | [[experimental-setups-optical-fiber\|💡 光学、光纤与化学传感]] | 光纤/光学传感器、湿度/生物/气体传感 | {optical_total} |
> | [[experimental-setups-spectroscopy-diffraction\|📡 谱学、衍射与宏观表征]] | XRD/TEM/EPR/磁光等谱学衍射手段 | {spectro_total} |
> | [[experimental-setups-devices-architectures\|🔧 器件制备流程与架构]] | 器件工艺流程、存储器件架构与性能 | {devices_total} |
>
> 物理公式（插层能、形成能、MAE、海森堡模型、挠曲电场等）仍收录于本页 [[#📐 物理公式与模型 (Formulas & Models)]] 一节。

[[科研Wiki/wiki/figures/experimental-setups|← 返回本页]]

---

{formulas_existing}

{related_existing}
"""

# ─── Write files ───
files_written = []
total_new = len(new_entries)

for fname, content in [
    ('experimental-setups.md', hub_content),
    ('experimental-setups-growth-synthesis.md', growth_sub),
    ('experimental-setups-probe-microscopy.md', probe_sub),
    ('experimental-setups-optical-fiber.md', optical_sub),
    ('experimental-setups-spectroscopy-diffraction.md', spectro_sub),
    ('experimental-setups-devices-architectures.md', devices_sub),
]:
    path = f'{FIG_DIR}/{fname}'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    files_written.append(path)
    h3c = count_h3(content)
    print(f"Written: {fname} ({len(content)} chars, {h3c} H3)")

# Clean up stale subpage
stale = f'{FIG_DIR}/experimental-setups-char.md'
if os.path.exists(stale):
    os.remove(stale)
    print(f"Removed stale: {stale}")

print(f"\nTotal new entries added: {total_new}")
print(f"Files written: {len(files_written)}")
