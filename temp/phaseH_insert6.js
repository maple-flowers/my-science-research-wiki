// Phase H batch1 插入：从 vault/temp/phaseH_batch1 读正文，插入到 wiki 目标页相关论文章节前
var pairs = [
  ['科研Wiki/temp/phaseH_batch1/ferroelectricity.md', '科研Wiki/wiki/concepts/ferroelectricity.md'],
  ['科研Wiki/temp/phaseH_batch1/berry-phase.md', '科研Wiki/wiki/concepts/berry-phase.md'],
  ['科研Wiki/temp/phaseH_batch1/density-of-states.md', '科研Wiki/wiki/concepts/density-of-states.md'],
  ['科研Wiki/temp/phaseH_batch1/tight-binding.md', '科研Wiki/wiki/concepts/tight-binding.md'],
  ['科研Wiki/temp/phaseH_batch1/graphene.md', '科研Wiki/wiki/entities/graphene.md'],
  ['科研Wiki/temp/phaseH_batch1/BaTiO3.md', '科研Wiki/wiki/entities/BaTiO3.md']
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
