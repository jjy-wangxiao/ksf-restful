"""
通用DTO - 用于跨模块共享的数据传输对象
"""
from dataclasses import dataclass
from typing import List, Any, Generic, TypeVar
from datetime import datetime

T = TypeVar('T')


@dataclass
class PaginationMeta:
    """分页元数据DTO"""
    page: int
    per_page: int
    total: int
    pages: int
    has_next: bool
    has_prev: bool
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'page': self.page,
            'per_page': self.per_page,
            'total': self.total,
            'pages': self.pages,
            'has_next': self.has_next,
            'has_prev': self.has_prev
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class PaginatedResponse(Generic[T]):
    """通用分页响应DTO"""
    data: List[T]
    meta: PaginationMeta
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'data': [item.to_dict() if hasattr(item, 'to_dict') else item for item in self.data],
            'meta': self.meta.to_dict()
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class ApiResponse:
    """标准API响应DTO"""
    success: bool
    data: Any = None
    message: str = ""
    error_code: str = None
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'success': self.success,
            'data': self.data.to_dict() if hasattr(self.data, 'to_dict') else self.data,
            'message': self.message,
            'error_code': self.error_code,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class ErrorResponse:
    """标准错误响应DTO"""
    success: bool = False
    error_code: str = "UNKNOWN_ERROR"
    message: str = "未知错误"
    details: dict = None
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
        if self.details is None:
            self.details = {}
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'success': self.success,
            'error_code': self.error_code,
            'message': self.message,
            'details': self.details,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict() 