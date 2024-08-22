@echo off

:: setting path
set PYTHON_PATH=C:\Users\_PLACEHOLDER_
set SCRIPT_PATH=C:\Users\_PLACEHOLDER_

:: run script
:loop
%PYTHON_PATH% %SCRIPT_PATH%
timeout /t 15
goto loop