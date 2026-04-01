@echo off
echo Iniciando Bot Horas...

:: Inicia el servidor Python en una ventana nueva
start "Servidor Bot Horas" cmd /k "cd /d %~dp0 && python servidor_final.py"

:: Espera 3 segundos a que arranque el servidor
timeout /t 3 /nobreak

:: Inicia ngrok en otra ventana nueva
start "Ngrok Bot Horas" cmd /k "cd /d %~dp0 && ngrok http 4321"

echo Bot iniciado correctamente.
