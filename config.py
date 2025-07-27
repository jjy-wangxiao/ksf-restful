import os

class Config:
    """基础配置类"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 分页配置
    POSTS_PER_PAGE = 10
    
    # 日志配置
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    LOG_FORMAT = os.environ.get('LOG_FORMAT', 'json')  # json 或 text
    LOG_FILE = os.environ.get('LOG_FILE', 'logs/ksf-restful.log')
    LOG_MAX_BYTES = int(os.environ.get('LOG_MAX_BYTES', 10 * 1024 * 1024))  # 10MB
    LOG_BACKUP_COUNT = int(os.environ.get('LOG_BACKUP_COUNT', 5))
    LOG_ENABLE_CONSOLE = os.environ.get('LOG_ENABLE_CONSOLE', 'true').lower() == 'true'
    LOG_ENABLE_FILE = os.environ.get('LOG_ENABLE_FILE', 'true').lower() == 'true'
    
    # 服务器配置
    HOST = os.environ.get('FLASK_HOST') or '127.0.0.1'
    PORT = int(os.environ.get('FLASK_PORT') or 5678)
    
    # 文件上传配置
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 50 * 1024 * 1024))  # 50MB
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data-dev.sqlite')
    LOG_LEVEL = 'DEBUG'
    LOG_FORMAT = 'text'  # 开发环境使用文本格式便于调试
    LOG_ENABLE_FILE = True  # 开发环境默认写入文件
    # 开发环境默认端口
    PORT = int(os.environ.get('FLASK_PORT') or 5678)

class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    """生产环境配置"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.sqlite')
    LOG_LEVEL = 'INFO'
    LOG_FORMAT = 'json'  # 生产环境使用JSON格式便于日志分析
    LOG_ENABLE_CONSOLE = False  # 生产环境默认不输出到控制台
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        
        # 生产环境使用新的日志系统
        from app.utils.logger import setup_logging
        
        setup_logging(
            log_level=cls.LOG_LEVEL,
            log_format=cls.LOG_FORMAT,
            log_file=cls.LOG_FILE,
            max_bytes=cls.LOG_MAX_BYTES,
            backup_count=cls.LOG_BACKUP_COUNT,
            enable_console=cls.LOG_ENABLE_CONSOLE,
            enable_file=cls.LOG_ENABLE_FILE
        )

class XmlConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('XML_DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data-dev.sqlite')
    LOG_LEVEL = 'DEBUG'
class DictConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DICT_DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data-dev.sqlite')
    LOG_LEVEL = 'DEBUG'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    'xml': XmlConfig,
    'dict': DictConfig
} 