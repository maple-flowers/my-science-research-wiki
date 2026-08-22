// Phase H batch2 插入：从 vault/temp/phaseH_batch2 读正文，插入到 wiki 目标页相关论文章节前
var pairs = [
  ['科研Wiki/temp/phaseH_batch2/2d-materials.md', '科研Wiki/wiki/concepts/2d-materials.md'],
  ['科研Wiki/temp/phaseH_batch2/Car-Parrinello.md', '科研Wiki/wiki/concepts/Car-Parrinello.md'],
  ['科研Wiki/temp/phaseH_batch2/LAPW.md', '科研Wiki/wiki/concepts/LAPW.md'],
  ['科研Wiki/temp/phaseH_batch2/PBE-functional.md', '科研Wiki/wiki/concepts/PBE-functional.md'],
  ['科研Wiki/temp/phaseH_batch2/aimd.md', '科研Wiki/wiki/concepts/aimd.md'],
  ['科研Wiki/temp/phaseH_batch2/bessel-beam.md', '科研Wiki/wiki/concepts/bessel-beam.md']
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
