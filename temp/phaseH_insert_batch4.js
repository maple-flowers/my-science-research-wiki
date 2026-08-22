// Phase H batch4 插入：从 vault/temp/phaseH_batch4 读正文，插入到 wiki 目标页相关论文章节前
var pairs = [
  ['科研Wiki/temp/phaseH_batch4/critical-thickness-ferroelectric.md', '科研Wiki/wiki/concepts/critical-thickness-ferroelectric.md'],
  ['科研Wiki/temp/phaseH_batch4/curie-temperature.md', '科研Wiki/wiki/concepts/curie-temperature.md'],
  ['科研Wiki/temp/phaseH_batch4/d-pi-a-architecture.md', '科研Wiki/wiki/concepts/d-pi-a-architecture.md'],
  ['科研Wiki/temp/phaseH_batch4/depolarization-field.md', '科研Wiki/wiki/concepts/depolarization-field.md'],
  ['科研Wiki/temp/phaseH_batch4/domain-wall-motion.md', '科研Wiki/wiki/concepts/domain-wall-motion.md'],
  ['科研Wiki/temp/phaseH_batch4/domain-wall.md', '科研Wiki/wiki/concepts/domain-wall.md']
];
var tasks = pairs.map(function (pr) {
  return app.vault.adapter.read(pr[0]).then(function (ins) {
    return app.vault.adapter.read(pr[1]).then(function (cur) {
      var c = ins.replace(/^\s*\n/, '').replace(/\s*$/, '');
      var marker = '## 📚 相关论文';
      var idx = cur.indexOf(marker);
      var neu;
      if (idx >= 0) {
        neu = cur.slice(0, idx) + c + '\n\n' + cur.slice(idx);
      } else {
        neu = cur + '\n\n' + c;
      }
      return app.vault.adapter.write(pr[1], neu);
    });
  }).then(function () { return pr[1] + ' OK'; });
});
Promise.all(tasks).then(function (r) {
  console.log(r.join('\n'));
  console.log('TOTAL=' + r.length);
}).catch(function (e) { console.log('ERR ' + e); });
