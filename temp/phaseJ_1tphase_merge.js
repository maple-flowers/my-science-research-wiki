// Phase J 方案B：1t-phase 双页合并 —— entities 版降为迁移说明页，6 实体页入链改指向 concepts
var newEntityPage = `---
tags: [entity, phase, material-structure, TMD]
title: 1T 相 / 1T-phase
type: entity
status: stub
aliases: [1T-phase]
formula: "MX2"
stoichiometry: 1T
class: [structure-phase, TMD]
properties: [octahedral-coordination, metallicity, CDW, Mott-insulator]
papers: [liPhaseTransitions2D2021, nakataRobustChargedensityWave2021, CastroNeto2001charge]
updated: 2026-08-19
---

# 1T 相 / 1T-phase

1T 相（1T phase）是过渡金属硫族化合物（TMD）中的一种晶体结构构型：过渡金属原子处于硫族原子构成的**八面体配位**环境，区别于三角棱柱配位的 2H 相。由于「1T 相」作为相构型概念在概念层已有规范页，本页保留为实体层别名/迁移说明页。

## 👵 太奶导读

乖孙，这一条是别名说明页。「1T 相」指 TMD 材料里金属原子坐在八面体配位中的晶体构型，它的完整机制（电荷密度波、磁性、相变工程）都在概念层的规范页里，从本页跳过去看就行。

## 名称与使用范围

- **规范页**：[[../concepts/1t-phase|1T 相（概念页）]]
- **使用范围**：1T 相是 TMD 晶体结构构型（与 2H、3R、1T′ 等同族的相概念），作为一般相构型概念归入概念层；具体材料体系中的 1T 相（如 1T-TaS₂、1T-VSe₂）在对应材料实体页中描述。

## 容易混淆的对象

- [[../entities/2h-phase|2H 相]]：三角棱柱配位的稳态相，与 1T 相对比。
- [[../concepts/1t-prime-phase|1T′ 相]]：1T 相的畸变衍生相。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/1t-phase|1T 相（概念页）]]：本名的规范页，含相构型机制、CDW 与磁性、相变工程等完整内容。
- [[../entities/TaS2|二硫化钽 (TaS₂)]]：1T 相代表性的材料体系。
- [[../entities/MoS2|二硫化钼 (MoS₂)]]：2H→1T 相变工程的代表性材料。

## 📚 相关论文 (Related Papers)

- [[../papers/liPhaseTransitions2D2021]]：系统分析了 1T 相及其衍生物相的相变与物理诱因。
- [[../papers/nakataRobustChargedensityWave2021]]：研究了 1T 相 TMD 中电子关联对 CDW 的增强作用。
- [[../papers/CastroNeto2001charge]]
`;

// 1) 重写 entities/1t-phase.md
var tasks = [];
var report = [];
var entPath = '科研Wiki/wiki/entities/1t-phase.md';
tasks.push(app.vault.adapter.write(entPath, newEntityPage).then(function () {
  report.push('entities/1t-phase.md: rewritten as migration page (status=stub)');
}));

// 2) 6 个实体页入链改向
var entPages = ['2h-phase', 'MoS2', 'MoTe2', 'TaS2', 'TiSe2', 'VSe2'];
entPages.forEach(function (slug) {
  var path = '科研Wiki/wiki/entities/' + slug + '.md';
  tasks.push(app.vault.adapter.read(path).then(function (content) {
    if (content.indexOf('[[../entities/1t-phase') === -1) {
      report.push(slug + '.md: NO_LINK skip');
      return;
    }
    var updated = content.split('[[../entities/1t-phase').join('[[../concepts/1t-phase');
    if (updated === content) { report.push(slug + '.md: NO_CHANGE'); return; }
    return app.vault.adapter.write(path, updated).then(function () {
      report.push(slug + '.md: link redirected to concepts/1t-phase');
    });
  }));
});

// 3) concepts/1t-phase.md 互链措辞调整
var conPath = '科研Wiki/wiki/concepts/1t-phase.md';
tasks.push(app.vault.adapter.read(conPath).then(function (content) {
  var oldLine = '- [[../entities/1t-phase|1T 相（实体页）]]：晶体结构、Peierls 不稳定性与相变工程（结构/物性侧重）。';
  var newLine = '- [[../entities/1t-phase|1T 相（实体层别名页）]]：本页的实体层别名/迁移说明页，含结构对比表与物性要点。';
  if (content.indexOf(oldLine) === -1) {
    report.push('concepts/1t-phase.md: OLD_LINE_NOT_FOUND');
    return;
  }
  var updated = content.split(oldLine).join(newLine);
  return app.vault.adapter.write(conPath, updated).then(function () {
    report.push('concepts/1t-phase.md: backlink wording adjusted');
  });
}));

Promise.all(tasks).then(function () {
  console.log(report.join('\n'));
  console.log('TOTAL=' + report.length);
}).catch(function (e) {
  console.log('ERR: ' + e);
});
