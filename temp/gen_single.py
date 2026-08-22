# -*- coding: utf-8 -*-
"""单论文 stub 页生成器：从论文 raw/note 结构化字段生成规范自包含页"""
import os, re, yaml, json, sys

BASE = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
RAW_NOTE = os.path.join(BASE, "raw", "note")
PAPER_DIR = os.path.join(BASE, "wiki", "papers")
WIKI = os.path.join(BASE, "wiki")

FIELD_KEYS = ["领域基础知识","研究背景","作者的问题意识","主要研究对象","主要研究方法","研究意义","研究结论","对领域的贡献","未来研究方向提及","未来研究方向思考"]

def extract_field(txt, key):
    lines = txt.split("\n")
    cap = False; out = []
    for ln in lines:
        s = ln.strip()
        s2 = s[1:].strip() if s.startswith(">") else s
        m = re.match(r'^([\u4e00-\u9fa5A-Za-z][\u4e00-\u9fa5A-Za-z_]*)::(.*)$', s2)
        if m:
            k, rest = m.group(1), m.group(2).strip()
            if k == key:
                cap = True
                if rest: out.append(rest)
                continue
            else:
                if cap: break
                continue
        if cap and s2: out.append(s2)
    return "\n".join(out).strip()

def get_abstract_zh(txt):
    m = re.search(r'【摘要翻译】(.*?)(?=\n\n|\n\s*>?\s*\[!tldr\]|\Z)', txt, re.S)
    if m:
        return re.sub(r'^\s*>\s*','',m.group(1).strip(),flags=re.M).strip()
    return ""

def get_title_zh(txt):
    m = re.search(r'中文标题:\s*(.*)', txt)
    if m: return m.group(1).strip()
    return ""

def get_paper_fm(citekey):
    fp = os.path.join(PAPER_DIR, citekey+".md")
    if not os.path.exists(fp): return {}
    txt = open(fp, encoding="utf-8").read()
    m = re.match(r'^---\n(.*?)\n---', txt, re.S)
    if not m: return {}
    try: return yaml.safe_load(m.group(1)) or {}
    except: return {}

def slug_display(slug):
    """把 slug 转成可读形式，保留原样（避免瞎翻译）"""
    return slug

if __name__ == "__main__":
    slug = sys.argv[1]
    # 定位 stub
    for layer in ["concepts","entities"]:
        fp = os.path.join(WIKI, layer, slug+".md")
        if os.path.exists(fp):
            txt = open(fp, encoding="utf-8").read()
            cites = re.findall(r'\.\./papers/([\w-]+)', txt)
            print(f"LAYER={layer} SLUG={slug} CITES={cites}")
            for c in cites:
                note = open(os.path.join(RAW_NOTE,c+".md"), encoding="utf-8").read()
                fm = get_paper_fm(c)
                print(f"--- citekey={c} year={fm.get('year')} title={fm.get('title','')[:80]}")
                for k in FIELD_KEYS:
                    v = extract_field(note, k)
                    if v:
                        print(f"  [{k}] {v[:150]}")
                ab = get_abstract_zh(note)
                if ab: print(f"  [摘要翻译] {ab[:150]}")
            break
