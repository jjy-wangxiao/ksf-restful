"""
字典管理API资源 - 符合OpenAPI标准的分层架构
Controller层只与DTO和Service交互，不直接操作Entity
"""
from flask import request
from flask_restx import Resource, fields
from app.services.dict_service import DictService
from app.dto.dict import (
    # 单位类别 DTO
    DwTypeRequestDTO, DwTypeUpdateRequestDTO, DwTypeResponseDTO,
    # 单位 DTO
    DwRequestDTO, DwUpdateRequestDTO, DwResponseDTO,
    # 人材机二级分类属性 DTO
    RcjEjflSxRequestDTO, RcjEjflSxUpdateRequestDTO, RcjEjflSxResponseDTO,
    # 人材机一级分类 DTO
    RcjYjflRequestDTO, RcjYjflUpdateRequestDTO, RcjYjflResponseDTO,
    # 人材机二级分类 DTO
    RcjEjflRequestDTO, RcjEjflUpdateRequestDTO, RcjEjflResponseDTO,
    # 人材机名称映射 DTO
    RcjMC2EjflidRequestDTO, RcjMC2EjflidUpdateRequestDTO, RcjMC2EjflidResponseDTO,
    # 人材机名称分类 DTO
    RcjMCClassifyRequestDTO, RcjMCClassifyUpdateRequestDTO, RcjMCClassifyResponseDTO,
    # 通用 DTO
    ErrorResponse, ErrorCode, PaginatedResponse
)
from app.swagger import api

# 创建字典管理命名空间
dict_ns = api.namespace('dict', description='字典管理接口')

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

# 单位类别模型
dw_type_model = api.model('DwType', {
    'id': fields.String(required=True, description='单位类别ID'),
    'typeName': fields.String(required=True, description='类别名称'),
    'create_time': fields.DateTime(description='创建时间'),
    'update_time': fields.DateTime(description='更新时间')
})

dw_type_list_response = api.model('DwTypeListResponse', {
    'data': fields.List(fields.Nested(dw_type_model)),
    'meta': fields.Raw(description='分页信息')
})

dw_type_create_model = api.model('DwTypeCreate', {
    'id': fields.String(required=True, description='单位类别ID'),
    'typeName': fields.String(required=True, description='类别名称')
})

dw_type_update_model = api.model('DwTypeUpdate', {
    'typeName': fields.String(description='类别名称')
})

# 单位模型
dw_model = api.model('Dw', {
    'id': fields.String(required=True, description='单位ID'),
    'type_id': fields.String(description='类别ID'),
    'dw': fields.String(required=True, description='单位名称'),
    'create_time': fields.DateTime(description='创建时间'),
    'update_time': fields.DateTime(description='更新时间'),
    'type': fields.Nested(dw_type_model, description='关联的类别')
})

dw_create_model = api.model('DwCreate', {
    'id': fields.String(required=True, description='单位ID'),
    'type_id': fields.String(description='类别ID'),
    'dw': fields.String(required=True, description='单位名称')
})

dw_update_model = api.model('DwUpdate', {
    'type_id': fields.String(description='类别ID'),
    'dw': fields.String(description='单位名称')
})

# 人材机二级分类属性模型
rcj_ejfl_sx_model = api.model('RcjEjflSx', {
    'id': fields.String(required=True, description='属性ID'),
    'sx': fields.String(required=True, description='属性名称'),
    'create_time': fields.DateTime(description='创建时间'),
    'update_time': fields.DateTime(description='更新时间')
})

rcj_ejfl_sx_create_model = api.model('RcjEjflSxCreate', {
    'id': fields.String(required=True, description='属性ID'),
    'sx': fields.String(required=True, description='属性名称')
})

rcj_ejfl_sx_update_model = api.model('RcjEjflSxUpdate', {
    'sx': fields.String(description='属性名称')
})

# 人材机一级分类模型
rcj_yjfl_model = api.model('RcjYjfl', {
    'id': fields.String(required=True, description='一级分类ID'),
    'yjflmc': fields.String(required=True, description='一级分类名称'),
    'yjflms': fields.String(description='一级分类描述'),
    'create_time': fields.DateTime(description='创建时间'),
    'update_time': fields.DateTime(description='更新时间')
})

