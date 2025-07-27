from flask_restx import Api, fields
from flask import Blueprint
import os

# 创建 API 蓝图
api_blueprint = Blueprint('api', __name__)

# 创建 API 实例
api = Api(
    api_blueprint,
    title='KSF RESTful API',
    version='1.0',
    description='基于Flask-RESTful的分层架构REST API项目（DTO + Service + Entity）',
    doc='/docs',
    validate=False  # 禁用验证，避免测试环境中的问题
)

# 定义通用响应模型
message_model = api.model('Message', {
    'message': fields.String(required=True, description='响应消息')
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
from app.api.v1.resources.matrix_resources import (
    FileListResource
)
from app.api.v1.resources.upload import (
    FileUploadResource, BatchUploadResource, FileResource, FileDownloadResource
)