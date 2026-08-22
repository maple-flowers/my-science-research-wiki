---
tags: [concept]
title: 'bessel-beam'
type: concept
status: developing
papers: ['Jia2023polymerization', 'Unknown2025diffractive', 'Wang2023ultracompact']
updated: 2026-08-18
---

# bessel-beam

> [!warning] 本页内容待重写（贡献句部分）
> 本页「相关论文」中部分条目的贡献句为占位或缺失，尚未逐篇核实该论文对本条目的具体贡献。
> 太奶导读与正文可参考。（标记于 2026-08-21）


贝塞尔光束（Bessel beam）是一类具有**无衍射（non-diffracting）**特性的光束，其横向强度分布由第一类贝塞尔函数描述，中心为一个随传播几乎不扩散的亮斑，四周环绕同心圆环。因其自愈（self-healing）与长焦深特性，贝塞尔光束在光镊、超分辨成像、激光加工与双光子聚合等领域具有独特价值；本库中它与飞秒激光双光子聚合（two-photon polymerization）制备微纳光学元件的应用密切相关。

## 👵 太奶导读

太奶啊，普通手电筒的光走远了会散成一大片，贝塞尔光束却像"一根笔直的光柱"，走很远中间还是细细的一根亮线。更神奇的是，就算被挡住一小块，它还能"自我修复"，继续往前传。所以它特别适合做精细的激光加工——在材料里刻出又细又长的结构，比如用双光子聚合做微小的光学零件。

## 🧩 核心内容与机制 (Core Content)

- **无衍射与自愈**：贝塞尔光束是亥姆霍兹方程在柱坐标下的解族，理想贝塞尔束横向轮廓不变；受阻后因平面波分量绕射可重建（自愈）。
- **锥形波前**：可看作具有固定锥角的平面波叠加，常通过轴棱锥（axicon）、衍射光学元件或空间光调制器生成。
- **高阶与变体**：高阶贝塞尔光束携带轨道角动量；马修-高斯（Mathieu-Gauss）等准无衍射光束为其推广（本库 Wang2023 即用相位板生成 Mathieu-Gauss 光束）。
- **应用**：双光子聚合/激光直写、长焦深显微、光镊、材料加工中的光束整形；本库 Jia2023、Unknown2025 涉及用贝塞尔光束进行飞秒双光子聚合加工。
- **工程挑战**：理想无衍射需无限能量，实际为准无衍射（Bessel-Gauss）近似；高数值孔径下的像差校正（如 Jia2023 的像差校正）是实用化的关键。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/two-photon-polymerization|双光子聚合]]：贝塞尔光束在微纳加工中的核心应用场景。
- [[../concepts/two-photon-absorption-cross-section|双光子吸收截面]]：双光子聚合的物理基础。
- [[../concepts/gaussian-beam|高斯光束]]：与贝塞尔束对比的常规光束形态。
- [[../entities/Ti-sapphire-laser|钛宝石激光器]]：飞秒双光子聚合的典型光源。

## 📚 相关论文 (Related Papers)

- [[../papers/Jia2023polymerization]] — Two-photon polymerization of femtosecond high-order Bessel beams with aberration correction
- [[../papers/Unknown2025diffractive]] — Millimeter-Scale Diffractive Optical Elements Fabricated by Two-Photon Polymerization for Beam Shaping in Materials Processing
- [[../papers/Wang2023ultracompact]] — Ultracompact phase plate fabricated by femtosecond laser two-photon polymerization for generation of Mathieu–Gauss beams

## 🏷️ 专业名词别名

- `bessel-beams`（concepts）
