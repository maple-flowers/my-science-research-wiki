---
tags: [concept, ftj, memory, device, tunneling]
category: [D02, Z01]
---

# 铁电隧道结与非挥发存储器 / Ferroelectric Tunnel Junctions (FTJ)

由两层电极中间夹一层超薄铁电势垒层（通常 $< 5\text{ nm}$）构成的金属-铁电-金属（M/FE/M）或二维范德华异质结器件。利用铁电极化方向反转改变势垒高度/形状，从而产生巨大的**隧道开关电阻比 (Giant Electroresistance, GER)**，实现非挥发性信息存储。

## 工作原理与优点

1. **电子隧穿与极化调控**：
   - 当铁电势垒层极化指向一侧时，由于电极不完全屏蔽效应在界面处产生电势降，使平均势垒高度降低（低阻态 LRS）；极化反转后势垒升高（高阻态 HRS）。
2. **二维[[sliding-ferroelectricity|滑动铁电]] FTJ 的优势**：
   - 传统三维氧化物 FTJ 存在临界厚度限制与界面电荷钉扎。
   - 利用原子级厚度的 2D vdW 材料（如 [[../entities/h-BN|h-BN]]、[[../entities/TMDs|3R-MoS₂]]）构成的滑动铁电 FTJ，势垒层无悬挂键、临界厚度降至单/双层，且畴壁高迁移率赋予器件超快写速度与低功耗（[[../../raw/note/2025_Sun_Sliding ferroelectri_KEY-KZZ35845]]、[[../../raw/note/2025_Sun_Sliding ferroelectri_KEY-UJRJMZE9]]）。
3. **神经形态计算与类脑突触应用**：
   - 通过外加脉冲调控畴壁在隧道区域的渐进式移动，FTJ 电导可连续多态调节，模拟生物突触的长期增强（LTP）与长期抑制（LTD）功能。

## 本库相关论文

- [[../../raw/note/2025_Sun_Sliding ferroelectri_KEY-KZZ35845]] / [[../../raw/note/2025_Sun_Sliding ferroelectri_KEY-UJRJMZE9]]：Sliding ferroelectricity in 2D materials and device applications — 详细总结了双层 h-BN、3R-MoS₂ 与 MoS₂/WS₂ 范德华异质结 FTJ 器件。
- [[../../raw/note/2026_Yu_Ferroelectric Contro_KEY-K8QQEGEB]]：Ferroelectric Control of Magnetism and Giant Magnetoresistance — 铁电控制隧道磁阻与巨磁阻效应。
- [[../../raw/note/2011_Xue_Emerging non-volatil_KEY-LCWGFCKH]]：Emerging non-volatile memories — 新型非挥发存储器综述。
- [[../../raw/note/2025_Tahir_Ferroelectricity and_KEY-CHFP8WVB]]：Ferroelectricity and Nonvolatile Memristor Applications — 自由立式薄膜铁电性与非挥发忆阻器应用。

## 关联概念与实体

- [[sliding-ferroelectricity|滑动/堆叠铁电性 Sliding Ferroelectricity]]
- [[polarization-switching|极化翻转 dynamics Polarization Switching]]
- [[2D-materials|二维范德华材料 2D Materials]]
- [[../entities/h-BN|氮化硼 h-BN]]
- [[../entities/TMDs|过渡金属硫化物 TMDs]]
