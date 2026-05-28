# Example: dashboard setup

1. Produce a Webwright JSON output matching `templates/dashboard-data-contract.json`.
2. Copy `dashboards/minimal-dashboard.html` to your dashboard filename.
3. Inject the latest JSON payload.

Windows:

```powershell
.\scripts\update-dashboard.ps1 -DataPath outputs\my-use-case\final_runs\run_1\data.json -DashboardPath dashboards\my-dashboard.html
```

macOS/Linux:

```bash
bash scripts/update-dashboard.sh outputs/my-use-case/final_runs/run_1/data.json dashboards/my-dashboard.html
```
