---
tags: [concept, density-functional-theory, dft-plus-u, self-interaction-error, electron-correlation, hubbard-u]
title: high-spin-state
type: concept
status: developing
year: 2004
papers: [zhouFirstprinciplesPredictionRedox2004]
updated: 2026-08-18
---

# high-spin-state

> [!warning] 本页内容待重写（太奶导读部分）
> 本页「太奶导读」为自动生成的占位内容，描述的是某篇论文的研究对象而非本条目本身，待按真实概念重写。
> 正文其余部分与贡献句已核，可参考。（标记于 2026-08-21）


一系列经典的锂离子电池正极材料，包括橄榄石型LiₓMPO₄ (M=Mn, Fe, Co, Ni)、层状LiₓMO₂ (M=Co, Ni) 和尖晶石型LiₓM₂O₄ (M=Mn, Co)。

## 👵 太奶导读

乖孙，这一条讲的是「一系列经典的锂离子电池正极材料，包括橄榄石型LiₓMPO₄ (M=Mn, Fe, Co, Ni)、层状LiₓMO₂ (M=Co, Ni) 和尖晶石型LiₓM₂O₄ (M=Mn, Co)」。
一句话记住它的发现：使用自洽计算U参数的GGA+U方法，能够将锂嵌入电压的计算误差从GGA的0.5-1.0V系统性地降低至几个百分点，与实验值高度吻合，且不牺牲对其他物理性质（如晶格参数、Jahn-Teller效应）的预测精度。

## 🧩 核心内容与机制 (Core Content)

- **研究背景**：LDA/GGA在计算锂离子电池正极材料的锂嵌入电压时，存在系统性的低估问题，误差高达0.5-1.0V，这严重限制了第一性原理计算在电池材料设计中的预测能力。
- **核心问题**：作者将GGA电压低估的根源锁定为电子自相互作用误差在离域的锂金属态和局域的过渡金属d轨道态之间无法有效抵消，并旨在通过能显式处理库仑关联的DFT+U方法来解决这一物理本质问题。
- **主要结论**：使用自洽计算U参数的GGA+U方法，能够将锂嵌入电压的计算误差从GGA的0.5-1.0V系统性地降低至几个百分点，与实验值高度吻合，且不牺牲对其他物理性质（如晶格参数、Jahn-Teller效应）的预测精度。
- **领域贡献**：1. 从物理根源上阐明了GGA电压误差的成因及GGA+U的修正机制；2. 推广并验证了自洽计算U参数的线性响应方法，确立了真正的第一性原理电压预测范式；3. 为计算电化学领域提供了验证该方法有效性的系统案例，成为后续研究的标杆。
- **研究意义**：建立起一套高精度预测过渡金属化合物氧化还原电位的理论框架和计算方案，证明了修正电子自相互作用是提升电压预测精度的关键，为理性设计新型电池材料提供了强大的计算工具。

## 📚 相关论文 (Related Papers)

- [[../papers/zhouFirstprinciplesPredictionRedox2004]]：1. 从物理根源上阐明了GGA电压误差的成因及GGA+U的修正机制；2. 推广并验证了自洽计算U参数的线性响应方法，确立了真正的第一性原理电压预测范式；3. 为计算电化学领域提供了验证该方法有效性的系统案例，成为后续研究的标杆。

## 🔗 关联概念与实体 (Related)

- [[../concepts/density-functional-theory|density-functional-theory]]
- [[../concepts/self-interaction-error|self-interaction-error]]
- [[../concepts/electron-correlation|electron-correlation]]
- [[../concepts/hubbard-u|hubbard-u]]
- [[../concepts/linear-response|linear-response]]
- [[../concepts/jahn-teller-distortion|jahn-teller-distortion]]
- [[../concepts/redox-potential|redox-potential]]
- [[../concepts/chemical-potential|chemical-potential]]
- [[../concepts/electron-localization|electron-localization]]
- [[../concepts/charge-order|charge-order]]
- [[../entities/VASP|VASP]]
