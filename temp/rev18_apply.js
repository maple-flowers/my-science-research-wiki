const fs = require('fs');
const base = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/wiki/concepts/';

const magnetoOpticalKerr = `---
tags: [concept, magneto-optics, spintronics, solid-state-physics]
title: 磁光克尔效应 / Magneto-Optical Kerr Effect (MOKE)
type: concept
status: mature
domain: [solid-state-physics, magneto-optics, spintronics]
mechanism: 磁性材料反射光的偏振态因磁化强度而改变，反射光偏振旋转角正比于磁化强度
related_concepts: [kerr-effect, faraday-effect, electromagnon, second-harmonic-generation, magnetoelectric-coupling, optical-activity]
papers: [zhaoOpticalFingerprintsTwodimensional2024, gaoGiantChiralMagnetoelectric2024a]
updated: 2026-08
---

# 磁光克尔效应 / Magneto-Optical Kerr Effect (MOKE)

磁光克尔效应（Magneto-Optical Kerr Effect, MOKE）是指线偏振光从磁性材料表面反射时，由于材料磁化强度（或奈尔矢量）的存在，反射光的偏振面发生旋转、且强度变化的磁光现象。它与透射几何下的[[../concepts/faraday-effect|法拉第效应]]互为表里，是探测磁性薄膜、界面与二维磁性材料最常用的光学手段之一。

## 👵 太奶导读

太奶啊，这就好比往一面**“带磁性的镜子”**上照一束光。镜子里的小磁铁（磁矩）会让反射出来的光的**振动方向（偏振面）**被轻轻扭一下。咱们量一量这个扭转角有多大，就能知道镜面附近的小磁铁是朝上还是朝下、劲儿有多大。关键是它**只测表面那层皮**（几十纳米内），所以特别适合看薄膜和单层二维材料里的磁性。

## 🏗️ 物理机制

MOKE 的物理根源是磁化强度 $\mathbf{M}$ 使材料的介电张量产生**反对称的非对角元**：

$$ \varepsilon = \varepsilon_0 \begin{pmatrix} 1 & iQm_z & -iQm_y \\ -iQm_z & 1 & iQm_x \\ iQm_y & -iQm_x & 1 \end{pmatrix} $$

其中 $Q$ 为磁光 Voigt 参数（正比于 $M$），$\hat{m}$ 为磁化方向单位矢量。这一非对角元导致介质对左旋与右旋圆偏振光的折射率不同（磁圆双折射），反射后两分量重新合成的线偏振光偏振面发生旋转，旋转角 $\theta_K$ 一级近似正比于磁化强度：$\theta_K \propto M$。因此 MOKE 本质上是对磁化矢量的**光学线性读出**。

## 🧩 三种几何构型

| 构型 | 磁化方向 | 探测内容 | 典型用途 |
| --- | --- | --- | --- |
| 极向 (Polar) | 垂直于反射面 | 面外磁化分量 | 垂直磁各向异性薄膜、[[../entities/MnBi2Te4\|MnBi2Te4]] 类磁拓扑材料 |
| 纵向 (Longitudinal) | 平行反射面且在入射面内 | 面内磁化、磁滞回线 | 面内各向异性、畴壁运动 |
| 横向 (Transverse) | 平行反射面且垂直入射面 | 反射率（非偏振）变化 | 磁化取向分辨、自旋阀读出 |

## 🔬 在二维多铁与自旋电子学中的应用

*   **光学指纹区分多铁态**：DFT 计算表明，层间滑移多铁体系（如双层 [[../entities/VSe2|VSe2]]）的四个多铁态在克尔旋转信号上遵循严格对称性规则，极性/奈尔矢量翻转会使 $\theta_K$ 变号，构成“电写-光读”的[[../concepts/magnetoelectric-coupling|磁电耦合]]光学指纹 [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]。
*   **时间分辨磁光克尔 (tr-RKerr)**：用飞秒泵浦-探测记录 $\theta_K$ 的瞬态演化，可实时追踪磁化强度非平衡动力学。在 [[../entities/NiI2|NiI2]] 中，tr-RKerr 捕获了[[../concepts/electromagnon|电磁振子]]引起的动态磁化振荡 $\Delta M$，并与探测电极化的时间分辨[[../concepts/second-harmonic-generation|二次谐波]] (tr-SHG) 对比，证实了巨大手性磁电耦合 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。
*   **二维磁性探测**：MOKE 对表面/界面敏感，是[[../entities/CrI3|CrI3]]、[[../entities/FePS3|FePS3]] 等范德华磁体层分辨磁性测量（层数依赖的磁序）的经典手段。

## 🧩 与法拉第效应的区别

| 对比项 | 磁光克尔 (MOKE) | [[../concepts/faraday-effect\|法拉第效应]] |
| --- | --- | --- |
| 几何 | 反射光 | 透射光 |
| 探测深度 | 表面/界面（约几十纳米） | 体相 |
| 对二维材料 | 敏感（单层可测） | 弱（信号被体相稀释） |
| 不可逆性 | 反射路径 | 非互易（往返翻倍） |

## 📚 相关论文 (Related Papers)

- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：证明克尔旋转可作为二维层间滑移多铁态的对称性约束光学指纹。
- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：用时间分辨克尔旋转捕获 NiI2 中电磁振子的动态磁信号。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/kerr-effect|克尔效应]]
- [[../concepts/faraday-effect|法拉第效应]]
- [[../concepts/electromagnon|电磁振子]]
- [[../concepts/second-harmonic-generation|二次谐波产生]]
- [[../concepts/optical-activity|旋光性与光学活性]]
- [[../entities/NiI2|二碘化镍 (NiI2)]]
- [[../entities/VSe2|二硒化钒 (VSe2)]]
`;

