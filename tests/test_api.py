import pytest
from app import create_app, db
from app.models import User, Post

@pytest.fixture
def app():
    """创建测试应用"""
    app = create_app('testing')
    
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
def runner(app):
    """创建测试运行器"""
    return app.test_cli_runner()

@pytest.fixture
def user():
    """创建测试用户"""
    user = User(
        username='testuser',
        email='test@example.com'
    )
    user.password = 'TestPass123'
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture
def admin_user():
    """创建管理员用户"""
    user = User(
        username='admin',
        email='admin@example.com',
        is_admin=True
    )
    user.password = 'AdminPass123'
    db.session.add(user)
    db.session.commit()
    return user

class TestAuthAPI:
    """认证API测试"""
    
    def test_user_registration(self, client):
        """测试用户注册"""
        response = client.post('/api/v1/users', json={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'NewPass123'
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data['message'] == '用户创建成功'
        assert data['user']['username'] == 'newuser'
    
    def test_user_login(self, client, user):
        """测试用户登录"""
        response = client.post('/api/v1/auth/login', json={
            'username': 'testuser',
            'password': 'TestPass123'
        })
        assert response.status_code == 200
        data = response.get_json()
        assert 'access_token' in data
        assert 'refresh_token' in data
    
    def test_invalid_login(self, client):
        """测试无效登录"""
        response = client.post('/api/v1/auth/login', json={
            'username': 'wronguser',
            'password': 'wrongpass'
        })
        assert response.status_code == 401

class TestUserAPI:
    """用户API测试"""
    
    def test_get_user_list(self, client, admin_user):
        """测试获取用户列表"""
        # 先登录获取token
        login_response = client.post('/api/v1/auth/login', json={
            'username': 'admin',
            'password': 'AdminPass123'
        })
        token = login_response.get_json()['access_token']
        
        response = client.get('/api/v1/users', headers={
            'Authorization': f'Bearer {token}'
        })
        assert response.status_code == 200
        data = response.get_json()
        assert 'items' in data
        assert 'pagination' in data
    
    def test_get_user_detail(self, client, user):
        """测试获取用户详情"""
        # 先登录获取token
        login_response = client.post('/api/v1/auth/login', json={
            'username': 'testuser',
            'password': 'TestPass123'
        })
        token = login_response.get_json()['access_token']
        
        response = client.get(f'/api/v1/users/{user.id}', headers={
            'Authorization': f'Bearer {token}'
        })
        assert response.status_code == 200
        data = response.get_json()
        assert data['user']['username'] == 'testuser'

class TestPostAPI:
    """文章API测试"""
    
    def test_get_post_list(self, client):
        """测试获取文章列表"""
        response = client.get('/api/v1/posts')
        assert response.status_code == 200
        data = response.get_json()
        assert 'items' in data
        assert 'pagination' in data
    
    def test_create_post(self, client, user):
        """测试创建文章"""
        # 先登录获取token
        login_response = client.post('/api/v1/auth/login', json={
            'username': 'testuser',
            'password': 'TestPass123'
        })
        token = login_response.get_json()['access_token']
        
        response = client.post('/api/v1/posts', json={
            'title': '测试文章',
            'content': '这是测试内容',
            'published': True
        }, headers={
            'Authorization': f'Bearer {token}'
        })
        assert response.status_code == 201
        data = response.get_json()
        assert data['message'] == '文章创建成功'
        assert data['post']['title'] == '测试文章' 