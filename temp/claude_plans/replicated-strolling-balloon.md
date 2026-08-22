# 计划 — 科研Wiki图表库细化分类方案

## Context (上下文)
为了让科研Wiki的图表库检索更加精准，我们拟将当前的 3 个大类（结构图、能带图、器件结构图）细化拆分为 8 个更具针对性的物理概念与应用分类子库，同时更新总索引 `_index.md`，使用户能快速定位具体的结构、能谱与器件特征。

---

## 推荐方案与执行步骤

### 1. 定义细化分类子库与关键词
我们将图表拆分为以下 8 个概念库（保存在 `wiki/figures/` 下）：

#### 类别一：结构与原子构型 (Structural/Crystal diagrams)
1. **晶体结构与原子排布 (`crystal-structures.md`)**：
   - 晶体结构、原子排布、晶面、晶胞构型、晶格畸变、配位多面体等。
   - 关键词：`晶体结构`, `原子排布`, `晶格`, `晶面`, `胞`, `多面体`, `coordination`, `polyhedra`, `lattice distortion` 等。
2. **异质结与堆叠层 (`heterostructures-stacking.md`)**：
   - 异质结界面、层状堆叠、层间相对滑动、莫尔超晶格、扭角构型、单/双层。
   - 关键词：`堆叠`, `层间`, `莫尔`, `扭角`, `异质结`, `双层`, `单层`, `界面`, `stacking`, `interlayer`, `bilayer`, `monolayer`, `twist`, `moire`, `interface`, `heterostructure` 等。
3. **畴与畴壁结构 (`domain-walls.md`)**：
   - 铁电/铁磁畴、畴壁原子排布、畴壁宽度、极化翻转畴演变。
   - 关键词：`畴`, `畴壁`, `domain`, `wall`, `dw` 等。

#### 类别二：能带结构与能谱 (Band structures & Spectra)
4. **电子能带与电子态 (`electronic-bands.md`)**：
   - 电子能带结构、电子态密度 (DOS/PDOS)、能隙、费米面、能带对齐等。
   - 关键词：`能带`, `态密度`, `dos`, `pdos`, `能隙`, `带隙`, `费米`, `对齐`, `band structure`, `band gap`, `density of states` 等。
5. **振动能谱与声子谱 (`vibrational-spectra.md`)**：
   - 声子色散曲线、声子态密度、红外与拉曼活性振动模式等。
   - 关键词：`声子`, `振动`, `拉曼`, `红外`, `raman`, `phonon`, `dispersion`, `infrared` 等。
6. **光学与吸收光谱 (`optical-spectra.md`)**：
   - 介电函数、光学吸收谱、折射率、光电导率等。
   - 关键词：`光谱`, `吸收谱`, `吸收率`, `介电`, `反射`, `折射`, `光电导`, `absorption`, `optical spectrum`, `dielectric`, `reflectivity` 等。

#### 类别三：器件设计与实验/测量装置 (Device & Experimental schematics)
7. **电子与突触器件 (`electronic-devices.md`)**：
   - 铁电隧道结 (FTJ)、忆阻器、晶体管、类脑突触存储器件设计。
   - 关键词：`忆阻`, `突触`, `隧道结`, `晶体管`, `存储器`, `ftj`, `memristor`, `transistor`, `synaptic`, `memory` 等。
8. **实验测试与测量装置 (`experimental-setups.md`)**：
   - 实验测量原理图、测试电路、PFM/STM 测量系统、样品制备流程等。
   - 关键词：`实验`, `装置`, `测量`, `电路`, `测试`, `回路`, `setup`, `experimental`, `measurement`, `circuit`, `apparatus` 等。

---

### 2. 编写与运行细化生成脚本
编写 `tools/generate_figure_wiki_fine.py` 脚本：
- **匹配机制**：读取 `raw/figures/*/manifest.json` 下的图表，并在 `caption_zh`、`llm_description`、`tags` 中扫描对应子类的关键词。
- **关联链接**：将每个图表生成格式化条目，包含关联文献相对链接 `[[../../raw/note/NOTE_FILENAME]]`，说明图号、页码以及在文章中的作用。
- **自动清理旧的三个分类文件**：删除旧的 `structural-diagrams.md`、`band-structures.md`、`device-schematics.md`。
- **重新生成 `_index.md`**：展示细化后的 8 个分类导航矩阵。

### 3. 更新 `SCHEMA.md` 规范
- 修改目录结构定义与标签规范，说明细化后的 8 个图表分类及链接方式。

---

## 验证方法
1. **文件目录校验**：
   - 确认旧的 3 个分类文件已删除，且 `wiki/figures/` 下存在这 8 个新的 `.md` 文件和更新后的 `_index.md`。
2. **链接连通性检验**：
   - 抽查文件，确认链接路径 `[[../../raw/note/NOTE_FILENAME]]` 在 Obsidian 中可正常点击跳转。
3. **图表覆盖统计**：
   - 查看生成的 `_index.md` 确定每类提取出的图表数量，确认是否有合理的覆盖面。
