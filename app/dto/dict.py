"""
字典管理相关的数据传输对象 (DTO)
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


# ==================== 单位类别 DTO ====================

@dataclass
class DwTypeRequestDTO:
    """单位类别请求DTO"""
    id: str
    typeName: str
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'typeName': self.typeName
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class DwTypeUpdateRequestDTO:
    """单位类别更新请求DTO"""
    typeName: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'typeName': self.typeName
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class DwTypeResponseDTO:
    """单位类别响应DTO"""
    id: str
    typeName: str
    create_time: datetime
    update_time: datetime
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'typeName': self.typeName,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None
        }
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()



@dataclass
class DwTypeInternalDTO:
    """单位类别内部DTO"""
    id: str
    typeName: str
    create_time: datetime
    update_time: datetime
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'typeName': self.typeName,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


# ==================== 单位 DTO ====================

@dataclass
class DwRequestDTO:
    """单位请求DTO"""
    id: str
    dw: str
    type_id: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'dw': self.dw,
            'type_id': self.type_id
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class DwUpdateRequestDTO:
    """单位更新请求DTO"""
    dw: Optional[str] = None
    type_id: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'dw': self.dw,
            'type_id': self.type_id
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class DwResponseDTO:
    """单位响应DTO"""
    id: str
    dw: str
    create_time: datetime
    update_time: datetime
    type_id: Optional[str] = None
    type: Optional[DwTypeResponseDTO] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'dw': self.dw,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None,
            'type_id': self.type_id,
            'type': self.type.to_dict() if self.type else None
        }
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()



@dataclass
class DwInternalDTO:
    """单位内部DTO"""
    id: str
    dw: str
    create_time: datetime
    update_time: datetime
    type_id: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'dw': self.dw,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None,
            'type_id': self.type_id
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


# ==================== 人材机二级分类属性 DTO ====================

@dataclass
class RcjEjflSxRequestDTO:
    """人材机二级分类属性请求DTO"""
    id: str
    sx: str
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'sx': self.sx
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class RcjEjflSxUpdateRequestDTO:
    """人材机二级分类属性更新请求DTO"""
    sx: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'sx': self.sx
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class RcjEjflSxResponseDTO:
    """人材机二级分类属性响应DTO"""
    id: str
    sx: str
    create_time: datetime
    update_time: datetime
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'sx': self.sx,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None
        }
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()



@dataclass
class RcjEjflSxInternalDTO:
    """人材机二级分类属性内部DTO"""
    id: str
    sx: str
    create_time: datetime
    update_time: datetime
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'sx': self.sx,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


# ==================== 人材机一级分类 DTO ====================

@dataclass
class RcjYjflRequestDTO:
    """人材机一级分类请求DTO"""
    id: str
    yjflmc: str
    yjflms: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'yjflmc': self.yjflmc,
            'yjflms': self.yjflms
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class RcjYjflUpdateRequestDTO:
    """人材机一级分类更新请求DTO"""
    yjflmc: Optional[str] = None
    yjflms: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'yjflmc': self.yjflmc,
            'yjflms': self.yjflms
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class RcjYjflResponseDTO:
    """人材机一级分类响应DTO"""
    id: str
    yjflmc: str
    create_time: datetime
    update_time: datetime
    yjflms: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'yjflmc': self.yjflmc,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None,
            'yjflms': self.yjflms
        }
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()



@dataclass
class RcjYjflInternalDTO:
    """人材机一级分类内部DTO"""
    id: str
    yjflmc: str
    create_time: datetime
    update_time: datetime
    yjflms: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'yjflmc': self.yjflmc,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None,
            'yjflms': self.yjflms
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


# ==================== 人材机二级分类 DTO ====================

@dataclass
class RcjEjflRequestDTO:
    """人材机二级分类请求DTO"""
    id: str
    ejflmc: str
    yjfl_id: Optional[str] = None
    ejflms: Optional[str] = None
    sx_ids: Optional[List[str]] = None
    dw_ids: Optional[List[str]] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'ejflmc': self.ejflmc,
            'yjfl_id': self.yjfl_id,
            'ejflms': self.ejflms,
            'sx_ids': self.sx_ids,
            'dw_ids': self.dw_ids
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class RcjEjflUpdateRequestDTO:
    """人材机二级分类更新请求DTO"""
    ejflmc: Optional[str] = None
    yjfl_id: Optional[str] = None
    ejflms: Optional[str] = None
    sx_ids: Optional[List[str]] = None
    dw_ids: Optional[List[str]] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'ejflmc': self.ejflmc,
            'yjfl_id': self.yjfl_id,
            'ejflms': self.ejflms,
            'sx_ids': self.sx_ids,
            'dw_ids': self.dw_ids
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class RcjEjflResponseDTO:
    """人材机二级分类响应DTO"""
    id: str
    ejflmc: str
    create_time: datetime
    update_time: datetime
    yjfl_id: Optional[str] = None
    ejflms: Optional[str] = None
    yjfl: Optional[RcjYjflResponseDTO] = None
    sxs: List[str] = None
    dws: List[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'ejflmc': self.ejflmc,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None,
            'yjfl_id': self.yjfl_id,
            'ejflms': self.ejflms,
            'yjfl': self.yjfl.to_dict() if self.yjfl else None,
            'sxs': self.sxs,
            'dws': self.dws
        }
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()



@dataclass
class RcjEjflInternalDTO:
    """人材机二级分类内部DTO"""
    id: str
    ejflmc: str
    create_time: datetime
    update_time: datetime
    yjfl_id: Optional[str] = None
    ejflms: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'ejflmc': self.ejflmc,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None,
            'yjfl_id': self.yjfl_id,
            'ejflms': self.ejflms
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


# ==================== 人材机名称映射 DTO ====================

@dataclass
class RcjMC2EjflidRequestDTO:
    """人材机名称映射请求DTO"""
    ejflid: str
    orignal_rcjmc: str
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'ejflid': self.ejflid,
            'orignal_rcjmc': self.orignal_rcjmc
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class RcjMC2EjflidUpdateRequestDTO:
    """人材机名称映射更新请求DTO"""
    orignal_rcjmc: Optional[str] = None
    ejflid: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'orignal_rcjmc': self.orignal_rcjmc,
            'ejflid': self.ejflid
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class RcjMC2EjflidResponseDTO:
    """人材机名称映射响应DTO"""
    id: int
    ejflid: str
    orignal_rcjmc: str
    create_time: datetime
    update_time: datetime
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'ejflid': self.ejflid,
            'orignal_rcjmc': self.orignal_rcjmc,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None
        }
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()



@dataclass
class RcjMC2EjflidInternalDTO:
    """人材机名称映射内部DTO"""
    id: int
    ejflid: str
    orignal_rcjmc: str
    create_time: datetime
    update_time: datetime
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'ejflid': self.ejflid,
            'orignal_rcjmc': self.orignal_rcjmc,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


# ==================== 人材机名称分类 DTO ====================

@dataclass
class RcjMCClassifyRequestDTO:
    """人材机名称分类请求DTO"""
    cleaned_rcj_original_mc: str
    yjflid: Optional[str] = None
    yjflmc: Optional[str] = None
    ejflid: Optional[str] = None
    ejflmc: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'cleaned_rcj_original_mc': self.cleaned_rcj_original_mc,
            'yjflid': self.yjflid,
            'yjflmc': self.yjflmc,
            'ejflid': self.ejflid,
            'ejflmc': self.ejflmc
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class RcjMCClassifyUpdateRequestDTO:
    """人材机名称分类更新请求DTO"""
    cleaned_rcj_original_mc: Optional[str] = None
    yjflid: Optional[str] = None
    yjflmc: Optional[str] = None
    ejflid: Optional[str] = None
    ejflmc: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'cleaned_rcj_original_mc': self.cleaned_rcj_original_mc,
            'yjflid': self.yjflid,
            'yjflmc': self.yjflmc,
            'ejflid': self.ejflid,
            'ejflmc': self.ejflmc
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class RcjMCClassifyResponseDTO:
    """人材机名称分类响应DTO"""
    id: int
    cleaned_rcj_original_mc: str
    create_time: datetime
    update_time: datetime
    yjflid: Optional[str] = None
    yjflmc: Optional[str] = None
    ejflid: Optional[str] = None
    ejflmc: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'cleaned_rcj_original_mc': self.cleaned_rcj_original_mc,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None,
            'yjflid': self.yjflid,
            'yjflmc': self.yjflmc,
            'ejflid': self.ejflid,
            'ejflmc': self.ejflmc
        }
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()



@dataclass
class RcjMCClassifyInternalDTO:
    """人材机名称分类内部DTO"""
    id: int
    cleaned_rcj_original_mc: str
    create_time: datetime
    update_time: datetime
    yjflid: Optional[str] = None
    yjflmc: Optional[str] = None
    ejflid: Optional[str] = None
    ejflmc: Optional[str] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'cleaned_rcj_original_mc': self.cleaned_rcj_original_mc,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None,
            'yjflid': self.yjflid,
            'yjflmc': self.yjflmc,
            'ejflid': self.ejflid,
            'ejflmc': self.ejflmc
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict() 