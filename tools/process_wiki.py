import os
import json
import re

KEYWORDS = ["raman", "phonon", "vibrational", "spectrum", "spectra", "IR", "infrared", "拉曼", "声子", "振动"]

def matches(text):
    if not text:
        return False
    text = text.lower()
    for kw in KEYWORDS:
        if kw in text:
            return True
    return False

def get_md_content(citekey, item_id, title, description, file_path):
    # This is a simplified version, real entries have Zotero metadata
    # But for figures we can use a standard format
    return f"### {citekey} - {item_id}\n\n"

# 1. Read existing file to find what's already there
wiki_path = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\wiki\figures\vibrational-spectra.md"
with open(wiki_path, 'r', encoding='utf-8') as f:
    existing_content = f.read()

# Identify existing citekey - item_id pairs
existing_items = set(re.findall(r"### ([\w-]+ - (?:Figure|Table|Formula|Equation) [\w-]+)", existing_content))

# 2. Scan manifests
all_found = {"Figures": [], "Tables": [], "Formulas": []}
base_dir = "raw/figures"
for root, dirs, files in os.walk(base_dir):
    if "manifest.json" in files:
        manifest_path = os.path.join(root, "manifest.json")
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            parent_key = data.get("parent_key", "")
            
            # Figures
            for fig in data.get("figures", []):
                item_id = f"Figure {fig.get('fig_number')}"
                full_id = f"{parent_key} - {item_id}"
                if matches(fig.get("title")) or matches(fig.get("llm_description")):
                    if full_id not in existing_items:
                        all_found["Figures"].append({
                            "citekey": parent_key,
                            "item_id": item_id,
                            "title": fig.get("title"),
                            "description": fig.get("llm_description"),
                            "file": fig.get("file"),
                            "path": os.path.abspath(os.path.join(root, fig.get("file"))).replace("\\", "/"),
                            "page": fig.get("page")
                        })
            
            # Tables
            for tab in data.get("tables", []):
                item_id = f"Table {tab.get('id')}"
                full_id = f"{parent_key} - {item_id}"
                if matches(tab.get("title", "")) or matches(tab.get("content", "")):
                    if full_id not in existing_items:
                        # For tables, we usually want the MD-T1 if possible
                        all_found["Tables"].append({
                            "citekey": parent_key,
                            "item_id": item_id,
                            "title": tab.get("title"),
                            "description": tab.get("content"),
                            "file": tab.get("file", ""),
                            "path": os.path.abspath(os.path.join(root, tab.get("file", ""))).replace("\\", "/") if tab.get("file") else ""
                        })

            # Formulas
            for form in data.get("formulas", []):
                item_id = f"Formula {form.get('id')}"
                if "Equation" in form.get("title", ""):
                     item_id = f"Equation {form.get('id')}"
                full_id = f"{parent_key} - {item_id}"
                if matches(form.get("title")) or matches(form.get("content")):
                    if full_id not in existing_items:
                        all_found["Formulas"].append({
                            "citekey": parent_key,
                            "item_id": item_id,
                            "title": form.get("title"),
                            "description": form.get("content"),
                            "file": form.get("file", ""),
                            "path": os.path.abspath(os.path.join(root, form.get("file", ""))).replace("\\", "/") if form.get("file") else ""
                        })

        except Exception as e:
            pass

print(json.dumps(all_found, indent=2, ensure_ascii=False))
