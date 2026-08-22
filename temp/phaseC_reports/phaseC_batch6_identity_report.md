# Phase C 第六批身份解析报告（第 191-210 页）

> 本批因 file-agent 派发连接不稳定，由主 Agent 直接基于审计工具数据 + 页面内容完成身份判定（只读，未修改任何页面）。

## 身份判定表

| # | 路径 | 身份 | 判定依据 |
| :-- | :-- | :-- | :-- |
| 191 | concepts/curvature-effect | short-aggregation | 曲率效应有效概念，仅 Wei2021 一篇 CNT 证据 |
| 192 | concepts/d-band-center | short-aggregation | d 带中心有效概念，Li2013bonding/Wei2021 证据 |
| 193 | concepts/d-orbital-hopping | short-aggregation | d 轨道跳跃有效概念，xun2024 证据 |
| 194 | concepts/d-p-hybridization | short-aggregation | d-p 杂化有效概念，gao2024 证据 |
| 195 | concepts/d-pi-a-architecture | short-aggregation | D-π-A 架构有效概念，5 篇论文；别名簇中心（d-pi-a-structure/donor-acceptor-push-pull/donor-pi-acceptor/push-pull-chromophore） |
| 196 | concepts/d0-magnetism | short-aggregation | d0 磁性有效概念，wang2025 证据 |
| 197 | concepts/d0-rule | short-aggregation | d0 规则有效概念，6 篇论文 |
| 198 | concepts/d1-electronic-configuration | short-aggregation | d1 电子构型有效概念，wong 证据 |
| 199 | concepts/dangling-bond-floating-bond | short-aggregation | 悬挂键/浮动键有效概念，kresse1994 证据 |
| 200 | concepts/davydov-soliton | short-aggregation | Davydov 孤子有效概念，forner1993 证据 |
| 201 | concepts/dbscan-clustering | short-aggregation | DBSCAN 聚类有效概念，yan2025 反链弱相关需核实 |
| 202 | concepts/debinding | short-aggregation | 脱脂工艺有效概念，Kotz2021 证据 |
| 203 | concepts/debye-screening-length | short-aggregation | 德拜屏蔽长度有效概念，sharma2019 证据 |
| 204 | concepts/defect-engineering | short-aggregation | 缺陷工程有效概念，martin2016/niu2021 证据 |
| 205 | concepts/defect-mediated-luminescence | short-aggregation | 缺陷介导发光有效概念，Gulhare2021 证据 |
| 206 | concepts/deformation-potential | short-aggregation | 形变势有效概念，peng2020/yan2025 证据 |
| 207 | concepts/density-functional-theory | canonical | 成熟页（mature），完整定义+机制+参数 |
| 208 | concepts/density-of-states | short-aggregation | 态密度有效概念，13 篇论文但无正文，canonical 候选 |
| 209 | concepts/depletion-layer-readout | short-aggregation | 耗尽层读出有效概念，Chen2016electrical 证据 |
| 210 | concepts/depletion-layer | short-aggregation | 耗尽层有效概念，3 篇论文 |

## 类别汇总

| 身份类型 | 数量 |
| :-- | :-- |
| canonical | 1 |
| short-aggregation | 19 |
| alias / ambiguous / misplaced / no-evidence | 0 |

## 问题清单

1. **跨层碰撞**：无新增（仍为 Phase A 已知 3 对）
2. **规范化名称重复**：无
3. **缩写/变体**：d-pi-a-architecture 为 D-π-A 架构别名簇中心（d-pi-a-structure、donor-acceptor-push-pull、donor-pi-acceptor、push-pull-chromophore 均指向它）
4. **父子概念**：d0-rule 与 d0-magnetism 同族；d-band-center 与 d-orbital-hopping、density-of-states 相关
5. **歧义词**：无
6. **跨层误放**：无
7. **无证据页**：无
8. **反链弱相关**：dbscan-clustering ← yan2025（DBSCAN 聚类与 III-V 半导体稳定性关系弱，需核实）

## 说明

- 本批 20 页全部位于 concepts 层
- 未修改任何页面，未提交，保护集合未触碰
- 下一批从第 211 页（concepts/depletion-region 或按字母序下一项）开始
