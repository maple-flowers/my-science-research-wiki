---
name: update-and-expand-research-wiki
description: Automate the synthesis and expansion of the Research Wiki, ensuring proper image rendering and clean project structure.
---

# Context
The user wants to keep the Research Wiki up-to-date with 531+ academic paper notes. This involves:
1. Updating existing Wiki pages with new findings.
2. Using standard Markdown image syntax (`![Title](path)`) with relative paths for all visual assets.
3. Automatically identifying and creating NEW Wiki pages for recurring concepts, entities, or topics found in the paper database.
4. Keeping the project root clean by using `tools/` for temporary files.

# Proposed Changes

## 1. Discovery and Expansion Analysis
- Use an agent to scan all 531 markdown files in `raw/note/`.
- Identify significant research clusters (materials, methods, concepts) that are frequently mentioned but lack a dedicated page in `wiki/`.
- Generate a list of proposed new files for `wiki/concepts/`, `wiki/entities/`, and `wiki/topics/`.

## 2. Update Workflow Script (`.claude/workflows/update_research_wiki.js`)
- **Formatting**: Reinforce `GLOBAL_TEMP_INSTRUCTION` to mandate Markdown image syntax.
- **Auto-Expansion Phase**: Add a new phase (or modify `Mapping`) that checks for the existence of proposed new pages and initializes them if they don't exist.
- **Refined Synthesis**: Ensure the subagents for each page are instructed to:
    - Search specifically for relevant papers.
    - Integrate findings into the narrative.
    - Embed relevant images from `raw/figures/{citekey}/` using the relative path syntax.
- **Writing Analysis**: Ensure yearly writing summaries are updated for all years present in the 531 papers.
- **Indexing**: Update `index.md` statistics and links to include the newly created pages.

## 3. Implementation of New Pages
- Based on the analysis, create initial versions of new Wiki pages.
- Let the workflow's synthesis phase populate them with detailed content.

# Verification Plan
1. Launch the updated workflow using `/workflow update_research_wiki`.
2. Verify that new Wiki pages (e.g., for specific materials like "CrTe2" or concepts like "Moire ferroelectricity") are created.
3. Check existing pages (e.g., `wiki/concepts/sliding-ferroelectricity.md`) to confirm they have been rewritten with new data and images.
4. Confirm `index.md` shows the correct paper count (531) and includes links to new pages.
5. Ensure no byproduct files (like `results.json`) remain in the root directory.
