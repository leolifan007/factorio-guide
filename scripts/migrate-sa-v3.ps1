# Clean SA Migration - V3
# Step 1: Restore tracked files, Step 2: Move with aliases

$repoDir = 'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide'
$contentDir = Join-Path $repoDir 'content\space-age'

# Restore tracked files from git (if missing)
cd $repoDir
git checkout -- content/space-age/ 2>$null

# Verify we have the tracked files
$tracked = @('vulcanus-guide.md','planet-order-guide.md','fulgora-recycling-guide.md','gleba-survival-guide.md','aquilo-guide.md','space-platform-guide.md','quality-module-guide.md')
Write-Host "Found files:"
Get-ChildItem $contentDir -Filter *.md -Name | ForEach-Object { Write-Host "  $_" }

# Mapping: section => files
$mapping = [ordered]@{
    'guide'    = @('planet-order-guide.md', 'vulcanus-guide.md')
    'fulgora'  = @('fulgora-recycling-guide.md')
    'gleba'    = @('gleba-survival-guide.md')
    'aquilo'   = @('aquilo-guide.md')
    'platform' = @('space-platform-guide.md')
    'quality'  = @('quality-module-guide.md')
}

# Create sub-directories
foreach ($sec in $mapping.Keys) {
    $dir = Join-Path $contentDir $sec
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
}

# Process each file
$errors = @()
foreach ($sec in $mapping.Keys) {
    $subdir = Join-Path $contentDir $sec
    foreach ($file in $mapping[$sec]) {
        $oldPath = Join-Path $contentDir $file
        $newPath = Join-Path $subdir $file
        
        if (-not (Test-Path $oldPath)) {
            $errors += "MISSING: $file"
            continue
        }
        
        Write-Host "Moving: $file  →  $sec/"
        
        # Read with UTF-8
        $content = [System.IO.File]::ReadAllText($oldPath, [System.Text.Encoding]::UTF8)
        
        # Verify front matter exists
        if (-not $content.StartsWith('---')) {
            $errors += "NO_FRONT_MATTER: $file - copying as-is"
        } else {
            # Build alias
            $slug = [System.IO.Path]::GetFileNameWithoutExtension($file)
            $alias = "/space-age/$slug/"
            
            # Add aliases to YAML front matter (between first --- and second ---)
            $regex = [regex]'^(---\s*\r?\n)(.*?)(\r?\n---)'
            $m = $regex.Match($content)
            if ($m.Success) {
                $fm = $m.Groups[2].Value
                if ($fm -notmatch '(?m)^aliases:') {
                    $fm = "$fm`naliases:`n  - $alias"
                    $content = $m.Groups[1].Value + $fm + $m.Groups[3].Value + $content.Substring($m.Length)
                }
            }
        }
        
        # Write to new location (UTF-8 no BOM)
        [System.IO.File]::WriteAllText($newPath, $content, [System.Text.UTF8Encoding]::new($false))
        
        # Delete old file
        Remove-Item $oldPath -Force
    }
}

# Verify
Write-Host "`n=== Verification ==="
$total = 0
foreach ($sec in $mapping.Keys) {
    $subdir = Join-Path $contentDir $sec
    Get-ChildItem $subdir -Filter *.md | ForEach-Object {
        $c = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
        $hasAliases = ($c -match 'aliases:')
        $isClean = ($c -match '^---')
        Write-Host "  $sec/$($_.Name)  clean=$isClean  aliases=$hasAliases"
        $total++
    }
}
Write-Host "Total files migrated: $total"

if ($errors.Count -gt 0) {
    Write-Host "`n=== ERRORS ==="
    $errors | ForEach-Object { Write-Host "  $_" }
}