const opticalKerr = `---
tags: [concept, nonlinear-optics, solid-state-physics, magneto-optics]
title: 光学克尔效应 / Optical Kerr Effect
type: concept
status: mature
domain: [nonlinear-optics, solid-state-physics]
mechanism: 强光场通过三阶非线性极化使介质折射率瞬时改变，变化量正比于光强
related_concepts: [kerr-effect, second-harmonic-generation, nonlinear-optics, magneto-optical-kerr-effect, faraday-effect]
papers: [zhaoOpticalFingerprintsTwodimensional2024, gajdosLinearOpticalProperties2006]
updated: 2026-08
---

# 光学克尔效应 / Optical Kerr Effect

光学克尔效应（Optical Kerr Effect, OKE，也称交流克尔效应/ac-Kerr 或光致双折射）是[[../concepts/nonlinear-optics|非线性光学]]中的三阶 ($\chi^{(3)}$) 效应：当强光（如飞秒激光脉冲）通过介质时，光场自身诱导介质折射率发生**瞬时改变**，且变化量与光强成正比。它不同于[[../concepts/magneto-optical-kerr-effect|磁光克尔效应]]（磁性介质反射光的偏振旋转），也区别于静态电场下二次电光效应，是超快光学与飞秒光谱的核心机制之一。

## 👵 太奶导读

太奶啊，普通的光照过去，玻璃的“脾气”（折射率）是不变的。但如果光**特别亮**（像打雷一样猛的一道光），它会自己把玻璃的“脾气”给**临时改一下**——光越亮，改得越多。等这道光过去了，玻璃又恢复原样。咱们就利用这个“自己改自己”的特性，来做超快的“光学开关”，还能顺便测出材料对光的响应有多快。

## 🏗️ 物理机制

光学克尔效应的折射率变化为：

$$ n = n_0 + n_2 I $$

其中 $n_0$ 为线性折射率，$I$ 为光强，$n_2$ 为**非线性折射率系数**，与三阶极化率 $\chi^{(3)}$ 直接相关（$n_2 \propto \mathrm{Re}\,\chi^{(3)}$）。由此产生的现象包括：

*   **自聚焦 (Self-focusing)**：高斯光束中心光强高、折射率大，介质等效为会聚透镜，导致光束自聚焦乃至成丝。
*   **自相位调制 (SPM)**：脉冲自身相位被调制，频谱展宽，是超连续谱产生的基础。
*   **光学克尔开关/克尔透镜锁模**：利用瞬时折射率变化实现飞秒级光开关与锁模激光器。
*   **泵浦-探测瞬态双折射**：泵浦光改变探测光的偏振椭圆度/透过率，可时间分辨地追踪载流子、声子与自旋的非平衡弛豫。

## 🧩 与磁光/静态克尔效应的区分

| 类型 | 驱动源 | 响应 | 机制阶数 | 时间尺度 |
| --- | --- | --- | --- | --- |
| 光学克尔 (OKE) | 光场（强光） | $\Delta n \propto I$ | 三阶 $\chi^{(3)}$ | 瞬时（飞秒） |
| [[../concepts/magneto-optical-kerr-effect\|磁光克尔 (MOKE)]] | 磁化强度 $\mathbf{M}$ | $\theta_K \propto M$ | 线性磁光 | 准静态 |
| [[../concepts/kerr-effect\|电光克尔 (二次)]] | 外电场 | $\Delta n \propto E^2$ | 三阶电光 | 准静态 |

## 🔬 在二维材料与磁光研究中的角色

*   在二维层间滑移多铁与磁性材料中，线性磁光响应（含[[../concepts/faraday-effect|法拉第效应]]与 MOKE）是读取磁序的标准探针 [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]；而 OKE 类瞬态非线性响应则可提供与之互补的超快动力学信息。
*   线性光学响应（介电函数、折射率）本身由[[../papers/gajdosLinearOpticalProperties2006|第一性原理线性光学计算]]给出，OKE 的非线性修正量 ($n_2$) 常在强场泵浦实验中被标定，两者结合可完整刻画材料的[[../concepts/optical-activity|光学响应]]。

## 📚 相关论文 (Related Papers)

- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：给出二维多铁材料线性磁光响应（克尔/法拉第）的第一性原理刻画，构成 OKE 研究的线性基线。
- [[../papers/gajdosLinearOpticalProperties2006]]：投影缀加波框架下线性光学性质的 DFT 方法，是计算光学响应（含非线性基线）的基础工具。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/kerr-effect|克尔效应]]
- [[../concepts/magneto-optical-kerr-effect|磁光克尔效应]]
- [[../concepts/second-harmonic-generation|二次谐波产生]]
- [[../concepts/nonlinear-optics|非线性光学]]
- [[../concepts/faraday-effect|法拉第效应]]
- [[../concepts/optical-activity|旋光性与光学活性]]
`;

