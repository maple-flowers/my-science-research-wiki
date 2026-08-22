const fs = require('fs');
const path = require('path');

const revDir = 'C:/Users/sgg/AppData/Roaming/Tencent/Marvis/User/oAN1i2V14p5-lhhSY365mxizlI-c/workspace/conv_1a0000cc73d_3cc2a0c40aa4/temp/rev4';
const wikiDir = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/wiki/concepts';

const files = [
  'canted-antiferromagnetism.md',
  'landau-lifshitz-equation.md',
  'magnetostatic-effect.md',
  'neel-vector.md',
  'spin-wave-logic.md',
];

for (const f of files) {
  const src = path.join(revDir, f);
  const dst = path.join(wikiDir, f);
  const content = fs.readFileSync(src, 'utf8');
  fs.writeFileSync(dst, content, 'utf8');
  console.log('WROTE', dst, content.length, 'bytes');
}
