param(
  [Parameter(Mandatory = $true)] [string]$DataPath,
  [Parameter(Mandatory = $true)] [string]$DashboardPath
)
$ErrorActionPreference = "Stop"
if (-not (Test-Path -LiteralPath $DataPath)) { throw "Data file not found: $DataPath" }
if (-not (Test-Path -LiteralPath $DashboardPath)) { throw "Dashboard file not found: $DashboardPath" }
$json = (Get-Content -Raw -LiteralPath $DataPath).Replace("</script>", "<\/script>")
$html = Get-Content -Raw -LiteralPath $DashboardPath
$replacement = '<script id="payload" type="application/json">' + $json + '</script>'
$updated = [regex]::Replace($html, '<script id="payload" type="application/json">.*?</script>', $replacement, [System.Text.RegularExpressions.RegexOptions]::Singleline)
Set-Content -LiteralPath $DashboardPath -Value $updated -Encoding UTF8
[pscustomobject]@{ dashboard = $DashboardPath; data = $DataPath; refreshedAt = (Get-Date).ToString("s") } | ConvertTo-Json
