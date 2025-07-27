"""
矩阵服务层 - 处理矩阵相关的业务逻辑
"""
from typing import Optional, Dict, Any, List
from app.models.models_13jt import File, Rcjhzmx
from app.models.RcjMCClassifyBig import RcjMCClassifyBig
from app.models.dict import RcjYjfl, RcjEjfl
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

    def get_tree(self, fileid: Optional[str] = None) -> List[TreeResponseDTO]:
        """
        获取树形结构 - 基于人材机分类体系
        
        Args:
            fileid: 文件ID，如果提供则获取特定文件的树形结构，否则获取完整的分类树
            
        Returns:
            List[TreeResponseDTO]: 树形结构列表
        """
        self.log_service_call("get_tree", fileid=fileid)
        try:
            # 根据fileid决定构建哪种树形结构
            if fileid:
                # 获取特定文件的树形结构
                tree_data = self._build_file_classification_tree(fileid)
            else:
                # 获取完整的分类树形结构
                tree_data = self._build_classification_tree()
            
            self.log_service_result("get_tree", tree_data, fileid=fileid)
            return tree_data
            
        except Exception as e:
            self.log_error(e, {"method": "get_tree", "fileid": fileid})
            raise
    
    def _build_file_classification_tree(self, fileid: str) -> List[TreeResponseDTO]:
        """
        构建特定文件的分类树形结构
        
        Args:
            fileid: 文件ID
            
        Returns:
            List[TreeResponseDTO]: 文件分类树形结构
        """
        try:
            # 1. 查询文件信息
            file = File.query.filter_by(id=fileid).first()
            if not file:
                self.log_not_found("File", fileid)
                return []
            
            # 2. 查询该文件关联的所有rcjhzmx
            rcjhzmx_list = Rcjhzmx.query.filter_by(file_id=fileid).all()
            if not rcjhzmx_list:
                self.logger.info("No rcjhzmx found for file", fileid=fileid)
                return []
            
            # 3. 收集所有二级分类信息
            ejfl_set = set()  # 使用集合去重
            ejfl_info = {}    # 存储二级分类的详细信息
            
            for rcjhzmx in rcjhzmx_list:
                # 通过classify_info关系获取RcjMCClassifyBig
                for classify_big in rcjhzmx.classify_info:
                    if classify_big.ejflid and classify_big.ejflmc:
                        ejfl_key = f"{classify_big.ejflid}_{classify_big.ejflmc}"
                        if ejfl_key not in ejfl_set:
                            ejfl_set.add(ejfl_key)
                            ejfl_info[ejfl_key] = {
                                'ejflid': classify_big.ejflid,
                                'ejflmc': classify_big.ejflmc,
                                'yjflid': classify_big.yjflid,
                                'yjflmc': classify_big.yjflmc
                            }
            
            # 4. 按一级分类分组构建树形结构
            yjfl_groups = {}
            for ejfl_key, info in ejfl_info.items():
                yjfl_key = f"{info['yjflid']}_{info['yjflmc']}"
                if yjfl_key not in yjfl_groups:
                    yjfl_groups[yjfl_key] = {
                        'yjflid': info['yjflid'],
                        'yjflmc': info['yjflmc'],
                        'ejfls': []
                    }
                yjfl_groups[yjfl_key]['ejfls'].append({
                    'ejflid': info['ejflid'],
                    'ejflmc': info['ejflmc']
                })
            
            # 5. 构建树形结构
            tree_data = []
            for yjfl_key, yjfl_data in yjfl_groups.items():
                # 构建二级分类节点，按ejflid排序
                ejfl_children = []
                sorted_ejfls = sorted(yjfl_data['ejfls'], key=lambda x: x['ejflid'])
                for ejfl in sorted_ejfls:
                    ejfl_children.append(
                        TreeResponseDTO(
                            title=f"{ejfl['ejflid']}-{ejfl['ejflmc']}",
                            key=f"ejfl-{ejfl['ejflid']}",
                            children=[]
                        )
                    )
                
                # 构建一级分类节点
                yjfl_node = TreeResponseDTO(
                    title=f"{yjfl_data['yjflid']}-{yjfl_data['yjflmc']}",
                    key=f"yjfl-{yjfl_data['yjflid']}",
                    children=ejfl_children
                )
                
                tree_data.append(yjfl_node)
            
            # 按一级分类ID排序
            tree_data.sort(key=lambda x: x.key.split('-')[1])
            
            return tree_data
            
        except Exception as e:
            self.log_error(e, {"method": "_build_file_classification_tree", "fileid": fileid})
            return []
    
    def _build_classification_tree(self) -> List[TreeResponseDTO]:
        """
        构建完整的分类树形结构 - 基于RcjYjfl和RcjEjfl
        
        Returns:
            List[TreeResponseDTO]: 分类树形结构
        """
        try:
            # 查询所有一级分类，按ID排序
            yjfls = RcjYjfl.query.order_by(RcjYjfl.id).all()
            
            tree_data = []
            for yjfl in yjfls:
                # 查询该一级分类下的所有二级分类，按ID排序
                ejfls = RcjEjfl.query.filter_by(yjfl_id=yjfl.id).order_by(RcjEjfl.id).all()
                
                # 构建二级分类节点
                ejfl_children = []
                for ejfl in ejfls:
                    ejfl_children.append(
                        TreeResponseDTO(
                            title=ejfl.ejflmc or f"二级分类{ejfl.id}",
                            key=f"ejfl-{ejfl.id}",
                            children=[]  # 可以在这里添加更深层的分类
                        )
                    )
                
                # 构建一级分类节点
                yjfl_node = TreeResponseDTO(
                    title=yjfl.yjflmc or f"一级分类{yjfl.id}",
                    key=f"yjfl-{yjfl.id}",
                    children=ejfl_children
                )
                
                tree_data.append(yjfl_node)
            
            return tree_data
            
        except Exception as e:
            self.log_error(e, {"method": "_build_classification_tree"})
            # 返回空列表而不是抛出异常，确保API不会崩溃
            return []