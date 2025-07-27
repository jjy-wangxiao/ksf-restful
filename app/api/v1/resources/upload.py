"""
文件上传API资源 - 处理Ant Design Upload组件的文件上传
"""
import os
import hashlib
from werkzeug.utils import secure_filename
from flask import request, current_app
from flask_restx import Resource, fields
from app.services.upload_service import UploadService
from app.dto.upload_dto import (
    FileUploadRequestDTO, FileUploadResponseDTO, FileListResponseDTO,
    ErrorResponse, ErrorCode
)
from app.swagger import api
from app.utils.decorators import paginated_response
from app.utils.logger import get_logger

# 创建文件上传命名空间
upload_ns = api.namespace('upload', description='文件上传接口')

# 获取日志记录器
logger = get_logger('app.api.upload')

# ==================== OpenAPI 模型定义 ====================

# 错误响应模型
error_model = api.model('Error', {
    'code': fields.String(required=True, description='错误码'),
    'message': fields.String(required=True, description='错误信息'),
    'details': fields.Raw(description='详细信息'),
    'timestamp': fields.DateTime(description='时间戳')
})

# 文件上传响应模型
file_upload_response_model = api.model('FileUploadResponse', {
    'id': fields.Integer(required=True, description='文件ID'),
    'filename': fields.String(required=True, description='文件名'),
    'original_filename': fields.String(required=True, description='原始文件名'),
    'file_size': fields.Integer(required=True, description='文件大小(字节)'),
    'file_type': fields.String(required=True, description='文件类型'),
    'hash': fields.String(required=True, description='文件哈希值'),
    'upload_time': fields.DateTime(required=True, description='上传时间'),
    'download_url': fields.String(description='下载链接'),
    'status': fields.String(required=True, description='上传状态')
})

# 文件列表模型
file_list_model = api.model('FileList', {
    'id': fields.Integer(required=True, description='文件ID'),
    'filename': fields.String(required=True, description='文件名'),
    'original_filename': fields.String(required=True, description='原始文件名'),
    'file_size': fields.Integer(required=True, description='文件大小(字节)'),
    'file_type': fields.String(required=True, description='文件类型'),
    'hash': fields.String(required=True, description='文件哈希值'),
    'upload_time': fields.DateTime(required=True, description='上传时间'),
    'status': fields.String(required=True, description='文件状态')
})

# 分页元数据模型
pagination_meta_model = api.model('PaginationMeta', {
    'page': fields.Integer(description='当前页码'),
    'per_page': fields.Integer(description='每页数量'),
    'total': fields.Integer(description='总记录数'),
    'pages': fields.Integer(description='总页数'),
    'has_next': fields.Boolean(description='是否有下一页'),
    'has_prev': fields.Boolean(description='是否有上一页')
})

# 文件列表分页响应模型
file_list_pagination_response = api.model('FileListPaginationResponse', {
    'data': fields.List(fields.Nested(file_list_model), description='文件列表'),
    'meta': fields.Nested(pagination_meta_model, description='分页信息')
})

# 批量上传响应模型
batch_upload_response_model = api.model('BatchUploadResponse', {
    'success_count': fields.Integer(required=True, description='成功上传数量'),
    'failed_count': fields.Integer(required=True, description='失败数量'),
    'files': fields.List(fields.Nested(file_upload_response_model), description='上传结果列表'),
    'errors': fields.List(fields.String, description='错误信息列表')
})

