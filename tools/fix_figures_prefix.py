#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Strip corrupted prefix garbage from wiki/figures subpages and restore H1+intro."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "wiki" / "figures"

# file -> (H1 title, blockquote intro)
HEADERS = {
    "crystal-structures-fundamentals.md": (
        "# 基础晶体结构 (Fundamental Crystal Structures)",
        "> 收录单层与多层晶体几何、堆垛构型、Janus 结构、层间滑移与结构畸变等基础晶体结构图。本页为 [[crystal-structures|晶体结构图库]] 的子页面。",
    ),
    "crystal-structures-computational.md": (
        "# 计算模拟与电子结构 (Computational Modeling & Electronic Structure)",
        "> 收录 DFT/MD 计算模型、吸附构型、电子结构、畴壁动力学与磁性计算等结构图。本页为 [[crystal-structures|晶体结构图库]] 的子页面。",
    ),
    "crystal-structures-phase.md": (
        "# 相变与缺陷结构 (Phase Transitions & Defect Structures)",
        "> 收录结构相图、CDW/超导竞争、熔化凝固、晶粒演化与非晶化等相变与缺陷结构图。本页为 [[crystal-structures|晶体结构图库]] 的子页面。",
    ),
    "crystal-structures-tables.md": (
        "# 数据表格与补充结构 (Data Tables & Supplementary Structures)",
        "> 收录关键数据表格以及溢出的基础晶体结构图。本页为 [[crystal-structures|晶体结构图库]] 的子页面。",
    ),
    "electronic-bands-computational.md": (
        "# 计算能带结构 (Computational Band Structures)",
        "> 本页收录第一性原理（DFT）与模型哈密顿量计算得到的电子能带结构图像，涵盖半金属/半导体的轨道分辨能带、应变与掺杂诱导的带隙调控、磁矩自旋分辨能带等关键结果。这些图像是理解二维范德华材料电子物性的核心证据。本页为 [[electronic-bands|电子能带与电子态]] 的子页面。",
    ),
    "mathematical-models-dft.md": (
        "# 数学模型与物理公式 (Mathematical Models & Formulas)",
        "> 本页为 [[mathematical-models|物理模型与数学公式]] 的子页面：DFT 与电子结构（Kohn-Sham、赝势、交换关联泛函、自洽场）。",
    ),
    "mathematical-models-fe-mf-a.md": (
        "# 数学模型与物理公式 (Mathematical Models & Formulas)",
        "> 本页为 [[mathematical-models|物理模型与数学公式]] 的子页面：铁电/多铁唯象模型与公式（上）。",
    ),
    "mathematical-models-fe-mf-b.md": (
        "# 数学模型与物理公式 (Mathematical Models & Formulas)",
        "> 本页为 [[mathematical-models|物理模型与数学公式]] 的子页面：铁电/多铁唯象模型与公式（中）。",
    ),
    "mathematical-models-cdw.md": (
        "# 数学模型与物理公式 (Mathematical Models & Formulas)",
        "> 本页为 [[mathematical-models|物理模型与数学公式]] 的子页面：电荷密度波、电荷有序模型。",
    ),
    "mathematical-models-hep.md": (
        "# 数学模型与物理公式 (Mathematical Models & Formulas)",
        "> 本页为 [[mathematical-models|物理模型与数学公式]] 的子页面：杂项理论模型与公式。",
    ),
    "mathematical-models-kinetics.md": (
        "# 数学模型与物理公式 (Mathematical Models & Formulas)",
        "> 本页为 [[mathematical-models|物理模型与数学公式]] 的子页面：相场动力学、畴演化、微结构动力学。",
    ),
    "mathematical-models-magnetism.md": (
        "# 数学模型与物理公式 (Mathematical Models & Formulas)",
        "> 本页为 [[mathematical-models|物理模型与数学公式]] 的子页面：海森堡模型、磁各向异性、自旋输运。",
    ),
    "mathematical-models-optics.md": (
        "# 数学模型与物理公式 (Mathematical Models & Formulas)",
        "> 本页为 [[mathematical-models|物理模型与数学公式]] 的子页面：介电函数、光学响应、非线性光学公式。",
    ),
    "mathematical-models-strain-mechanics.md": (
        "# 数学模型与物理公式 (Mathematical Models & Formulas)",
        "> 本页为 [[mathematical-models|物理模型与数学公式]] 的子页面：弹性、挠曲电、应变耦合。",
    ),
    "experimental-setups-devices-architectures.md": (
        "# 器件制备流程与架构 (Device Fabrication & Architectures)",
        "> 收录器件工艺流程、存储器件架构（FeFET/FTJ/FeRAM/STT-RAM）、二维材料异质结堆叠与微纳加工图表。本页为 [[experimental-setups|实验测试与测量装置]] 的子页面。",
    ),
    "experimental-setups-growth-synthesis.md": (
        "# 生长、合成与高通量筛选 (Growth, Synthesis & Screening)",
        "> 收录 CVD/MBE/ALD 等二维材料生长合成装置示意图、高通量 DFT 筛选流程以及材料制备方法对比表，重点聚焦铁电/多铁二维范德华材料的可控制备路线。本页为 [[experimental-setups|实验测试与测量装置]] 的子页面。",
    ),
    "experimental-setups-optical-fiber.md": (
        "# 光学、光纤与化学传感 (Optical, Fiber & Chemical Sensing)",
        "> 收录光纤/光学传感器、湿度/生物/气体传感、激光微纳加工（飞秒 TPP）、光电流成像与等离激元耦合等光学表征与传感平台的装置示意、测试数据与性能对比。本页为 [[experimental-setups|实验测试与测量装置]] 的子页面。",
    ),
    "experimental-setups-probe-microscopy.md": (
        "# 探针显微与局域表征 (Probe Microscopy & Local Characterization)",
        "> 收录 PFM、AFM、CAFM、STM、MFM、KPFM 等探针显微表征手段在二维铁电/多铁材料中的成像与应用，包括畴结构可视化、极化翻转动力学、局域电导测绘以及磁性畴的磁光成像。本页为 [[experimental-setups|实验测试与测量装置]] 的子页面。",
    ),
    "experimental-setups-spectroscopy-diffraction.md": (
        "# 谱学、衍射与宏观表征 (Spectroscopy, Diffraction & Macroscopic Probes)",
        "> 收录 XRD、TEM、EPR、磁光、太赫兹光谱等宏观谱学与衍射表征手段的实验装置、数据图谱及物理解释，涵盖结构精修、相纯度确认、磁性结构测定与电输运测量等关键环节。本页为 [[experimental-setups|实验测试与测量装置]] 的子页面。",
    ),
    "optical-spectra-2d-shg-multiferroic.md": (
        "# 二维材料光学、SHG 与多铁光谱 (2D Materials Optics, SHG & Multiferroic Spectra)",
        "> 收录非线性光学与 Z 扫描、范德华材料光学表征（NiI₂、MnBi₂Te₄、In₂Se₃ 等）、SHG 偏振映射、应变工程光学响应等相关图表。本页为 [[optical-spectra|光学与吸收光谱]] 的子页面。",
    ),
    "optical-spectra-thinfilms-nlo.md": (
        "# 薄膜光谱、第一性原理与器件 (Thin-Film Spectra, ab initio & Devices)",
        "> 收录电荷介电矩阵、SnTe/SnO₂ 薄膜光学带隙、介电函数 ab initio 计算、湿度/磁导率/激光直写等器件光谱图表。本页为 [[optical-spectra|光学与吸收光谱]] 的子页面。",
    ),
}

BACKLINK_RE = re.compile(r".*?(\[\[[^\]]*← 返回[^\]]*\]\])")

for fname, (h1, intro) in HEADERS.items():
    fpath = ROOT / fname
    text = fpath.read_text(encoding="utf-8")
    lines = text.split("\n")
    cut = None
    for i, line in enumerate(lines):
        if "← 返回" in line:
            m = BACKLINK_RE.match(line)
            if m:
                lines[i] = m.group(1)
            cut = i
            break
    if cut is None:
        print(f"SKIP (no backlink): {fname}")
        continue
    body = "\n".join(lines[cut:]).lstrip("\n")
    new_text = f"{h1}\n\n{intro}\n\n{body}"
    fpath.write_text(new_text, encoding="utf-8")
    print(f"FIXED: {fname} (cut {cut} lines)")
