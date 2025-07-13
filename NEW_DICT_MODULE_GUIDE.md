# 新字典模块开发指南

## 概述

本文档详细说明如何在Flask-RESTX项目中添加一个新的字典模块进行CRUD操作。项目采用分层架构，包含Model、DTO、Service、API Resource等层次。

## 项目架构

```
app/
├── models/          # 数据模型层 (Entity)
├── dto/            # 数据传输对象层
├── services/       # 业务逻辑层
├── api/v1/resources/ # API控制器层
└── schemas/        # 数据验证层
```

## 开发步骤

### 第一步：定义数据模型 (Model)

在 `app/models/` 目录下创建或修改模型文件：

```python
# app/models/your_module.py
from app.models import db
from datetime import datetime

class YourModule(db.Model):
    __tablename__ = 'your_module'
    
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'create_time': self.create_time.isoformat() if self.create_time else None,
            'update_time': self.update_time.isoformat() if self.update_time else None
        }
```

### 第二步：创建DTO (Data Transfer Object)

在 `app/dto/` 目录下创建或修改DTO文件：

```python
# app/dto/your_module.py
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from app.dto import BaseDTO, PaginatedResponse

@dataclass
class YourModuleRequestDTO(BaseDTO):
    """创建请求DTO"""
    id: str
    name: str
    description: Optional[str] = None
    status: bool = True

@dataclass
class YourModuleUpdateRequestDTO(BaseDTO):
    """更新请求DTO"""
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None

@dataclass
class YourModuleResponseDTO(BaseDTO):
    """响应DTO"""
    id: str
    name: str
    description: Optional[str]
    status: bool
    create_time: Optional[datetime]
    update_time: Optional[datetime]

@dataclass
class YourModulePaginatedResponse(PaginatedResponse):
    """分页响应DTO"""
    data: List[YourModuleResponseDTO]
```

### 第三步：实现业务逻辑 (Service)

在 `app/services/` 目录下创建或修改服务文件：

```python
# app/services/your_module_service.py
from typing import List, Optional, Tuple
from app.models.your_module import YourModule
from app.dto.your_module import (
    YourModuleRequestDTO, 
    YourModuleUpdateRequestDTO, 
    YourModuleResponseDTO,
    YourModulePaginatedResponse
)
from app.services.base_service import BaseService
from app.utils.response_builder import ResponseBuilder
from app.utils.pagination import PaginationMeta

class YourModuleService(BaseService):
    def __init__(self):
        super().__init__()
    
    def create(self, dto: YourModuleRequestDTO) -> YourModuleResponseDTO:
        """创建新记录"""
        # 检查ID是否已存在
        if self.get_by_id(dto.id):
            raise ValueError(f"ID {dto.id} 已存在")
        
        # 创建新记录
        model = YourModule(
            id=dto.id,
            name=dto.name,
            description=dto.description,
            status=dto.status
        )
        
        self.db.session.add(model)
        self.db.session.commit()
        
        return YourModuleResponseDTO(
            id=model.id,
            name=model.name,
            description=model.description,
            status=model.status,
            create_time=model.create_time,
            update_time=model.update_time
        )
    
    def get_by_id(self, id: str) -> Optional[YourModuleResponseDTO]:
        """根据ID获取记录"""
        model = YourModule.query.get(id)
        if not model:
            return None
        
        return YourModuleResponseDTO(
            id=model.id,
            name=model.name,
            description=model.description,
            status=model.status,
            create_time=model.create_time,
            update_time=model.update_time
        )
    
    def get_paginated(
        self, 
        page: int = 1, 
        per_page: int = 10,
        filters: Optional[dict] = None
    ) -> YourModulePaginatedResponse:
        """获取分页数据"""
        query = YourModule.query
        
        # 应用过滤条件
        if filters:
            if filters.get('name'):
                query = query.filter(YourModule.name.like(f"%{filters['name']}%"))
            if filters.get('status') is not None:
                query = query.filter(YourModule.status == filters['status'])
        
        # 执行分页查询
        pagination = query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        # 构建响应数据
        data = [
            YourModuleResponseDTO(
                id=item.id,
                name=item.name,
                description=item.description,
                status=item.status,
                create_time=item.create_time,
                update_time=item.update_time
            ) for item in pagination.items
        ]
        
        # 构建分页元数据
        meta = PaginationMeta(
            page=page,
            per_page=per_page,
            total=pagination.total,
            pages=pagination.pages,
            has_next=pagination.has_next,
            has_prev=pagination.has_prev
        )
        
        return YourModulePaginatedResponse(data=data, meta=meta)
    
    def update(self, id: str, dto: YourModuleUpdateRequestDTO) -> YourModuleResponseDTO:
        """更新记录"""
        model = YourModule.query.get(id)
        if not model:
            raise ValueError(f"ID {id} 不存在")
        
        # 更新字段
        if dto.name is not None:
            model.name = dto.name
        if dto.description is not None:
            model.description = dto.description
        if dto.status is not None:
            model.status = dto.status
        
        self.db.session.commit()
        
        return YourModuleResponseDTO(
            id=model.id,
            name=model.name,
            description=model.description,
            status=model.status,
            create_time=model.create_time,
            update_time=model.update_time
        )
    
    def delete(self, id: str) -> bool:
        """删除记录"""
        model = YourModule.query.get(id)
        if not model:
            return False
        
        self.db.session.delete(model)
        self.db.session.commit()
        return True
```

