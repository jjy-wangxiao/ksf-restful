from flask_restx import Api, fields
from flask import Blueprint

# 创建 API 蓝图
api_blueprint = Blueprint('api', __name__)

# 创建 API 实例
api = Api(
    api_blueprint,
    title='KSF RESTful API',
    version='1.0',
    description='一个基于Flask-RESTful的完整REST API项目框架（测试版本，无认证）',
    doc='/docs'
)

# 创建命名空间
auth_ns = api.namespace('auth', description='认证相关接口')
users_ns = api.namespace('users', description='用户管理接口')
posts_ns = api.namespace('posts', description='文章管理接口')
dict_ns = api.namespace('dict', description='字典管理接口')

# 定义通用响应模型
message_model = api.model('Message', {
    'message': fields.String(required=True, description='响应消息')
})

error_model = api.model('Error', {
    'message': fields.String(required=True, description='错误消息'),
    'errors': fields.Raw(description='详细错误信息')
})

pagination_model = api.model('Pagination', {
    'page': fields.Integer(description='当前页码'),
    'pages': fields.Integer(description='总页数'),
    'per_page': fields.Integer(description='每页数量'),
    'total': fields.Integer(description='总记录数'),
    'has_next': fields.Boolean(description='是否有下一页'),
    'has_prev': fields.Boolean(description='是否有上一页')
})

# 导入所有资源 - 这很重要！
from app.api.v1.resources.dict import (
    DwTypeListResource, DwTypeResource,
    DwListResource, DwResource,
    RcjEjflSxListResource, RcjEjflSxResource,
    RcjYjflListResource, RcjYjflResource,
    RcjEjflListResource, RcjEjflResource,
    RcjMC2EjflidListResource, RcjMC2EjflidResource,
    RcjMCClassifyListResource, RcjMCClassifyResource
) 