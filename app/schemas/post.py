from marshmallow import Schema, fields, validate

class PostSchema(Schema):
    """文章序列化模式"""
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    content = fields.Str()
    published = fields.Bool()
    author_id = fields.Str(dump_only=True)
    author = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class PostCreateSchema(Schema):
    """文章创建模式"""
    title = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    content = fields.Str(required=True, validate=validate.Length(min=1))
    published = fields.Bool(missing=False)

class PostUpdateSchema(Schema):
    """文章更新模式"""
    title = fields.Str(validate=validate.Length(min=1, max=200))
    content = fields.Str(validate=validate.Length(min=1))
    published = fields.Bool() 