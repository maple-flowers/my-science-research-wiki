---
name: projects-overview
description: 七大主线科研项目索引、知识库关联说明与文献池映射
---

# 核心科研项目索引 (Projects)

本目录为科研 Wiki 与本地七个核心科研项目的连接桥梁。通过本索引，明确各项目的物理存储位置、研究课题属性、知识库概念/实体链接以及对应的 Zotero 参考文献池。

---

## 知识库与科研项目的联动机制

1. **底层物理支撑**：项目的实际计算数据、模拟脚本（VASP/LAMMPS）与论文草稿存放在 `E:\swan_goose\燕燕\香香\` 目录下。
2. **理论与知识沉淀**：科研 Wiki 中的概念卡片 (`wiki/concepts/`)、材料实体 (`wiki/entities/`)、方法总结与图表库 (`figures/`) 为各项目提供物理机制解释与模拟方法支持。
3. **参考文献闭环**：每个项目在 Zotero 中均建立专属的子文献池（父分类：`科研项目文献池 [C7ZJV399]`）。当在 Zotero 中完成文献抓取与元数据更新后，LLM 将自动提取文献分析并更新至各项目卡片中。

---

## 七大项目卡片列表

| 项目编号 | 项目名称 | 知识库核心链接 | Zotero 文献池 Key | 物理路径 |
| :--- | :--- | :--- | :--- | :--- |
| [[project-1-two-photon|项目一]] | 双光固化和双光发光 | [[../../wiki/concepts/2D-materials\|二维材料]] | `MMAD3PQB` | `E:\swan_goose\燕燕\香香\项目一：双光固化和双光发光` |
| [[project-2-mn-multiferroics|项目二]] | Mn极化结构铁电材料 | [[../../wiki/concepts/multiferroicity\|多铁性]], [[../../wiki/entities/BiFeO3\|BiFeO3]] | `PTX5TBVQ` | `E:\swan_goose\燕燕\香香\项目二：Mn极化结构铁电材料` |
| [[project-3-topological-devices|项目三]] | 拓扑量子器件 | [[../../wiki/concepts/altermagnetism\|变换磁性]], [[../../wiki/concepts/sliding-ferroelectricity\|滑动铁电]] | `TQD2026X` | `E:\swan_goose\燕燕\香香\项目三：拓扑量子器件` |
| [[project-4-ttf-molecular-calc|项目四]] | lsl老师的ttf分子计算 | [[../../wiki/entities/deep-potential\|Deep Potential]] | `ZQUX2PP6` | `E:\swan_goose\燕燕\香香\项目四：lsl老师的ttf分子计算` |
| [[project-5-snte-ferroelectric-sim|项目五]] | lammps势函数SnTe铁电模拟 | [[../../wiki/entities/SnTe\|SnTe]], [[../../wiki/concepts/sliding-ferroelectricity\|滑动铁电]] | `K9PXCWF9` | `E:\swan_goose\燕燕\香香\项目五：lammps势函数SnTe铁电模拟` |
| [[project-6-humidity-sensor|项目六]] | 小花闻的电压湿度传感器 | [[../../wiki/concepts/2D-materials\|二维材料]] | `7Z2S985G` | `E:\swan_goose\燕燕\香香\项目六：小花闻的电压湿度传感器` |
| [[project-7-cdw-charge-density-wave|项目七]] | CDW电荷密度波 | [[../../wiki/concepts/magnetoelectric-coupling\|磁电耦合]] | `WMIAAIAE` | `E:\swan_goose\燕燕\香香\项目七：CDW电荷密度波` |

---

## 自动化更新交互说明

当您在 Zotero 的 `科研项目文献池` 或其子文件夹中添加、抓取了新的文献及元数据后，只需对我说一声：
> “**帮我更新科研wiki**”

我将自动检索 Zotero 对应项目 Collection 中的最新文献，解析其摘要与元数据，更新各项目的主题文献关联与知识体系。
