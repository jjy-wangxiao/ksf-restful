
## �� API 接口

### 认证接口

| 方法 | 路径 | 描述 | 权限 |
|------|------|------|------|
| POST | `/api/v1/auth/login` | 用户登录 | 公开 |
| POST | `/api/v1/auth/refresh` | 刷新令牌 | 需要刷新令牌 |

### 用户接口

| 方法 | 路径 | 描述 | 权限 |
|------|------|------|------|
| GET | `/api/v1/users` | 获取用户列表 | 管理员 |
| POST | `/api/v1/users` | 创建用户 | 公开 |
| GET | `/api/v1/users/<id>` | 获取用户详情 | 登录用户 |
| PUT | `/api/v1/users/<id>` | 更新用户信息 | 本人或管理员 |
| DELETE | `/api/v1/users/<id>` | 删除用户 | 管理员 |

### 文章接口

| 方法 | 路径 | 描述 | 权限 |
|------|------|------|------|
| GET | `/api/v1/posts` | 获取文章列表 | 公开 |
| POST | `/api/v1/posts` | 创建文章 | 登录用户 |
| GET | `/api/v1/posts/<id>` | 获取文章详情 | 公开/作者 |
| PUT | `/api/v1/posts/<id>` | 更新文章 | 作者或管理员 |
| DELETE | `/api/v1/posts/<id>` | 删除文章 | 作者或管理员 |

### 请求示例

#### 用户登录
```bash
curl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "AdminPass123"
  }'
```

#### 创建文章
```bash
curl -X POST http://localhost:5000/api/v1/posts \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <access_token>" \
  -d '{
    "title": "我的第一篇文章",
    "content": "这是文章内容",
    "published": true
  }'
```

## ⚙️ 环境配置

### 环境变量

项目支持多环境配置，主要环境变量包括：

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `FLASK_CONFIG` | `development` | 应用环境 |
| `SECRET_KEY` | `dev-secret-key` | Flask 密钥 |
| `JWT_SECRET_KEY` | `jwt-secret-key` | JWT 密钥 |
| `DATABASE_URL` | `sqlite:///data.sqlite` | 生产数据库 |
| `DEV_DATABASE_URL` | `sqlite:///data-dev.sqlite` | 开发数据库 |
| `TEST_DATABASE_URL` | `sqlite:///:memory:` | 测试数据库 |
| `LOG_LEVEL` | `INFO` | 日志级别 |

### 配置环境

#### 开发环境
```bash
# .env 文件
FLASK_CONFIG=development
SECRET_KEY=your-dev-secret-key
JWT_SECRET_KEY=your-dev-jwt-secret-key
DEV_DATABASE_URL=sqlite:///data-dev.sqlite
LOG_LEVEL=DEBUG
```

#### 生产环境
```bash
# 环境变量
export FLASK_CONFIG=production
export SECRET_KEY=your-production-secret-key
export JWT_SECRET_KEY=your-production-jwt-secret-key
export DATABASE_URL=postgresql://user:pass@host:5432/db
export LOG_LEVEL=INFO
```

## �� 开发指南

### 代码规范

项目使用以下工具确保代码质量：

- **black** - 代码格式化
- **flake8** - 代码检查
- **mypy** - 类型检查
- **isort** - 导入排序

### 开发命令

```bash
# 代码格式化
python manage.py format-code

# 代码检查
python manage.py lint

# 类型检查
python manage.py type-check

# 运行测试
python manage.py test

# 生成测试数据
python manage.py generate-fake-data
```

### Git 工作流

项目使用 pre-commit 钩子确保代码质量：

```bash
# 安装 pre-commit 钩子
poetry run pre-commit install

# 手动运行检查
poetry run pre-commit run --all-files
```

## ➕ 新增模块指南

### 步骤概览

新增一个完整的模块需要以下步骤：

