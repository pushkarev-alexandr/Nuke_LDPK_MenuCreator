@echo off
set INIT_PATH=%USERPROFILE%\.nuke\init.py

:: Check if the line already exists in the file
findstr /C:"nuke.pluginAddPath('./3DE4')" "%INIT_PATH%" >nul
if %errorlevel% neq 0 (
    echo. >> "%INIT_PATH%"
    echo nuke.pluginAddPath^('./3DE4'^) >> "%INIT_PATH%"
)

xcopy "3DE4" "%USERPROFILE%\.nuke\3DE4" /E /I /Y
explorer "%USERPROFILE%\.nuke\3DE4"
rem pause
