# =========================================================================
# CONFIGURADOR DE TAREA PROGRAMADA EN WINDOWS (Task Scheduler)
# =========================================================================
# Este script registra la ejecución automática diaria de groq_automator.py
# a las 8:00 AM de forma local en segundo plano.

$taskName = "MensajesPositivosDiarios"
$workingDir = "C:\Users\neo\Documents\agente\mensajes positivos"
$scriptPath = "$workingDir\groq_automator.py"

# Encontrar ruta de python
$pythonPath = (Get-Command python.exe -ErrorAction SilentlyContinue).Source
if (-not $pythonPath) {
    $pythonPath = "python"
}

Write-Host "Registrando tarea programada: $taskName" -ForegroundColor Cyan
Write-Host "Directorio de trabajo: $workingDir"
Write-Host "Ruta de Python: $pythonPath"

# Crear acción de la tarea
$action = New-ScheduledTaskAction -Execute $pythonPath -Argument "`"$scriptPath`"" -WorkingDirectory $workingDir

# Crear disparador diario a las 8:00 AM
$trigger = New-ScheduledTaskTrigger -Daily -At 8:00AM

# Crear configuraciones de compatibilidad y ahorro de energía
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

# Registrar la tarea en el sistema (requiere privilegios de ejecución)
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Force

Write-Host ""
Write-Host "¡TAREA PROGRAMADA REGISTRADA EXITOSAMENTE!" -ForegroundColor Green
Write-Host "La tarea se ejecutará de forma silenciosa todos los días a las 8:00 AM." -ForegroundColor Yellow
Write-Host "Puedes monitorear las ejecuciones y logs en: $workingDir\scratch\automation_log.txt"
