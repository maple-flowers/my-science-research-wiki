// 补 NO_STATUS 页的 status 字段（按行数：<12 stub，否则 developing）
var targets = ['antiferromagnetism', 'd0-rule', 'exchange-interaction', 'slidetronics', 'spin-texture', 'vdW-heterostructure', 'weak-ferromagnetism'];
var dir = '科研Wiki/wiki/concepts';
var tasks = [];
var report = [];
targets.forEach(function (name) {
  var path = dir + '/' + name + '.md';
  tasks.push(app.vault.adapter.read(path).then(function (content) {
    if (!/^\uFEFF?---\s*\r?\n/.test(content)) { report.push(name + ': NO_FM skip'); return; }
    if (content.match(/^status:\s*/m)) { report.push(name + ': HAS_STATUS skip'); return; }
    var lines = content.split('\n').length;
    var status = lines < 12 ? 'stub' : 'developing';
    var updated = content.replace(/^---\r?\n/, '---\nstatus: ' + status + '\n');
    return app.vault.adapter.write(path, updated).then(function () {
      report.push(name + ': status=' + status + ' lines=' + lines);
    });
  }));
});
Promise.all(tasks).then(function () {
  console.log(report.join('\n'));
  console.log('TOTAL=' + report.length);
}).catch(function (e) {
  console.log('ERR: ' + e);
});
