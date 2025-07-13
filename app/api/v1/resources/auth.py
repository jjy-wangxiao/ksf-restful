from flask import request
from flask_restx import Resource, fields
from app import db
from app.models.user import User
from app.schemas.user import UserSchema
from app.utils.decorators import validate_json
from app.swagger import auth_ns, message_model, error_model

user_schema = UserSchema()

# 定义请求和响应模型
login_model = auth_ns.model('LoginRequest', {
    'username': fields.String(required=True, description='用户名'),
    'password': fields.String(required=True, description='密码')
})

login_response_model = auth_ns.model('LoginResponse', {
    'message': fields.String(description='响应消息'),
    'user': fields.Raw(description='用户信息')
})

@auth_ns.route('/login')
class AuthResource(Resource):
    """认证资源"""
    
    @auth_ns.doc('用户登录')
    @auth_ns.expect(login_model)
    @auth_ns.response(200, '登录成功', login_response_model)
    @auth_ns.response(400, '请求参数错误', error_model)
    @auth_ns.response(401, '用户名或密码错误', error_model)
    @auth_ns.response(403, '账户已被禁用', error_model)
    @validate_json
    def post(self):
        """用户登录"""
        data = request.get_json()
        
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return {'message': '用户名和密码不能为空'}, 400
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.verify_password(password):
            if not user.is_active:
                return {'message': '账户已被禁用'}, 403
            
            return {
                'message': '登录成功',
                'user': user_schema.dump(user)
            }, 200
        else:
            return {'message': '用户名或密码错误'}, 401

@auth_ns.route('/refresh')
class RefreshResource(Resource):
    """刷新令牌资源"""
    
    @auth_ns.doc('刷新访问令牌')
    @auth_ns.response(200, '令牌刷新成功', login_response_model)
    @auth_ns.response(401, '令牌无效或用户不存在', error_model)
    def post(self):
        """刷新访问令牌（测试版本，直接返回成功）"""
        return {
            'message': '令牌刷新成功（测试模式）'
        }, 200 