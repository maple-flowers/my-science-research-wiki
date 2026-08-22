// 修复 9 个异常页：AIGC 页补标准字段 / pump-probe 两页 type 修正 / slidetronics 两页补 tags
var root = '科研Wiki/wiki';
var report = [];
function getPapers(content) {
  var papers = [];
  var re = /\[\[\.\.\/papers\/([^\]\|#]+)/g;
  var mm;
  while ((mm = re.exec(content)) !== null) {
    var p = mm[1].trim();
    if (papers.indexOf(p) === -1) papers.push(p);
  }
  return papers.map(function (x) { return '\'' + x + '\''; }).join(', ');
}
function getTitle(content, fallback) {
  var m = content.match(/^#\s+(.+)$/m);
  return m ? m[1].trim() : fallback;
}
// 1) AIGC 水印页：补 tags/title/type/papers/updated（保留 AIGC 块）
var aigcFiles = ['antiferromagnetism', 'd0-rule', 'exchange-interaction', 'vdW-heterostructure', 'weak-ferromagnetism'];
aigcFiles.forEach(function (name) {
  var p = root + '/concepts/' + name + '.md';
  app.vault.adapter.read(p).then(function (c) {
    if (!/^---\nstatus: developing\nAIGC:/.test(c)) { report.push('AIGC_SKIP ' + p); return; }
    var title = getTitle(c, name);
    var papers = getPapers(c);
    var fm = '---\ntags: [concept]\ntitle: \'' + title.replace(/'/g, "''") + '\'\ntype: concepts\nstatus: developing\npapers: [' + papers + ']\nupdated: 2026-08-18\nAIGC:';
    return app.vault.adapter.write(p, c.replace(/^---\nstatus: developing\nAIGC:/, fm)).then(function () {
      report.push('AIGC_FIX ' + p);
    });
  });
});
// 2) entities 目录误标 type=concept → entity
['pump-probe', 'ultrafast-spectroscopy'].forEach(function (name) {
  var p = root + '/entities/' + name + '.md';
  app.vault.adapter.read(p).then(function (c) {
    if (!/^(?m)^type: concept$/m.test(c)) { report.push('TYPE_SKIP ' + p); return; }
    return app.vault.adapter.write(p, c.replace(/(?m)^type: concept$/, 'type: entity')).then(function () {
      report.push('TYPE_FIX ' + p);
    });
  });
});
// 3) slidetronics / spin-texture 缺 tags 字段
['slidetronics', 'spin-texture'].forEach(function (name) {
  var p = root + '/concepts/' + name + '.md';
  app.vault.adapter.read(p).then(function (c) {
    if (!/^---\nstatus: developing\n/.test(c)) { report.push('TAGS_SKIP ' + p); return; }
    return app.vault.adapter.write(p, c.replace(/^---\n(status: developing\n)/, '---\ntags: [concept]\n$1')).then(function () {
      report.push('TAGS_FIX ' + p);
    });
  });
});
setTimeout(function () {
  console.log(report.join('\n'));
  console.log('DONE ' + report.length);
}, 3000);
