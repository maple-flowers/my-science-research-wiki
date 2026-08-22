// 修正 tags 首元素：按目录统一为 concept/entity，去除多余重复项
var dirs = ['科研Wiki/wiki/concepts', '科研Wiki/wiki/entities'];
var tasks = [];
var report = [];
dirs.forEach(function (dir) {
  var singular = dir.indexOf('/concepts') !== -1 ? 'concept' : 'entity';
  app.vault.getFiles().forEach(function (f) {
    if (!f.path.startsWith(dir + '/')) return;
    if (!f.path.endsWith('.md')) return;
    tasks.push(app.vault.adapter.read(f.path).then(function (content) {
      var changed = false;
      var c = content;
      c = c.replace(/^(tags:\s*\[)([^\]]*)(\])/m, function (m, p1, p2, p3) {
        var items = p2.split(',').map(function (s) { return s.trim(); }).filter(function (s) { return s !== '' && s !== 'concept' && s !== 'entity'; });
        var res = singular;
        if (items.length > 0) { res += ', ' + items.join(', '); }
        if (p1 + res + p3 === m) { return m; }
        changed = true;
        return p1 + res + p3;
      });
      if (!changed) return;
      return app.vault.adapter.write(f.path, c).then(function () {
        report.push(f.path);
      });
    }));
  });
});
Promise.all(tasks).then(function () {
  console.log('TOTAL=' + report.length);
}).catch(function (e) {
  console.log('ERR: ' + e);
});
