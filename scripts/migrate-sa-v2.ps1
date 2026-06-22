# Clean SA Migration Script - V2
# Move files, add Hugo aliases, preserve content integrity

$contentDir = 'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\content\space-age'

$mapping = [ordered]@{
    'guide'    = @('planet-order-guide.md', 'vulcanus-guide.md')
    'vulcanus' = @('vulcanus-lava-processing.md')
    'fulgora'  = @('fulgora-recycling-guide.md', 'fulgora-scrap-overflow.md')
    'gleba'    = @('gleba-survival-guide.md', 'gleba-bioflux-production.md', 'gleba-pentapod-defense.md')
    'aquilo'   = @('aquilo-guide.md')
    'platform' = @('space-platform-guide.md', 'space-platform-ship-design.md', 'cross-planet-logistics.md')
    'quality'  = @('quality-module-guide.md', 'quality-module-upcycling.md')
}

# Create sub-directories
foreach ($sec in $mapping.Keys) {
    $dir = Join-Path $contentDir $sec
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
}

function Add-AliasToFrontMatter {
    param([string]$content, [string]$alias)
    
    # Match YAML front matter --- ... ---
    $regex = [regex]'^---\s*\r?\n(.*?)\r?\n---\r?\n'
    $match = $regex.Match($content)
    if (-not $match.Success) { return $null }
    
    $fm = $match.Groups[1].Value
    $body = $content.Substring($match.Length)
    
    # Add aliases if not present
    if ($fm -notmatch '(?m)^aliases:') {
        $fm += "`naliases:`n  - $alias"
    }
    
    return "---`n$fm`n---`n$body"
}

foreach ($sec in $mapping.Keys) {
    $subdir = Join-Path $contentDir $sec
    
    foreach ($file in $mapping[$sec]) {
        $oldPath = Join-Path $contentDir $file
        $newPath = Join-Path $subdir $file
        
        if (-not (Test-Path $oldPath)) { Write-Warning "NOT FOUND: $oldPath"; continue }
        
        # Read file with explicit UTF-8
        Write-Host "Processing: $file → $sec/"
        $content = [System.IO.File]::ReadAllText($oldPath, [System.Text.Encoding]::UTF8)
        
        # Build alias
        $slug = [System.IO.Path]::GetFileNameWithoutExtension($file)
        $alias = "/space-age/$slug/"
        
        # Add aliases to front matter
        $newContent = Add-AliasToFrontMatter -content $content -alias $alias
        if (-not $newContent) {
            Write-Warning "No YAML front matter in $file, copying as-is"
            $newContent = $content
        }
        
        # Write to new location
        [System.IO.File]::WriteAllText($newPath, $newContent, [System.Text.UTF8Encoding]::new($false))
        
        # Remove old file
        Remove-Item $oldPath -Force
    }
}

Write-Host "`nDone! Checking results..."
Get-ChildItem $contentDir -Recurse -Filter *.md | ForEach-Object {
    $c = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
    $hasAlias = $c -match 'aliases:'
    Write-Host "  $($_.Directory.Name)/$($_.Name) - aliases:$hasAlias"
}
