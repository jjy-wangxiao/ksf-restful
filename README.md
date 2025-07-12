# KSF RESTful API

一个基于Flask-RESTful的完整REST API项目框架，包含用户认证、权限管理、数据验证等功能。

## 功能特性

- 🔐 JWT认证和授权
- 👥 用户管理系统
- 📝 文章管理系统
- 🔒 基于角色的权限控制
- 📊 数据验证和序列化
- 📄 分页支持
- 🧪 完整的测试框架
- 🐳 Docker支持
- 📝 API文档

## 项目结构

```
ksf-restful/
├── app/                    # 应用主目录
│   ├── __init__.py        # 应用工厂
│   ├── api/               # API相关
│   │   └── v1/           # API版本1
│   │       ├── __init__.py
│   │       └── resources/ # API资源
│   │           ├── auth.py
│   │           ├── users.py
│   │           └── posts.py
│   ├── models/            # 数据模型
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── post.py
│   ├── schemas/           # 数据验证模式
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── post.py
│   ├── utils/             # 工具函数
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   └── pagination.py
│   └── errors/            # 错误处理
│       ├── __init__.py
│       └── handlers.py
├── tests/                 # 测试文件
│   ├── __init__.py
│   └── test_api.py
├── config.py             # 配置文件
├── run.py               # 应用入口
├── manage.py            # 管理脚本
├── requirements.txt     # 依赖文件
├── Dockerfile          # Docker配置
├── docker-compose.yml  # Docker Compose配置
└── README.md           # 项目说明
```

## 快速开始

### 1. 安装依赖

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 初始化数据库

```bash
# 初始化数据库表
python manage.py init-db

# 创建管理员用户
python manage.py create-admin
```

### 3. 运行应用

```bash
# 开发模式
python run.py

# 或者使用Flask命令
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

### 4. 使用Docker

```bash
# 构建并启动服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

## API文档

### 认证

#### 用户登录
```
POST /api/v1/auth/login
Content-Type: application/json

{
    "username": "admin",
    "password": "password"
}
```

#### 刷新令牌
```
POST /api/v1/auth/refresh
Authorization: Bearer <refresh_token>
```

### 用户管理

#### 获取用户列表
```
GET /api/v1/users?page=1&per_page=10
Authorization: Bearer <access_token>
```

#### 创建用户
```
POST /api/v1/users
Content-Type: application/json

{
    "username": "newuser",
    "email": "user@example.com",
    "password": "Password123"
}
```

#### 获取用户详情
```
GET /api/v1/users/<user_id>
Authorization: Bearer <access_token>
```

#### 更新用户
```
PUT /api/v1/users/<user_id>
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "username": "updateduser",
    "email": "updated@example.com"
}
```

#### 删除用户
```
DELETE /api/v1/users/<user_id>
Authorization: Bearer <access_token>
```

### 文章管理

#### 获取文章列表
```
GET /api/v1/posts?page=1&per_page=10&published=true
```

#### 创建文章
```
POST /api/v1/posts
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "title": "文章标题",
    "content": "文章内容",
    "published": true
}
```

#### 获取文章详情
```
GET /api/v1/posts/<post_id>
```

#### 更新文章
```
PUT /api/v1/posts/<post_id>
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "title": "更新的标题",
    "content": "更新的内容",
    "published": false
}
```

#### 删除文章
```
DELETE /api/v1/posts/<post_id>
Authorization: Bearer <access_token>
```

## 管理命令

```bash
# 运行测试
python manage.py test

# 初始化数据库
python manage.py init-db

# 创建管理员用户
python manage.py create-admin

# 生成测试数据
python manage.py generate-fake-data
```

## 配置

项目支持三种环境配置：

- `development`: 开发环境
- `testing`: 测试环境
- `production`: 生产环境

通过环境变量 `FLASK_CONFIG` 设置：

```bash
export FLASK_CONFIG=production
```

## 测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_api.py

# 生成覆盖率报告
pytest --cov=app tests/
```

## 部署

### 使用Docker部署

```bash
# 构建镜像
docker build -t ksf-restful .

# 运行容器
docker run -d -p 5000:5000 --name ksf-restful ksf-restful
```

### 使用Docker Compose部署

```bash
# 启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 停止服务
docker-compose down
```

## 贡献

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式

如有问题或建议，请提交 Issue 或联系项目维护者。 