@upload_ns.route('/files')
class FileUploadResource(Resource):
    """文件上传资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.upload_service = UploadService()
    
    @upload_ns.doc('上传单个文件')
    @upload_ns.response(201, '上传成功', file_upload_response_model)
    @upload_ns.response(400, '请求错误', error_model)
    @upload_ns.response(409, '文件已存在', error_model)
    @upload_ns.response(413, '文件过大', error_model)
    def post(self):
        """上传单个文件 - 支持Ant Design Upload组件"""
        try:
            # 检查是否有文件
            if 'file' not in request.files:
                return {
                    'code': 'NO_FILE',
                    'message': '没有选择文件',
                    'details': '请选择要上传的文件'
                }, 400
            
            file = request.files['file']
            
            # 检查文件名
            if file.filename == '':
                return {
                    'code': 'NO_FILENAME',
                    'message': '文件名为空',
                    'details': '请选择有效的文件'
                }, 400
            
            # 获取额外的表单数据（Ant Design Upload可能传递的）
            file_type = request.form.get('fileType', '')
            description = request.form.get('description', '')
            category = request.form.get('category', '')
            
            # 创建上传请求DTO
            upload_request = FileUploadRequestDTO(
                file=file,
                file_type=file_type,
                description=description,
                category=category
            )
            
            # 调用服务层处理上传
            result = self.upload_service.upload_single_file(upload_request)
            
            logger.info("File uploaded successfully", 
                       filename=result.filename, 
                       file_id=result.id,
                       file_size=result.file_size)
            
            return result.to_dict(), 201
            
        except ValueError as e:
            # 处理文件已存在等验证错误
            if "文件已存在" in str(e):
                logger.warning("File already exists", error=str(e), filename=file.filename if 'file' in locals() else 'unknown')
                return {
                    'code': 'FILE_ALREADY_EXISTS',
                    'message': '文件已存在',
                    'details': str(e)
                }, 409
            else:
                logger.error("File validation failed", error=str(e), filename=file.filename if 'file' in locals() else 'unknown')
                return {
                    'code': 'VALIDATION_ERROR',
                    'message': '文件验证失败',
                    'details': str(e)
                }, 400
        except Exception as e:
            logger.error("File upload failed", error=str(e), filename=file.filename if 'file' in locals() else 'unknown')
            return {
                'code': 'UPLOAD_ERROR',
                'message': '文件上传失败',
                'details': str(e)
            }, 500
    
    @upload_ns.doc('获取文件列表')
    @upload_ns.param('page', '页码', type=int, default=1)
    @upload_ns.param('per_page', '每页数量', type=int, default=10)
    @upload_ns.param('file_type', '文件类型过滤', type=str)
    @upload_ns.param('category', '文件分类过滤', type=str)
    @upload_ns.response(200, '获取成功', file_list_pagination_response)
    @paginated_response
    def get(self):
        """获取文件列表"""
        try:
            page = request.args.get('page', 1, type=int)
            per_page = request.args.get('per_page', 10, type=int)
            file_type = request.args.get('file_type', '')
            category = request.args.get('category', '')
            
            result = self.upload_service.get_file_list(
                page=page, 
                per_page=per_page,
                file_type=file_type,
                category=category
            )
            
            return result, 200
            
        except Exception as e:
            logger.error("Failed to get file list", error=str(e))
            return {
                'code': 'LIST_ERROR',
                'message': '获取文件列表失败',
                'details': str(e)
            }, 500

@upload_ns.route('/files/batch')
class BatchUploadResource(Resource):
    """批量文件上传资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.upload_service = UploadService()
    
    @upload_ns.doc('批量上传文件')
    @upload_ns.response(201, '批量上传完成', batch_upload_response_model)
    @upload_ns.response(400, '请求错误', error_model)
    def post(self):
        """批量上传文件 - 支持Ant Design Upload组件的multiple模式"""
        try:
            files = request.files.getlist('files')
            
            if not files or all(f.filename == '' for f in files):
                return {
                    'code': 'NO_FILES',
                    'message': '没有选择文件',
                    'details': '请选择要上传的文件'
                }, 400
            
            # 获取额外的表单数据
            file_type = request.form.get('fileType', '')
            description = request.form.get('description', '')
            category = request.form.get('category', '')
            
            # 调用服务层处理批量上传
            result = self.upload_service.upload_multiple_files(
                files=files,
                file_type=file_type,
                description=description,
                category=category
            )
            
            logger.info("Batch upload completed", 
                       success_count=result.success_count,
                       failed_count=result.failed_count)
            
            return result.to_dict(), 201
            
        except Exception as e:
            logger.error("Batch upload failed", error=str(e))
            return {
                'code': 'BATCH_UPLOAD_ERROR',
                'message': '批量上传失败',
                'details': str(e)
            }, 500

@upload_ns.route('/files/<int:file_id>')
@upload_ns.param('file_id', '文件ID')
class FileResource(Resource):
    """单个文件资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.upload_service = UploadService()
    
    @upload_ns.doc('获取文件信息')
    @upload_ns.response(200, '获取成功', file_list_model)
    @upload_ns.response(404, '文件不存在', error_model)
    def get(self, file_id):
        """获取文件信息"""
        try:
            file_info = self.upload_service.get_file_info(file_id)
            return file_info.to_dict(), 200
            
        except FileNotFoundError:
            return {
                'code': 'FILE_NOT_FOUND',
                'message': '文件不存在',
                'details': f'文件ID {file_id} 不存在'
            }, 404
        except Exception as e:
            logger.error("Failed to get file info", file_id=file_id, error=str(e))
            return {
                'code': 'GET_FILE_ERROR',
                'message': '获取文件信息失败',
                'details': str(e)
            }, 500
    
    @upload_ns.doc('删除文件')
    @upload_ns.response(200, '删除成功')
    @upload_ns.response(400, '文件不存在', error_model)
    def delete(self, file_id):
        """删除文件"""
        try:
            self.upload_service.delete_file(file_id)
            
            logger.info("File deleted successfully", file_id=file_id)
            return {'message': '文件删除成功'}, 200
            
        except FileNotFoundError:
            return {
                'code': 'FILE_NOT_FOUND',
                'message': '文件不存在',
                'details': f'文件ID {file_id} 不存在'
            }, 400
        except Exception as e:
            logger.error("Failed to delete file", file_id=file_id, error=str(e))
            return {
                'code': 'DELETE_FILE_ERROR',
                'message': '删除文件失败',
                'details': str(e)
            }, 500

@upload_ns.route('/files/<int:file_id>/download')
@upload_ns.param('file_id', '文件ID')
class FileDownloadResource(Resource):
    """文件下载资源"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.upload_service = UploadService()
    
    @upload_ns.doc('下载文件')
    @upload_ns.response(200, '下载成功')
    @upload_ns.response(404, '文件不存在', error_model)
    def get(self, file_id):
        """下载文件"""
        try:
            return self.upload_service.download_file(file_id)
            
        except FileNotFoundError:
            return {
                'code': 'FILE_NOT_FOUND',
                'message': '文件不存在',
                'details': f'文件ID {file_id} 不存在'
            }, 404
        except Exception as e:
            logger.error("Failed to download file", file_id=file_id, error=str(e))
            return {
                'code': 'DOWNLOAD_ERROR',
                'message': '文件下载失败',
                'details': str(e)
            }, 500 
        
