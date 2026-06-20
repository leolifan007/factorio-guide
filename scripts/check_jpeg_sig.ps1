$base = "C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide"

Write-Host "=== 正常显示的3张图片签名 ==="
$good = @("your-first-factory.jpg","smelting-ratios.jpg","basic-rail-network.jpg")
foreach ($f in $good) {
    $p = Join-Path $base "static\images\featured" $f
    $bytes = [System.IO.File]::ReadAllBytes($p)
    $sig = "0x{0:X2}{1:X2}" -f $bytes[0],$bytes[1]
    Write-Host "$f : $sig ($($bytes.Length) bytes)"
}

Write-Host "`n=== 修复的3张图片签名 ==="
$bad = @("main-bus-design.jpg","red-science-pack.jpg","quality-modules.jpg")
foreach ($f in $bad) {
    $p = Join-Path $base "static\images\featured" $f
    $bytes = [System.IO.File]::ReadAllBytes($p)
    $sig = "0x{0:X2}{1:X2}" -f $bytes[0],$bytes[1]
    Write-Host "$f : $sig ($($bytes.Length) bytes)"
}
