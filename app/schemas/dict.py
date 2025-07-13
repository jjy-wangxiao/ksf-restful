from marshmallow import Schema, fields, validate, validates, ValidationError
from datetime import datetime

class DwTypeSchema(Schema):
    """单位类别序列化模式"""
    id = fields.Str(required=True, validate=validate.Length(equal=2), description='单位类别ID')
    typeName = fields.Str(required=True, validate=validate.Length(min=1, max=10), description='类别名称')
    create_time = fields.DateTime(dump_only=True)
    update_time = fields.DateTime(dump_only=True)

class DwTypeCreateSchema(Schema):
    """单位类别创建模式"""
    id = fields.Str(required=True, validate=validate.Length(equal=2), description='单位类别ID')
    typeName = fields.Str(required=True, validate=validate.Length(min=1, max=10), description='类别名称')

class DwTypeUpdateSchema(Schema):
    """单位类别更新模式"""
    typeName = fields.Str(validate=validate.Length(min=1, max=10), description='类别名称')

class DwSchema(Schema):
    """单位序列化模式"""
    id = fields.Str(required=True, validate=validate.Length(equal=4), description='单位ID')
    type_id = fields.Str(validate=validate.Length(equal=2), description='类别ID')
    dw = fields.Str(required=True, validate=validate.Length(min=1, max=10), description='单位名称')
    create_time = fields.DateTime(dump_only=True)
    update_time = fields.DateTime(dump_only=True)
    type = fields.Nested(DwTypeSchema, dump_only=True)

class DwCreateSchema(Schema):
    """单位创建模式"""
    id = fields.Str(required=True, validate=validate.Length(equal=4), description='单位ID')
    type_id = fields.Str(validate=validate.Length(equal=2), description='类别ID')
    dw = fields.Str(required=True, validate=validate.Length(min=1, max=10), description='单位名称')

class DwUpdateSchema(Schema):
    """单位更新模式"""
    type_id = fields.Str(validate=validate.Length(equal=2), description='类别ID')
    dw = fields.Str(validate=validate.Length(min=1, max=10), description='单位名称')

class RcjEjflSxSchema(Schema):
    """人材机二级分类属性序列化模式"""
    id = fields.Str(required=True, validate=validate.Length(equal=4), description='属性ID')
    sx = fields.Str(required=True, validate=validate.Length(min=1, max=10), description='属性名称')
    create_time = fields.DateTime(dump_only=True)
    update_time = fields.DateTime(dump_only=True)

class RcjEjflSxCreateSchema(Schema):
    """人材机二级分类属性创建模式"""
    id = fields.Str(required=True, validate=validate.Length(equal=4), description='属性ID')
    sx = fields.Str(required=True, validate=validate.Length(min=1, max=10), description='属性名称')

class RcjEjflSxUpdateSchema(Schema):
    """人材机二级分类属性更新模式"""
    sx = fields.Str(validate=validate.Length(min=1, max=10), description='属性名称')

class RcjYjflSchema(Schema):
    """人材机一级分类序列化模式"""
    id = fields.Str(required=True, validate=validate.Length(equal=4), description='一级分类ID')
    yjflmc = fields.Str(required=True, validate=validate.Length(min=1, max=100), description='一级分类名称')
    yjflms = fields.Str(validate=validate.Length(max=100), description='一级分类描述')
    create_time = fields.DateTime(dump_only=True)
    update_time = fields.DateTime(dump_only=True)

class RcjYjflCreateSchema(Schema):
    """人材机一级分类创建模式"""
    id = fields.Str(required=True, validate=validate.Length(equal=4), description='一级分类ID')
    yjflmc = fields.Str(required=True, validate=validate.Length(min=1, max=100), description='一级分类名称')
    yjflms = fields.Str(validate=validate.Length(max=100), description='一级分类描述')

class RcjYjflUpdateSchema(Schema):
    """人材机一级分类更新模式"""
    yjflmc = fields.Str(validate=validate.Length(min=1, max=100), description='一级分类名称')
    yjflms = fields.Str(validate=validate.Length(max=100), description='一级分类描述')

class RcjEjflSchema(Schema):
    """人材机二级分类序列化模式"""
    id = fields.Str(required=True, validate=validate.Length(equal=4), description='二级分类ID')
    yjfl_id = fields.Str(validate=validate.Length(equal=2), description='一级分类ID')
    ejflmc = fields.Str(required=True, validate=validate.Length(min=1, max=100), description='二级分类名称')
    ejflms = fields.Str(validate=validate.Length(max=100), description='二级分类描述')
    create_time = fields.DateTime(dump_only=True)
    update_time = fields.DateTime(dump_only=True)
    yjfl = fields.Nested(RcjYjflSchema, dump_only=True)
    sxs = fields.List(fields.Str(), dump_only=True, description='关联的属性列表')
    dws = fields.List(fields.Str(), dump_only=True, description='关联的单位列表')

