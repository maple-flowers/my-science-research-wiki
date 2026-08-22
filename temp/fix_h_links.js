// Phase H 断链修复：wikilink 大小写 + 3 张图片路径修正
var edits = [
  // bifeo3 -> BiFeO3（4 页）
  { f: '科研Wiki/wiki/concepts/antiferromagnetism.md', from: '[[../entities/bifeo3', to: '[[../entities/BiFeO3' },
  { f: '科研Wiki/wiki/concepts/d0-rule.md', from: '[[../entities/bifeo3', to: '[[../entities/BiFeO3' },
  { f: '科研Wiki/wiki/concepts/exchange-interaction.md', from: '[[../entities/bifeo3', to: '[[../entities/BiFeO3' },
  { f: '科研Wiki/wiki/concepts/weak-ferromagnetism.md', from: '[[../entities/bifeo3', to: '[[../entities/BiFeO3' },
  // vdW-heterostructure 五处大小写
  { f: '科研Wiki/wiki/concepts/vdW-heterostructure.md', from: '[[../entities/in2se3', to: '[[../entities/In2Se3' },
  { f: '科研Wiki/wiki/concepts/vdW-heterostructure.md', from: '[[../entities/rui2', to: '[[../entities/RuI2' },
  { f: '科研Wiki/wiki/concepts/vdW-heterostructure.md', from: '[[../entities/rucl2', to: '[[../entities/RuCl2' },
  { f: '科研Wiki/wiki/concepts/vdW-heterostructure.md', from: '[[../entities/2h-tas2', to: '[[../entities/2H-TaS2' },
  { f: '科研Wiki/wiki/concepts/vdW-heterostructure.md', from: '[[../entities/tas2', to: '[[../entities/TaS2' },
  // MoSe2 -> 2d-materials 大小写
  { f: '科研Wiki/wiki/entities/MoSe2.md', from: '[[../concepts/2D-materials', to: '[[../concepts/2d-materials' },
  // 图片路径修正（随机串错配）
  { f: '科研Wiki/wiki/concepts/skyrmion.md', from: 'gongAbsenceCriticalThickness2023/fig_1_Q8LV7XLD.png', to: 'gongAbsenceCriticalThickness2023/fig_1_SYSSN7EC.png' },
  { f: '科研Wiki/wiki/concepts/spin-spiral.md', from: 'cheongMultiferroicsMagneticTwist2007a/fig_1_G5K2M3NX.png', to: 'cheongMultiferroicsMagneticTwist2007a/fig_1_D8A9TF3K.png' },
  { f: '科研Wiki/wiki/entities/WS2.md', from: 'RecentAdvancesGrowth2025/fig_1_NDNYXQ2A.png', to: 'RecentAdvancesGrowth2025/fig_1_7IQ7CDIJ.png' }
];
var tasks = [];
var report = [];
edits.forEach(function (e) {
  tasks.push(app.vault.adapter.read(e.f).then(function (content) {
    if (content.indexOf(e.from) === -1) {
      report.push('SKIP(not-found): ' + e.f + ' :: ' + e.from);
      return;
    }
    var cnt = content.split(e.from).length - 1;
    var updated = content.split(e.from).join(e.to);
    return app.vault.adapter.write(e.f, updated).then(function () {
      report.push('OK x' + cnt + ': ' + e.f + ' :: ' + e.from + ' -> ' + e.to);
    });
  }));
});
Promise.all(tasks).then(function () {
  console.log(report.join('\n'));
}).catch(function (err) {
  console.log('ERR: ' + err);
});
