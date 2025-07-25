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
    
    @matrix_ns.doc('树形结构资源')
    @matrix_ns.response(200, '获取成功', file_list_pagination_response)
    @paginated_response
    def get(self):
        """树形结构资源"""
        fileid = request.args.get('fileid', None, type=str)
        
        result = self.matrix_service.get_tree(fileid=fileid)
        return result, 200
