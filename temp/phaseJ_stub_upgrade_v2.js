// Phase J 收尾 v2：status stub -> developing（宽松替换）
var targets = ['conformal-invariance', 'scale-invariance', 'unparticles'];
var dir = '科研Wiki/wiki/concepts';
var tasks = [];
var report = [];
targets.forEach(function (name) {
  var path = dir + '/' + name + '.md';
  tasks.push(app.vault.adapter.read(path).then(function (content) {
    if (content.indexOf('status: stub') === -1) {
      report.push(name + ': NOT_FOUND status:stub | head=' + JSON.stringify(content.slice(0, 60)));
      return;
    }
    var updated = content.replace(/status:\s*stub(?=\r?\n)/, 'status: developing');
    if (updated === content) { report.push(name + ': NO_CHANGE'); return; }
    return app.vault.adapter.write(path, updated).then(function () {
      report.push(name + ': stub->developing OK');
    });
  }));
});
Promise.all(tasks).then(function () {
  console.log(report.join('\n'));
  console.log('TOTAL=' + report.length);
}).catch(function (e) {
  console.log('ERR: ' + e);
});
