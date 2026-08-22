const fs = require('fs');
const path = require('path');

const SRC = 'C:/Users/sgg/AppData/Roaming/Tencent/Marvis/User/oAN1i2V14p5-lhhSY365mxizlI-c/workspace/conv_1a0000cc73d_3cc2a0c40aa4/temp/rev2';
const DST_ROOT = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/wiki';

const jobs = [
  ['ferroelectric-metal.md', 'concepts/ferroelectric-metal.md'],
  ['polar-metal.md', 'concepts/polar-metal.md'],
  ['metallic-ferroelectricity.md', 'concepts/metallic-ferroelectricity.md'],
  ['elemental-polar-metals.md', 'concepts/elemental-polar-metals.md'],
  ['magnetic-polar-metal.md', 'concepts/magnetic-polar-metal.md'],
  ['hyper-ferroelectric-metal.md', 'concepts/hyper-ferroelectric-metal.md'],
  ['hyperferroelectrics.md', 'concepts/hyperferroelectrics.md'],
  ['LiOsO3.md', 'entities/LiOsO3.md'],
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
