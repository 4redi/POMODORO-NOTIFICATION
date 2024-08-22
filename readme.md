# Pomodoro Notification
A python desktop notification to remind me to take a break using the pomodoro technique (25minutes work x 5minutes break)

# Installing
- clone the repo
- install the ```plyer``` library
- open the explain.bat and replace with your paths
- open task scheduler (use ```WIN+R``` then type ```taskschd. msc```)
- create a new task (enter title + a simple description)
- select run time (i chose when i log in)
- chose a starter file (browse to the ```explain.bat``` file)
- click Finish


# !
License -> [MIT](LICENSE)


### Script for explain.bat

```BAT
: Replace placeholder with your own path
@echo off

:: setting path
set PYTHON_PATH=C:\Users\_PLACEHOLDER_
set SCRIPT_PATH=C:\Users\_PLACEHOLDER_

:: run script
:loop
%PYTHON_PATH% %SCRIPT_PATH%
timeout /t 15
goto loop

```