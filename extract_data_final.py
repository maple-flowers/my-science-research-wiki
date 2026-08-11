import os
import json
import re
import sys

def clean_text(text):
    if not text:
        return ""
    # Remove markdown bold/italic
    text = re.sub(r'\*\*|\*', '', text)
    # Remove blockquote prefix
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove excessive newlines
    text = re.sub(r'\n+', ' ', text)
    return text.strip()

def split_items(text):
    if not text:
        return []
    # Use a safer regex for splitting
    # Replace numbered list markers with a consistent delimiter
    text = re.sub(r'\d+[.\)]\s*', '||', text)
    # Split by common separators
    items = re.split(r'[;；。\|]', text)
    return [i.strip() for i in items if i.strip() and len(i.strip()) > 1]

def extract_from_files():
    note_dir = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\raw\note"
    files = [f for f in os.listdir(note_dir) if f.endswith('.md')]

    results = []

    for filename in files:
        filepath = os.path.join(note_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

                # Extract qnkey (citekey)
                citekey_match = re.search(r'qnkey::\s*(.*)', content)
                citekey = citekey_match.group(1).strip() if citekey_match else os.path.splitext(filename)[0]

                # Extract title
                title = ""
                # Priority 1: title:: or 标题: in metadata sections
                t_match = re.search(r'(?:title|标题|title::)\s*[:：]\s*(.*)', content, re.IGNORECASE)
                if t_match:
                    title = clean_text(t_match.group(1))

                # Priority 2: first # Header
                if not title:
                    h1_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
                    if h1_match:
                        title = clean_text(h1_match.group(1))

                # Extract year
                year_match = re.search(r'dateY::\s*(\d{4})', content)
                year = year_match.group(1).strip() if year_match else ""

                # Extract materials
                materials = []
                # Look for the section in the AI summary or metadata
                m_match = re.search(r'主要研究对象\s*[:：]{2}\s*(.*?)(?=\n\s*[\w\u4e00-\u9fa5]+[：:]{2}|\n\s*##|\n\s*%|\Z)', content, re.DOTALL)
                if m_match:
                    materials = split_items(clean_text(m_match.group(1)))

                # Extract methods
                methods = []
                meth_match = re.search(r'主要研究方法\s*[:：]{2}\s*(.*?)(?=\n\s*[\w\u4e00-\u9fa5]+[：:]{2}|\n\s*##|\n\s*%|\Z)', content, re.DOTALL)
                if meth_match:
                    methods = split_items(clean_text(meth_match.group(1)))

                results.append({
                    "citekey": citekey,
                    "title": title,
                    "year": year,
                    "materials": materials,
                    "methods": methods
                })
        except Exception:
            continue

    return results

if __name__ == "__main__":
    data = extract_from_files()
    output_path = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\results.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Successfully extracted {len(data)} items to {output_path}")