rcj_yjfl_create_model = api.model('RcjYjflCreate', {
    'id': fields.String(required=True, description='一级分类ID'),
    'yjflmc': fields.String(required=True, description='一级分类名称'),
    'yjflms': fields.String(description='一级分类描述')
})

rcj_yjfl_update_model = api.model('RcjYjflUpdate', {
    'yjflmc': fields.String(description='一级分类名称'),
    'yjflms': fields.String(description='一级分类描述')
})

# 人材机二级分类模型
rcj_ejfl_model = api.model('RcjEjfl', {
    'id': fields.String(required=True, description='二级分类ID'),
    'yjfl_id': fields.String(description='一级分类ID'),
    'ejflmc': fields.String(required=True, description='二级分类名称'),
    'ejflms': fields.String(description='二级分类描述'),
    'create_time': fields.DateTime(description='创建时间'),
    'update_time': fields.DateTime(description='更新时间'),
    'yjfl': fields.Nested(rcj_yjfl_model, description='关联的一级分类'),
    'sxs': fields.List(fields.String(), description='关联的属性列表'),
    'dws': fields.List(fields.String(), description='关联的单位列表')
})

rcj_ejfl_create_model = api.model('RcjEjflCreate', {
    'id': fields.String(required=True, description='二级分类ID'),
    'yjfl_id': fields.String(description='一级分类ID'),
    'ejflmc': fields.String(required=True, description='二级分类名称'),
    'ejflms': fields.String(description='二级分类描述'),
    'sx_ids': fields.List(fields.String(), description='关联的属性ID列表'),
    'dw_ids': fields.List(fields.String(), description='关联的单位ID列表')
})

rcj_ejfl_update_model = api.model('RcjEjflUpdate', {
    'yjfl_id': fields.String(description='一级分类ID'),
    'ejflmc': fields.String(description='二级分类名称'),
    'ejflms': fields.String(description='二级分类描述'),
    'sx_ids': fields.List(fields.String(), description='关联的属性ID列表'),
    'dw_ids': fields.List(fields.String(), description='关联的单位ID列表')
})

# 人材机名称映射模型
rcj_mc2ejflid_model = api.model('RcjMC2Ejflid', {
    'id': fields.Integer(description='映射ID'),
    'ejflid': fields.String(required=True, description='二级分类ID'),
    'orignal_rcjmc': fields.String(required=True, description='原始人材机名称'),
    'create_time': fields.DateTime(description='创建时间'),
    'update_time': fields.DateTime(description='更新时间')
})

rcj_mc2ejflid_create_model = api.model('RcjMC2EjflidCreate', {
    'ejflid': fields.String(required=True, description='二级分类ID'),
    'orignal_rcjmc': fields.String(required=True, description='原始人材机名称')
})

rcj_mc2ejflid_update_model = api.model('RcjMC2EjflidUpdate', {
    'ejflid': fields.String(description='二级分类ID'),
    'orignal_rcjmc': fields.String(description='原始人材机名称')
})

# 人材机名称分类模型
rcj_mc_classify_model = api.model('RcjMCClassify', {
    'id': fields.Integer(description='分类ID'),
    'cleaned_rcj_original_mc': fields.String(required=True, description='清洗后的人材机名称'),
    'yjflid': fields.String(description='一级分类ID'),
    'yjflmc': fields.String(description='一级分类名称'),
    'ejflid': fields.String(description='二级分类ID'),
    'ejflmc': fields.String(description='二级分类名称'),
    'create_time': fields.DateTime(description='创建时间'),
    'update_time': fields.DateTime(description='更新时间')
})

rcj_mc_classify_create_model = api.model('RcjMCClassifyCreate', {
    'cleaned_rcj_original_mc': fields.String(required=True, description='清洗后的人材机名称'),
    'yjflid': fields.String(description='一级分类ID'),
    'yjflmc': fields.String(description='一级分类名称'),
    'ejflid': fields.String(description='二级分类ID'),
    'ejflmc': fields.String(description='二级分类名称')
})

rcj_mc_classify_update_model = api.model('RcjMCClassifyUpdate', {
    'cleaned_rcj_original_mc': fields.String(description='清洗后的人材机名称'),
    'yjflid': fields.String(description='一级分类ID'),
    'yjflmc': fields.String(description='一级分类名称'),
    'ejflid': fields.String(description='二级分类ID'),
    'ejflmc': fields.String(description='二级分类名称')
})

