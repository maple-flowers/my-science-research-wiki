const fs = require('fs');
const path = require('path');
const b64 = 'B64_DATA';
const pages = JSON.parse(Buffer.from(b64, 'base64').toString('utf-8'));
const base = 'E:\\swan_goose\\宝宝\\笔记库\\sgg\\科研Wiki\\wiki\\concepts';
for (const [slug, content] of Object.entries(pages)) {
  const p = path.join(base, slug + '.md');
  fs.writeFileSync(p, content, 'utf-8');
  console.log('written', slug, content.length);
}
