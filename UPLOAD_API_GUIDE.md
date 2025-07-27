# 文件上传API使用指南

## 概述

本项目提供了完整的文件上传API，专门用于接收Ant Design Upload组件上传的文档。API支持单个文件上传、批量上传、文件管理等功能。

## API端点

### 1. 单个文件上传

**POST** `/api/v1/upload/files`

上传单个文件，支持Ant Design Upload组件的标准格式。

#### 请求格式

```javascript
// 前端代码示例
const formData = new FormData();
formData.append('file', file);
formData.append('fileType', 'document');  // 可选
formData.append('description', '文件描述');  // 可选
formData.append('category', '文档');  // 可选

fetch('/api/v1/upload/files', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

#### 请求参数

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| file | File | 是 | 要上传的文件 |
| fileType | string | 否 | 文件类型标识 |
| description | string | 否 | 文件描述 |
| category | string | 否 | 文件分类 |

#### 响应格式

```json
{
  "id": 1,
  "filename": "abc123.txt",
  "original_filename": "test.txt",
  "file_size": 1024,
  "file_type": "txt",
  "hash": "d41d8cd98f00b204e9800998ecf8427e",
  "upload_time": "2024-01-01T12:00:00",
  "download_url": "/api/v1/upload/files/1/download",
  "status": "success"
}
```

### 2. 批量文件上传

**POST** `/api/v1/upload/files/batch`

批量上传多个文件，支持Ant Design Upload组件的multiple模式。

#### 请求格式

```javascript
// 前端代码示例
const formData = new FormData();
files.forEach(file => {
  formData.append('files', file);
});
formData.append('fileType', 'document');
formData.append('description', '批量上传');
formData.append('category', '文档');

