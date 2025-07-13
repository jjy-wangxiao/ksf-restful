from app import db
from datetime import datetime
import uuid
import random

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
        from app.models.user import User
        
        # 预定义的文章标题和内容模板
        titles = [
            "如何提高编程效率", "Python开发最佳实践", "Flask框架入门指南", 
            "RESTful API设计原则", "数据库优化技巧", "前端开发趋势", 
            "机器学习基础", "云计算技术解析", "DevOps实践指南", 
            "微服务架构设计", "网络安全防护", "移动应用开发", 
            "大数据处理技术", "人工智能应用", "区块链技术详解"
        ]
        
        content_templates = [
            "这是一篇关于{title}的详细文章。我们将从基础概念开始，逐步深入探讨相关技术和最佳实践。",
            "在本文中，我们将全面介绍{title}的相关知识。通过实际案例和代码示例，帮助读者更好地理解和应用。",
            "{title}是当前技术领域的热门话题。本文将为您提供深入的分析和实用的建议。",
            "本文将详细讲解{title}的核心概念、实现方法和应用场景。适合初学者和有经验的开发者阅读。",
            "通过本文，您将了解到{title}的最新发展动态、技术要点和实践经验。"
        ]
        
        user_count = User.query.count()
        if user_count == 0:
            # 如果没有用户，先创建一个默认用户
            default_user = User(
                username='default_author',
                email='default@example.com',
                password='password123'
            )
            db.session.add(default_user)
            db.session.commit()
            user_count = 1
        
        for i in range(count):
            # 随机选择一个用户作为作者
            u = User.query.offset(random.randint(0, user_count - 1)).first()
            
            # 生成随机标题
            base_title = random.choice(titles)
            title = f"{base_title} - 第{i+1}部分"
            
            # 生成随机内容
            content_template = random.choice(content_templates)
            content = content_template.format(title=base_title)
            content += f"\n\n这是第{i+1}篇文章的详细内容。包含了丰富的技术信息和实用的代码示例。"
            
            p = Post(
                title=title,
                content=content,
                published=random.choice([True, True, True, False]),  # 75%概率发布
                author_id=u.id
            )
            db.session.add(p)
        
        db.session.commit() 