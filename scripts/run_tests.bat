@echo off
REM SWABox 测试运行脚本
REM 使用方法: run_tests.bat [test_type]
REM test_type: all, unit, integration, gui, network, coverage, fast

setlocal enabledelayedexpansion

REM 获取脚本所在目录的父目录（项目根目录）
set SCRIPT_DIR=%~dp0
set PROJECT_ROOT=%SCRIPT_DIR%..

if "%1"=="" (
    set TEST_TYPE=all
) else (
    set TEST_TYPE=%1
)

echo ========================================
echo SWABox 自动化测试
echo 测试类型: %TEST_TYPE%
echo ========================================

REM 设置pytest配置文件路径
set PYTEST_CONFIG=%PROJECT_ROOT%\config\pytest.ini

if "%TEST_TYPE%"=="all" (
    pytest -c %PYTEST_CONFIG% -v --tb=short --cov=lib --cov-report=html --cov-report=term-missing
) else if "%TEST_TYPE%"=="unit" (
    pytest -c %PYTEST_CONFIG% -v -m unit --tb=short
) else if "%TEST_TYPE%"=="integration" (
    pytest -c %PYTEST_CONFIG% -v -m integration --tb=short
) else if "%TEST_TYPE%"=="gui" (
    pytest -c %PYTEST_CONFIG% -v -m gui --tb=short
) else if "%TEST_TYPE%"=="network" (
    pytest -c %PYTEST_CONFIG% -v -m network --tb=short
) else if "%TEST_TYPE%"=="coverage" (
    pytest -c %PYTEST_CONFIG% -v --cov=lib --cov-report=html --cov-report=term-missing --cov-report=xml
    echo.
    echo 覆盖率报告已生成:
    echo - HTML: htmlcov\index.html
    echo - XML: coverage.xml
) else if "%TEST_TYPE%"=="fast" (
    pytest -c %PYTEST_CONFIG% -v -x --tb=short
) else (
    echo 未知的测试类型: %TEST_TYPE%
    echo 可用的测试类型: all, unit, integration, gui, network, coverage, fast
    exit /b 1
)

echo.
echo ========================================
echo 测试完成!
echo ========================================

if "%TEST_TYPE%"=="coverage" (
    echo.
    echo 正在打开覆盖率报告...
    start htmlcov\index.html
)

endlocal