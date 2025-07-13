from flask import request
from flask_restx import Resource, fields
from app import db
from app.models.user import User
from app.schemas.user import UserSchema, UserCreateSchema
from app.utils.decorators import validate_json
from app.utils.pagination import paginate
from app.swagger import users_ns, message_model, error_model, pagination_model

user_schema = UserSchema()
users_schema = UserSchema(many=True)
user_create_schema = UserCreateSchema()

# 定义模型
user_model = users_ns.model('User', {
    'id': fields.String(description='用户ID'),
    'username': fields.String(description='用户名'),
    'email': fields.String(description='邮箱'),
    'is_active': fields.Boolean(description='是否激活'),
    'is_admin': fields.Boolean(description='是否管理员'),
    'created_at': fields.DateTime(description='创建时间'),
    'updated_at': fields.DateTime(description='更新时间')
})

user_create_model = users_ns.model('UserCreate', {
    'username': fields.String(required=True, description='用户名'),
    'email': fields.String(required=True, description='邮箱'),
    'password': fields.String(required=True, description='密码')
})

user_update_model = users_ns.model('UserUpdate', {
    'username': fields.String(description='用户名'),
    'email': fields.String(description='邮箱'),
    'password': fields.String(description='密码')
})

user_list_response = users_ns.model('UserListResponse', {
    'items': fields.List(fields.Nested(user_model), description='用户列表'),
    'pagination': fields.Nested(pagination_model, description='分页信息')
})

@users_ns.route('/')
class UserListResource(Resource):
    """用户列表资源"""
    
    @users_ns.doc('获取用户列表')
    @users_ns.param('page', '页码', type=int, default=1)
    @users_ns.param('per_page', '每页数量', type=int, default=10)
    @users_ns.response(200, '获取成功', user_list_response)
    def get(self):
        """获取用户列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        users = User.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return paginate(users, users_schema)
    
    @users_ns.doc('创建新用户')
    @users_ns.expect(user_create_model)
    @users_ns.response(201, '创建成功', user_model)
    @users_ns.response(400, '数据验证失败', error_model)
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

@users_ns.route('/<string:user_id>')
@users_ns.param('user_id', '用户ID')
class UserResource(Resource):
    """单个用户资源"""
    
    @users_ns.doc('获取用户信息')
    @users_ns.response(200, '获取成功', user_model)
    @users_ns.response(404, '用户不存在', error_model)
    def get(self, user_id):
        """获取用户信息"""
        user = User.query.get_or_404(user_id)
        return {'user': user_schema.dump(user)}
    
    @users_ns.doc('更新用户信息')
    @users_ns.expect(user_update_model)
    @users_ns.response(200, '更新成功', user_model)
    @users_ns.response(400, '数据验证失败', error_model)
    @users_ns.response(404, '用户不存在', error_model)
    @validate_json
    def put(self, user_id):
        """更新用户信息"""
        user = User.query.get_or_404(user_id)
        
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
    
    @users_ns.doc('删除用户')
    @users_ns.response(200, '删除成功', message_model)
    @users_ns.response(404, '用户不存在', error_model)
    def delete(self, user_id):
        """删除用户"""
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        
        return {'message': '用户删除成功'}, 200 