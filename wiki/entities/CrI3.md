---
tags: [entity, material, magnetic, 2D, vdW, multiferroic, sliding-ferroelectricity]
title: 碘化铬 / Chromium Triiodide (CrI3)
type: entity
status: mature
category: [D01, Z02]
formula: CrI3
aliases: ["三碘化铬", "CrI₃", "chromium triiodide"]
class: [transition-metal-trihalide, vdW, magnetic-insulator]
properties: [ising-ferromagnetism, stacking-dependent-magnetism, sliding-ferroelectricity, magnetoelectric-coupling]
related_entities: [Cr2Ge2Te6, Fe3GeTe2, NiI2, CrInTe2]
key_quantities:
  Tc_monolayer: "~45 K"
  magnetic_easy_axis: "面外 (Ising 型)"
  Cr_state: "Cr³⁺ t2g³，S = 3/2"
  note: "层间磁序随堆垛（平行/反平行）在 FM/AFM 间切换；滑动极化来自层间界面电荷重排（理论）"
papers: [kaurRecentAdvancesTheoretical2025a, yangRipplingFerroicPhase2021, zhangNonvolatileControlTopological2025]
updated: 2026-08
---

# 碘化铬 / Chromium Triiodide (CrI3)

CrI3 是二维范德华磁性绝缘体的里程碑材料：2017 年它成为首个在单层厚度下被实验证实具有铁磁性的材料，证明磁各向异性可在二维极限下稳定长程磁序（绕开 Mermin–Wagner 限制）。单层 CrI3 是面外易轴的 Ising 铁磁体；双层/多层的层间磁序对堆垛方式高度敏感，并由此衍生出滑动铁电性与磁电耦合，是二维"滑移电子学 (slidetronics)"的原型体系之一 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 👵 太奶导读

太奶，您把这材料想成一摞扑克牌，每张牌是一层原子。单层的时候，牌上画满了朝同一个方向站的小磁针（都朝上或都朝下），这就是"铁磁"，能耐到约零下二百二十八度（45 K）。

妙就妙在两张牌叠一起的时候：它们是对齐着放还是错开一点放，两层的磁针是"头对头"还是"背靠背"可就不一样了——一种叠法两层磁针同向（铁磁），另一种叠法反向（反铁磁）。只要让上面这张牌相对底下那张轻轻一搓（这就是"滑动"），叠法变了，磁的脾气也跟着变；更巧的是这一搓还把材料的对称给搓没了，凭空搓出一个电的方向来。于是"搓一下牌"就能同时管磁又管电，这就是磁电耦合，做又薄又省电的存储器全靠它。

要提醒太奶一句：这里"搓出电来"主要是理论家算出来的门道，真正在 CrI3 上把电方向测出来的实验还不多；有些资料把别的碘化物（比如碘化汞 HgI2）测得的大极化安到 CrI3 头上，那是张冠李戴，咱们这儿只说 CrI3 自己的事儿。

## 🏗️ 结构概览

CrI3 是层状范德华晶体：铬（Cr）原子被碘（I）原子八面体配位，形成"碘—铬—碘"三明治单层，层间靠弱范德华力结合，可机械剥离。多层的层间堆垛分平行与反平行构型，直接决定层间磁耦合与是否破缺反演对称。

![图：CrI3、Cr2Ge2Te6、Fe3GeTe2 双层的几何结构（a–c）与铁电翻转能垒（d）](../../raw/figures/kaurRecentAdvancesTheoretical2025a/fig_21_7MRZGUTM.png)
*   **看图要点**：(a) 为反平行堆垛的 CrI3 双层（Cr 蓝、I 紫），平行堆垛中心对称、反平行堆垛非中心对称——后者因破缺反演对称而允许垂直极化；(d) 对比三种磁性双层沿滑动路径的铁电翻转能垒，能垒越低意味着"一搓就翻"越省电 [[../papers/kaurRecentAdvancesTheoretical2025a]]。
*   **来源**：[[../papers/kaurRecentAdvancesTheoretical2025a]] -> [[../figures/crystal-structures|晶体结构]]

## 🧩 Ising 铁磁性与堆垛依赖的层间磁序

- **单层铁磁**：Cr³⁺ 为 $t_{2g}^3$（$S=3/2$），经 Cr–I–Cr 超交换耦合，单层 $T_C\approx45$ K，面外磁各向异性稳定长程铁磁序。
- **层间磁序随堆垛切换**：双层 CrI3 基态为铁磁，而其层间耦合对堆垛极其敏感——菱方（rhombohedral, AB）堆垛倾向层间铁磁，单斜（monoclinic, AB′）堆垛倾向反铁磁；层间相对滑动可在两者间切换。
- **磁性起源的滑动极化**：在非中心对称的反平行堆垛中，层间界面电子云重排（而非离子位移）产生垂直极化；滑动翻转堆垛即可翻转极化，并同步改变磁基态，实现电写磁读式的磁电耦合 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 🎯 波纹工程与外场调控

- **波纹（ripples）**：二维薄膜本征的面外弯曲波纹引入局域应变场，可在顺电背景中稳定短程铁性序、形成极性纳米微区，提升铁性相变温度，并把畴翻转从协同雪崩式改为局域随机过程。该工作以 GeSe 为模型，CrI3 作为磁性二维体系被列为重要拓展对象 [[../papers/yangRipplingFerroicPhase2021]]。
- **异质结拓扑调控**：借助滑动铁电性，可对 CrI3 相关异质结中的拓扑序进行非易失电学控制 [[../papers/zhangNonvolatileControlTopological2025]]。

## 📊 主要物性参数

| 参数 | 数值 | 备注 |
| :--- | :--- | :--- |
| 单层 $T_C$ | ~45 K | Ising 铁磁 |
| 磁易轴 | 面外 | 各向异性稳定 2D 磁序 |
| Cr 价态/自旋 | Cr³⁺，$t_{2g}^3$，$S=3/2$ | Cr–I–Cr 超交换 |
| 层间磁序 | 堆垛依赖（FM/AFM） | 平行↔反平行堆垛切换 |
| 极化来源 | 层间界面电荷重排 | 滑动铁电（理论为主） |
| 材料家族 | 过渡金属三卤化物 | 范德华磁性绝缘体 |

## 📚 相关论文 (Related Papers)

- [[../papers/kaurRecentAdvancesTheoretical2025a]]：综述滑动铁电，含 §3.4 CrI3/Cr2Ge2Te6/Fe3GeTe2 双层的堆垛、翻转能垒与磁电耦合。
- [[../papers/yangRipplingFerroicPhase2021]]：波纹对二维铁性相变与畴开关的影响（CrI3 为磁性拓展体系）。
- [[../papers/zhangNonvolatileControlTopological2025]]：滑动铁电对 CrI3 相关异质结拓扑序的非易失控制。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/sliding-ferroelectricity|滑动铁电性]]、[[../concepts/magnetoelectric-coupling|磁电耦合]]、[[../concepts/ferromagnetism|铁磁性]]、[[../concepts/magnetic-anisotropy-energy|磁各向异性能]]、[[../concepts/interlayer-stacking|层间堆垛]]
- [[../entities/Cr2Ge2Te6|Cr2Ge2Te6]]（二维铁磁半导体对照）、[[../entities/Fe3GeTe2|Fe3GeTe2]]（金属性二维铁磁对照）、[[../entities/NiI2|NiI2]]（II 型多铁对照）
