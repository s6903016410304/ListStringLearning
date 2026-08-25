@echo off
title Python List & String Learning

cd /d "%~dp0"

python main.py

if errorlevel 1 (
    echo.
    echo Python ไม่สามารถเปิดโปรแกรมได้
    echo กำลังลองใช้ py แทน...
    py main.py
)

pause