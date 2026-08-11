import os
import json
import re

def extract_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    citekey = os.path.splitext(os.path.basename(file_path))[0]

    # Extract Title
    title_match = re.search(r'^title::\s*(.*)$', content, re.MULTILINE)
    if not title_match:
        title_match = re.search(r'^标题:\s*(.*)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""

    # Extract Year
    year_match = re.search(r'^dateY::\s*(\d{4})$', content, re.MULTILINE)
    if not year_match:
        year_match = re.search(r'^date::\s*(\d{4})$', content, re.MULTILINE)
    year = year_match.group(1).strip() if year_match else ""

    # Extract Materials (from 主要研究对象)
    materials = []
    materials_match = re.search(r'^主要研究对象::\s*(.*)$', content, re.MULTILINE)
    if materials_match:
        m_str = materials_match.group(1).strip()
        # Basic splitting by common delimiters
        materials = [item.strip() for item in re.split(r'[;；,，]', m_str) if item.strip()]

    # Extract Methods (from 主要研究方法)
    methods = []
    methods_match = re.search(r'^主要研究方法::\s*(.*)$', content, re.MULTILINE)
    if methods_match:
        met_str = methods_match.group(1).strip()
        methods = [item.strip() for item in re.split(r'[;；,，]', met_str) if item.strip()]

    return {
        "citekey": citekey,
        "title": title,
        "year": year,
        "materials": materials,
        "methods": methods
    }

def main():
    directory = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\raw\note"
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.md')]

    results = []
    for f in files:
        try:
            results.append(extract_metadata(f))
        except Exception as e:
            # Silently skip or log errors if needed, but for this task we want output
            pass

    print(json.dumps(results, ensure_ascii=False))

if __name__ == "__main__":
    main()
