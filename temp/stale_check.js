var files = app.vault.getMarkdownFiles();
var targets = ['bamboo-like-N-CNTs', 'glassy-carbon'];
var missing = [];
var resolved = {};
var p = Promise.all(files.map(function(f) {
  return app.vault.cachedRead(f).then(function(c) {
    var re = /\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]/g;
    var m;
    while ((m = re.exec(c)) !== null) {
      var target = m[1].trim();
      var base = target.split('/').pop();
      if (targets.indexOf(base) >= 0) {
        var dest = app.metadataCache.getFirstLinkpathDest(target, f.path);
        if (dest) {
          resolved[base] = dest.path;
        } else {
          missing.push(f.path + ' -> ' + target);
        }
      }
    }
  });
})).then(function() {
  var out = 'RESOLVED:\n';
  Object.keys(resolved).forEach(function(k) { out += k + ' => ' + resolved[k] + '\n'; });
  out += 'MISSING:\n';
  out += missing.length ? missing.join('\n') : '(none)';
  return out;
});
p;