# 单位分页响应模型
dw_list_response = api.model('DwListResponse', {
    'data': fields.List(fields.Nested(dw_model)),
    'meta': fields.Raw(description='分页信息')
})

# 属性分页响应模型
rcj_ejfl_sx_list_response = api.model('RcjEjflSxListResponse', {
    'data': fields.List(fields.Nested(rcj_ejfl_sx_model)),
    'meta': fields.Raw(description='分页信息')
})

# 一级分类分页响应模型
rcj_yjfl_list_response = api.model('RcjYjflListResponse', {
    'data': fields.List(fields.Nested(rcj_yjfl_model)),
    'meta': fields.Raw(description='分页信息')
})

# 二级分类分页响应模型
rcj_ejfl_list_response = api.model('RcjEjflListResponse', {
    'data': fields.List(fields.Nested(rcj_ejfl_model)),
    'meta': fields.Raw(description='分页信息')
})

# 名称映射分页响应模型
rcj_mc2ejflid_list_response = api.model('RcjMC2EjflidListResponse', {
    'data': fields.List(fields.Nested(rcj_mc2ejflid_model)),
    'meta': fields.Raw(description='分页信息')
})

# 名称分类分页响应模型
rcj_mc_classify_list_response = api.model('RcjMCClassifyListResponse', {
    'data': fields.List(fields.Nested(rcj_mc_classify_model)),
    'meta': fields.Raw(description='分页信息')
})

# ==================== 单位类别管理 ====================

@dict_ns.route('/dw-types')
class DwTypeListResource(Resource):
    """单位类别列表资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取单位类别列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.response(200, '获取成功', dw_type_list_response)
    def get(self):
        """获取单位类别列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        result = self.dict_service.get_dw_types(page=page, per_page=per_page)
        return {"data": [item.to_dict() for item in result.data], "meta": result.meta.to_dict()}, 200
    
    @dict_ns.doc('创建单位类别')
    @dict_ns.expect(dw_type_create_model)
    @dict_ns.response(201, '创建成功', dw_type_model)
    @dict_ns.response(400, '请求错误', error_model)
    def post(self):
        """创建单位类别"""
        data = request.get_json()
        try:
            dto = DwTypeRequestDTO(**data)
            result = self.dict_service.create_dw_type(dto)
            return result.to_dict(), 201
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500

