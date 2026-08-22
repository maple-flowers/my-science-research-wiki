# Plan - Update Paper Wiki Entry Format

The user wants to update the frontmatter of a specific paper wiki entry by changing standard YAML key-value pairs for content fields into Dataview-style inline fields (using `::`) while preserving the YAML multiline scalar markers (`>-`).

## User Request
- File: `E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/wiki/papers/zhangNonvolatileControlTopological2025.md`
- Fields to update: `领域基础知识`, `研究背景`, `作者的问题意识`, `主要研究对象`, `主要研究方法`, `研究意义`, `研究结论`, `对领域的贡献`, `未来研究方向提及`, `未来研究方向思考`
- Format change: `"Field": >-` -> `Field:: >-`
- Goal: Return the full updated content.

## Steps
1. **Read file**: Read the content of `E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/wiki/papers/zhangNonvolatileControlTopological2025.md`. (Completed)
2. **Transform content**:
    - Iterate through the lines.
    - For each of the specified fields, locate the line starting with `"Field": >-` (or `|-`).
    - Replace it with `Field:: >-` (or `:: |-`).
3. **Return result**: Provide the complete file text with the applied changes.

## Proposed Changes
- Line 19: `"领域基础知识": >-` -> `领域基础知识:: >-`
- Line 21: `"研究背景": >-` -> `研究背景:: >-`
- Line 23: `"作者的问题意识": >-` -> `作者的问题意识:: >-`
- Line 25: `"主要研究对象": >-` -> `主要研究对象:: >-`
- Line 27: `"主要研究方法": >-` -> `主要研究方法:: >-`
- Line 29: `"研究意义": >-` -> `研究意义:: >-`
- Line 31: `"研究结论": >-` -> `研究结论:: >-`
- Line 33: `"对领域的贡献": >-` -> `对领域的贡献:: >-`
- Line 35: `"未来研究方向提及": >-` -> `未来研究方向提及:: >-`
- Line 37: `"未来研究方向思考": >-` -> `未来研究方向思考:: >-`

All other content will remain unchanged.
