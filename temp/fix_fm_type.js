// 修正 203 页：tags: [] + 复数 type → 单数 type + tags 首元素一致
var dirs = ['科研Wiki/wiki/concepts', '科研Wiki/wiki/entities'];
var tasks = [];
var report = [];
dirs.forEach(function (dir) {
  app.vault.getFiles().forEach(function (f) {
    if (!f.path.startsWith(dir + '/')) return;
    if (!f.path.endsWith('.md')) return;
    tasks.push(app.vault.adapter.read(f.path).then(function (content) {
      var head = content.split('\n', 12).join('\n');
      if (head.indexOf('tags: []') === -1) return; // 仅处理本轮补 fm 的页
      var type = f.path.indexOf('/concepts/') !== -1 ? 'concept' : 'entity';
      var newHead = content
        .replace('tags: []', 'tags: [' + type + ']')
        .replace('type: concepts', 'type: concept')
        .replace('type: entities', 'type: entity');
      if (newHead === content) return;
      return app.vault.adapter.write(f.path, newHead).then(function () {
        report.push(f.path + ' -> ' + type);
      });
    }));
  });
});
Promise.all(tasks).then(function () {
  console.log(report.join('\n'));
  console.log('TOTAL=' + report.length);
}).catch(function (e) {
  console.log('ERR: ' + e);
});
