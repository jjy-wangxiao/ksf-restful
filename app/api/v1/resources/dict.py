from flask import request
from flask_restx import Resource, fields
from app import db
from app.models.dict import (
    DwType, Dw, RcjEjflSx, RcjYjfl, RcjEjfl, 
    RcjMC2Ejflid, RcjMCClassify
)
from app.schemas.dict import (
    DwTypeSchema, DwTypeCreateSchema, DwTypeUpdateSchema,
    DwSchema, DwCreateSchema, DwUpdateSchema,
    RcjEjflSxSchema, RcjEjflSxCreateSchema, RcjEjflSxUpdateSchema,
    RcjYjflSchema, RcjYjflCreateSchema, RcjYjflUpdateSchema,
    RcjEjflSchema, RcjEjflCreateSchema, RcjEjflUpdateSchema,
    RcjMC2EjflidSchema, RcjMC2EjflidCreateSchema, RcjMC2EjflidUpdateSchema,
    RcjMCClassifySchema, RcjMCClassifyCreateSchema, RcjMCClassifyUpdateSchema
)
from app.utils.decorators import validate_json
from app.utils.pagination import paginate
from app.swagger import api, message_model, error_model, pagination_model

# 创建字典管理命名空间
dict_ns = api.namespace('dict', description='字典管理接口')

# 定义Swagger模型
dw_type_model = api.model('DwType', {
    'id': fields.String(required=True, description='单位类别ID'),
    'typeName': fields.String(required=True, description='类别名称'),
    'create_time': fields.DateTime(description='创建时间'),
    'update_time': fields.DateTime(description='更新时间')
})

dw_type_create_model = api.model('DwTypeCreate', {
    'id': fields.String(required=True, description='单位类别ID'),
    'typeName': fields.String(required=True, description='类别名称')
})

dw_type_update_model = api.model('DwTypeUpdate', {
    'typeName': fields.String(description='类别名称')
})

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

# 创建Schema实例
dw_type_schema = DwTypeSchema()
dw_types_schema = DwTypeSchema(many=True)
dw_type_create_schema = DwTypeCreateSchema()
dw_type_update_schema = DwTypeUpdateSchema()

dw_schema = DwSchema()
dws_schema = DwSchema(many=True)
dw_create_schema = DwCreateSchema()
dw_update_schema = DwUpdateSchema()

rcj_ejfl_sx_schema = RcjEjflSxSchema()
rcj_ejfl_sxs_schema = RcjEjflSxSchema(many=True)
rcj_ejfl_sx_create_schema = RcjEjflSxCreateSchema()
rcj_ejfl_sx_update_schema = RcjEjflSxUpdateSchema()

rcj_yjfl_schema = RcjYjflSchema()
rcj_yjfls_schema = RcjYjflSchema(many=True)
rcj_yjfl_create_schema = RcjYjflCreateSchema()
rcj_yjfl_update_schema = RcjYjflUpdateSchema()

rcj_ejfl_schema = RcjEjflSchema()
rcj_ejfls_schema = RcjEjflSchema(many=True)
rcj_ejfl_create_schema = RcjEjflCreateSchema()
rcj_ejfl_update_schema = RcjEjflUpdateSchema()

rcj_mc2ejflid_schema = RcjMC2EjflidSchema()
rcj_mc2ejflids_schema = RcjMC2EjflidSchema(many=True)
rcj_mc2ejflid_create_schema = RcjMC2EjflidCreateSchema()
rcj_mc2ejflid_update_schema = RcjMC2EjflidUpdateSchema()

rcj_mc_classify_schema = RcjMCClassifySchema()
rcj_mc_classifies_schema = RcjMCClassifySchema(many=True)
rcj_mc_classify_create_schema = RcjMCClassifyCreateSchema()
rcj_mc_classify_update_schema = RcjMCClassifyUpdateSchema()