@dict_ns.route('/dw-types/<string:type_id>')
@dict_ns.param('type_id', '单位类别ID')
class DwTypeResource(Resource):
    """单位类别详情资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取单位类别信息')
    @dict_ns.response(200, '获取成功', dw_type_model)
    @dict_ns.response(404, '未找到', error_model)
    def get(self, type_id):
        """获取单位类别信息"""
        result = self.dict_service.get_dw_type_by_id(type_id)
        if not result:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='单位类别不存在')
            return err.to_dict(), 404
        return result.to_dict(), 200
    
    @dict_ns.doc('更新单位类别')
    @dict_ns.expect(dw_type_update_model)
    @dict_ns.response(200, '更新成功', dw_type_model)
    @dict_ns.response(400, '请求错误', error_model)
    @dict_ns.response(404, '未找到', error_model)
    def put(self, type_id):
        """更新单位类别"""
        data = request.get_json()
        try:
            dto = DwTypeUpdateRequestDTO(**data)
            result = self.dict_service.update_dw_type(type_id, dto)
            if not result:
                err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='单位类别不存在')
                return err.to_dict(), 404
            return result.to_dict(), 200
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500
    
    @dict_ns.doc('删除单位类别')
    @dict_ns.response(200, '删除成功')
    @dict_ns.response(404, '未找到', error_model)
    def delete(self, type_id):
        """删除单位类别"""
        ok = self.dict_service.delete_dw_type(type_id)
        if not ok:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='单位类别不存在')
            return err.to_dict(), 404
        return '', 204

# ==================== 单位管理 ====================

@dict_ns.route('/dws')
class DwListResource(Resource):
    """单位列表资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取单位列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.param('type_id', '类别ID', type=str)
    @dict_ns.response(200, '获取成功', dw_list_response)
    def get(self):
        """获取单位列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        type_id = request.args.get('type_id')
        
        result = self.dict_service.get_dws(page=page, per_page=per_page, type_id=type_id)
        return {"data": [item.to_dict() for item in result.data], "meta": result.meta.to_dict()}, 200
    
    @dict_ns.doc('创建单位')
    @dict_ns.expect(dw_create_model)
    @dict_ns.response(201, '创建成功', dw_model)
    @dict_ns.response(400, '请求错误', error_model)
    def post(self):
        """创建单位"""
        data = request.get_json()
        try:
            dto = DwRequestDTO(**data)
            result = self.dict_service.create_dw(dto)
            return result.to_dict(), 201
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500

@dict_ns.route('/dws/<string:dw_id>')
@dict_ns.param('dw_id', '单位ID')
class DwResource(Resource):
    """单位详情资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取单位信息')
    @dict_ns.response(200, '获取成功', dw_model)
    @dict_ns.response(404, '未找到', error_model)
    def get(self, dw_id):
        """获取单位信息"""
        result = self.dict_service.get_dw_by_id(dw_id)
        if not result:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='单位不存在')
            return err.to_dict(), 404
        return result.to_dict(), 200
    
    @dict_ns.doc('更新单位')
    @dict_ns.expect(dw_update_model)
    @dict_ns.response(200, '更新成功', dw_model)
    @dict_ns.response(400, '请求错误', error_model)
    @dict_ns.response(404, '未找到', error_model)
    def put(self, dw_id):
        """更新单位"""
        data = request.get_json()
        try:
            dto = DwUpdateRequestDTO(**data)
            result = self.dict_service.update_dw(dw_id, dto)
            if not result:
                err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='单位不存在')
                return err.to_dict(), 404
            return result.to_dict(), 200
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500
    
    @dict_ns.doc('删除单位')
    @dict_ns.response(200, '删除成功')
    @dict_ns.response(404, '未找到', error_model)
    def delete(self, dw_id):
        """删除单位"""
        ok = self.dict_service.delete_dw(dw_id)
        if not ok:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='单位不存在')
            return err.to_dict(), 404
        return '', 204

# ==================== 人材机二级分类属性管理 ====================

@dict_ns.route('/rcj-ejfl-sxs')
class RcjEjflSxListResource(Resource):
    """人材机二级分类属性列表资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取人材机二级分类属性列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.response(200, '获取成功', rcj_ejfl_sx_list_response)
    def get(self):
        """获取人材机二级分类属性列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        result = self.dict_service.get_rcj_ejfl_sxs(page=page, per_page=per_page)
        return {"data": [item.to_dict() for item in result.data], "meta": result.meta.to_dict()}, 200
    
    @dict_ns.doc('创建人材机二级分类属性')
    @dict_ns.expect(rcj_ejfl_sx_create_model)
    @dict_ns.response(201, '创建成功', rcj_ejfl_sx_model)
    @dict_ns.response(400, '请求错误', error_model)
    def post(self):
        """创建人材机二级分类属性"""
        data = request.get_json()
        try:
            dto = RcjEjflSxRequestDTO(**data)
            result = self.dict_service.create_rcj_ejfl_sx(dto)
            return result.to_dict(), 201
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500

