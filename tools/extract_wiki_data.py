import os
import json
import re

def extract_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    citekey = os.path.splitext(os.path.basename(file_path))[0]

    # Extract Title
    title_match = re.search(r'^[> ]*title::\s*(.*)$', content, re.MULTILINE)
    if not title_match:
        title_match = re.search(r'^[> ]*标题:\s*(.*)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""

    # Extract Year
    year_match = re.search(r'^[> ]*dateY::\s*(\d{4})$', content, re.MULTILINE)
    if not year_match:
        year_match = re.search(r'^[> ]*date::\s*(\d{4})$', content, re.MULTILINE)
    year = year_match.group(1).strip() if year_match else ""

    # Extract Materials (from 主要研究对象 or Metadata)
    materials = []
    materials_match = re.search(r'^[> ]*主要研究对象::\s*(.*)$', content, re.MULTILINE)
    if materials_match:
        m_str = materials_match.group(1).strip()
        materials = [item.strip() for item in re.split(r'[;；,，]', m_str) if item.strip()]

    # Fallback to scanning content for chemical formulas if empty
    if not materials:
        # Simple heuristic for chemical formulas like In2Se3, BiFeO3
        chem_matches = re.findall(r'\b([A-Z][a-z]?\d?[A-Z][a-z]?\d?[a-z0-9]*)\b', content)
        materials = list(set([m for m in chem_matches if len(m) > 2]))[:5]

    # Extract Methods (from 主要研究方法)
    methods = []
    methods_match = re.search(r'^[> ]*主要研究方法::\s*(.*)$', content, re.MULTILINE)
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
    output_path = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\tools\extracted_results.json"
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.md')]

    results = []
    for f in files:
        try:
            results.append(extract_metadata(f))
        except Exception as e:
            # print(f"Error processing {f}: {e}")
            pass

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"Successfully extracted {len(results)} files to {output_path}")

if __name__ == "__main__":
    main()
