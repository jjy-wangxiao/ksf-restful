"""
矩阵管理API资源 - 符合OpenAPI标准的分层架构
Controller层只与DTO和Service交互，不直接操作Entity
"""
from flask import request
from flask_restx import Resource, fields
from app.services.matrix_service import MatrixService
from app.services.dict_service import DictService
from app.dto.matrix_dto import (
    FileListQueryDTO,
    FileListResponseDTO,
    TreeResponseDTO,
    ErrorResponse,
    ErrorCode
)
from app.dto.dict import (
    DwTypeRequestDTO,
    DwTypeUpdateRequestDTO,
    DwTypeResponseDTO,
    DwRequestDTO,
    DwUpdateRequestDTO,
    DwResponseDTO,
    RcjEjflSxRequestDTO,
    RcjEjflSxUpdateRequestDTO,
    RcjEjflSxResponseDTO,
    RcjYjflRequestDTO,
    RcjYjflUpdateRequestDTO,
    RcjYjflResponseDTO,
    RcjEjflRequestDTO,
    RcjEjflUpdateRequestDTO,
    RcjEjflResponseDTO,
    RcjMC2EjflidRequestDTO,
    RcjMC2EjflidUpdateRequestDTO,
    RcjMC2EjflidResponseDTO,
    RcjMCClassifyRequestDTO,
    RcjMCClassifyUpdateRequestDTO,
    RcjMCClassifyResponseDTO
)
from app.swagger import api
from app.utils.decorators import paginated_response

# 创建字典管理命名空间
matrix_ns = api.namespace('matrix', description='矩阵管理接口')

# ==================== OpenAPI 模型定义 ====================

# 错误响应模型
error_model = api.model('Error', {
    'code': fields.String(required=True, description='错误码'),
    'message': fields.String(required=True, description='错误信息'),
    'details': fields.Raw(description='详细信息'),
    'timestamp': fields.DateTime(description='时间戳')
})

# 分页元数据模型
pagination_meta_model = api.model('PaginationMeta', {
    'page': fields.Integer(description='当前页码'),
    'per_page': fields.Integer(description='每页数量'),
    'total': fields.Integer(description='总记录数'),
    'pages': fields.Integer(description='总页数'),
    'has_next': fields.Boolean(description='是否有下一页'),
    'has_prev': fields.Boolean(description='是否有上一页')
})

# 通用分页响应模型
pagination_response_model = api.model('PaginatedResponse', {
    'data': fields.List(fields.Raw(), description='数据列表'),
    'meta': fields.Nested(pagination_meta_model, description='分页信息')
})

# M3文件选择模型
fileList_model = api.model('FileList', {
    'id': fields.String(required=True, description='ID'),
    'filename': fields.String(required=True, description='文件名'),
    'hashcode': fields.String(required=True, description='文件Hash')
})

# 文件列表分页响应模型
file_list_pagination_response = api.model('FileListPaginationResponse', {
    'data': fields.List(fields.Nested(fileList_model), description='文件列表信息'),
    'meta': fields.Nested(pagination_meta_model, description='分页信息')
})

# 树形结构节点模型 - 符合前端Ant Design Tree组件格式
tree_node_model = api.model('TreeNode', {
    'title': fields.String(required=True, description='节点标题'),
    'key': fields.String(required=True, description='节点唯一标识'),
    'children': fields.List(fields.Nested('self'), description='子节点列表')
})

# 树形结构响应模型
tree_response_model = api.model('TreeResponse', {
    'data': fields.List(fields.Nested(tree_node_model), description='树形结构数据')
})

@matrix_ns.route('/filelist')
class FileListResource(Resource):
    """文件列表资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matrix_service = MatrixService()
    
    @matrix_ns.doc('获取文件列表')
    @matrix_ns.param('page', '页码', type=int, default=1)
    @matrix_ns.param('per_page', '每页数量', type=int, default=10)
    @matrix_ns.response(200, '获取成功', file_list_pagination_response)
    @matrix_ns.response(400, '参数错误', error_model)
    @matrix_ns.response(500, '服务器错误', error_model)
    @paginated_response
    def get(self):
        """获取文件列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        result = self.matrix_service.get_file_list(page=page, per_page=per_page)
        return result, 200


@matrix_ns.route('/tree')
class TreeResource(Resource):
    """树形结构资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matrix_service = MatrixService()
    
    @matrix_ns.doc('获取树形结构')
    @matrix_ns.param('fileid', '文件ID', type=str, required=False)
    @matrix_ns.response(200, '获取成功', tree_response_model)
    @matrix_ns.response(400, '参数错误', error_model)
    @matrix_ns.response(404, '文件不存在', error_model)
    @matrix_ns.response(500, '服务器错误', error_model)
    def get(self):
        """获取树形结构"""
        try:
            # 获取查询参数
            fileid = request.args.get('fileid', None, type=str)
            
            # 参数验证
            if fileid is not None and not fileid.strip():
                return ErrorResponse(
                    code=ErrorCode.VALIDATION_ERROR,
                    message="文件ID不能为空字符串"
                ).to_dict(), 400
            
            # 调用服务层获取树形结构
            tree_data = self.matrix_service.get_tree(fileid=fileid)
            
            # 构建响应 - 直接返回树形结构数组，符合前端期望格式
            response_data = [node.to_dict() for node in tree_data]
            
            return response_data, 200
            
        except Exception as e:
            # 记录错误日志
            self.matrix_service.log_error(e, {"method": "get_tree", "fileid": fileid})
            
            # 返回错误响应
            return ErrorResponse(
                code=ErrorCode.INTERNAL_ERROR,
                message="获取树形结构失败",
                details={"error": str(e)}
            ).to_dict(), 500


@matrix_ns.route('/rcjclassify')
class RcjMCClassifyByEjflIdListResource(Resource):
    """人材机名称分类列表资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matrix_service = MatrixService()
        
    @matrix_ns.doc('获取人材机名称分类列表')
    @matrix_ns.param('fileid', '文件ID', type=str)
    @matrix_ns.param('ejflid', '二级分类ID', type=str)
    @matrix_ns.response(200, '获取成功')
    def get(self):
        """获取人材机名称分类列表"""
        fileid = request.args.get('fileid', None, type=str)
        ejflid = request.args.get('ejflid', None, type=str)
        result = self.matrix_service.get_rcj_mc_classifies_by_fileid(fileid, ejflid)
        return result, 200
    
@matrix_ns.route('/m3')
class M3Resource(Resource):
    """M3资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matrix_service = MatrixService()
        
    @matrix_ns.doc('获取M3')
    @matrix_ns.param('ejflid', '二级分类ID', type=str)
    @matrix_ns.response(200, '获取成功')
    def get(self):
        """获取M3"""
        ejflid = request.args.get('ejflid', None, type=str)
        result = self.matrix_service.get_m3(ejflid)
        return result, 200
    
@matrix_ns.route('/fileparser')
class FileParserResource(Resource):
    """文件解析资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matrix_service = MatrixService()
        
    @matrix_ns.doc('解析文件')
    @matrix_ns.param('fileid', '文件ID', type=str)
    @matrix_ns.response(200, '解析成功')
    def get(self):
        """解析文件"""
        fileid = request.args.get('fileid', None, type=str)
        result = self.matrix_service.parse_file(fileid)
        return result, 200