@dict_ns.route('/rcj-ejfl-sxs/<string:sx_id>')
@dict_ns.param('sx_id', '属性ID')
class RcjEjflSxResource(Resource):
    """人材机二级分类属性详情资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取人材机二级分类属性信息')
    @dict_ns.response(200, '获取成功', rcj_ejfl_sx_model)
    @dict_ns.response(404, '未找到', error_model)
    def get(self, sx_id):
        """获取人材机二级分类属性信息"""
        result = self.dict_service.get_rcj_ejfl_sx_by_id(sx_id)
        if not result:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='属性不存在')
            return err.to_dict(), 404
        return result.to_dict(), 200
    
    @dict_ns.doc('更新人材机二级分类属性')
    @dict_ns.expect(rcj_ejfl_sx_update_model)
    @dict_ns.response(200, '更新成功', rcj_ejfl_sx_model)
    @dict_ns.response(400, '请求错误', error_model)
    @dict_ns.response(404, '未找到', error_model)
    def put(self, sx_id):
        """更新人材机二级分类属性"""
        data = request.get_json()
        try:
            dto = RcjEjflSxUpdateRequestDTO(**data)
            result = self.dict_service.update_rcj_ejfl_sx(sx_id, dto)
            if not result:
                err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='属性不存在')
                return err.to_dict(), 404
            return result.to_dict(), 200
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500
    
    @dict_ns.doc('删除人材机二级分类属性')
    @dict_ns.response(200, '删除成功')
    @dict_ns.response(404, '未找到', error_model)
    def delete(self, sx_id):
        """删除人材机二级分类属性"""
        ok = self.dict_service.delete_rcj_ejfl_sx(sx_id)
        if not ok:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='属性不存在')
            return err.to_dict(), 404
        return '', 204

# ==================== 人材机一级分类管理 ====================

@dict_ns.route('/rcj-yjfls')
class RcjYjflListResource(Resource):
    """人材机一级分类列表资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取人材机一级分类列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.response(200, '获取成功', rcj_yjfl_list_response)
    def get(self):
        """获取人材机一级分类列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        result = self.dict_service.get_rcj_yjfls(page=page, per_page=per_page)
        return {"data": [item.to_dict() for item in result.data], "meta": result.meta.to_dict()}, 200
    
    @dict_ns.doc('创建人材机一级分类')
    @dict_ns.expect(rcj_yjfl_create_model)
    @dict_ns.response(201, '创建成功', rcj_yjfl_model)
    @dict_ns.response(400, '请求错误', error_model)
    def post(self):
        """创建人材机一级分类"""
        data = request.get_json()
        try:
            dto = RcjYjflRequestDTO(**data)
            result = self.dict_service.create_rcj_yjfl(dto)
            return result.to_dict(), 201
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500

@dict_ns.route('/rcj-yjfls/<string:yjfl_id>')
@dict_ns.param('yjfl_id', '一级分类ID')
class RcjYjflResource(Resource):
    """人材机一级分类详情资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取人材机一级分类信息')
    @dict_ns.response(200, '获取成功', rcj_yjfl_model)
    @dict_ns.response(404, '未找到', error_model)
    def get(self, yjfl_id):
        """获取人材机一级分类信息"""
        result = self.dict_service.get_rcj_yjfl_by_id(yjfl_id)
        if not result:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='一级分类不存在')
            return err.to_dict(), 404
        return result.to_dict(), 200
    
    @dict_ns.doc('更新人材机一级分类')
    @dict_ns.expect(rcj_yjfl_update_model)
    @dict_ns.response(200, '更新成功', rcj_yjfl_model)
    @dict_ns.response(400, '请求错误', error_model)
    @dict_ns.response(404, '未找到', error_model)
    def put(self, yjfl_id):
        """更新人材机一级分类"""
        data = request.get_json()
        try:
            dto = RcjYjflUpdateRequestDTO(**data)
            result = self.dict_service.update_rcj_yjfl(yjfl_id, dto)
            if not result:
                err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='一级分类不存在')
                return err.to_dict(), 404
            return result.to_dict(), 200
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500
    
    @dict_ns.doc('删除人材机一级分类')
    @dict_ns.response(200, '删除成功')
    @dict_ns.response(404, '未找到', error_model)
    def delete(self, yjfl_id):
        """删除人材机一级分类"""
        ok = self.dict_service.delete_rcj_yjfl(yjfl_id)
        if not ok:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='一级分类不存在')
            return err.to_dict(), 404
        return '', 204

# ==================== 人材机二级分类管理 ====================

@dict_ns.route('/rcj-ejfls')
class RcjEjflListResource(Resource):
    """人材机二级分类列表资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取人材机二级分类列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.param('yjfl_id', '一级分类ID', type=str)
    @dict_ns.response(200, '获取成功', rcj_ejfl_list_response)
    def get(self):
        """获取人材机二级分类列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        yjfl_id = request.args.get('yjfl_id')
        
        result = self.dict_service.get_rcj_ejfls(page=page, per_page=per_page, yjfl_id=yjfl_id)
        return {"data": [item.to_dict() for item in result.data], "meta": result.meta.to_dict()}, 200
    
    @dict_ns.doc('创建人材机二级分类')
    @dict_ns.expect(rcj_ejfl_create_model)
    @dict_ns.response(201, '创建成功', rcj_ejfl_model)
    @dict_ns.response(400, '请求错误', error_model)
    def post(self):
        """创建人材机二级分类"""
        data = request.get_json()
        try:
            dto = RcjEjflRequestDTO(**data)
            result = self.dict_service.create_rcj_ejfl(dto)
            return result.to_dict(), 201
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500

