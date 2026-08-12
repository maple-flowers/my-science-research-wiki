#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enrich wiki/figures leaf entries with 关键特征 pulled from raw/note 图表解析.

For each image embed in wiki/figures/*.md (leaf pages):
  1. parse its path -> <citekey>/<filename>
  2. read raw/figures/<citekey>/manifest.json, find the figure entry by file,
     take the real label from llm_description ("Figure X.Y:" / "Fig. N:" etc.)
  3. open raw/note/<citekey>.md and locate the caption section whose header
     contains that figure number (图N / 图表 N.M / Figure N)
  4. extract a concise 关键特征 sentence from the caption body
  5. (apply mode) insert it right after the 来源 line if no 关键特征 present

Dry run by default; pass --apply to write. Never uses newline="\n".
"""
import re, json, glob, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FIG_DIR = os.path.join(ROOT, "wiki", "figures")
NOTE_DIR = os.path.join(ROOT, "raw", "note")
RAWFIG_DIR = os.path.join(ROOT, "raw", "figures")

APPLY = "--apply" in sys.argv

def strip_bq(line):
    # raw notes are block-quoted with leading '> '
    return line.lstrip().lstrip(">").lstrip()

def load_manifest_index(citekey):
    """Return {filename: real_label_text} from manifest llm_description."""
    mp = os.path.join(RAWFIG_DIR, citekey, "manifest.json")
    out = {}
    if not os.path.exists(mp):
        return out
    try:
        m = json.load(open(mp, encoding="utf-8"))
    except Exception:
        return out
    for key in ("figures", "tables", "formulas"):
        for f in m.get(key, []):
            fn = f.get("file")
            if not fn:
                continue
            desc = (f.get("llm_description") or "").strip()
            out[fn] = desc
    return out

LABEL_RE = re.compile(r'(?:Figure|Fig\.?|FIG\.?|Table|Tab\.?)\s*([A-Z]?\d+(?:\.\d+)?)', re.I)

def extract_label(desc):
    """Return normalized label tokens to match, e.g. '5.10' or '3'."""
    if not desc:
        return []
    m = LABEL_RE.search(desc)
    if not m:
        # maybe starts with a bare number
        m = re.match(r'\s*([A-Z]?\d+(?:\.\d+)?)', desc)
        if not m:
            return []
    return [m.group(1)]

def find_caption(note_text, labels):
    """Find a caption block in note. Returns cleaned concise text or None."""
    lines = note_text.splitlines()
    n = len(lines)
    for i, line in enumerate(lines):
        s = strip_bq(line).strip()
        mh = re.match(r'^#{2,6}\s*(.+?)\s*$', s)
        if not mh:
            continue
        head = mh.group(1)
        # must look like a figure header
        if not re.search(r'(图\s*表?|Figure|Fig\.?|FIG\.?)\s*[A-Z]?\d', head):
            continue
        for lab in labels:
            # match label, allowing 图3 / 图 3 / 图表 3 / Figure 3 / 3.x
            # boundary: after the number must NOT be a digit or .digit (avoids 3 matching 3.7)
            patterns = [
                r'图\s*表?\s*0*' + re.escape(str(lab)) + r'(?![\d.])',
                r'(?:Figure|Fig\.?|FIG\.?)\s*0*' + re.escape(str(lab)) + r'(?![\d.])',
            ]
            if any(re.search(p, head) for p in patterns):
                body = collect_body(lines, i + 1)
                return summarize(body)
    return None

def collect_body(lines, start):
    """Collect following blockquote/body lines until next same-or-higher header."""
    body = []
    for j in range(start, len(lines)):
        s = strip_bq(lines[j]).strip()
        if re.match(r'^#{2,6}\s+', s):
            break
        if s.startswith("---") or s.startswith("***"):
            break
        body.append(s)
    return "\n".join(body).strip()

def summarize(body):
    """Pull the most informative line: prefer tagged key-info, then a
    (a)-panel content bullet, then any substantive bullet/prose line."""
    if not body:
        return None
    lines = [clean_inline(l) for l in body.splitlines()]
    lines = [l for l in lines if l and not l.startswith(("---", "***"))]
    TAG = r'(核心信息|关键(信息|特征|结论|证据)|主要结论|结论|要点|物理意义|图像说明)'
    for l in lines:
        if re.match(r'^[-*]?\s*\**' + TAG + r'\**[:：]', l):
            t = clean_bullet(l)
            if t and len(t) >= 8:
                return t
    for l in lines:
        if re.match(r'^[-*]?\s*\**\(?[a-e]\)?[.、)：:]?\s*\**[^*：:]{2,20}\**[:：]\s*\S', l):
            return clean_bullet(l)
    for l in lines:
        if re.match(r'^[-*]', l) and len(l) >= 14 and not re.match(r'^(类型|Type)[:：]', l):
            return clean_bullet(l)
    for l in lines:
        if not (l.startswith("_") and l.endswith("_")) and len(l) >= 14 and not re.match(r'^(类型|Type|注[:：])', l):
            return l
    return None

def clean_bullet(l):
    l = re.sub(r'^[-*]\s*', '', l)
    l = re.sub(r'\*\*([^*]+)\*\*', r'\1', l)
    l = re.sub(r'^[^：:]{1,16}[:：]\s*', '', l)
    return clean_inline(l)

def clean_inline(t):
    t = t.strip().strip('*').strip()
    t = t.replace("**", "").replace("__", "").replace("`", "")
    if t.startswith("_") and t.endswith("_") and t.count("_") >= 2:
        t = t[1:-1]
    t = re.sub(r'\s+', ' ', t).strip()
    if len(t) > 240:
        t = t[:237].rstrip() + "…"
    return t

IMG_RE = re.compile(r'!\[[^\]]*\]\((\.\./\.\./raw/figures/([^/]+)/([^)]+))\)')
SRC_RE = re.compile(r'^(\s*\*\s*\*\*来源\*\*[:：].*)$', re.M)
HAS_KF = re.compile(r'\*\*(关键特征|看图要点)\*\*')

def process_page(path, stats):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    # only leaf-ish pages with embeds; skip pure hubs (few/no embeds) handled by callers
    out = text
    offset = 0
    page_changes = 0
    for m in IMG_RE.finditer(text):
        citekey = m.group(2)
        fn = m.group(3)
        # find block end: next ### or next image or ---
        start = m.end()
        # look at the window after this embed for 来源/关键特征
        nxt = re.search(r'\n### |\n!\[|\Z', text[start:])
        block_end = start + nxt.start() if nxt else len(text)
        block = text[start:block_end]
        if HAS_KF.search(block):
            stats["already"] += 1
            continue
        src = SRC_RE.search(block)
        if not src:
            stats["nosrc"] += 1
            continue
        # map
        idx = manifest_cache.get(citekey)
        if idx is None:
            idx = load_manifest_index(citekey)
            manifest_cache[citekey] = idx
        desc = idx.get(fn)
        labels = extract_label(desc)
        if not labels:
            stats["nolabel"] += 1
            continue
        note_path = os.path.join(NOTE_DIR, citekey + ".md")
        if not os.path.exists(note_path):
            stats["nonote"] += 1
            continue
        note_text = note_cache.get(citekey)
        if note_text is None:
            note_text = open(note_path, encoding="utf-8", errors="ignore").read()
            note_cache[citekey] = note_text
        cap = find_caption(note_text, labels)
        if not cap:
            stats["nocap"] += 1
            if stats["nocap"] <= 25:
                stats["nocap_ex"].append(f"{citekey}/{fn} labels={labels} desc={desc[:50]}")
            continue
        # insert after source line
        src_line = src.group(1)
        indent = re.match(r'^(\s*)', src_line).group(1)
        new_line = f"{indent}*   **关键特征**：{cap}"
        replacement = src_line + "\n" + new_line
        # perform on out with position tracking
        abs_src_start = offset + src.start()
        abs_src_end = offset + src.end()
        out = out[:abs_src_start] + replacement + out[abs_src_end:]
        offset += len(replacement) - (src.end() - src.start())
        page_changes += 1
        stats["added"] += 1
    if APPLY and page_changes:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(out)
    return page_changes

manifest_cache = {}
note_cache = {}
stats = {"added": 0, "already": 0, "nosrc": 0, "nolabel": 0, "nonote": 0, "nocap": 0, "nocap_ex": []}

for f in sorted(glob.glob(os.path.join(FIG_DIR, "*.md"))):
    n = process_page(f, stats)
    if n:
        print(f"[{'APPLY' if APPLY else 'DRY '}] {os.path.basename(f)}: {n} added")

print("\n=== summary ===")
for k, v in stats.items():
    if k != "nocap_ex":
        print(f"{k}: {v}")
if stats["nocap_ex"]:
    print("\n-- sample unmatched --")
    for e in stats["nocap_ex"]:
        print("  ", e)
