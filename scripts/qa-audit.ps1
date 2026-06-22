# QA Auditer – Factorio Guide SOP

$base = 'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide'
$articles = Get-ChildItem "$base\content\space-age" -Recurse -Filter *.md | Where-Object { $_.Name -notin @('_index.md', 'SA_CONTENT_PLAN.md') }

$allPass = $true
$totalWarn = 0

foreach ($article in $articles) {
    $rel = $article.FullName.Replace("$base\", "")
    $w = 0
    $c = [System.IO.File]::ReadAllText($article.FullName, [System.Text.Encoding]::UTF8)
    $len = $c.Length
    $lines = $c -split "`n"
    $bodyStart = $c.IndexOf('---', 3)
    $body = ''
    if ($bodyStart -gt 0) { $body = $c.Substring($bodyStart + 3) }
    
    Write-Host "== $rel == ($len chars)"
    
    # 1. No BOM
    $bytes = [System.IO.File]::ReadAllBytes($article.FullName)
    if ($bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) { $w++; Write-Host "  FAIL: BOM detected" }
    else { Write-Host "  OK: No BOM" }
    
    # 2. Front matter
    if (-not $c.StartsWith('---')) { $w++; Write-Host "  FAIL: Missing front matter" }
    else { Write-Host "  OK: Front matter" }
    
    # 3. Title
    if ($c -notmatch '(?m)^title: ') { $w++; Write-Host "  FAIL: No title" }
    else { Write-Host "  OK: Title" }
    
    # 4. Description
    if ($c -notmatch '(?m)^description: ') { $w++; Write-Host "  FAIL: No description" }
    else { Write-Host "  OK: Description" }
    
    # 5. Tags
    if ($c -notmatch '(?m)^tags: ') { $w++; Write-Host "  FAIL: No tags" }
    else { Write-Host "  OK: Tags" }
    
    # 6. Aliases
    if ($c -notmatch '(?m)^aliases:') { $w++; Write-Host "  FAIL: No aliases" }
    else { Write-Host "  OK: Aliases" }
    
    # 7. Diagrams
    $diag = ([regex]::Matches($c, '{{<\s*diagram\s+')).Count
    if ($diag -lt 1) { $w++; Write-Host "  FAIL: 0 diagrams" }
    else { Write-Host "  OK: $diag diagram(s)" }
    
    # 8. Tables (count consecutive |...| lines >= 3 = 1 table)
    $tblCount = 0
    $inRow = $false; $rowN = 0
    foreach ($line in $lines) {
        $t = $line.TrimStart()
        if ($t.StartsWith('|') -and $t.EndsWith('|')) {
            $rowN++
            $inRow = $true
        } else {
            if ($inRow -and $rowN -ge 3) { $tblCount++ }
            $inRow = $false; $rowN = 0
        }
    }
    if ($tblCount -lt 2) { $w++; Write-Host "  FAIL: $tblCount table(s), need >= 2" }
    else { Write-Host "  OK: $tblCount table(s)" }
    
    # 9. Material icons
    $mat = ([regex]::Matches($c, '{{<\s*material\s+')).Count
    if ($mat -lt 2) { $w++; Write-Host "  FAIL: $mat material icon(s), need >= 2" }
    else { Write-Host "  OK: $mat material icon(s)" }
    
    # 10. Internal refs
    $refs = ([regex]::Matches($c, '{{<\s*ref\s+')).Count
    if ($refs -lt 2) { $w++; Write-Host "  FAIL: $refs ref(s), need >= 2" }
    else { Write-Host "  OK: $refs ref(s)" }
    
    # 11. Smart quotes
    if ($c -match "[\x{2018}\x{2019}\x{201C}\x{201D}]") { $w++; Write-Host "  FAIL: Smart (curly) quotes found" }
    else { Write-Host "  OK: No smart quotes" }
    
    # 12. Body length
    $bl = if ($bodyStart -gt 0) { $body.Length } else { $len }
    if ($bl -lt 5000) { $w++; Write-Host "  FAIL: Body $bl chars (need >= 5000)" }
    else { Write-Host "  OK: Body $bl chars" }
    
    # 13. Em-dash warning (non-fatal)
    if ($c -match "[\x{2013}\x{2014}\x{2015}]") { Write-Host "  NOTE: em-dash detected (ensure byte-level encoding is correct)" }
    else { Write-Host "  OK: No em-dash" }
    
    $status = if ($w -le 3) { 'PASS' } else { 'FAIL' }
    if ($status -eq 'FAIL') { $allPass = $false }
    $totalWarn += $w
    Write-Host "  => $status (warnings: $w)"
    Write-Host ""
}

Write-Host "================================"
Write-Host "TOTAL: $($articles.Count) articles, $totalWarn warnings"
if ($allPass) { Write-Host "RESULT: ALL PASS" } else { Write-Host "RESULT: SOME FAIL - needs fixes" }
