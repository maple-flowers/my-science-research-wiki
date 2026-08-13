#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Extract ALL figure entries from wiki/papers "关键图表" sections.
Handles both layouts:
  A) image-first:  - ![alt](img) -> [[slug|..]] / - **图示描述**: / - **关键特征**:
  B) header-first: - **图N** title / - **图示描述**: / - **关键特征**: / ![alt](img) -> [[slug|..]]
"""
import re, os, sys, json

sys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8', closefd=False)

WIKI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS_DIR = os.path.join(WIKI_DIR, "wiki", "papers")

IMG_RE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
ARROW_RE = re.compile(r'!\[[^\]]*\]\([^)]+\)\s*(?:->|→|⟶)\s*\[\[\.\./figures/([^|\]]+)(?:\|[^\]]*)?\]\]')
HDR_RE = re.compile(r'^\s*-\s*\*\*([^*]+)\*\*\s*(.*)$')
DESC_RE = re.compile(r'\*\*图示描述\*\*\s*[:：]\s*(.*)')
FEAT_RE = re.compile(r'\*\*关键特征\*\*\s*[:：]\s*(.*)')
CONC_RE = re.compile(r'\*\*(?:结论|结论/意义|意义)\*\*\s*[:：]')

SECTION_START = re.compile(r'关键图表')
# A new top-level section begins with a heading or a non-indented field
SECTION_END = re.compile(r'^(#{1,6}\s|\S+::|---\s*$|\S)')


def _section_from(content, start_pos):
    """Slice a section body starting after the line at start_pos.

    The body ends at the next markdown heading, a horizontal rule, or a
    dataview-style `field::` line at column 0. Plain prose lines do NOT end
    the section — several papers open the section with an explanatory
    sentence before the figure bullets.
    """
    rest = content[start_pos:]
    start = start_pos + (rest.index('\n') + 1 if '\n' in rest else len(rest))
    out = []
    for ln in content[start:].split('\n'):
        if ln.strip() == '':
            out.append(ln)
            continue
        if re.match(r'^#{1,6}\s', ln):
            break
        if re.match(r'^---\s*$', ln):
            break
        if re.match(r'^\S[^\s:]*::', ln):
            break
        out.append(ln)
    return '\n'.join(out)


def get_section(content):
    """Return the 关键图表 section text.

    Papers mention 关键图表 in several places (TOC lists, back-links, and the
    real section). Collect every candidate and keep whichever body actually
    contains figure images.
    """
    candidates = []
    for hm in re.finditer(r'^#{1,6}\s*.*关键图表.*$', content, re.M):
        candidates.append(hm.end())
    for hm in SECTION_START.finditer(content):
        candidates.append(hm.end())

    best, best_imgs = None, -1
    for pos in candidates:
        body = _section_from(content, pos)
        n = len(IMG_RE.findall(body))
        if n > best_imgs:
            best, best_imgs = body, n
    return best


META_LABELS = ('图示描述', '关键特征', '结论', '意义', '结论/意义')
META_BULLET = re.compile(
    r'^\s*-\s*\*\*(?:' + '|'.join(map(re.escape, META_LABELS)) + r')\*\*'
)


def split_blocks(section):
    """Split section into per-figure blocks.

    A new block starts at a list bullet that is NOT a metadata bullet
    (图示描述 / 关键特征 / 结论). Papers vary in whether metadata bullets are
    nested under the figure bullet or written as siblings at the same indent,
    so indentation alone cannot delimit blocks.
    """
    lines = section.split('\n')
    blocks, cur = [], []
    for ln in lines:
        stripped = ln.lstrip()
        is_bullet = stripped.startswith('- ')
        if is_bullet and not META_BULLET.match(ln):
            if cur:
                blocks.append('\n'.join(cur))
            cur = [ln]
        else:
            if cur:
                cur.append(ln)
            elif is_bullet:
                cur = [ln]
    if cur:
        blocks.append('\n'.join(cur))
    return blocks


def parse_block(block, paper):
    """Extract figure entries from a block. One entry per image. Returns list."""
    # Find each image together with its optional arrow slug
    pairs = []
    for m in IMG_RE.finditer(block):
        img_alt, img_path = m.group(1), m.group(2)
        tail = block[m.end():m.end() + 200]
        am = re.match(r'\s*(?:->|→|⟶)\s*\[\[\.\./figures/([^|\]]+)(?:\|[^\]]*)?\]\]', tail)
        pairs.append((img_alt, img_path, am.group(1) if am else ""))
    if not pairs:
        return []

    # Title from bold header (shared by the block)
    hdr_title = ""
    for ln in block.split('\n'):
        hm = HDR_RE.match(ln)
        if hm:
            label, rest = hm.group(1).strip(), hm.group(2).strip()
            if label in ('图示描述', '关键特征', '结论', '意义', '结论/意义'):
                continue
            hdr_title = (label + ' ' + rest).strip()
            break

    # desc / feat: collect the line plus continuation lines
    def grab(regex):
        lines = block.split('\n')
        for i, ln in enumerate(lines):
            m = regex.search(ln)
            if not m:
                continue
            parts = [m.group(1).strip()]
            for nxt in lines[i + 1:]:
                s = nxt.strip()
                if not s:
                    break
                if (DESC_RE.search(nxt) or FEAT_RE.search(nxt) or CONC_RE.search(nxt)
                        or s.startswith('- ') or s.startswith('!')):
                    break
                parts.append(s)
            return ' '.join(parts).strip()
        return ""

    desc, feat = grab(DESC_RE), grab(FEAT_RE)
    single = len(pairs) == 1

    out = []
    for img_alt, img_path, slug in pairs:
        # For single-image blocks the header describes that image.
        # For multi-image blocks prefer the per-image alt, falling back to header.
        if single:
            title = hdr_title or img_alt.strip()
        else:
            title = img_alt.strip() or hdr_title
        out.append({
            "paper": paper,
            "alt": title,
            "img": img_path,
            "current_slug": slug,
            "desc": desc,
            "feat": feat,
        })
    return out


def main():
    all_entries = []
    stats = []
    no_section = []

    for f in sorted(os.listdir(PAPERS_DIR)):
        if not f.endswith('.md'):
            continue
        paper = f[:-3]
        content = open(os.path.join(PAPERS_DIR, f), encoding='utf-8').read()
        section = get_section(content)
        if section is None:
            no_section.append(paper)
            continue
        blocks = split_blocks(section)
        n = 0
        captured = set()
        for b in blocks:
            for e in parse_block(b, paper):
                all_entries.append(e)
                captured.add(e['img'])
                n += 1
        # Catch images in the section that sat outside any bullet block
        for m in IMG_RE.finditer(section):
            img_alt, img_path = m.group(1), m.group(2)
            if img_path in captured:
                continue
            tail = section[m.end():m.end() + 200]
            am = re.match(r'\s*(?:->|→|⟶)\s*\[\[\.\./figures/([^|\]]+)(?:\|[^\]]*)?\]\]', tail)
            all_entries.append({
                "paper": paper,
                "alt": img_alt.strip(),
                "img": img_path,
                "current_slug": am.group(1) if am else "",
                "desc": "",
                "feat": "",
            })
            captured.add(img_path)
            n += 1
        # Catch images not inside any bullet block
        stats.append((paper, n))

    # Dedupe by img path (keep first)
    seen, deduped = set(), []
    for e in all_entries:
        if e['img'] in seen:
            continue
        seen.add(e['img'])
        deduped.append(e)

    print(f"Papers scanned: {len(stats)}")
    print(f"Papers with no 关键图表 section: {len(no_section)}")
    for p in no_section:
        print(f"    {p}")
    print(f"Entries extracted: {len(all_entries)} (deduped: {len(deduped)})")

    withslug = sum(1 for e in deduped if e['current_slug'])
    print(f"  with arrow slug: {withslug}")
    print(f"  without slug:    {len(deduped) - withslug}")
    withdesc = sum(1 for e in deduped if e['desc'])
    print(f"  with 图示描述:   {withdesc}")

    out = os.path.join(WIKI_DIR, "tools", "figure_entries_full.json")
    json.dump(deduped, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f"\nSaved {len(deduped)} entries to tools/figure_entries_full.json")

    # Compare against old extraction
    old_path = os.path.join(WIKI_DIR, "tools", "figure_entries.json")
    if os.path.exists(old_path):
        old = json.load(open(old_path, encoding='utf-8'))
        old_imgs = {e['img'] for e in old}
        new_imgs = {e['img'] for e in deduped}
        print(f"\nOld extraction: {len(old)} entries")
        print(f"  newly found:  {len(new_imgs - old_imgs)}")
        print(f"  lost:         {len(old_imgs - new_imgs)}")
        lost = old_imgs - new_imgs
        for img in list(lost)[:15]:
            print(f"    LOST: {img}")


if __name__ == "__main__":
    main()
