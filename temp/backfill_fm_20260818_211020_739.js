// 批量补 frontmatter v2：全单引号，适配 code= 参数传递
var dirs = ['科研Wiki/wiki/concepts', '科研Wiki/wiki/entities'];
var today = '2026-08-18';
var tasks = [];
var report = [];
function esc(y) { return y.replace(/'/g, "''"); }
dirs.forEach(function (dir) {
  app.vault.getFiles().forEach(function (f) {
    if (!f.path.startsWith(dir + '/')) return;
    if (!f.path.endsWith('.md')) return;
    tasks.push(app.vault.adapter.read(f.path).then(function (content) {
      if (/^\uFEFF?---\s*\r?\n/.test(content)) return;
      var m1 = content.match(/^#\s+(.+)$/m);
      var title = m1 ? m1[1].trim() : f.basename;
      var papers = [];
      var re = /\[\[\.\.\/papers\/([^\]\|#]+)/g;
      var mm;
      while ((mm = re.exec(content)) !== null) {
        var p = mm[1].trim();
        if (papers.indexOf(p) === -1) papers.push(p);
      }
      var type = f.path.indexOf('/concepts/') !== -1 ? 'concepts' : 'entities';
      var lines = content.split('\n').length;
      var status = lines < 12 ? 'stub' : 'developing';
      var papersStr = papers.map(function (x) { return '\'' + x + '\''; }).join(', ');
      var fm = '---\ntags: []\ntitle: \'' + esc(title) + '\'\ntype: ' + type + '\nstatus: ' + status + '\npapers: [' + papersStr + ']\nupdated: ' + today + '\n---\n\n';
      return app.vault.adapter.write(f.path, fm + content).then(function () {
        report.push(f.path + ' | ' + status + ' | papers=' + papers.length);
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