### 第四步：创建API资源 (Resource)

在 `app/api/v1/resources/` 目录下创建或修改资源文件：

```python
# app/api/v1/resources/your_module.py
from flask import request
from flask_restx import Resource, fields
from app.services.your_module_service import YourModuleService
from app.dto.your_module import (
    YourModuleRequestDTO, 
    YourModuleUpdateRequestDTO, 
    YourModuleResponseDTO
)
from app.swagger import api
from app.utils.decorators import paginated_response
from app.utils.response_builder import ResponseBuilder

# 创建命名空间
your_module_ns = api.namespace('your-module', description='你的模块管理接口')

# ==================== OpenAPI 模型定义 ====================

# 基础模型
your_module_model = api.model('YourModule', {
    'id': fields.String(required=True, description='模块ID'),
    'name': fields.String(required=True, description='模块名称'),
    'description': fields.String(description='模块描述'),
    'status': fields.Boolean(description='状态'),
    'create_time': fields.DateTime(description='创建时间'),
    'update_time': fields.DateTime(description='更新时间')
})

# 分页响应模型
your_module_pagination_response = api.model('YourModulePaginationResponse', {
    'data': fields.List(fields.Nested(your_module_model), description='模块列表'),
    'meta': fields.Nested(api.model('PaginationMeta', {
        'page': fields.Integer(description='当前页码'),
        'per_page': fields.Integer(description='每页数量'),
        'total': fields.Integer(description='总记录数'),
        'pages': fields.Integer(description='总页数'),
        'has_next': fields.Boolean(description='是否有下一页'),
        'has_prev': fields.Boolean(description='是否有上一页')
    }), description='分页信息')
})

# 创建模型
your_module_create_model = api.model('YourModuleCreate', {
    'id': fields.String(required=True, description='模块ID'),
    'name': fields.String(required=True, description='模块名称'),
    'description': fields.String(description='模块描述'),
    'status': fields.Boolean(description='状态')
})

# 更新模型
your_module_update_model = api.model('YourModuleUpdate', {
    'name': fields.String(description='模块名称'),
    'description': fields.String(description='模块描述'),
    'status': fields.Boolean(description='状态')
})

# 错误响应模型
error_model = api.model('Error', {
    'code': fields.String(required=True, description='错误码'),
    'message': fields.String(required=True, description='错误信息'),
    'details': fields.Raw(description='详细信息'),
    'timestamp': fields.DateTime(description='时间戳')
})

# ==================== API 资源类 ====================

@your_module_ns.route('/')
class YourModuleListResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = YourModuleService()
    
    @your_module_ns.doc('获取模块列表')
    @your_module_ns.param('page', '页码', type=int, default=1)
    @your_module_ns.param('per_page', '每页数量', type=int, default=10)
    @your_module_ns.param('name', '模块名称', type=str)
    @your_module_ns.param('status', '状态', type=bool)
    @your_module_ns.response(200, '获取成功', your_module_pagination_response)
    @paginated_response
    def get(self):
        """获取模块列表（分页）"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # 构建过滤条件
        filters = {}
        if request.args.get('name'):
            filters['name'] = request.args.get('name')
        if request.args.get('status') is not None:
            filters['status'] = request.args.get('status', type=bool)
        
        result = self.service.get_paginated(page=page, per_page=per_page, filters=filters)
        return ResponseBuilder.build_paginated_response(result)
    
    @your_module_ns.doc('创建模块')
    @your_module_ns.expect(your_module_create_model)
    @your_module_ns.response(201, '创建成功', your_module_model)
    @your_module_ns.response(400, '请求错误', error_model)
    def post(self):
        """创建新模块"""
        data = request.get_json()
        
        # 构建DTO
        dto = YourModuleRequestDTO(
            id=data['id'],
            name=data['name'],
            description=data.get('description'),
            status=data.get('status', True)
        )
        
        result = self.service.create(dto)
        return ResponseBuilder.build_success_response(result, status_code=201)

@your_module_ns.route('/<string:module_id>')
@your_module_ns.param('module_id', '模块ID')
class YourModuleResource(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service = YourModuleService()
    
    @your_module_ns.doc('获取模块信息')
    @your_module_ns.response(200, '获取成功', your_module_model)
    @your_module_ns.response(404, '未找到', error_model)
    def get(self, module_id):
        """获取模块详细信息"""
        result = self.service.get_by_id(module_id)
        if not result:
            return ResponseBuilder.build_error_response('NOT_FOUND', f'模块 {module_id} 不存在', status_code=404)
        
        return ResponseBuilder.build_success_response(result)
    
    @your_module_ns.doc('更新模块')
    @your_module_ns.expect(your_module_update_model)
    @your_module_ns.response(200, '更新成功', your_module_model)
    @your_module_ns.response(400, '请求错误', error_model)
    @your_module_ns.response(404, '未找到', error_model)
    def put(self, module_id):
        """更新模块信息"""
        data = request.get_json()
        
        # 构建DTO
        dto = YourModuleUpdateRequestDTO(
            name=data.get('name'),
            description=data.get('description'),
            status=data.get('status')
        )
        
        try:
            result = self.service.update(module_id, dto)
            return ResponseBuilder.build_success_response(result)
        except ValueError as e:
            return ResponseBuilder.build_error_response('NOT_FOUND', str(e), status_code=404)
    
    @your_module_ns.doc('删除模块')
    @your_module_ns.response(200, '删除成功')
    @your_module_ns.response(404, '未找到', error_model)
    def delete(self, module_id):
        """删除模块"""
        success = self.service.delete(module_id)
        if not success:
            return ResponseBuilder.build_error_response('NOT_FOUND', f'模块 {module_id} 不存在', status_code=404)
        
        return ResponseBuilder.build_success_response({'message': '删除成功'})
```

