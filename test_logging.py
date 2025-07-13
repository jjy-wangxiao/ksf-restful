#!/usr/bin/env python3
"""
测试日志系统功能
"""
import os
import sys
import time
from datetime import datetime

# 设置环境变量
os.environ['LOG_LEVEL'] = 'DEBUG'
os.environ['LOG_FORMAT'] = 'text'
os.environ['LOG_ENABLE_FILE'] = 'false'

# 导入日志模块
from app.utils.logger import (
    setup_logging, 
    get_logger, 
    LoggerMixin,
    log_request_info,
    log_response_info,
    log_error,
    log_database_operation,
    log_business_operation
)

def test_basic_logging():
    """测试基本日志功能"""
    print("=== 测试基本日志功能 ===")
    
    # 设置日志
    setup_logging(log_level='DEBUG', log_format='text', enable_file=False)
    
    # 获取日志记录器
    logger = get_logger('test.basic')
    
    # 记录不同级别的日志
    logger.debug("这是一条调试日志", debug_info="调试信息")
    logger.info("这是一条信息日志", user_id=123, action="login")
    logger.warning("这是一条警告日志", warning_type="rate_limit")
    logger.error("这是一条错误日志", error_code=500, error_msg="服务器错误")
    
    print("基本日志功能测试完成\n")

def test_logger_mixin():
    """测试LoggerMixin"""
    print("=== 测试LoggerMixin ===")
    
    class TestService(LoggerMixin):
        def test_method(self):
            self.logger.info("使用LoggerMixin记录日志", method="test_method")
            # 直接使用日志函数
            log_database_operation(self.logger, "READ", "User", "123")
            log_business_operation(self.logger, "User Login", user_id=123)
    
    service = TestService()
    service.test_method()
    print("LoggerMixin测试完成\n")

def test_request_logging():
    """测试请求日志"""
    print("=== 测试请求日志 ===")
    
    logger = get_logger('test.request')
    
    # 模拟请求数据
    request_data = {
        'method': 'POST',
        'url': '/api/v1/dict/dw-types',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'remote_addr': '192.168.1.100',
        'content_type': 'application/json',
        'content_length': 1024
    }
    
    response_data = {
        'status_code': 201,
        'content_type': 'application/json',
        'content_length': 512,
        'response_time': 150.5
    }
    
    log_request_info(logger, request_data)
    log_response_info(logger, response_data)
    print("请求日志测试完成\n")

def test_error_logging():
    """测试错误日志"""
    print("=== 测试错误日志 ===")
    
    logger = get_logger('test.error')
    
    try:
        # 模拟一个错误
        raise ValueError("这是一个测试错误")
    except Exception as e:
        log_error(logger, e, {"context": "test_error_logging", "user_id": 123})
    
    print("错误日志测试完成\n")

def test_database_logging():
    """测试数据库操作日志"""
    print("=== 测试数据库操作日志 ===")
    
    logger = get_logger('test.database')
    
    # 模拟数据库操作
    log_database_operation(logger, "CREATE", "User", "user_123", email="test@example.com")
    log_database_operation(logger, "READ", "User", "user_123")
    log_database_operation(logger, "UPDATE", "User", "user_123", field="email")
    log_database_operation(logger, "DELETE", "User", "user_123")
    
    print("数据库操作日志测试完成\n")

def test_business_logging():
    """测试业务操作日志"""
    print("=== 测试业务操作日志 ===")
    
    logger = get_logger('test.business')
    
    # 模拟业务操作
    log_business_operation(logger, "用户注册", user_id=123, email="new@example.com")
    log_business_operation(logger, "用户登录", user_id=123, ip="192.168.1.100")
    log_business_operation(logger, "数据导出", user_id=123, export_type="csv")
    
    print("业务操作日志测试完成\n")

def test_performance_logging():
    """测试性能日志"""
    print("=== 测试性能日志 ===")
    
    logger = get_logger('test.performance')
    
    # 模拟性能监控
    start_time = time.time()
    time.sleep(0.1)  # 模拟快速操作
    duration = time.time() - start_time
    
    logger.debug("快速操作完成", duration=round(duration * 1000, 2))
    
    # 模拟慢操作
    start_time = time.time()
    time.sleep(1.2)  # 模拟慢操作
    duration = time.time() - start_time
    
    logger.warning("慢操作检测", duration=round(duration * 1000, 2), threshold=1000)
    
    print("性能日志测试完成\n")

def test_json_logging():
    """测试JSON格式日志"""
    print("=== 测试JSON格式日志 ===")
    
    # 切换到JSON格式
    setup_logging(log_level='INFO', log_format='json', enable_file=False)
    
    logger = get_logger('test.json')
    
    logger.info("JSON格式日志测试", 
                user_id=123, 
                action="test", 
                timestamp=datetime.now().isoformat(),
                metadata={"version": "1.0", "environment": "test"})
    
    print("JSON格式日志测试完成\n")

def main():
    """主测试函数"""
    print("开始测试日志系统...\n")
    
    try:
        test_basic_logging()
        test_logger_mixin()
        test_request_logging()
        test_error_logging()
        test_database_logging()
        test_business_logging()
        test_performance_logging()
        test_json_logging()
        
        print("所有测试完成！")
        print("\n日志系统功能验证：")
        print("✓ 基本日志记录")
        print("✓ LoggerMixin混入类")
        print("✓ 请求/响应日志")
        print("✓ 错误日志记录")
        print("✓ 数据库操作日志")
        print("✓ 业务操作日志")
        print("✓ 性能监控日志")
        print("✓ JSON格式日志")
        
    except Exception as e:
        print(f"测试过程中出现错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 