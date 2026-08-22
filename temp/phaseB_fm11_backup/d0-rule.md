---
tags: [concept]
title: 'd⁰规则 / d⁰ Rule'
type: concept
status: developing
papers: ['hillWhyAreThere2000a', 'fengFerroelectricityMultiferroicityTwodimensional2020', 'aiFerroelectricityCoexistedPorbital2022', 'zhaoOpticalFingerprintsTwodimensional2024', 'tangMultiferroicityTwodimensionalVan2025', 'RecentAdvancesGrowth2025']
updated: 2026-08-18
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d1440e82f85676d2b3ce24ffb8efaf05_3c6f8b439a7b11f1a98a525400f8a581
    ReservedCode1: SYmsos5XmN8yUxCRfzn+/oB4rEZXYelhL0okgAKU7atTAbYKJnMmjpdg6tBoB56DmUEAZZOh1hpLKpnDWKQtKYuZlWlpXQpCmZLDW70o6g78+6yoDT8mSf2xEGhtF/W9wGPrkaq5r+b+La4+K3rhN3/2dfhwd4i14Dw4OX7aZIPv/utyUcJjh1NRwxU=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d1440e82f85676d2b3ce24ffb8efaf05_3c6f8b439a7b11f1a98a525400f8a581
    ReservedCode2: SYmsos5XmN8yUxCRfzn+/oB4rEZXYelhL0okgAKU7atTAbYKJnMmjpdg6tBoB56DmUEAZZOh1hpLKpnDWKQtKYuZlWlpXQpCmZLDW70o6g78+6yoDT8mSf2xEGhtF/W9wGPrkaq5r+b+La4+K3rhN3/2dfhwd4i14Dw4OX7aZIPv/utyUcJjh1NRwxU=
---



# d⁰规则 / d⁰ Rule

d⁰ 规则（d⁰ rule）由 Nicola Hill 于 2000 年提出（[[../papers/hillWhyAreThere2000a]]）：**在钙钛矿氧化物中，经典的位移型铁电要求 B 位过渡金属离子具有 d⁰ 电子构型，而磁性则要求 d 轨道存在未配对电子**。两者对同一 d 轨道的需求相互排斥，这正是"为什么磁性铁电体如此稀少"的根源。d⁰ 规则并非不可逾越的禁令——化学（孤对电子）、结构（几何铁电）与自旋（磁性掺杂/自旋驱动）三类破局路径，构成了现代多铁材料设计的核心框架。

## 👵 太奶导读

可以这样想：要做出"铁电"（一按电场就能翻过来复过去的电荷排列），材料里那个关键的小离子（B 位离子）最好"两手空空"——d 轨道是空的（d⁰），这样它才乐意跟周围的氧"牵手"（杂化），一歪就产生电荷分离。但要做出"磁性"，恰恰需要这个离子 d 轨道里有"存货"（未成对电子）才能自带小磁铁。同一个原子，既要"两手空空"又要"手里有货"，这就矛盾了——所以又磁又电的材料特别少见。不过科学家找到几个"开后门"的办法：让别的原子（比如铋的孤对电子）来干铁电的活，或者靠整体结构扭曲、靠层与层之间的滑动来产生电，把 d 轨道腾出来专门搞磁性。

## 🧩 物理起源：为什么铁电偏爱 d⁰

在 ABO₃ 钙钛矿中，铁电不稳定性源自 **B–O 共价杂化**：B 位 d 轨道与 O 2p 轨道杂化形成的不对称键电荷，提供使 B 离子偏心位移（向氧八面体的一角移动）的驱动力。当 B 位为 d⁰ 构型（如 Ti⁴⁺、Nb⁵⁺）时，成键态被填充、反键态空置，杂化能量增益最大化，铁电畸变稳定；而当 d 轨道被部分占据（dⁿ, n≠0），占据态与 O 2p 的杂化倾向于抵消畸变驱动力（与 Jahn–Teller 畸变（[[../concepts/jahn-teller-distortion|Jahn-Teller畸变]]）竞争），从而抑制偏心位移。Hill 通过第一性原理对比 BiMnO₃ 与 LaMnO₃、YMnO₃ 与 LaMnO₃，定量展示了这一 d 电子占据如何压制铁电不稳定性。

## 🧰 破局路径

| 路径     | 机制                                                                                   | 代表体系              | 证据来源                                                                                                           |                                    |
| :----- | :----------------------------------------------------------------------------------- | :---------------- | :------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| 化学驱动   | A 位 Bi³⁺ 6s² 孤对电子与 O 2p 强共价提供铁电驱动力（[[../concepts/stereochemically-active-lone-pair]] | 立体化学活性孤对电子]]）     | BiMnO₃                                                                                                         | [[../papers/hillWhyAreThere2000a]] |
| 结构驱动   | 小半径 A 位稳定六方非中心对称结构，绕开 d⁰ 需求（[[../concepts/geometric-ferroelectricity]]               | 几何铁电]]）           | YMnO₃                                                                                                          | [[../papers/hillWhyAreThere2000a]] |
| 磁性掺杂   | 在非磁性铁电母体中替换磁性原子，靠晶格畸变调制磁交换实现电控磁                                                      | ScCrP₂Se₆         | [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]                                            |                                    |
| p 轨道磁性 | 以 N-2p 巡游铁磁替代 d 电子磁性，从根本上绕开 d 轨道矛盾                                                   | X₂NO₂（X = In, Tl） | [[../papers/aiFerroelectricityCoexistedPorbital2022]]                                                          |                                    |
| 层间滑动   | 二维 vdW 层间相对滑动产生铁电，与层内磁序解耦共存                                                          | 层间滑动多铁            | [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]、[[../papers/tangMultiferroicityTwodimensionalVan2025]] |                                    |

