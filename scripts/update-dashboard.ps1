param(
  [Parameter(Mandatory = $true)] [string]$DataPath,
  [Parameter(Mandatory = $true, ValueFromRemainingArguments = $true)] [string[]]$DashboardPath
)
$ErrorActionPreference = "Stop"

# Generation-side fix for hsf_c8c57fa44fb445a77fa4423b: JSON-parse + canonical
# re-serialize the payload instead of splicing raw text with only '</script>'
# escaped. Uses the same shared update_dashboard.py gate as the bash variant.
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not (Test-Path -LiteralPath $DataPath)) { throw "Data file not found: $DataPath" }
foreach ($d in $DashboardPath) {
  if (-not (Test-Path -LiteralPath $d)) { throw "Dashboard file not found: $d" }
}

& python3 (Join-Path $ScriptDir "update_dashboard.py") $DataPath @DashboardPath
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$refreshedAt = (Get-Date).ToString("s")
[pscustomobject]@{ dashboard = ($DashboardPath -join ", "); data = $DataPath; refreshedAt = $refreshedAt } | ConvertTo-Json
