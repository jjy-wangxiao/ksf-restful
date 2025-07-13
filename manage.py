#!/usr/bin/env python3
"""
数据库管理脚本
提供数据库初始化、迁移等管理功能
"""
import os
import sys
import click
from flask.cli import FlaskGroup
from app import create_app, db
from app.models import *  # 导入所有模型以确保Flask-Migrate能检测到

# 设置环境变量
os.environ.setdefault('FLASK_APP', 'run.py')

app = create_app()
cli = FlaskGroup(app)

@cli.command()
def init_db():
    """初始化数据库"""
    click.echo('正在初始化数据库...')
    with app.app_context():
        db.create_all()
        click.echo('数据库初始化完成！')

@cli.command()
def drop_db():
    """删除所有表"""
    if click.confirm('确定要删除所有数据库表吗？此操作不可逆！'):
        click.echo('正在删除数据库表...')
        with app.app_context():
            db.drop_all()
            click.echo('数据库表删除完成！')

@cli.command()
def init_migrations():
    """初始化migration系统"""
    click.echo('正在初始化migration系统...')
    os.system('flask db init')
    click.echo('migration系统初始化完成！')

@cli.command()
@click.option('--message', '-m', help='迁移消息')
def migrate(message):
    """生成新的迁移文件"""
    if not message:
        message = click.prompt('请输入迁移消息')
    
    click.echo(f'正在生成迁移文件: {message}')
    os.system(f'flask db migrate -m "{message}"')
    click.echo('迁移文件生成完成！')

@cli.command()
def upgrade():
    """应用所有待执行的迁移"""
    click.echo('正在应用数据库迁移...')
    os.system('flask db upgrade')
    click.echo('数据库迁移应用完成！')

@cli.command()
def downgrade():
    """回滚最后一次迁移"""
    if click.confirm('确定要回滚最后一次迁移吗？'):
        click.echo('正在回滚最后一次迁移...')
        os.system('flask db downgrade')
        click.echo('迁移回滚完成！')

@cli.command()
def history():
    """显示迁移历史"""
    click.echo('迁移历史:')
    os.system('flask db history')

@cli.command()
def current():
    """显示当前数据库版本"""
    click.echo('当前数据库版本:')
    os.system('flask db current')

@cli.command()
def show():
    """显示所有迁移"""
    click.echo('所有迁移:')
    os.system('flask db show')

@cli.command()
def reset():
    """重置数据库（删除所有表并重新创建）"""
    if click.confirm('确定要重置数据库吗？所有数据将丢失！'):
        click.echo('正在重置数据库...')
        with app.app_context():
            db.drop_all()
            db.create_all()
        click.echo('数据库重置完成！')

@cli.command()
def seed():
    """填充示例数据"""
    click.echo('正在填充示例数据...')
    with app.app_context():
        # 这里可以添加示例数据填充逻辑
        # 例如：创建默认用户、基础配置等
        click.echo('示例数据填充完成！')

@cli.command()
def check():
    """检查数据库连接"""
    click.echo('正在检查数据库连接...')
    try:
        with app.app_context():
            # 使用新的SQLAlchemy语法
            with db.engine.connect() as conn:
                conn.execute(db.text('SELECT 1'))
            click.echo('✅ 数据库连接正常！')
    except Exception as e:
        click.echo(f'❌ 数据库连接失败: {e}')

if __name__ == '__main__':
    cli() 