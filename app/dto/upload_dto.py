"""
文件上传DTO - 数据传输对象
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from werkzeug.datastructures import FileStorage


@dataclass
class FileUploadRequestDTO:
    """文件上传请求DTO"""
    file: FileStorage
    file_type: str = ''
    description: str = ''
    category: str = ''
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'file_type': self.file_type,
            'description': self.description,
            'category': self.category
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class FileUploadResponseDTO:
    """文件上传响应DTO"""
    id: int
    filename: str
    original_filename: str
    file_size: int
    file_type: str
    hash: str
    upload_time: datetime
    download_url: str
    status: str
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'filename': self.filename,
            'original_filename': self.original_filename,
            'file_size': self.file_size,
            'file_type': self.file_type,
            'hash': self.hash,
            'upload_time': self.upload_time.isoformat() if self.upload_time else None,
            'download_url': self.download_url,
            'status': self.status
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class FileListResponseDTO:
    """文件列表响应DTO"""
    id: int
    filename: str
    original_filename: str
    file_size: int
    file_type: str
    hash: str
    upload_time: datetime
    status: str
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'id': self.id,
            'filename': self.filename,
            'original_filename': self.original_filename,
            'file_size': self.file_size,
            'file_type': self.file_type,
            'hash': self.hash,
            'upload_time': self.upload_time.isoformat() if self.upload_time else None,
            'status': self.status
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class BatchUploadResponseDTO:
    """批量上传响应DTO"""
    success_count: int
    failed_count: int
    files: List[FileUploadResponseDTO]
    errors: List[str]
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'success_count': self.success_count,
            'failed_count': self.failed_count,
            'files': [file.to_dict() for file in self.files],
            'errors': self.errors
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


@dataclass
class ErrorResponse:
    """错误响应DTO"""
    code: str
    message: str
    details: Optional[str] = None
    timestamp: Optional[datetime] = None
    
    def to_dict(self):
        """转换为字典，用于JSON序列化"""
        return {
            'code': self.code,
            'message': self.message,
            'details': self.details,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }
    
    def __json__(self):
        """Flask-RESTX JSON序列化支持"""
        return self.to_dict()


class ErrorCode:
    """错误码常量"""
    NO_FILE = "NO_FILE"
    NO_FILENAME = "NO_FILENAME"
    UPLOAD_ERROR = "UPLOAD_ERROR"
    BATCH_UPLOAD_ERROR = "BATCH_UPLOAD_ERROR"
    FILE_NOT_FOUND = "FILE_NOT_FOUND"
    GET_FILE_ERROR = "GET_FILE_ERROR"
    DELETE_FILE_ERROR = "DELETE_FILE_ERROR"
    DOWNLOAD_ERROR = "DOWNLOAD_ERROR"
    LIST_ERROR = "LIST_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    FILE_ALREADY_EXISTS = "FILE_ALREADY_EXISTS"  # 新增：文件已存在错误码 