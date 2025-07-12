from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app import db
from app.models.user import User
from app.schemas.user import UserSchema
from app.utils.decorators import validate_json

user_schema = UserSchema()

class AuthResource(Resource):
    """认证资源"""
    
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
            
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            
            return {
                'message': '登录成功',
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user': user_schema.dump(user)
            }, 200
        else:
            return {'message': '用户名或密码错误'}, 401

class RefreshResource(Resource):
    """刷新令牌资源"""
    
    @jwt_required(refresh=True)
    def post(self):
        """刷新访问令牌"""
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user or not user.is_active:
            return {'message': '用户不存在或已被禁用'}, 401
        
        access_token = create_access_token(identity=current_user_id)
        
        return {
            'message': '令牌刷新成功',
            'access_token': access_token
        }, 200 