import pytest
from app import create_app, db
from app.models.dict import DwType, Dw, RcjEjflSx, RcjYjfl, RcjEjfl, RcjMC2Ejflid, RcjMCClassify

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
def dw_type(app):
    """创建测试单位类别"""
    dw_type = DwType(id='01', typeName='重量')
    db.session.add(dw_type)
    db.session.commit()
    return dw_type

@pytest.fixture
def dw(app, dw_type):
    """创建测试单位"""
    dw = Dw(id='0010', type_id='01', dw='千克')
    db.session.add(dw)
    db.session.commit()
    return dw

@pytest.fixture
def rcj_yjfl(app):
    """创建测试人材机一级分类"""
    yjfl = RcjYjfl(id='0100', yjflmc='材料', yjflms='建筑材料')
    db.session.add(yjfl)
    db.session.commit()
    return yjfl

@pytest.fixture
def rcj_ejfl_sx(app):
    """创建测试人材机二级分类属性"""
    sx = RcjEjflSx(id='0001', sx='规格')
    db.session.add(sx)
    db.session.commit()
    return sx

class TestDwTypeAPI:
    """测试单位类别API"""
    
    def test_get_dw_types(self, client):
        """测试获取单位类别列表"""
        response = client.get('/api/v1/dict/dw-types')
        assert response.status_code == 200
        data = response.get_json()
        assert 'items' in data
        assert 'pagination' in data
    
    def test_create_dw_type(self, client):
        """测试创建单位类别"""
        response = client.post('/api/v1/dict/dw-types', json={
            'id': '01',
            'typeName': '重量'
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data['message'] == '单位类别创建成功'
        assert data['dw_type']['id'] == '01'
        assert data['dw_type']['typeName'] == '重量'
    
    def test_get_dw_type(self, client, dw_type):
        """测试获取单个单位类别"""
        response = client.get(f'/api/v1/dict/dw-types/{dw_type.id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data['dw_type']['id'] == dw_type.id
        assert data['dw_type']['typeName'] == dw_type.typeName
    
    def test_update_dw_type(self, client, dw_type):
        """测试更新单位类别"""
        response = client.put(f'/api/v1/dict/dw-types/{dw_type.id}', json={
            'typeName': '长度'
        })
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == '单位类别更新成功'
        assert data['dw_type']['typeName'] == '长度'
    
    def test_delete_dw_type(self, client, dw_type):
        """测试删除单位类别"""
        response = client.delete(f'/api/v1/dict/dw-types/{dw_type.id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == '单位类别删除成功'

class TestDwAPI:
    """测试单位API"""
    
    def test_get_dws(self, client):
        """测试获取单位列表"""
        response = client.get('/api/v1/dict/dws')
        assert response.status_code == 200
        data = response.get_json()
        assert 'items' in data
        assert 'pagination' in data
    
    def test_create_dw(self, client, dw_type):
        """测试创建单位"""
        response = client.post('/api/v1/dict/dws', json={
            'id': '0010',
            'type_id': '01',
            'dw': '千克'
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data['message'] == '单位创建成功'
        assert data['dw']['id'] == '0010'
        assert data['dw']['dw'] == '千克'
    
    def test_get_dw(self, client, dw):
        """测试获取单个单位"""
        response = client.get(f'/api/v1/dict/dws/{dw.id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data['dw']['id'] == dw.id
        assert data['dw']['dw'] == dw.dw
    
    def test_update_dw(self, client, dw):
        """测试更新单位"""
        response = client.put(f'/api/v1/dict/dws/{dw.id}', json={
            'dw': '公斤'
        })
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == '单位更新成功'
        assert data['dw']['dw'] == '公斤'
    
    def test_delete_dw(self, client, dw):
        """测试删除单位"""
        response = client.delete(f'/api/v1/dict/dws/{dw.id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == '单位删除成功'

class TestRcjYjflAPI:
    """测试人材机一级分类API"""
    
    def test_get_rcj_yjfls(self, client):
        """测试获取人材机一级分类列表"""
        response = client.get('/api/v1/dict/rcj-yjfls')
        assert response.status_code == 200
        data = response.get_json()
        assert 'items' in data
        assert 'pagination' in data
    
    def test_create_rcj_yjfl(self, client):
        """测试创建人材机一级分类"""
        response = client.post('/api/v1/dict/rcj-yjfls', json={
            'id': '0100',
            'yjflmc': '材料',
            'yjflms': '建筑材料'
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data['message'] == '人材机一级分类创建成功'
        assert data['yjfl']['id'] == '0100'
        assert data['yjfl']['yjflmc'] == '材料'
    
    def test_get_rcj_yjfl(self, client, rcj_yjfl):
        """测试获取单个人材机一级分类"""
        response = client.get(f'/api/v1/dict/rcj-yjfls/{rcj_yjfl.id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data['yjfl']['id'] == rcj_yjfl.id
        assert data['yjfl']['yjflmc'] == rcj_yjfl.yjflmc
    
    def test_update_rcj_yjfl(self, client, rcj_yjfl):
        """测试更新人材机一级分类"""
        response = client.put(f'/api/v1/dict/rcj-yjfls/{rcj_yjfl.id}', json={
            'yjflmc': '设备'
        })
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == '人材机一级分类更新成功'
        assert data['yjfl']['yjflmc'] == '设备'
    
    def test_delete_rcj_yjfl(self, client, rcj_yjfl):
        """测试删除人材机一级分类"""
        response = client.delete(f'/api/v1/dict/rcj-yjfls/{rcj_yjfl.id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == '人材机一级分类删除成功'

class TestRcjEjflSxAPI:
    """测试人材机二级分类属性API"""
    
    def test_get_rcj_ejfl_sxs(self, client):
        """测试获取人材机二级分类属性列表"""
        response = client.get('/api/v1/dict/rcj-ejfl-sxs')
        assert response.status_code == 200
        data = response.get_json()
        assert 'items' in data
        assert 'pagination' in data
    
    def test_create_rcj_ejfl_sx(self, client):
        """测试创建人材机二级分类属性"""
        response = client.post('/api/v1/dict/rcj-ejfl-sxs', json={
            'id': '0001',
            'sx': '规格'
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data['message'] == '人材机二级分类属性创建成功'
        assert data['sx']['id'] == '0001'
        assert data['sx']['sx'] == '规格'
    
    def test_get_rcj_ejfl_sx(self, client, rcj_ejfl_sx):
        """测试获取单个人材机二级分类属性"""
        response = client.get(f'/api/v1/dict/rcj-ejfl-sxs/{rcj_ejfl_sx.id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data['sx']['id'] == rcj_ejfl_sx.id
        assert data['sx']['sx'] == rcj_ejfl_sx.sx
    
    def test_update_rcj_ejfl_sx(self, client, rcj_ejfl_sx):
        """测试更新人材机二级分类属性"""
        response = client.put(f'/api/v1/dict/rcj-ejfl-sxs/{rcj_ejfl_sx.id}', json={
            'sx': '尺寸'
        })
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == '人材机二级分类属性更新成功'
        assert data['sx']['sx'] == '尺寸'
    
    def test_delete_rcj_ejfl_sx(self, client, rcj_ejfl_sx):
        """测试删除人材机二级分类属性"""
        response = client.delete(f'/api/v1/dict/rcj-ejfl-sxs/{rcj_ejfl_sx.id}')
        assert response.status_code == 200
        data = response.get_json()
        assert data['message'] == '人材机二级分类属性删除成功' 