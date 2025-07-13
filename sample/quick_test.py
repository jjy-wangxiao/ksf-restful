#!/usr/bin/env python3
"""
KSF RESTful API 快速测试脚本
快速验证API基本功能，不进行完整的CRUD测试
"""

import requests
import json
import sys
from datetime import datetime

def log(message: str, level: str = "INFO"):
    """日志输出"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def quick_test(base_url: str = "http://127.0.0.1:5678"):
    """快速测试API基本功能"""
    log("🚀 开始KSF RESTful API快速测试")
    log(f"测试目标: {base_url}")
    
    api_prefix = "/api/v1"
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    })
    
    tests_passed = 0
    tests_failed = 0
    
    # 测试列表
    test_cases = [
        {
            "name": "Swagger文档访问",
            "method": "GET",
            "endpoint": "/docs",
            "expected_status": 200
        },
        {
            "name": "单位类别列表",
            "method": "GET", 
            "endpoint": "/dict/dw-types",
            "expected_status": 200,
            "params": {"page": 1, "per_page": 5}
        },
        {
            "name": "单位列表",
            "method": "GET",
            "endpoint": "/dict/dws", 
            "expected_status": 200,
            "params": {"page": 1, "per_page": 5}
        },
        {
            "name": "人材机一级分类列表",
            "method": "GET",
            "endpoint": "/dict/rcj-yjfls",
            "expected_status": 200,
            "params": {"page": 1, "per_page": 5}
        },
        {
            "name": "人材机二级分类列表", 
            "method": "GET",
            "endpoint": "/dict/rcj-ejfls",
            "expected_status": 200,
            "params": {"page": 1, "per_page": 5}
        },
        {
            "name": "404错误处理",
            "method": "GET",
            "endpoint": "/dict/nonexistent",
            "expected_status": 404
        }
    ]
    
    # 运行测试
    for test in test_cases:
        log(f"测试: {test['name']}")
        
        try:
            url = f"{base_url}{api_prefix}{test['endpoint']}"
            params = test.get('params', {})
            
            response = session.request(
                method=test['method'],
                url=url,
                params=params,
                timeout=10
            )
            
            if response.status_code == test['expected_status']:
                log(f"✅ {test['name']} 通过")
                tests_passed += 1
            else:
                log(f"❌ {test['name']} 失败 - 期望状态码 {test['expected_status']}, 实际 {response.status_code}")
                tests_failed += 1
                
        except requests.exceptions.RequestException as e:
            log(f"❌ {test['name']} 异常: {str(e)}", "ERROR")
            tests_failed += 1
    
    # 输出结果
    log("=" * 50)
    log("📊 快速测试结果")
    log(f"通过: {tests_passed}")
    log(f"失败: {tests_failed}")
    log(f"总计: {tests_passed + tests_failed}")
    
    if tests_failed == 0:
        log("🎉 所有快速测试通过！API基本功能正常")
        return True
    else:
        log("⚠️ 部分测试失败，请检查API配置")
        return False

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='KSF RESTful API 快速测试')
    parser.add_argument('--url', default='http://127.0.0.1:5678',
                       help='API服务器地址 (默认: http://127.0.0.1:5678)')
    
    args = parser.parse_args()
    
    success = quick_test(args.url)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 