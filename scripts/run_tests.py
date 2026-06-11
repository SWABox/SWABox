#!/usr/bin/env python
"""
运行所有测试的脚本
"""
import subprocess
import sys
import os

def run_tests(test_type="all"):
    """
    运行测试
    
    Args:
        test_type: 测试类型 (all, unit, integration, gui, network)
    """
    # 获取项目根目录（scripts目录的父目录）
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)
    
    # 设置pytest配置文件路径
    pytest_config = os.path.join(project_root, "config", "pytest.ini")
    
    test_commands = {
        "all": ["pytest", "-c", pytest_config, "-v", "--tb=short", "--cov=lib", "--cov-report=html", "--cov-report=term-missing"],
        "unit": ["pytest", "-c", pytest_config, "-v", "-m", "unit", "--tb=short"],
        "integration": ["pytest", "-c", pytest_config, "-v", "-m", "integration", "--tb=short"],
        "gui": ["pytest", "-c", pytest_config, "-v", "-m", "gui", "--tb=short"],
        "network": ["pytest", "-c", pytest_config, "-v", "-m", "network", "--tb=short"],
        "coverage": ["pytest", "-c", pytest_config, "-v", "--cov=lib", "--cov-report=html", "--cov-report=term-missing", "--cov-report=xml"],
        "fast": ["pytest", "-c", pytest_config, "-v", "-x", "--tb=short"]
    }
    
    if test_type not in test_commands:
        print(f"未知的测试类型: {test_type}")
        print(f"可用的测试类型: {', '.join(test_commands.keys())}")
        sys.exit(1)
    
    cmd = test_commands[test_type]
    print(f"运行测试命令: {' '.join(cmd)}")
    print("-" * 80)
    
    try:
        result = subprocess.run(cmd, check=True)
        print("-" * 80)
        print("测试完成!")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print("-" * 80)
        print(f"测试失败，返回码: {e.returncode}")
        return e.returncode

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_type = sys.argv[1]
    else:
        test_type = "all"
    
    sys.exit(run_tests(test_type))