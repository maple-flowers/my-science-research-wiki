// Phase H 缺图清理：删断图块 + 修 tab hash 笔误
var targets = [
  '科研Wiki/wiki/concepts/charge-sloshing.md',
  '科研Wiki/wiki/concepts/methfessel-paxton-smearing.md',
  '科研Wiki/wiki/concepts/monkhorst-pack-grid.md',
  '科研Wiki/wiki/concepts/plane-wave-basis.md',
  '科研Wiki/wiki/concepts/self-consistent-field-cycle.md',
  '科研Wiki/wiki/concepts/magnon-hall-effect.md',
  '科研Wiki/wiki/concepts/neel-temperature.md',
  '科研Wiki/wiki/concepts/topological-magnon.md',
  '科研Wiki/wiki/entities/FePS3.md',
  '科研Wiki/wiki/entities/MnPSe3.md',
  '科研Wiki/wiki/entities/NiPS3.md',
  '科研Wiki/wiki/entities/NbSe2.md',
  '科研Wiki/wiki/entities/TaS2.md',
  '科研Wiki/wiki/figures/electronic-bands-cdw-transport.md',
  '科研Wiki/wiki/figures/vibrational-spectra.md',
  '科研Wiki/wiki/papers/huProgressProspectsLowdimensional2019.md',
  '科研Wiki/wiki/papers/chowdhuryReviewTheoreticalComputational.md'
];
var badFigRe = /!\[[^\]]*\]\(\.\.\/\.\.\/raw\/figures\/(?:kresseEfficiencyAbinitioTotal1996a\/[^\)]*|tanRevealingEmergentMagnetic2024\/fig_1_A3L3NFIH[^\)]*|Inosov2008fermi\/fig_2_UK4SYAPY[^\)]*|nakataRobustChargedensityWave2021\/fig_1_6T5AGUJF[^\)]*)\)\r?\n(?:\*\s*[^\n]*\r?\n)*/g;
var rep1 = { from: 'tab_2_GG7NXE5PZ.png', to: 'tab_2_GG7NXE5P.png' };
var rep2 = { from: 'tab_2_2GIU5ZQ2A.png', to: 'tab_2_2GIU5ZQ2.png' };
var tasks = [];
var report = [];
targets.forEach(function (p) {
  tasks.push(app.vault.adapter.read(p).then(function (content) {
    var orig = content;
    var removed = 0;
    content = content.replace(badFigRe, function (blk) { removed++; return ''; });
    var hasRep1 = content.indexOf(rep1.from) !== -1;
    var hasRep2 = content.indexOf(rep2.from) !== -1;
    content = content.split(rep1.from).join(rep1.to);
    content = content.split(rep2.from).join(rep2.to);
    if (content !== orig) {
      return app.vault.adapter.write(p, content).then(function () {
        report.push(p.replace('科研Wiki/wiki/', '') + ' | delImgBlock=' + removed + ' | rep_tab_GG7NXE5P=' + hasRep1 + ' | rep_tab_2GIU5ZQ2=' + hasRep2);
      });
    }
    report.push(p.replace('科研Wiki/wiki/', '') + ' | NO CHANGE');
  }));
});
Promise.all(tasks).then(function () {
  console.log(report.join('\n'));
  console.log('TOTAL=' + report.length);
}).catch(function (e) { console.log('ERR: ' + e); });
