const fs = require('fs');
const path = require('path');
const DST_ROOT = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/wiki';
const pages = [
  'concepts/interlayer-polarization-coupling.md',
  'concepts/sliding-ferroelectricity.md',
  'entities/HgI2.md',
  'entities/InSe.md',
  'entities/ReS2.md',
];
const report = [];
for (const rel of pages) {
  const p = path.join(DST_ROOT, rel);
  if (!fs.existsSync(p)) { report.push('MISS ' + rel); continue; }
  let t = fs.readFileSync(p, 'utf8');
  // 在 frontmatter 闭合标记后补 status: mature
  const m = t.match(/^---\n([\s\S]*?)\n---/);
  if (!m) { report.push('NO_FM ' + rel); continue; }
  if (/^status:/m.test(m[1])) { report.push('HAS_STATUS ' + rel); continue; }
  const newT = '---\n' + m[1] + '\nstatus: mature\n---' + t.slice(m[0].length);
  fs.writeFileSync(p, newT, 'utf8');
  report.push('OK ' + rel);
}
console.log(report.join('\n'));
