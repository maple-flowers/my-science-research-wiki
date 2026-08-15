---
tags:
  - type/ideas-index
---

# 研究想法库 (Research Ideas)

> 记录领域空白、验证想法可行性、产生 research idea 的地方。把"读论文时一闪而过的灵感"沉淀为可追踪、可验证、可落地的结构化卡片。

[[科研Wiki/index|← 返回 Wiki 总索引]] · [[format-spec|想法条目编写规范]]

---

## 本目录是什么

`wiki/ideas/` 是科研 Wiki 的「研究想法层」，回答三个问题：

| 条目类型 | 回答的问题 | 文件名前缀 | 说明 |
| :--- | :--- | :--- | :--- |
| 🕳️ 领域空白 gap | 还有什么是没人做/没做透的？ | `gap-` | 从文献综述中发现的开放问题 |
| 💡 研究想法 idea | 我打算怎么补这个空白？ | `idea-` | 针对 gap 提出的可验证假设与方案 |
| 🔬 可行性验证 validation | 这个想法到底行不行？ | `validation-` | 对 idea 的验证尝试与结论 |
| 🧭 科研范式 paradigm | 这类研究是怎么做的？ | `paradigm-` | 从论文中提炼可复用的研究套路与方法论模板 |

四者关系：**gap 是问题 → idea 是假设 → validation 是证据**；idea 验证通过后可 `adopted` 落地为 `wiki/projects/` 项目，否定则 `rejected` 废弃。**paradigm 是方法**：从论文中提炼"这类研究怎么做"，为 gap / idea 提供可复用的研究套路与流程模板。

---

## 想法生命周期

```
gap        : open ─────────────────────────────▶ filled（被 idea 或 project 填补）
idea       : proposed → validating → validated → adopted（落地 project）
                        │                         └ rejected（废弃）
                        └─────────────────────▶ superseded（被新 idea 替代）
validation : draft → in-progress → done / inconclusive
paradigm   : active ────────────────────────────▶ superseded（被新范式替代）
                        └─────────────────────▶ obsolete（过时废弃）
```

- `proposed`：想法刚提出，只有假设与大致方案。
- `validating`：正在做计算 / 实验 / 文献验证。
- `validated`：验证通过，想法被证明可行。
- `adopted`：已采纳并落地为 `wiki/projects/` 项目（正文须双链项目页）。
- `rejected`：验证否定，废弃（保留页面并写明否定原因）。
- `superseded`：被更新的 idea 替代（保留页面并链向新 idea）。

---

## 当前条目索引

当前共 **10 张 paradigm 卡片**（科研范式层已建立），尚无 gap / idea / validation 卡片。

| 类型 | 编号 | 标题 | 状态 | 关联主题 |
| :--- | :--- | :--- | :--- | :--- |
| 🧭 paradigm | P01 | [[paradigm-first-principles-material-design\|第一性原理材料设计预测]] | active | 材料模拟计算设计 / 多铁性材料 |
| 🧭 paradigm | P02 | [[paradigm-high-throughput-screening\|高通量筛选与数据驱动材料发现]] | active | 材料模拟计算设计 / 多铁性材料 |
| 🧭 paradigm | P03 | [[paradigm-method-development\|计算方法学开发与基准验证]] | active | 材料模拟计算设计 |
| 🧭 paradigm | P04 | [[paradigm-ml-potential-md\|机器学习势与大规模分子动力学模拟]] | active | 材料模拟计算设计 / 多铁性材料 |
| 🧭 paradigm | P05 | [[paradigm-phenomenological-theory\|唯象与解析理论建模]] | active | 多铁性材料 / 材料模拟计算设计 |
| 🧭 paradigm | P06 | [[paradigm-experiment-theory-loop\|实验-理论闭环]] | active | 多铁性材料 / 材料模拟计算设计 |
| 🧭 paradigm | P07 | [[paradigm-device-development\|器件开发与性能验证]] | active | 多铁性材料 |
| 🧭 paradigm | P08 | [[paradigm-microfabrication\|微纳加工与结构制备]] | active | —（尚无对应主题页） |
| 🧭 paradigm | P09 | [[paradigm-review-framework\|综述与领域框架构建]] | active | 多铁性材料 / 材料模拟计算设计 |
| 🧭 paradigm | P10 | [[paradigm-classical-mesoscale-simulation\|经典与介观尺度模拟]] | active | 多铁性材料 / 材料模拟计算设计 |

**范式层的读法**：P01–P04 是计算路线（从单点预测 → 批量筛选 → 方法本身 → 大尺度动力学），P05 是解析理论，P06 是实验与理论的会合点，P07–P08 是走向器件与加工的下游，P09 是把整个领域收敛成框架，P10 覆盖原子尺度之上的介观模拟。读一篇新论文时，先判断它属于哪一种范式，能快速定位它在领域中的位置。

> 下一步：从「读文献时发现的空白」开始，先建一张 `gap-*.md`，再围绕它提 `idea-*.md`，验证后补 `validation-*.md`。范式卡片可作为选择研究路线的模板。

---

## 使用指引

1. **先读规范**：[[format-spec|想法条目编写规范]] 定义了四种卡片的 frontmatter、正文模板、命名与双链规则。
2. **从 gap 开始**：每张 idea 必须锚定至少一个 gap；每张 validation 必须锚定一个 idea；每张 paradigm 必须锚定至少一篇代表论文。
3. **双链联动**：引用论文一律 `[[../papers/<citekey>]]`（不直链 `raw/note/`）；引用概念 / 实体 / 主题 / 项目用对应相对路径。
4. **落地闭环**：idea 被采纳后，把 `status` 改为 `adopted` 并双链 `[[../projects/project-1-two-photon|项目1]]`；同时在该 project 页的「与 Wiki 联系」回链 idea。
5. **想法是活的**：随验证推进更新 `status` 与「生命周期日志」，不必一次写全。
