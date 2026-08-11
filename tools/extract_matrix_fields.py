"""Extract the 10 literature-matrix fields from every raw/note/*.md.

Each note contains a blockquoted region of the form:
    > 领域基础知识:: ... 研究背景:: ... 作者的问题意识:: ... 主要研究对象:: ...
    > 主要研究方法:: ... 研究意义:: ... 研究结论:: ... 对领域的贡献:: ...
    > 未来研究方向提及:: ... 未来研究方向思考:: ...

The fields may live on one physical line or span several blockquoted lines.
We locate the FIRST occurrence of "领域基础知识::" after a blockquote marker,
then collect following blockquoted lines until a line that no longer continues
the block (blank line, new heading, non-">" line). Fields are then split with
a regex that looks ahead for the next "  字段名:: " delimiter.

Output: tools/ingest_papers/_matrix.json  — {citekey: {field: text, ...}}
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NOTES = REPO / "raw" / "note"
OUT = REPO / "tools" / "ingest_papers" / "_matrix.json"

FIELDS = [
    "领域基础知识",
    "研究背景",
    "作者的问题意识",
    "主要研究对象",
    "主要研究方法",
    "研究意义",
    "研究结论",
    "对领域的贡献",
    "未来研究方向提及",
    "未来研究方向思考",
]

ALT = {
    "对领域的贡献": ("对领域的贡献", "对本领域的贡献", "领域贡献"),
    "作者的问题意识": ("作者的问题意识", "问题意识"),
}


def collect_block(lines: list[str], start: int) -> str:
    """Collect contiguous blockquoted lines starting at `start`."""
    buf: list[str] = []
    i = start
    while i < len(lines):
        ln = lines[i].rstrip("\n")
        stripped = ln.lstrip()
        if not stripped.startswith(">"):
            break
        # strip one leading ">" and optional space
        content = stripped[1:].lstrip()
        buf.append(content)
        i += 1
    return " ".join(buf).strip()


def find_block(text: str) -> str | None:
    lines = text.splitlines()
    for idx, ln in enumerate(lines):
        if "领域基础知识::" in ln and ln.lstrip().startswith(">"):
            return collect_block(lines, idx)
    # fallback: find un-blockquoted (some notes may have it without >)
    for idx, ln in enumerate(lines):
        if "领域基础知识::" in ln:
            return collect_block(lines, idx)
    return None


def split_fields(block: str) -> dict[str, str]:
    """Split a block like 'A:: x  B:: y  C:: z' into {A: x, B: y, C: z}."""
    # Build alternation of all known field labels (longest first so that
    # "对领域的贡献" matches before any shorter prefix).
    labels = sorted({alt for alts in ALT.values() for alt in alts} | set(FIELDS),
                    key=len, reverse=True)
    # Allow either "::" or ":" as the field separator — some notes use a single
    # colon for the later fields (对领域的贡献 / 未来研究方向提及 / 未来研究方向思考).
    pat = re.compile(r"\s*(" + "|".join(re.escape(l) for l in labels) + r")::?\s*")
    matches = list(pat.finditer(block))
    result: dict[str, str] = {}
    canonical = {}
    for canon, alts in ALT.items():
        for a in alts:
            canonical[a] = canon
    for i, m in enumerate(matches):
        label = m.group(1)
        canon = canonical.get(label, label)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(block)
        value = block[start:end].strip()
        # keep the FIRST occurrence if a canonical field appears twice
        result.setdefault(canon, value)
    return result


def clean(value: str) -> str:
    value = value.replace("\n", " ").strip()
    value = re.sub(r"\s+", " ", value)
    return value


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    matrix: dict[str, dict[str, str]] = {}
    missing: list[str] = []
    for note in sorted(NOTES.glob("*.md")):
        citekey = note.stem
        text = note.read_text(encoding="utf-8", errors="replace")
        block = find_block(text)
        if not block:
            missing.append(citekey)
            matrix[citekey] = {}
            continue
        fields = split_fields(block)
        matrix[citekey] = {k: clean(v) for k, v in fields.items()}
        absent = [f for f in FIELDS if f not in matrix[citekey]]
        if absent:
            missing.append(f"{citekey} (缺: {', '.join(absent)})")
    OUT.write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding="utf-8")
    total = len(matrix)
    full = sum(1 for v in matrix.values() if len(v) == len(FIELDS))
    print(f"wrote {OUT.relative_to(REPO)}: {full}/{total} notes have all {len(FIELDS)} fields")
    if missing:
        print("notes needing attention:")
        for m in missing:
            print(f"  - {m}")


if __name__ == "__main__":
    main()
