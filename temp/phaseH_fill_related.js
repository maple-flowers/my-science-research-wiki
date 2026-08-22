// Phase H 收尾：为 9 个 concepts 补「关联概念与实体」节、AFM 补相关论文+关联节、BTO 补关联节、faraday/kerr 归一化标题
var jobs = [
  // concepts 缺关联节：插入到「## 📚 相关论文」之前
  { target: '科研Wiki/wiki/concepts/additive-manufacturing.md', mode: 'before', anchor: '## 📚 相关论文', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/two-photon-polymerization|双光子聚合]]：增材制造中基于双光子吸收的亚微米三维光刻工艺，属 AM 的光固化（TPP）分支。' },
  { target: '科研Wiki/wiki/concepts/bamboo-like-N-CNTs.md', mode: 'before', anchor: '## 📚 相关论文', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../entities/bamboo-like-N-CNTs|bamboo-like-N-CNTs（实体页）]]：本概念名的规范页，含竹节状氮掺杂碳纳米管的完整材料信息。\n- [[../entities/carbon-nanotube|碳纳米管]]：竹节状形貌所属的基础材料家族。' },
  { target: '科研Wiki/wiki/concepts/glassy-carbon.md', mode: 'before', anchor: '## 📚 相关论文', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../entities/glassy-carbon|glassy-carbon（实体页）]]：本概念名的规范页，含玻碳的完整材料信息。\n- [[../concepts/conjugated-polymer|共轭聚合物]]：在玻碳电极上电合成的目标材料体系。' },
  { target: '科研Wiki/wiki/concepts/steepest-ascent-path.md', mode: 'before', anchor: '## 📚 相关论文', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/steepest-ascent|最陡上升法]]：本页的规范名，Bader 分析中沿电荷密度梯度上升的数值方法。\n- [[../concepts/bader-analysis|Bader 电荷分析]]：使用最陡上升路径划分原子电荷区域的框架。' },
  { target: '科研Wiki/wiki/concepts/surface-terminations.md', mode: 'before', anchor: '## 📚 相关论文', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/surface-termination|表面端接]]：本页的规范名（单数形式）。\n- [[../entities/MXenes|MXenes]]：表面端接（-O/-OH/-F）调控是 MXene 家族性能调制的核心手段。' },
  { target: '科研Wiki/wiki/concepts/two-photon-cross-section.md', mode: 'before', anchor: '## 📚 相关论文', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/two-photon-absorption-cross-section|双光子吸收截面]]：本页的规范名（全称），度量双光子吸收效率的定量指标。\n- [[../concepts/two-photon-polymerization|双光子聚合]]：依赖大双光子截面的引发剂驱动 3D 光刻工艺。' },
  { target: '科研Wiki/wiki/concepts/type-i-multiferroics.md', mode: 'before', anchor: '## 📚 相关论文', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/type-i-multiferroic|I 型多铁]]：本页的规范名（单数形式）。\n- [[../concepts/magnetoelectric-coupling|磁电耦合]]：I 型多铁中磁性-铁电协同耦合的下游物性。' },
  { target: '科研Wiki/wiki/concepts/van-der-waals-heterostructure.md', mode: 'before', anchor: '## 📚 相关论文', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/vdW-heterostructure|范德华异质结]]：本页的规范名（简称）。\n- [[../concepts/2d-materials|二维材料]]：构成 vdW 异质结的基础层状材料。' },
  { target: '科研Wiki/wiki/concepts/variable-spring-constants.md', mode: 'before', anchor: '## 📚 相关论文', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../concepts/variable-spring-constant|可变弹性常数]]：本页的规范名（单数形式）。\n- [[../concepts/minimum-energy-path|最小能量路径]]：可变弹簧常数所服务的 NEB 搜索目标。\n- [[../concepts/nudged-elastic-band|NEB 方法]]：使用可变弹簧常数稳定路径搜索的弹性带算法。' },
  // entities/AFM：追加相关论文节 + 关联节
  { target: '科研Wiki/wiki/entities/AFM.md', mode: 'append', anchor: '', block: '\n## 📚 相关论文 (Related Papers)\n\n- [[../papers/Kumar2017microstructuring|Kumar et al.]] — 为本库 AFM（原子力显微镜）作为材料表征/微结构加工工具提供了使用示例证据。\n\n## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../entities/c-AFM|导电原子力显微镜 (c-AFM)]]：AFM 的导电模式衍生变体，同时表征形貌与局域电学性质。\n- [[../concepts/antiferromagnetism|反铁磁性]]：AFM 的另一常见含义，指磁矩反平行排列的有序磁态。' },
  // entities/BTO：插入关联节到「## 🔗 规范页」之前
  { target: '科研Wiki/wiki/entities/BTO.md', mode: 'before', anchor: '## 🔗 规范页', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)\n\n- [[../entities/BaTiO3|BaTiO₃]]：BTO 缩写对应的规范实体页，含钛酸钡完整材料信息。' },
  // faraday-effect / kerr-effect：归一化关联节标题
  { target: '科研Wiki/wiki/concepts/faraday-effect.md', mode: 'replace', anchor: '## 🔗 关联概念与 entities', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)' },
  { target: '科研Wiki/wiki/concepts/kerr-effect.md', mode: 'replace', anchor: '## 🔗 关联概念与 entities', block: '## 🔗 关联概念与实体 (Related Concepts & Entities)' }
];

var tasks = jobs.map(function (j) {
  return app.vault.adapter.read(j.target).then(function (cur) {
    var neu;
    if (j.mode === 'before') {
      var idx = cur.indexOf(j.anchor);
      if (idx < 0) return j.target + ' SKIP(anchor-not-found)';
      neu = cur.slice(0, idx) + j.block + '\n\n' + cur.slice(idx);
    } else if (j.mode === 'append') {
      neu = cur + j.block;
    } else if (j.mode === 'replace') {
      var i2 = cur.indexOf(j.anchor);
      if (i2 < 0) return j.target + ' SKIP(anchor-not-found)';
      neu = cur.slice(0, i2) + j.block + cur.slice(i2 + j.anchor.length);
    }
    return app.vault.adapter.write(j.target, neu).then(function () {
      return j.target + ' OK';
    });
  });
});
Promise.all(tasks).then(function (r) {
  console.log(r.join('\n'));
  console.log('TOTAL=' + r.length);
}).catch(function (e) { console.log('ERR ' + e); });
