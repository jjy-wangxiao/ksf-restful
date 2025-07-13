"""
装饰器模块
提供通用的API装饰器功能
"""
from functools import wraps
from flask import request, jsonify

def validate_json(f):
    """
    验证请求是否为JSON格式的装饰器
    
    用法:
        @validate_json
        def post(self):
            data = request.get_json()
            # 处理数据...
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            return jsonify({'message': '请求必须是JSON格式'}), 400
        return f(*args, **kwargs)
    return decorated_function

# 注意：认证相关的装饰器已移除，在测试阶段不需要
# 如需添加认证装饰器，可以在此处扩展 