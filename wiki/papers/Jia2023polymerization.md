---
citekey: Jia2023polymerization
title: "Two-photon polymerization of femtosecond high-order Bessel beams with aberration correction"
authors: [Erse Jia, Chen Xie, Na Xiao, Francois Courvoisier, Minglie Hu]
year: 2023
journal: "Chinese Optics Letters"
doi: "10.3788/COL202321.071203"
url: "https://doi.org/10.3788/COL202321.071203"
paper_type: experiment
status: ingested
year_read: 2026
original_note:: [[../../raw/note/Jia2023polymerization]]
projects: [project-1]
concepts: [two-photon-polymerization, aberration-correction, bessel-beams, high-order-bessel-beams, orbital-angular-momentum, adaptive-optics, wavefront-sensing, optical-vortex, diffraction-free-beam, photopolymerization, self-healing-beam, complex-amplitude-modulation]
entities: [spatial-light-modulator, BBO-crystal, SU-8, CCD-camera, Holoeye-PLUTO, Olympus-20x-objective, ZEISS-Gemini-300, femtosecond-fiber-laser, mechanical-shutter, ND-filter]
methods: [multichannel-interferometric-wavefront-sensing, two-photon-polymerization, scanning-electron-microscopy, angular-spectrum-method, computer-generated-hologram, blazed-grating-diffraction, phase-only-modulation, fourier-spectrum-imaging, circularity-analysis]
materials: [SU-8-2075, cyclopentanone]
figures: [experimental-setups, beam-intensity-profiles, sem-micrographs, circularity-measurement, wavefront-sensing-schematic]
领域基础知识:: >-
  飞秒激光双光子聚合是一种利用超快激光脉冲在光敏材料内部引发双光子吸收，从而实现亚微米级分辨率的三维微纳加工技术。自适应光学通过空间光调制器等可编程器件动态调控光场波前，以生成任意结构光束或补偿像差。光学像差是光学系统中偏离理想成像条件的各种误差，会导致焦点模糊、光场畸变。高阶贝塞尔光束是一种具有环形强度分布和轨道角动量的无衍射光束，对相位畸变极其敏感。
研究背景:: >-
  在飞秒激光双光子聚合系统中，引入自适应光学技术虽然能大幅提升加工效率与灵活性，但系统内光学元件的缺陷、装配误差等因素会引入严重的光学像差，导致加工质量下降。尤其是对于高阶贝塞尔光束这种对相位极其敏感的结构光，像差会使其光场严重扭曲，从而无法制造出高质量的微纳结构。现有像差校正方法多依赖复杂数学工具，应用门槛高。
作者的问题意识:: >-
  如何开发一种简单、鲁棒、无需复杂数学工具和额外硬件，就能在自适应光学双光子聚合系统内部实现原位像差校正的方法，以解决因像差导致的高阶贝塞尔光束光场扭曲及由此引发的微纳结构加工质量劣化问题。
主要研究对象:: >-
  基于单个纯相位空间光调制器的多通道干涉波前传感技术，及其在飞秒高阶贝塞尔光束双光子聚合加工系统中的像差校正效果与最终加工的微管阵列质量。
主要研究方法:: >-
  1. 原理上，将空间光调制器像素阵列划分为多个子通道，通过多通道干涉测量技术，逐一探测各通道相位，重构并补偿系统波前像差。 2. 实验上，将该技术集成到自建的飞秒双光子聚合系统中，有意引入显著像差，通过对比高阶贝塞尔光束校正前后的光场强度分布和最终加工的微管结构的扫描电子显微镜图像及圆形度数据，验证其有效性。
研究意义:: >-
  1. 技术层面：提供了一种极简、低成本、无需额外波前传感器与复杂算法的原位像差校正方案，极大地降低了自适应光学激光加工系统的操作门槛。 2. 应用层面：显著提升了基于高阶贝塞尔光束的双光子聚合加工质量，实现了高均匀性、高圆度微管阵列的快速制造，为高质量微纳加工提供了更普适的工具。
研究结论:: >-
  基于单个纯相位空间光调制器的多通道干涉波前传感技术能够成功集成到双光子聚合系统中，有效测量并补偿超过4π的波前像差。实验证明，该方法能使严重畸变的高阶贝塞尔光束恢复至近乎理想的强度分布，并利用校正后的光束制造出结构完整、壁厚均匀、圆形度高且无倒塌的高质量聚合物微管阵列，其加工质量远优于未校正的情况。
