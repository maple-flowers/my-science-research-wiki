Wannier90 是**计算最大化局域 Wannier 函数（MLWF）的开源软件**，通过对 DFT 能带（通常来自 VASP/Quantum ESPRESSO）做幺正变换构造紧束缚模型，用于能带插值、输运（Boltzmann/Buttiker）、拓扑不变量（Z₂/Chern）、贝里曲率、电子-声子耦合与自旋-能谷等性质计算，是连接第一性原理与多体/输运模型的桥梁（本库计算论文常用工具）。

## 👵 太奶导读

太奶啊，DFT 算出的能带是"全局图"，但研究输运、拓扑、局域化学键时，希望把电子"关"到一个个局域轨道里（像画成局部的"小元胞"）。Wannier90 就干这个：把平面波能带"重新排版"成最局域的 Wannier 函数，得到一套"精确的紧束缚模型"。之后算电导、拓扑数、自旋霍尔都方便了。

## 🧩 核心内容与机制 (Core Content)

- **MLWF**：通过 Wannier 函数离散化/局域化（disentanglement + spread 最小化）构造紧束缚哈密顿量（本库 Wannier 计算论文）。
- **能带插值**：粗 k 网格 DFT → 精细 k 网格插值，用于输运与光学计算（本库输运论文）。
- **拓扑与几何**：计算 Z₂ 不变量、Chern 数、贝里曲率与反常霍尔电导（本库拓扑物性论文）。
- **输运与耦合**：Boltzmann 输运、电子-声子耦合（electron-phonon-coupling，配合 EPW）（本库热电与超导论文）。
- **工作流**：VASP→Wannier90 两步（本库 VASP 计算论文）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../entities/VASP|VASP]]：Wannier90 的 DFT 上游。
- [[../concepts/band-structure|能带结构]]：Wannier 插值的对象。
- [[../concepts/topological-insulator|拓扑绝缘体]]：Wannier 计算的拓扑量。
- [[../concepts/electron-phonon-coupling|电子-声子耦合]]：Wannier 的输运应用。

