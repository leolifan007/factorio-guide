# SA Migration V4 - Simple approach, no regex fuss
$repoDir = 'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide'
$contentDir = Join-Path $repoDir 'content\space-age'

# Restore from git
cd $repoDir; git checkout -- content/space-age/ 2>$null

# Remove old sub-dirs if exist
Get-ChildItem $contentDir -Directory | Where-Object { $_.Name -in @('guide','vulcanus','fulgora','gleba','aquilo','platform','quality') } | Remove-Item -Recurse -Force

# Verify we have the files
Write-Host "Source files:"
Get-ChildItem $contentDir -Filter *.md -Name | Where-Object { $_ -ne '_index.md' -and $_ -ne 'SA_CONTENT_PLAN.md' }

# Mapping
$mapping = [ordered]@{
    'guide'    = @('planet-order-guide.md', 'vulcanus-guide.md')
    'fulgora'  = @('fulgora-recycling-guide.md')
    'gleba'    = @('gleba-survival-guide.md')
    'aquilo'   = @('aquilo-guide.md')
    'platform' = @('space-platform-guide.md')
    'quality'  = @('quality-module-guide.md')
}

# Create subdirs
foreach ($sec in $mapping.Keys) {
    $null = New-Item -ItemType Directory -Path (Join-Path $contentDir $sec) -Force
}

# Migrate each file
foreach ($sec in $mapping.Keys) {
    $subdir = Join-Path $contentDir $sec
    foreach ($file in $mapping[$sec]) {
        $oldPath = Join-Path $contentDir $file
        $newPath = Join-Path $subdir $file
        
        if (-not (Test-Path $oldPath)) { Write-Warning "MISSING: $file"; continue }
        
        Write-Host "→ $file  →  $sec/"
        $content = [System.IO.File]::ReadAllText($oldPath, [System.Text.Encoding]::UTF8)
        
        # Get slug for alias
        $slug = [System.IO.Path]::GetFileNameWithoutExtension($file)
        $alias = "/space-age/$slug/"
        
        # Simple front matter processing - split on --- boundaries
        $trimmed = $content.TrimStart()
        if ($trimmed.StartsWith('---')) {
            $endOfFM = $trimmed.IndexOf('---', 3)
            if ($endOfFM -gt 0) {
                $fm = $trimmed.Substring(3, $endOfFM - 3)
                $body = $trimmed.Substring($endOfFM + 3)
                
                # Check if aliases already present
                if ($fm -notmatch '(?m)^aliases:') {
                    $fm = $fm.TrimEnd() + "`naliases:`n  - $alias"
                }
                
                $newContent = "---$fm---$body"
                [System.IO.File]::WriteAllText($newPath, $newContent, [System.Text.UTF8Encoding]::new($false))
            }
        }
        
        Remove-Item $oldPath -Force
    }
}

# Verify
Write-Host "`n=== Verification ==="
$ok = 0; $bad = 0
foreach ($sec in $mapping.Keys) {
    $subdir = Join-Path $contentDir $sec
    foreach ($file in $mapping[$sec]) {
        $fp = Join-Path $subdir $file
        if (-not (Test-Path $fp)) { Write-Host "  ✗ $sec/$file - MISSING"; $bad++; continue }
        $c = [System.IO.File]::ReadAllText($fp, [System.Text.Encoding]::UTF8)
        $clean = $c.StartsWith('---')
        $alias = $c -match '(?m)^aliases:'
        Write-Host "  ✓ $sec/$file  clean=$clean  alias=$alias"
        if ($clean -and $alias) { $ok++ } else { $bad++ }
    }
}
Write-Host "`nTotal: $ok OK, $bad FAIL"