class RcjEjflCreateSchema(Schema):
    """人材机二级分类创建模式"""
    id = fields.Str(required=True, validate=validate.Length(equal=4), description='二级分类ID')
    yjfl_id = fields.Str(validate=validate.Length(equal=2), description='一级分类ID')
    ejflmc = fields.Str(required=True, validate=validate.Length(min=1, max=100), description='二级分类名称')
    ejflms = fields.Str(validate=validate.Length(max=100), description='二级分类描述')
    sx_ids = fields.List(fields.Str(), description='关联的属性ID列表')
    dw_ids = fields.List(fields.Str(), description='关联的单位ID列表')

class RcjEjflUpdateSchema(Schema):
    """人材机二级分类更新模式"""
    yjfl_id = fields.Str(validate=validate.Length(equal=2), description='一级分类ID')
    ejflmc = fields.Str(validate=validate.Length(min=1, max=100), description='二级分类名称')
    ejflms = fields.Str(validate=validate.Length(max=100), description='二级分类描述')
    sx_ids = fields.List(fields.Str(), description='关联的属性ID列表')
    dw_ids = fields.List(fields.Str(), description='关联的单位ID列表')

class RcjMC2EjflidSchema(Schema):
    """人材机名称到二级分类ID映射序列化模式"""
    id = fields.Int(dump_only=True)
    ejflid = fields.Str(required=True, validate=validate.Length(equal=4), description='二级分类ID')
    orignal_rcjmc = fields.Str(required=True, validate=validate.Length(min=1, max=50), description='原始人材机名称')
    create_time = fields.DateTime(dump_only=True)
    update_time = fields.DateTime(dump_only=True)

class RcjMC2EjflidCreateSchema(Schema):
    """人材机名称到二级分类ID映射创建模式"""
    ejflid = fields.Str(required=True, validate=validate.Length(equal=4), description='二级分类ID')
    orignal_rcjmc = fields.Str(required=True, validate=validate.Length(min=1, max=50), description='原始人材机名称')

class RcjMC2EjflidUpdateSchema(Schema):
    """人材机名称到二级分类ID映射更新模式"""
    ejflid = fields.Str(validate=validate.Length(equal=4), description='二级分类ID')
    orignal_rcjmc = fields.Str(validate=validate.Length(min=1, max=50), description='原始人材机名称')

class RcjMCClassifySchema(Schema):
    """人材机名称分类序列化模式"""
    id = fields.Int(dump_only=True)
    cleaned_rcj_original_mc = fields.Str(required=True, validate=validate.Length(min=1, max=100), description='清洗后的人材机名称')
    yjflid = fields.Str(validate=validate.Length(equal=2), description='一级分类ID')
    yjflmc = fields.Str(validate=validate.Length(max=10), description='一级分类名称')
    ejflid = fields.Str(validate=validate.Length(equal=4), description='二级分类ID')
    ejflmc = fields.Str(validate=validate.Length(max=10), description='二级分类名称')
    create_time = fields.DateTime(dump_only=True)
    update_time = fields.DateTime(dump_only=True)

class RcjMCClassifyCreateSchema(Schema):
    """人材机名称分类创建模式"""
    cleaned_rcj_original_mc = fields.Str(required=True, validate=validate.Length(min=1, max=100), description='清洗后的人材机名称')
    yjflid = fields.Str(validate=validate.Length(equal=2), description='一级分类ID')
    yjflmc = fields.Str(validate=validate.Length(max=10), description='一级分类名称')
    ejflid = fields.Str(validate=validate.Length(equal=4), description='二级分类ID')
    ejflmc = fields.Str(validate=validate.Length(max=10), description='二级分类名称')

class RcjMCClassifyUpdateSchema(Schema):
    """人材机名称分类更新模式"""
    cleaned_rcj_original_mc = fields.Str(validate=validate.Length(min=1, max=100), description='清洗后的人材机名称')
    yjflid = fields.Str(validate=validate.Length(equal=2), description='一级分类ID')
    yjflmc = fields.Str(validate=validate.Length(max=10), description='一级分类名称')
    ejflid = fields.Str(validate=validate.Length(equal=4), description='二级分类ID')
    ejflmc = fields.Str(validate=validate.Length(max=10), description='二级分类名称')
