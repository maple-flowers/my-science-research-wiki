# 双光子激发 / Two-Photon Excitation

双光子激发（two-photon excitation, TPE）指**分子或材料通过同时吸收两个光子（通常近红外）跃迁到激发态**的非线性光学过程。其跃迁概率正比于入射光强平方，因此只有在**焦点处光强极大**时才显著发生——这赋予 TPE 天然的**三维空间选择性**与**深穿透**优势，广泛用于双光子荧光显微、三维光刻/双光子聚合、光动力治疗与体内成像。

## 👵 太奶导读

普通荧光是"一颗光子一榔头"把电子敲上去（单光子吸收）；双光子激发则是"两颗光子同时使劲"，而且**两颗光子必须同一瞬间撞上电子**才有效。因为这种"同时性"在光束最集中的焦点处最容易发生，所以它能做到"指哪打哪"——只在焦点那一小块区域发光/固化，其他区域完全不受影响。这就是它能做 3D 打印和深层组织成像的原因。

## 🧩 基本物理：双光子吸收截面

双光子吸收的强弱由**双光子吸收截面 σ₂**（单位 GM，1 GM = 10⁻⁵⁰ cm⁴·s·photon⁻¹）刻画。D-π-A / D-π-D 型推拉电子体系通过增大分子内电荷转移（ICT）显著放大 σ₂。Nakanishi 等建立基于双光子波函数的全量子多模理论，证明矩形时间窗波函数在特定条件下可完全抑制单光子吸收而保持双光子吸收（纠缠诱导双光子透明）（[[../papers/Nakanishi2009full|Nakanishi 2009]]）。

## 🔬 双光子荧光探针与成像

- **双光子三重荧光探针**：在二苯乙烯骨架上引入双氰基受体与二甲氨基给体，构建 D-π-A 型探针，发射峰随溶剂极性从 445 nm 红移至 641 nm（≈196 nm），σ₂ 高达 5560–6670 GM，并首次在双光子激发下观察到 LE/TICT/激基复合物三重荧光，可同时传感极性、粘度与温度（[[../papers/H2017fluorescence|H 2017]]、[[../papers/Huang2019solvatochromic|Huang 2019]]、[[../papers/Huang2023two|Huang 2023]]）。
- **三维缺陷成像**：飞秒钛宝石激光双光子激发可在多晶 ZnSe 内部 200 μm 深度实现三维缺陷光致发光成像（[[../papers/Khitrov2002internal|Khitrov 2002]]）。

## 🖨️ 双光子聚合引发剂

双光子聚合（[[../concepts/photopolymerization|光聚合]]）利用 TPE 的焦点选择性实现亚微米级三维微纳加工。其核心是**双光子引发剂**：机理分顺序/同时双光子吸收，分子设计准则为 D-π-D / D-π-A-π-D / A-π-D-π-A，代表性化合物包括二苯乙烯衍生物、噻嗪染料、三苯胺与香豆素/酮香豆素二元体系（[[../papers/WRZYSZCZYNSKI2010initiators|Wrzyszczyński 2010]]，见 [[../concepts/two-photon-absorption|双光子吸收]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/H2017fluorescence]] — Dicyanostilbene-based Two-photon Thermo-solvatochromic Fluorescence Probes with Two-photon Triple Fluorescence
- [[../papers/Huang2019solvatochromic]] — Stilbene-Based Two-Photon Thermo-Solvatochromic Fluorescence Probes with Large Two-Photon Absorption Cross Sections and Two-Photon Triple Fluorescence
- [[../papers/Huang2023two]] — Two Dicyanostilbene-Based Two-Photon Fluorescence Environmentally Sensitive Probes with Large Two-Photon Absorption Cross Sections and Two-Photon Triple Fluorescence
- [[../papers/Nakanishi2009full]] — Full Quantum Analysis of Two-Photon Absorption Using Two-Photon Wave Function
- [[../papers/Khitrov2002internal]] — Internal Defects Observed by Two-Photon-Induced Photoluminescence
- [[../papers/WRZYSZCZYNSKI2010initiators]] — Two-photon initiators of polymerization

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/two-photon-absorption|双光子吸收]]：TPE 的定量描述——吸收截面与跃迁选择定则。
- [[../concepts/nonlinear-optics|非线性光学]]：双光子过程属于二阶以上的非线性光学效应。
- [[../concepts/photoluminescence|光致发光]]：双光子激发荧光探测的本质。
- [[../concepts/photopolymerization|光聚合]]：双光子聚合引发剂的应用领域。
- [[../concepts/phosphorescence|磷光]]：与双光子激发相关的长寿命发光通道。
- [[../entities/ZnSe|ZnSe]]：双光子诱导三维缺陷成像的代表材料。
- [[../entities/GaN|GaN]]：双光子微加工与集成光电子器件材料。
*（内容由AI生成，仅供参考）*
