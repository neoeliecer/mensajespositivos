@echo off
title Dashboard de Mensajes Positivos
chcp 65001 >nul

:: Directorio de trabajo
cd /d "C:\Users\neo\Documents\agente\mensajes positivos\dashboard"

echo ==========================================================
echo 🌟 INICIADOR AUTOMÁTICO DEL DASHBOARD DE MENSAJES POSITIVOS
echo ==========================================================
echo.

:: Verificar si el puerto 3000 ya está en uso por Next.js
netstat -ano | findstr :3000 >nul
if %errorlevel% equ 0 (
    echo [✓] El servidor local ya está en ejecución.
    echo [i] Abriendo tu navegador de internet en: http://localhost:3000
    start http://localhost:3000
) else (
    echo [i] El servidor no está corriendo. Iniciando Next.js en puerto 3000...
    
    :: Ejecutar el servidor en segundo plano minimizado
    start /min "Servidor Next.js - Mensajes Positivos" cmd /c npm run dev
    
    echo [i] Esperando 5 segundos a que el servidor esté listo...
    timeout /t 5 /nobreak >nul
    
    echo [✓] Servidor iniciado. Abriendo navegador...
    start http://localhost:3000
)

echo.
echo ==========================================================
echo Puedes dejar esta ventana abierta o cerrarla. ¡Listo!
echo ==========================================================
timeout /t 3 >nul
exit
