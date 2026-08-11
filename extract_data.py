import os
import json
import re
import sys

# Ensure stdout uses utf-8
sys.stdout.reconfigure(encoding='utf-8')

note_dir = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\raw\note"
files = [f for f in os.listdir(note_dir) if f.endswith('.md')]

results = []

def clean_text(text):
    if not text:
        return ""
    # Remove markdown bold/italic
    text = re.sub(r'\*\*|\*', '', text)
    # Remove blockquote prefix
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

def split_items(text):
    if not text:
        return []
    # Split by semicolon, period, or Chinese separators
    # Also handle numbered lists like 1), 2) or 1., 2.
    text = re.sub(r'\d+[.\)]\s*', '||', text)
    items = re.split(r'[;；。||]', text)
    return [i.strip() for i in items if i.strip() and len(i.strip()) > 1]

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
            # Priority 1: title:: or 标题: in first lines or metadata
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

            # Extract materials - using a negative lookahead to stop at the next key
            # We look for the start of the next "Key::" or a header
            materials = []
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
    except Exception as e:
        pass

print(json.dumps(results, ensure_ascii=False, indent=2))
