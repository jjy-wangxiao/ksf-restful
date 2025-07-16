"""
Flask应用工厂 - 遵循OpenAPI标准的分层架构
"""
import os
from dotenv import load_dotenv
from flask import Flask

# 加载.env文件
load_dotenv()
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
import json
from datetime import datetime
from enum import Enum

# 初始化SQLAlchemy
db = SQLAlchemy()

# 初始化Flask-Migrate
migrate = Migrate()

class CustomJSONEncoder(json.JSONEncoder):
    """自定义JSON编码器，支持DTO和枚举序列化"""
    
    def default(self, obj):
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, Enum):
            return str(obj)
        return super().default(obj)


def create_app(config_name=None):
    """应用工厂函数"""
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # 设置自定义JSON编码器
    app.json_encoder = CustomJSONEncoder
    
    # 初始化日志系统
    from app.utils.logger import setup_logging, get_logger
    
    setup_logging(
        log_level=app.config.get('LOG_LEVEL', 'INFO'),
        log_format=app.config.get('LOG_FORMAT', 'json'),
        log_file=app.config.get('LOG_FILE'),
        max_bytes=app.config.get('LOG_MAX_BYTES', 10 * 1024 * 1024),
        backup_count=app.config.get('LOG_BACKUP_COUNT', 5),
        enable_console=app.config.get('LOG_ENABLE_CONSOLE', True),
        enable_file=app.config.get('LOG_ENABLE_FILE', True)
    )
    
    # 获取应用日志记录器
    logger = get_logger('app')
    logger.info("Application starting", config=config_name)
    
    # 初始化SQLAlchemy
    db.init_app(app)
    
    # 初始化Flask-Migrate
    migrate.init_app(app, db)
    
    # 初始化扩展
    CORS(app)
    
    # 配置Flask-Limiter
    # 开发环境使用内存存储，生产环境建议使用Redis
    storage_uri = os.environ.get('FLASK_LIMITER_STORAGE_URI', 'memory://')
    limiter = Limiter(
        app=app,
        key_func=get_remote_address,
        default_limits=["200 per day", "50 per hour"],
        storage_uri=storage_uri
    )
    
    # 注册蓝图
    from app.swagger import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    
    # 注册错误处理器蓝图
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    
    # 设置中间件
    from app.utils.middleware import setup_request_logging, setup_error_logging, setup_performance_monitoring
    
    setup_request_logging(app)
    setup_error_logging(app)
    setup_performance_monitoring(app)
    
    logger.info("Application initialized successfully")
    
    return app 