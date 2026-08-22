(() => {
  const fs = require('fs');
  const base = 'E:/swan_goose/宝宝/笔记库/sgg/科研Wiki/wiki/';
  const edits = [
    ['papers/Wei2021.md', '[[../concepts/bamboo-like-N-CNTs|bamboo-like-N-CNTs]]', '[[../entities/bamboo-like-N-CNTs|bamboo-like-N-CNTs]]'],
    ['papers/Doroodmand2017conjugated.md', '[[../concepts/glassy-carbon|玻碳电极]]', '[[../entities/glassy-carbon|玻碳电极]]'],
    ['concepts/1t-phase.md', '\n- [[../entities/1t-phase|1T 相（实体层别名页）]]：本页的实体层别名/迁移说明页，含结构对比表与物性要点。', '']
  ];
  const out = [];
  for (const [rel, from, to] of edits) {
    const p = base + rel;
    const t0 = fs.readFileSync(p, 'utf8');
    const cnt = t0.split(from).length - 1;
    if (cnt === 0) { out.push(rel + ': NO_MATCH'); continue; }
    const t1 = t0.split(from).join(to);
    fs.writeFileSync(p, t1, 'utf8');
    out.push(rel + ': replaced=' + cnt);
  }
  return out.join('\n');
})()