对领域的贡献:: >-
  为激光精密加工领域贡献了一种易于推广的“傻瓜式”像差原位校正方法，桥接了复杂的自适应光学技术与实际的工业应用需求，通过简化系统装调与操作流程，促进了自适应光学在激光加工中的普及。
未来研究方向提及:: >-
  1. 将波前校正范围扩展到整个光学系统，包括物镜与样品界面。 2. 结合实时监测技术（如光学相干断层扫描），实现加工过程中的动态像差补偿。 3. 将该技术拓展至复振幅调制，以实现更精细的结构特征校正。
未来研究方向思考:: >-
  1. 研究该方法在不同类型像差（如社会性高频像差）下的校正精度边界，并与传统模态法进行对比。 2. 探索如何分离并预先补偿空间光调制器自身的固有波前误差，以提高校正的纯粹性。 3. 系统研究像差校正后，该加工系统的极限分辨率与最大纵横比等关键性能指标。 4. 验证该方法对艾里光束、完美涡旋光束等其他复杂结构光场及多焦点并行加工场景的适用性。
tags:
  - paper
  - type/experiment
  - year/2023
  - project/project-1
  - relevance/project-1/strong
  - concept/two-photon-polymerization
  - concept/aberration-correction
  - concept/bessel-beams
  - concept/high-order-bessel-beams
  - concept/orbital-angular-momentum
  - concept/adaptive-optics
  - concept/wavefront-sensing
  - concept/optical-vortex
  - concept/diffraction-free-beam
  - concept/photopolymerization
  - concept/self-healing-beam
  - concept/complex-amplitude-modulation
  - entity/spatial-light-modulator
  - entity/BBO-crystal
  - entity/SU-8
  - entity/CCD-camera
  - entity/Holoeye-PLUTO
  - entity/Olympus-20x-objective
  - entity/ZEISS-Gemini-300
  - entity/femtosecond-fiber-laser
  - method/multichannel-interferometric-wavefront-sensing
  - method/two-photon-polymerization
  - method/scanning-electron-microscopy
  - method/angular-spectrum-method
  - method/computer-generated-hologram
  - method/blazed-grating-diffraction
  - method/phase-only-modulation
  - method/fourier-spectrum-imaging
  - method/circularity-analysis
  - material/SU-8-2075
  - material/cyclopentanone
  - topic/two-photon-polymerization
  - topic/adaptive-optics
  - topic/structured-light
  - topic/femtosecond-laser
  - topic/microfabrication
---

## Jia2023polymerization — 带像差校正的飞秒高阶贝塞尔光束的双光子聚合

