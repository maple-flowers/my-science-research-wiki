# 计划：通过开放 API 批量导入 7 个项目文献池至 Zotero 并在科研 Wiki 同步

## Context (背景)
用户要求为 Scientific Wiki 中的 7 个核心科研项目（Project 1 至 Project 7）各配置至少 50 篇专业文献（总计 350+ 篇）。由于 Google Scholar 的网页端存在严格的 CAPTCHA / 429 限制，无法用 Playwright 直接稳定抓取；故我们采用开放学术图谱 API (OpenAlex) 批量检索各领域的 Top 50 高关联性论文（优先考虑 Review 与 High-impact original papers），并利用 Zotero API 直接写入 7 个子文献池文件夹中，最终联动更新项目的 Wiki 文档。

## 关键文件与位置
- 新增/修改脚本：`E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\tools\populate_zotero_pools.py`
- 修改项目与Wiki文件：
  - `E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\wiki\projects\project-5-in2se3-lammps-potential.md` 重命名为 `project-5-snte-pbte-superlattice-lammps.md` 并修改内容。
  - `E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\wiki\projects\project-1-two-photon.md` 等其他 6 个项目卡片。
  - `E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\index.md` 中的链接指向更新。
- 记录日志：`E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\log.md`

## 详细执行方案

### 阶段 1：开发与更新 Zotero 文献池自动注入脚本
修改 `tools/populate_zotero_pools.py`，实现以下逻辑：
1. **API 检索逻辑**：
   - 使用 `Crossref` 检索接口（原脚本已使用 Crossref）。
   - 过滤条件：无/直接通过 API 限制条数。
2. **检索查询词定义**：
   - **P01** (MMAD3PQB): `"two-photon polymerization" OR "two-photon photoluminescence"`
   - **P02** (PTX5TBVQ): `("BiFeO3" OR "multiferroic") AND "polarization switching"`
   - **P03** (BCFMXHAU): `"mechanoluminescence" OR "piezoluminescence"`
   - **P04** (ZQUX2PP6): `"tetrathiafulvalene" OR "TTF" "charge transfer"`
   - **P05** (K9PXCWF9): `("SnTe" OR "PbTe" OR "tin telluride" OR "lead telluride") AND ("superlattice" OR "polarization" OR "skyrmion" OR "Kittel" OR "LAMMPS" OR "Deep Potential" OR "molecular dynamics")` (修正为 SnTe/PbTe 超晶格极化与势函数检索式)
   - **P06** (7Z2S985G): `"humidity sensor" AND "optical bandgap"`
   - **P07** (WMIAAIAE): `"charge density wave" AND ("Fermi surface nesting" OR "transition metal dichalcogenides")`
3. **Zotero 入库**：
   - 编写批量入库代码，利用 Zotero API 接口直接将检索到的 350+ 篇文献（各 50 篇以上）自动写入 Zotero 的 7 个 Collection 对应的 key 中。

### 阶段 2：运行与数据校验
1. 运行修改后的 `populate_zotero_pools.py`，拉取正确的文献并写入本地缓存 `openalex_papers.json`（文件名虽为 openalex，但内含 Crossref 抓取数据）。
2. 调用 Python 脚本或 Zotero 接口，自动批量入库，确保每个 Collection 的文献数目均满足 $\ge 50$ 篇的标准。

### 阶段 3：更新项目 Wiki 卡片与全局索引
1. 重命名 `project-5-in2se3-lammps-potential.md` 为 `project-5-snte-pbte-superlattice-lammps.md`，更新其中的标题、简介、物理概念（关联 SnTe/PbTe、极化拓扑态、Kittel 等）、本地路径及参考文献池。
2. 更新 `index.md`，把项目五的链接修改为指向 `wiki/projects/project-5-snte-pbte-superlattice-lammps`。
3. 读取 Zotero 文献库各 Collection 的入库数据，更新 `wiki/projects/project-*.md` 文件的 `## 3. Zotero 参考文献池积累` 部分，以 Markdown 列表格式列出这 50 篇的核心代表性文献（包含 Title、Author、Year、DOI 链接）。
4. 在 `log.md` 中记录本次文献池构建、P05 体系变更及 Wiki 项目同步日志。

## 验证与测试
- 运行同步脚本，确认终端无报错输出，且输出各 Collection 入库文献的成功计数。
- 在 Zotero 客户端或 Zotero 网页版中查看 7 个子文献池的内容是否已填充完毕。
- 检查 `wiki/projects/` 下 7 个项目 markdown 文件的更新情况，验证链接有效性。
