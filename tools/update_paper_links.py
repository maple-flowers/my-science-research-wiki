#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Update paper links and frontmatter figures: field to match new figure classification.
- Replaces -> [[../figures/old-slug|old-desc]] with -> [[../figures/new-slug|new-desc]]
- Updates frontmatter figures: field with new slugs
"""
import json, re, os, sys
from collections import defaultdict

sys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8', closefd=False)

WIKI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS_DIR = os.path.join(WIKI_DIR, "wiki", "papers")

# Display names for each figure page slug
SLUG_NAMES = {
    # Non-split categories (single pages)
    "heterostructures-stacking": "异质结与堆叠",
    "experimental-setups": "实验装置与测量系统",
    "optical-spectra": "光学光谱",
    "vibrational-spectra": "振动光谱",
    # Split category subpages
    "electronic-bands-band-structures": "能带结构与带隙",
    "electronic-bands-dos-fermi": "态密度与费米面",
    "electronic-bands-cdw-transport": "CDW与输运性质",
    "mathematical-models-formulas": "光学、输运与其他解析公式",
    "mathematical-models-computational": "计算方法与泛函",
    "mathematical-models-simulations": "模拟与数值结果",
    "mathematical-models-elasticity-strain": "应变、弹性与力学模型",
    "mathematical-models-magnetoelectric": "磁电耦合与多铁理论",
    "crystal-structures-bulk": "体相晶体结构",
    "crystal-structures-surfaces-defects": "表面、缺陷与形貌",
    "crystal-structures-xrd-phases": "XRD与相变",
    "electronic-devices-sensors": "传感器与探测器",
    "electronic-devices-memory-transistors": "存储器与晶体管",
    "domain-walls-structures": "畴结构与畴壁",
    "domain-walls-switching-properties": "极化翻转与铁电性能",
}

# Pattern for arrow links: ![alt](img) -> [[../figures/slug|desc]]
# Also matches Unicode arrow ⟶ and variations
ARROW_PATTERN = re.compile(
    r'(!\[[^\]]*\]\(([^)]+)\)\s*(?:->|→|⟶)\s*)\[\[../figures/([^|]+)\|([^\]]+)\]\]'
)


def load_slug_map():
    """Load the img_path -> slug mapping."""
    with open(os.path.join(WIKI_DIR, "tools", "figure_slug_map.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def update_paper(filepath, slug_map):
    """Update a single paper file. Returns (changed, num_links_updated, new_slugs)."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_slugs = set()
    link_count = 0
    link_changes = 0

    def replace_arrow(m):
        nonlocal link_count, link_changes
        prefix = m.group(1)  # ![alt](img) ->
        img = m.group(2)     # img path
        old_slug = m.group(3)
        old_desc = m.group(4)

        link_count += 1

        # Look up new slug
        new_slug = slug_map.get(img)
        if new_slug is None:
            # Try matching by filename
            filename = os.path.basename(img)
            for map_img, map_slug in slug_map.items():
                if os.path.basename(map_img) == filename:
                    new_slug = map_slug
                    break

        if new_slug is None:
            # Can't find mapping, keep original
            return m.group(0)

        new_desc = SLUG_NAMES.get(new_slug, new_slug)
        new_slugs.add(new_slug)

        if new_slug != old_slug or new_desc != old_desc:
            link_changes += 1

        return f'{prefix}[[../figures/{new_slug}|{new_desc}]]'

    # Replace arrow links
    new_content = ARROW_PATTERN.sub(replace_arrow, content)

    # Update frontmatter figures: field
    # Handle inline format: figures: [a, b, c]
    # Handle block format: figures:\n  - a\n  - b
    sorted_slugs = sorted(new_slugs)

    if sorted_slugs:
        # Try inline format first
        inline_pattern = re.compile(r'^figures:\s*\[([^\]]*)\]', re.MULTILINE)
        if inline_pattern.search(new_content):
            new_inline = f"figures: [{', '.join(sorted_slugs)}]"
            new_content = inline_pattern.sub(new_inline, new_content, count=1)
        else:
            # Try block format
            block_pattern = re.compile(r'^figures:\s*\n((?:\s+-\s+\S+\n)*)', re.MULTILINE)
            if block_pattern.search(new_content):
                block_replacement = "figures:\n" + "".join(f"  - {s}\n" for s in sorted_slugs)
                new_content = block_pattern.sub(block_replacement, new_content, count=1)
            else:
                # No figures: field found, but we have slugs
                # This shouldn't happen if the paper has arrow links
                pass

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True, link_changes, sorted_slugs

    return False, 0, sorted_slugs


def main():
    slug_map = load_slug_map()
    print(f"Loaded slug map: {len(slug_map)} entries")

    # Process all papers
    papers = [f for f in os.listdir(PAPERS_DIR) if f.endswith(".md")]
    papers.sort()

    total_changed = 0
    total_links = 0
    total_link_changes = 0
    papers_with_no_links = []

    for paper_file in papers:
        filepath = os.path.join(PAPERS_DIR, paper_file)
        changed, link_changes, new_slugs = update_paper(filepath, slug_map)

        # Count links in the file
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        link_count = len(ARROW_PATTERN.findall(content))

        if link_count == 0:
            papers_with_no_links.append(paper_file)

        total_links += link_count
        if changed:
            total_changed += 1
            total_link_changes += link_changes
            print(f"  Updated: {paper_file} ({link_changes} links, slugs: {new_slugs})")

    print(f"\n=== Summary ===")
    print(f"  Papers updated: {total_changed}")
    print(f"  Total link changes: {total_link_changes}")
    print(f"  Total arrow links: {total_links}")

    if papers_with_no_links:
        print(f"\n=== Papers with no arrow links ({len(papers_with_no_links)}) ===")
        for p in papers_with_no_links:
            print(f"  {p}")


if __name__ == "__main__":
    main()
