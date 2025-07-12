from marshmallow import Schema, fields, validate, validates, ValidationError
import re

class UserSchema(Schema):
    """用户序列化模式"""
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=64))
    email = fields.Email(required=True)
    is_active = fields.Bool(dump_only=True)
    is_admin = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class UserCreateSchema(Schema):
    """用户创建模式"""
    username = fields.Str(required=True, validate=validate.Length(min=3, max=64))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6, max=128))
    
    @validates('username')
    def validate_username(self, value):
        """验证用户名格式"""
        if not re.match(r'^[a-zA-Z0-9_]+$', value):
            raise ValidationError('用户名只能包含字母、数字和下划线')
    
    @validates('password')
    def validate_password(self, value):
        """验证密码强度"""
        if len(value) < 6:
            raise ValidationError('密码长度至少6位')
        if not re.search(r'[A-Z]', value):
            raise ValidationError('密码必须包含至少一个大写字母')
        if not re.search(r'[a-z]', value):
            raise ValidationError('密码必须包含至少一个小写字母')
        if not re.search(r'\d', value):
            raise ValidationError('密码必须包含至少一个数字')

class UserUpdateSchema(Schema):
    """用户更新模式"""
    username = fields.Str(validate=validate.Length(min=3, max=64))
    email = fields.Email()
    password = fields.Str(validate=validate.Length(min=6, max=128))
    
    @validates('username')
    def validate_username(self, value):
        """验证用户名格式"""
        if not re.match(r'^[a-zA-Z0-9_]+$', value):
            raise ValidationError('用户名只能包含字母、数字和下划线')
    
    @validates('password')
    def validate_password(self, value):
        """验证密码强度"""
        if len(value) < 6:
            raise ValidationError('密码长度至少6位')
        if not re.search(r'[A-Z]', value):
            raise ValidationError('密码必须包含至少一个大写字母')
        if not re.search(r'[a-z]', value):
            raise ValidationError('密码必须包含至少一个小写字母')
        if not re.search(r'\d', value):
            raise ValidationError('密码必须包含至少一个数字') 