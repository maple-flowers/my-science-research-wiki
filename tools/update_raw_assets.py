#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Raw Assets (Figures, Tables, Formulas) from Zotero and Notes.
Mechanical ingestion only. Extracts images for Figs, Tables, and Eqs.
"""

import os
import sys
import json
import re
import shutil
import subprocess
from pathlib import Path

# Configure paths
BASE_DIR = Path(r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki")
FIGURES_RAW_DIR = BASE_DIR / "raw" / "figures"
NOTES_RAW_DIR = BASE_DIR / "raw" / "note"
ZOTERO_STORAGE_DIR = Path(r"C:\Users\sgg\Zotero\storage")

def log(citekey, msg):
    try:
        # Forcite key or message might contain Chinese characters that GBK can't handle
        output = f"[{citekey}] {msg}"
        sys.stdout.buffer.write((output + "\n").encode('utf-8'))
        sys.stdout.flush()
    except Exception:
        try:
            print(f"[{citekey}] {msg.encode('ascii', 'replace').decode('ascii')}")
        except Exception:
            pass

def fetch_zotero_figure_note(citekey):
    """Fetch 'Zotero Figure 结果' note using cli-anything-zotero CLI."""
    log(citekey, "FETCH: Requesting Zotero Figure note via CLI...")
    try:
        res = subprocess.run(["cli-anything-zotero", "item", "find", citekey, "--json"], capture_output=True, text=True, encoding='utf-8', errors='replace')
        if res.returncode != 0 or not res.stdout.strip():
            log(citekey, "FETCH: Parent item not found via CLI.")
            return None

        items = json.loads(res.stdout)
        if not items:
            log(citekey, "FETCH: Empty items list from CLI.")
            return None

        parent_key = items[0]["key"]

        # Get children
        res_children = subprocess.run(["cli-anything-zotero", "item", "children", parent_key, "--json"], capture_output=True, text=True, encoding='utf-8', errors='replace')
        if res_children.returncode != 0:
            log(citekey, "FETCH: Failed to get children via CLI.")
            return None

        children = json.loads(res_children.stdout)
        for child in children:
            if child.get("typeName") == "note" and "Zotero Figure 结果" in child.get("title", ""):
                note_key = child["key"]
                log(citekey, f"FETCH: Found target note key: {note_key}")

                # Get note content
                res_note = subprocess.run(["cli-anything-zotero", "note", "get", note_key, "--json"], capture_output=True, text=True, encoding='utf-8', errors='replace')
                if res_note.returncode == 0:
                    note_data = json.loads(res_note.stdout)
                    return note_data.get("noteContent") or note_data.get("noteText")

    except Exception as e:
        log(citekey, f"FETCH ERR: {e}")
    return None

def clean_blockquotes(text):
    if not text: return ""
    lines = text.split('\n')
    cleaned = []
    for line in lines:
        m = re.match(r'^\s*>\s?(.*)', line)
        if m:
            cleaned.append(m.group(1))
        else:
            cleaned.append(line)
    return '\n'.join(cleaned)

def extract_metadata_from_note(note_text):
    meta = {"tags": [], "materials": [], "methods": []}
    if not note_text: return meta

    # 1. Frontmatter
    fm_match = re.search(r'^---\n(.*?)\n---', note_text, re.DOTALL)
    if fm_match:
        for line in fm_match.group(1).split('\n'):
            for field in ['tags', 'materials', 'methods']:
                if line.startswith(f'{field}:'):
                    val_str = line.split(':', 1)[1].strip()
                    vals = [v.strip(' "\'[]') for v in val_str.split(',') if v.strip()]
                    meta[field].extend(vals)

    # 2. Dataview fields
    for line in note_text.split('\n'):
        m_tags = re.search(r'tags::\s*(.*)', line)
        if m_tags:
            for t in re.findall(r'#([^\s#]+)', m_tags.group(1)):
                if '材料：' in t or '材料:' in t:
                    meta['materials'].append(re.sub(r'^材料[：:]', '', t).strip())
                elif t not in ['🤖️', 'reading', '📝']:
                    meta['tags'].append(t)

    meta['tags'] = list(dict.fromkeys(meta['tags']))
    meta['materials'] = list(dict.fromkeys(meta['materials']))
    meta['methods'] = list(dict.fromkeys(meta['methods']))
    return meta

def extract_zotero_assets(note_text, citekey):
    """Extract Figures, Tables, and Equations from the 'Zotero Figure 结果' section."""
    assets = {"figure": {}, "table": {}, "equation": {}}

    # Try finding the content after "Zotero Figure 结果"
    z_match = re.search(r'(?:##\s*(?:<[^>]+>)?\s*(?:❸\s*)?|<h2>)Zotero Figure 结果(.*?)(?:##|</div>|$)', note_text, re.DOTALL | re.IGNORECASE)

    if z_match:
        z_text = z_match.group(1)
        # Match Type (Fig/Table/Eq), number, optional page, and following content
        pattern = r'(?:\*\*|<strong>)(Figure|Fig\.|图|Table|表|Equation|Formula|公式|Eq\.)\s*(\d+|I+|[A-Z])(?:\*\*|</strong>)\s*(?:·\s*第\s*(\d+)\s*页)?(.*?)(?=(?:\*\*|<strong>)(?:Figure|Fig\.|图|Table|表|Equation|Formula|公式|Eq\.)|##|<h2>|$)'

        for m in re.finditer(pattern, z_text, re.DOTALL | re.IGNORECASE):
            type_raw = m.group(1).lower()
            num = m.group(2)
            page = m.group(3) or "-"
            body = m.group(4).strip()

            # Map to canonical types
            category = "figure"
            if any(kw in type_raw for kw in ["table", "表"]): category = "table"
            elif any(kw in type_raw for kw in ["equation", "formula", "公式", "eq"]): category = "equation"

            key_match = re.search(r'data-attachment-key=["\']([A-Za-z0-9]+)["\']', body)
            key = key_match.group(1) if key_match else None
            caption = re.sub(r'<[^>]+>', '', body).strip()

            assets[category][num] = {
                "title": f"{category.capitalize()} {num}",
                "desc": caption[:500],
                "page": page,
                "attachment_key": key
            }
    return assets

def extract_tables_content(note_text):
    tables = []
    cleaned = clean_blockquotes(note_text)
    # HTML Tables
    for i, m in enumerate(re.finditer(r'(?s)<table.*?>.*?</table>', cleaned, re.IGNORECASE)):
        tables.append({"id": f"T{i+1}", "title": f"Table {i+1}", "content": m.group(0), "page": "-"})
    # Markdown Tables
    md_pattern = r'\n\|[^\n]+\n\|[-| :]+\n(?:\|[^\n]+\n)+'
    for i, m in enumerate(re.finditer(md_pattern, cleaned)):
        tables.append({"id": f"MD-T{i+1}", "title": f"MD Table {i+1}", "content": m.group(0).strip(), "page": "-"})
    return tables

def extract_formulas_content(note_text):
    formulas = []
    cleaned = clean_blockquotes(note_text)
    for i, m in enumerate(re.finditer(r'(?s)\$\$(.*?)\$\$', cleaned)):
        formulas.append({"id": f"eq{i+1}", "title": f"Equation {i+1}", "content": m.group(0).strip(), "page": "-"})
    return formulas

def sync_category_images(citekey, items, target_dir, prefix_char):
    """Sync images for a specific category (figures, tables, equations)."""
    if not ZOTERO_STORAGE_DIR.exists():
        return []

    synced_files = []
    IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

    for num, info in items.items():
        key = info.get("attachment_key")
        if not key: continue

        source_dir = ZOTERO_STORAGE_DIR / key
        if not source_dir.exists(): continue

        for file_path in source_dir.iterdir():
            if file_path.suffix.lower() in IMAGE_EXTS:
                # Format: {prefix}_{num}_{key}.ext (e.g., fig_1_ABC.png, tab_1_DEF.png)
                target_name = f"{prefix_char}_{num}_{key}{file_path.suffix.lower()}"
                target_path = target_dir / target_name

                try:
                    if not target_path.exists():
                        shutil.copy2(file_path, target_path)
                        log(citekey, f"SYNC: Copied {file_path.name} -> {target_name}")
                    synced_files.append(str(target_path.relative_to(BASE_DIR)))
                    info["file"] = target_name
                except Exception as e:
                    log(citekey, f"SYNC ERR copying {file_path.name}: {e}")
    return synced_files

def process_paper(citekey, note_path):
    log(citekey, f"PROCESS: Starting to sync raw assets from {note_path}...")
    target_dir = FIGURES_RAW_DIR / citekey
    target_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = target_dir / "manifest.json"

    manifest = {"parent_key": citekey, "title": "", "figures": [], "tables": [], "formulas": [], "tags": [], "materials": [], "methods": []}
    if manifest_path.exists():
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest.update(json.load(f))
            log(citekey, f"MANIFEST: Existing manifest.json loaded from {manifest_path}")
        except Exception as e:
            log(citekey, f"MANIFEST WARN: Failed to read existing manifest: {e}")

    try:
        with open(note_path, "r", encoding="utf-8", errors="replace") as f:
            note_text = f.read()
            log(citekey, f"READ: Read note file {note_path.name} successfully, size: {len(note_text)} chars")
    except Exception as e:
        log(citekey, f"READ ERR: Failed to read note file {note_path}: {e}")
        note_text = ""

    meta = extract_metadata_from_note(note_text)
    manifest["tags"] = list(set(manifest["tags"] + meta["tags"]))
    manifest["materials"] = list(set(manifest["materials"] + meta["materials"]))
    manifest["methods"] = list(set(manifest["methods"] + meta["methods"]))
    log(citekey, f"METADATA: Extracted tags:{meta['tags']}, materials:{meta['materials']}, methods:{meta['methods']}")

    if not manifest["title"]:
        t_match = re.search(r'^title::\s*(.*)', note_text, re.MULTILINE)
        manifest["title"] = t_match.group(1).strip() if t_match else citekey
        log(citekey, f"TITLE: Resolved title: {manifest['title']}")

    # Extract Assets from local note
    assets = extract_zotero_assets(note_text, citekey)
    log(citekey, f"EXTRACT: From note extracted Figs:{len(assets['figure'])}, Tabs:{len(assets['table'])}, Eqs:{len(assets['equation'])}")

    # If missing data, try Zotero CLI
    has_keys = any(items for items in assets.values() if any(f.get("attachment_key") for f in items.values()))
    if not has_keys:
        log(citekey, "FETCH: Missing attachment keys, falling back to Zotero CLI query...")
        z_note = fetch_zotero_figure_note(citekey)
        if z_note:
            log(citekey, "FETCH: Zotero Figure note found from CLI, extracting assets...")
            z_assets = extract_zotero_assets(z_note, citekey)
            log(citekey, f"FETCH: Zotero note extracted Figs:{len(z_assets['figure'])}, Tabs:{len(z_assets['table'])}, Eqs:{len(z_assets['equation'])}")
            # Merge
            for cat in assets:
                for num, info in z_assets[cat].items():
                    if num not in assets[cat]: assets[cat][num] = info
                    else:
                        if info.get("attachment_key"): assets[cat][num]["attachment_key"] = info["attachment_key"]
                        if info.get("page") != "-": assets[cat][num]["page"] = info["page"]
        else:
            log(citekey, "FETCH WARN: No note content retrieved from Zotero CLI.")

    # Sync Images for all categories
    log(citekey, "SYNC: Copying image files from Zotero storage...")
    synced_figs = sync_category_images(citekey, assets["figure"], target_dir, "fig")
    synced_tabs = sync_category_images(citekey, assets["table"], target_dir, "tab")
    synced_eqs = sync_category_images(citekey, assets["equation"], target_dir, "eq")
    log(citekey, f"SYNC DONE: Synced files counts -> Figs:{len(synced_figs)}, Tabs:{len(synced_tabs)}, Eqs:{len(synced_eqs)}")

    # Rebuild Figures
    manifest_figs = []
    for num, info in sorted(assets["figure"].items(), key=lambda x: str(x[0])):
        manifest_figs.append({
            "fig_number": num, "title": info["title"], "llm_description": info["desc"],
            "page": info["page"], "attachment_key": info.get("attachment_key"),
            "file": info.get("file", ""), "tags": manifest["tags"],
            "materials": manifest["materials"], "methods": manifest["methods"]
        })
    manifest["figures"] = manifest_figs

    # Rebuild Tables
    # Combine content-extracted (MD/HTML) and image-extracted (Zotero)
    content_tables = extract_tables_content(note_text)
    log(citekey, f"TABLES: Found {len(content_tables)} content-based tables in note")
    image_tables = []
    for num, info in sorted(assets["table"].items(), key=lambda x: str(x[0])):
        image_tables.append({
            "id": f"tab_{num}", "title": info["title"], "content": info["desc"],
            "page": info["page"], "attachment_key": info.get("attachment_key"),
            "file": info.get("file", "")
        })
    manifest["tables"] = image_tables + content_tables

    # Rebuild Formulas
    content_eqs = extract_formulas_content(note_text)
    log(citekey, f"FORMULAS: Found {len(content_eqs)} content-based formulas in note")
    image_eqs = []
    for num, info in sorted(assets["equation"].items(), key=lambda x: str(x[0])):
        image_eqs.append({
            "id": f"eq_{num}", "title": info["title"], "content": info["desc"],
            "page": info["page"], "attachment_key": info.get("attachment_key"),
            "file": info.get("file", "")
        })
    manifest["formulas"] = image_eqs + content_eqs

    try:
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)
        log(citekey, f"DONE: Manifest updated. Figs:{len(manifest_figs)}, Tabs:{len(manifest['tables'])}, Eqs:{len(manifest['formulas'])}")
    except Exception as e:
        log(citekey, f"WRITE MANIFEST ERR: {e}")

def main():
    try:
        sys.stdout.buffer.write("=== Raw Asset Sync Engine ===\n".encode('utf-8'))
        sys.stdout.flush()
    except Exception:
        print("=== Raw Asset Sync Engine ===")
    note_index = {}
    for p in NOTES_RAW_DIR.glob("*.md"):
        stem = p.stem
        m = re.search(r"KEY-([A-Za-z0-9]+)", stem)
        citekey = m.group(1) if m else stem
        note_index[citekey] = p

    if len(sys.argv) > 1:
        citekey = sys.argv[1]
        if citekey in note_index:
            process_paper(citekey, note_index[citekey])
    else:
        for citekey, path in note_index.items():
            process_paper(citekey, path)

if __name__ == "__main__":
    main()
