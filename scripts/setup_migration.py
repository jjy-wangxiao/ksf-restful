#!/usr/bin/env python3
"""
自动化设置数据库迁移的脚本
"""
import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """运行命令并处理错误"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} 完成")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} 失败: {e}")
        print(f"错误输出: {e.stderr}")
        return None

def check_flask_app():
    """检查Flask应用配置"""
    print("🔍 检查Flask应用配置...")
    
    # 检查必要的文件
    required_files = ['run.py', 'app/__init__.py', 'config.py']
    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"❌ 缺少必要文件: {file_path}")
            return False
    
    # 检查环境变量
    flask_app = os.environ.get('FLASK_APP')
    if not flask_app:
        os.environ['FLASK_APP'] = 'run.py'
        print("✅ 设置 FLASK_APP=run.py")
    
    return True

def setup_migration():
    """设置数据库迁移"""
    print("🚀 开始设置数据库迁移系统...")
    
    # 检查Flask应用配置
    if not check_flask_app():
        print("❌ Flask应用配置检查失败")
        return False
    
    # 检查migrations目录是否已存在
    migrations_dir = Path('migrations')
    if migrations_dir.exists():
        print("⚠️  migrations目录已存在，跳过初始化")
    else:
        # 初始化migration系统
        result = run_command('flask db init', '初始化migration系统')
        if not result:
            return False
    
    # 生成初始迁移
    result = run_command('flask db migrate -m "Initial migration"', '生成初始迁移')
    if not result:
        return False
    
    # 应用迁移
    result = run_command('flask db upgrade', '应用迁移')
    if not result:
        return False
    
    print("🎉 数据库迁移系统设置完成！")
    return True

def show_usage():
    """显示使用说明"""
    print("""
📋 数据库迁移使用说明:

1. 生成新的迁移:
   python manage.py migrate -m "描述变更"

2. 应用迁移:
   python manage.py upgrade

3. 回滚迁移:
   python manage.py downgrade

4. 查看迁移历史:
   python manage.py history

5. 查看当前版本:
   python manage.py current

或者直接使用Flask命令:
   flask db migrate -m "描述"
   flask db upgrade
   flask db downgrade
   flask db history
   flask db current
""")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        show_usage()
    else:
        success = setup_migration()
        if success:
            show_usage()
        else:
            sys.exit(1) 