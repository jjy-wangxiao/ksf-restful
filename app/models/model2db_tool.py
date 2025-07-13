# orm建表工具，用于将模型文件中的表结构转换为数据库表

# 使用方法：
# python model2db_tool.py --reset
# 如果需要清空所有表数据，则使用 --reset 参数
# 如果不需要清空所有表数据，则不使用 --reset 参数




import argparse
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ksf.model.models_dict import Base as dict_Base

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="批量导入13jt文件到数据库")
    parser.add_argument('--reset', action='store_true', help='导入前清空所有表数据')
    args = parser.parse_args()

    # 数据库配置 - 优化连接参数
    DATABASE_URL = "sqlite:///dict_database.db"
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
    
        
    if args.reset:
        print("[警告] 正在清空所有表数据...")
        # 如果表已存在，则先删除表
        # 删除所有表
        dict_Base.metadata.drop_all(engine)
        print("所有表数据已清空。")
    
    # 创建所有表
    dict_Base.metadata.create_all(engine)
    print("所有表数据已创建。")

if __name__ == "__main__":
    import sys
    # sys.argv.append('--reset')
    main() 