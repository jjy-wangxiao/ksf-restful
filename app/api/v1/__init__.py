from flask import Blueprint
from flask_restful import Api

api_v1 = Blueprint('api_v1', __name__)
api = Api(api_v1)

# 导入资源
from app.api.v1.resources.auth import AuthResource, RefreshResource
from app.api.v1.resources.users import UserListResource, UserResource
from app.api.v1.resources.posts import PostListResource, PostResource

# 注册资源
api.add_resource(AuthResource, '/auth/login')
api.add_resource(RefreshResource, '/auth/refresh')
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<string:user_id>')
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<string:post_id>') 