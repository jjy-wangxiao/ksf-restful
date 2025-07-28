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
            
            # 3. 收集所有classify_info并去重
            classify_info_set = set()  # 用于去重的集合
            ejfl_count = {}  # 二级分类计数: {ejflid: count}
            yjfl_count = {}  # 一级分类计数: {yjflid: count}
            ejfl_info = {}   # 二级分类信息: {ejflid: {ejflmc, yjflid, yjflmc}}
            yjfl_info = {}   # 一级分类信息: {yjflid: {yjflmc}}
            
            for rcjhzmx in rcjhzmx_list:
                # 通过classify_info关系获取RcjMCClassifyBig
                for classify_big in rcjhzmx.classify_info:
                    if classify_big.ejflid and classify_big.ejflmc:
                        # 使用classify_info.id进行去重
                        if classify_big.id not in classify_info_set:
                            classify_info_set.add(classify_big.id)
                            
                            # 统计二级分类
                            if classify_big.ejflid not in ejfl_count:
                                ejfl_count[classify_big.ejflid] = 0
                                ejfl_info[classify_big.ejflid] = {
                                    'ejflmc': classify_big.ejflmc,
                                    'yjflid': classify_big.yjflid,
                                    'yjflmc': classify_big.yjflmc
                                }
                            ejfl_count[classify_big.ejflid] += 1
                            
                            # 统计一级分类
                            if classify_big.yjflid not in yjfl_count:
                                yjfl_count[classify_big.yjflid] = 0
                                yjfl_info[classify_big.yjflid] = {
                                    'yjflmc': classify_big.yjflmc
                                }
                            yjfl_count[classify_big.yjflid] += 1
            
            # 4. 按一级分类分组构建树形结构
            yjfl_groups = {}
            for ejflid, count in ejfl_count.items():
                info = ejfl_info[ejflid]
                yjflid = info['yjflid']
                
                if yjflid not in yjfl_groups:
                    yjfl_groups[yjflid] = {
                        'yjflmc': yjfl_info[yjflid]['yjflmc'],
                        'ejfls': []
                    }
                
                yjfl_groups[yjflid]['ejfls'].append({
                    'ejflid': ejflid,
                    'ejflmc': info['ejflmc'],
                    'count': count
                })
            
            # 5. 构建树形结构
            tree_data = []
            for yjflid, yjfl_data in yjfl_groups.items():
                # 构建二级分类节点，按ejflid排序
                ejfl_children = []
                sorted_ejfls = sorted(yjfl_data['ejfls'], key=lambda x: x['ejflid'])
                for ejfl in sorted_ejfls:
                    ejfl_children.append(
                        TreeResponseDTO(
                            title=f"{ejfl['ejflid']}-{ejfl['ejflmc']} ({ejfl['count']})",
                            key=f"ejfl-{ejfl['ejflid']}",
                            children=[],
                            count=ejfl['count']
                        )
                    )
                
                # 统计该一级分类下的总数量（该一级分类下所有classify_info的总数）
                yjfl_total_count = yjfl_count[yjflid]
                
                # 构建一级分类节点
                yjfl_node = TreeResponseDTO(
                    title=f"{yjflid}-{yjfl_data['yjflmc']} ({yjfl_total_count})",
                    key=f"yjfl-{yjflid}",
                    children=ejfl_children,
                    count=yjfl_total_count
                )
                
                tree_data.append(yjfl_node)
            
            # 按一级分类ID排序
            tree_data.sort(key=lambda x: x.key.split('-')[1])
            
            # 计算总数量（所有classify_info的总数）
            total_count = sum(yjfl_count.values())
            
            # 获取文件名
            file_obj = File.query.get(fileid)
            filename = file_obj.filename if file_obj else f"文件{fileid}"
            
            # 创建根节点
            root_node = TreeResponseDTO(
                title=f"{filename} ({total_count})",
                key=f"file-{fileid}",
                children=tree_data,
                count=total_count
            )
            
            return [root_node]
            
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
                    # 统计该二级分类的数量（即该二级分类本身的数量）
                    ejfl_count = 1  # 每个二级分类本身算1个
                    
                    ejfl_children.append(
                        TreeResponseDTO(
                            title=f"{ejfl.ejflmc or f'二级分类{ejfl.id}'} ({ejfl_count})",
                            key=f"ejfl-{ejfl.id}",
                            children=[],  # 可以在这里添加更深层的分类
                            count=ejfl_count
                        )
                    )
                
                # 统计该一级分类下的总数量（即该一级分类下有多少个二级分类）
                yjfl_total_count = len(ejfl_children)
                
                # 构建一级分类节点
                yjfl_node = TreeResponseDTO(
                    title=f"{yjfl.yjflmc or f'一级分类{yjfl.id}'} ({yjfl_total_count})",
                    key=f"yjfl-{yjfl.id}",
                    children=ejfl_children,
                    count=yjfl_total_count
                )
                
                tree_data.append(yjfl_node)
            
            # 计算总数量（所有一级分类的数量之和）
            total_count = sum(node.count for node in tree_data)
            
            # 创建根节点
            root_node = TreeResponseDTO(
                title=f"完整分类树 ({total_count})",
                key="root-complete",
                children=tree_data,
                count=total_count
            )
            
            return [root_node]
            
        except Exception as e:
            self.log_error(e, {"method": "_build_classification_tree"})
            # 返回空列表而不是抛出异常，确保API不会崩溃
            return []
        
    def get_rcj_mc_classifies_by_fileid(self, fileid: str, ejflid: str) -> List[any]:
        """
        根据文件ID、二级分类ID和一级分类ID获取人材机名称分类列表
        """
        try:
            rcjhzmx_list = Rcjhzmx.query.filter_by(file_id=fileid).all()
            sxs = RcjEjfl.query.filter_by(id=ejflid).first()._sxs

            if not rcjhzmx_list:
                self.logger.info("No rcjhzmx found for file", fileid=fileid)
                return []
            # 对所有classify_big去重后统计
            unique_classify_big_set = set()
            resp_list = []
            for rcjhzmx in rcjhzmx_list:
                classify_big_list = rcjhzmx.classify_info
                for classify_big in classify_big_list:
                    if classify_big.ejflid == ejflid:
                        if classify_big.id not in unique_classify_big_set:
                            unique_classify_big_set.add(classify_big.id)
                
                            resp_item = {}

                            resp_item['id'] = rcjhzmx.id
                            resp_item['original_rcjmc'] = rcjhzmx.mc
                            resp_item['dw'] = rcjhzmx.dw
                            resp_item['dj'] = rcjhzmx.dj
                            resp_item['bjsj'] = rcjhzmx.jingjibiao.toubiaoxx[0].bztime
                            resp_item['cleaned_rcjmc'] = classify_big.cleaned_rcjmc
                            resp_item['parsed_rcjmc'] = classify_big.parsed_rcjmc
                            
                            for sx in sxs:
                                # 动态获取属性值，例如sx_0001、sx_0002等
                                sx_attr = f'sx_{sx.id:0>4}'
                                resp_item[sx.id] = getattr(classify_big, sx_attr, None)
                            resp_list.append(resp_item)

            return resp_list
        except Exception as e:
            self.log_error(e, {"method": "get_rcj_mc_classifies_by_fileid", "fileid": fileid, "ejflid": ejflid})
            return []