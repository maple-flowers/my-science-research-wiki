# Plan: Refactor Research Asset System & Intelligent Wiki Update

This plan overhauls the figure, table, and formula tracking system, introduces an agentic workflow for maintaining the research wiki, and migrates Project 5 to its new theme. It distinguishes between mechanical "raw" ingestion (Python) and intelligent "wiki" synthesis (LLM Workflow).

## Context
The user manages a research wiki where paper notes are stored in Obsidian. They want a clear separation:
1. **Raw Ingestion**: Python scripts to sync Zotero assets and metadata into `raw/figures/` and `raw/note/`.
2. **Wiki Synthesis (Agent-Led)**: An LLM-driven workflow to update all knowledge layers (`concepts`, `entities`, `projects`, `figures`, and `write`) by synthesizing new information from the raw layer. **Crucially, academic writing pattern extraction is now moved from Python to the LLM Workflow for higher quality.**

## Proposed Changes

### 1. `科研Wiki/tools/update_raw_assets.py` & `run_ingest.py` (Mechanical Ingest)
- **Role**: Sync images and extract structural metadata (manifest.json).
- **Encoding Fix**: Use robust byte-stream logging to handle Windows GBK/UTF-8 conflicts.
- **Run Ingest**: Now only triggers `update_raw_assets.py`. The `generate_writing_wiki.py` script is superseded by the Agent Workflow.

### 2. `.claude/workflows/update_research_wiki.js` (Agentic Synthesis)
- **Phase 1-2: Discovery & Mapping**: Identify new papers and map them to Wiki files.
- **Phase 3: Synthesis**: 
    - **Concepts/Entities**: Integrate physical insights and mechanisms.
    - **Projects**: Update progress logs and literature mappings for the 7 core projects.
    - **Figures**: Catalog new figures/tables/formulas from `manifest.json` into thematic wiki pages.
- **Phase 4: Writing Analysis (LLM)**: Agents extract professional academic sentences from the bilingual transcription sections of `raw/note/*.md` and update `wiki/write/{year}.md`. This ensures only high-quality, relevant patterns are captured.
- **Phase 5: Indexing**: Rebuild `index.md`.

### 3. Project 5 Migration (Completed)
- SnTe ferroelectric simulation focus.

## Critical Files
- `科研Wiki/tools/run_ingest.py` (Updated to remove python writing script)
- `.claude/workflows/update_research_wiki.js` (Major logic for all Wiki updates)
- `科研Wiki/update.md` (Update instructions)

## Implementation Steps
1. **Update `run_ingest.py`**: Remove the call to `generate_writing_wiki.py`.
2. **Refine `update_research_wiki.js`**: Implement the full synthesis logic for figures, projects, and writing patterns.
3. **Run Mechanical Ingest**: Sync assets.
4. **Run Intelligent Workflow**: Perform the full wiki update.

## Verification Plan
- **Synthesis Quality**: Check `wiki/write/2026.md` (or relevant year) to ensure it contains agent-extracted sentences.
- **Cross-Linking**: Ensure new SnTe figures appear in `wiki/figures/structural-diagrams.md` if applicable.
- **Project Progress**: Check `wiki/projects/project-5-snte-ferroelectric-sim.md` for literature updates.

