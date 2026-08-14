---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d1440e82f85676d2b3ce24ffb8efaf05_e7cc02eb979e11f19467525400287e28
    ReservedCode1: Wscc7Zg80Xqbl5j0Uf7U6joV2iV72gdBsKnmBIZSzJ3yQsmqeQTjcSIP6uUDEJfLAaaOcbc9MEi85tT0H02tZVwQG1uLMpk7KXHnP4Mq9sESSg2Y3MEXQUkEd6r9zajNcvKk9MbjfGHDCf3GlTjQTQwnfsTd4zu9NXWwXyUPiR7IivNhl7H4FgDNoL4=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d1440e82f85676d2b3ce24ffb8efaf05_e7cc02eb979e11f19467525400287e28
    ReservedCode2: Wscc7Zg80Xqbl5j0Uf7U6joV2iV72gdBsKnmBIZSzJ3yQsmqeQTjcSIP6uUDEJfLAaaOcbc9MEi85tT0H02tZVwQG1uLMpk7KXHnP4Mq9sESSg2Y3MEXQUkEd6r9zajNcvKk9MbjfGHDCf3GlTjQTQwnfsTd4zu9NXWwXyUPiR7IivNhl7H4FgDNoL4=
---

# 项目三名称统一与 Unknown 年份修复报告

- 生成时间：2026-08-14
- 知识库根目录：`E:\swan_goose\宝宝\笔记库\sgg\科研Wiki`

## 一、修复结果总览

| 任务 | 状态 | 修复处数 |
| :--- | :--- | ---: |
| 项目三名称统一为「应力发光神经网络」 | 完成 | 3 |
| Unknown 年份映射修复 | 完成 | 3 |

全库悬空引用：221 → 220（chowdhury 的 `../write/Unknown` 已消除）。

## 二、任务①：项目三名称统一

### 2.1 修改明细（projects/index.md，共 3 处）

| 位置 | 修改前 | 修改后 |
| :--- | :--- | :--- |
| 项目名称列 | 拓扑量子器件 | 应力发光神经网络 |
| 物理路径列 | `E:\swan_goose\燕燕\香香\项目三：拓扑量子器件` | `E:\swan_goose\燕燕\香香\项目三：应力发光神经网络` |
| Zotero 文献池 Key | `TQD2026X` | `BCFMXHAU` |

其中 Zotero Key 的修正依据为 `projects/project-3-mechanoluminescence-nn.md` frontmatter 中的 `zotero_collection_key: BCFMXHAU`，保证索引与项目文件数据一致。

### 2.2 保持原样项说明

`papers/pedramraziManipulatingTopologicalDomain2019.md` 正文中出现的「拓扑量子器件」（1 处）保持原样，原因：
- 该论文 frontmatter `projects: [project-5]`，归属项目五（SnTe 铁电模拟），与项目三无关；
- 该处出现在"对领域的贡献"段落（"为拓扑量子器件的设计开辟了新路径"），属物理学科领域通用术语，而非项目名称。

### 2.3 slug 引用核验

`project-3-topological-devices` 旧 slug 全库已 0 处（上一轮已修正），`project-3-mechanoluminescence-nn` 共 13 处引用全部有效，无需改动。

## 三、任务②：Unknown 年份映射

### 3.1 修改明细（共 3 处）

| 文件 | 修改前 | 修改后 | 依据 |
| :--- | :--- | :--- | :--- |
| `format-spec.md` | 无年份论文归入 `Unknown.md` | 无年份论文归入 `1945-1999.md`（最早时间段） | 任务要求映射到最早时间段 |
| `write/_index.md` | 含 `Unknown` 占位行 | 删除该行（1945–1999 段已存在） | Unknown 分类不再需要 |
| `papers/chowdhuryReviewTheoreticalComputational.md` | `[[../write/Unknown]]（笔记元数据 date 为 NaN；按参考文献推断可补入 2021/2022）` | `[[../write/2020-2024\|2022]]` | frontmatter `year: 2022` |

### 3.2 决策说明（chowdhury）

chowdhury 论文的正文链接 `[[../write/Unknown]]` 经核查属于**历史笔误**：frontmatter 中 `year: 2022` 为权威数据，且正文注释本身已写明"按参考文献推断可补入 2021/2022"。因此按真实年份归入 `2020-2024` 段（而非按字面映射到最早段 `1945-1999`），避免 2022 年综述被误归入奠基性文献段。

若确需强制按任务字面将其归入 `1945-1999`，可再次调整。

### 3.3 说明：Unknown 前缀论文

全库存在 5 个以 `Unknown` 为作者前缀的论文文件（`Unknown2003charge`、`Unknown2014optical`、`Unknown2014passive`、`Unknown2022polymerization`、`Unknown2025diffractive`），其 `Unknown` 表示**作者未知**而非年份未知，各文件 frontmatter 均有具体年份，且引用的 `[[../papers/UnknownYYYY...]]` 链接均有效，不在本任务范围，未做改动。

## 四、备份信息

修复前文件已备份至：
`E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\temp\fix_backup_names_unknown_20260814\`
（共 4 个文件：projects/index.md、write/_index.md、format-spec.md、papers/chowdhuryReviewTheoreticalComputational.md）

## 五、验证

- 「拓扑量子器件」残留：仅 pedramrazi 论文科学术语 1 处（预期保持原样）。
- `write/Unknown` 悬空引用：0 处（已消除）。
- `project-3-topological-devices` 旧 slug：0 处。
- 全库悬空引用：221 → 220。
*（内容由AI生成，仅供参考）*