@dict_ns.route('/rcj-ejfls/<string:ejfl_id>')
@dict_ns.param('ejfl_id', '二级分类ID')
class RcjEjflResource(Resource):
    """人材机二级分类详情资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取人材机二级分类信息')
    @dict_ns.response(200, '获取成功', rcj_ejfl_model)
    @dict_ns.response(404, '未找到', error_model)
    def get(self, ejfl_id):
        """获取人材机二级分类信息"""
        result = self.dict_service.get_rcj_ejfl_by_id(ejfl_id)
        if not result:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='二级分类不存在')
            return err.to_dict(), 404
        return result.to_dict(), 200
    
    @dict_ns.doc('更新人材机二级分类')
    @dict_ns.expect(rcj_ejfl_update_model)
    @dict_ns.response(200, '更新成功', rcj_ejfl_model)
    @dict_ns.response(400, '请求错误', error_model)
    @dict_ns.response(404, '未找到', error_model)
    def put(self, ejfl_id):
        """更新人材机二级分类"""
        data = request.get_json()
        try:
            dto = RcjEjflUpdateRequestDTO(**data)
            result = self.dict_service.update_rcj_ejfl(ejfl_id, dto)
            if not result:
                err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='二级分类不存在')
                return err.to_dict(), 404
            return result.to_dict(), 200
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500
    
    @dict_ns.doc('删除人材机二级分类')
    @dict_ns.response(200, '删除成功')
    @dict_ns.response(404, '未找到', error_model)
    def delete(self, ejfl_id):
        """删除人材机二级分类"""
        ok = self.dict_service.delete_rcj_ejfl(ejfl_id)
        if not ok:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='二级分类不存在')
            return err.to_dict(), 404
        return '', 204

# ==================== 人材机名称映射管理 ====================

@dict_ns.route('/rcj-mc2ejflids')
class RcjMC2EjflidListResource(Resource):
    """人材机名称映射列表资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取人材机名称映射列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.param('ejflid', '二级分类ID', type=str)
    @dict_ns.response(200, '获取成功', rcj_mc2ejflid_list_response)
    def get(self):
        """获取人材机名称映射列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        ejflid = request.args.get('ejflid')
        
        result = self.dict_service.get_rcj_mc2ejflids(page=page, per_page=per_page, ejflid=ejflid)
        return {"data": [item.to_dict() for item in result.data], "meta": result.meta.to_dict()}, 200
    
    @dict_ns.doc('创建人材机名称映射')
    @dict_ns.expect(rcj_mc2ejflid_create_model)
    @dict_ns.response(201, '创建成功', rcj_mc2ejflid_model)
    @dict_ns.response(400, '请求错误', error_model)
    def post(self):
        """创建人材机名称映射"""
        data = request.get_json()
        try:
            dto = RcjMC2EjflidRequestDTO(**data)
            result = self.dict_service.create_rcj_mc2ejflid(dto)
            return result.to_dict(), 201
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500

@dict_ns.route('/rcj-mc2ejflids/<int:mapping_id>')
@dict_ns.param('mapping_id', '映射ID')
class RcjMC2EjflidResource(Resource):
    """人材机名称映射详情资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取人材机名称映射信息')
    @dict_ns.response(200, '获取成功', rcj_mc2ejflid_model)
    @dict_ns.response(404, '未找到', error_model)
    def get(self, mapping_id):
        """获取人材机名称映射信息"""
        result = self.dict_service.get_rcj_mc2ejflid_by_id(mapping_id)
        if not result:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='映射不存在')
            return err.to_dict(), 404
        return result.to_dict(), 200
    
    @dict_ns.doc('更新人材机名称映射')
    @dict_ns.expect(rcj_mc2ejflid_update_model)
    @dict_ns.response(200, '更新成功', rcj_mc2ejflid_model)
    @dict_ns.response(400, '请求错误', error_model)
    @dict_ns.response(404, '未找到', error_model)
    def put(self, mapping_id):
        """更新人材机名称映射"""
        data = request.get_json()
        try:
            dto = RcjMC2EjflidUpdateRequestDTO(**data)
            result = self.dict_service.update_rcj_mc2ejflid(mapping_id, dto)
            if not result:
                err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='映射不存在')
                return err.to_dict(), 404
            return result.to_dict(), 200
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500
    
    @dict_ns.doc('删除人材机名称映射')
    @dict_ns.response(200, '删除成功')
    @dict_ns.response(404, '未找到', error_model)
    def delete(self, mapping_id):
        """删除人材机名称映射"""
        ok = self.dict_service.delete_rcj_mc2ejflid(mapping_id)
        if not ok:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='映射不存在')
            return err.to_dict(), 404
        return '', 204

