// Phase J 收尾：3 个已具备机制小节+论文证据的概念页 status stub -> developing
var targets = ['conformal-invariance', 'scale-invariance', 'unparticles'];
var dir = '科研Wiki/wiki/concepts';
var tasks = [];
var report = [];
targets.forEach(function (name) {
  var path = dir + '/' + name + '.md';
  tasks.push(app.vault.adapter.read(path).then(function (content) {
    if (!/^status:\s*stub\s*\r?\n/.test(content)) { report.push(name + ': NOT_STUB skip'); return; }
    var updated = content.replace(/^status:\s*stub\s*\r?\n/m, 'status: developing\n');
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
