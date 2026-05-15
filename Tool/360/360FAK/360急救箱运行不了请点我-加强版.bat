@echo off
title=保护模式

cd %~dp0

set myname=%~dp0
set   count=0
for /r %~dp0 %%i in (*SuperKillller.exe) do call :add

if   /i  %count%  LSS  1   (echo 请用压缩软件解压后,到目录中运行!)
if   /i  %count%  LSS  1   (pause)
if   /i  %count%  LSS  1   (exit)

del /f  /q "%myname%%username%*.exe"


for /f "tokens=1-3 delims=-" %%a in ("%date:~0,10%") do (rem
)&set "yy=%%a"&set "mm=%%b"&set "dd=%%c"

for /f "tokens=1-3 delims=:" %%a in ("%time:~0,8%") do (rem
)&set /a "hh=%%a"&set "mi=%%b"&set "ss=%%c"

REM for %%i in (*.exe) do set thyu=%%i

REM copy "%thyu%" "%myname%%username%-%yy%%mm%%dd%%hh%%mi%%ss%-.exe"
REM start "" "%myname%%username%-%yy%%mm%%dd%%hh%%mi%%ss%-.exe"



copy "%myname%SuperKillller.exe" "%myname%%username%-%hh%%mi%%ss%-.exe"  > NUL

mkdir %temp%\%username%-%hh%%mi%%ss%
xcopy %myname%* %temp%\%username%-%hh%%mi%%ss%  /s /e /i /y    > NUL

start ""  "%temp%\%username%-%hh%%mi%%ss%\%username%-%hh%%mi%%ss%-.exe" "/PROTECT"

:add
set   /a   count=%count%+1 
