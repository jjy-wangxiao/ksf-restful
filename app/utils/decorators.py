from functools import wraps
from flask import request, jsonify

def validate_json(f):
    """验证请求是否为JSON格式"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            return jsonify({'message': '请求必须是JSON格式'}), 400
        return f(*args, **kwargs)
    return decorated_function

# 移除认证相关的装饰器，在测试阶段不需要 