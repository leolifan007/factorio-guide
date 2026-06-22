# Factorio Guide SA Restructure Migration Script
# Moves flat /space-age/ articles into 7 sub-sections with Hugo aliases

$contentDir = 'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\content\space-age'

# ════════ File → Section Mapping ════════
$sections = [ordered]@{
    'planet-order-guide.md'         = 'guide'
    'vulcanus-guide.md'             = 'guide'
    'vulcanus-lava-processing.md'   = 'vulcanus'
    'fulgora-recycling-guide.md'    = 'fulgora'
    'fulgora-scrap-overflow.md'     = 'fulgora'
    'gleba-survival-guide.md'       = 'gleba'
    'gleba-bioflux-production.md'   = 'gleba'
    'gleba-pentapod-defense.md'     = 'gleba'
    'aquilo-guide.md'               = 'aquilo'
    'space-platform-guide.md'       = 'platform'
    'space-platform-ship-design.md' = 'platform'
    'cross-planet-logistics.md'     = 'platform'
    'quality-module-guide.md'       = 'quality'
    'quality-module-upcycling.md'   = 'quality'
}

# ════════ Create sub-directories ════════
$sections.Values | Select-Object -Unique | ForEach-Object {
    $d = "$contentDir\$_"
    if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force | Out-Null }
}

# ════════ Move files with aliases + fix garbled chars ════════
foreach ($file in $sections.Keys) {
    $section = $sections[$file]
    $oldPath = "$contentDir\$file"
    $newPath = "$contentDir\$section\$file"
    
    if (-not (Test-Path $oldPath)) { Write-Warning "NOT FOUND: $oldPath"; continue }
    
    # Read raw bytes to handle encoding issues
    $bytes = [System.IO.File]::ReadAllBytes($oldPath)
    
    # Fix garbled UTF-8 double-encoding (em dash — E2 80 94)
    # Pattern: 0xE9 0x88 0xA5 → "—"
    $fixBytes = New-Object 'System.Collections.Generic.List[byte]'
    $i = 0
    while ($i -lt $bytes.Length) {
        if ($i -le $bytes.Length - 3 -and $bytes[$i] -eq 0xE9 -and $bytes[$i+1] -eq 0x88 -and $bytes[$i+2] -eq 0xA5) {
            $fixBytes.AddRange([byte[]]@(0xE2, 0x80, 0x94))  # UTF-8 em dash
            $i += 3
        }
        elseif ($i -le $bytes.Length - 3 -and $bytes[$i] -eq 0xE9 -and $bytes[$i+1] -eq 0x88 -and $bytes[$i+2] -eq 0xAB) {
            $fixBytes.AddRange([byte[]]@(0xE2, 0x80, 0x94))
            $i += 3
        }
        else {
            $fixBytes.Add($bytes[$i])
            $i += 1
        }
    }
    
    $content = [System.Text.Encoding]::UTF8.GetString($fixBytes.ToArray())
    
    # Compute old URL alias
    $slug = [System.IO.Path]::GetFileNameWithoutExtension($file)
    $alias = "/space-age/$slug/"
    
    # Add aliases to YAML front matter
    if ($content -match '^(---\s*\n)(.*?)(\n---)(\n.*)$' -or $content -match '^(---\s*\r?\n)(.*?)(\r?\n---)(\r?\n.*)$') {
        $dashes = $matches[1]
        $frontMatter = $matches[2]
        $closing = $matches[3]
        $body = $matches[4]
        
        if ($frontMatter -notmatch '^aliases:') {
            $frontMatter += "`naliases:`n  - $alias"
        }
        
        $newContent = "$dashes$frontMatter$closing$body"
    } else {
        Write-Warning "No YAML front matter in $file"
        $newContent = $content
    }
    
    # Fix garbled emoji in front matter fields
    # Replace common garbled emoji patterns with clean text
    $patterns = @{
        '鈥?\s*' = '— '
        '鈿?' = ''
        '馃尶' = ''
        '馃拵' = ''
        '馃殌' = ''
    }
    foreach ($p in $patterns.Keys) { $newContent = $newContent -replace $p, $patterns[$p] }
    
    # Write to new location with clean UTF-8 (no BOM)
    [System.IO.File]::WriteAllText($newPath, $newContent, [System.Text.UTF8Encoding]::new($false))
    
    # Remove old file
    Remove-Item $oldPath -Force
    Write-Host "MOVED: $file → $section/"
}
