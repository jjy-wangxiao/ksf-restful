"""
装饰器工具 - 简化API响应处理
"""
from functools import wraps
from flask import request, jsonify
from app.utils.response_builder import ResponseBuilder
from app.dto.common import ApiResponse


def api_response(func):
    """API响应装饰器，自动处理DTO到JSON的转换"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            
            # 如果返回的是元组 (data, status_code)
            if isinstance(result, tuple) and len(result) == 2:
                data, status_code = result
            else:
                data, status_code = result, 200
            
            # 如果数据有to_dict方法，自动调用
            if hasattr(data, 'to_dict'):
                return data.to_dict(), status_code
            else:
                return data, status_code
                
        except Exception as e:
            # 记录错误日志
            error_response = ResponseBuilder.error(
                error_code="INTERNAL_ERROR",
                message=str(e)
            )
            return error_response.to_dict(), 500
    
    return wrapper


def paginated_response(func):
    """分页响应装饰器，自动处理分页数据"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            
            # 如果返回的是元组 (data, status_code)
            if isinstance(result, tuple) and len(result) == 2:
                data, status_code = result
            else:
                data, status_code = result, 200
            
            # 确保返回的是分页响应DTO
            if hasattr(data, 'to_dict'):
                return data.to_dict(), status_code
            else:
                return data, status_code
                
        except Exception as e:
            error_response = ResponseBuilder.error(
                error_code="INTERNAL_ERROR",
                message=str(e)
            )
            return error_response.to_dict(), 500
    
    return wrapper


def validate_request(schema_class=None):
    """请求验证装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # 如果有schema类，进行验证
                if schema_class:
                    data = request.get_json()
                    # 这里可以添加schema验证逻辑
                    # validated_data = schema_class().load(data)
                    # kwargs['validated_data'] = validated_data
                
                return func(*args, **kwargs)
                
            except Exception as e:
                error_response = ResponseBuilder.error(
                    error_code="VALIDATION_ERROR",
                    message=str(e)
                )
                return error_response.to_dict(), 400
        
        return wrapper
    return decorator 