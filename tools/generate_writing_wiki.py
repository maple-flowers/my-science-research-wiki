#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Writing Style Wiki from raw/note/*.md
Extracts academic writing patterns from bilingual sections and groups them by publication year.
Provides detailed logging as requested.
"""

import os
import re
import json
from pathlib import Path
import yaml

# Paths configuration
BASE_DIR = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
NOTES_RAW_DIR = BASE_DIR / "raw" / "note"
WIKI_WRITE_DIR = BASE_DIR / "wiki" / "write"

# Canonical categories and their fuzzy markers
SECTION_MAP = {
    "Introduction": ["引言", "Introduction", "Abstract", "Background", "背景", "综述"],
    "Methods": ["方法", "Methods", "Experimental", "Computational", "Model", "模型", "理论", "Methodology"],
    "Results & Discussion": ["结果", "讨论", "Results", "Discussion", "发现", "Findings", "Analysis", "分析"],
    "Conclusion": ["结论", "Conclusion", "Summary", "展望", "Outlook", "总结"]
}

def log(category, msg):
    print(f"[{category}] {msg}")

def get_canonical_section(header):
    header = header.lower()
    for canonical, markers in SECTION_MAP.items():
        if any(marker.lower() in header for marker in markers):
            return canonical
    return "Other"

def extract_english_sentences(text):
    """Extract significant English sentences from bilingual text."""
    if not text: return []
    # Clean HTML if present
    text = re.sub(r'<[^>]+>', '', text)
    # Remove Bold markers which are often used for emphasis or translations
    text = text.replace('**', '')

    lines = text.split('\n')
    patterns = []
    for line in lines:
        line = line.strip()
        if not line or len(line) < 15: continue

        # Filter out lines that are likely just formulas or meta info
        # Check for citation markers [1], http, doi, etc.
        if re.search(r'\[\d+\]|http|doi:|variable::|\$\$.*?\$\$|[\d=+\\_\^]', line): continue

        # Heuristic: > 70% ASCII
        ascii_count = sum(1 for c in line if ord(c) < 128)
        if ascii_count / len(line) > 0.7:
            # Clean up leading markers like "* ", "- ", "1. "
            cleaned = re.sub(r'^[#* \t\d\.\->]+', '', line).strip()
            # Must start with letter, be long enough, and look like a sentence
            if cleaned and len(cleaned) > 25 and cleaned[0].isupper():
                # Avoid capturing the prompt-like lines from AI or headers
                ai_meta_keywords = [
                    "Interpretation", "Analysis", "Summary", "Deep Dive", "Note:",
                    "I've", "I am now", "Need to", "Need be", "Need include",
                    "Let's", "I will", "My goal", "My duty", "Specifically,", "Moreover,",
                    "Need ", "Prompt:", "Instructions:", "Requirement:",
                    "Now I have", "My plan", "I'll thoroughly", "I'm focusing on",
                    "Initiating ", "Formulating ", "Developing ", "Refining ",
                    "Commencing ", "Dissecting ", "Dissect ", "Dissected ",
                    "Breaking down", "Break it into", "Breaking it into",
                    "Mapped to", "Mapping each", "Mapping it", "Linking my",
                    "Segmenting the project", "Targeting the", "Targets ",
                    "Adhering to", "Adheres to", "Sticking to", "Word count",
                    "Technical terms", "Equivalent", "Visualization", "Markdown",
                    "Expert", "Literature", "Researcher", "Professor",
                    "Read-through", "Methodical", "Comprehensive strategy",
                    "Solidifying my approach", "Immersion", "Immersed",
                    "Solidifying ", "I'm now ", "I am now ", "I have now ",
                    "Finished formulating", "Just finished", "I have just",
                    "Mapped the content", "Identifying technical terms"
                ]
                if any(kw.lower() in cleaned.lower() for kw in ai_meta_keywords): continue
                patterns.append(cleaned)
    return patterns

def parse_note_content(content, citekey):
    """Find and parse the writing patterns from the note."""
    # Target the bilingual transcription section
    # Pattern: ## ❷ 🤖️ 论文双语转写📌
    pattern = r'##\s*.*?论文双语转写.*?📌\n(.*?)(?:\n##\s|$)'
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

    if not match:
        log(citekey, "PARSE: '论文双语转写' section not found. Attempting fuzzy fallback...")
        # Fallback: look for Introduction/Methods/etc. headers directly if the main block is missing
        sections = {}
        for canonical in SECTION_MAP.keys():
            # This is a bit risky but helps with varied templates
            m = re.search(rf'##\s*(?:.*?)({canonical}|{"|".join(SECTION_MAP[canonical])})(.*?)(?:\n##\s|$)', content, re.DOTALL | re.IGNORECASE)
            if m:
                body = m.group(2).strip()
                patterns = extract_english_sentences(body)
                if patterns:
                    sections[canonical] = patterns
        return sections

    bilingual_content = match.group(1)

    # Split by sub-headers (e.g., ### Introduction)
    sections = {}
    sub_header_pattern = r'\n(?:###|####)\s*(.*?)\n'
    splits = list(re.finditer(sub_header_pattern, bilingual_content))

    if not splits:
        log(citekey, "PARSE: No sub-headers found in bilingual section. Extracting all sentences as 'General'.")
        patterns = extract_english_sentences(bilingual_content)
        if patterns:
            sections["General"] = patterns
        return sections

    log(citekey, f"PARSE: Found {len(splits)} sub-headers in bilingual section.")
    for i, m in enumerate(splits):
        header = m.group(1).strip()
        canonical = get_canonical_section(header)

        start = m.end()
        end = splits[i+1].start() if i+1 < len(splits) else len(bilingual_content)
        body = bilingual_content[start:end].strip()

        patterns = extract_english_sentences(body)
        if patterns:
            if canonical not in sections:
                sections[canonical] = []
            sections[canonical].extend(patterns)
            log(citekey, f"PARSE: Extracted {len(patterns)} sentences from '{header}' -> '{canonical}'")

    return sections

def main():
    log("SYSTEM", "Starting Writing Wiki Generation...")
    WIKI_WRITE_DIR.mkdir(parents=True, exist_ok=True)

    yearly_data = {} # year -> list of {citekey, title, sections}
    note_files = list(NOTES_RAW_DIR.glob("*.md"))
    log("SYSTEM", f"Found {len(note_files)} note files in {NOTES_RAW_DIR}")

    for note_path in note_files:
        citekey = note_path.stem
        try:
            with open(note_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            log(citekey, f"ERROR: Could not read file: {e}")
            continue

        # 1. Resolve Year
        year = "Unknown"
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            try:
                fm = yaml.safe_load(fm_match.group(1))
                if isinstance(fm, dict):
                    year = str(fm.get('dateY') or fm.get('year') or "Unknown")
                    if year == "Unknown" and 'date' in fm:
                        m_year = re.search(r'(\d{4})', str(fm['date']))
                        if m_year: year = m_year.group(1)
            except: pass

        if year == "Unknown":
            m_year = re.search(r'(\d{4})', citekey)
            if m_year: year = m_year.group(1)

        # 2. Extract Writing Sections
        writing_sections = parse_note_content(content, citekey)
        if not writing_sections:
            # log(citekey, "SKIP: No academic writing patterns found.")
            continue

        # 3. Resolve Title
        title_match = re.search(r'^title::\s*(.*)', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else citekey

        if year not in yearly_data:
            yearly_data[year] = []

        yearly_data[year].append({
            "citekey": citekey,
            "title": title,
            "sections": writing_sections
        })
        log(citekey, f"COLLECT: Added to year {year} with {sum(len(v) for v in writing_sections.values())} total sentences.")

    # 4. Generate Yearly Wiki Pages
    for year, papers in sorted(yearly_data.items(), reverse=True):
        out_file = WIKI_WRITE_DIR / f"{year}.md"
        log("GENERATE", f"Creating wiki page for year {year} ({len(papers)} papers)...")

        md_content = [
            f"# Academic Writing Patterns: {year}",
            "",
            f"> 本页面聚合了 {year} 年发表的文献中的核心学术表达、逻辑转承与写作用词。",
            "",
            "[[_index|← 返回总索引]]",
            "",
            "---",
            ""
        ]

        # Group by canonical section across all papers in that year
        agg_sections = {}
        for paper in papers:
            for sec_name, patterns in paper["sections"].items():
                if sec_name not in agg_sections:
                    agg_sections[sec_name] = []
                agg_sections[sec_name].append({
                    "title": paper["title"],
                    "citekey": paper["citekey"],
                    "patterns": patterns
                })

        # Define order of display
        display_order = ["Introduction", "Methods", "Results & Discussion", "Conclusion", "General", "Other"]

        for sec_name in display_order:
            if sec_name not in agg_sections: continue

            md_content.append(f"## 📝 {sec_name}")
            for entry in agg_sections[sec_name]:
                # Link back to the original note in raw/note/
                note_link = f"[[../../raw/note/{entry['citekey']}|{entry['title']}]]"
                md_content.append(f"### From: {note_link}")

                # Deduplicate and limit patterns for brevity in the summary page
                unique_patterns = list(dict.fromkeys(entry["patterns"]))
                for p in unique_patterns[:8]: # Limit to top 8 unique patterns
                    md_content.append(f"- {p}")
                md_content.append("")
            md_content.append("---")

        with open(out_file, "w", encoding="utf-8") as f:
            f.write("\n".join(md_content))
        log("GENERATE", f"Saved {out_file.name}")

    # 5. Generate _index.md
    index_file = WIKI_WRITE_DIR / "_index.md"
    log("INDEX", "Updating Writing Wiki Index...")
    index_content = [
        "# 学术写作用词与思路索引 (Writing Style Index)",
        "",
        "> [!INFO] 查看指引",
        "> 本库通过分析文献的“双语转写”部分，按年份聚合了不同研究阶段（引言、方法、讨论、结论）的学术用词与写作逻辑。",
        "",
        "## 按年份浏览",
        "",
        "| 年份 | 文献总数 | 核心链接 |",
        "| :--- | :--- | :--- |"
    ]

    total_papers = 0
    for year in sorted(yearly_data.keys(), reverse=True):
        count = len(yearly_data[year])
        total_papers += count
        index_content.append(f"| {year} | {count} | [[{year}\|查看 {year} 年写作总结]] |")

    index_content.extend([
        "",
        "## 检索建议",
        "- **按模块学习**：如果你正在写 Introduction，可以点击不同年份的页面，直接定位到 `## Introduction` 模块查看表达方式。",
        "- **快速跳转**：点击来源文献链接可直接回到原始双语笔记查看上下文。",
        "",
        f"*最后更新统计: 扫描 {len(note_files)} 篇文献，识别出 {total_papers} 篇包含有效写作模式的文献，生成 {len(yearly_data)} 个年度索引。*",
        f"*更新时间: {Path(__file__).stat().st_mtime} (Unix Epoch)*"
    ])

    with open(index_file, "w", encoding="utf-8") as f:
        f.write("\n".join(index_content))
    log("INDEX", f"Generated index at {index_file.name}")
    log("SYSTEM", "Writing Wiki Generation Complete.")

if __name__ == "__main__":
    main()
