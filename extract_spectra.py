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

results = {"figures": [], "tables": [], "formulas": []}

base_dir = "raw/figures"
for root, dirs, files in os.walk(base_dir):
    if "manifest.json" in files:
        manifest_path = os.path.join(root, "manifest.json")
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            parent_key = data.get("parent_key", "")
            
            # Check figures
            for fig in data.get("figures", []):
                if matches(fig.get("title")) or matches(fig.get("llm_description")):
                    results["figures"].append({
                        "citekey": parent_key,
                        "item_id": f"Figure {fig.get('fig_number')}",
                        "title": fig.get("title"),
                        "description": fig.get("llm_description"),
                        "file": fig.get("file"),
                        "path": os.path.join(root, fig.get("file")).replace("\\", "/")
                    })
            
            # Check tables
            for tab in data.get("tables", []):
                if matches(tab.get("title")) or matches(tab.get("content")):
                    results["tables"].append({
                        "citekey": parent_key,
                        "item_id": f"Table {tab.get('id')}",
                        "title": tab.get("title"),
                        "description": tab.get("content"),
                        "file": tab.get("file", ""),
                        "path": os.path.join(root, tab.get("file", "")).replace("\\", "/") if tab.get("file") else ""
                    })

            # Check formulas
            for form in data.get("formulas", []):
                if matches(form.get("title")) or matches(form.get("content")):
                    results["formulas"].append({
                        "citekey": parent_key,
                        "item_id": f"Formula {form.get('id')}",
                        "title": form.get("title"),
                        "description": form.get("content"),
                        "file": form.get("file", ""),
                        "path": os.path.join(root, form.get("file", "")).replace("\\", "/") if form.get("file") else ""
                    })

        except Exception as e:
            pass

print(json.dumps(results, indent=2, ensure_ascii=False))
