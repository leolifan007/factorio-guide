$repo = "C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide"
Set-Location $repo

# Copy old missing images
Copy-Item "static\images\featured\main-bus.jpg" "static\images\featured\main-bus-design.jpg"
Copy-Item "static\images\featured\red-science.jpg" "static\images\featured\red-science-pack.jpg"
Copy-Item "static\images\featured\quality-module.jpg" "static\images\featured\quality-modules.jpg"
Write-Host "Old image copies created"

# Rebuild
Remove-Item -Recurse -Force docs -ErrorAction SilentlyContinue
& "C:\Program Files\QClaw\v0.2.26.557\resources\openclaw\config\bin\node.cmd" "C:\Users\ROG\AppData\Roaming\QClaw\npm-global\node_modules\hugo-bin\bin\cli.js" --minify 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "Build OK"
} else {
    Write-Host "Build FAILED"
}
