var pairs = [
  ['科研Wiki/temp/phaseH_batch5/dzyaloshinskii-moriya-interaction.md','科研Wiki/wiki/concepts/dzyaloshinskii-moriya-interaction.md'],
  ['科研Wiki/temp/phaseH_batch5/electron-correlation.md','科研Wiki/wiki/concepts/electron-correlation.md'],
  ['科研Wiki/temp/phaseH_batch5/electron-phonon-coupling.md','科研Wiki/wiki/concepts/electron-phonon-coupling.md'],
  ['科研Wiki/temp/phaseH_batch5/epitaxial-strain.md','科研Wiki/wiki/concepts/epitaxial-strain.md'],
  ['科研Wiki/temp/phaseH_batch5/equivalent-photon-approximation.md','科研Wiki/wiki/concepts/equivalent-photon-approximation.md'],
  ['科研Wiki/temp/phaseH_batch5/evanescent-field.md','科研Wiki/wiki/concepts/evanescent-field.md'],
  ['科研Wiki/temp/phaseH_batch6/exciton-condensation.md','科研Wiki/wiki/concepts/exciton-condensation.md'],
  ['科研Wiki/temp/phaseH_batch6/exclusive-production.md','科研Wiki/wiki/concepts/exclusive-production.md'],
  ['科研Wiki/temp/phaseH_batch6/fermi-surfaces.md','科研Wiki/wiki/concepts/fermi-surfaces.md'],
  ['科研Wiki/temp/phaseH_batch6/ferroelasticity.md','科研Wiki/wiki/concepts/ferroelasticity.md'],
  ['科研Wiki/temp/phaseH_batch6/ferroelectric-metal.md','科研Wiki/wiki/concepts/ferroelectric-metal.md'],
  ['科研Wiki/temp/phaseH_batch6/ferroelectric-tunnel-junction.md','科研Wiki/wiki/concepts/ferroelectric-tunnel-junction.md']
];
var tasks = pairs.map(function (pr) {
  return app.vault.adapter.read(pr[0]).then(function (ins) {
    return app.vault.adapter.read(pr[1]).then(function (cur) {
      var c = ins.replace(/^\s*\n/, '').replace(/\s*$/, '');
      var marker = '## 📚 相关论文';
      var idx = cur.indexOf(marker);
      var neu;
      if (idx >= 0) {
        neu = cur.slice(0, idx) + c + '\n\n' + cur.slice(idx);
      } else {
        neu = cur + '\n\n' + c;
      }
      return app.vault.adapter.write(pr[1], neu);
    });
  }).then(function () { return pr[1] + ' OK'; });
});
Promise.all(tasks).then(function (r) {
  console.log(r.join('\n'));
  console.log('TOTAL=' + r.length);
}).catch(function (e) { console.log('ERR ' + e); });
