"""
响应构建器 - 统一构建API响应
"""
from typing import List, Any, Optional
from app.dto.common import PaginatedResponse, PaginationMeta, ApiResponse, ErrorResponse
from datetime import datetime


class ResponseBuilder:
    """响应构建器"""
    
    @staticmethod
    def success(data: Any = None, message: str = "操作成功") -> ApiResponse:
        """构建成功响应"""
        return ApiResponse(
            success=True,
            data=data,
            message=message
        )
    
    @staticmethod
    def error(error_code: str, message: str, details: Optional[dict] = None) -> ErrorResponse:
        """构建错误响应"""
        return ErrorResponse(
            success=False,
            error_code=error_code,
            message=message,
            details=details or {}
        )
    
    @staticmethod
    def paginated(data: List[Any], page: int, per_page: int, total: int, 
                  pages: int, has_next: bool, has_prev: bool) -> PaginatedResponse:
        """构建分页响应"""
        meta = PaginationMeta(
            page=page,
            per_page=per_page,
            total=total,
            pages=pages,
            has_next=has_next,
            has_prev=has_prev
        )
        
        return PaginatedResponse(
            data=data,
            meta=meta
        )
    
    @staticmethod
    def from_pagination(pagination, data: List[Any]) -> PaginatedResponse:
        """从Flask-SQLAlchemy分页对象构建分页响应"""
        return ResponseBuilder.paginated(
            data=data,
            page=pagination.page,
            per_page=pagination.per_page,
            total=pagination.total,
            pages=pagination.pages,
            has_next=pagination.has_next,
            has_prev=pagination.has_prev
        ) 