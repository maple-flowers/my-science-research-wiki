const fs = require('fs');
const path = require('path');

const SRC = 'C:/Users/sgg/AppData/Roaming/Tencent/Marvis/User/oAN1i2V14p5-lhhSY365mxizlI-c/workspace/conv_1a0000cc73d_3cc2a0c40aa4/temp/rev3';
const DST_ROOT = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/wiki';

const jobs = [
  ['d0-magnetism.md', 'concepts/d0-magnetism.md'],
  ['d-p-hybridization.md', 'concepts/d-p-hybridization.md'],
  ['electron-filling-magnetism.md', 'concepts/electron-filling-magnetism.md'],
  ['d-orbital-hopping.md', 'concepts/d-orbital-hopping.md'],
  ['stoner-ferromagnetism.md', 'concepts/stoner-ferromagnetism.md'],
  ['bipolar-magnetic-semiconductor.md', 'concepts/bipolar-magnetic-semiconductor.md'],
  ['electron-hole-correlation.md', 'concepts/electron-hole-correlation.md'],
];

const report = [];
for (const [srcName, rel] of jobs) {
  const srcPath = path.join(SRC, srcName);
  const dstPath = path.join(DST_ROOT, rel);
  if (!fs.existsSync(srcPath)) { report.push('MISSING_SRC ' + srcPath); continue; }
  const dstDir = path.dirname(dstPath);
  if (!fs.existsSync(dstDir)) { report.push('MISSING_DST_DIR ' + dstDir); continue; }
  const content = fs.readFileSync(srcPath, 'utf8');
  fs.writeFileSync(dstPath, content, 'utf8');
  const stat = fs.statSync(dstPath);
  report.push('OK ' + rel + ' -> ' + stat.size + ' bytes');
}
console.log(report.join('\n'));
