---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d1440e82f85676d2b3ce24ffb8efaf05_cd755546988511f1a98a525400f8a581
    ReservedCode1: 6IY2iE475ur31IGYe7yblA3i/tCJocRbjCEh6j2ePezTvmHxXqAsIxQHB4xc1C08Nnpqph6xxCJ6vTB108kDvi7MTLqlywlAx0QzSQ/KyR1Be5Jssf5OF0HC0u0rxLzclFB8Vp5BoAc8u7mSl2dhtq4c84eLF2M2sY3tKZTIfrn8muZJkBigMRx1Wzk=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d1440e82f85676d2b3ce24ffb8efaf05_cd755546988511f1a98a525400f8a581
    ReservedCode2: 6IY2iE475ur31IGYe7yblA3i/tCJocRbjCEh6j2ePezTvmHxXqAsIxQHB4xc1C08Nnpqph6xxCJ6vTB108kDvi7MTLqlywlAx0QzSQ/KyR1Be5Jssf5OF0HC0u0rxLzclFB8Vp5BoAc8u7mSl2dhtq4c84eLF2M2sY3tKZTIfrn8muZJkBigMRx1Wzk=
---

# 科研Wiki 重复名词合并名单

> 扫描范围：`E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\wiki\concepts\`（1289 页，正式 103）与 `wiki\entities\`（500 页，正式 28），含正式页与无 frontmatter 中间产物页。
> 判定标准：语义完全相同的重复名词（大小写变体 / 连字符变体 / 单复数 / 缩写与全称 / 同义词 / 同材料不同写法）。
> 保留 slug 优先选择正式页（有 frontmatter）；无正式页时按命名规范（concepts 全小写 kebab-case，entities 保留大写/化学式）。
> 目录标注：`c/` = concepts，`e/` = entities。

## A. 大小写变体（含跨目录重复）

| 保留 slug | 应合并 slug | 重复原因 |
|---|---|---|
| c/ARPES | c/arpes, e/arpes, e/ARPES | 角分辨光电子能谱，大小写变体且 concepts/entities 双目录各建一页 |
| c/Car-Parrinello | c/car-parrinello, c/car-parrinello-method, e/car-parrinello, e/Car-Parrinello | Car-Parrinello 分子动力学方法，大小写变体 + 跨目录 + 加 method 后缀 |
| c/LAPW | c/lapw, e/lapw, e/LAPW | 线性缀加平面波，大小写变体且跨目录 |
| e/MAX-phase | c/max-phase, c/MAX-phase, e/MAX-phase | MAX 相，大小写变体且跨目录 |
| c/PBE-functional | c/pbe-functional, e/pbe-functional, e/PBE-functional | PBE 泛函，大小写变体且跨目录 |
| e/Sc2CO2 | c/sc2co2, c/Sc2CO2, e/sc2co2 | Sc2CO2 材料，大小写变体且跨目录 |

## B. 连字符 / 去连字符变体

| 保留 slug | 应合并 slug | 重复原因 |
|---|---|---|
| c/pseudogap（正式） | c/pseudo-gap | 赝能隙，pseudo-gap 与 pseudogap 同义 |
| c/optical-band-gap | c/optical-bandgap | 光学带隙，连字符有无变体 |
| e/MoTe2（正式） | e/mo-te2 | 二碲化钼，去连字符+小写变体 |

## C. 单复数变体

| 保留 slug | 应合并 slug | 重复原因 |
|---|---|---|
| c/bessel-beam | c/bessel-beams | 贝塞尔光束，单复数 |
| c/domain-wall | c/domain-walls | 畴壁，单复数 |
| c/skyrmion（正式） | c/skyrmions, c/magnetic-skyrmion | 斯格明子，单复数 + 加 magnetic 前缀同义 |
| c/surface-termination | c/surface-terminations | 表面终止，单复数 |
| c/type-i-multiferroic | c/type-i-multiferroics | 第一类多铁，单复数 |
| c/type-ii-multiferroicity（正式） | c/type-ii-multiferroic, c/type-ii-multiferroics | 第二类多铁，单复数 + 词形变体 |
| c/variable-spring-constant | c/variable-spring-constants | 变弹簧常数，单复数 |
| c/polar-vortex | c/polar-vortices | 极性涡旋，单复数 |
| e/MAX-phase | e/MAX-phases | MAX 相，单复数 |
| e/carbon-nanotube | e/carbon-nanotubes | 碳纳米管，单复数 |

## D. 缩写与全称

| 保留 slug | 应合并 slug | 重复原因 |
|---|---|---|
| c/paw-method（正式） | c/projector-augmented-wave（正式） | 投影增强波法，PAW 缩写与全称，两页均为正式页完全重复 |
| c/ict-mechanism（正式） | c/intramolecular-charge-transfer | 分子内电荷转移，ICT 缩写与全称 |
| c/tict-mechanism（正式） | c/twisted-intramolecular-charge-transfer | 扭曲分子内电荷转移，TICT 缩写与全称 |
| c/aimd | c/ab-initio-molecular-dynamics | 从头算分子动力学，AIMD 缩写与全称 |
| c/dftb | c/dftb-density-functional-tight-binding | 密度泛函紧束缚，DFTB 缩写与全称 |
| c/nudged-elastic-band | c/neb | 爬坡弹性带，NEB 缩写与全称 |
| c/climbing-image-neb | c/cneb | 爬坡镜像 NEB，CI-NEB 缩写与全称 |
| c/generalized-gradient-approximation | c/gga-functional | 广义梯度近似，GGA 缩写与全称 |
| c/DFT-U（正式） | c/dft-plus-u | DFT+U 方法，连字符与加号写法变体 |
| c/vdW-heterostructure | c/van-der-waals-heterostructure | 范德华异质结，vdW 缩写与全称 |
| c/piezoresponse-force-microscopy | c/pfm-piezoresponse-force-microscopy | 压电力显微镜，PFM 前缀冗余 |
| c/pump-probe（正式） | c/pump-probe-technique | 泵浦-探测技术，加 technique 后缀同义 |
| c/quantum-spin-hall-effect（正式） | c/quantum-spin-hall | 量子自旋霍尔效应，加 effect 后缀同义 |
| c/two-photon-absorption-cross-section | c/two-photon-cross-section | 双光子吸收截面，absorption 省略变体 |
| c/bader-analysis | c/bader-charge-analysis | Bader 电荷分析，加 charge 同义 |
| c/mulliken-population | c/mulliken-population-analysis | Mulliken 布居分析，加 analysis 同义 |
| c/self-consistent-field-cycle（正式） | c/self-consistent-field | 自洽场循环，加 cycle 同义 |
| c/landau-lifshitz-equation | c/llg-equation | LLG 方程（Landau-Lifshitz-Gilbert），缩写与全称，高度重叠 |
| c/resistive-switching（正式） | c/resistive-switching-memory | 阻变 / 阻变存储器，同一现象与器件名 |
| c/band-structure | c/electronic-band-structure | 能带结构，加 electronic 同义 |
| c/local-excited-state | c/locally-excited-state | 局域激发态，local/locally 词形变体 |
| c/d-pi-a-architecture | c/d-pi-a-structure, c/donor-acceptor-push-pull, c/donor-pi-acceptor, c/push-pull-chromophore | D-π-A 供体-受体推拉结构，五种写法同义 |
| c/inverse-dzyaloshinskii-moriya | c/inverse-dm-interaction | 逆 DM 相互作用，全称与缩写 |
| c/half-metallicity | c/half-metal | 半金属性 / 半金属，词形变体 |

## E. 同义词 / 同概念不同写法

| 保留 slug | 应合并 slug | 重复原因 |
|---|---|---|
| c/high-order-topology（正式） | c/higher-order-topology | 高阶拓扑，high/higher 词形变体 |
| c/kittel-law | c/kittels-law | Kittel 定律，所有格变体 |
| c/kosterlitz-thouless | c/kosterlitz-thouless-transition | KT 转变，加 transition 同义 |
| c/ginzburg-landau | c/landau-ginzburg | Ginzburg-Landau 理论，人名顺序变体 |
| c/multiferroic-tunnel-junction | c/multiferroic-tunneling-junction | 多铁隧道结，tunnel/tunneling 拼写变体 |
| c/soft-mode | c/soft-mode-phonon, c/soft-phonon-mode | 软模，三种词序/词形变体 |
| c/spin-spiral（正式） | c/spiral-magnetic-order, c/spiral-magnetism, c/spiral-spin-structure | 螺旋磁序，四种写法同义 |
| c/helical-magnetism | c/helical-spin-order | 螺旋磁性，词形变体（与 spin-spiral 组高度相关） |
| c/steepest-ascent | c/steepest-ascent-path | 最陡上升路径，加 path 同义 |
| c/charge-order | c/charge-ordering | 电荷有序，order/ordering 词形变体 |
| c/depolarization-field | c/depolarizing-field | 退极化场，depolarization/depolarizing 词形变体 |
| c/evanescent-field | c/evanescent-wave | 倏逝场/倏逝波，field/wave 同义 |
| c/exciton-condensation | c/excitonic-condensation | 激子凝聚，exciton/excitonic 词形变体 |
| c/first-order-phase-transition | c/first-order-transition | 一级相变，加 phase 同义 |
| c/magnetic-anisotropy（正式） | c/magnetic-anisotropy-energy | 磁各向异性，加 energy 同义 |
| c/peierls-instability（正式） | c/peierls-transition | 派尔斯不稳定性/转变，同一物理现象，高度重叠 |

## F. entities 同材料不同写法

| 保留 slug | 应合并 slug | 重复原因 |
|---|---|---|
| e/Au | e/gold | 金元素，化学符号与英文名 |
| e/Si | e/silicon | 硅元素，化学符号与英文名 |
| e/Ti-sapphire-laser | e/Ti-Sa-laser, e/titanium-sapphire-laser | 钛蓝宝石激光器，三种写法同义 |
| e/TaSe2-xTex | e/tase2-xtex-solid-solution | TaSe2-xTex 固溶体，化学式与描述名 |
| e/MnBi2Te4 | e/mn-bi2-te4-mbt | MnBi2Te4 材料，化学式与描述名 |
| e/CuCrP2S6 | e/cu-crp2s6, e/ccps-cucrp2s6, e/cucrp2s6 | CuCrP2S6 材料，化学式与多种描述名 |
| e/CuInP2S6 | e/cips-cu-in-p2s6 | CuInP2S6 材料，化学式与描述名 |
| e/1T-MoTe2 | e/d1t-mote2 | 1T-MoTe2 材料，相标注写法变体 |
| e/MoS2（正式） | e/molybdenum-disulfide | 二硫化钼，化学式与英文名 |

## 统计

- 共 **69 组**重复名词（A 6 组 + B 3 组 + C 10 组 + D 24 组 + E 17 组 + F 9 组）
- 涉及应合并页面约 **100+ 个**（含跨目录同名页）
- 涉及正式页的重复组：paw-method/projector-augmented-wave（双正式页）、type-ii-multiferroicity、skyrmion、spin-spiral、ict-mechanism、tict-mechanism、pump-probe、quantum-spin-hall-effect、magnetic-anisotropy、resistive-switching、self-consistent-field-cycle、peierls-instability、pseudogap、DFT-U、MoS2、MoTe2 等

## 备注

- 以下候选经语义验证**不重复**，未列入：ict-mechanism/tict-mechanism（ICT 与 TICT 是不同机制）、sliding-ferroelectricity/ferroelectricity、spin-spiral-multiferroics/spin-spiral、type-i-type-ii-multiferroics（不同概念）、ferroelectric-tunnel-junction/multiferroic-tunnel-junction（铁电 vs 多铁隧道结）、stt-ram/mlc-stt-ram（子类关系）、charge-density-wave 系列、exchange 系列、hall-effect 系列、发光系列等。
- 跨目录同名页（如 arpes/ARPES 同时存在于 concepts 与 entities）需在合并时决定归属目录，建议按语义：方法/概念归 concepts，材料/器件归 entities。
*（内容由AI生成，仅供参考）*