1. **创建数据模型** (app/models/)
2. **创建数据验证模式** (app/schemas/)
3. **创建 API 资源** (app/api/v1/resources/)
4. **注册 API 路由** (app/api/v1/__init__.py)
5. **创建测试文件** (tests/)
6. **更新文档**

### 详细步骤

#### 1. 创建数据模型

```python
# app/models/comment.py
from app import db
from datetime import datetime
import uuid

class Comment(db.Model):
    """评论模型"""
    __tablename__ = 'comments'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.String(36), db.ForeignKey('posts.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # 关系
    user = db.relationship('User', backref='comments')
    post = db.relationship('Post', backref='comments')
    
    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'user_id': self.user_id,
            'post_id': self.post_id,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
```

#### 2. 创建数据验证模式

```python
# app/schemas/comment.py
from marshmallow import Schema, fields, validate

class CommentSchema(Schema):
    """评论序列化模式"""
    id = fields.Str(dump_only=True)
    content = fields.Str(required=True, validate=validate.Length(min=1, max=1000))
    user_id = fields.Str(dump_only=True)
    post_id = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)

class CommentCreateSchema(Schema):
    """评论创建模式"""
    content = fields.Str(required=True, validate=validate.Length(min=1, max=1000))
    post_id = fields.Str(required=True)
```

#### 3. 创建 API 资源

```python
# app/api/v1/resources/comments.py
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.comment import Comment
from app.schemas.comment import CommentSchema, CommentCreateSchema
from app.utils.decorators import validate_json
from app.utils.pagination import paginate

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
comment_create_schema = CommentCreateSchema()

class CommentListResource(Resource):
    """评论列表资源"""
    
    def get(self):
        """获取评论列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        comments = Comment.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return paginate(comments, comments_schema)
    
    @jwt_required()
    @validate_json
    def post(self):
        """创建评论"""
        data = request.get_json()
        current_user_id = get_jwt_identity()
        
        # 验证数据
        errors = comment_create_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        comment = Comment(
            content=data['content'],
            post_id=data['post_id'],
            user_id=current_user_id
        )
        
        db.session.add(comment)
        db.session.commit()
        
        return {
            'message': '评论创建成功',
            'comment': comment_schema.dump(comment)
        }, 201

class CommentResource(Resource):
    """单个评论资源"""
    
    @jwt_required()
    def get(self, comment_id):
        """获取评论详情"""
        comment = Comment.query.get_or_404(comment_id)
        return {'comment': comment_schema.dump(comment)}
    
    @jwt_required()
    def delete(self, comment_id):
        """删除评论"""
        current_user_id = get_jwt_identity()
        comment = Comment.query.get_or_404(comment_id)
        
        # 只能删除自己的评论
        if comment.user_id != current_user_id:
            return {'message': '权限不足'}, 403
        
        db.session.delete(comment)
        db.session.commit()
        
        return {'message': '评论删除成功'}, 200
```

#### 4. 注册 API 路由

```python
# app/api/v1/__init__.py
# 添加导入
from app.api.v1.resources.comments import CommentListResource, CommentResource

# 添加路由
api.add_resource(CommentListResource, '/comments')
api.add_resource(CommentResource, '/comments/<string:comment_id>')
```

#### 5. 创建测试文件

```python
# tests/test_comments.py
import pytest
from app import create_app, db
from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def user(app):
    user = User(username='testuser', email='test@example.com')
    user.password = 'TestPass123'
    db.session.add(user)
    db.session.commit()
    return user

class TestCommentAPI:
    def test_create_comment(self, client, user):
        """测试创建评论"""
        # 先登录获取token
        login_response = client.post('/api/v1/auth/login', json={
            'username': 'testuser',
            'password': 'TestPass123'
        })
        token = login_response.get_json()['access_token']
        
        # 创建文章
        post_response = client.post('/api/v1/posts', json={
            'title': '测试文章',
            'content': '测试内容',
            'published': True
        }, headers={'Authorization': f'Bearer {token}'})
        post_id = post_response.get_json()['post']['id']
        
        # 创建评论
        response = client.post('/api/v1/comments', json={
            'content': '测试评论',
            'post_id': post_id
        }, headers={'Authorization': f'Bearer {token}'})
        
        assert response.status_code == 201
        data = response.get_json()
        assert data['message'] == '评论创建成功'
        assert data['comment']['content'] == '测试评论'
    
    def test_get_comments(self, client):
        """测试获取评论列表"""
        response = client.get('/api/v1/comments')
        assert response.status_code == 200
        data = response.get_json()
        assert 'items' in data
        assert 'pagination' in data
```

