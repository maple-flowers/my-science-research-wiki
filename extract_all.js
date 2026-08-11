const fs = require('fs');
const path = require('path');

const noteDir = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/raw/note';

function parseFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split(/\r?\n/);

    const data = {
      qnkey: null,
      title: null,
      dateY: null,
      materialsStr: null,
      methodsStr: null,
      yamlTitle: null,
      yamlDate: null,
      h1Title: null
    };

    // 1. First H1
    for (const line of lines) {
      if (line.startsWith('# ')) {
        data.h1Title = line.substring(2).trim();
        break;
      }
    }

    // 2. YAML Frontmatter
    let inFrontmatter = false;
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();
      if (line === '---') {
        if (!inFrontmatter && i === 0) inFrontmatter = true;
        else if (inFrontmatter) { inFrontmatter = false; break; }
      } else if (inFrontmatter) {
        const match = line.match(/^([^:]+):\s*(.*)$/);
        if (match) {
          const k = match[1].trim();
          const v = match[2].trim();
          if (k === '中文标题') data.yamlTitle = v;
          else if (k === 'date' || k === 'dateY') data.yamlDate = v;
        }
      }
    }

    // 3. Dataview fields (multi-line)
    // Looking for lines like "Key:: Value"
    // Also handling the case where Key:: is preceded by symbols or Markdown syntax
    for (const line of lines) {
      const trimmed = line.trim();
      // We look for the presence of "::"
      const dvMatch = trimmed.match(/(?:^|[\s>\[\(])([^:\[\]\(\)\s>][^:\[\]\(\)>]*?)::\s*(.*)$/);
      if (dvMatch) {
        let key = dvMatch[1].trim();
        let val = dvMatch[2].trim();

        // Clean up key
        if (key.startsWith('>')) key = key.substring(1).trim();

        // Map keys
        if (key === 'qnkey') data.qnkey = val;
        else if (key === 'title') data.title = val;
        else if (key === 'dateY') data.dateY = val;
        else if (key === 'date' && !data.dateY) data.dateY = val;
        else if (key === '主要研究对象') data.materialsStr = val;
        else if (key === '主要研究方法') data.methodsStr = val;
      }
    }

    // Final value selection
    const citekey = data.qnkey || path.basename(filePath, '.md');
    const title = data.title || data.yamlTitle || data.h1Title || citekey;

    let year = data.dateY || data.yamlDate || "";
    const yearMatch = String(year).match(/\b(19|20)\d{2}\b/);
    year = yearMatch ? yearMatch[0] : "";
    if (!year) {
      const citekeyYearMatch = citekey.match(/\b(19|20)\d{2}\b/);
      if (citekeyYearMatch) year = citekeyYearMatch[0];
    }

    const splitList = (str) => {
      if (!str) return [];

      // Clean up surrounding brackets/parens if the whole thing is wrapped
      str = str.trim();
      if (str.startsWith('[') && str.endsWith(']')) str = str.slice(1, -1).trim();
      if (str.startsWith('(') && str.endsWith(')')) str = str.slice(1, -1).trim();

      // Detection for numbered/bullet lists
      const listMarkers = /((?:\d+[\)\.])|(?:[①-⑩]))/;
      if (listMarkers.test(str)) {
        // Split by markers, but keep them temporarily to identify segments
        const parts = str.split(new RegExp(`(?=${listMarkers.source})`));
        const items = parts
          .map(p => p.replace(new RegExp(`^${listMarkers.source}\\s*`), '').trim())
          .map(p => p.replace(/[。；;]$/, '').trim())
          .filter(p => p.length > 0 && p !== str);

        if (items.length > 0) return items;
      }

      // Default split by various separators
      return str.split(/[、；，;,\n]+/)
        .map(p => p.trim())
        .map(p => p.replace(/[。]$/, '').trim())
        .filter(p => p.length > 0);
    };

    let materials = splitList(data.materialsStr);
    let methods = splitList(data.methodsStr);

    // Fallback if list splitting resulted in nothing but string exists
    if (materials.length === 0 && data.materialsStr) {
      materials = [data.materialsStr.replace(/[。]$/, '').trim()];
    }
    if (methods.length === 0 && data.methodsStr) {
      methods = [data.methodsStr.replace(/[。]$/, '').trim()];
    }

    return {
      citekey,
      title,
      year: String(year),
      materials,
      methods
    };
  } catch (e) {
    return null;
  }
}

const files = fs.readdirSync(noteDir).filter(f => f.endsWith('.md'));
const results = [];

for (const file of files) {
  const fullPath = path.join(noteDir, file);
  const parsed = parseFile(fullPath);
  if (parsed) {
    results.push(parsed);
  }
}

process.stdout.write(JSON.stringify({ papers: results }, null, 2));
