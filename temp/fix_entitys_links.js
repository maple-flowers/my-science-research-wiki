var files = app.vault.getMarkdownFiles();
var changed = [];
var p = Promise.all(files.map(function(f) {
  return app.vault.cachedRead(f).then(function(c) {
    var n = c;
    n = n.split('../entitys/bamboo-like-N-CNTs').join('../entities/bamboo-like-N-CNTs');
    n = n.split('../entitys/glassy-carbon').join('../entities/glassy-carbon');
    if (n !== c) {
      changed.push(f.path);
      return app.vault.adapter.write(f.path, n);
    }
  });
})).then(function() { return changed.join('\n') || 'NO_CHANGE'; });
p;
