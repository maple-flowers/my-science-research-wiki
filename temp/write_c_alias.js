const content = `---
tags: [carbon-material, glassy-carbon]
title: glassy-carbon
type: concepts
status: stub
aliases: ["玻碳", "玻璃碳"]
updated: 2026-08-18
---

# glassy-carbon

玻碳（glassy carbon / 玻璃碳）是**一种非晶态碳材料**，兼具玻璃的硬度和碳材料的导电性，常用作电化学电极基底材料。由于该名称具体指代一种碳材料实体，其规范页已迁移至实体层。

## 👵 太奶导读

乖孙，这一条是别名说明页。「glassy-carbon（玻碳/玻璃碳）」是一种非晶态碳材料，常作电极用，它是一类具体的材料实体，规范内容在实体页里，从本页跳过去看就行。

## 名称与使用范围

- **规范页**：[[../entities/glassy-carbon|glassy-carbon（实体页）]]
- **使用范围**：Doroodmand2017 论文中用作电合成共轭 Salen 聚合物的电极基底，属具体材料实体，故归入实体层。

## 容易混淆的对象

- [[../concepts/conjugated-polymer|conjugated-polymer]]：共轭聚合物是通用机制/概念；玻碳本身是承载该聚合物的电极材料实体。

## 📚 相关论文 (Related Papers)

- [[../papers/Doroodmand2017conjugated]]：提出了水致变色反射滤光片的新概念并应用于湿度传感。
`;
app.vault.adapter.write('科研Wiki/wiki/concepts/glassy-carbon.md', content).then(function(r) { return 'C_CONCEPTS_ALIAS_WRITTEN'; });
