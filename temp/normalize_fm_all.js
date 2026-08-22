// 全库 frontmatter 归一化：type 单数化 + tags 首元素插入 concept/entity
var dirs = ['科研Wiki/wiki/concepts', '科研Wiki/wiki/entities'];
var tasks = [];
var report = [];
dirs.forEach(function (dir) {
  var singular = dir.indexOf('/concepts/') !== -1 ? 'concept' : 'entity';
  app.vault.getFiles().forEach(function (f) {
    if (!f.path.startsWith(dir + '/')) return;
    if (!f.path.endsWith('.md')) return;
    tasks.push(app.vault.adapter.read(f.path).then(function (content) {
      var changed = false;
      var c = content;
      if (/^type:\s*concepts$/m.test(c)) { c = c.replace(/^type:\s*concepts$/m, 'type: concept'); changed = true; }
      if (/^type:\s*entities$/m.test(c)) { c = c.replace(/^type:\s*entities$/m, 'type: entity'); changed = true; }
      c = c.replace(/^(tags:\s*\[)([^\]]*)(\])/m, function (m, p1, p2, p3) {
        var first = p2.trim().split(',')[0].trim();
        if (first === singular) return m;
        changed = true;
        if (p2.trim() === '') return p1 + singular + p3;
        return p1 + singular + ', ' + p2 + p3;
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
