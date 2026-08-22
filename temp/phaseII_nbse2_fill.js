(async () => {
  const path = '科研Wiki/wiki/entities/NbSe2.md';
  const content = await app.vault.adapter.read(path);
  const marker = '## 🔬 电子结构与费米面\n';
  if (!content.includes(marker)) return 'marker-not-found';
  const newText = marker + '\n2H-NbSe₂ 是金属，费米面附近的电子态主要由 Nb 的 4d 能带贡献，在布里渊区中形成多个空穴与电子口袋。ARPES 等实验对费米面形状与能带色散的直接测量，是将 CDW 起因与超导配对联系起来的核心证据。早期理论把 CDW 归因于费米面嵌套驱动的电荷不稳定性，但进一步研究表明动量依赖的电子-声子耦合对 CDW 波矢的选择同样重要，因此需要结合能带结构、声子色散与电子-声子矩阵元共同解释。单层 NbSe₂ 的 CDW 转变温度相比块体升高，说明维度降低与屏蔽减弱会改变电子-声子相互作用和关联强度，进而重新平衡 CDW 与超导两种序。\n';
  const idx = content.indexOf(marker);
  const after = content.slice(idx + marker.length);
  // 该节原有一句占位，替换标题后到下一节前的整段
  const next = after.indexOf('\n## ');
  const oldBlock = marker + after.slice(0, next);
  const updated = content.replace(oldBlock, newText);
  await app.vault.adapter.write(path, updated);
  return 'OK';
})()
