#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Raw Assets (Figures, Tables, Formulas) from Zotero and Notes.
Mechanical ingestion only.
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
    print(f"[{citekey}] {msg}")

def fetch_zotero_figure_note(citekey):
    """Fetch 'Zotero Figure 结果' note using cli-anything-zotero CLI."""
    log(citekey, "FETCH: Requesting Zotero Figure note via CLI...")
    try:
        # Find the parent item
        res = subprocess.run(["cli-anything-zotero", "item", "find", citekey, "--json"], capture_output=True, text=True)
        if res.returncode != 0 or not res.stdout.strip():
            log(citekey, "FETCH: Parent item not found via CLI.")
            return None

        items = json.loads(res.stdout)
        if not items:
            log(citekey, "FETCH: Empty items list from CLI.")
            return None

        parent_key = items[0]["key"]

        # Get children
        res_children = subprocess.run(["cli-anything-zotero", "item", "children", parent_key, "--json"], capture_output=True, text=True)
        if res_children.returncode != 0:
            log(citekey, "FETCH: Failed to get children via CLI.")
            return None

        children = json.loads(res_children.stdout)
        for child in children:
            if child.get("typeName") == "note" and "Zotero Figure 结果" in child.get("title", ""):
                note_key = child["key"]
                log(citekey, f"FETCH: Found target note key: {note_key}")

                # Get note content
                res_note = subprocess.run(["cli-anything-zotero", "note", "get", note_key, "--json"], capture_output=True, text=True)
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

def extract_figures(note_text, citekey):
    figures = {}
    cleaned_text = clean_blockquotes(note_text)

    # Phase 1: Deep Analysis Section (Descriptions)
    m_sec3 = re.search(r'(##\s*三[、\.].*?)(##\s*(?:四[、\.]|.*?论文双语转写)|$)', cleaned_text, re.DOTALL)
    if m_sec3:
        sec_text = m_sec3.group(1)
        header_pattern = r'\n###\s*(?:\*\*|\*)?(?:\d+\.\d+\s*)?((?:图表?\s*|Figure\s*|Fig\.\s*|表\s*|Table\s*|Box\s*)(\d+|I+|[A-Z]))\s*[:：\.\-](.*?)(?:\*\*|\*)?\n'
        for m in re.finditer(header_pattern, sec_text, re.IGNORECASE):
            fig_num = m.group(2)
            title = m.group(3).strip()
            figures[fig_num] = {"title": title, "desc": "", "page": "-", "attachment_key": None}

    # Phase 2: Zotero Figure Results (Keys and Captions)
    z_match = re.search(r'(?:##\s*(?:<[^>]+>)?\s*(?:❸\s*)?|<h2>)Zotero Figure 结果(.*?)(?:##|</div>|$)', note_text, re.DOTALL | re.IGNORECASE)

    if z_match:
        z_text = z_match.group(1)
        pattern = r'(?:\*\*|<strong>)(?:Figure|Fig\.|图)\s*(\d+|I+|[A-Z])(?:\*\*|</strong>)\s*(?:·\s*第\s*(\d+)\s*页)?(.*?)(?=(?:\*\*|<strong>)(?:Figure|Fig\.|图)|##|<h2>|$)'

        for m in re.finditer(pattern, z_text, re.DOTALL | re.IGNORECASE):
            num = m.group(1)
            page = m.group(2) or "-"
            body = m.group(3).strip()

            key_match = re.search(r'data-attachment-key=["\']([A-Za-z0-9]+)["\']', body)
            key = key_match.group(1) if key_match else None
            caption = re.sub(r'<[^>]+>', '', body).strip()

            if num not in figures:
                figures[num] = {"title": f"Figure {num}", "desc": caption[:500], "page": page, "attachment_key": key}
            else:
                figures[num]["attachment_key"] = key
                figures[num]["page"] = page
                if not figures[num]["desc"]:
                    figures[num]["desc"] = caption[:500]

    return figures

def extract_tables(note_text):
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

def extract_formulas(note_text):
    formulas = []
    cleaned = clean_blockquotes(note_text)
    for i, m in enumerate(re.finditer(r'(?s)\$\$(.*?)\$\$', cleaned)):
        formulas.append({"id": f"eq{i+1}", "title": f"Equation {i+1}", "content": m.group(0).strip(), "page": "-"})
    return formulas

def sync_images(citekey, figures, target_dir):
    if not ZOTERO_STORAGE_DIR.exists():
        log(citekey, f"SYNC ERR: Zotero storage not found at {ZOTERO_STORAGE_DIR}")
        return []

    synced_files = []
    IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

    for num, info in figures.items():
        key = info.get("attachment_key")
        if not key:
            continue

        source_dir = ZOTERO_STORAGE_DIR / key
        if not source_dir.exists():
            continue

        for file_path in source_dir.iterdir():
            if file_path.suffix.lower() in IMAGE_EXTS:
                target_name = f"fig_{num}_{key}{file_path.suffix.lower()}"
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
    log(citekey, "PROCESS: Syncing raw assets...")
    target_dir = FIGURES_RAW_DIR / citekey
    target_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = target_dir / "manifest.json"

    manifest = {"parent_key": citekey, "title": "", "figures": [], "tables": [], "formulas": [], "tags": [], "materials": [], "methods": []}
    if manifest_path.exists():
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest.update(json.load(f))
        except: pass

    try:
        with open(note_path, "r", encoding="utf-8") as f:
            note_text = f.read()
    except:
        note_text = ""

    meta = extract_metadata_from_note(note_text)
    manifest["tags"] = list(set(manifest["tags"] + meta["tags"]))
    manifest["materials"] = list(set(manifest["materials"] + meta["materials"]))
    manifest["methods"] = list(set(manifest["methods"] + meta["methods"]))

    if not manifest["title"]:
        t_match = re.search(r'^title::\s*(.*)', note_text, re.MULTILINE)
        manifest["title"] = t_match.group(1).strip() if t_match else citekey

    figs_data = extract_figures(note_text, citekey)
    missing_keys = not figs_data or any(not f.get("attachment_key") for f in figs_data.values())
    if missing_keys:
        z_note = fetch_zotero_figure_note(citekey)
        if z_note:
            z_figs = extract_figures(z_note, citekey)
            for num, z_info in z_figs.items():
                if num not in figs_data:
                    figs_data[num] = z_info
                else:
                    if z_info.get("attachment_key"):
                        figs_data[num]["attachment_key"] = z_info["attachment_key"]
                    if z_info.get("page") != "-":
                        figs_data[num]["page"] = z_info["page"]

    sync_images(citekey, figs_data, target_dir)

    manifest_figs = []
    for num, info in sorted(figs_data.items(), key=lambda x: str(x[0])):
        entry = {
            "fig_number": num,
            "title": info["title"],
            "llm_description": info["desc"],
            "page": info["page"],
            "attachment_key": info.get("attachment_key"),
            "file": info.get("file", ""),
            "tags": manifest["tags"],
            "materials": manifest["materials"],
            "methods": manifest["methods"]
        }
        manifest_figs.append(entry)
    manifest["figures"] = manifest_figs
    manifest["tables"] = extract_tables(note_text)
    manifest["formulas"] = extract_formulas(note_text)

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

def main():
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
