const fs = require('fs');
const jsonPath = 'C:/Users/sgg/AppData/Roaming/Tencent/Marvis/User/oAN1i2V14p5-lhhSY365mxizlI-c/workspace/conv_1a0000cc73d_3cc2a0c40aa4/temp/rev19/rev19_pages.json';
const pages = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
let n = 0;
for (const [slug, content] of Object.entries(pages)) {
  const p = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/wiki/concepts/' + slug + '.md';
  fs.writeFileSync(p, content, 'utf8');
  n++;
}
console.log('written', n);
