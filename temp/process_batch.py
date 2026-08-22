# -*- coding: utf-8 -*-
"""分批执行：对指定论文子集，完成 papers 补链 + concepts/entities 反链补齐。
用法: python process_batch.py <citekey1> <citekey2> ...
"""
import re, sys, json
from pathlib import Path

REPO = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
PAPERS_DIR = REPO / 'wiki' / 'papers'
CONCEPTS_DIR = REPO / 'wiki' / 'concepts'
ENTITIES_DIR = REPO / 'wiki' / 'entities'
OUT = Path(r"C:\Users\sgg\AppData\Roaming\Tencent\Marvis\User\oAN1i2V14p5-lhhSY365mxizlI-c\workspace\conv_1a0000cc73d_3cc2a0c40aa4\temp")

FM_RE = re.compile(r'^---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)', re.DOTALL)

def read(p):
    return p.read_text(encoding='utf-8', errors='replace')

def write(p, text):
    p.write_text(text, encoding='utf-8')

def split_fm(text):
    m = FM_RE.match(text)
    return (m.group(1), text[m.end():]) if m else (None, text)

def get_title(citekey):
    p = PAPERS_DIR / f"{citekey}.md"
    if not p.exists():
        return citekey
    fm, _ = split_fm(read(p))
    if fm:
        m = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', fm, re.MULTILINE)
        if m:
            return m.group(1).strip()
    return citekey

def strip_prefix(slug):
    """剥离 entities/ concepts/ 前缀"""
    for pre in ('entities/', 'concepts/'):
        if slug.startswith(pre):
            return slug[len(pre):]
    return slug

def add_paper_link(text, typ, slug):
    """在 paper 正文「🔗 Wiki 双链」章节补链接行。返回 (新文本, 是否新增)"""
    link = f"[[../{typ}/{slug}]]"
    if link in text:
        return text, False
    # 定位 Wiki 双链章节
    m = re.search(r'(##\s*🔗\s*Wiki\s*双链.*?)(?=\n##\s|\Z)', text, re.DOTALL)
    if not m:
        return text, False
    sec = m.group(1)
    new_line = f"  - {'概念' if typ=='concepts' else '实体'} {link}"
    # 在章节末尾追加（保留章节后空行）
    sec_new = sec.rstrip('\n') + '\n' + new_line + '\n'
    text = text[:m.start(1)] + sec_new + text[m.end(1):]
    return text, True

def add_formal_backlink(text, citekey):
    """正式页：frontmatter papers 字段 + 正文「📚 相关论文」节。返回 (新文本, 是否新增)"""
    changed = False
    fm, body = split_fm(text)
    if fm is None:
        return text, False
    # 1. frontmatter papers 字段
    if re.search(r'^papers:\s*\[', fm, re.MULTILINE):
        # 行内 [a, b] 格式
        def repl(mo):
            inner = mo.group(1)
            items = [x.strip() for x in inner.split(',') if x.strip()]
            if any(x.lower() == citekey.lower() for x in items):
                return mo.group(0)
            nonlocal changed
            changed = True
            return f"papers: [{', '.join(items + [citekey])}]"
        fm = re.sub(r'^papers:\s*\[(.*?)\]', repl, fm, count=1, flags=re.MULTILINE | re.DOTALL)
    elif re.search(r'^papers:\s*$', fm, re.MULTILINE):
        # 多行 - a 格式
        def repl2(mo):
            block = mo.group(0)
            items = re.findall(r'^\s*-\s*(.+?)\s*$', block, re.MULTILINE)
            if any(x.lower() == citekey.lower() for x in items):
                return block
            nonlocal changed
            changed = True
            return block.rstrip('\n') + f"\n  - {citekey}\n"
        fm = re.sub(r'^papers:\s*$.*?(?=^\w|\Z)', repl2, fm, count=1, flags=re.MULTILINE | re.DOTALL)
    # 2. 正文「📚 相关论文」节
    backlink = f"[[../papers/{citekey}]]"
    if backlink in body:
        pass
    else:
        m = re.search(r'(##\s*📚\s*相关论文.*?)(?=\n##\s|\Z)', body, re.DOTALL)
        if m:
            sec = m.group(1)
            sec_new = sec.rstrip('\n') + '\n- ' + backlink + '\n'
            body = body[:m.start(1)] + sec_new + body[m.end(1):]
            changed = True
        else:
            # 无相关论文节，在正文末尾创建
            body = body.rstrip('\n') + f'\n\n## 📚 相关论文 (Related Papers)\n\n- {backlink}\n'
            changed = True
    return fm + '---\n' + body, changed