### 第五步：注册API路由

在 `app/api/v1/__init__.py` 中注册新的命名空间：

```python
# app/api/v1/__init__.py
from flask import Blueprint
from flask_restx import Api
from app.api.v1.resources.dict import dict_ns
from app.api.v1.resources.your_module import your_module_ns  # 新增

# 创建蓝图
api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# 创建API实例
api = Api(
    api_v1_bp,
    title='KSF RESTful API',
    version='1.0',
    description='KSF项目RESTful API文档',
    doc='/docs'
)

# 添加命名空间
api.add_namespace(dict_ns)
api.add_namespace(your_module_ns)  # 新增
```

### 第六步：创建数据库迁移

```bash
# 生成迁移文件
flask db migrate -m "Add your_module table"

# 应用迁移
flask db upgrade
```

### 第七步：编写测试

在 `tests/` 目录下创建测试文件：

```python
# tests/test_your_module.py
import pytest
from app import create_app
from app.models.your_module import YourModule
from app.services.your_module_service import YourModuleService
from app.dto.your_module import YourModuleRequestDTO, YourModuleUpdateRequestDTO

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        # 创建测试数据库表
        from app.models import db
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def service():
    return YourModuleService()

class TestYourModuleService:
    def test_create_module(self, service):
        dto = YourModuleRequestDTO(
            id='test001',
            name='测试模块',
            description='这是一个测试模块',
            status=True
        )
        
        result = service.create(dto)
        assert result.id == 'test001'
        assert result.name == '测试模块'
    
    def test_get_by_id(self, service):
        # 先创建
        dto = YourModuleRequestDTO(id='test002', name='测试模块2')
        service.create(dto)
        
        # 再查询
        result = service.get_by_id('test002')
        assert result is not None
        assert result.name == '测试模块2'
    
    def test_update_module(self, service):
        # 先创建
        dto = YourModuleRequestDTO(id='test003', name='原始名称')
        service.create(dto)
        
        # 再更新
        update_dto = YourModuleUpdateRequestDTO(name='新名称')
        result = service.update('test003', update_dto)
        assert result.name == '新名称'
    
    def test_delete_module(self, service):
        # 先创建
        dto = YourModuleRequestDTO(id='test004', name='待删除模块')
        service.create(dto)
        
        # 再删除
        success = service.delete('test004')
        assert success is True
        
        # 验证已删除
        result = service.get_by_id('test004')
        assert result is None

class TestYourModuleAPI:
    def test_get_modules_list(self, client):
        response = client.get('/api/v1/your-module/')
        assert response.status_code == 200
    
    def test_create_module(self, client):
        data = {
            'id': 'api001',
            'name': 'API测试模块',
            'description': '通过API创建的测试模块'
        }
        
        response = client.post('/api/v1/your-module/', json=data)
        assert response.status_code == 201
        
        result = response.get_json()
        assert result['data']['id'] == 'api001'
    
    def test_get_module_detail(self, client):
        # 先创建
        data = {'id': 'api002', 'name': '详情测试模块'}
        client.post('/api/v1/your-module/', json=data)
        
        # 再查询详情
        response = client.get('/api/v1/your-module/api002')
        assert response.status_code == 200
        
        result = response.get_json()
        assert result['data']['name'] == '详情测试模块'
    
    def test_update_module(self, client):
        # 先创建
        data = {'id': 'api003', 'name': '原始名称'}
        client.post('/api/v1/your-module/', json=data)
        
        # 再更新
        update_data = {'name': '更新后的名称'}
        response = client.put('/api/v1/your-module/api003', json=update_data)
        assert response.status_code == 200
        
        result = response.get_json()
        assert result['data']['name'] == '更新后的名称'
    
    def test_delete_module(self, client):
        # 先创建
        data = {'id': 'api004', 'name': '待删除模块'}
        client.post('/api/v1/your-module/', json=data)
        
        # 再删除
        response = client.delete('/api/v1/your-module/api004')
        assert response.status_code == 200
        
        # 验证已删除
        get_response = client.get('/api/v1/your-module/api004')
        assert get_response.status_code == 404
```

