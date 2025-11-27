@echo off
echo Deploiement du dashboard de Noel sur le NAS...
echo.

REM Copie du fichier vers le NAS via SCP
scp christmas_dashboard.html Mac-Antho@192.168.1.174:/volume1/web/noel/

echo.
echo Deploiement termine!
echo Accedez au dashboard via: http://192.168.1.174/noel/christmas_dashboard.html
echo.
pause
