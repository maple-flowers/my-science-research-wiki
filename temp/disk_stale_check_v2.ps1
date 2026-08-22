# 全库 wikilink 断链校验（磁盘直扫，不依赖 Obsidian cache）v2
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
$bad = @{}
$total = 0
$badTotal = 0
foreach ($f in $allFiles) {
  $dir = $f.DirectoryName
  $relPath = $f.FullName.Replace($wiki, 'wiki')
  if ($relPath -match 'format-spec\.md$') { continue }
  $content = Get-Content -Raw -Encoding UTF8 $f.FullName
  $matches = [regex]::Matches($content, '\[\[([^\]]+?)\]\]')
  foreach ($m in $matches) {
    $link = $m.Groups[1].Value.Trim()
    $link = ($link -split '#')[0]
    $link = $link -replace '\\\|', '|'
    $link = ($link -split '\|')[0]
    if ($link -eq '') { continue }
    if ($link -match '^(\.\.?/)') {
      try {
        $rel = [System.IO.Path]::GetFullPath((Join-Path $dir $link))
      } catch {
        $badTotal++
        if (-not $bad.ContainsKey($link)) { $bad[$link] = 0 }
        $bad[$link]++
        continue
      }
      if (-not [System.IO.File]::Exists($rel) -and -not [System.IO.File]::Exists($rel + '.md')) {
        $total++
        if (-not $missing.ContainsKey($link)) { $missing[$link] = @() }
        if ($missing[$link].Count -lt 8) { $missing[$link] += $f.FullName.Replace($wiki, 'wiki') }
      }
    } else {
      $base = $link
      if (-not $nameIndex.ContainsKey($base)) {
        $total++
        if (-not $missing.ContainsKey($link)) { $missing[$link] = @() }
        if ($missing[$link].Count -lt 8) { $missing[$link] += $f.FullName.Replace($wiki, 'wiki') }
      }
    }
  }
}
$out = "MISSING_TOTAL=$total BAD_LINK_TOTAL=$badTotal`n"
foreach ($k in ($missing.Keys | Sort-Object)) {
  $out += "[$k]`n"
  foreach ($v in $missing[$k]) { $out += "  $v`n" }
}
if ($bad.Count -gt 0) {
  $out += "`nBAD_PATHS:`n"
  foreach ($k in ($bad.Keys | Sort-Object)) { $out += "[$k] x$($bad[$k])`n" }
}
$dest = "C:\Users\sgg\AppData\Roaming\Tencent\Marvis\User\oAN1i2V14p5-lhhSY365mxizlI-c\workspace\conv_1a0000cc73d_3cc2a0c40aa4\temp\disk_stale_check.txt"
[System.IO.File]::WriteAllText($dest, $out, (New-Object System.Text.UTF8Encoding($false)))
Write-Output "DONE total=$total bad=$badTotal unique=$($missing.Count)"
