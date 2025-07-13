"""
中间件模块
提供请求日志记录、性能监控等功能
"""
import time
from typing import Dict, Any
from flask import request, g, Response
from app.utils.logger import get_logger, log_request_info, log_response_info


def setup_request_logging(app):
    """设置请求日志中间件"""
    
    @app.before_request
    def before_request():
        """请求前处理"""
        # 记录请求开始时间
        g.start_time = time.time()
        
        # 获取请求信息
        request_data = {
            'method': request.method,
            'url': request.url,
            'user_agent': request.headers.get('User-Agent'),
            'remote_addr': request.remote_addr,
            'content_type': request.content_type,
            'content_length': request.content_length,
            'query_string': dict(request.args),
            'headers': dict(request.headers)
        }
        
        # 记录请求信息
        logger = get_logger('app.api')
        log_request_info(logger, request_data)
        
        # 将请求ID添加到g对象中，用于关联日志
        g.request_id = f"{int(g.start_time * 1000)}"
    
    @app.after_request
    def after_request(response: Response):
        """请求后处理"""
        # 计算响应时间
        if hasattr(g, 'start_time'):
            response_time = time.time() - g.start_time
        else:
            response_time = 0
        
        # 获取响应信息
        response_data = {
            'status_code': response.status_code,
            'content_type': response.content_type,
            'content_length': response.content_length,
            'response_time': round(response_time * 1000, 2)  # 转换为毫秒
        }
        
        # 记录响应信息
        logger = get_logger('app.api')
        log_response_info(logger, response_data)
        
        # 添加响应时间到响应头
        response.headers['X-Response-Time'] = f"{response_time:.3f}s"
        
        return response
    
    @app.teardown_request
    def teardown_request(exception=None):
        """请求结束处理"""
        if exception:
            logger = get_logger('app.api')
            logger.error(
                "Request failed",
                exception=str(exception),
                exception_type=type(exception).__name__
            )


def setup_error_logging(app):
    """设置错误日志中间件"""
    
    @app.errorhandler(Exception)
    def handle_exception(e):
        """全局异常处理"""
        logger = get_logger('app.errors')
        logger.error(
            "Unhandled exception",
            exception=str(e),
            exception_type=type(e).__name__,
            url=request.url,
            method=request.method,
            remote_addr=request.remote_addr
        )
        
        # 重新抛出异常，让Flask的默认错误处理器处理
        raise e
    
    @app.errorhandler(404)
    def not_found_error(error):
        """404错误处理"""
        logger = get_logger('app.errors')
        logger.warning(
            "Page not found",
            url=request.url,
            method=request.method,
            remote_addr=request.remote_addr
        )
        return error
    
    @app.errorhandler(500)
    def internal_error(error):
        """500错误处理"""
        logger = get_logger('app.errors')
        logger.error(
            "Internal server error",
            url=request.url,
            method=request.method,
            remote_addr=request.remote_addr
        )
        return error


def setup_performance_monitoring(app):
    """设置性能监控中间件"""
    
    @app.before_request
    def before_request_performance():
        """请求前性能监控"""
        g.request_start_time = time.perf_counter()
    
    @app.after_request
    def after_request_performance(response: Response):
        """请求后性能监控"""
        if hasattr(g, 'request_start_time'):
            duration = time.perf_counter() - g.request_start_time
            
            # 记录慢请求
            if duration > 1.0:  # 超过1秒的请求
                logger = get_logger('app.performance')
                logger.warning(
                    "Slow request detected",
                    duration=round(duration, 3),
                    url=request.url,
                    method=request.method,
                    status_code=response.status_code
                )
            
            # 记录所有请求的性能数据
            logger = get_logger('app.performance')
            logger.debug(
                "Request performance",
                duration=round(duration, 3),
                url=request.url,
                method=request.method,
                status_code=response.status_code
            )
        
        return response 