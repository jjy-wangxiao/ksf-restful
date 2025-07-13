"""
pytest配置文件
设置测试环境和共享fixture
"""
import pytest
import os
import sys
from unittest.mock import Mock, patch

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 设置测试环境变量
os.environ['FLASK_ENV'] = 'testing'
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'


@pytest.fixture(scope="session")
def app():
    """创建测试应用实例"""
    from app import create_app
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'WTF_CSRF_ENABLED': False,
        'RESTX_VALIDATE': False,  # 禁用Flask-RESTX的验证
        'RESTX_MASK_SWAGGER': False  # 禁用Swagger掩码
    })
    return app


@pytest.fixture(scope="session")
def client(app):
    """创建测试客户端"""
    return app.test_client()


@pytest.fixture(scope="session")
def runner(app):
    """创建测试运行器"""
    return app.test_cli_runner()


@pytest.fixture(autouse=True)
def mock_db():
    """自动模拟数据库会话"""
    with patch('app.services.dict_service.db') as mock_db:
        # 模拟数据库会话
        mock_session = Mock()
        mock_db.session = mock_session
        yield mock_db


@pytest.fixture
def sample_dw_type_data():
    """示例单位类别数据"""
    return {
        "id": "01",
        "typeName": "重量",
        "create_time": "2024-01-01T00:00:00",
        "update_time": "2024-01-01T00:00:00"
    }


@pytest.fixture
def sample_dw_data():
    """示例单位数据"""
    return {
        "id": "0010",
        "type_id": "01",
        "dw": "个",
        "create_time": "2024-01-01T00:00:00",
        "update_time": "2024-01-01T00:00:00"
    }


@pytest.fixture
def sample_rcj_ejfl_sx_data():
    """示例人材机二级分类属性数据"""
    return {
        "id": "0001",
        "sx": "规格",
        "create_time": "2024-01-01T00:00:00",
        "update_time": "2024-01-01T00:00:00"
    }


@pytest.fixture
def sample_rcj_yjfl_data():
    """示例人材机一级分类数据"""
    return {
        "id": "01",
        "yjflmc": "人工费",
        "yjflms": "人工相关费用",
        "create_time": "2024-01-01T00:00:00",
        "update_time": "2024-01-01T00:00:00"
    }


@pytest.fixture
def sample_rcj_ejfl_data():
    """示例人材机二级分类数据"""
    return {
        "id": "0101",
        "yjfl_id": "01",
        "ejflmc": "砌筑工",
        "ejflms": "砌筑相关工种",
        "sxs": ["规格", "尺寸"],
        "dws": ["个", "米"],
        "create_time": "2024-01-01T00:00:00",
        "update_time": "2024-01-01T00:00:00"
    }


@pytest.fixture
def sample_rcj_mc2ejflid_data():
    """示例人材机名称映射数据"""
    return {
        "id": 1,
        "ejflid": "0101",
        "orignal_rcjmc": "砌筑工",
        "create_time": "2024-01-01T00:00:00",
        "update_time": "2024-01-01T00:00:00"
    }


@pytest.fixture
def sample_rcj_mc_classify_data():
    """示例人材机名称分类数据"""
    return {
        "id": 1,
        "cleaned_rcj_original_mc": "砌筑工",
        "yjflid": "01",
        "yjflmc": "人工费",
        "ejflid": "0101",
        "ejflmc": "砌筑工",
        "create_time": "2024-01-01T00:00:00",
        "update_time": "2024-01-01T00:00:00"
    }


@pytest.fixture
def mock_pagination():
    """模拟分页对象"""
    def _create_pagination(items, page=1, per_page=10, total=None):
        if total is None:
            total = len(items)
        
        mock_pagination = Mock()
        mock_pagination.page = page
        mock_pagination.per_page = per_page
        mock_pagination.total = total
        mock_pagination.pages = (total + per_page - 1) // per_page
        mock_pagination.has_next = page < mock_pagination.pages
        mock_pagination.has_prev = page > 1
        mock_pagination.items = items
        return mock_pagination
    
    return _create_pagination


@pytest.fixture
def mock_models():
    """模拟所有模型类"""
    with patch('app.services.dict_service.DwType') as mock_dw_type, \
         patch('app.services.dict_service.Dw') as mock_dw, \
         patch('app.services.dict_service.RcjEjflSx') as mock_rcj_ejfl_sx, \
         patch('app.services.dict_service.RcjYjfl') as mock_rcj_yjfl, \
         patch('app.services.dict_service.RcjEjfl') as mock_rcj_ejfl, \
         patch('app.services.dict_service.RcjMC2Ejflid') as mock_rcj_mc2ejflid, \
         patch('app.services.dict_service.RcjMCClassify') as mock_rcj_mc_classify:
        
        yield {
            'DwType': mock_dw_type,
            'Dw': mock_dw,
            'RcjEjflSx': mock_rcj_ejfl_sx,
            'RcjYjfl': mock_rcj_yjfl,
            'RcjEjfl': mock_rcj_ejfl,
            'RcjMC2Ejflid': mock_rcj_mc2ejflid,
            'RcjMCClassify': mock_rcj_mc_classify
        }


# 测试标记
def pytest_configure(config):
    """配置pytest标记"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )


# 测试收集钩子
def pytest_collection_modifyitems(config, items):
    """修改测试收集"""
    for item in items:
        # 为没有标记的测试添加unit标记
        if not any(item.iter_markers()):
            item.add_marker(pytest.mark.unit)
        
        # 为API测试添加integration标记
        if "test_api" in item.nodeid:
            item.add_marker(pytest.mark.integration)
        
        # 为Service测试添加unit标记
        if "test_service" in item.nodeid:
            item.add_marker(pytest.mark.unit)
        
        # 为DTO测试添加unit标记
        if "test_dto" in item.nodeid:
            item.add_marker(pytest.mark.unit) 