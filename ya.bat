@echo off
setlocal enabledelayedexpansion

REM 获取脚本的真实路径
set "SCRIPT_PATH=%~f0"
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

REM 检查是否提供了源文件参数
if "%~1"=="" (
    echo 雅语言解释器
    echo 用法: ya ^<源文件^>
    echo 示例: ya examples/hello_world.ya
    exit /b 1
)

REM 检查 Python 环境
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set "PYTHON_CMD=python"
) else (
    where python3 >nul 2>nul
    if %ERRORLEVEL% EQU 0 (
        set "PYTHON_CMD=python3"
    ) else (
        echo 错误: 未找到 Python 解释器
        exit /b 1
    )
)

REM 执行雅语言解释器
"%PYTHON_CMD%" "%SCRIPT_DIR%\src\main.py" "%~1" 