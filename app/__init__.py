from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from dotenv import load_dotenv

# 初始化扩展
db = SQLAlchemy()
migrate = Migrate()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

load_dotenv()  # 自动加载 .env 文件

def create_app(config_name=None):
    """应用工厂函数"""
    app = Flask(__name__)
    
    # 配置
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')
    
    app.config.from_object(f'config.{config_name.capitalize()}Config')
    
    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    limiter.init_app(app)
    
    # 注册 Swagger API
    from app.swagger import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    
    # 注册错误处理器
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    
    # 创建数据库表
    with app.app_context():
        db.create_all()
    
    return app 