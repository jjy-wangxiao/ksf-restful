from flask import request
from flask_restx import Resource, fields
from app import db
from app.models.post import Post
from app.models.user import User
from app.schemas.post import PostSchema, PostCreateSchema
from app.utils.decorators import validate_json
from app.utils.pagination import paginate
from app.swagger import posts_ns, message_model, error_model, pagination_model

post_schema = PostSchema()
posts_schema = PostSchema(many=True)
post_create_schema = PostCreateSchema()

# 定义模型
post_model = posts_ns.model('Post', {
    'id': fields.String(description='文章ID'),
    'title': fields.String(description='标题'),
    'content': fields.String(description='内容'),
    'published': fields.Boolean(description='是否发布'),
    'author_id': fields.String(description='作者ID'),
    'author': fields.String(description='作者名'),
    'created_at': fields.DateTime(description='创建时间'),
    'updated_at': fields.DateTime(description='更新时间')
})

post_create_model = posts_ns.model('PostCreate', {
    'title': fields.String(required=True, description='标题'),
    'content': fields.String(description='内容'),
    'published': fields.Boolean(description='是否发布', default=False),
    'author_id': fields.String(description='作者ID')
})

post_update_model = posts_ns.model('PostUpdate', {
    'title': fields.String(description='标题'),
    'content': fields.String(description='内容'),
    'published': fields.Boolean(description='是否发布')
})

post_list_response = posts_ns.model('PostListResponse', {
    'items': fields.List(fields.Nested(post_model), description='文章列表'),
    'pagination': fields.Nested(pagination_model, description='分页信息')
})

@posts_ns.route('/')
class PostListResource(Resource):
    """文章列表资源"""
    
    @posts_ns.doc('获取文章列表')
    @posts_ns.param('page', '页码', type=int, default=1)
    @posts_ns.param('per_page', '每页数量', type=int, default=10)
    @posts_ns.param('published', '是否只显示已发布', type=bool, default=True)
    @posts_ns.response(200, '获取成功', post_list_response)
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
    
    @posts_ns.doc('创建新文章')
    @posts_ns.expect(post_create_model)
    @posts_ns.response(201, '创建成功', post_model)
    @posts_ns.response(400, '数据验证失败', error_model)
    @validate_json
    def post(self):
        """创建新文章"""
        data = request.get_json()
        
        # 验证数据
        errors = post_create_schema.validate(data)
        if errors:
            return {'message': '数据验证失败', 'errors': errors}, 400
        
        # 检查作者是否存在
        author_id = data.get('author_id')
        if author_id:
            author = User.query.get(author_id)
            if not author:
                return {'message': '指定的作者不存在'}, 400
        else:
            # 如果没有指定作者，使用第一个用户作为默认作者
            author = User.query.first()
            if not author:
                return {'message': '没有可用的用户作为作者'}, 400
            author_id = author.id
        
        # 创建文章
        post = Post(
            title=data['title'],
            content=data['content'],
            published=data.get('published', False),
            author_id=author_id
        )
        
        db.session.add(post)
        db.session.commit()
        
        return {
            'message': '文章创建成功',
            'post': post_schema.dump(post)
        }, 201

@posts_ns.route('/<string:post_id>')
@posts_ns.param('post_id', '文章ID')
class PostResource(Resource):
    """单个文章资源"""
    
    @posts_ns.doc('获取文章详情')
    @posts_ns.response(200, '获取成功', post_model)
    @posts_ns.response(404, '文章不存在', error_model)
    def get(self, post_id):
        """获取文章详情"""
        post = Post.query.get_or_404(post_id)
        return {'post': post_schema.dump(post)}
    
    @posts_ns.doc('更新文章')
    @posts_ns.expect(post_update_model)
    @posts_ns.response(200, '更新成功', post_model)
    @posts_ns.response(400, '数据验证失败', error_model)
    @posts_ns.response(404, '文章不存在', error_model)
    @validate_json
    def put(self, post_id):
        """更新文章"""
        post = Post.query.get_or_404(post_id)
        
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
    
    @posts_ns.doc('删除文章')
    @posts_ns.response(200, '删除成功', message_model)
    @posts_ns.response(404, '文章不存在', error_model)
    def delete(self, post_id):
        """删除文章"""
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        
        return {'message': '文章删除成功'}, 200 