VASP（Vienna Ab initio Simulation Package，维也纳第一性原理模拟包）是**基于平面波基组与赝势的密度泛函理论（DFT）计算软件**，支持结构优化、电子结构、声子、分子动力学、GW/BSE、杂化泛函与含自旋轨道（SOC）等计算，是材料科学、凝聚态物理与化学领域应用最广泛的第一性原理工具之一（本库绝大多数计算论文的主力软件）。

## 👵 太奶导读

太奶啊，VASP 是"材料计算界最常用的算盘"：科学家想知道一种新材料的电子结构、能不能铁电、超导温度多高，就把原子坐标"喂"给 VASP，它用密度泛函理论"硬算"出来。全世界海量论文的"计算图"都是 VASP 画的。你在这个 Wiki 里看到的各种能带、声子、形成能，大多出自它手。

## 🧩 核心内容与机制 (Core Content)

- **方法**：平面波基组 + PAW 赝势 + DFT（LDA/GGA/PBE、杂化 HSE、DFT+U）（本库 DFT 计算论文）。
- **功能**：结构优化、能带（band-structure）、态密度、声子（有限位移/DFPT）、弹性、磁性、GW/BSE 激发态与分子动力学（本库计算论文）。
- **物理量**：形成能（formation-energy）、能带对齐（band-alignment）、极化（born-effective-charge）、电子-声子耦合（electron-phonon-coupling，与 EPW 联动）（本库迁移与势垒论文）。
- **进阶**：自旋轨道耦合（spin-orbit-coupling）与拓扑不变量、NEB 过渡态、应力-应变。
- **生态**：与 Wannier90（紧束缚/输运）、Phonopy（声子）等联动（本库 Wannier 与声子论文）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/density-functional-theory|密度泛函理论]]：VASP 的理论基础。
- [[../entities/Wannier90|Wannier90]]：VASP 的能带插值伙伴。
- [[../concepts/band-structure|能带结构]]：VASP 的核心输出。
- [[../concepts/formation-energy|形成能]]：VASP 的缺陷计算。

