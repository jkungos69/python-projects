$ErrorActionPreference = "Stop"

$taskName = "PythonLoginLogoutMonitor"
$projectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$scriptPath = Join-Path $projectDir "login_logout_monitor.py"
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
$pyCommand = Get-Command py -ErrorAction SilentlyContinue

if ($pythonCommand) {
    $python = $pythonCommand.Source
    $arguments = "`"$scriptPath`""
} elseif ($pyCommand) {
    $python = $pyCommand.Source
    $arguments = "-3 `"$scriptPath`""
} else {
    throw "Python was not found. Install Python or make sure python.exe/py.exe is available."
}

$action = New-ScheduledTaskAction `
    -Execute $python `
    -Argument $arguments `
    -WorkingDirectory $projectDir

$trigger = New-ScheduledTaskTrigger -AtLogOn
$principal = New-ScheduledTaskPrincipal `
    -UserId "$env:USERDOMAIN\$env:USERNAME" `
    -LogonType Interactive `
    -RunLevel Highest
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 1)

Register-ScheduledTask `
    -TaskName $taskName `
    -Action $action `
    -Trigger $trigger `
    -Principal $principal `
    -Settings $settings `
    -Description "Starts the Python login/logout event monitor at user logon." `
    -Force | Out-Null

Write-Host "Created scheduled task: $taskName"
Write-Host "Events will be written to: $(Join-Path $projectDir 'events.csv')"
