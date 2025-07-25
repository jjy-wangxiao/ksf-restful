"""
矩阵服务层 - 处理矩阵相关的业务逻辑
"""
from typing import Optional, Dict, Any
from app.models.models_13jt import File
from app.services.base_service import BaseService
from app.dto.common import PaginatedResponse, PaginationMeta

from app.dto.matrix_dto import (
    FileListQueryDTO,
    FileListResponseDTO,
    TreeResponseDTO
)
from app.utils.response_builder import ResponseBuilder


class MatrixService(BaseService):
    """矩阵服务类"""
    
    def __init__(self):
        super().__init__()
    
    def get_file_list(self, page: int = 1, per_page: int = 10) -> PaginatedResponse[FileListResponseDTO]:
        """
        获取文件列表
        
        Args:
            query_params: 查询参数字典，包含分页和过滤条件
            
        Returns:
            PaginatedResponse[FileListResponseDTO]: 分页响应
        """
        self.log_service_call("get_file_list",  page=page, per_page=per_page)
        try:
            pagination = File.query.paginate(
                page=page, per_page=per_page, error_out=False
            )
            
            # 转换为DTO
            file_list_dto = [
                    FileListResponseDTO(
                    id=file.id,
                    filename=file.filename,
                    hashcode=file.hash
                )
                for file in pagination.items
            ]
            
            # 使用响应构建器创建分页响应
            result = ResponseBuilder.from_pagination(pagination, file_list_dto)
            self.log_service_result("get_file_list", result, total_count=pagination.total)
            return result
            
        except Exception as e:
            self.log_error(e, {"method": "get_dw_types", "page": page, "per_page": per_page})
            raise

    def get_tree(self, fileid: str) -> TreeResponseDTO:
        """
        获取树形结构
        """
        self.log_service_call("get_tree", fileid=fileid)