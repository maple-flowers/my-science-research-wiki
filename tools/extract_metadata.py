import os
import re
import json
import glob

def clean_text(text):
    if not text:
        return ""
    # Remove markdown links [[ ]] or [ ]( )
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove bold/italic markers
    text = text.replace('**', '').replace('__', '').replace('*', '').replace('_', '')
    return text.strip()

def extract_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        data = {
            "citekey": None,
            "title": None,
            "year": None,
            "materials": [],
            "methods": []
        }
        
        # 1. Extract citekey (qnkey)
        citekey_match = re.search(r'qnkey::\s*([^\s\n\r|]+)', content)
        if citekey_match:
            data["citekey"] = citekey_match.group(1).strip()
        else:
            data["citekey"] = os.path.basename(file_path).replace('.md', '')
            
        # 2. Extract title
        title_match = re.search(r'title::\s*(.+)', content)
        if title_match:
            data["title"] = clean_text(title_match.group(1))
        else:
            fm_match = re.search(r'中文标题:\s*(.+)', content)
            if fm_match:
                data["title"] = clean_text(fm_match.group(1))
            else:
                h1_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
                if h1_match:
                    data["title"] = clean_text(h1_match.group(1))
        
        if not data["title"]:
            data["title"] = data["citekey"]
                
        # 3. Extract year
        year_match = re.search(r'dateY::\s*(\d{4})', content)
        if not year_match:
            year_match = re.search(r'date:\s*(\d{4})', content)
        if year_match:
            data["year"] = year_match.group(1).strip()
            
        # 4. Extract materials
        mat_patterns = [
            r'主要研究对象::\s*([^\n\r]+)',
            r'Materials?::\s*([^\n\r]+)',
            r'研究了([^\n\r。]+?)(?:的(?:性质|表征|输运|物理|电学))'
        ]
        for p in mat_patterns:
            matches = re.finditer(p, content)
            for m in matches:
                val = clean_text(m.group(1))
                if val and val not in data["materials"] and len(val) < 500:
                    data["materials"].append(val)
        
        # If still empty, try to guess from title (common materials like BiFeO3, SrTiO3, etc.)
        if not data["materials"]:
            common_mats = ["BiFeO3", "SrTiO3", "PbTiO3", "BaTiO3", "WTe2", "MoS2", "SnTe", "PbTe", "MXene"]
            for cm in common_mats:
                if cm.lower() in data["title"].lower():
                    data["materials"].append(cm)

        # 5. Extract methods
        meth_patterns = [
            r'主要研究方法::\s*([^\n\r]+)',
            r'Methods?::\s*([^\n\r]+)',
            r'采用([^\n\r。]+?)(?:(?:方法|技术|手段))'
        ]
        for p in meth_patterns:
            matches = re.finditer(p, content)
            for m in matches:
                val = clean_text(m.group(1))
                if val and val not in data["methods"] and len(val) < 500:
                    data["methods"].append(val)
        
        # Keyword based extraction for methods
        common_methods = ["DFT", "STM", "ARPES", "STEM", "PLD", "XRD", "PPMS", "SQUID", "第一性原理", "密度泛函理论", "压电力显微镜", "PFM"]
        for cmeth in common_methods:
            if cmeth in content and cmeth not in data["methods"]:
                data["methods"].append(cmeth)

        return data
    except Exception as e:
        return None

def main():
    directory = "E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/raw/note"
    files = glob.glob(os.path.join(directory, "*.md"))
    
    results = []
    for file_path in files:
        file_data = extract_from_file(file_path)
        if file_data:
            results.append(file_data)
            
    with open('tools/results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
