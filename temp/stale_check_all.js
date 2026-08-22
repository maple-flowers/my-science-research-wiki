const fs = require('fs');
const files = app.vault.getMarkdownFiles();
const missing = {};
let total = 0;
for (const f of files) {
  const cache = app.metadataCache.getFileCache(f);
  if (!cache || !cache.links) continue;
  for (const l of cache.links) {
    const resolved = app.metadataCache.getFirstLinkpathDest(l.link, f.path);
    if (!resolved) {
      total++;
      const key = l.link;
      if (!missing[key]) missing[key] = [];
      if (missing[key].length < 5) missing[key].push(f.path);
    }
  }
}
const out = 'MISSING_TOTAL=' + total + '\n' + JSON.stringify(missing, null, 1);
const dest = 'C:/Users/sgg/AppData/Roaming/Tencent/Marvis/User/oAN1i2V14p5-lhhSY365mxizlI-c/workspace/conv_1a0000cc73d_3cc2a0c40aa4/temp/stale_check_result.txt';
fs.writeFileSync(dest, out, 'utf8');
console.log('done total=' + total);
