from flask import jsonify, request
from werkzeug.http import HTTP_STATUS_CODES
from app.errors import bp
from app.utils.logger import get_logger

# 获取错误日志记录器
error_logger = get_logger('app.errors')

def error_response(status_code, message=None):
    """错误响应格式化"""
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

def bad_request(message):
    """400错误"""
    return error_response(400, message)

@bp.app_errorhandler(404)
def not_found_error(error):
    """404错误"""
    error_logger.warning(
        "404 Not Found",
        url=request.url,
        method=request.method,
        remote_addr=request.remote_addr,
        user_agent=request.headers.get('User-Agent')
    )
    return error_response(404, '资源不存在')

@bp.app_errorhandler(500)
def internal_error(error):
    """500错误"""
    error_logger.error(
        "500 Internal Server Error",
        url=request.url,
        method=request.method,
        remote_addr=request.remote_addr,
        user_agent=request.headers.get('User-Agent'),
        error=str(error),
        exc_info=True
    )
    return error_response(500, '服务器内部错误')

@bp.app_errorhandler(400)
def bad_request_error(error):
    """400错误"""
    error_logger.warning(
        "400 Bad Request",
        url=request.url,
        method=request.method,
        remote_addr=request.remote_addr,
        user_agent=request.headers.get('User-Agent'),
        error=str(error)
    )
    return error_response(400, '请求参数错误')

@bp.app_errorhandler(401)
def unauthorized_error(error):
    """401错误"""
    error_logger.warning(
        "401 Unauthorized",
        url=request.url,
        method=request.method,
        remote_addr=request.remote_addr,
        user_agent=request.headers.get('User-Agent')
    )
    return error_response(401, '未授权访问')

@bp.app_errorhandler(403)
def forbidden_error(error):
    """403错误"""
    error_logger.warning(
        "403 Forbidden",
        url=request.url,
        method=request.method,
        remote_addr=request.remote_addr,
        user_agent=request.headers.get('User-Agent')
    )
    return error_response(403, '权限不足')

@bp.app_errorhandler(405)
def method_not_allowed_error(error):
    """405错误"""
    error_logger.warning(
        "405 Method Not Allowed",
        url=request.url,
        method=request.method,
        remote_addr=request.remote_addr,
        user_agent=request.headers.get('User-Agent')
    )
    return error_response(405, '请求方法不允许') 