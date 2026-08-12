---
tags: [entity, material, multiferroic, 2D, magnetic, vdW]
category: [D01, Z02]
---

# 硫代磷酸铜铬 / Copper Chromium Thiophosphate (CuCrP2S6, CCPS)

CuCrP2S6 (CCPS) 是范德华过渡金属硫代磷酸盐 (TMTPs，ABP2X6) 家族中极具代表性的二维本征多铁材料。作为典型的 **I 型多铁**候选者，其铁电序与磁序源于不同的原子子晶格：铁电性由 Cu⁺ 离子的偏心位移驱动，而磁性则来源于 Cr³⁺ 离子的 3d 电子 [[../papers/laiTwodimensionalFerromagnetismDriven2019]]。

## 1. 自旋-电偶极-谷三重锁定

CCPS 的核心物理价值在于其独特的"自旋-电偶极-谷 (Spin–Dipole–Valley)"三重锁定机制。在强自旋轨道耦合 (SOC) 的介导下，这三个自由度通过对称性破缺相互耦合。由于其铁电相属于极低对称性的 P1 空间群，材料展现出显著的塞曼型谷劈裂 (Zeeman-type valley splitting) [[../papers/laiTwodimensionalFerromagnetismDriven2019]]。

最引人注目的是其单向磁晶各向异性 (Unidirectional magnetocrystalline anisotropy)。理论预测表明，外电场翻转 Cu⁺ 位移产生的电极化方向时，会同步改变易磁化轴的方向。这种锁定效应允许在无需外磁场的情况下，通过电场实现磁矩的可逆翻转，为超低功耗的电控磁存储器件提供了理论路径 [[../papers/tangMultiferroicityTwodimensionalVan2025]]。

## 2. 驱动铁电性与竞争极性相

CCPS 展现了"驱动铁电性 (Driven Ferroelectricity)"。在单层极限下，其基态通常为反铁电 (AFE) 相，但铁电 (FE) 相与其能量极其接近（相差约几十 meV/f.u.） [[../papers/neumayerCompetingPolarPhases2025]]。通过施加外部偏压，可以将 Cu⁺ 离子驱动至范德华间隙内的亚稳态位置（in-gap FE 相），并凭借较高的势垒在室温下保持非易失性。实验上，压电力显微镜 (PFM) 在少层纳米片中观测到了明显的 180° 相位翻转和蝴蝶回线，证实了这种电场驱动的面外铁电性 [[../papers/laiTwodimensionalFerromagnetismDriven2019]]。

## 3. 磁序与层数依赖

CCPS 的磁性呈现显著的层数依赖。块体通常表现为层间反铁磁 (AFM)，但剥离至纳米片厚度时，层内强磁交换作用主导，使其显现出本征铁磁性 ($T_C \approx 64\text{ K}$) [[../papers/laiTwodimensionalFerromagnetismDriven2019]]。这使 CCPS 成为研究二维极限下多铁序共存与相互作用的理想平台，也是目前少有的经实验证实的单层多铁体系 [[../papers/tangMultiferroicityTwodimensionalVan2025]]。凭借磁与电的双重铁性，该材料可实现四种逻辑态 ($P\uparrow M\uparrow$, $P\uparrow M\downarrow$, $P\downarrow M\uparrow$, $P\downarrow M\downarrow$) 的非易失性存储 [[../papers/kaurRecentAdvancesTheoretical2025a]]。

## 4. 本库相关论文

- [[../papers/laiTwodimensionalFerromagnetismDriven2019]]：单层 CCPS 中铁磁性与铁电性的实验共存，自旋-偶极-谷锁定。
- [[../papers/tangMultiferroicityTwodimensionalVan2025]]：二维范德华多铁性综述，讨论电控磁与单向各向异性。
- [[../papers/neumayerCompetingPolarPhases2025]]：CCPS 中 FE/AFE 竞争极性相与驱动铁电性。
- [[../papers/FerroelectricityMultiferroicityAtomic2023]]：原子尺度多铁性综述中 CCPS 作为 I 型多铁案例。
- [[../papers/kaurRecentAdvancesTheoretical2025a]]：二维多铁体系理论预测与性能地图，含 CCPS 多态存储。

## 5. 关联概念与实体

- [[../concepts/multiferroicity|多铁性 Multiferroicity]]
- [[../concepts/magnetoelectric-coupling|磁电耦合 Magnetoelectric Coupling]]
- [[../concepts/type-i-multiferroics|I 型多铁 Type-I Multiferroicity]]
- [[../entities/CuInP2S6|硫磷酸铜铟 CuInP2S6]]（同族位移型铁电参考）
- [[../entities/NiI2|碘化镍 NiI2]]（第二类多铁对照）
- [[../entities/Cr2Ge2Te6|Cr2Ge2Te6]]（二维磁性参考）
