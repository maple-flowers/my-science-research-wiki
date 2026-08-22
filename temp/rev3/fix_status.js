const fs = require('fs');
const path = require('path');

const WIKI = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/wiki';
const SRC = 'C:/Users/sgg/AppData/Roaming/Tencent/Marvis/User/oAN1i2V14p5-lhhSY365mxizlI-c/workspace/conv_1a0000cc73d_3cc2a0c40aa4/temp/rev3';

// 1) 修复后的 d-p-hybridization.md 覆盖落盘
const fixed = path.join(SRC, 'd-p-hybridization.md');
const dstDP = path.join(WIKI, 'concepts', 'd-p-hybridization.md');
fs.writeFileSync(dstDP, fs.readFileSync(fixed, 'utf8'), 'utf8');
console.log('OK overwrite concepts/d-p-hybridization.md -> ' + fs.statSync(dstDP).size + ' bytes');

// 2) 为缺 status 的 5 页补 status: mature
const targets = [
  'concepts/ferroelectric-metal.md',
  'concepts/magnetic-polar-metal.md',
  'concepts/metallic-ferroelectricity.md',
  'concepts/polar-metal.md',
  'entities/LiOsO3.md',
];

for (const rel of targets) {
  const p = path.join(WIKI, rel);
  if (!fs.existsSync(p)) { console.log('MISSING ' + rel); continue; }
  let content = fs.readFileSync(p, 'utf8');
  // frontmatter 结束标志
  const m = content.match(/^---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)/s);
  if (!m) { console.log('NO_FM ' + rel); continue; }
  const fmBlock = m[1];
  if (/^status\s*:/m.test(fmBlock)) { console.log('HAS_STATUS ' + rel); continue; }
  // 在 frontmatter 第一行(---之后)插入 status: mature
  const lines = content.split(/\r?\n/);
  // 找到第一个 --- 结束位置
  let idx = -1;
  for (let i = 0; i < lines.length; i++) {
    if (i > 0 && lines[i].trim() === '---') { idx = i; break; }
  }
  if (idx < 0) { console.log('PARSE_FAIL ' + rel); continue; }
  lines.splice(idx, 0, 'status: mature');
  content = lines.join('\n');
  fs.writeFileSync(p, content, 'utf8');
  console.log('FIXED ' + rel + ' -> ' + fs.statSync(p).size + ' bytes');
}
