# 全库 wikilink 断链校验（磁盘直扫，不依赖 Obsidian cache）
$vault = "E:\swan_goose\宝宝\笔记库\sgg"
$wiki = "E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\wiki"
$allFiles = Get-ChildItem -Path $wiki -Recurse -Filter *.md
$nameIndex = @{}
foreach ($f in $allFiles) {
  $base = [System.IO.Path]::GetFileNameWithoutExtension($f.Name)
  if (-not $nameIndex.ContainsKey($base)) { $nameIndex[$base] = @() }
  $nameIndex[$base] += $f.FullName
}
$missing = @{}
$total = 0
foreach ($f in $allFiles) {
  $dir = $f.DirectoryName
  $content = Get-Content -Raw -Encoding UTF8 $f.FullName
  $matches = [regex]::Matches($content, '\[\[([^\]]+?)\]\]')
  foreach ($m in $matches) {
    $link = $m.Groups[1].Value.Trim()
    # 去掉锚点 #section
    $link = ($link -split '#')[0]
    # 去掉显示文本
    $link = ($link -split '\|')[0]
    if ($link -match '^(\.\.?/)') {
      # 相对路径链接
      $rel = [System.IO.Path]::GetFullPath((Join-Path $dir $link))
      if (-not [System.IO.File]::Exists($rel)) {
        $total++
        if (-not $missing.ContainsKey($link)) { $missing[$link] = @() }
        if ($missing[$link].Count -lt 8) { $missing[$link] += $f.FullName.Replace($wiki, 'wiki') }
      }
    } else {
      # 裸链接按 basename 匹配
      $base = $link
      if (-not $nameIndex.ContainsKey($base)) {
        $total++
        if (-not $missing.ContainsKey($link)) { $missing[$link] = @() }
        if ($missing[$link].Count -lt 8) { $missing[$link] += $f.FullName.Replace($wiki, 'wiki') }
      }
    }
  }
}
$out = "MISSING_TOTAL=$total`n"
foreach ($k in ($missing.Keys | Sort-Object)) {
  $out += "[$k]`n"
  foreach ($v in $missing[$k]) { $out += "  $v`n" }
}
$dest = "C:\Users\sgg\AppData\Roaming\Tencent\Marvis\User\oAN1i2V14p5-lhhSY365mxizlI-c\workspace\conv_1a0000cc73d_3cc2a0c40aa4\temp\disk_stale_check.txt"
[System.IO.File]::WriteAllText($dest, $out, (New-Object System.Text.UTF8Encoding($false)))
Write-Output "DONE total=$total unique=$($missing.Count)"
