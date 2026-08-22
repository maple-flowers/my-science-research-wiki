# 对分布函数 / Pair Distribution Function

对分布函数（pair distribution function, PDF, g(r)）**描述材料中任意原子周围、距离 r 处出现另一个原子的概率密度**，由总散射（X 射线/中子）数据傅里叶变换得到，可同时解析晶格周期性秩序与局域/无序结构。PDF 特别适合研究纳米材料、插层体系、电荷密度波与超导竞争等"短程有序、长程部分无序"的体系。

## 👵 太奶导读

想知道材料里原子是怎么"站位"的，普通衍射只能看到"整齐划一的队列"（周期性）。但很多材料表面整齐、暗地里局部却乱成一团。对分布函数这招"不看队列看邻居"：统计每个原子周围多远处有多少邻居，把无序和畸变也照出来。想看"纳米级、插层、带点乱的"材料，它是一把好手。

## 🧩 PDF 与 CDW-超导竞争

- **晶格、CDW 与超导的层级关系**：对 TaSe₂₋ₓTeₓ（x=0, 0.2, 0.66, 1, 1.66, 2）固溶体的研究表明，强烈的晶格畸变（如 Ta 原子层皱褶）对电荷密度波（CDW）与超导（SC）序均有害；完美的二维晶格有序是 CDW 出现的前提但不足以产生 SC，SC 序还需要过渡金属（Ta）亚晶格在三维空间上具有周期性，而局部化学无序可能促进 SC 序的出现（[[../papers/Petkov2020hierarchy|Petkov 2020]]）。

## 🧩 PDF 与纳米/插层结构

- **插层离子的局域排布**：PDF 确凿证实沸石 ITQ-4 伪一维纳米孔道中的铯以正离子 Cs⁺ 形式存在，占据特定晶格位置并排列成短程有序、连续的锯齿形链状结构，形成带正电的亚晶格，为孔道中低密度电子气提供电荷平衡，解释了最大铯负载量的物理根源（[[../papers/petkovStructureIntercalatedCs2002|Petkov 2002]]）。
- **纳米粒子结构演化的辅助解析**：分子动力学与结构模拟结合，可解析钛纳米粒子堆积模式、熔化与相变路径，其中尺寸与温度依赖的结构多样性（二十面体、HCP、BCC 共存）正是 PDF 类局域结构分析的典型对象（[[../papers/Zhang2019a|Zhang 2019a]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Petkov2020hierarchy]] — Hierarchy among the crystal lattice, charge density wave, and superconducting orders in transition metal dichalcogenides
- [[../papers/Zhang2019a]] — Studying Stability of Atom Packing for Ti Nanoparticles on Heating by Molecular Dynamics Simulations
- [[../papers/petkovStructureIntercalatedCs2002]] — Structure of Intercalated Cs in Zeolite ITQ-4

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/superconductivity|超导电性]]：PDF 揭示的晶格-电子层级关系。
- [[../concepts/charge-density-wave|电荷密度波]]：PDF 解析的局部畸变序。
- [[../concepts/molecular-dynamics|分子动力学]]：与 PDF 互补的结构模拟。
- [[../concepts/penetration-depth|穿透深度]]：超导序的实验探针。
- [[../entities/TaSe2|TaSe₂]]：CDW-超导竞争的端元材料。
- [[../entities/NbSe2|NbSe₂]]：CDW-超导竞争的单晶体系。
- [[../entities/Ti|Ti]]：纳米粒子结构演化研究对象。
*（内容由AI生成，仅供参考）*
