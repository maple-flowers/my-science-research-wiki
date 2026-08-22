// Phase H 补充：为 12 个缺 frontmatter 的 concepts 页补 frontmatter
var slugs = ['dzyaloshinskii-moriya-interaction','electron-correlation','electron-phonon-coupling','epitaxial-strain','equivalent-photon-approximation','evanescent-field','exciton-condensation','exclusive-production','fermi-surfaces','ferroelasticity','ferroelectric-metal','ferroelectric-tunnel-junction'];
app.vault.adapter.read('科研Wiki/temp/phaseH_fm12.json').then(function (js) {
  var map = JSON.parse(js);
  var tasks = slugs.map(function (slug) {
    var target = '科研Wiki/wiki/concepts/' + slug + '.md';
    return app.vault.adapter.read(target).then(function (cur) {
      if (cur.indexOf('---\n') === 0) {
        return target + ' SKIP(has-fm)';
      }
      var neu = map[slug] + '\n\n' + cur;
      return app.vault.adapter.write(target, neu).then(function () {
        return target + ' OK';
      });
    });
  });
  return Promise.all(tasks);
}).then(function (r) {
  console.log(r.join('\n'));
  console.log('TOTAL=' + r.length);
}).catch(function (e) { console.log('ERR ' + e); });
