"""
服务基类
提供通用的日志记录和错误处理功能
"""
from typing import Optional, Any, Dict
from app.utils.logger import LoggerMixin, log_database_operation, log_business_operation, log_error


class BaseService(LoggerMixin):
    """服务基类，提供通用的日志记录功能"""
    
    def __init__(self):
        """初始化服务"""
        self.logger.info(f"{self.__class__.__name__} service initialized")
    
    def log_database_operation(self, operation: str, table: str, record_id: Optional[str] = None, **kwargs):
        """记录数据库操作"""
        log_database_operation(self.logger, operation, table, record_id, **kwargs)
    
    def log_business_operation(self, operation: str, **kwargs):
        """记录业务操作"""
        log_business_operation(self.logger, operation, **kwargs)
    
    def log_error(self, error: Exception, context: Optional[Dict[str, Any]] = None):
        """记录错误信息"""
        log_error(self.logger, error, context)
    
    def log_service_call(self, method_name: str, **kwargs):
        """记录服务方法调用"""
        self.logger.debug(
            f"Service method called: {method_name}",
            method=method_name,
            **kwargs
        )
    
    def log_service_result(self, method_name: str, result: Any, **kwargs):
        """记录服务方法结果"""
        self.logger.debug(
            f"Service method completed: {method_name}",
            method=method_name,
            result_type=type(result).__name__,
            **kwargs
        )
    
    def log_validation_error(self, field: str, value: Any, message: str):
        """记录验证错误"""
        self.logger.warning(
            "Validation error",
            field=field,
            value=value,
            message=message
        )
    
    def log_not_found(self, entity_type: str, entity_id: str):
        """记录未找到实体"""
        self.logger.info(
            f"{entity_type} not found",
            entity_type=entity_type,
            entity_id=entity_id
        )
    
    def log_duplicate_error(self, entity_type: str, field: str, value: str):
        """记录重复错误"""
        self.logger.warning(
            f"{entity_type} already exists",
            entity_type=entity_type,
            field=field,
            value=value
        ) 