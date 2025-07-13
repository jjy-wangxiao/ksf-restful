"""
数据模型模块
导入所有模型以确保Flask-Migrate能够检测到
"""

# 导入所有模型
from .dict import (
    DwType,
    Dw,
    RcjEjflSx,
    RcjYjfl,
    RcjEjfl,
    RcjMC2Ejflid,
    RcjMCClassify
)

# 导出所有模型
__all__ = [
    'DwType',
    'Dw', 
    'RcjEjflSx',
    'RcjYjfl',
    'RcjEjfl',
    'RcjMC2Ejflid',
    'RcjMCClassify'
]
