(async () => {
  const base = "科研Wiki/wiki/";
  const fixes = [
    ["concepts/easy-axis.md", "[[../entities/Fe3GeTe2|Fe₃GaTe₂]]", "[[../entities/Fe3GaTe2|Fe₃GaTe₂]]"],
    ["concepts/magnetic-anisotropy.md", "[[../entities/Fe3GeTe2|Fe₃GaTe₂]]", "[[../entities/Fe3GaTe2|Fe₃GaTe₂]]"],
  ];
  const out = [];
  for (const [p, old, neu] of fixes) {
    const fp = base + p;
    const txt = await app.vault.adapter.read(fp);
    if (!txt.includes(old)) { out.push(p + " :: NOT_FOUND"); continue; }
    const n = txt.split(old).length - 1;
    await app.vault.adapter.write(fp, txt.split(old).join(neu));
    out.push(p + " :: replaced x" + n);
  }
  return out.join("\n");
})();
