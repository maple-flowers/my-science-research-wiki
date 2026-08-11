import os
import json

root_dir = "E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/raw/figures"
total_figures = 0
total_papers = 0

for subdir, dirs, files in os.walk(root_dir):
    if "manifest.json" in files:
        total_papers += 1
        manifest_path = os.path.join(subdir, "manifest.json")
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                total_figures += len(data.get("figures", []))
                total_figures += len(data.get("tables", []))
                total_figures += len(data.get("formulas", []))
        except Exception as e:
            print(f"Error reading {manifest_path}: {e}")

print(f"Total papers with figures: {total_papers}")
print(f"Total figure elements: {total_figures}")
