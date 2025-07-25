"""
矩阵相关的数据传输对象 (DTO)
遵循OpenAPI 3.0标准，明确分离Request、Response和Internal DTO
"""
import json
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
from typing import Optional, List, Dict, Any


def datetime_to_iso(obj):
    """将datetime对象转换为ISO格式字符串"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj


class ErrorCode(Enum):
    """错误码枚举，符合OpenAPI标准"""
    VALIDATION_ERROR = "VALIDATION_ERROR"
    NOT_FOUND = "NOT_FOUND"
    DUPLICATE_ENTRY = "DUPLICATE_ENTRY"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    
    def __str__(self):
        return self.value


@dataclass
class ErrorResponse:
    """标准错误响应DTO"""
    code: ErrorCode
    message: str
    details: Optional[Dict[str, Any]] = None
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'code': str(self.code),
            'message': self.message,
            'details': self.details,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


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
class PaginatedResponse:
    """分页响应DTO"""
    data: List[Any]
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


# ==================== uRcjItem DTO ====================

@dataclass
class FileListQueryDTO:
    """uRcjItem查询DTO - 用于接收查询参数"""
    fileid: Optional[str] = None
    filename: Optional[str] = None
    filehash: Optional[str] = None
    filestatus: Optional[str] = None

    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'original_rcj_mc': self.original_rcj_mc,
            'cleaned_rcj_mc': self.cleaned_rcj_mc,
            'yjflid': self.yjflid,
            'ejflid': self.ejflid,
            'sjjhflid': self.sjjhflid,
            'sjjhflzt': self.sjjhflzt,
            'dw': self.dw
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class FileListResponseDTO:
    """uRcjItem响应DTO"""
    id: str
    filename: str
    hashcode: str
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'filename': self.filename,
            'hashcode': self.hashcode
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()

@dataclass
class TreeResponseDTO:
    """树形结构响应DTO"""
    id: str
    filename: str
    hashcode: str
    