def add_intermediate_backlink(text, citekey, title):
    """中间产物页：列表追加 - [[../papers/<citekey>]] — <标题>。返回 (新文本, 是否新增)"""
    line = f"- [[../papers/{citekey}]] — {title}"
    if line in text:
        return text, False
    text = text.rstrip('\n') + '\n' + line + '\n'
    return text, True

def create_intermediate_page(typ, slug, citekey, title):
    """新建中间产物页。若已存在则追加反链。返回 (是否新建, 是否新增反链)"""
    d = CONCEPTS_DIR if typ == 'concepts' else ENTITIES_DIR
    p = d / f"{slug}.md"
    if p.exists():
        text = read(p)
        new_text, added = add_intermediate_backlink(text, citekey, title)
        if added:
            write(p, new_text)
        return False, added
    content = f"# {slug}\n\n- [[../papers/{citekey}]] — {title}\n"
    write(p, content)
    return True, True

def process_citekey(citekey, entries):
    """处理单篇论文的所有条目。返回统计 dict"""
    stats = {'paper_links': 0, 'formal_backlinks': 0, 'intermediate_backlinks': 0, 'created_pages': 0}
    # paper 侧补链
    pp = PAPERS_DIR / f"{citekey}.md"
    if not pp.exists():
        print(f"  [跳过] paper 不存在: {citekey}")
        return stats
    text = read(pp)
    for e in entries:
        typ = e['type']
        slug = strip_prefix(e['slug'])
        text, added = add_paper_link(text, typ, slug)
        if added:
            stats['paper_links'] += 1
    write(pp, text)
    # 页面侧反链
    title = get_title(citekey)
    for e in entries:
        typ = e['type']
        slug = strip_prefix(e['slug'])
        d = CONCEPTS_DIR if typ == 'concepts' else ENTITIES_DIR
        p = d / f"{slug}.md"
        if not p.exists():
            created, added = create_intermediate_page(typ, slug, citekey, title)
            if created:
                stats['created_pages'] += 1
            if added:
                stats['intermediate_backlinks'] += 1
            continue
        text = read(p)
        fm, _ = split_fm(text)
        if fm is not None:
            # 正式页
            new_text, added = add_formal_backlink(text, citekey)
            if added:
                write(p, new_text)
                stats['formal_backlinks'] += 1
        else:
            # 中间产物页
            new_text, added = add_intermediate_backlink(text, citekey, title)
            if added:
                write(p, new_text)
                stats['intermediate_backlinks'] += 1
    return stats

def main():
    citekeys = sys.argv[1:]
    data = json.loads((OUT / 'suggestions_full.json').read_text(encoding='utf-8'))
    cat = data['cat']
    # 构建 citekey -> entries 映射（B/C/D 类）
    by_paper = {}
    for k in ['B', 'C', 'D']:
        for e in cat[k]:
            by_paper.setdefault(e['citekey'], []).append(e)
    total = {'paper_links': 0, 'formal_backlinks': 0, 'intermediate_backlinks': 0, 'created_pages': 0}
    for ck in citekeys:
        entries = by_paper.get(ck, [])
        if not entries:
            print(f"  [跳过] 无候选: {ck}")
            continue
        s = process_citekey(ck, entries)
        for kk in total:
            total[kk] += s[kk]
        print(f"  [完成] {ck}: 论文补链 {s['paper_links']}, 正式页反链 {s['formal_backlinks']}, 中间页反链 {s['intermediate_backlinks']}, 新建页 {s['created_pages']}")
    print(f"  [批次汇总] {json.dumps(total, ensure_ascii=False)}")

if __name__ == '__main__':
    main()
