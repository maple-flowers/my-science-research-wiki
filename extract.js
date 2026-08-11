const fs = require('fs');
const path = require('path');

const noteDir = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/raw/note';

function parseFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split(/\r?\n/);

  let qnkey = null;
  let title = null;
  let dateY = null;
  let materialsStr = null;
  let methodsStr = null;

  // 1. Fallback title from first H1 header
  let h1Title = null;
  for (const line of lines) {
    if (line.startsWith('# ')) {
      h1Title = line.substring(2).trim();
      break;
    }
  }

  // 2. Parse YAML Frontmatter
  let inFrontmatter = false;
  let yamlData = {};
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line === '---') {
      if (!inFrontmatter && i === 0) {
        inFrontmatter = true;
      } else if (inFrontmatter) {
        inFrontmatter = false;
        break;
      }
    } else if (inFrontmatter) {
      const match = line.match(/^([^:]+):\s*(.*)$/);
      if (match) {
        yamlData[match[1].trim()] = match[2].trim();
      }
    }
  }

  // 3. Parse Dataview inline fields
  for (const line of lines) {
    const trimmed = line.trim();
    // Match keys ending with ::
    if (trimmed.includes('::')) {
      const parts = trimmed.split('::');
      let key = parts[0].trim();
      let val = parts.slice(1).join('::').trim();

      // Clean up key
      if (key.startsWith('>')) key = key.substring(1).trim();
      if (key.startsWith('[') && key.endsWith(']')) key = key.slice(1, -1).trim();
      if (key.startsWith('(') && key.endsWith(')')) key = key.slice(1, -1).trim();

      // Clean up val
      if (val.startsWith('[') && val.endsWith(']')) val = val.slice(1, -1).trim();
      if (val.startsWith('(') && val.endsWith(')')) val = val.slice(1, -1).trim();

      if (key === 'qnkey') qnkey = val;
      if (key === 'title') title = val;
      if (key === 'dateY') dateY = val;
      if (key === '主要研究对象') materialsStr = val;
      if (key === '主要研究方法') methodsStr = val;
      if (key === 'date' && !dateY) {
        // Extract 4-digit year
        const yearMatch = val.match(/\b\d{4}\b/);
        if (yearMatch) dateY = yearMatch[0];
      }
    }
  }

  // Fallbacks
  const finalCitekey = qnkey || path.basename(filePath, '.md');
  const finalTitle = title || yamlData['中文标题'] || h1Title || finalCitekey;

  let finalYear = dateY || yamlData['dateY'] || yamlData['date'];
  if (!finalYear) {
    // Try to find year from file name or first 4-digit number
    const match = finalCitekey.match(/\b(19|20)\d{2}\b/);
    if (match) finalYear = match[0];
  }
  if (!finalYear) finalYear = "";

  // Helper to split materials and methods
  function splitList(str) {
    if (!str) return [];

    // Check for numbered list like 1) or 1. or ①
    // If it has numbered list, split by the numbers
    const numberedRegex = /(?:\d+[\)\.]|①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩)\s*/;
    if (numberedRegex.test(str)) {
      const parts = str.split(/(?=\d+[\)\.]|①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩)/);
      return parts
        .map(p => p.replace(/^(?:\d+[\)\.]|①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩)\s*/, '').trim())
        .map(p => p.replace(/[。；;]$/, '').trim())
        .filter(p => p.length > 0);
    }

    // Otherwise split by common Chinese/English punctuation
    const separators = /[、；，;,\n]+/;
    return str
      .split(separators)
      .map(p => p.trim())
      .map(p => p.replace(/[。]$/, '').trim())
      .filter(p => p.length > 0);
  }

  const materials = splitList(materialsStr);
  const methods = splitList(methodsStr);

  return {
    citekey: finalCitekey,
    title: finalTitle,
    year: String(finalYear),
    materials,
    methods
  };
}

// Test with 3 files
const testFiles = [
  'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/raw/note/Delley2000.md',
  'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/raw/note/Ahn2015ferroelectric.md',
  'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/raw/note/aiFerroelectricityCoexistedPorbital2022.md'
];

testFiles.forEach(f => {
  if (fs.existsSync(f)) {
    console.log(JSON.stringify(parseFile(f), null, 2));
  } else {
    console.log(`Not found: ${f}`);
  }
});
