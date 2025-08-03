#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
动态解析13jt文件并通过ORM存储到数据库
根据XML标签名自动匹配模型类，避免硬编码
性能优化版本 - 按文件批量处理
"""

import os
import sys
import glob
import xml.etree.ElementTree as ET
from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from typing import Dict, Any, Optional
import argparse
import hashlib

# 项目根目录已经在pyproject.toml中配置

# from app.models.models_13jt import Base
import app.models.models_13jt as models_13jt

# 动态导入所有模型类
def get_all_models():
    """动态获取所有模型类"""
    models = {}
    for attr_name in dir(models_13jt):
        attr = getattr(models_13jt, attr_name)
        if hasattr(attr, '__tablename__'):
            if "origin_13jt_" in attr.__tablename__:
                # 使用表名作为键，模型类作为值
                models[attr.__tablename__] = attr
    return models

def get_13jt_files(directory):
    """获取13jt目录下的所有文件，扩展名包含大小写，不包含子目录"""
    pattern1 = os.path.join(directory, "*.13jt")
    pattern2 = os.path.join(directory, "*.13JT")
    
    files = []
    files.extend(glob.glob(pattern1))
    files.extend(glob.glob(pattern2))
    
    return files

def xml_to_dict(element):
    """将XML元素转换为字典"""
    result = {}
    
    # 处理属性 - 这是主要的数据来源
    for key, value in element.attrib.items():
        # 将属性名转换为小写，匹配数据库字段
        field_name = key.lower()
        result[field_name] = value
    
    # 处理子元素的文本内容（如果有的话）
    if element.text and element.text.strip():
        result['text'] = element.text.strip()
    
    return result

def create_model_instance(model_class, data):
    """创建模型实例"""
    instance = model_class()
    
    # 设置时间戳
    # now = datetime.now()
    # instance.create_time = now
    # instance.update_time = now
    
    # 动态设置字段值
    for key, value in data.items():
        if hasattr(instance, key) and value is not None:
            setattr(instance, key, str(value))
    
    return instance

def find_foreign_key_field(child_model, parent_table_name):
    """通过分析模型字段自动查找外键字段"""
    # 直接根据表名推断外键字段名
    expected_field_name = f"{parent_table_name}_id"
    
    # 检查字段是否存在
    if hasattr(child_model, expected_field_name):
        return expected_field_name
    
    return None

def process_xml_element(element, models, session, parent_chain=None):
    """递归处理XML元素，支持多层级外键关系"""
    #加入异常处理，如果模型不存在则抛出异常
    try:
        tag_name = element.tag.lower()
        
        # 初始化父级链
        if parent_chain is None:
            parent_chain = []
        
        # 查找对应的模型类
        model_class = None
        for table_name, model in models.items():
            if table_name == "origin_13jt_"+tag_name:
                model_class = model
                break
        
        if model_class:
            # 转换XML为字典
            data = xml_to_dict(element)
            
            # 创建模型实例
            instance = create_model_instance(model_class, data)
            
            # 设置多层级外键关系
            for parent_info in parent_chain:
                parent_id, parent_field = parent_info
                if hasattr(instance, parent_field):
                    setattr(instance, parent_field, parent_id)
            
            # 添加到session并立即flush以获取ID
            session.add(instance)

            # 如果有子节点，则需要先flush，否则子节点会找不到父节点id
            if len(element) > 0: 
                session.flush()  # 立即刷新以获取ID
            
                # 更新父级链，添加当前元素
                current_parent_chain = parent_chain + [(instance.id, f"{tag_name}_id")]
            
                # 处理子元素
                for child in element:
                    process_xml_element(child, models, session, current_parent_chain)
                    
        else:
            # 如果没有找到对应的模型，递归处理子元素
            for child in element:
                process_xml_element(child, models, session, parent_chain)
    except Exception as e:
        print(f"处理xml元素时出错: {e}")
        raise

def import_13jt_file(file_path, models, session, fileid):
    """导入单个13jt文件"""
    try:
        print(f"-"*100)
        print(f"正在处理文件: {os.path.basename(file_path)}")
        
        # 创建文件模型
        file_model = None
        for table_name, model in models.items():
            if table_name == 'origin_13jt_file':
                file_model = model
                break

        if file_model:
            file_instance = file_model(
                id = fileid,
                filename=os.path.basename(file_path),
                filesize=os.path.getsize(file_path),
                filetype=os.path.basename(file_path).split('.')[-1].lower()
            )
            # 计算文件hash
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
                file_instance.hash = file_hash
        else:
            raise Exception("未找到文件模型")

        # session.add(file_instance)
        # session.flush()

        current_parent_chain = [(file_instance.id, 'file_id')]

        # 解析XML
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # 处理根元素
        process_xml_element(root, models, session, current_parent_chain)
        
        # 文件处理完成，提交事务
        session.commit()
        print(f"✓ 成功导入: {os.path.basename(file_path)}")
        
    except Exception as e:
        session.rollback()
        print(f"✗ 导入失败: 错误信息：\r\n{str(e)}\r\n")
        raise

def clear_all_tables(session, Base):
    """清空所有表数据"""
    # 关闭外键约束（sqlite）
    # 判断数据库类型，分别处理sqlite和mysql
    engine = session.get_bind()
    db_dialect = engine.dialect.name.lower()
    if db_dialect == 'sqlite':
        session.execute(text('PRAGMA foreign_keys = OFF;'))
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()
        session.execute(text('PRAGMA foreign_keys = ON;'))
    elif db_dialect == 'mysql':
        # 关闭外键约束
        session.execute(text('SET FOREIGN_KEY_CHECKS=0;'))
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()
        # 恢复外键约束
        session.execute(text('SET FOREIGN_KEY_CHECKS=1;'))
    elif db_dialect == 'postgresql':
        # 关闭外键约束
        session.execute(text('SET session_replication_role = replica;'))
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()
        # 恢复外键约束
        session.execute(text('SET session_replication_role = DEFAULT;'))
    else:
        # 其他数据库，直接删除
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="批量导入13jt文件到数据库")
    parser.add_argument('--reset', action='store_true', help='导入前清空所有表数据')
    args = parser.parse_args()

    # 数据库配置 - 优化连接参数
    # DATABASE_URL = "mysql+pymysql://ksf_restx_dev:ksf_restx_dev@192.168.110.129:3306/ksf_restx_dev"
    DATABASE_URL = "sqlite:///db.sqlite"

    # 创建数据库引擎
    if "mysql" in DATABASE_URL.lower():
        engine = create_engine(
        DATABASE_URL, 
        echo=False,
        pool_pre_ping=True,
        pool_recycle=3600,
        connect_args={
                "connect_timeout": 30,
                "read_timeout": 30,
                "write_timeout": 30
            }
        )
    else:
        engine = create_engine(
            DATABASE_URL, 
            echo=False,
            pool_pre_ping=True,
            pool_recycle=3600,
            connect_args={
                "timeout": 30,
                "check_same_thread": False
            }
        )
    
    # 创建所有表
    Base.metadata.create_all(engine)
    
    # 获取所有模型类
    models = get_all_models()
    print(f"找到 {len(models)} 个模型类")
    
    # 创建会话
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # 是否清空所有表
    if args.reset:
        print("[警告] 正在清空所有表数据...")
        clear_all_tables(session, Base)
        print("所有表数据已清空。")
    
    # 获取13jt文件列表
    directory = "resources/13jt"
    files = get_13jt_files(directory)
    
    if not files:
        print(f"在 {directory} 目录下没有找到.13jt或.13JT文件")
        return
    
    print(f"找到 {len(files)} 个13jt文件")
    
    # 导入所有文件
    success_count = 0
    total_start_time = datetime.now()
    
    for i, file_path in enumerate(files, 1):
        try:
            file_start_time = datetime.now()
            import_13jt_file(file_path, models, session)
            file_end_time = datetime.now()
            file_duration = (file_end_time - file_start_time).total_seconds()
            print(f"文件 {i}/{len(files)} 处理完成，耗时: {file_duration:.2f}秒")
            success_count += 1
        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {e}\r\n")
            continue
    
    total_end_time = datetime.now()
    total_duration = (total_end_time - total_start_time).total_seconds()
    
    print(f"\n导入完成: {success_count}/{len(files)} 个文件成功导入")
    print(f"总耗时: {total_duration:.2f}秒")
    print(f"平均每个文件: {total_duration/len(files):.2f}秒")
    print(f"-"*100)
    
    # 关闭会话
    session.close()

if __name__ == "__main__":
    import sys
    # sys.argv.append('--reset')
    main() 