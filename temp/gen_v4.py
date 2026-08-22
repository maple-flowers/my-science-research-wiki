# -*- coding: utf-8 -*-
"""stub 页生成器 v4：生成符合 DoD 的规范自包含 developing 页（含多论文聚合），写盘"""
import os, re, yaml, sys, json

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
        for x in (p["fm"].get("concepts",[]) or []):
            if x in concept_files and (x,"concept") not in rel: rel.append((x,"concept"))
        for x in (p["fm"].get("entities",[]) or []):
            if x in entity_files and (x,"entity") not in rel: rel.append((x,"entity"))
    return rel

def build_page(layer, slug, papers):
    year = papers[0]["fm"].get("year")
    cites = [p["cite"] for p in papers]
    tags = []
    for p in papers:
        for x in (p["fm"].get("concepts",[]) or [])[:5]:
            if x not in tags and x!=slug: tags.append(x)
    tags = tags[:10]

    fields = {}
    for p in papers:
        for k in FIELD_KEYS:
            v=extract_field(p["note"],k)
            if v: fields.setdefault(k,[]).append(v)
    def F(k, idx=0):
        arr = fields.get(k,[])
        return arr[idx] if idx < len(arr) else (arr[0] if arr else "")
    # 综合多篇：研究对象取第一篇；背景/结论/贡献聚合
    obj = F("主要研究对象")
    bg = F("研究背景")
    concl = "；".join(fields.get("研究结论",[]))
    contrib = "；".join(fields.get("对领域的贡献",[]))
    meaning = F("研究意义")
    method = F("主要研究方法")
    problem = F("作者的问题意识")

    # 定义段
    is_multi = len(papers)>1
    def_lines=[]
    if is_multi:
        def_lines.append(f"本文档围绕 **{slug}** 汇集 {len(papers)} 篇论文的证据，覆盖其结构、物性与机制等多方面信息。")
    elif obj:
        def_lines.append(obj.split("。")[0]+"。")
    else:
        ab0 = get_abstract_zh(papers[0]["note"])
        if ab0: def_lines.append(ab0.split("。")[0]+"。")
    def_lines.append("")
    definition = "\n".join(def_lines)

    # 太奶导读
    tln=[]
    tln.append("## 👵 太奶导读")
    tln.append("")
    if is_multi:
        tln.append(f"乖孙，这一条讲的是「{slug}」，由多篇论文的证据共同支撑。")
    elif obj:
        tln.append(f"乖孙，这一条讲的是「{obj.split('。')[0]}」。")
    elif len(papers)==1:
        ab0 = get_abstract_zh(papers[0]["note"])
        if ab0:
            tln.append(f"乖孙，这一条要讲的核心对象是「{ab0.split('。')[0]}」。")
        else:
            tln.append("乖孙，这是一篇论文的研究主题。")
    if concl:
        c0 = re.sub(r'^\d+[\.、]\s*','',concl.split("；")[0].split("。")[0])
        tln.append("一句话记住它的发现：" + c0 + "。")
    else:
        tln.append("这篇论文为它提供了关键证据。")
    tln.append("")

    # 结构概览（entity）
    overview=[]
    if layer=="entity":
        overview.append("## 🏗️ 结构概览 (Structure)")
        overview.append("")
        if obj: overview.append("- **研究对象**："+obj.replace("\n","；"))
        if method: overview.append("- **研究方法**："+method.replace("\n","；"))
        overview.append("")

    # 核心内容
    core=[]
    core.append("## 🧩 核心内容与机制 (Core Content)")
    core.append("")
    if bg: core.append("- **研究背景**："+bg.replace("\n","；"))
    if problem: core.append("- **核心问题**："+problem.replace("\n","；"))
    if concl: core.append("- **主要结论**："+concl.replace("\n","；"))
    if contrib: core.append("- **领域贡献**："+contrib.replace("\n","；"))
    if meaning: core.append("- **研究意义**："+meaning.replace("\n","；"))
    core.append("")

    # 相关论文
    papers_sec=[]
    papers_sec.append("## 📚 相关论文 (Related Papers)")
    papers_sec.append("")
    for p in papers:
        ct = extract_field(p["note"],"对领域的贡献")
        if not ct: ct = extract_field(p["note"],"研究结论")
        if ct:
            ctxt = ct.replace("\n","；").split("。")[0]+"。"
        else:
            ctxt = "为本文档提供核心证据。"
        papers_sec.append(f"- [[../papers/{p['cite']}]]：{ctxt}")
    papers_sec.append("")

    # 关联
    rel_sec=[]
    rel_sec.append("## 🔗 关联概念与实体 (Related)")
    rel_sec.append("")
    rel = [r for r in collect_related(papers) if r[0]!=slug]
    if rel:
        for rslug, rtyp in rel[:16]:
            rel_sec.append(f"- [[../{rtyp}s/{rslug}|{rslug}]]")
    else:
        rel_sec.append("_（暂无已验证的关联页面）_")
    rel_sec.append("")

    # frontmatter
    fm=[]
    fm.append("---")
    fm.append(f"tags: [{', '.join(tags)}]" if tags else "tags: []")
    fm.append(f"title: {slug}")
    fm.append(f"type: {layer}")
    fm.append("status: developing")
    if year: fm.append(f"year: {year}")
    fm.append(f"papers: [{', '.join(cites)}]")
    fm.append("updated: 2026-08-18")
    fm.append("---")

    parts = ["\n".join(fm), "", f"# {slug}", "", definition.rstrip("\n"), ""]
    parts += [ "\n".join(tln).rstrip("\n"), ""]
    if overview: parts += overview
    parts += core + papers_sec + rel_sec
    return "\n".join(parts)

def gen(slug):
    layer, stub = find_page(slug)
    if not layer: return None
    cites = re.findall(r'\.\./papers/([\w-]+)', stub)
    papers=[]
    for c in cites:
        nf=os.path.join(RAW_NOTE,c+".md")
        note=open(nf,encoding="utf-8").read() if os.path.exists(nf) else ""
        papers.append({"cite":c,"fm":get_paper_fm(c),"note":note})
    return layer, build_page(layer, slug, papers)

if __name__=="__main__":
    # 用法：python gen_v4.py <slug...>
    outdir = sys.argv[1]
    for slug in sys.argv[2:]:
        r = gen(slug)
        if r:
            layer, page = r
            fp = os.path.join(WIKI, layer, slug+".md")
            with open(fp, "w", encoding="utf-8") as f:
                f.write(page)
            print("WROTE", layer, slug)
