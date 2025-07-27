"""
文件上传功能测试
"""
import pytest
import os
import tempfile
from io import BytesIO
from werkzeug.datastructures import FileStorage
from app import create_app, db
from app.models.models_13jt import File
from app.services.upload_service import UploadService
from app.dto.upload_dto import FileUploadRequestDTO


@pytest.fixture
def app():
    """创建测试应用"""
    app = create_app('testing')
    app.config['UPLOAD_FOLDER'] = tempfile.mkdtemp()
    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB for testing
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """创建测试客户端"""
    return app.test_client()


@pytest.fixture
def sample_file():
    """创建示例文件"""
    content = b"This is a test file content for upload testing."
    return FileStorage(
        stream=BytesIO(content),
        filename="test.txt",
        content_type="text/plain"
    )


class TestFileUpload:
    """文件上传测试类"""
    
    def test_upload_single_file_success(self, client, sample_file):
        """测试单个文件上传成功"""
        response = client.post(
            '/api/v1/upload/files',
            data={'file': (sample_file, 'test.txt')},
            content_type='multipart/form-data'
        )
        
        assert response.status_code == 201
        data = response.get_json()
        assert 'id' in data
        assert data['original_filename'] == 'test.txt'
        assert data['status'] == 'success'
    
    def test_upload_no_file(self, client):
        """测试没有文件的上传请求"""
        response = client.post('/api/v1/upload/files')
        assert response.status_code == 400
        data = response.get_json()
        assert data['code'] == 'NO_FILE'
    
    def test_upload_empty_filename(self, client):
        """测试空文件名的上传请求"""
        response = client.post(
            '/api/v1/upload/files',
            data={'file': (BytesIO(b''), '')},
            content_type='multipart/form-data'
        )
        assert response.status_code == 400
        data = response.get_json()
        assert data['code'] == 'NO_FILENAME'
    
    def test_upload_with_extra_data(self, client, sample_file):
        """测试带额外数据的上传请求"""
        response = client.post(
            '/api/v1/upload/files',
            data={
                'file': (sample_file, 'test.txt'),
                'fileType': 'document',
                'description': 'Test document',
                'category': 'test'
            },
            content_type='multipart/form-data'
        )
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['status'] == 'success'
    
    def test_get_file_list(self, client, sample_file):
        """测试获取文件列表"""
        # 先上传一个文件
        client.post(
            '/api/v1/upload/files',
            data={'file': (sample_file, 'test.txt')},
            content_type='multipart/form-data'
        )
        
        # 获取文件列表
        response = client.get('/api/v1/upload/files')
        assert response.status_code == 200
        data = response.get_json()
        assert 'data' in data
        assert 'meta' in data
        assert len(data['data']) >= 1
    
    def test_get_file_info(self, client, sample_file):
        """测试获取文件信息"""
        # 先上传一个文件
        upload_response = client.post(
            '/api/v1/upload/files',
            data={'file': (sample_file, 'test.txt')},
            content_type='multipart/form-data'
        )
        file_id = upload_response.get_json()['id']
        
        # 获取文件信息
        response = client.get(f'/api/v1/upload/files/{file_id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data['id'] == file_id
        assert data['filename'] == 'test.txt'  # 当前实现中filename就是原始文件名
    
    def test_get_nonexistent_file(self, client):
        """测试获取不存在的文件信息"""
        response = client.get('/api/v1/upload/files/99999')
        assert response.status_code == 404
        data = response.get_json()
        assert data['code'] == 'FILE_NOT_FOUND'
    
    def test_delete_file(self, client, sample_file):
        """测试删除文件"""
        # 先上传一个文件
        upload_response = client.post(
            '/api/v1/upload/files',
            data={'file': (sample_file, 'test.txt')},
            content_type='multipart/form-data'
        )
        file_id = upload_response.get_json()['id']
        
        # 删除文件
        response = client.delete(f'/api/v1/upload/files/{file_id}')
        assert response.status_code == 200
        
        # 验证文件已被删除
        get_response = client.get(f'/api/v1/upload/files/{file_id}')
        assert get_response.status_code == 404
    
    def test_download_file(self, client, sample_file):
        """测试文件下载"""
        # 先上传一个文件
        upload_response = client.post(
            '/api/v1/upload/files',
            data={'file': (sample_file, 'test.txt')},
            content_type='multipart/form-data'
        )
        file_id = upload_response.get_json()['id']
        
        # 下载文件
        response = client.get(f'/api/v1/upload/files/{file_id}/download')
        assert response.status_code == 200
        assert 'attachment; filename=' in response.headers['Content-Disposition']
    
    def test_batch_upload(self, client):
        """测试批量上传"""
        # 创建多个测试文件
        files = [
            ('file1.txt', b'Content of file 1'),
            ('file2.txt', b'Content of file 2'),
            ('file3.txt', b'Content of file 3')
        ]
        
        data = {}
        for filename, content in files:
            data['files'] = (BytesIO(content), filename)
        
        response = client.post(
            '/api/v1/upload/files/batch',
            data=data,
            content_type='multipart/form-data'
        )
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['success_count'] == 3
        assert data['failed_count'] == 0
        assert len(data['files']) == 3


class TestFileValidation:
    """文件验证测试类"""
    
    def test_invalid_file_extension(self, client):
        """测试无效文件扩展名"""
        content = b"Invalid file content"
        response = client.post(
            '/api/v1/upload/files',
            data={'file': (BytesIO(content), 'test.exe')},
            content_type='multipart/form-data'
        )
        
        assert response.status_code == 500  # 或者400，取决于实现
        data = response.get_json()
        assert '不支持' in data['details']
    
    def test_file_size_limit(self, client):
        """测试文件大小限制"""
        # 创建一个超过大小限制的文件内容
        large_content = b"x" * (11 * 1024 * 1024)  # 11MB
        
        response = client.post(
            '/api/v1/upload/files',
            data={'file': (BytesIO(large_content), 'large.txt')},
            content_type='multipart/form-data'
        )
        
        # 应该返回413或500错误
        assert response.status_code in [413, 500]


class TestFileDuplication:
    """文件重复上传测试类"""
    
    def test_duplicate_file_upload(self, client):
        """测试重复文件上传"""
        # 创建两个相同内容的文件
        content = b"This is a test file content for upload testing."
        file1 = FileStorage(
            stream=BytesIO(content),
            filename="test1.txt",
            content_type="text/plain"
        )
        file2 = FileStorage(
            stream=BytesIO(content),
            filename="test2.txt",
            content_type="text/plain"
        )
        
        # 第一次上传
        response1 = client.post(
            '/api/v1/upload/files',
            data={'file': (file1, 'test1.txt')},
            content_type='multipart/form-data'
        )
        assert response1.status_code == 201
        file_id1 = response1.get_json()['id']
        
        # 第二次上传相同内容的文件
        response2 = client.post(
            '/api/v1/upload/files',
            data={'file': (file2, 'test2.txt')},
            content_type='multipart/form-data'
        )
        assert response2.status_code == 201
        file_id2 = response2.get_json()['id']
        
        # 应该返回相同的文件ID（因为文件哈希相同）
        assert file_id1 == file_id2 


class TestUploadService:
    """文件上传服务测试类"""
    
    def setup_method(self):
        """测试前准备"""
        self.upload_service = UploadService()
        self.upload_service.db = Mock()
        self.upload_service.db.session = Mock()
        
        # 创建测试文件
        self.test_content = b"test file content"
        self.test_file = FileStorage(
            stream=BytesIO(self.test_content),
            filename="test.txt",
            content_type="text/plain"
        )
    
    def test_upload_single_file_success(self):
        """测试成功上传单个文件"""
        # Mock数据库查询 - 文件不存在
        self.upload_service.db.session.query.return_value.filter_by.return_value.first.return_value = None
        
        # Mock文件系统操作
        with patch('os.path.getsize', return_value=len(self.test_content)):
            with patch('os.makedirs'):
                with patch('builtins.open', create=True):
                    # 创建上传请求
                    upload_request = FileUploadRequestDTO(file=self.test_file)
                    
                    # 执行上传
                    result = self.upload_service.upload_single_file(upload_request)
                    
                    # 验证结果
                    assert result.filename == "test.txt"
                    assert result.file_size == len(self.test_content)
                    assert result.status == "success"
    
    def test_upload_single_file_already_exists(self):
        """测试上传已存在的文件"""
        # Mock已存在的文件
        existing_file = File(
            id=1,
            filename="test.txt",
            filesize=len(self.test_content),
            filetype="txt",
            hash="test_hash"
        )
        self.upload_service.db.session.query.return_value.filter_by.return_value.first.return_value = existing_file
        
        # 创建上传请求
        upload_request = FileUploadRequestDTO(file=self.test_file)
        
        # 验证抛出异常
        with pytest.raises(ValueError, match="文件已存在"):
            self.upload_service.upload_single_file(upload_request)
    
    def test_upload_single_file_invalid_extension(self):
        """测试上传不支持的文件类型"""
        # 创建不支持的文件类型
        invalid_file = FileStorage(
            stream=BytesIO(b"test"),
            filename="test.exe",
            content_type="application/octet-stream"
        )
        
        upload_request = FileUploadRequestDTO(file=invalid_file)
        
        # 验证抛出异常
        with pytest.raises(ValueError, match="不支持的文件类型"):
            self.upload_service.upload_single_file(upload_request)
    
    def test_upload_single_file_too_large(self):
        """测试上传过大的文件"""
        # Mock文件大小超过限制
        large_content = b"x" * (self.upload_service.max_file_size + 1)
        large_file = FileStorage(
            stream=BytesIO(large_content),
            filename="large.txt",
            content_type="text/plain"
        )
        
        upload_request = FileUploadRequestDTO(file=large_file)
        
        # 验证抛出异常
        with pytest.raises(ValueError, match="文件过大"):
            self.upload_service.upload_single_file(upload_request)
    
    def test_get_file_list_success(self):
        """测试获取文件列表成功"""
        # Mock分页结果
        mock_pagination = Mock()
        mock_pagination.items = []
        mock_pagination.total = 0
        mock_pagination.page = 1
        mock_pagination.per_page = 10
        mock_pagination.pages = 0
        mock_pagination.has_next = False
        mock_pagination.has_prev = False
        
        self.upload_service.db.session.query.return_value.filter.return_value.order_by.return_value.paginate.return_value = mock_pagination
        
        # 执行获取文件列表
        result = self.upload_service.get_file_list(page=1, per_page=10)
        
        # 验证结果
        assert result.data == []
        assert result.meta.total == 0
    
    def test_get_file_info_success(self):
        """测试获取文件信息成功"""
        # Mock文件
        mock_file = File(
            id=1,
            filename="test.txt",
            filesize=100,
            filetype="txt",
            hash="test_hash"
        )
        self.upload_service.db.session.query.return_value.get.return_value = mock_file
        
        # 执行获取文件信息
        result = self.upload_service.get_file_info(1)
        
        # 验证结果
        assert result.id == 1
        assert result.filename == "test.txt"
    
    def test_get_file_info_not_found(self):
        """测试获取不存在的文件信息"""
        # Mock文件不存在
        self.upload_service.db.session.query.return_value.get.return_value = None
        
        # 验证抛出异常
        with pytest.raises(FileNotFoundError, match="文件ID 1 不存在"):
            self.upload_service.get_file_info(1)
    
    def test_delete_file_success(self):
        """测试删除文件成功"""
        # Mock文件
        mock_file = File(
            id=1,
            filename="test.txt",
            filesize=100,
            filetype="txt",
            hash="test_hash"
        )
        self.upload_service.db.session.query.return_value.get.return_value = mock_file
        
        # Mock文件系统操作
        with patch('os.path.exists', return_value=True):
            with patch('os.remove'):
                # 执行删除
                self.upload_service.delete_file(1)
                
                # 验证数据库操作
                self.upload_service.db.session.delete.assert_called_once_with(mock_file)
                self.upload_service.db.session.commit.assert_called_once()
    
    def test_delete_file_not_found(self):
        """测试删除不存在的文件"""
        # Mock文件不存在
        self.upload_service.db.session.query.return_value.get.return_value = None
        
        # 验证抛出异常
        with pytest.raises(FileNotFoundError, match="文件ID 1 不存在"):
            self.upload_service.delete_file(1) 