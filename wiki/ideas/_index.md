---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d1440e82f85676d2b3ce24ffb8efaf05_066f98b497e011f19467525400287e28
    ReservedCode1: eK1dqso85F0DeDhvBBjswM7zTQ8EoegZmRUOuaLU5j2W+doHxL5EoJfJ0O4gcg2sAor8932Lbur1e1wuTejG7nTNX93dZBK/ZlAhaEi4sbFEqv6Bl+T/1A2b4aScKzi6RDsBkGtbugbhykyL92YQZ1uuC9wRb6/GcXyzEkyQFz8dMMGhV0qyPEkKbYo=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d1440e82f85676d2b3ce24ffb8efaf05_066f98b497e011f19467525400287e28
    ReservedCode2: eK1dqso85F0DeDhvBBjswM7zTQ8EoegZmRUOuaLU5j2W+doHxL5EoJfJ0O4gcg2sAor8932Lbur1e1wuTejG7nTNX93dZBK/ZlAhaEi4sbFEqv6Bl+T/1A2b4aScKzi6RDsBkGtbugbhykyL92YQZ1uuC9wRb6/GcXyzEkyQFz8dMMGhV0qyPEkKbYo=
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

三者关系：**gap 是问题 → idea 是假设 → validation 是证据**；idea 验证通过后可 `adopted` 落地为 `wiki/projects/` 项目，否定则 `rejected` 废弃。

---

## 想法生命周期

```
gap        : open ─────────────────────────────▶ filled（被 idea 或 project 填补）
idea       : proposed → validating → validated → adopted（落地 project）
                        │                         └ rejected（废弃）
                        └─────────────────────▶ superseded（被新 idea 替代）
validation : draft → in-progress → done / inconclusive
```

- `proposed`：想法刚提出，只有假设与大致方案。
- `validating`：正在做计算 / 实验 / 文献验证。
- `validated`：验证通过，想法被证明可行。
- `adopted`：已采纳并落地为 `wiki/projects/` 项目（正文须双链项目页）。
- `rejected`：验证否定，废弃（保留页面并写明否定原因）。
- `superseded`：被更新的 idea 替代（保留页面并链向新 idea）。

---

## 当前条目索引

*本目录当前为空，尚无 gap / idea / validation 卡片。*

| 类型 | 编号 | 标题 | 状态 | 关联 |
| :--- | :--- | :--- | :--- | :--- |
| — | — | — | — | — |

> 首次使用：从「读文献时发现的空白」开始，先建一张 `gap-*.md`，再围绕它提 `idea-*.md`，验证后补 `validation-*.md`。

---

## 使用指引

1. **先读规范**：[[format-spec|想法条目编写规范]] 定义了三种卡片的 frontmatter、正文模板、命名与双链规则。
2. **从 gap 开始**：每张 idea 必须锚定至少一个 gap；每张 validation 必须锚定一个 idea。
3. **双链联动**：引用论文一律 `[[../papers/<citekey>]]`（不直链 `raw/note/`）；引用概念 / 实体 / 主题 / 项目用对应相对路径。
4. **落地闭环**：idea 被采纳后，把 `status` 改为 `adopted` 并双链 `[[../projects/project-N-slug|项目N]]`；同时在该 project 页的「与 Wiki 联系」回链 idea。
5. **想法是活的**：随验证推进更新 `status` 与「生命周期日志」，不必一次写全。
*（内容由AI生成，仅供参考）*
