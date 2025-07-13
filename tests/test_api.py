"""
API层测试文件
测试API端点的请求和响应
"""
import pytest
import json
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime
from app import create_app
from app.dto.dict import (
    DwTypeRequestDTO, DwTypeUpdateRequestDTO, DwTypeResponseDTO,
    DwRequestDTO, DwUpdateRequestDTO, DwResponseDTO,
    RcjEjflSxRequestDTO, RcjEjflSxUpdateRequestDTO, RcjEjflSxResponseDTO,
    RcjYjflRequestDTO, RcjYjflUpdateRequestDTO, RcjYjflResponseDTO,
    RcjEjflRequestDTO, RcjEjflUpdateRequestDTO, RcjEjflResponseDTO,
    RcjMC2EjflidRequestDTO, RcjMC2EjflidUpdateRequestDTO, RcjMC2EjflidResponseDTO,
    RcjMCClassifyRequestDTO, RcjMCClassifyUpdateRequestDTO, RcjMCClassifyResponseDTO,
    PaginationMeta, PaginatedResponse, ErrorCode, ErrorResponse
)
from app.services.dict_service import DictService


@pytest.fixture
def app():
    """创建测试应用"""
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    """创建测试客户端"""
    return app.test_client()


class TestDwTypeAPI:
    """测试单位类别API"""
    
    def test_get_dw_types_success(self, client):
        """测试获取单位类别列表成功"""
        with patch.object(DictService, 'get_dw_types') as mock_service:
            mock_service.return_value = PaginatedResponse(
                data=[
                    DwTypeResponseDTO(
                        id="01",
                        typeName="重量",
                        create_time=datetime.now(),
                        update_time=datetime.now()
                    ),
                    DwTypeResponseDTO(
                        id="02",
                        typeName="长度",
                        create_time=datetime.now(),
                        update_time=datetime.now()
                    )
                ],
                meta=PaginationMeta(
                    page=1,
                    per_page=10,
                    total=2,
                    pages=1,
                    has_next=False,
                    has_prev=False
                )
            )
            response = client.get('/api/v1/dict/dw-types?page=1&per_page=10')
            data = json.loads(response.data)
            assert response.status_code == 200
            assert len(data['data']) == 2
            assert data['data'][0]['id'] == "01"
            assert data['data'][1]['id'] == "02"
    
    def test_get_dw_type_by_id_success(self, client):
        """测试根据ID获取单位类别成功"""
        with patch.object(DictService, 'get_dw_type_by_id') as mock_service:
            mock_service.return_value = DwTypeResponseDTO(
                id="01",
                typeName="重量",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
            response = client.get('/api/v1/dict/dw-types/01')
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['id'] == "01"
            assert data['typeName'] == "重量"
    
    def test_get_dw_type_by_id_not_found(self, client):
        """测试根据ID获取单位类别失败"""
        with patch.object(DictService, 'get_dw_type_by_id') as mock_service:
            mock_service.return_value = None
            response = client.get('/api/v1/dict/dw-types/99')
            assert response.status_code == 404
    
    def test_create_dw_type_success(self, client):
        """测试创建单位类别成功"""
        with patch.object(DictService, 'create_dw_type') as mock_service:
            mock_service.return_value = DwTypeResponseDTO(
                id="01",
                typeName="重量",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
            request_data = {
                "id": "01",
                "typeName": "重量"
            }
            response = client.post(
                '/api/v1/dict/dw-types',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            data = json.loads(response.data)
            assert response.status_code == 201
            assert data['id'] == "01"
            assert data['typeName'] == "重量"
    
    def test_create_dw_type_duplicate_id(self, client):
        """测试创建单位类别ID重复"""
        with patch.object(DictService, 'create_dw_type') as mock_service:
            mock_service.side_effect = ValueError("ID已存在")
            request_data = {
                "id": "01",
                "typeName": "重量"
            }
            response = client.post(
                '/api/v1/dict/dw-types',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            assert response.status_code == 400
    
    def test_update_dw_type_success(self, client):
        """测试更新单位类别成功"""
        with patch.object(DictService, 'update_dw_type') as mock_service:
            mock_service.return_value = DwTypeResponseDTO(
                id="01",
                typeName="长度",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
            request_data = {
                "typeName": "长度"
            }
            response = client.put(
                '/api/v1/dict/dw-types/01',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['id'] == "01"
            assert data['typeName'] == "长度"

    def test_update_dw_type_not_found(self, client):
        """测试更新单位类别失败"""
        with patch.object(DictService, 'update_dw_type') as mock_service:
            mock_service.return_value = None
            request_data = {
                "typeName": "长度"
            }
            response = client.put(
                '/api/v1/dict/dw-types/99',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            assert response.status_code == 404

    def test_delete_dw_type_success(self, client):
        """测试删除单位类别成功"""
        with patch.object(DictService, 'delete_dw_type') as mock_service:
            mock_service.return_value = True
            response = client.delete('/api/v1/dict/dw-types/01')
            assert response.status_code == 204

    def test_delete_dw_type_not_found(self, client):
        """测试删除单位类别失败"""
        with patch.object(DictService, 'delete_dw_type') as mock_service:
            mock_service.return_value = False
            response = client.delete('/api/v1/dict/dw-types/99')
            assert response.status_code == 404


class TestDwAPI:
    """测试单位API"""
    
    def test_get_dws_success(self, client):
        """测试获取单位列表成功"""
        with patch.object(DictService, 'get_dws') as mock_service:
            mock_service.return_value = PaginatedResponse(
                data=[
                    DwResponseDTO(
                        id="0010",
                        dw="个",
                        type_id="01",
                        create_time=datetime.now(),
                        update_time=datetime.now(),
                        type=DwTypeResponseDTO(
                            id="01",
                            typeName="重量",
                            create_time=datetime.now(),
                            update_time=datetime.now()
                        )
                    )
                ],
                meta=PaginationMeta(
                    page=1,
                    per_page=10,
                    total=1,
                    pages=1,
                    has_next=False,
                    has_prev=False
                )
            )
            response = client.get('/api/v1/dict/dws?page=1&per_page=10&type_id=01')
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['data'][0]['id'] == "0010"
            assert data['data'][0]['dw'] == "个"
            assert data['data'][0]['type_id'] == "01"
            assert data['data'][0]['type']['id'] == "01"
    
    def test_get_dw_by_id_success(self, client):
        """测试根据ID获取单位成功"""
        with patch.object(DictService, 'get_dw_by_id') as mock_service:
            mock_service.return_value = DwResponseDTO(
                id="0010",
                dw="个",
                type_id="01",
                create_time=datetime.now(),
                update_time=datetime.now(),
                type=DwTypeResponseDTO(
                    id="01",
                    typeName="重量",
                    create_time=datetime.now(),
                    update_time=datetime.now()
                )
            )
            response = client.get('/api/v1/dict/dws/0010')
            data = json.loads(response.data)
            assert response.status_code == 200
            assert data['id'] == "0010"
            assert data['dw'] == "个"
            assert data['type_id'] == "01"
            assert data['type']['id'] == "01"
    
    def test_create_dw_success(self, client):
        """测试创建单位成功"""
        with patch.object(DictService, 'create_dw') as mock_service:
            mock_service.return_value = DwResponseDTO(
                id="0010",
                dw="个",
                type_id="01",
                create_time=datetime.now(),
                update_time=datetime.now(),
                type=DwTypeResponseDTO(
                    id="01",
                    typeName="重量",
                    create_time=datetime.now(),
                    update_time=datetime.now()
                )
            )
            request_data = {
                "id": "0010",
                "dw": "个",
                "type_id": "01"
            }
            response = client.post(
                '/api/v1/dict/dws',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            data = json.loads(response.data)
            assert response.status_code == 201
            assert data['id'] == "0010"
            assert data['dw'] == "个"
            assert data['type_id'] == "01"
            assert data['type']['id'] == "01"


class TestRcjEjflSxAPI:
    """测试人材机二级分类属性API"""
    
    def test_get_rcj_ejfl_sxs_success(self, client):
        """测试获取人材机二级分类属性列表成功"""
        with patch.object(DictService, 'get_rcj_ejfl_sxs') as mock_service:
            mock_service.return_value = PaginatedResponse(
                data=[
                    RcjEjflSxResponseDTO(
                        id="0001",
                        sx="规格",
                        create_time=datetime.now(),
                        update_time=datetime.now()
                    )
                ],
                meta=PaginationMeta(
                    page=1,
                    per_page=10,
                    total=1,
                    pages=1,
                    has_next=False,
                    has_prev=False
                )
            )
            response = client.get('/api/v1/dict/rcj-ejfl-sxs?page=1&per_page=10')
            data = json.loads(response.data)
            assert response.status_code == 200
            assert len(data['data']) == 1
            assert data['data'][0]['id'] == "0001"
            assert data['data'][0]['sx'] == "规格"

    def test_create_rcj_ejfl_sx_success(self, client):
        """测试创建人材机二级分类属性成功"""
        with patch.object(DictService, 'create_rcj_ejfl_sx') as mock_service:
            mock_service.return_value = RcjEjflSxResponseDTO(
                id="0001",
                sx="规格",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
            request_data = {
                "id": "0001",
                "sx": "规格"
            }
            response = client.post(
                '/api/v1/dict/rcj-ejfl-sxs',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            data = json.loads(response.data)
            assert response.status_code == 201
            assert data['id'] == "0001"
            assert data['sx'] == "规格"


class TestRcjYjflAPI:
    """测试人材机一级分类API"""
    
    def test_get_rcj_yjfls_success(self, client):
        """测试获取人材机一级分类列表成功"""
        with patch.object(DictService, 'get_rcj_yjfls') as mock_service:
            mock_service.return_value = PaginatedResponse(
                data=[
                    RcjYjflResponseDTO(
                        id="01",
                        yjflmc="人工费",
                        yjflms="人工相关费用",
                        create_time=datetime.now(),
                        update_time=datetime.now()
                    )
                ],
                meta=PaginationMeta(
                    page=1,
                    per_page=10,
                    total=1,
                    pages=1,
                    has_next=False,
                    has_prev=False
                )
            )
            response = client.get('/api/v1/dict/rcj-yjfls?page=1&per_page=10')
            data = json.loads(response.data)
            assert response.status_code == 200
            assert len(data['data']) == 1
            assert data['data'][0]['id'] == "01"
            assert data['data'][0]['yjflmc'] == "人工费"

    def test_create_rcj_yjfl_success(self, client):
        """测试创建人材机一级分类成功"""
        with patch.object(DictService, 'create_rcj_yjfl') as mock_service:
            mock_service.return_value = RcjYjflResponseDTO(
                id="01",
                yjflmc="人工费",
                yjflms="人工相关费用",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
            request_data = {
                "id": "01",
                "yjflmc": "人工费",
                "yjflms": "人工相关费用"
            }
            response = client.post(
                '/api/v1/dict/rcj-yjfls',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            data = json.loads(response.data)
            assert response.status_code == 201
            assert data['id'] == "01"
            assert data['yjflmc'] == "人工费"


class TestRcjEjflAPI:
    """测试人材机二级分类API"""
    
    def test_get_rcj_ejfls_success(self, client):
        """测试获取人材机二级分类列表成功"""
        with patch.object(DictService, 'get_rcj_ejfls') as mock_service:
            mock_service.return_value = PaginatedResponse(
                data=[
                    RcjEjflResponseDTO(
                        id="0101",
                        yjfl_id="01",
                        ejflmc="砌筑工",
                        ejflms="砌筑相关工种",
                        create_time=datetime.now(),
                        update_time=datetime.now(),
                        sxs=["规格", "尺寸"],
                        dws=["个", "米"],
                        yjfl=RcjYjflResponseDTO(
                            id="01",
                            yjflmc="人工费",
                            yjflms="人工相关费用",
                            create_time=datetime.now(),
                            update_time=datetime.now()
                        )
                    )
                ],
                meta=PaginationMeta(
                    page=1,
                    per_page=10,
                    total=1,
                    pages=1,
                    has_next=False,
                    has_prev=False
                )
            )
            response = client.get('/api/v1/dict/rcj-ejfls?page=1&per_page=10&yjfl_id=01')
            data = json.loads(response.data)
            assert response.status_code == 200
            assert len(data['data']) == 1
            assert data['data'][0]['id'] == "0101"
            assert data['data'][0]['ejflmc'] == "砌筑工"

    def test_create_rcj_ejfl_success(self, client):
        """测试创建人材机二级分类成功"""
        with patch.object(DictService, 'create_rcj_ejfl') as mock_service:
            mock_service.return_value = RcjEjflResponseDTO(
                id="0101",
                yjfl_id="01",
                ejflmc="砌筑工",
                ejflms="砌筑相关工种",
                create_time=datetime.now(),
                update_time=datetime.now(),
                sxs=["规格", "尺寸"],
                dws=["个", "米"]
            )
            request_data = {
                "id": "0101",
                "ejflmc": "砌筑工",
                "yjfl_id": "01",
                "ejflms": "砌筑相关工种",
                "sx_ids": ["0001", "0002"],
                "dw_ids": ["0010", "0011"]
            }
            response = client.post(
                '/api/v1/dict/rcj-ejfls',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            data = json.loads(response.data)
            assert response.status_code == 201
            assert data['id'] == "0101"
            assert data['ejflmc'] == "砌筑工"


class TestRcjMC2EjflidAPI:
    """测试人材机名称映射API"""
    
    def test_get_rcj_mc2ejflids_success(self, client):
        """测试获取人材机名称映射列表成功"""
        with patch.object(DictService, 'get_rcj_mc2ejflids') as mock_service:
            mock_service.return_value = PaginatedResponse(
                data=[
                    RcjMC2EjflidResponseDTO(
                        id=1,
                        ejflid="0101",
                        orignal_rcjmc="砌筑工",
                        create_time=datetime.now(),
                        update_time=datetime.now()
                    )
                ],
                meta=PaginationMeta(
                    page=1,
                    per_page=10,
                    total=1,
                    pages=1,
                    has_next=False,
                    has_prev=False
                )
            )
            response = client.get('/api/v1/dict/rcj-mc2ejflids?page=1&per_page=10&ejflid=0101')
            data = json.loads(response.data)
            assert response.status_code == 200
            assert len(data['data']) == 1
            assert data['data'][0]['id'] == 1
            assert data['data'][0]['orignal_rcjmc'] == "砌筑工"

    def test_create_rcj_mc2ejflid_success(self, client):
        """测试创建人材机名称映射成功"""
        with patch.object(DictService, 'create_rcj_mc2ejflid') as mock_service:
            mock_service.return_value = RcjMC2EjflidResponseDTO(
                id=1,
                ejflid="0101",
                orignal_rcjmc="砌筑工",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
            request_data = {
                "ejflid": "0101",
                "orignal_rcjmc": "砌筑工"
            }
            response = client.post(
                '/api/v1/dict/rcj-mc2ejflids',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            data = json.loads(response.data)
            assert response.status_code == 201
            assert data['id'] == 1
            assert data['orignal_rcjmc'] == "砌筑工"


class TestRcjMCClassifyAPI:
    """测试人材机名称分类API"""
    
    def test_get_rcj_mc_classifies_success(self, client):
        """测试获取人材机名称分类列表成功"""
        with patch.object(DictService, 'get_rcj_mc_classifies') as mock_service:
            mock_service.return_value = PaginatedResponse(
                data=[
                    RcjMCClassifyResponseDTO(
                        id=1,
                        cleaned_rcj_original_mc="砌筑工",
                        yjflid="01",
                        yjflmc="人工费",
                        ejflid="0101",
                        ejflmc="砌筑工",
                        create_time=datetime.now(),
                        update_time=datetime.now()
                    )
                ],
                meta=PaginationMeta(
                    page=1,
                    per_page=10,
                    total=1,
                    pages=1,
                    has_next=False,
                    has_prev=False
                )
            )
            response = client.get('/api/v1/dict/rcj-mc-classifies?page=1&per_page=10&yjflid=01&ejflid=0101')
            data = json.loads(response.data)
            assert response.status_code == 200
            assert len(data['data']) == 1
            assert data['data'][0]['id'] == 1
            assert data['data'][0]['cleaned_rcj_original_mc'] == "砌筑工"

    def test_create_rcj_mc_classify_success(self, client):
        """测试创建人材机名称分类成功"""
        with patch.object(DictService, 'create_rcj_mc_classify') as mock_service:
            mock_service.return_value = RcjMCClassifyResponseDTO(
                id=1,
                cleaned_rcj_original_mc="砌筑工",
                yjflid="01",
                yjflmc="人工费",
                ejflid="0101",
                ejflmc="砌筑工",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
            request_data = {
                "cleaned_rcj_original_mc": "砌筑工",
                "yjflid": "01",
                "yjflmc": "人工费",
                "ejflid": "0101",
                "ejflmc": "砌筑工"
            }
            response = client.post(
                '/api/v1/dict/rcj-mc-classifies',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            data = json.loads(response.data)
            assert response.status_code == 201
            assert data['id'] == 1
            assert data['cleaned_rcj_original_mc'] == "砌筑工"


class TestErrorHandling:
    """测试错误处理"""
    
    def test_validation_error(self, client):
        """测试验证错误"""
        # 发送无效的JSON数据
        response = client.post(
            '/api/v1/dict/dw-types',
            data='invalid json',
            content_type='application/json'
        )
        
        # 验证响应
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'message' in data
        assert 'JSON' in data['message'] or '无效' in data['message']
    
    def test_method_not_allowed(self, client):
        """测试方法不允许"""
        # 发送不支持的HTTP方法
        response = client.patch('/api/v1/dict/dw-types/01')
        
        # 验证响应
        assert response.status_code == 405
    
    def test_not_found(self, client):
        """测试资源不存在"""
        # 访问不存在的端点
        response = client.get('/api/v1/nonexistent')
        
        # 验证响应
        assert response.status_code == 404


if __name__ == "__main__":
    pytest.main([__file__]) 