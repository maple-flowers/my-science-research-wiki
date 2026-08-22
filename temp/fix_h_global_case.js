// Phase H 前置：全库 wikilink 大小写规范化
var map = [
  { dir: 'entities', from: 'bifeo3', to: 'BiFeO3' },
  { dir: 'entities', from: 'in2se3', to: 'In2Se3' },
  { dir: 'entities', from: 'rui2', to: 'RuI2' },
  { dir: 'entities', from: 'rucl2', to: 'RuCl2' },
  { dir: 'entities', from: '2h-tas2', to: '2H-TaS2' },
  { dir: 'entities', from: 'tas2', to: 'TaS2' },
  { dir: 'concepts', from: '2D-materials', to: '2d-materials' }
];
var files = app.vault.getFiles().filter(function (f) { return f.path.endsWith('.md'); });
var tasks = [];
var report = [];
files.forEach(function (f) {
  tasks.push(app.vault.adapter.read(f.path).then(function (content) {
    var updated = content;
    var changed = false;
    map.forEach(function (m) {
      var from = '[[../' + m.dir + '/' + m.from;
      if (updated.indexOf(from) !== -1) {
        updated = updated.split(from).join('[[../' + m.dir + '/' + m.to);
        changed = true;
      }
    });
    if (changed) {
      return app.vault.adapter.write(f.path, updated).then(function () {
        report.push(f.path);
      });
    }
  }));
});
Promise.all(tasks).then(function () {
  console.log('FILES=' + report.length);
  console.log(report.join('\n'));
}).catch(function (e) {
  console.log('ERR: ' + e);
});