#### 6. 数据库迁移

```bash
# 生成迁移文件
flask db migrate -m "Add comments table"

# 应用迁移
flask db upgrade
```

### 检查清单

新增模块完成后，请检查以下项目：

- [ ] **数据模型**：创建 `app/models/xxx.py`
- [ ] **数据验证**：创建 `app/schemas/xxx.py`
- [ ] **API 资源**：创建 `app/api/v1/resources/xxx.py`
- [ ] **路由注册**：在 `app/api/v1/__init__.py` 中注册
- [ ] **测试文件**：创建 `tests/test_xxx.py`
- [ ] **数据库迁移**：运行 `flask db migrate` 和 `flask db upgrade`
- [ ] **权限检查**：确认权限控制正确
- [ ] **文档更新**：更新 API 文档

## 🚀 部署

### Docker 部署

#### 1. 构建镜像

```bash
docker build -t ksf-restful .
```

#### 2. 使用 Docker Compose

```bash
# 启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

#### 3. 生产环境配置

```yaml
# docker-compose.prod.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_CONFIG=production
      - DATABASE_URL=postgresql://user:pass@db:5432/ksf_restful
      - SECRET_KEY=your-production-secret-key
      - JWT_SECRET_KEY=your-production-jwt-secret-key
    depends_on:
      - db
    restart: unless-stopped
```

### 传统部署

#### 1. 服务器准备

```bash
# 安装 Python 3.12
sudo apt update
sudo apt install python3.12 python3.12-venv

# 安装 PostgreSQL
sudo apt install postgresql postgresql-contrib

# 安装 Redis（可选）
sudo apt install redis-server
```

#### 2. 应用部署

```bash
# 克隆项目
git clone <repository-url>
cd ksf-restful

# 创建虚拟环境
python3.12 -m venv venv
source venv/bin/activate

# 安装依赖
pip install poetry
poetry install --only main

# 配置环境变量
cp env.example .env
# 编辑 .env 文件

# 初始化数据库
python manage.py init-db
python manage.py create-admin

# 使用 Gunicorn 启动
gunicorn --bind 0.0.0.0:5000 --workers 4 run:app
```

## 🧪 测试

### 运行测试

```bash
# 运行所有测试
python manage.py test

# 运行特定测试文件
python manage.py test tests/test_auth.py

# 运行测试并生成覆盖率报告
poetry run pytest --cov=app --cov-report=html

# 运行特定测试类
poetry run pytest tests/test_api.py::TestAuthAPI
```

### 测试覆盖率

项目集成了测试覆盖率工具，可以生成详细的覆盖率报告：

```bash
# 生成覆盖率报告
poetry run pytest --cov=app --cov-report=html --cov-report=term-missing

# 查看 HTML 报告
open htmlcov/index.html
```

### 测试类型

- **单元测试**：测试单个函数或类
- **集成测试**：测试 API 接口
- **功能测试**：测试完整业务流程

## �� 贡献指南

### 开发流程

1. **Fork 项目**
2. **创建功能分支**：`git checkout -b feature/new-feature`
3. **提交更改**：`git commit -am 'Add new feature'`
4. **推送分支**：`git push origin feature/new-feature`
5. **创建 Pull Request**

### 代码规范

- 遵循 PEP 8 代码规范
- 使用 black 进行代码格式化
- 通过 flake8 代码检查
- 通过 mypy 类型检查
- 编写测试用例

### 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：
