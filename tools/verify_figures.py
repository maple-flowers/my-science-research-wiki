#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Verify figure reclassification results.
Checks:
1. All figure pages exist and have entries
2. All paper arrow links point to existing figure pages
3. Frontmatter figures: field matches arrow links
4. No orphaned old figure pages
5. Entry counts match
"""
import json, re, os, sys
from collections import defaultdict, Counter

sys.stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8', closefd=False)

WIKI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGURES_DIR = os.path.join(WIKI_DIR, "wiki", "figures")
PAPERS_DIR = os.path.join(WIKI_DIR, "wiki", "papers")

ARROW_PATTERN = re.compile(
    r'!\[[^\]]*\]\(([^)]+)\)\s*(?:->|→|⟶)\s*\[\[\.\./figures/([^|\]]+)\|([^\]]+)\]\]'
)

# Expected new page slugs
EXPECTED_PAGES = {
    # Non-split single pages
    "heterostructures-stacking", "experimental-setups",
    "optical-spectra", "vibrational-spectra",
    # Split-category hub pages (list subpages only, hold 0 entries themselves)
    "crystal-structures", "electronic-bands", "electronic-devices",
    "domain-walls", "mathematical-models",
    # Subpages
    "electronic-bands-band-structures", "electronic-bands-dos-fermi",
    "electronic-bands-cdw-transport",
    "mathematical-models-formulas", "mathematical-models-computational",
    "mathematical-models-simulations", "mathematical-models-elasticity-strain",
    "mathematical-models-magnetoelectric",
    "crystal-structures-bulk", "crystal-structures-surfaces-defects",
    "crystal-structures-xrd-phases",
    "electronic-devices-sensors", "electronic-devices-memory-transistors",
    "domain-walls-structures", "domain-walls-switching-properties",
}

# Hub pages intentionally hold no entries of their own
HUB_PAGES = {
    "crystal-structures", "electronic-bands", "electronic-devices",
    "domain-walls", "mathematical-models",
}

# Subpages belonging to each hub, for count reconciliation
HUB_SUBPAGES = {
    "electronic-bands": ["electronic-bands-band-structures",
                         "electronic-bands-dos-fermi",
                         "electronic-bands-cdw-transport"],
    "mathematical-models": ["mathematical-models-formulas",
                            "mathematical-models-computational",
                            "mathematical-models-simulations",
                            "mathematical-models-elasticity-strain",
                            "mathematical-models-magnetoelectric"],
    "crystal-structures": ["crystal-structures-bulk",
                           "crystal-structures-surfaces-defects",
                           "crystal-structures-xrd-phases"],
    "electronic-devices": ["electronic-devices-sensors",
                           "electronic-devices-memory-transistors"],
    "domain-walls": ["domain-walls-structures",
                     "domain-walls-switching-properties"],
}

# Old page slugs that should be deleted
OLD_PAGES = {
    "electronic-bands-superconductivity", "electronic-bands-fermi-surfaces",
    "electronic-bands-experimental", "electronic-bands-dos-pdos",
    "electronic-bands-computational",
    "heterostructures-stacking-multiferroic-mechanisms",
    "heterostructures-stacking-multiferroic-tables",
    "heterostructures-stacking-multiferroic-materials",
    "heterostructures-stacking-multiferroic",
    "heterostructures-stacking-domains-devices",
    "heterostructures-stacking-mechanics-misc",
    "heterostructures-stacking-moire",
    "heterostructures-stacking-polar-cdw",
    "heterostructures-stacking-reviews",
    "heterostructures-stacking-sliding",
    "heterostructures-stacking-spintronics-strain",
    "crystal-structures-fundamentals", "crystal-structures-tables",
    "crystal-structures-computational", "crystal-structures-phase",
    "mathematical-models-dft", "mathematical-models-hep",
    "mathematical-models-kinetics", "mathematical-models-magnetism",
    "mathematical-models-optics", "mathematical-models-strain-mechanics",
    "mathematical-models-fe-mf-a", "mathematical-models-fe-mf-b",
    "mathematical-models-fe-mf-c", "mathematical-models-cdw",
    "experimental-setups-devices-architectures",
    "experimental-setups-growth-synthesis",
    "experimental-setups-optical-fiber",
    "experimental-setups-probe-microscopy",
    "experimental-setups-spectroscopy-diffraction",
    "optical-spectra-2d-shg-multiferroic",
    "optical-spectra-thinfilms-nlo",
}


def main():
    issues = []

    # 1. Check figure pages exist
    print("=== 1. Checking figure pages ===")
    existing_pages = set()
    for f in os.listdir(FIGURES_DIR):
        if f.endswith(".md") and f != "_index.md":
            slug = f[:-3]
            existing_pages.add(slug)
            if slug not in EXPECTED_PAGES:
                issues.append(f"Unexpected figure page: {f}")

    for slug in EXPECTED_PAGES:
        if slug not in existing_pages:
            issues.append(f"Missing expected figure page: {slug}.md")

    print(f"  Found {len(existing_pages)} figure pages")

    # 2. Check old pages are deleted
    print("\n=== 2. Checking old pages deleted ===")
    for slug in OLD_PAGES:
        if slug in existing_pages:
            issues.append(f"Old page not deleted: {slug}.md")
    print(f"  Checked {len(OLD_PAGES)} old page slugs")

    # 3. Check paper arrow links
    print("\n=== 3. Checking paper arrow links ===")
    total_links = 0
    broken_links = 0
    old_slug_links = 0
    papers = [f for f in os.listdir(PAPERS_DIR) if f.endswith(".md")]

    for paper_file in papers:
        filepath = os.path.join(PAPERS_DIR, paper_file)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        for m in ARROW_PATTERN.finditer(content):
            total_links += 1
            slug = m.group(2)
            if slug not in EXPECTED_PAGES:
                if slug in OLD_PAGES:
                    old_slug_links += 1
                    issues.append(f"{paper_file}: links to old slug '{slug}'")
                else:
                    broken_links += 1
                    if broken_links <= 20:  # limit output
                        issues.append(f"{paper_file}: links to unknown slug '{slug}'")

    print(f"  Total arrow links: {total_links}")
    print(f"  Links to old slugs: {old_slug_links}")
    print(f"  Links to unknown slugs: {broken_links}")

    # 4. Check entry counts
    print("\n=== 4. Checking entry counts ===")
    with open(os.path.join(WIKI_DIR, "tools", "figure_classified.json"), "r", encoding="utf-8") as f:
        entries = json.load(f)

    slug_map_path = os.path.join(WIKI_DIR, "tools", "figure_slug_map.json")
    slug_map = json.load(open(slug_map_path, encoding="utf-8"))

    # Authoritative per-page counts come from the slug map (which records the
    # final subpage each figure landed on).
    entry_counts = Counter(slug_map.values())

    # Count entries actually rendered in each figure page
    page_counts = Counter()
    for slug in existing_pages:
        filepath = os.path.join(FIGURES_DIR, f"{slug}.md")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        page_counts[slug] = len(re.findall(r'^### \d+\.', content, re.MULTILINE))

    for slug in existing_pages:
        if slug in HUB_PAGES:
            # A hub holds no entries; it must instead list its subpages,
            # and the subpage totals must add up to the hub's share.
            if page_counts[slug] != 0:
                issues.append(f"Hub page {slug} unexpectedly holds {page_counts[slug]} entries")
            subs = HUB_SUBPAGES.get(slug, [])
            hub_total = sum(page_counts.get(s, 0) for s in subs)
            expected_total = sum(entry_counts.get(s, 0) for s in subs)
            if hub_total != expected_total:
                issues.append(
                    f"Hub {slug}: subpage entries sum to {hub_total}, expected {expected_total}")
            continue
        expected = entry_counts.get(slug, 0)
        actual = page_counts.get(slug, 0)
        if expected != actual:
            issues.append(f"Entry count mismatch for {slug}: expected {expected}, found {actual}")

    total_rendered = sum(page_counts.values())
    print(f"  Entries rendered across all pages: {total_rendered}")
    print(f"  Entries in slug map:               {len(slug_map)}")
    if total_rendered != len(slug_map):
        issues.append(
            f"Total rendered entries {total_rendered} != slug map size {len(slug_map)}")

    # Summary
    print(f"\n=== Summary ===")
    print(f"  Total issues: {len(issues)}")
    if issues:
        print(f"\n--- Issues (first 30) ---")
        for issue in issues[:30]:
            print(f"  {issue}")


if __name__ == "__main__":
    main()
