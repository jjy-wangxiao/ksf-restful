from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from app.models.user import User

def validate_json(f):
    """验证请求是否为JSON格式"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            return jsonify({'message': '请求必须是JSON格式'}), 400
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """验证管理员权限"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        if not current_user_id:
            return jsonify({'message': '需要登录'}), 401
        
        user = User.query.get(current_user_id)
        if not user or not user.is_admin:
            return jsonify({'message': '需要管理员权限'}), 403
        
        return f(*args, **kwargs)
    return decorated_function

def owner_required(f):
    """验证资源所有者权限"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        if not current_user_id:
            return jsonify({'message': '需要登录'}), 401
        
        user = User.query.get(current_user_id)
        if not user:
            return jsonify({'message': '用户不存在'}), 401
        
        # 检查是否为管理员或资源所有者
        resource_user_id = kwargs.get('user_id')
        if resource_user_id and user.id != resource_user_id and not user.is_admin:
            return jsonify({'message': '权限不足'}), 403
        
        return f(*args, **kwargs)
    return decorated_function 