# 单位类别管理
@dict_ns.route('/dw-types')
class DwTypeListResource(Resource):
    """单位类别列表资源"""
    
    @dict_ns.doc('获取单位类别列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.response(200, '获取成功')
    def get(self):
        """获取单位类别列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        dw_types = DwType.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return paginate(dw_types, dw_types_schema)
    
    @dict_ns.doc('创建单位类别')
    @dict_ns.expect(dw_type_create_model)
    @dict_ns.response(201, '创建成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @validate_json
    def post(self):
        """创建单位类别"""
        data = request.get_json()
        
        # 验证数据
        errors = dw_type_create_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 检查ID是否已存在
        if DwType.query.get(data['id']):
            return {'message': '单位类别ID已存在'}, 400
        
        # 检查名称是否已存在
        if DwType.query.filter_by(typeName=data['typeName']).first():
            return {'message': '单位类别名称已存在'}, 400
        
        # 创建单位类别
        dw_type = DwType(
            id=data['id'],
            typeName=data['typeName']
        )
        
        db.session.add(dw_type)
        db.session.commit()
        
        return {
            'message': '单位类别创建成功',
            'dw_type': dw_type_schema.dump(dw_type)
        }, 201

@dict_ns.route('/dw-types/<string:type_id>')
@dict_ns.param('type_id', '单位类别ID')
class DwTypeResource(Resource):
    """单个单位类别资源"""
    
    @dict_ns.doc('获取单位类别信息')
    @dict_ns.response(200, '获取成功')
    @dict_ns.response(404, '单位类别不存在', error_model)
    def get(self, type_id):
        """获取单位类别信息"""
        dw_type = DwType.query.get_or_404(type_id)
        return {'dw_type': dw_type_schema.dump(dw_type)}
    
    @dict_ns.doc('更新单位类别')
    @dict_ns.expect(dw_type_update_model)
    @dict_ns.response(200, '更新成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @dict_ns.response(404, '单位类别不存在', error_model)
    @validate_json
    def put(self, type_id):
        """更新单位类别"""
        dw_type = DwType.query.get_or_404(type_id)
        
        data = request.get_json()
        
        # 验证数据
        errors = dw_type_update_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 更新字段
        if 'typeName' in data:
            existing_type = DwType.query.filter_by(typeName=data['typeName']).first()
            if existing_type and existing_type.id != type_id:
                return {'message': '单位类别名称已存在'}, 400
            dw_type.typeName = data['typeName']
        
        db.session.commit()
        
        return {
            'message': '单位类别更新成功',
            'dw_type': dw_type_schema.dump(dw_type)
        }
    
    @dict_ns.doc('删除单位类别')
    @dict_ns.response(200, '删除成功', message_model)
    @dict_ns.response(404, '单位类别不存在', error_model)
    def delete(self, type_id):
        """删除单位类别"""
        dw_type = DwType.query.get_or_404(type_id)
        db.session.delete(dw_type)
        db.session.commit()
        
        return {'message': '单位类别删除成功'}, 200

# 单位管理
@dict_ns.route('/dws')
class DwListResource(Resource):
    """单位列表资源"""
    
    @dict_ns.doc('获取单位列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.param('type_id', '类别ID', type=str)
    @dict_ns.response(200, '获取成功')
    def get(self):
        """获取单位列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        type_id = request.args.get('type_id')
        
        query = Dw.query
        if type_id:
            query = query.filter_by(type_id=type_id)
        
        dws = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return paginate(dws, dws_schema)
    
    @dict_ns.doc('创建单位')
    @dict_ns.expect(dw_create_model)
    @dict_ns.response(201, '创建成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @validate_json
    def post(self):
        """创建单位"""
        data = request.get_json()
        
        # 验证数据
        errors = dw_create_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 检查ID是否已存在
        if Dw.query.get(data['id']):
            return {'message': '单位ID已存在'}, 400
        
        # 检查名称是否已存在
        if Dw.query.filter_by(dw=data['dw']).first():
            return {'message': '单位名称已存在'}, 400
        
        # 检查类别是否存在
        if data.get('type_id') and not DwType.query.get(data['type_id']):
            return {'message': '指定的单位类别不存在'}, 400
        
        # 创建单位
        dw = Dw(
            id=data['id'],
            type_id=data.get('type_id'),
            dw=data['dw']
        )
        
        db.session.add(dw)
        db.session.commit()
        
        return {
            'message': '单位创建成功',
            'dw': dw_schema.dump(dw)
        }, 201

@dict_ns.route('/dws/<string:dw_id>')
@dict_ns.param('dw_id', '单位ID')
class DwResource(Resource):
    """单个单位资源"""
    
    @dict_ns.doc('获取单位信息')
    @dict_ns.response(200, '获取成功')
    @dict_ns.response(404, '单位不存在', error_model)
    def get(self, dw_id):
        """获取单位信息"""
        dw = Dw.query.get_or_404(dw_id)
        return {'dw': dw_schema.dump(dw)}
    
    @dict_ns.doc('更新单位')
    @dict_ns.expect(dw_update_model)
    @dict_ns.response(200, '更新成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @dict_ns.response(404, '单位不存在', error_model)
    @validate_json
    def put(self, dw_id):
        """更新单位"""
        dw = Dw.query.get_or_404(dw_id)
        
        data = request.get_json()
        
        # 验证数据
        errors = dw_update_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 更新字段
        if 'type_id' in data:
            if data['type_id'] and not DwType.query.get(data['type_id']):
                return {'message': '指定的单位类别不存在'}, 400
            dw.type_id = data['type_id']
        
        if 'dw' in data:
            existing_dw = Dw.query.filter_by(dw=data['dw']).first()
            if existing_dw and existing_dw.id != dw_id:
                return {'message': '单位名称已存在'}, 400
            dw.dw = data['dw']
        
        db.session.commit()
        
        return {
            'message': '单位更新成功',
            'dw': dw_schema.dump(dw)
        }
    
    @dict_ns.doc('删除单位')
    @dict_ns.response(200, '删除成功', message_model)
    @dict_ns.response(404, '单位不存在', error_model)
    def delete(self, dw_id):
        """删除单位"""
        dw = Dw.query.get_or_404(dw_id)
        db.session.delete(dw)
        db.session.commit()
        
        return {'message': '单位删除成功'}, 200

# 人材机二级分类属性管理
@dict_ns.route('/rcj-ejfl-sxs')
class RcjEjflSxListResource(Resource):
    """人材机二级分类属性列表资源"""
    
    @dict_ns.doc('获取人材机二级分类属性列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.response(200, '获取成功')
    def get(self):
        """获取人材机二级分类属性列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        sxs = RcjEjflSx.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return paginate(sxs, rcj_ejfl_sxs_schema)
    
    @dict_ns.doc('创建人材机二级分类属性')
    @dict_ns.expect(rcj_ejfl_sx_create_model)
    @dict_ns.response(201, '创建成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @validate_json
    def post(self):
        """创建人材机二级分类属性"""
        data = request.get_json()
        
        # 验证数据
        errors = rcj_ejfl_sx_create_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 检查ID是否已存在
        if RcjEjflSx.query.get(data['id']):
            return {'message': '属性ID已存在'}, 400
        
        # 检查名称是否已存在
        if RcjEjflSx.query.filter_by(sx=data['sx']).first():
            return {'message': '属性名称已存在'}, 400
        
        # 创建属性
        sx = RcjEjflSx(
            id=data['id'],
            sx=data['sx']
        )
        
        db.session.add(sx)
        db.session.commit()
        
        return {
            'message': '人材机二级分类属性创建成功',
            'sx': rcj_ejfl_sx_schema.dump(sx)
        }, 201

@dict_ns.route('/rcj-ejfl-sxs/<string:sx_id>')
@dict_ns.param('sx_id', '属性ID')
class RcjEjflSxResource(Resource):
    """单个人材机二级分类属性资源"""
    
    @dict_ns.doc('获取人材机二级分类属性信息')
    @dict_ns.response(200, '获取成功')
    @dict_ns.response(404, '属性不存在', error_model)
    def get(self, sx_id):
        """获取人材机二级分类属性信息"""
        sx = RcjEjflSx.query.get_or_404(sx_id)
        return {'sx': rcj_ejfl_sx_schema.dump(sx)}
    
    @dict_ns.doc('更新人材机二级分类属性')
    @dict_ns.expect(rcj_ejfl_sx_update_model)
    @dict_ns.response(200, '更新成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @dict_ns.response(404, '属性不存在', error_model)
    @validate_json
    def put(self, sx_id):
        """更新人材机二级分类属性"""
        sx = RcjEjflSx.query.get_or_404(sx_id)
        
        data = request.get_json()
        
        # 验证数据
        errors = rcj_ejfl_sx_update_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 更新字段
        if 'sx' in data:
            existing_sx = RcjEjflSx.query.filter_by(sx=data['sx']).first()
            if existing_sx and existing_sx.id != sx_id:
                return {'message': '属性名称已存在'}, 400
            sx.sx = data['sx']
        
        db.session.commit()
        
        return {
            'message': '人材机二级分类属性更新成功',
            'sx': rcj_ejfl_sx_schema.dump(sx)
        }
    
    @dict_ns.doc('删除人材机二级分类属性')
    @dict_ns.response(200, '删除成功', message_model)
    @dict_ns.response(404, '属性不存在', error_model)
    def delete(self, sx_id):
        """删除人材机二级分类属性"""
        sx = RcjEjflSx.query.get_or_404(sx_id)
        db.session.delete(sx)
        db.session.commit()
        
        return {'message': '人材机二级分类属性删除成功'}, 200

# 人材机一级分类管理
@dict_ns.route('/rcj-yjfls')
class RcjYjflListResource(Resource):
    """人材机一级分类列表资源"""
    
    @dict_ns.doc('获取人材机一级分类列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.response(200, '获取成功')
    def get(self):
        """获取人材机一级分类列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        yjfls = RcjYjfl.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return paginate(yjfls, rcj_yjfls_schema)
    
    @dict_ns.doc('创建人材机一级分类')
    @dict_ns.expect(rcj_yjfl_create_model)
    @dict_ns.response(201, '创建成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @validate_json
    def post(self):
        """创建人材机一级分类"""
        data = request.get_json()
        
        # 验证数据
        errors = rcj_yjfl_create_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 检查ID是否已存在
        if RcjYjfl.query.get(data['id']):
            return {'message': '一级分类ID已存在'}, 400
        
        # 检查名称是否已存在
        if RcjYjfl.query.filter_by(yjflmc=data['yjflmc']).first():
            return {'message': '一级分类名称已存在'}, 400
        
        # 创建一级分类
        yjfl = RcjYjfl(
            id=data['id'],
            yjflmc=data['yjflmc'],
            yjflms=data.get('yjflms')
        )
        
        db.session.add(yjfl)
        db.session.commit()
        
        return {
            'message': '人材机一级分类创建成功',
            'yjfl': rcj_yjfl_schema.dump(yjfl)
        }, 201

@dict_ns.route('/rcj-yjfls/<string:yjfl_id>')
@dict_ns.param('yjfl_id', '一级分类ID')
class RcjYjflResource(Resource):
    """单个人材机一级分类资源"""
    
    @dict_ns.doc('获取人材机一级分类信息')
    @dict_ns.response(200, '获取成功')
    @dict_ns.response(404, '一级分类不存在', error_model)
    def get(self, yjfl_id):
        """获取人材机一级分类信息"""
        yjfl = RcjYjfl.query.get_or_404(yjfl_id)
        return {'yjfl': rcj_yjfl_schema.dump(yjfl)}
    
    @dict_ns.doc('更新人材机一级分类')
    @dict_ns.expect(rcj_yjfl_update_model)
    @dict_ns.response(200, '更新成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @dict_ns.response(404, '一级分类不存在', error_model)
    @validate_json
    def put(self, yjfl_id):
        """更新人材机一级分类"""
        yjfl = RcjYjfl.query.get_or_404(yjfl_id)
        
        data = request.get_json()
        
        # 验证数据
        errors = rcj_yjfl_update_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 更新字段
        if 'yjflmc' in data:
            existing_yjfl = RcjYjfl.query.filter_by(yjflmc=data['yjflmc']).first()
            if existing_yjfl and existing_yjfl.id != yjfl_id:
                return {'message': '一级分类名称已存在'}, 400
            yjfl.yjflmc = data['yjflmc']
        
        if 'yjflms' in data:
            yjfl.yjflms = data['yjflms']
        
        db.session.commit()
        
        return {
            'message': '人材机一级分类更新成功',
            'yjfl': rcj_yjfl_schema.dump(yjfl)
        }
    
    @dict_ns.doc('删除人材机一级分类')
    @dict_ns.response(200, '删除成功', message_model)
    @dict_ns.response(404, '一级分类不存在', error_model)
    def delete(self, yjfl_id):
        """删除人材机一级分类"""
        yjfl = RcjYjfl.query.get_or_404(yjfl_id)
        db.session.delete(yjfl)
        db.session.commit()
        
        return {'message': '人材机一级分类删除成功'}, 200

# 人材机二级分类管理
@dict_ns.route('/rcj-ejfls')
class RcjEjflListResource(Resource):
    """人材机二级分类列表资源"""
    
    @dict_ns.doc('获取人材机二级分类列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.param('yjfl_id', '一级分类ID', type=str)
    @dict_ns.response(200, '获取成功')
    def get(self):
        """获取人材机二级分类列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        yjfl_id = request.args.get('yjfl_id')
        
        query = RcjEjfl.query
        if yjfl_id:
            query = query.filter_by(yjfl_id=yjfl_id)
        
        ejfls = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return paginate(ejfls, rcj_ejfls_schema)
    
    @dict_ns.doc('创建人材机二级分类')
    @dict_ns.expect(rcj_ejfl_create_model)
    @dict_ns.response(201, '创建成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @validate_json
    def post(self):
        """创建人材机二级分类"""
        data = request.get_json()
        
        # 验证数据
        errors = rcj_ejfl_create_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 检查ID是否已存在
        if RcjEjfl.query.get(data['id']):
            return {'message': '二级分类ID已存在'}, 400
        
        # 检查一级分类是否存在
        if data.get('yjfl_id') and not RcjYjfl.query.get(data['yjfl_id']):
            return {'message': '指定的一级分类不存在'}, 400
        
        # 创建二级分类
        ejfl = RcjEjfl(
            id=data['id'],
            yjfl_id=data.get('yjfl_id'),
            ejflmc=data['ejflmc'],
            ejflms=data.get('ejflms')
        )
        
        # 处理关联的属性
        if data.get('sx_ids'):
            sxs = RcjEjflSx.query.filter(RcjEjflSx.id.in_(data['sx_ids'])).all()
            ejfl._sxs = sxs
        
        # 处理关联的单位
        if data.get('dw_ids'):
            dws = Dw.query.filter(Dw.id.in_(data['dw_ids'])).all()
            ejfl._dws = dws
        
        db.session.add(ejfl)
        db.session.commit()
        
        return {
            'message': '人材机二级分类创建成功',
            'ejfl': rcj_ejfl_schema.dump(ejfl)
        }, 201

@dict_ns.route('/rcj-ejfls/<string:ejfl_id>')
@dict_ns.param('ejfl_id', '二级分类ID')
class RcjEjflResource(Resource):
    """单个人材机二级分类资源"""
    
    @dict_ns.doc('获取人材机二级分类信息')
    @dict_ns.response(200, '获取成功')
    @dict_ns.response(404, '二级分类不存在', error_model)
    def get(self, ejfl_id):
        """获取人材机二级分类信息"""
        ejfl = RcjEjfl.query.get_or_404(ejfl_id)
        return {'ejfl': rcj_ejfl_schema.dump(ejfl)}
    
    @dict_ns.doc('更新人材机二级分类')
    @dict_ns.expect(rcj_ejfl_update_model)
    @dict_ns.response(200, '更新成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @dict_ns.response(404, '二级分类不存在', error_model)
    @validate_json
    def put(self, ejfl_id):
        """更新人材机二级分类"""
        ejfl = RcjEjfl.query.get_or_404(ejfl_id)
        
        data = request.get_json()
        
        # 验证数据
        errors = rcj_ejfl_update_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 更新字段
        if 'yjfl_id' in data:
            if data['yjfl_id'] and not RcjYjfl.query.get(data['yjfl_id']):
                return {'message': '指定的一级分类不存在'}, 400
            ejfl.yjfl_id = data['yjfl_id']
        
        if 'ejflmc' in data:
            ejfl.ejflmc = data['ejflmc']
        
        if 'ejflms' in data:
            ejfl.ejflms = data['ejflms']
        
        # 更新关联的属性
        if 'sx_ids' in data:
            sxs = RcjEjflSx.query.filter(RcjEjflSx.id.in_(data['sx_ids'])).all()
            ejfl._sxs = sxs
        
        # 更新关联的单位
        if 'dw_ids' in data:
            dws = Dw.query.filter(Dw.id.in_(data['dw_ids'])).all()
            ejfl._dws = dws
        
        db.session.commit()
        
        return {
            'message': '人材机二级分类更新成功',
            'ejfl': rcj_ejfl_schema.dump(ejfl)
        }
    
    @dict_ns.doc('删除人材机二级分类')
    @dict_ns.response(200, '删除成功', message_model)
    @dict_ns.response(404, '二级分类不存在', error_model)
    def delete(self, ejfl_id):
        """删除人材机二级分类"""
        ejfl = RcjEjfl.query.get_or_404(ejfl_id)
        db.session.delete(ejfl)
        db.session.commit()
        
        return {'message': '人材机二级分类删除成功'}, 200

# 人材机名称到二级分类ID映射管理
@dict_ns.route('/rcj-mc2ejflids')
class RcjMC2EjflidListResource(Resource):
    """人材机名称到二级分类ID映射列表资源"""
    
    @dict_ns.doc('获取人材机名称到二级分类ID映射列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.param('ejflid', '二级分类ID', type=str)
    @dict_ns.response(200, '获取成功')
    def get(self):
        """获取人材机名称到二级分类ID映射列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        ejflid = request.args.get('ejflid')
        
        query = RcjMC2Ejflid.query
        if ejflid:
            query = query.filter_by(ejflid=ejflid)
        
        mappings = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return paginate(mappings, rcj_mc2ejflids_schema)
    
    @dict_ns.doc('创建人材机名称到二级分类ID映射')
    @dict_ns.expect(rcj_mc2ejflid_create_model)
    @dict_ns.response(201, '创建成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @validate_json
    def post(self):
        """创建人材机名称到二级分类ID映射"""
        data = request.get_json()
        
        # 验证数据
        errors = rcj_mc2ejflid_create_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 检查二级分类是否存在
        if not RcjEjfl.query.get(data['ejflid']):
            return {'message': '指定的二级分类不存在'}, 400
        
        # 检查原始名称是否已存在
        if RcjMC2Ejflid.query.filter_by(orignal_rcjmc=data['orignal_rcjmc']).first():
            return {'message': '原始人材机名称已存在'}, 400
        
        # 创建映射
        mapping = RcjMC2Ejflid(
            ejflid=data['ejflid'],
            orignal_rcjmc=data['orignal_rcjmc']
        )
        
        db.session.add(mapping)
        db.session.commit()
        
        return {
            'message': '人材机名称到二级分类ID映射创建成功',
            'mapping': rcj_mc2ejflid_schema.dump(mapping)
        }, 201

@dict_ns.route('/rcj-mc2ejflids/<int:mapping_id>')
@dict_ns.param('mapping_id', '映射ID')
class RcjMC2EjflidResource(Resource):
    """单个人材机名称到二级分类ID映射资源"""
    
    @dict_ns.doc('获取人材机名称到二级分类ID映射信息')
    @dict_ns.response(200, '获取成功')
    @dict_ns.response(404, '映射不存在', error_model)
    def get(self, mapping_id):
        """获取人材机名称到二级分类ID映射信息"""
        mapping = RcjMC2Ejflid.query.get_or_404(mapping_id)
        return {'mapping': rcj_mc2ejflid_schema.dump(mapping)}
    
    @dict_ns.doc('更新人材机名称到二级分类ID映射')
    @dict_ns.expect(rcj_mc2ejflid_update_model)
    @dict_ns.response(200, '更新成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @dict_ns.response(404, '映射不存在', error_model)
    @validate_json
    def put(self, mapping_id):
        """更新人材机名称到二级分类ID映射"""
        mapping = RcjMC2Ejflid.query.get_or_404(mapping_id)
        
        data = request.get_json()
        
        # 验证数据
        errors = rcj_mc2ejflid_update_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 更新字段
        if 'ejflid' in data:
            if not RcjEjfl.query.get(data['ejflid']):
                return {'message': '指定的二级分类不存在'}, 400
            mapping.ejflid = data['ejflid']
        
        if 'orignal_rcjmc' in data:
            existing_mapping = RcjMC2Ejflid.query.filter_by(orignal_rcjmc=data['orignal_rcjmc']).first()
            if existing_mapping and existing_mapping.id != mapping_id:
                return {'message': '原始人材机名称已存在'}, 400
            mapping.orignal_rcjmc = data['orignal_rcjmc']
        
        db.session.commit()
        
        return {
            'message': '人材机名称到二级分类ID映射更新成功',
            'mapping': rcj_mc2ejflid_schema.dump(mapping)
        }
    
    @dict_ns.doc('删除人材机名称到二级分类ID映射')
    @dict_ns.response(200, '删除成功', message_model)
    @dict_ns.response(404, '映射不存在', error_model)
    def delete(self, mapping_id):
        """删除人材机名称到二级分类ID映射"""
        mapping = RcjMC2Ejflid.query.get_or_404(mapping_id)
        db.session.delete(mapping)
        db.session.commit()
        
        return {'message': '人材机名称到二级分类ID映射删除成功'}, 200

# 人材机名称分类管理
@dict_ns.route('/rcj-mc-classifies')
class RcjMCClassifyListResource(Resource):
    """人材机名称分类列表资源"""
    
    @dict_ns.doc('获取人材机名称分类列表')
    @dict_ns.param('page', '页码', type=int, default=1)
    @dict_ns.param('per_page', '每页数量', type=int, default=10)
    @dict_ns.param('yjflid', '一级分类ID', type=str)
    @dict_ns.param('ejflid', '二级分类ID', type=str)
    @dict_ns.response(200, '获取成功')
    def get(self):
        """获取人材机名称分类列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        yjflid = request.args.get('yjflid')
        ejflid = request.args.get('ejflid')
        
        query = RcjMCClassify.query
        if yjflid:
            query = query.filter_by(yjflid=yjflid)
        if ejflid:
            query = query.filter_by(ejflid=ejflid)
        
        classifies = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return paginate(classifies, rcj_mc_classifies_schema)
    
    @dict_ns.doc('创建人材机名称分类')
    @dict_ns.expect(rcj_mc_classify_create_model)
    @dict_ns.response(201, '创建成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @validate_json
    def post(self):
        """创建人材机名称分类"""
        data = request.get_json()
        
        # 验证数据
        errors = rcj_mc_classify_create_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 检查清洗后的名称是否已存在
        if RcjMCClassify.query.filter_by(cleaned_rcj_original_mc=data['cleaned_rcj_original_mc']).first():
            return {'message': '清洗后的人材机名称已存在'}, 400
        
        # 创建分类
        classify = RcjMCClassify(
            cleaned_rcj_original_mc=data['cleaned_rcj_original_mc'],
            yjflid=data.get('yjflid'),
            yjflmc=data.get('yjflmc'),
            ejflid=data.get('ejflid'),
            ejflmc=data.get('ejflmc')
        )
        
        db.session.add(classify)
        db.session.commit()
        
        return {
            'message': '人材机名称分类创建成功',
            'classify': rcj_mc_classify_schema.dump(classify)
        }, 201

@dict_ns.route('/rcj-mc-classifies/<int:classify_id>')
@dict_ns.param('classify_id', '分类ID')
class RcjMCClassifyResource(Resource):
    """单个人材机名称分类资源"""
    
    @dict_ns.doc('获取人材机名称分类信息')
    @dict_ns.response(200, '获取成功')
    @dict_ns.response(404, '分类不存在', error_model)
    def get(self, classify_id):
        """获取人材机名称分类信息"""
        classify = RcjMCClassify.query.get_or_404(classify_id)
        return {'classify': rcj_mc_classify_schema.dump(classify)}
    
    @dict_ns.doc('更新人材机名称分类')
    @dict_ns.expect(rcj_mc_classify_update_model)
    @dict_ns.response(200, '更新成功')
    @dict_ns.response(400, '数据验证失败', error_model)
    @dict_ns.response(404, '分类不存在', error_model)
    @validate_json
    def put(self, classify_id):
        """更新人材机名称分类"""
        classify = RcjMCClassify.query.get_or_404(classify_id)
        
        data = request.get_json()
        
        # 验证数据
        errors = rcj_mc_classify_update_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 更新字段
        if 'cleaned_rcj_original_mc' in data:
            existing_classify = RcjMCClassify.query.filter_by(cleaned_rcj_original_mc=data['cleaned_rcj_original_mc']).first()
            if existing_classify and existing_classify.id != classify_id:
                return {'message': '清洗后的人材机名称已存在'}, 400
            classify.cleaned_rcj_original_mc = data['cleaned_rcj_original_mc']
        
        if 'yjflid' in data:
            classify.yjflid = data['yjflid']
        
        if 'yjflmc' in data:
            classify.yjflmc = data['yjflmc']
        
        if 'ejflid' in data:
            classify.ejflid = data['ejflid']
        
        if 'ejflmc' in data:
            classify.ejflmc = data['ejflmc']
        
        db.session.commit()
        
        return {
            'message': '人材机名称分类更新成功',
            'classify': rcj_mc_classify_schema.dump(classify)
        }
    
    @dict_ns.doc('删除人材机名称分类')
    @dict_ns.response(200, '删除成功', message_model)
    @dict_ns.response(404, '分类不存在', error_model)
    def delete(self, classify_id):
        """删除人材机名称分类"""
        classify = RcjMCClassify.query.get_or_404(classify_id)
        db.session.delete(classify)
        db.session.commit()
        
        return {'message': '人材机名称分类删除成功'}, 200