### 第八步：更新文档

1. **更新API文档**：访问 `/api/v1/docs` 查看自动生成的Swagger文档
2. **更新README**：在项目README中添加新模块的说明
3. **更新数据库文档**：在 `DATABASE_MIGRATION.md` 中记录新的表结构

## 最佳实践

### 1. 命名规范
- 模型类：使用PascalCase，如 `YourModule`
- 表名：使用snake_case，如 `your_module`
- API路径：使用kebab-case，如 `/api/v1/your-module`
- 变量名：使用snake_case，如 `your_module_service`

### 2. 错误处理
- 使用统一的错误响应格式
- 在Service层抛出业务异常
- 在API层捕获异常并返回标准错误响应

### 3. 数据验证
- 在DTO中使用类型注解
- 在API层使用Swagger模型进行参数验证
- 在Service层进行业务逻辑验证

### 4. 分页处理
- 使用统一的分页响应格式
- 支持过滤和排序功能
- 使用 `@paginated_response` 装饰器

### 5. 测试覆盖
- 编写Service层单元测试
- 编写API层集成测试
- 测试正常流程和异常情况

## 常见问题

### Q1: 如何处理关联关系？
A1: 在模型中定义外键关系，在DTO中包含关联对象，在Service中处理关联查询。

### Q2: 如何添加自定义过滤条件？
A2: 在Service的 `get_paginated` 方法中添加过滤逻辑，在API中接收过滤参数。

### Q3: 如何处理软删除？
A3: 在模型中添加 `deleted_at` 字段，在查询时过滤已删除的记录。

### Q4: 如何添加缓存？
A4: 在Service层添加缓存逻辑，使用Redis或其他缓存系统。

## 总结

通过以上8个步骤，您可以完整地添加一个新的字典模块。每个步骤都有明确的职责：

- **Model层**：定义数据结构
- **DTO层**：定义数据传输格式
- **Service层**：实现业务逻辑
- **API层**：提供HTTP接口
- **测试层**：确保代码质量

这种分层架构确保了代码的可维护性、可测试性和可扩展性。 