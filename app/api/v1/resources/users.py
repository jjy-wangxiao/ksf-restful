from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.user import User
from app.schemas.user import UserSchema, UserCreateSchema
from app.utils.decorators import validate_json, admin_required
from app.utils.pagination import paginate

user_schema = UserSchema()
users_schema = UserSchema(many=True)
user_create_schema = UserCreateSchema()

class UserListResource(Resource):
    """用户列表资源"""
    
    @jwt_required()
    @admin_required
    def get(self):
        """获取用户列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        users = User.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return paginate(users, users_schema)
    
    @validate_json
    def post(self):
        """创建新用户"""
        data = request.get_json()
        
        # 验证数据
        errors = user_create_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 检查用户名和邮箱是否已存在
        if User.query.filter_by(username=data['username']).first():
            return {'message': '用户名已存在'}, 400
        
        if User.query.filter_by(email=data['email']).first():
            return {'message': '邮箱已存在'}, 400
        
        # 创建用户
        user = User(
            username=data['username'],
            email=data['email']
        )
        user.password = data['password']
        
        db.session.add(user)
        db.session.commit()
        
        return {
            'message': '用户创建成功',
            'user': user_schema.dump(user)
        }, 201

class UserResource(Resource):
    """单个用户资源"""
    
    @jwt_required()
    def get(self, user_id):
        """获取用户信息"""
        user = User.query.get_or_404(user_id)
        return {'user': user_schema.dump(user)}
    
    @jwt_required()
    def put(self, user_id):
        """更新用户信息"""
        current_user_id = get_jwt_identity()
        user = User.query.get_or_404(user_id)
        
        # 只能更新自己的信息，除非是管理员
        if current_user_id != user_id:
            current_user = User.query.get(current_user_id)
            if not current_user.is_admin:
                return {'message': '权限不足'}, 403
        
        data = request.get_json()
        
        # 更新字段
        if 'username' in data:
            existing_user = User.query.filter_by(username=data['username']).first()
            if existing_user and existing_user.id != user_id:
                return {'message': '用户名已存在'}, 400
            user.username = data['username']
        
        if 'email' in data:
            existing_user = User.query.filter_by(email=data['email']).first()
            if existing_user and existing_user.id != user_id:
                return {'message': '邮箱已存在'}, 400
            user.email = data['email']
        
        if 'password' in data:
            user.password = data['password']
        
        db.session.commit()
        
        return {
            'message': '用户信息更新成功',
            'user': user_schema.dump(user)
        }
    
    @jwt_required()
    @admin_required
    def delete(self, user_id):
        """删除用户"""
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        
        return {'message': '用户删除成功'}, 200 