const jointMeasure = `---
tags: [concept, magneto-optics, multiferroicity, magnetoelectric-coupling, nonlinear-optics]
title: 磁光-电联合测量 / Joint Magneto-Optical and Electric Measurement
type: concept
status: mature
domain: [solid-state-physics, magneto-optics, multiferroicity]
mechanism: 将磁光探针（tr-RKerr/法拉第/RMCD）与电学或极化探针（tr-SHG/压电/光电导）在时间或空间上协同探测，解耦磁序与电极化响应
related_concepts: [magneto-optical-kerr-effect, faraday-effect, second-harmonic-generation, electromagnon, magnetoelectric-coupling, polarization-switching]
papers: [gaoGiantChiralMagnetoelectric2024a, wuCoexistenceFerroelectricityAntiferroelectricity2024]
updated: 2026-08
---

# 磁光-电联合测量 / Joint Magneto-Optical and Electric Measurement

磁光-电联合测量（Joint Magneto-Optical and Electric Measurement）指在同一材料体系上，将**磁光探针**（如时间分辨磁光克尔 tr-RKerr、[[../concepts/faraday-effect|法拉第效应]]、反射磁圆二色 RMCD）与**电学/极化探针**（如时间分辨[[../concepts/second-harmonic-generation|二次谐波]] tr-SHG、压电力显微镜、光电导）协同或同时测量，从而在时域或实空间解耦磁性（$\mathbf{M}$）与电极化（$\mathbf{P}$）两类自由度的响应。它对多铁性、手性[[../concepts/magnetoelectric-coupling|磁电耦合]]与非共线磁结构的判定尤为关键。

## 👵 太奶导读

太奶啊，一种材料里既藏着“磁”又藏着“电”，它们还互相牵着对方。光用一个探针看不清楚——看“磁”的探针会被“电”干扰，看“电”的又分不清“磁”。所以咱们**同时上两把尺子**：一把专门量“磁”（看反射光的偏振），一把专门量“电”（看二次谐波），把两个信号一比，就能分清谁是谁、谁拉着谁了。

## 🏗️ 方法框架

*   **磁学通道（磁光探针）**：[[../concepts/magneto-optical-kerr-effect|磁光克尔]]/法拉第旋转、RMCD 对磁化强度（或奈尔矢量）敏感，给出 $\Delta M$ 的时域演化。
*   **电学通道（极化探针）**：tr-SHG 对电极化敏感（偶极贡献随极化符号反转），给出 $\Delta P$；光电导/介电响应则给出电荷动力学。
*   **联合判据**：两通道信号存在特定相位差、或对温度/偏置场的依赖不同，即可判定磁电耦合的存在性、手性与相对强度。若 $\Delta M$ 与 $\Delta P$ 以相同频率振荡但相位错开，说明存在由电磁振子中介的动力学磁电耦合。

## 🔬 典型实例

*   **NiI2 中的手性磁电振荡**：在范德华多铁 [[../entities/NiI2|NiI2]] 中，研究者将 tr-RKerr 与 tr-SHG 在同一飞秒实验上联合测量，发现磁化强度与电极化以相同频率振荡且相位差显著，从而证实巨大手性磁电耦合与[[../concepts/electromagnon|电磁振子]]的相干激发 [[../papers/gaoGiantChiralMagnetoelectric2024a]]。
*   **二维多铁磁电序区分**：对层间滑移/多铁体系，联合使用线性磁光（克尔/法拉第）指纹与二次谐波指纹，可将四个多铁态（极性 × 奈尔矢量组合）逐一分辨，实现“电写-光读”的完整表征链。
*   **非共线磁序与铁电序共存**：在三层 NiI2 器件中，RMCD 观测到非共线反铁磁序及拓扑“半子对”磁畴，与铁电/反铁电共存行为相关联 [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]，体现了磁光通道与电学通道在实空间成像上的互补性。

## 📚 相关论文 (Related Papers)

- [[../papers/gaoGiantChiralMagnetoelectric2024a]]：tr-RKerr 与 tr-SHG 联合测量，证实 NiI2 中的巨大手性磁电振荡。
- [[../papers/wuCoexistenceFerroelectricityAntiferroelectricity2024]]：二维范德华多铁中铁电与反铁电共存，结合磁光观测非共线磁序。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/magneto-optical-kerr-effect|磁光克尔效应]]
- [[../concepts/faraday-effect|法拉第效应]]
- [[../concepts/second-harmonic-generation|二次谐波产生]]
- [[../concepts/electromagnon|电磁振子]]
- [[../concepts/magnetoelectric-coupling|磁电耦合]]
- [[../concepts/polarization-switching|极化翻转]]
- [[../entities/NiI2|二碘化镍 (NiI2)]]
`;

