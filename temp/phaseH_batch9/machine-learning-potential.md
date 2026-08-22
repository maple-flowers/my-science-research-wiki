机器学习势（machine learning potential, MLP）是**用机器学习模型（神经网络、核回归等）拟合原子构型到能量/力的映射**、以接近第一性原理精度实现大规模与长时间分子动力学模拟的势函数。它保留 DFT 精度、免除其成本，是现代材料模拟（相变、缺陷、扩散、电化学）的核心工具。

## 👵 太奶导读

太奶啊，模拟材料时最准的"电子级计算"（DFT）很慢，几千个原子就算不动；最快的"经验公式"（经典势）快但经常不准。机器学习势的聪明办法是：先用 DFT 算一批数据当"题库"，训练一个 AI 学会"原子怎么摆能量多少"，然后让这个 AI 代替 DFT 去算——又快又准。材料科学家现在的"模拟神器"。

## 🧩 核心内容与机制 (Core Content)

- **工作流**：DFT 生成训练集（能量/力/应力）→ 训练 ML 模型（如 DeepMD、NequIP、MACE 等）→ 验证 → 用于分子动力学/蒙特卡洛（本库 MLP 相关论文）。
- **精度与效率**：保留近 DFT 精度，可将模拟尺度提升到数万-数亿原子、纳秒-微秒时间尺度，突破传统 ab initio MD 限制。
- **应用场景**：结构相变（structural-phase-transition）、缺陷迁移（nudged-elastic-band 补充）、热输运、液体/无定形材料、催化界面与合金（本库多篇 MLP 驱动的相变与力学论文）。
- **挑战**：训练集多样性、外推可靠性、不确定性量化与长程相互作用（电荷、范德华）描述。
- **与经典 MD 的关系**：MLP 可视为"从 DFT 学习出的高精度经典势"，与分子动力学（molecular-dynamics）工作流无缝衔接。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/density-functional-theory|密度泛函理论]]：MLP 的精度来源。
- [[../concepts/molecular-dynamics|分子动力学]]：MLP 的主要应用场景。
- [[../concepts/structural-phase-transition|结构相变]]：MLP 研究的重要问题。
- [[../concepts/formation-energy|形成能]]：MLP 用于缺陷与稳定性。

