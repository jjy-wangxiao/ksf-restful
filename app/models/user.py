from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid
import random
import string

class User(db.Model):
    """用户模型"""
    __tablename__ = 'users'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 关系
    posts = db.relationship('Post', backref='author', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """转换为字典"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_active': self.is_active,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @staticmethod
    def generate_fake(count=100):
        """生成测试数据"""
        from sqlalchemy.exc import IntegrityError
        
        # 预定义的用户名和邮箱前缀
        first_names = ['alice', 'bob', 'charlie', 'diana', 'edward', 'fiona', 'george', 'helen', 
                      'ivan', 'julia', 'kevin', 'lisa', 'mike', 'nancy', 'oscar', 'pamela']
        last_names = ['smith', 'johnson', 'williams', 'brown', 'jones', 'garcia', 'miller', 'davis']
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com']
        
        for i in range(count):
            # 生成随机用户名
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            number = random.randint(1, 999)
            username = f"{first_name}_{last_name}{number}"
            
            # 生成随机邮箱
            email = f"{first_name}.{last_name}{number}@{random.choice(domains)}"
            
            # 生成随机密码
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            
            u = User(
                username=username,
                email=email,
                password=password
            )
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback() 