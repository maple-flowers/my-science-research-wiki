$wiki = "E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\wiki"
$plural = 0; $concept = 0; $entity = 0; $mismatch = 0; $total = 0
Get-ChildItem "$wiki\concepts","$wiki\entities" -Recurse -Filter *.md | ForEach-Object {
  $total++
  $c = Get-Content -Raw -Encoding UTF8 $_.FullName
  if ($c -match '(?m)^type:\s*(concepts|entities)\s*$') { $plural++ }
  $t = ''
  if ($c -match '(?m)^type:\s*(\S+)\s*$') { $t = $matches[1] }
  if ($t -eq 'concept') { $concept++ }
  if ($t -eq 'entity') { $entity++ }
  $head = ''
  if ($c -match '(?m)^tags:\s*\[([^\]]*)\]') { $head = ($matches[1] -split ',')[0].Trim() }
  if ($t -ne '' -and $head -ne $t) { $mismatch++ }
}
Write-Output "TOTAL=$total PLURAL=$plural concept=$concept entity=$entity TAGS_MISMATCH=$mismatch"
