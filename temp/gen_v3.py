# -*- coding: utf-8 -*-
"""单论文 stub 页生成器 v3：生成符合 DoD 的规范自包含 developing 页（输出到 stdout，不写盘）"""
import os, re, yaml

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

def find_page(slug):
    for layer in ["concepts","entities"]:
        fp=os.path.join(WIKI,layer,slug+".md")
        if os.path.exists(fp):
            return layer, open(fp,encoding="utf-8").read()
    return None, None

def collect_related(papers):
    rel=[]
    for p in papers:
        for x in p["fm"].get("concepts",[]) or []:
            if x in concept_files and (x,"concept") not in rel: rel.append((x,"concept"))
        for x in p["fm"].get("entities",[]) or []:
            if x in entity_files and (x,"entity") not in rel: rel.append((x,"entity"))
    return rel

def build_page(layer, slug, papers, stub_text):
    title_zh = get_title_zh(papers[0]["note"])
    year = papers[0]["fm"].get("year")
    cites = [p["cite"] for p in papers]
    tags = []
    for p in papers:
        for x in (p["fm"].get("concepts",[]) or [])[:6]:
            if x not in tags and x!=slug: tags.append(x)
    tags = tags[:8]

    first_abs = get_abstract_zh(papers[0]["note"])
    fields = {}
    for p in papers:
        for k in FIELD_KEYS:
            v=extract_field(p["note"],k)
            if v: fields.setdefault(k,[]).append(v)
    def F(k): return fields.get(k,[""])[0]

    obj = F("主要研究对象")
    bg = F("研究背景")
    concl = F("研究结论")
    contrib = F("对领域的贡献")
    meaning = F("研究意义")
    method = F("主要研究方法")
    domain = F("领域基础知识")
    problem = F("作者的问题意识")

    # ===== frontmatter =====
    fm_lines=[]
    fm_lines.append("---")
    fm_lines.append(f"tags: [{' , '.join(tags)}]" if tags else "tags: []")
    fm_lines.append(f"title: {slug}")
    fm_lines.append(f"type: {layer}")
    fm_lines.append("status: developing")
    if year: fm_lines.append(f"year: {year}")
    fm_lines.append(f"papers: [{', '.join(cites)}]")
    fm_lines.append("updated: 2026-08-18")
    fm_lines.append("---")
    body=[]
    body.append(f"# {slug}")
    body.append("")
    # ===== 定义段 =====
    if domain:
        d0 = domain.split("。")[0]
        body.append(d0 + "。" + (" 本文聚焦于 " + obj.split("。")[0] + "。" if obj else ""))
    elif obj:
        body.append("本文研究对象为 " + obj.split("。")[0] + "。")
    else:
        body.append(first_abs.split("。")[0] + "。")
    body.append("")
    # ===== 太奶导读 =====
    body.append("## 👵 太奶导读")
    body.append("")
    if obj:
        body.append(f"乖孙，这篇论文做的是「{obj.split('。')[0]}」。")
    tail = ""
    if concl:
        c0 = re.sub(r'^\d+[\.、]?\s*','',concl.split("。")[0])
        tail = "一句话记住它的发现：" + c0 + "。"
    body.append(tail if tail else "一句话记住：这篇论文为这个条目提供了关键实验/理论证据。")
    body.append("")
    # ===== 结构概览 / 机制 =====
    if layer=="entity":
        body.append("## 🏗️ 结构概览 (Structure)")
        body.append("")
        if obj: body.append("- **研究对象**："+obj.replace("\n","；"))
        if method: body.append("- **研究方法**："+method.replace("\n","；"))
        body.append("")
    body.append("## 🧩 核心内容与机制 (Core Content)")
    body.append("")
    if bg: body.append("- **研究背景**："+bg.replace("\n","；"))
    if problem: body.append("- **核心问题**："+problem.replace("\n","；"))
    if concl: body.append("- **主要结论**："+concl.replace("\n","；"))
    if contrib: body.append("- **领域贡献**："+contrib.replace("\n","；"))
    if meaning: body.append("- **研究意义**："+meaning.replace("\n","；"))
    body.append("")
    # ===== 相关论文 =====
    body.append("## 📚 相关论文 (Related Papers)")
    body.append("")
    for p in papers:
        ct = extract_field(p["note"],"对领域的贡献")
        if not ct: ct = extract_field(p["note"],"研究结论")
        ctxt = (ct.split("。")[0] if ct else "为本文档提供核心证据。") + "。"
        body.append(f"- [[../papers/{p['cite']}]]：{ctxt}")
    body.append("")
    # ===== 关联 =====
    rel = collect_related(papers)
    rel = [r for r in rel if r[0]!=slug]
    body.append("## 🔗 关联概念与实体 (Related)")
    body.append("")
    if rel:
        for rslug, rtyp in rel[:14]:
            d = rslug
            body.append(f"- [[../{rtyp}s/{rslug}|{d}]]")
    else:
        body.append("_（暂无已验证的关联页面）_")
    body.append("")
    return "\n".join(fm_lines) + "\n\n" + "\n".join(body)

def gen(slug):
    layer, stub = find_page(slug)
    if not layer: return None
    cites = re.findall(r'\.\./papers/([\w-]+)', stub)
    papers=[]
    for c in cites:
        nf=os.path.join(RAW_NOTE,c+".md")
        note=open(nf,encoding="utf-8").read() if os.path.exists(nf) else ""
        papers.append({"cite":c,"fm":get_paper_fm(c),"note":note})
    return build_page(layer, slug, papers, stub)

if __name__=="__main__":
    import sys
    for slug in sys.argv[1:]:
        page=gen(slug)
        print("="*70)
        print(page if page else f"NOT FOUND {slug}")
        print("="*70)