fetch('/api/v1/upload/files/batch', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

#### 响应格式

```json
{
  "success_count": 3,
  "failed_count": 0,
  "files": [
    {
      "id": 1,
      "filename": "abc123.txt",
      "original_filename": "file1.txt",
      "file_size": 1024,
      "file_type": "txt",
      "hash": "d41d8cd98f00b204e9800998ecf8427e",
      "upload_time": "2024-01-01T12:00:00",
      "download_url": "/api/v1/upload/files/1/download",
      "status": "success"
    }
  ],
  "errors": []
}
```

### 3. 获取文件列表

**GET** `/api/v1/upload/files`

获取已上传文件的列表，支持分页和过滤。

#### 请求参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| page | int | 1 | 页码 |
| per_page | int | 10 | 每页数量 |
| file_type | string | - | 文件类型过滤 |
| category | string | - | 文件分类过滤 |

#### 响应格式

```json
{
  "data": [
    {
      "id": 1,
      "filename": "abc123.txt",
      "original_filename": "test.txt",
      "file_size": 1024,
      "file_type": "txt",
      "hash": "d41d8cd98f00b204e9800998ecf8427e",
      "upload_time": "2024-01-01T12:00:00",
      "status": "active"
    }
  ],
  "meta": {
    "page": 1,
    "per_page": 10,
    "total": 1,
    "pages": 1,
    "has_next": false,
    "has_prev": false
  }
}
```

### 4. 获取文件信息

**GET** `/api/v1/upload/files/{file_id}`

获取指定文件的详细信息。

#### 响应格式

```json
{
  "id": 1,
  "filename": "abc123.txt",
  "original_filename": "test.txt",
  "file_size": 1024,
  "file_type": "txt",
  "hash": "d41d8cd98f00b204e9800998ecf8427e",
  "upload_time": "2024-01-01T12:00:00",
  "status": "active"
}
```

### 5. 删除文件

**DELETE** `/api/v1/upload/files/{file_id}`

删除指定的文件。

#### 响应格式

```json
{
  "message": "文件删除成功"
}
```

### 6. 下载文件

**GET** `/api/v1/upload/files/{file_id}/download`

下载指定的文件。

#### 响应

返回文件流，浏览器会自动下载文件。

## Ant Design Upload组件集成

### 基本用法

```jsx
import { Upload, Button, message } from 'antd';
import { UploadOutlined } from '@ant-design/icons';

const FileUpload = () => {
  const [fileList, setFileList] = useState([]);
  const [uploading, setUploading] = useState(false);

  const handleUpload = () => {
    const formData = new FormData();
    fileList.forEach(file => {
      formData.append('file', file);
    });

    setUploading(true);

    fetch('/api/v1/upload/files', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      setFileList([]);
      message.success('上传成功');
    })
    .catch(() => {
      message.error('上传失败');
    })
    .finally(() => {
      setUploading(false);
    });
  };

  const props = {
    onRemove: file => {
      const index = fileList.indexOf(file);
      const newFileList = fileList.slice();
      newFileList.splice(index, 1);
      setFileList(newFileList);
    },
    beforeUpload: file => {
      setFileList([...fileList, file]);
      return false;
    },
    fileList,
  };

  return (
    <>
      <Upload {...props}>
        <Button icon={<UploadOutlined />}>选择文件</Button>
      </Upload>
      <Button
        type="primary"
        onClick={handleUpload}
        disabled={fileList.length === 0}
        loading={uploading}
        style={{ marginTop: 16 }}
      >
        {uploading ? '上传中' : '开始上传'}
      </Button>
    </>
  );
};
```

### 自动上传

```jsx
import { Upload, message } from 'antd';
import { InboxOutlined } from '@ant-design/icons';

const { Dragger } = Upload;

const AutoUpload = () => {
  const props = {
    name: 'file',
    multiple: true,
    action: '/api/v1/upload/files',
    onChange(info) {
      const { status } = info.file;
      if (status !== 'uploading') {
        console.log(info.file, info.fileList);
      }
      if (status === 'done') {
        message.success(`${info.file.name} 文件上传成功`);
      } else if (status === 'error') {
        message.error(`${info.file.name} 文件上传失败`);
      }
    },
    onDrop(e) {
      console.log('Dropped files', e.dataTransfer.files);
    },
  };

  return (
    <Dragger {...props}>
      <p className="ant-upload-drag-icon">
        <InboxOutlined />
      </p>
      <p className="ant-upload-text">点击或拖拽文件到此区域上传</p>
      <p className="ant-upload-hint">
        支持单个或批量上传，严禁上传公司数据或其他敏感文件
      </p>
    </Dragger>
  );
};
```

### 批量上传

```jsx
import { Upload, Button, message } from 'antd';
import { UploadOutlined } from '@ant-design/icons';

const BatchUpload = () => {
  const [fileList, setFileList] = useState([]);
  const [uploading, setUploading] = useState(false);

  const handleBatchUpload = () => {
    const formData = new FormData();
    fileList.forEach(file => {
      formData.append('files', file);
    });

    setUploading(true);

    fetch('/api/v1/upload/files/batch', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      if (data.success_count > 0) {
        message.success(`成功上传 ${data.success_count} 个文件`);
      }
      if (data.failed_count > 0) {
        message.error(`失败 ${data.failed_count} 个文件`);
      }
      setFileList([]);
    })
    .catch(() => {
      message.error('批量上传失败');
    })
    .finally(() => {
      setUploading(false);
    });
  };

  const props = {
    multiple: true,
    onRemove: file => {
      const index = fileList.indexOf(file);
      const newFileList = fileList.slice();
      newFileList.splice(index, 1);
      setFileList(newFileList);
    },
    beforeUpload: file => {
      setFileList([...fileList, file]);
      return false;
    },
    fileList,
  };

  return (
    <>
      <Upload {...props}>
        <Button icon={<UploadOutlined />}>选择多个文件</Button>
      </Upload>
      <Button
        type="primary"
        onClick={handleBatchUpload}
        disabled={fileList.length === 0}
        loading={uploading}
        style={{ marginTop: 16 }}
      >
        {uploading ? '上传中' : '批量上传'}
      </Button>
    </>
  );
};
```

## 配置说明

### 环境变量

在 `.env` 文件中配置以下参数：

```bash
# 文件上传配置
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=52428800
```

### 支持的文件类型

默认支持以下文件类型：
- 文本文件：txt
- 文档文件：pdf, doc, docx
- 图片文件：png, jpg, jpeg, gif
- 表格文件：xls, xlsx
- 演示文件：ppt, pptx
- 压缩文件：zip, rar, 7z

### 文件大小限制

默认最大文件大小为 50MB，可通过 `MAX_CONTENT_LENGTH` 环境变量调整。

## 错误处理

### 常见错误码

| 错误码 | 说明 | HTTP状态码 |
|--------|------|------------|
| NO_FILE | 没有选择文件 | 400 |
| NO_FILENAME | 文件名为空 | 400 |
| UPLOAD_ERROR | 文件上传失败 | 500 |
| FILE_NOT_FOUND | 文件不存在 | 404 |
| VALIDATION_ERROR | 文件验证失败 | 400 |

### 错误响应格式

```json
{
  "code": "UPLOAD_ERROR",
  "message": "文件上传失败",
  "details": "具体错误信息",
  "timestamp": "2024-01-01T12:00:00"
}
```

## 安全特性

1. **文件类型验证**：只允许上传指定类型的文件
2. **文件大小限制**：防止上传过大的文件
3. **文件名安全化**：使用 `secure_filename` 处理文件名
4. **文件哈希去重**：相同内容的文件只存储一份
5. **路径遍历防护**：防止恶意文件路径

## 性能优化

1. **文件去重**：通过MD5哈希避免重复存储
2. **分页查询**：文件列表支持分页
3. **异步处理**：支持批量上传的异步处理
4. **缓存机制**：文件信息缓存优化

## 测试

运行测试命令：

```bash
# 运行所有测试
pytest tests/test_upload.py

# 运行特定测试
pytest tests/test_upload.py::TestFileUpload::test_upload_single_file_success
```

## 部署注意事项

1. **存储目录权限**：确保上传目录有正确的读写权限
2. **磁盘空间**：监控上传目录的磁盘使用情况
3. **备份策略**：定期备份重要的上传文件
4. **CDN配置**：生产环境建议使用CDN加速文件下载 