## 📄 元数据
Erse Jia、Chen Xie、Na Xiao、Francois Courvoisier、Minglie Hu，2023，Chinese Optics Letters，21(7): 071203，DOI [10.3788/COL202321.071203](https://doi.org/10.3788/COL202321.071203)
## 💡 一句话
用单个纯相位 SLM 将多通道干涉波前传感原位集成到飞秒 2PP 系统中，无需泽尼克/Gerchberg–Saxton 等复杂算法即可补偿超过 4π 的系统像差，使高阶贝塞尔光束（m=6）恢复近理想形态，并快速制造出高圆度、壁厚均匀、无倒塌的 SU-8 微管阵列。

## 🔗 Wiki 双链
  - 年度 [[../write/2023]]
  - 项目 [[../projects/project-1-two-photon]]
  - 相关论文 [[../../raw/note/Jia2023polymerization]]
  - 概念：
    - [[../concepts/two-photon-polymerization|双光子聚合 (2PP)]]
    - [[../concepts/photopolymerization|光聚合]]
    - [[../concepts/bessel-beams|贝塞尔光束]]
    - [[../concepts/diffraction-free-beam|无衍射光束]]
    - [[../concepts/orbital-angular-momentum|轨道角动量 (OAM)]]
    - [[../concepts/adaptive-optics|自适应光学]]
    - [[../concepts/aberration-correction|像差校正]]
    - [[../concepts/wavefront-sensing|波前传感]]
  - 实体：
    - [[../entities/spatial-light-modulator|空间光调制器 (SLM)]]
    - [[../entities/SU-8|SU-8 光刻胶]]
    - [[../entities/BBO-crystal|BBO 倍频晶体]]

## 🆕 新概念/实体建议
  - `figures/beam-intensity-profiles.md` — 结构光纵向/横向强度分布图类型。
  - `figures/sem-micrographs.md` — SEM 微结构照片图类型。

## 📊 关键图表
笔记未附图片（raw/figures/Jia2023polymerization/ 下仅有 manifest.json，figures 列表为空）。论文图 1–6 的内容已在笔记正文（双语转写与 AI 解读）中详述：图1 波前传感原理及校正前后傅里叶谱；图2 实验装置；图3 m=6 高阶贝塞尔光束校正前后纵/横向光强与主瓣尺寸演化；图4 微管 SEM（校正前 a–c、校正后 d–f，比例尺 20 μm）；图5 内外环圆形度；图6 m=4/6/8 贝塞尔光束加工的微管（外径 17.6/20.6/26.06 μm）。

## 🔬 项目连接
  - **project-1（双光固化和双光发光）—— strong（强相关）**：本文虽然在 Zotero 中被归入"01_双光子聚合引发剂"分类，但按内容参考价值判定，它是一篇直接的 2PP 加工光学/工艺论文。对项目一的可复用价值 include：(1) 给出了一套完整的 2PP 加工系统搭建参数（1038 nm→BBO 倍频 518 nm、90 fs、1 MHz、SLM Holoeye PLUTO、Olympus 20×/NA 0.4 物镜、SU-8 2075 工艺参数：1500 r/min 旋涂、65 °C/5 min + 95 °C/10 min 前烘、1.5 mW（1.5 nJ/脉冲）曝光、单管 <0.8 s）；(2) 系统讨论了结构光（贝塞尔/涡旋/自聚焦/axilens）单次曝光替代逐点扫描以提高效率的路线；(3) 提供了一种低门槛的像差原位校正方法，可直接用于项目一中任何基于 SLM 的双光固化装置的装调；(4) 阐明了像差导致能量沉积不均→聚合收缩应力不均→微结构倒塌的机制，对评估固化均匀性有参考意义。它不涉及双光子引发剂分子设计或发光机理，因此不是 core，但作为加工平台与质量控制方法学是 strong。
  - project-2/3/4/5/6/7：无直接连接（无 Mn 多铁、机械发光 NN、TTF 分子计算、SnTe 铁电、湿度传感、CDW 相关内容）。

## 📝 组织与用词
论文按"问题（自适应光学 2PP 中的像差）→ 原理（多通道干涉波前传感，公式 I∝|Ui|²+|Ur|²+2|Ui||Ur|cos(φi−φr)，干涉最强即同相位）→ 装置（含飞秒源、BBO 倍频、SLM、望远镜、CCD）→ 光束校正（傅里叶谱与纵/横光强对比模拟）→ 2PP 加工（SU-8 微管 SEM + 圆形度 C=4πA/P² 量化）→ 不同拓扑荷普适性（m=4/6/8）→ 结论与展望"递进。值得在 wiki 中复用的术语：
  - 双光子聚合 / Two-photon polymerization (2PP)
  - 高阶贝塞尔光束 / high-order Bessel beam
  - 像差校正 / aberration correction
  - 空间光调制器 / spatial light modulator (SLM)
  - 多通道干涉波前传感 / multichannel interferometric wavefront sensing
  - 自适应光学 / adaptive optics
  - 无衍射区 / nondiffracting region
  - 轨道角动量 / orbital angular momentum (OAM)
  - 闪耀光栅相位 / blazed grating phase
  - 圆形度 / circularity (C = 4πA/P²)
  - 复振幅调制 / complex amplitude modulation
  - 光学相干断层扫描 / optical coherence tomography (OCT)

## ✏️ 可写入 Wiki 的要点
  1. 多通道干涉波前传感原理：将纯相位 SLM 像素阵列划分为 M×N（实验用 20×20）通道，每通道加载独立开关的闪耀光栅相位；选一通道作相位参考，其余测试通道相位以 π/10 步长从 0 扫到 2π，CCD 在透镜焦平面记录一级衍射干涉强度；由 I∝|Ui|²+|Ur|²+2|Ui||Ur|cos(φi−φr)，强度最大即 φi=φr，遍历后重构全波前并加载互补相位掩模补偿，无需 Shack–Hartmann 等额外波前传感器，也无需泽尼克多项式或 Gerchberg–Saxton 迭代。
  2. 实验系统参数：自制飞秒光纤放大系统输出 90 fs 变换极限脉冲，中心 1038 nm，1 MHz 重频；BBO 晶体产生 518/519 nm 二次谐波（SH）用于加工；扩束至约 8 mm 照射 Holoeye PLUTO 纯相位 SLM（1920×1080）；由 f=1 m 透镜与 Olympus 20×、NA 0.4 显微物镜组成望远镜把调制光缩到微米尺度；机械快门控制曝光；ND 滤光片调功率；CCD 位于透镜焦平面做波前检测。
  3. 通道数权衡：典型器件像差为低空间频率平滑函数，≥10×10 通道即可充分采样；通道越多波前越精细，但单通道像素过少会使一级衍射干涉光强过弱而无法检测。本文取 20×20 通道、π/10 相位增量。
  4. 故意不做精密对准引入显著像差，检测到跨光束 >4π 的相位起伏；补偿后高阶贝塞尔光束（生成相位 φ(r,θ)=−k sinγ·r + mθ，m=6、γ=4°）的傅里叶谱由扭曲断裂的环恢复为均匀完整圆环，环半径因补偿相位整体会聚性质而略缩。
  5. 校正后光束在实空间的纵向传播剖面恢复笔直无衍射轨迹，z=250 μm 处横向环形强度高度对称，主瓣在无衍射区收敛到约 20 μm 恒定直径，与基于角谱法（angular spectrum method）的理想模拟高度吻合；未校正光束主瓣无法保持无衍射、环数减少。
  6. SU-8 工艺：MicroChem SU-8 2075 用环戊酮稀释（SU-8:环戊酮=5:1），1500 r/min 旋涂于玻璃载玻片；65 °C 5 min + 95 °C 10 min 前烘；SH 光平均功率 ≤1.5 mW @ 1 MHz（单脉冲 1.5 nJ），低重频避免热效应；曝光后硬烘、显影得到高度约 30 μm 的微结构；必须把贝塞尔光束的无衍射区横跨整个光刻胶层以获得良好管形，横向平移+曝光制造阵列，单管平均时间（含移动+曝光）<0.8 s。
  7. 像差对微管质量的影响：未校正光束加工的微管严重变形、倒塌、壁厚不均，外壁出现玻璃基底与管底之间的锥形过渡聚合区；机理是畸变主瓣能量沉积不均导致局部聚合度/交联密度差异，聚合收缩应力分布不均把结构拉弯。校正后阵列整齐、单管完整直立、壁厚均匀，外径约 20.8 μm、壁厚约 4.3 μm，未再观察到倒塌。
  8. 圆形度量化：C=4πA/P²（A 面积，P 周长），越接近 1 越圆。笔记正文给出"校正前/后外环平均圆形度分别为 0.919 和 0.893，内环分别为 0.956 和 0.939"，并指出外环对像差更敏感、改善更显著。注意：按 C 越接近 1 越圆的定义，校正后数值应更高，因此笔记此处的数值顺序疑为转写/AI 解读时前后颠倒（应为校正前 0.893、校正后 0.919 等），引用时需核对原文图 5。
  9. 普适性：用 m=4、6、8 的校正后高阶贝塞尔光束分别加工出外径 17.6、20.6、26.06 μm 的微管，均高圆度、基底附着牢固，证明通过拓扑荷数 m 可灵活调控微管尺寸，方法不依赖特定参数。
  10. 展望与局限：当前仅校正 SLM 到物镜前的像差（受空间所限未把物镜及样品界面纳入，可在物镜后加透镜监测其焦平面信号扩展到全系统）；加工前静态校正，打印过程无实时反馈，未来可结合 OCT 等实时监测形成闭闭环，补偿光刻胶收缩、热效应等动态畸变；可扩展到复振幅调制实现更精细特征；可推广到飞秒激光诱导周期性表面结构（LIPSS）等其他需要良好波前的激光加工场景。
