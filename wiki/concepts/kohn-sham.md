---
tags: [concept, DFT, quantum-mechanics]
category: [Z01]
---

# Kohn-Sham 方程 / Kohn-Sham Equations

**Kohn-Sham（KS）方程**是密度泛函理论（DFT）的核心方程，将多电子问题映射为等效的单电子问题。通过引入交换关联泛函，KS 方程在保持计算可行性的同时近似处理电子-电子相互作用。

## 核心内容

### 方程形式
KS 方程：[-½∇² + V_eff[n(r)]] ψ_i(r) = ε_i ψ_i(r)，其中有效势 V_eff = V_ext + V_H + V_xc。

### 自洽场迭代
- 从初始电荷密度出发，循环求解 KS 方程直至电荷密度收敛（自洽场，SCF）[[../papers/kresseEfficientIterativeSchemes1996d]]。
- 收敛效率依赖于迭代算法（共轭梯度、阻尼混合等）。

### 交换关联泛函
- LDA（局域密度近似）、GGA（广义梯度近似）、hybrid（混合泛函）等不同层级。
- 范德华修正（DFT-D3）对层状材料至关重要。

## Related Papers

- [[../papers/gajdosLinearOpticalProperties2006]]：KS 方程在光学性质计算中的应用

## 关联概念与实体

- [[../concepts/density-functional-theory|密度泛函理论]]
- [[../concepts/self-consistent-field|自洽场]]
- [[../concepts/harris-foulkes-functional|Harris-Foulkes 泛函]]
