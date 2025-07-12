from app import db
from datetime import datetime
import uuid

class Post(db.Model):
    """文章模型"""
    __tablename__ = 'posts'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    published = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 外键
    author_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    
    def __repr__(self):
        return f'<Post {self.title}>'
    
    def to_dict(self):
        """转换为字典"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'published': self.published,
            'author_id': self.author_id,
            'author': self.author.username if self.author else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @staticmethod
    def generate_fake(count=100):
        """生成测试数据"""
        from random import seed, randint
        import forgery_py
        from app.models.user import User
        
        seed()
        user_count = User.query.count()
        for i in range(count):
            u = User.query.offset(randint(0, user_count - 1)).first()
            p = Post(
                title=forgery_py.lorem_ipsum.title(),
                content=forgery_py.lorem_ipsum.paragraphs(),
                published=True,
                author=u
            )
            db.session.add(p)
        db.session.commit() 