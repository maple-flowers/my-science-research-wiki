---
tags: [concept]
title: '最陡上升路径 / Steepest Ascent Path'
type: concept
status: developing
papers: ['tangGridbasedBaderAnalysis2009']
updated: 2026-08-18
---

# 最陡上升路径 / Steepest Ascent Path

最陡上升路径（steepest ascent path）是**最陡上升法（[[../concepts/steepest-ascent|steepest-ascent]]）**的完整拼写形式（加 -path），指沿标量场（如电子电荷密度）梯度方向连续上升、直至到达临界点（原子核或键临界点）的路径。

## 👵 太奶导读

太奶，最陡上升路径就是"顺着坡一直往上走的路"：在电子云密度这张"地形图"里，从密度最低处沿最陡的方向往上爬，最后停在山顶（原子核）或山口（键鞍点）。Bader 电荷分析靠它来给原子"圈地盘"。

## 📛 名称与使用范围

- **规范名**：steepest-ascent（concepts 页）
- **别名**：steepest-ascent-path
- **使用范围**：Bader 电荷密度分析、临界点搜索、优化算法中"沿最陡方向上升/下降"的路径术语。

## ⚠️ 容易混淆的对象

- **steepest-descent（最陡下降）**：方向相反，用于极小值搜索。
- **gradient-path（梯度路径）**：与之含义相近的另一表述。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/steepest-ascent|最陡上升法]]：本页的规范名，Bader 分析中沿电荷密度梯度上升的数值方法。
- [[../concepts/bader-analysis|Bader 电荷分析]]：使用最陡上升路径划分原子电荷区域的框架。

## 📚 相关论文 (Related Papers)

- [[../papers/tangGridbasedBaderAnalysis2009]] — A grid-based Bader analysis algorithm without lattice bias（网格 Bader 分析基于最陡上升路径定位临界点）

## 🔗 规范页 (Canonical Page)

- [[../concepts/steepest-ascent|steepest-ascent]]：本页所指的标准条目。
