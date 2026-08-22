var jobs = [
  { t: '科研Wiki/wiki/concepts/additive-manufacturing.md', a: '## 📚 相关论文', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/two-photon-polymerization|双光子聚合]]：增材制造中基于双光子吸收的亚微米三维光刻工艺，属 AM 的光固化（TPP）分支。' },
  { t: '科研Wiki/wiki/concepts/bamboo-like-N-CNTs.md', a: '## 📚 相关论文', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../entities/bamboo-like-N-CNTs|bamboo-like-N-CNTs（实体页）]]：本概念名的规范页，含竹节状氮掺杂碳纳米管的完整材料信息。\n- [[../entities/carbon-nanotube|碳纳米管]]：竹节状形貌所属的基础材料家族。' },
  { t: '科研Wiki/wiki/concepts/glassy-carbon.md', a: '## 📚 相关论文', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../entities/glassy-carbon|glassy-carbon（实体页）]]：本概念名的规范页，含玻碳的完整材料信息。\n- [[../concepts/conjugated-polymer|共轭聚合物]]：在玻碳电极上电合成的目标材料体系。' },
  { t: '科研Wiki/wiki/concepts/steepest-ascent-path.md', a: '## 📚 相关论文', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/steepest-ascent|最陡上升法]]：本页的规范名，Bader 分析中沿电荷密度梯度上升的数值方法。\n- [[../concepts/bader-analysis|Bader 电荷分析]]：使用最陡上升路径划分原子电荷区域的框架。' },
  { t: '科研Wiki/wiki/concepts/surface-terminations.md', a: '## 📚 相关论文', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/surface-termination|表面端接]]：本页的规范名（单数形式）。\n- [[../entities/MXenes|MXenes]]：表面端接（-O/-OH/-F）调控是 MXene 家族性能调制的核心手段。' },
  { t: '科研Wiki/wiki/concepts/two-photon-cross-section.md', a: '## 📚 相关论文', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/two-photon-absorption-cross-section|双光子吸收截面]]：本页的规范名（全称），度量双光子吸收效率的定量指标。\n- [[../concepts/two-photon-polymerization|双光子聚合]]：依赖大双光子截面的引发剂驱动 3D 光刻工艺。' },
  { t: '科研Wiki/wiki/concepts/type-i-multiferroics.md', a: '## 📚 相关论文', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/type-i-multiferroic|I 型多铁]]：本页的规范名（单数形式）。\n- [[../concepts/magnetoelectric-coupling|磁电耦合]]：I 型多铁中磁性-铁电协同耦合的下游物性。' },
  { t: '科研Wiki/wiki/concepts/van-der-waals-heterostructure.md', a: '## 📚 相关论文', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/vdW-heterostructure|范德华异质结]]：本页的规范名（简称）。\n- [[../concepts/2d-materials|二维材料]]：构成 vdW 异质结的基础层状材料。' },
  { t: '科研Wiki/wiki/concepts/variable-spring-constants.md', a: '## 📚 相关论文', b: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/variable-spring-constant|可变弹性常数]]：本页的规范名（单数形式）。\n- [[../concepts/minimum-energy-path|最小能量路径]]：可变弹簧常数所服务的 NEB 搜索目标。\n- [[../concepts/nudged-elastic-band|NEB 方法]]：使用可变弹簧常数稳定路径搜索的弹性带算法。' }
];
var tasks = jobs.map(function (j) {
  return app.vault.adapter.read(j.t).then(function (cur) {
    var idx = cur.indexOf(j.a);
    if (idx < 0) return j.t + ' SKIP';
    return app.vault.adapter.write(j.t, cur.slice(0, idx) + j.b + '\n\n' + cur.slice(idx)).then(function () { return j.t + ' OK'; });
  });
});
Promise.all(tasks).then(function (r) { console.log(r.join('\n')); console.log('TOTAL=' + r.length); }).catch(function (e) { console.log('ERR ' + e); });
