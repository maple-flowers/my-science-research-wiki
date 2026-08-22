# -*- coding: utf-8 -*-
"""单论文 stub 页生成器 v2：生成规范自包含页内容（不写盘，输出到 stdout）"""
import os, re, yaml, sys

BASE = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
RAW_NOTE = os.path.join(BASE, "raw", "note")
PAPER_DIR = os.path.join(BASE, "wiki", "papers")
WIKI = os.path.join(BASE, "wiki")

FIELD_KEYS = ["领域基础知识","研究背景","作者的问题意识","主要研究对象","主要研究方法","研究意义","研究结论","对领域的贡献","未来研究方向提及","未来研究方向思考"]

def extract_field(txt, key):
    lines = txt.split("\n"); cap=False; out=[]
    for ln in lines:
        s=ln.strip(); s2=s[1:].strip() if s.startswith(">") else s
        m=re.match(r'^([\u4e00-\u9fa5A-Za-z][\u4e00-\u9fa5A-Za-z_]*)::(.*)$', s2)
        if m:
            k,rest=m.group(1),m.group(2).strip()
            if k==key:
                cap=True
                if rest: out.append(rest)
                continue
            else:
                if cap: break
                continue
        if cap and s2: out.append(s2)
    return "\n".join(out).strip()

def get_abstract_zh(txt):
    m=re.search(r'【摘要翻译】(.*?)(?=\n\n|\n\s*>?\s*\[!tldr\]|\Z)',txt,re.S)
    if m: return re.sub(r'^\s*>\s*','',m.group(1).strip(),flags=re.M).strip()
    return ""

def get_title_zh(txt):
    m=re.search(r'中文标题:\s*(.*)',txt)
    if m: return m.group(1).strip()
    return ""

def get_paper_fm(citekey):
    fp=os.path.join(PAPER_DIR,citekey+".md")
    if not os.path.exists(fp): return {}
    t=open(fp,encoding="utf-8").read()
    m=re.match(r'^---\n(.*?)\n---',t,re.S)
    if not m: return {}
    try: return yaml.safe_load(m.group(1)) or {}
    except: return {}

concept_files={f[:-3] for f in os.listdir(os.path.join(WIKI,"concepts"))}
entity_files={f[:-3] for f in os.listdir(os.path.join(WIKI,"entities"))}

def gen(slug):
    for layer in ["concepts","entities"]:
        fp=os.path.join(WIKI,layer,slug+".md")
        if os.path.exists(fp):
            txt=open(fp,encoding="utf-8").read()
            cites=re.findall(r'\.\./papers/([\w-]+)',txt)
            # 读每篇论文
            papers=[]
            for c in cites:
                note_fp=os.path.join(RAW_NOTE,c+".md")
                note=open(note_fp,encoding="utf-8").read() if os.path.exists(note_fp) else ""
                fm=get_paper_fm(c)
                papers.append({"cite":c,"fm":fm,"note":note})
            return layer, slug, papers
    return None

def build_page(layer, slug, papers):
    # 综合所有论文信息
    title_zhs=[get_title_zh(p["note"]) for p in papers if get_title_zh(p["note"])]
    abss=[get_abstract_zh(p["note"]) for p in papers if get_abstract_zh(p["note"])]
    fields_all={}
    for p in papers:
        for k in FIELD_KEYS:
            v=extract_field(p["note"],k)
            if v: fields_all.setdefault(k,[]).append(v)
    # 关联概念实体：从论文 frontmatter 收集真实存在页面
    rel=[]
    for p in papers:
        for x in p["fm"].get("concepts",[]):
            if x in concept_files and x not in rel: rel.append(("concept",x))
        for x in p["fm"].get("entities",[]):
            if x in entity_files and x not in rel: rel.append(("entity",x))
    # 避免自引用
    rel=[r for r in rel if r[1]!=slug]

    # ===== 组织正文 =====
    first = abss[0] if abss else (fields_all.get("研究背景",[""])[0] if fields_all.get("研究背景") else "")
    lines=[]
    lines.append(f"# {slug}")
    lines.append("")
    lines.append(first)
    lines.append("")
    # 太奶导读
    bg = fields_all.get("研究背景",[""])[0] if fields_all.get("研究背景") else ""
    lines.append("## 👵 太奶导读")
    lines.append("")
    lines.append("乖孙，" + _taiNai(bg, fields_all, first))
    lines.append("")
    # 结构概览 / 机制
    obj = fields_all.get("主要研究对象",[""])[0] if fields_all.get("主要研究对象") else ""
    method = fields_all.get("主要研究方法",[""])[0] if fields_all.get("主要研究方法") else ""
    concl = fields_all.get("研究结论",[""])[0] if fields_all.get("研究结论") else ""
    if layer=="entity":
        lines.append("## 🏗️ 结构概览")
        lines.append("")
        if obj: lines.append("- **研究对象**："+obj)
        if method: lines.append("- **研究方法**："+method.replace("\n","；"))
        lines.append("")
    lines.append("## 🧩 核心内容与机制")
    lines.append("")
    if concl: lines.append("- **核心结论**："+concl.replace("\n","；"))
    contrib = fields_all.get("对领域的贡献",[""])[0] if fields_all.get("对领域的贡献") else ""
    if contrib: lines.append("- **领域贡献**："+contrib)
    meaning = fields_all.get("研究意义",[""])[0] if fields_all.get("研究意义") else ""
    if meaning: lines.append("- **研究意义**："+meaning)
    lines.append("")
    # 相关论文
    lines.append("## 📚 相关论文 (Related Papers)")
    lines.append("")
    for p in papers:
        contrib_txt = extract_field(p["note"],"对领域的贡献")
        if not contrib_txt:
            contrib_txt = extract_field(p["note"],"研究结论")
        c=contrib_txt[:120] if contrib_txt else "提供本页相关证据"
        lines.append(f"- [[../papers/{p['cite']}]]：{c}")
    lines.append("")
    # 关联概念
    lines.append("## 🔗 关联概念与实体 (Related Concepts & Entities)")
    lines.append("")
    for typ, rslug in rel[:12]:
        disp = rslug
        lines.append(f"- [[../{typ}s/{rslug}|{disp}]]")
    lines.append("")
    return "\n".join(lines)

def _taiNai(bg, fields, first):
    # 生成白话导读：基于背景/结论改写
    concl = fields.get("研究结论",[""])[0] if fields.get("研究结论") else ""
    obj = fields.get("主要研究对象",[""])[0] if fields.get("主要研究对象") else ""
    simple = ""
    if obj:
        simple = f"这篇文章研究的是{obj}。"
    if concl:
        # 取结论第一个分句
        c0 = concl.split("。")[0]
        simple += f"它的核心发现是：{c0}。"
    else:
        simple += "这篇论文给出了这一概念/实体的关键证据。"
    return simple

if __name__=="__main__":
    for slug in sys.argv[1:]:
        r=gen(slug)
        if r:
            layer, slug2, papers=r
            page=build_page(layer,slug2,papers)
            print("="*70)
            print(page)
            print("="*70)
