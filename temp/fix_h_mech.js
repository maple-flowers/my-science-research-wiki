// Phase H 机械缺口修复：type 单数化 / 补 title / 去 BOM
var files = [
  '科研Wiki/wiki/concepts/antiferromagnetism.md',
  '科研Wiki/wiki/concepts/d0-rule.md',
  '科研Wiki/wiki/concepts/exchange-interaction.md',
  '科研Wiki/wiki/concepts/vdW-heterostructure.md',
  '科研Wiki/wiki/concepts/weak-ferromagnetism.md',
  '科研Wiki/wiki/concepts/slidetronics.md',
  '科研Wiki/wiki/concepts/spin-texture.md',
  '科研Wiki/wiki/concepts/undercooling.md',
  '科研Wiki/wiki/concepts/vdw-correction.md',
  '科研Wiki/wiki/concepts/wannier-function.md'
];
var report = [];
var tasks = files.map(function (path) {
  return app.vault.adapter.read(path).then(function (content) {
    var log = path + ': ';
    var parts = [];
    var changed = false;
    if (content.charCodeAt(0) === 0xFEFF) { content = content.slice(1); parts.push('BOM-removed'); changed = true; }
    var m = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
    if (!m) { parts.push('NO-FM'); changed = true; }
    else {
      var fm = m[1];
      var fm2 = fm.replace(/(^|\n)type:\s*concepts\s*(\r?)$/mg, '$1type: concept$2');
      if (fm2 !== fm) { parts.push('type-fixed'); changed = true; }
      fm = fm2;
      if (!/(^|\n)title:/.test(fm)) {
        var h1 = content.match(/^#\s+(.+)$/m);
        var t = h1 ? h1[1].trim() : path.replace(/^.*\//, '').replace(/\.md$/, '');
        fm = fm + '\ntitle: \'' + t.replace(/'/g, "''") + '\'';
        parts.push('title-added'); changed = true;
      }
      if (changed) {
        content = content.slice(0, m.index) + '---\n' + fm + '\n---' + content.slice(m.index + m[0].length);
      }
    }
    if (changed) {
      return app.vault.adapter.write(path, content).then(function () {
        report.push(log + parts.join(','));
      });
    } else {
      report.push(log + 'no-change');
    }
  });
});
Promise.all(tasks).then(function () {
  console.log(report.join('\n'));
  console.log('DONE=' + report.length);
}).catch(function (e) { console.log('ERR: ' + e); });
