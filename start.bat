@echo off
echo "Démarrage en cours ..."
python.exe run_app.py
echo "Fin du programme"
pause



REM @echo off
REM title Animation

REM set count=0
REM cls

REM echo Demarrage en cours ...

REM :loop
REM set /A count+=1

REM if %count%==1 (
  REM set "dots=."
REM ) else if %count%==2 (
  REM set "dots=.."
REM ) else if %count%==3 (
  REM set "dots=..."
REM )

setlocal enabledelayedexpansion
set "message=Demarrage en cours %dots%"
echo !message!

if %count%==3 (
  set count=0
)

timeout 1 > nul
goto loop