---
tags: [entity, device, ferroelectric, memory, non-volatile]
category: [D02, Z01]
---

# 铁电随机存取存储器 / Ferroelectric Random Access Memory (FeRAM / FRAM)

**FeRAM** 是一种利用铁电体自发极化电场效应进行非易失性数据存储的随机存取存储器。其物理核心在于铁电电容器 (FeCAP) 中极化状态的非易失双稳态，通过电场翻转实现逻辑 "0" 与 "1" 的写入。FeRAM 兼具 DRAM 的快速读写能力（< 50 ns）与 Flash 的非易失性，是当前高可靠性嵌入式存储器的核心技术方向 [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。

## 1. 架构演进与微缩物理

*   **1T-1C 结构与破坏性读出**：传统 FeRAM 采用类似 DRAM 的 1T-1C（一晶体管-一电容）单元。读取时，位线感测放大器探测极化翻转产生的电荷流。由于读取过程涉及极化翻转，其本质是破坏性的，读取后需自动执行写回操作 [[../papers/xueEmergingNonvolatileMemories2011]]。
*   **铪基铁电的突破**：传统钙钛矿材料（如 [[PZT|PZT]]）面临“尺寸效应”瓶颈，厚度减薄至数十纳米以下时极化性能剧烈衰减。2011 年 [[HZO|HZO]] 等铪基铁电材料的发现突破了这一限制，其与 CMOS 工艺的高度兼容性使得 FeRAM 得以实现 3D 垂直堆叠集成（类似 3D NAND），大幅提升了存储密度 [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。
*   **二维铁电与“再成键”机制**：新兴的二维材料（如 [[SnTe|SnTe]]、[[In2Se3|In2Se3]]）由于其范德华层状结构，能在单层极限（~1 nm）下保持稳定的铁电性。其中，[[In2Se3|In2Se3]] 表现出独特的“再成键” (Re-bonding) 翻转机制，通过原子横向位移约 100 pm 来打破并重建共价键，从而在本征上抵抗退极化场，为超薄、高密度 FeRAM 提供了物理支撑 [[../papers/huangTwodimensionalIn2Se3Rising2022]]。

## 2. 性能图景与应用场景

FeRAM 的关键优势在于极高的写耐久性（$10^{12}\text{--}10^{15}$ 次循环）和极低的写入功耗（$\text{fJ/bit}$ 量级），这使其在以下领域具有统治力：
*   **高频写入记录**：如汽车黑匣子、智能仪表及工业物联网终端。
*   **神经形态计算**：利用铁电畴的渐进式翻转模拟突触可塑性（如 LTP/LTD），Hf-FEs 交叉阵列可物理实现高效的向量-矩阵乘法 (VMM) [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。
*   **航空航天**：由于其信息存储不依赖电荷，FeRAM 具有天然的抗总剂量 (TID) 辐射特性。

## 3. 关键挑战：唤醒、疲劳与热预算

尽管前景广阔，但 FeRAM 的大规模应用仍需克服多重屏障：
1.  **可靠性效应**：铪基铁电在初始循环中存在“唤醒效应” (Wake-up effect)，即极化值随循环增加而增大；而长期循环后会出现“疲劳效应” (Fatigue)，源于氧空位对畴壁的钉扎 [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]。
2.  **热预算冲突**：HfO2 结晶通常需要 $>450^\circ\text{C}$ 的热处理，这与后道工艺 (BEOL) 限制的 $<400^\circ\text{C}$ 热预算存在冲突，亟需开发如 PE-ALD 等低温沉积技术。
3.  **二维集成挑战**：对于 [[SnTe|SnTe]] 等二维体系，如何实现晶圆级的大面积均匀生长及高质量的金属-半导体接触仍是工程难题 [[../papers/guanRecentProgressTwoDimensional2020]]。

## 4. 相关指标对比

| 指标 | 传统 FeRAM (PZT) | 铪基 FeRAM (HZO) | 二维 FeRAM (SnTe/In2Se3) |
| :--- | :--- | :--- | :--- |
| **可微缩极限** | ~100 nm | < 10 nm | < 1 nm (Atomic layer) |
| **工作电压** | 3.3 - 5.0 V | 1.0 - 1.8 V | < 1 V (潜力值) |
| **翻转速度** | 50 - 100 ns | < 10 ns | 亚纳秒 (理论) / 80 ns (实验) |
| **CMOS 兼容性** | 差 (铅污染/厚度限制) | 极佳 (High-k 介质基础) | 尚待验证 (范德华集成) |

## 5. 本库相关代表性论文

- [[../papers/chenHafniumBasedFerroelectricPostMoore2026]]：系统梳理了铪基铁电在 1T-1C 及 3D 集成中的最新物理与架构进展。
- [[../papers/huangTwodimensionalIn2Se3Rising2022]]：详述了二维 In2Se3 的相变型铁电机理及其在非易失性存储中的潜力。
- [[../papers/xueEmergingNonvolatileMemories2011]]：从存储层次结构视角对比了 FeRAM 与 PCM、STT-RAM 等新兴存储器的优劣。
- [[../papers/guanRecentProgressTwoDimensional2020]]：提供了 SnTe 等二维铁电体原型器件（ON/OFF 比达 3000）的实验锚点。

## 6. 关联概念与实体

- [[../entities/HZO|HZO]] / [[../entities/HfO2|HfO2]] (核心铪基材料)
- [[../entities/SnTe|SnTe]] / [[../entities/In2Se3|In2Se3]] (二维候选材料)
- [[../entities/FeFET|FeFET]] (铁电场效应管，非破坏性读出路线)
- [[../concepts/polarization-switching|极化翻转机制]] (NLS 模型与 KAI 模型)
- [[../concepts/depolarization-field|退极化场]] (微缩化的核心瓶颈)
- [[../projects/project-5-snte-ferroelectric-sim|Project-5]] (SnTe 存储器模拟参考)
