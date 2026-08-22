# Event Automation Monitor

Python monitor for Windows login, logout, lock, and unlock events.

It reads Windows Event Log entries and writes them to `events.csv`.

## Requirements

- Install Python 3 from <https://www.python.org/downloads/windows/>
- Run the monitor from an Administrator PowerShell if Windows says `Access is denied`

## What it tracks

- `4624` - successful login
- `4634` - logout
- `4647` - user started logout
- `4800` - workstation locked
- `4801` - workstation unlocked

Some Windows systems require administrator permissions to read the Security event log.

## Run once

```powershell
py .\login_logout_monitor.py --once
```

## Keep monitoring

```powershell
py .\login_logout_monitor.py
```

The monitor checks every 10 seconds by default:

```powershell
py .\login_logout_monitor.py --interval 5
```

## Start automatically when you log in

Run PowerShell as your normal user from this folder:

```powershell
.\setup_login_task.ps1
```

That creates a Windows Scheduled Task named `PythonLoginLogoutMonitor` that starts the monitor when you log in.
If your Windows account is an administrator, the task is registered with the highest available run level.

To remove it later:

```powershell
Unregister-ScheduledTask -TaskName PythonLoginLogoutMonitor -Confirm:$false
```
