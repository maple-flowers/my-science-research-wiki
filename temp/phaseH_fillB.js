var jobs = [
  { t: '科研Wiki/wiki/entities/AFM.md', mode: 'append', a: '', b: '\n## 📚 相关论文 (Related Papers)\n\n- [[../papers/Kumar2017microstructuring|Kumar et al.]] — 为本库 AFM（原子力显微镜）作为材料表征/微结构加工工具提供了使用示例证据。\n\n## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../entities/c-AFM|导电原子力显微镜 (c-AFM)]]：AFM 的导电模式衍生变体，同时表征形貌与局域电学性质。\n- [[../concepts/antiferromagnetism|反铁磁性]]：AFM 的另一常见含义，指磁矩反平行排列的有序磁态。' },
  { t: '科研Wiki/wiki/entities/BTO.md', mode: 'before', a: '## 🔗 规范页', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../entities/BaTiO3|BaTiO₃]]：BTO 缩写对应的规范实体页，含钛酸钡完整材料信息。' },
  { t: '科研Wiki/wiki/concepts/faraday-effect.md', mode: 'replace', a: '## 🔗 关联概念与 entities', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)' },
  { t: '科研Wiki/wiki/concepts/kerr-effect.md', mode: 'replace', a: '## 🔗 关联概念与 entities', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)' }
];
var tasks = jobs.map(function (j) {
  return app.vault.adapter.read(j.t).then(function (cur) {
    var neu;
    if (j.mode === 'before') {
      var idx = cur.indexOf(j.a);
      if (idx < 0) return j.t + ' SKIP';
      neu = cur.slice(0, idx) + j.b + '\n\n' + cur.slice(idx);
    } else if (j.mode === 'append') {
      neu = cur + j.b;
    } else {
      var i2 = cur.indexOf(j.a);
      if (i2 < 0) return j.t + ' SKIP';
      neu = cur.slice(0, i2) + j.b + cur.slice(i2 + j.a.length);
    }
    return app.vault.adapter.write(j.t, neu).then(function () { return j.t + ' OK'; });
  });
});
Promise.all(tasks).then(function (r) { console.log(r.join('\n')); console.log('TOTAL=' + r.length); }).catch(function (e) { console.log('ERR ' + e); });
