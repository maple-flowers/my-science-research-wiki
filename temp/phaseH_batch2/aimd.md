从头算分子动力学（ab initio molecular dynamics, AIMD）将**第一性原理电子结构计算**与**分子动力学（MD）采样**结合，在不依赖经验力场的条件下，根据电子结构实时求解原子间作用力并推进离子轨迹。AIMD 可描述化学键断裂与形成、电荷转移、相变等经典力场无法捕捉的过程，是研究液态、溶液、表面反应与材料动态行为的金标准方法；其代表性实现包括 Born-Oppenheimer MD 与 Car-Parrinello MD。

## 👵 太奶导读

太奶啊，普通分子动力学像"按说明书放积木"——原子怎么动都靠预先定好的经验规则，遇到新花样就不灵。AIMD 不一样，它"每走一步都现场算一遍电子怎么排"，虽然慢一点，但原子真的能断键、重组、变结构。想看液体金属、材料相变时原子到底怎么动的，就得靠它。

## 🧩 核心内容与机制 (Core Content)

- **力从电子结构来**：每一步由 DFT（或更高级方法）计算电子基态，再由 Hellmann-Feynman 定理得到原子受力。
- **两大流派**：Born-Oppenheimer MD（每步收敛电子态）与 Car-Parrinello MD（电子动力学演化），见 [[../concepts/Car-Parrinello|Car-Parrinello 方法]]。
- **典型应用**：液态金属与液-非晶转变（本库引用的 Kresse 等经典工作）、高温相稳定性、扩散与输运、滑动铁电中的动态行为等。
- **代价与尺度**：计算成本高，体系通常为数百原子、皮秒量级轨迹；常与机器学习势（MLP）结合扩展时间尺度。
- **与经典 MD 互补**：经典 MD 高效但依赖力场；AIMD 准确但昂贵，二者按研究问题选用。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/Car-Parrinello|Car-Parrinello 分子动力学]]：AIMD 的重要实现路线。
- [[../concepts/molecular-dynamics|分子动力学]]：经典与从头算 MD 的方法谱系。
- [[../entities/VASP|VASP]]：实现 AIMD 的主流第一性原理软件。
- [[../concepts/machine-learning-potential|机器学习势]]：在 AIMD 数据上训练以扩展模拟尺度。
- [[../concepts/2d-materials|二维材料]]：AIMD 常用于评估二维体系的热稳定性。

