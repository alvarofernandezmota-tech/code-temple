@echo off
REM Arranca TANK SCRAP 1990 en Windows: doble clic y a jugar.
REM Prepara el entorno la primera vez y no toca el Python del sistema.
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (set PY=py) else (set PY=python)

%PY% --version >nul 2>nul
if errorlevel 1 (
  echo No encuentro Python. Instalalo desde https://www.python.org/downloads/
  echo Marca "Add Python to PATH" en el instalador.
  pause
  exit /b 1
)

if not exist .venv (
  echo Preparando el entorno ^(solo la primera vez^)...
  %PY% -m venv .venv
)

.venv\Scripts\python.exe -c "import pygame" >nul 2>nul
if errorlevel 1 (
  echo Instalando pygame...
  .venv\Scripts\python.exe -m pip install --quiet --upgrade pip
  .venv\Scripts\python.exe -m pip install --quiet -r requirements.txt
)

echo Arrancando TANK SCRAP 1990 - flechas para moverte, B para construir.
.venv\Scripts\python.exe -m tank_scrap %*
if errorlevel 1 pause
