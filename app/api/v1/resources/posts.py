from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.post import Post
from app.models.user import User
from app.schemas.post import PostSchema, PostCreateSchema
from app.utils.decorators import validate_json, admin_required
from app.utils.pagination import paginate

post_schema = PostSchema()
posts_schema = PostSchema(many=True)
post_create_schema = PostCreateSchema()

class PostListResource(Resource):
    """文章列表资源"""
    
    def get(self):
        """获取文章列表"""
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        published_only = request.args.get('published', 'true').lower() == 'true'
        
        query = Post.query
        if published_only:
            query = query.filter_by(published=True)
        
        posts = query.order_by(Post.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return paginate(posts, posts_schema)
    
    @jwt_required()
    @validate_json
    def post(self):
        """创建新文章"""
        current_user_id = get_jwt_identity()
        data = request.get_json()
        
        # 验证数据
        errors = post_create_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 创建文章
        post = Post(
            title=data['title'],
            content=data['content'],
            published=data.get('published', False),
            author_id=current_user_id
        )
        
        db.session.add(post)
        db.session.commit()
        
        return {
            'message': '文章创建成功',
            'post': post_schema.dump(post)
        }, 201

class PostResource(Resource):
    """单个文章资源"""
    
    def get(self, post_id):
        """获取文章详情"""
        post = Post.query.get_or_404(post_id)
        
        # 未发布的文章只有作者和管理员可以查看
        if not post.published:
            current_user_id = get_jwt_identity()
            if not current_user_id:
                return {'message': '文章不存在'}, 404
            
            current_user = User.query.get(current_user_id)
            if not current_user or (current_user.id != post.author_id and not current_user.is_admin):
                return {'message': '文章不存在'}, 404
        
        return {'post': post_schema.dump(post)}
    
    @jwt_required()
    @validate_json
    def put(self, post_id):
        """更新文章"""
        current_user_id = get_jwt_identity()
        post = Post.query.get_or_404(post_id)
        
        # 只有作者和管理员可以更新
        current_user = User.query.get(current_user_id)
        if current_user.id != post.author_id and not current_user.is_admin:
            return {'message': '权限不足'}, 403
        
        data = request.get_json()
        
        # 更新字段
        if 'title' in data:
            post.title = data['title']
        
        if 'content' in data:
            post.content = data['content']
        
        if 'published' in data:
            post.published = data['published']
        
        db.session.commit()
        
        return {
            'message': '文章更新成功',
            'post': post_schema.dump(post)
        }
    
    @jwt_required()
    def delete(self, post_id):
        """删除文章"""
        current_user_id = get_jwt_identity()
        post = Post.query.get_or_404(post_id)
        
        # 只有作者和管理员可以删除
        current_user = User.query.get(current_user_id)
        if current_user.id != post.author_id and not current_user.is_admin:
            return {'message': '权限不足'}, 403
        
        db.session.delete(post)
        db.session.commit()
        
        return {'message': '文章删除成功'}, 200 