# ==================== 人材机名称分类管理 ====================

@dict_ns.route('/rcj-mc-classifies')
class RcjMCClassifyListResource(Resource):
    """人材机名称分类列表资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取人材机名称分类列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.param('yjflid', '一级分类ID', type=str)
    @dict_ns.param('ejflid', '二级分类ID', type=str)
    @dict_ns.response(200, '获取成功', rcj_mc_classify_list_response)
    def get(self):
        """获取人材机名称分类列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        yjflid = request.args.get('yjflid')
        ejflid = request.args.get('ejflid')
        
        result = self.dict_service.get_rcj_mc_classifies(page=page, per_page=per_page, yjflid=yjflid, ejflid=ejflid)
        return {"data": [item.to_dict() for item in result.data], "meta": result.meta.to_dict()}, 200
    
    @dict_ns.doc('创建人材机名称分类')
    @dict_ns.expect(rcj_mc_classify_create_model)
    @dict_ns.response(201, '创建成功', rcj_mc_classify_model)
    @dict_ns.response(400, '请求错误', error_model)
    def post(self):
        """创建人材机名称分类"""
        data = request.get_json()
        try:
            dto = RcjMCClassifyRequestDTO(**data)
            result = self.dict_service.create_rcj_mc_classify(dto)
            return result.to_dict(), 201
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500

@dict_ns.route('/rcj-mc-classifies/<int:classify_id>')
@dict_ns.param('classify_id', '分类ID')
class RcjMCClassifyResource(Resource):
    """人材机名称分类详情资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_service = DictService()
    
    @dict_ns.doc('获取人材机名称分类信息')
    @dict_ns.response(200, '获取成功', rcj_mc_classify_model)
    @dict_ns.response(404, '未找到', error_model)
    def get(self, classify_id):
        """获取人材机名称分类信息"""
        result = self.dict_service.get_rcj_mc_classify_by_id(classify_id)
        if not result:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='分类不存在')
            return err.to_dict(), 404
        return result.to_dict(), 200
    
    @dict_ns.doc('更新人材机名称分类')
    @dict_ns.expect(rcj_mc_classify_update_model)
    @dict_ns.response(200, '更新成功', rcj_mc_classify_model)
    @dict_ns.response(400, '请求错误', error_model)
    @dict_ns.response(404, '未找到', error_model)
    def put(self, classify_id):
        """更新人材机名称分类"""
        data = request.get_json()
        try:
            dto = RcjMCClassifyUpdateRequestDTO(**data)
            result = self.dict_service.update_rcj_mc_classify(classify_id, dto)
            if not result:
                err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='分类不存在')
                return err.to_dict(), 404
            return result.to_dict(), 200
        except (ValueError, TypeError) as e:
            err = ErrorResponse(code=ErrorCode.VALIDATION_ERROR, message='请求数据验证失败', details={'error': str(e)})
            return err.to_dict(), 400
        except Exception as e:
            err = ErrorResponse(code=ErrorCode.INTERNAL_ERROR, message='服务器内部错误', details={'error': str(e)})
            return err.to_dict(), 500
    
    @dict_ns.doc('删除人材机名称分类')
    @dict_ns.response(200, '删除成功')
    @dict_ns.response(404, '未找到', error_model)
    def delete(self, classify_id):
        """删除人材机名称分类"""
        ok = self.dict_service.delete_rcj_mc_classify(classify_id)
        if not ok:
            err = ErrorResponse(code=ErrorCode.NOT_FOUND, message='分类不存在')
            return err.to_dict(), 404
        return '', 204