## 🔬 核心判据：Hill 2000

[[../papers/hillWhyAreThere2000a]] 通过 DFT 平面波赝势计算与紧束缚拟合，系统论证了 d⁰ 规则：
- **矛盾的本质**：铁电位移需要 B 位 d⁰ 构型（利于共价杂化），磁性需要 dⁿ（n≠0）未配对电子，二者在钙钛矿 B 位天然冲突；
- **化学破局**：BiMnO₃ 中 Bi³⁺ 的 6s² 孤对电子与 O 2p 形成强共价键，提供独立于 B 位 d 电子的铁电驱动力；
- **结构破局**：YMnO₃ 中半径较小的 Y³⁺ 稳定了本征非中心对称的六方结构，使铁电不依赖 B 位 d⁰ 构型。

该文将多铁研究从盲目的材料搜寻引向基于电子结构与化学键合的理性设计，是磁电多铁领域的经典必读文献。

## 🔬 二维破局：磁性掺杂与 p 轨道磁性

在二维极限下，d⁰ 规则的破局出现新途径。feng 等（[[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]）基于第一性原理预言：非磁性铁电母体 Sc₂P₂Se₆（面外极化 3.09 μC/cm²，源自 P 原子不对称翘曲）经一半 Sc 被 Cr 替换得到 ScCrP₂Se₆，同时具有铁电与铁磁；其磁电耦合机制独特——**铁电相磁基态为反铁磁，反铁电相磁基态为铁磁**，源于相变引起的晶格畸变对 Cr–Se–Se–Cr 间接交换作用路径的调制；施加约 0.82 V/Å 的外电场即可在 FM 与 AFM 态间可逆电控切换。

ai 等（[[../papers/aiFerroelectricityCoexistedPorbital2022]]）走得更远：在二维类 MXene 氧氮化物 X₂NO₂（X = In, Tl）中预测铁电性、N-2p 驱动的巡游铁磁性与金属性三者共存，**以 p 轨道磁性完全替代 d 电子磁性，从根本上绕开 d⁰ 规则**，并在 Tl₂NO₂/WTe₂ 异质结中演示了界面磁电耦合。

## 🔬 层间滑动多铁与表征工具箱

zhao 等（[[../papers/zhaoOpticalFingerprintsTwodimensional2024]]）证明二维层间滑动多铁材料的四个多铁态（P↑N↑/P↑N↓/P↓N↓/P↓N↑）在克尔效应（反常光电导 σ^A_xy）与 SHG 张量上具有严格可区分的"光学指纹"，斜入射 PPP 偏振分辨 SHG 的"六瓣花"图案可无损识别全部四个态。tang 综述（[[../papers/tangMultiferroicityTwodimensionalVan2025]]）系统提出在二维范德华材料中"人工设计"多铁性的四大策略（磁中造电、电中生磁、弹中诱电、异质结组装）。RecentAdvancesGrowth2025（[[../papers/RecentAdvancesGrowth2025]]）则从实验角度综述二维多铁（重点为 II 型铁磁-铁电/铁磁-铁弹体系）的 CVD/PVD/MBE/ALD 生长、STM/SHG/拉曼/太赫兹表征及器件应用，以 NiI₂、Cr₂S₃、CuCrSe₂、p 型 SnSe 为里程碑案例。

## 📚 相关论文 (Related Papers)

- [[../papers/hillWhyAreThere2000a]]：提出 d⁰ 规则及化学/结构两条破局路径，多铁理性设计的奠基文献。
- [[../papers/fengFerroelectricityMultiferroicityTwodimensional2020]]：Sc₂P₂Se₆/ScCrP₂Se₆ 二维多铁，磁性掺杂 + 晶格畸变调制交换实现电控磁。
- [[../papers/aiFerroelectricityCoexistedPorbital2022]]：X₂NO₂ 中 p 轨道巡游铁磁与铁电共存，从根本上绕开 d⁰ 规则。
- [[../papers/zhaoOpticalFingerprintsTwodimensional2024]]：层间滑动多铁四态的光学指纹（SHG/克尔效应）无损识别。
- [[../papers/RecentAdvancesGrowth2025]]：二维多铁生长、表征与器件应用综述。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：二维 vdW 多铁"人工设计"四大策略综述。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/ferroelectricity|铁电性]]：d⁰ 规则约束的对象之一。
- [[../concepts/ferromagnetism|铁磁性]]：d⁰ 规则约束的另一端。
- [[../concepts/multiferroicity|多铁性]]：铁电与磁序共存，d⁰ 规则直接制约的目标。
- [[../concepts/magnetoelectric-coupling|磁电耦合]]：突破 d⁰ 规则后实现的电场控磁/磁场控电。
- [[../concepts/exchange-interaction|交换作用]]：磁性掺杂路径中晶格畸变所调制的物理量。
- [[../concepts/weak-ferromagnetism|弱铁磁性]]：在不触犯 d⁰ 矛盾前提下获得磁性的路径之一。
- [[../concepts/stereochemically-active-lone-pair|立体化学活性孤对电子]]：化学破局的微观机制。
- [[../concepts/geometric-ferroelectricity|几何铁电]]：结构破局的核心机制。
- [[../concepts/jahn-teller-distortion|Jahn-Teller畸变]]：与铁电畸变竞争 d 电子占据的晶格效应。
- [[../concepts/sliding-ferroelectricity|滑动铁电]]：二维层间滑动破局路径的基础。
- [[../concepts/2d-materials|二维材料]]：d⁰ 规则破局的新平台。
- [[../entities/BiFeO3|BiFeO₃]]、[[../entities/BiMnO3|BiMnO₃]]、[[../entities/YMnO3|YMnO₃]]：d⁰ 规则破局的三维代表体系。
*（内容由AI生成，仅供参考）*
