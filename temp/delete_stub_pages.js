(() => {
  const targets = ['科研Wiki/wiki/entities/1t-phase.md', '科研Wiki/wiki/concepts/bamboo-like-N-CNTs.md', '科研Wiki/wiki/concepts/glassy-carbon.md'];
  const done = [];
  return Promise.all(targets.map(rel => {
    const f = app.vault.getAbstractFileByPath(rel);
    if (!f) { done.push(rel + ': NOT_FOUND'); return Promise.resolve(); }
    return app.vault.trash(f, true).then(() => { done.push(rel + ': trashed'); });
  })).then(() => done.join('\n'));
})()
