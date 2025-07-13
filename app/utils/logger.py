"""
日志配置模块
提供结构化和JSON格式的日志记录功能
"""
import os
import sys
import logging
import logging.config
from datetime import datetime
from typing import Dict, Any, Optional
from pathlib import Path

import structlog
from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """自定义JSON日志格式化器"""
    
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        
        # 添加时间戳
        if not log_record.get('timestamp'):
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        
        # 添加日志级别
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname
        
        # 添加模块信息
        if log_record.get('module'):
            log_record['module'] = log_record['module']
        else:
            log_record['module'] = record.module
        
        # 添加函数名
        if log_record.get('funcName'):
            log_record['function'] = log_record['funcName']
        else:
            log_record['function'] = record.funcName
        
        # 添加行号
        if log_record.get('lineno'):
            log_record['line'] = log_record['lineno']
        else:
            log_record['line'] = record.lineno


def setup_logging(
    log_level: str = "INFO",
    log_format: str = "json",
    log_file: Optional[str] = None,
    max_bytes: int = 10 * 1024 * 1024,  # 10MB
    backup_count: int = 5,
    enable_console: bool = True,
    enable_file: bool = True
) -> None:
    """
    设置日志配置
    
    Args:
        log_level: 日志级别 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_format: 日志格式 (json, text)
        log_file: 日志文件路径
        max_bytes: 单个日志文件最大大小
        backup_count: 保留的日志文件数量
        enable_console: 是否启用控制台输出
        enable_file: 是否启用文件输出
    """
    
    # 确保日志目录存在
    if log_file:
        log_dir = Path(log_file).parent
        log_dir.mkdir(parents=True, exist_ok=True)
    
    # 配置structlog
    processors = [
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer() if log_format == "json" else structlog.dev.ConsoleRenderer(),
    ]
    
    # 只在需要异常格式化时添加 format_exc_info
    if log_format == "json":
        # 在 JSON 格式中，我们使用 exc_info=True 来记录异常
        processors.insert(-2, structlog.processors.format_exc_info)
    
    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    
    # 创建日志配置字典
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': CustomJsonFormatter,
                'format': '%(timestamp)s %(level)s %(name)s %(module)s %(funcName)s %(lineno)d %(message)s'
            },
            'text': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(lineno)d - %(funcName)s - %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        'handlers': {},
        'loggers': {
            '': {  # root logger
                'level': log_level.upper(),
                'handlers': [],
                'propagate': True
            },
            'app': {
                'level': log_level.upper(),
                'handlers': [],
                'propagate': False
            },
            'app.services': {
                'level': log_level.upper(),
                'handlers': [],
                'propagate': False
            },
            'app.api': {
                'level': log_level.upper(),
                'handlers': [],
                'propagate': False
            },
            'app.models': {
                'level': log_level.upper(),
                'handlers': [],
                'propagate': False
            },
            'werkzeug': {
                'level': 'INFO',
                'handlers': [],
                'propagate': False
            },
            'sqlalchemy': {
                'level': 'WARNING',
                'handlers': [],
                'propagate': False
            },
            'gunicorn': {
                'level': 'INFO',
                'handlers': [],
                'propagate': False
            }
        }
    }
    
    # 添加控制台处理器
    if enable_console:
        console_handler = {
            'class': 'logging.StreamHandler',
            'level': log_level.upper(),
            'formatter': log_format,
            'stream': 'ext://sys.stdout'
        }
        log_config['handlers']['console'] = console_handler
        
        # 为所有logger添加控制台处理器
        for logger_name in log_config['loggers']:
            log_config['loggers'][logger_name]['handlers'].append('console')
    
    # 添加文件处理器
    if enable_file and log_file:
        file_handler = {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': log_level.upper(),
            'formatter': log_format,
            'filename': log_file,
            'maxBytes': max_bytes,
            'backupCount': backup_count,
            'encoding': 'utf8'
        }
        log_config['handlers']['file'] = file_handler
        
        # 为所有logger添加文件处理器
        for logger_name in log_config['loggers']:
            log_config['loggers'][logger_name]['handlers'].append('file')
    
    # 应用日志配置
    logging.config.dictConfig(log_config)


def get_logger(name: str) -> structlog.BoundLogger:
    """
    获取结构化日志记录器
    
    Args:
        name: 日志记录器名称
        
    Returns:
        结构化日志记录器实例
    """
    return structlog.get_logger(name)


class LoggerMixin:
    """日志记录器混入类，为类提供日志功能"""
    
    @property
    def logger(self) -> structlog.BoundLogger:
        """获取当前类的日志记录器"""
        return get_logger(f"{self.__class__.__module__}.{self.__class__.__name__}")


def log_request_info(logger: structlog.BoundLogger, request_data: Dict[str, Any]) -> None:
    """
    记录请求信息
    
    Args:
        logger: 日志记录器
        request_data: 请求数据字典
    """
    logger.info(
        "API Request",
        method=request_data.get('method'),
        url=request_data.get('url'),
        user_agent=request_data.get('user_agent'),
        remote_addr=request_data.get('remote_addr'),
        content_type=request_data.get('content_type'),
        content_length=request_data.get('content_length')
    )


def log_response_info(logger: structlog.BoundLogger, response_data: Dict[str, Any]) -> None:
    """
    记录响应信息
    
    Args:
        logger: 日志记录器
        response_data: 响应数据字典
    """
    logger.info(
        "API Response",
        status_code=response_data.get('status_code'),
        content_type=response_data.get('content_type'),
        content_length=response_data.get('content_length'),
        response_time=response_data.get('response_time')
    )


def log_error(logger: structlog.BoundLogger, error: Exception, context: Optional[Dict[str, Any]] = None) -> None:
    """
    记录错误信息
    
    Args:
        logger: 日志记录器
        error: 异常对象
        context: 上下文信息
    """
    error_data = {
        'error_type': type(error).__name__,
        'error_message': str(error),
        'error_module': getattr(error, '__module__', 'unknown'),
    }
    
    if context:
        error_data.update(context)
    
    logger.error("Application Error", **error_data, exc_info=True)


def log_database_operation(logger: structlog.BoundLogger, operation: str, table: str, record_id: Optional[str] = None, **kwargs) -> None:
    """
    记录数据库操作
    
    Args:
        logger: 日志记录器
        operation: 操作类型 (CREATE, READ, UPDATE, DELETE)
        table: 表名
        record_id: 记录ID
        **kwargs: 其他上下文信息
    """
    log_data = {
        'operation': operation,
        'table': table,
        'record_id': record_id
    }
    log_data.update(kwargs)
    
    logger.info("Database Operation", **log_data)


def log_business_operation(logger: structlog.BoundLogger, operation: str, **kwargs) -> None:
    """
    记录业务操作
    
    Args:
        logger: 日志记录器
        operation: 操作描述
        **kwargs: 上下文信息
    """
    log_data = {'operation': operation}
    log_data.update(kwargs)
    
    logger.info("Business Operation", **log_data) 