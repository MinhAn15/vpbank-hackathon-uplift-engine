# Dry run timer for rehearsals (PowerShell)
# Usage: .\scripts\dry_run_timer.ps1 -minutes 5
param(
    [int]$minutes = 5
)
$seconds = $minutes * 60
Write-Host "Starting dry-run timer: $minutes minute(s)"
for ($i=$seconds; $i -ge 0; $i--) {
    $m = [math]::Floor($i/60)
    $s = $i % 60
    Write-Host -NoNewline "\rTime left: {0:00}:{1:00} " -f $m, $s
    Start-Sleep -Seconds 1
}
Write-Host "`nTime's up!" -ForegroundColor Yellow
