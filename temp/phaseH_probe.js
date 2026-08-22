var path = '科研Wiki/wiki/concepts/ferroelectricity.md';
var marker = '## \u{1F4DA} 相关论文 (Related Papers)';
app.vault.adapter.read(path).then(function (content) {
  console.log('READ lines=' + content.split('\n').length + ' hasMarker=' + content.indexOf(marker));
  console.log('DONE');
});
