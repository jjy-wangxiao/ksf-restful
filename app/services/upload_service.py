"""
文件上传服务层 - 处理文件上传的业务逻辑
"""
import os
import hashlib
import mimetypes
from datetime import datetime
from typing import List, Optional
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from flask import current_app, send_file
from app.models.models_13jt import File
from app.services.base_service import BaseService
from app.dto.upload_dto import (
    FileUploadRequestDTO, FileUploadResponseDTO, FileListResponseDTO,
    BatchUploadResponseDTO
)
from app.dto.common import PaginatedResponse, PaginationMeta
from app.utils.response_builder import ResponseBuilder


class UploadService(BaseService):
    """文件上传服务类"""
    
    def __init__(self):
        super().__init__()
        from app import db
        self.db = db
        self.allowed_extensions = {
            'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 
            'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7z'
        }
        self.max_file_size = 50 * 1024 * 1024  # 50MB
    
    def upload_single_file(self, upload_request: FileUploadRequestDTO) -> FileUploadResponseDTO:
        """
        上传单个文件
        
        Args:
            upload_request: 上传请求DTO
            
        Returns:
            FileUploadResponseDTO: 上传响应DTO
        """
        self.log_service_call("upload_single_file", filename=upload_request.file.filename)
        
        try:
            file = upload_request.file
            
            # 验证文件
            self._validate_file(file)
            
            # 生成安全的文件名
            original_filename = secure_filename(file.filename)
            file_extension = self._get_file_extension(original_filename)
            
            # 计算文件哈希
            file_hash = self._calculate_file_hash(file)
            
            # 检查文件是否已存在
            existing_file = File.query.filter_by(hash=file_hash).first()
            if existing_file:
                self.log_service_result("upload_single_file", "File already exists", file_id=existing_file.id)
                raise ValueError(f"文件已存在，文件ID: {existing_file.id}, 文件名: {existing_file.filename}")
            
            # 生成存储文件名
            storage_filename = f"{file_hash}{file_extension}"
            
            # 确保上传目录存在
            upload_dir = self._get_upload_directory()
            os.makedirs(upload_dir, exist_ok=True)
            
            # 保存文件
            file_path = os.path.join(upload_dir, storage_filename)
            file.save(file_path)
            
            # 获取文件大小
            file_size = os.path.getsize(file_path)
            
            # 创建数据库记录
            db_file = File(
                hash=file_hash,
                filename=original_filename,  # 存储原始文件名
                filesize=file_size,
                filetype=file_extension.lstrip('.')
            )
            
            self.db.session.add(db_file)
            self.db.session.commit()
            
            # 创建响应DTO
            result = self._create_upload_response(db_file, original_filename)
            
            self.log_service_result("upload_single_file", result, file_id=db_file.id)
            return result
            
        except Exception as e:
            self.db.session.rollback()
            self.log_error(e, {"method": "upload_single_file", "filename": upload_request.file.filename})
            raise
    
    def upload_multiple_files(self, files: List[FileStorage], 
                            file_type: str = '', description: str = '', 
                            category: str = '') -> BatchUploadResponseDTO:
        """
        批量上传文件
        
        Args:
            files: 文件列表
            file_type: 文件类型
            description: 文件描述
            category: 文件分类
            
        Returns:
            BatchUploadResponseDTO: 批量上传响应DTO
        """
        self.log_service_call("upload_multiple_files", file_count=len(files))
        
        uploaded_files = []
        errors = []
        success_count = 0
        failed_count = 0
        
        for file in files:
            try:
                # 创建上传请求DTO
                upload_request = FileUploadRequestDTO(
                    file=file,
                    file_type=file_type,
                    description=description,
                    category=category
                )
                
                # 上传单个文件
                result = self.upload_single_file(upload_request)
                uploaded_files.append(result)
                success_count += 1
                
            except Exception as e:
                # 为文件已存在的情况提供更明确的错误信息
                if "文件已存在" in str(e):
                    error_msg = f"文件 {file.filename} 已存在: {str(e)}"
                else:
                    error_msg = f"文件 {file.filename} 上传失败: {str(e)}"
                errors.append(error_msg)
                failed_count += 1
                self.logger.error("File upload failed in batch", 
                                filename=file.filename, error=str(e))
        
        result = BatchUploadResponseDTO(
            success_count=success_count,
            failed_count=failed_count,
            files=uploaded_files,
            errors=errors
        )
        
        self.log_service_result("upload_multiple_files", result, 
                               success_count=success_count, failed_count=failed_count)
        return result
    
    def get_file_list(self, page: int = 1, per_page: int = 10,
                     file_type: str = '', category: str = '') -> PaginatedResponse[FileListResponseDTO]:
        """
        获取文件列表
        
        Args:
            page: 页码
            per_page: 每页数量
            file_type: 文件类型过滤
            category: 文件分类过滤
            
        Returns:
            PaginatedResponse[FileListResponseDTO]: 分页响应
        """
        self.log_service_call("get_file_list", page=page, per_page=per_page)
        
        try:
            # 构建查询
            query = File.query
            
            # 应用过滤条件
            if file_type:
                query = query.filter(File.filetype == file_type)
            
            # 按创建时间倒序排列
            query = query.order_by(File.create_time.desc())
            
            # 分页
            pagination = query.paginate(
                page=page, per_page=per_page, error_out=False
            )
            
            # 转换为DTO
            file_list_dto = [
                FileListResponseDTO(
                    id=file.id,
                    filename=file.filename,
                    original_filename=file.filename,  # 这里可以根据需要调整
                    file_size=file.filesize or 0,
                    file_type=file.filetype or '',
                    hash=file.hash,
                    upload_time=file.create_time,
                    status='active'
                )
                for file in pagination.items
            ]
            
            # 使用响应构建器创建分页响应
            result = ResponseBuilder.from_pagination(pagination, file_list_dto)
            
            self.log_service_result("get_file_list", result, total_count=pagination.total)
            return result
            
        except Exception as e:
            self.log_error(e, {"method": "get_file_list", "page": page, "per_page": per_page})
            raise
    
    def get_file_info(self, file_id: int) -> FileListResponseDTO:
        """
        获取文件信息
        
        Args:
            file_id: 文件ID
            
        Returns:
            FileListResponseDTO: 文件信息DTO
        """
        self.log_service_call("get_file_info", file_id=file_id)
        
        try:
            file = File.query.get(file_id)
            if not file:
                raise FileNotFoundError(f"文件ID {file_id} 不存在")
            
            result = FileListResponseDTO(
                id=file.id,
                filename=file.filename,
                original_filename=file.filename,
                file_size=file.filesize or 0,
                file_type=file.filetype or '',
                hash=file.hash,
                upload_time=file.create_time,
                status='active'
            )
            
            self.log_service_result("get_file_info", result)
            return result
            
        except FileNotFoundError:
            raise
        except Exception as e:
            self.log_error(e, {"method": "get_file_info", "file_id": file_id})
            raise
    
    def delete_file(self, file_id: int) -> None:
        """
        删除文件
        
        Args:
            file_id: 文件ID
        """
        self.log_service_call("delete_file", file_id=file_id)
        
        try:
            file = File.query.get(file_id)
            if not file:
                raise FileNotFoundError(f"文件ID {file_id} 不存在")
            
            # 删除物理文件
            file_path = self._get_file_path(file.filename)
            if os.path.exists(file_path):
                os.remove(file_path)
            
            # 删除数据库记录
            self.db.session.delete(file)
            self.db.session.commit()
            
            self.log_service_result("delete_file", "File deleted successfully")
            
        except FileNotFoundError:
            raise
        except Exception as e:
            self.db.session.rollback()
            self.log_error(e, {"method": "delete_file", "file_id": file_id})
            raise
    
    def download_file(self, file_id: int):
        """
        下载文件
        
        Args:
            file_id: 文件ID
            
        Returns:
            Flask响应对象
        """
        self.log_service_call("download_file", file_id=file_id)
        
        try:
            file = File.query.get(file_id)
            if not file:
                raise FileNotFoundError(f"文件ID {file_id} 不存在")
            
            file_path = self._get_file_path(file.filename)
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"文件 {file.filename} 不存在于磁盘")
            
            # 返回文件下载响应
            return send_file(
                file_path,
                as_attachment=True,
                download_name=file.filename,
                mimetype=self._get_mime_type(file.filename)
            )
            
        except FileNotFoundError:
            raise
        except Exception as e:
            self.log_error(e, {"method": "download_file", "file_id": file_id})
            raise
    
    def _validate_file(self, file: FileStorage) -> None:
        """验证文件"""
        # 检查文件扩展名
        if not self._allowed_file(file.filename):
            raise ValueError(f"不支持的文件类型: {file.filename}")
        
        # 检查文件大小
        file.seek(0, 2)  # 移动到文件末尾
        file_size = file.tell()
        file.seek(0)  # 重置到文件开头
        
        if file_size > self.max_file_size:
            raise ValueError(f"文件过大: {file_size} bytes (最大允许: {self.max_file_size} bytes)")
    
    def _allowed_file(self, filename: str) -> bool:
        """检查文件扩展名是否允许"""
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self.allowed_extensions
    
    def _get_file_extension(self, filename: str) -> str:
        """获取文件扩展名"""
        if '.' in filename:
            return '.' + filename.rsplit('.', 1)[1].lower()
        return ''
    
    def _calculate_file_hash(self, file: FileStorage) -> str:
        """计算文件哈希值"""
        file.seek(0)
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
        file.seek(0)
        return hash_md5.hexdigest()
    
    def _get_upload_directory(self) -> str:
        """获取上传目录"""
        upload_dir = current_app.config.get('UPLOAD_FOLDER', 'uploads')
        if not os.path.isabs(upload_dir):
            upload_dir = os.path.join(current_app.root_path, '..', upload_dir)
        return upload_dir
    
    def _get_file_path(self, filename: str) -> str:
        """获取文件完整路径"""
        upload_dir = self._get_upload_directory()
        return os.path.join(upload_dir, filename)
    
    def _get_mime_type(self, filename: str) -> str:
        """获取文件的MIME类型"""
        mime_type, _ = mimetypes.guess_type(filename)
        return mime_type or 'application/octet-stream'
    
    def _create_upload_response(self, db_file: File, original_filename: str) -> FileUploadResponseDTO:
        """创建上传响应DTO"""
        return FileUploadResponseDTO(
            id=db_file.id,
            filename=db_file.filename,
            original_filename=original_filename,
            file_size=db_file.filesize or 0,
            file_type=db_file.filetype or '',
            hash=db_file.hash,
            upload_time=db_file.create_time,
            download_url=f"/api/v1/upload/files/{db_file.id}/download",
            status='success'
        ) 