fs.writeFileSync(base + 'magneto-optical-kerr-effect.md', magnetoOpticalKerr, 'utf8');
fs.writeFileSync(base + 'optical-kerr-effect.md', opticalKerr, 'utf8');
fs.writeFileSync(base + 'magneto-optical-electric-joint-measurement.md', jointMeasure, 'utf8');

// --- 补强 faraday-effect：插入关键参数速览表 ---
let faraday = fs.readFileSync(base + 'faraday-effect.md', 'utf8');
const faradayInsert = `| 参数 | 符号 | 含义 |
| --- | --- | --- |
| 法拉第旋转角 | $\\\\theta$ | 出射偏振面相对入射的旋转角度 |
| 费尔德常数 | $V$ | 材料磁光活性强弱，色散显著 |
| 磁感应强度 | $B$ | 传播方向上的磁场分量 |
| 光程 | $L$ | 光在介质中穿过的长度 |

**关键特性**：法拉第效应是**不可逆的（Non-reciprocal）**`;
if (faraday.includes('**关键特性**：法拉第效应是**不可逆的（Non-reciprocal）**')) {
  faraday = faraday.replace('**关键特性**：法拉第效应是**不可逆的（Non-reciprocal）**', faradayInsert);
  fs.writeFileSync(base + 'faraday-effect.md', faraday, 'utf8');
  console.log('faraday-effect patched');
} else {
  console.log('faraday-effect ANCHOR NOT FOUND');
}

// --- 补强 kerr-effect：插入三种 MOKE 构型对比表 ---
let kerr = fs.readFileSync(base + 'kerr-effect.md', 'utf8');
const kerrInsert = `    *   **横向克尔 (Transverse MOKE)**：磁化强度平行于反射面且垂直于入射面。

| 构型 | 磁化方向 | 探测内容 | 典型用途 |
| --- | --- | --- | --- |
| 极向 (Polar) | 垂直反射面 | 面外磁化分量 | 垂直各向异性、磁拓扑薄膜 |
| 纵向 (Longitudinal) | 平行反射面、入射面内 | 面内磁化、磁滞回线 | 面内各向异性、畴壁运动 |
| 横向 (Transverse) | 平行反射面、垂直入射面 | 反射率变化 | 磁化取向分辨、自旋阀 |
`;
if (kerr.includes('    *   **横向克尔 (Transverse MOKE)**：磁化强度平行于反射面且垂直于入射面。')) {
  kerr = kerr.replace('    *   **横向克尔 (Transverse MOKE)**：磁化强度平行于反射面且垂直于入射面。', kerrInsert);
  fs.writeFileSync(base + 'kerr-effect.md', kerr, 'utf8');
  console.log('kerr-effect patched');
} else {
  console.log('kerr-effect ANCHOR NOT FOUND');
}

console.log('rev18 done');
