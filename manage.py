import os
import click
from flask.cli import with_appcontext
from app import create_app, db
import app.models  # 显式导入所有模型，确保db.create_all()生效
from app.models import User, Post
from app.models.dict import DwType, Dw, RcjEjflSx, RcjYjfl, RcjEjfl, RcjMC2Ejflid, RcjMCClassify

app = create_app()

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """运行测试"""
    import pytest
    if test_names:
        pytest.main(list(test_names))
    else:
        pytest.main(['tests/'])

@app.cli.command()
@with_appcontext
def init_db():
    """初始化数据库"""
    from app.models.user import User
    from app.models.post import Post
    db.create_all()
    click.echo('数据库表创建完成')
    # 调试输出
    click.echo(f'当前数据库URI: {db.engine.url}')
    inspector = db.inspect(db.engine)
    tables = inspector.get_table_names()
    click.echo(f'当前数据库所有表: {tables}')
    if not tables:
        click.echo('警告：没有任何表被创建，请检查模型导入和app context！')

@app.cli.command()
@with_appcontext
def create_admin():
    """创建管理员用户"""
    username = click.prompt('管理员用户名')
    email = click.prompt('管理员邮箱')
    password = click.prompt('管理员密码', hide_input=True)
    
    user = User(
        username=username,
        email=email,
        is_admin=True
    )
    user.password = password
    
    db.session.add(user)
    db.session.commit()
    
    click.echo(f'管理员用户 {username} 创建成功')

@app.cli.command()
@with_appcontext
def generate_fake_data():
    """生成测试数据"""
    from app.models.user import User
    from app.models.post import Post
    # 先确保表存在
    db.create_all()
    # 清空现有数据
    click.echo('清空现有数据...')
    db.session.query(Post).delete()
    db.session.query(User).delete()
    db.session.commit()
    click.echo('数据清空完成')
    # 生成用户
    click.echo('开始生成用户数据...')
    User.generate_fake(10)
    user_count = User.query.count()
    click.echo(f'生成{user_count}个测试用户')
    # 生成文章
    click.echo('开始生成文章数据...')
    Post.generate_fake(50)
    post_count = Post.query.count()
    click.echo(f'生成{post_count}篇测试文章')
    click.echo('测试数据生成完成！')

@app.cli.command()
def format_code():
    """格式化代码"""
    import subprocess
    try:
        subprocess.run(['black', '.'], check=True)
        click.echo('代码格式化完成')
    except subprocess.CalledProcessError:
        click.echo('代码格式化失败')
    except FileNotFoundError:
        click.echo('请先安装black: poetry add --group dev black')

@app.cli.command()
def lint():
    """代码检查"""
    import subprocess
    try:
        subprocess.run(['flake8', '.'], check=True)
        click.echo('代码检查通过')
    except subprocess.CalledProcessError:
        click.echo('代码检查失败')
    except FileNotFoundError:
        click.echo('请先安装flake8: poetry add --group dev flake8')

@app.cli.command()
def type_check():
    """类型检查"""
    import subprocess
    try:
        subprocess.run(['mypy', 'app'], check=True)
        click.echo('类型检查通过')
    except subprocess.CalledProcessError:
        click.echo('类型检查失败')
    except FileNotFoundError:
        click.echo('请先安装mypy: poetry add --group dev mypy')

@app.cli.command()
def docs():
    """启动API文档服务器"""
    import subprocess
    try:
        click.echo('启动API文档服务器...')
        click.echo('文档地址: http://localhost:5000/api/v1/docs')
        subprocess.run(['python', 'run.py'], check=True)
    except KeyboardInterrupt:
        click.echo('文档服务器已停止')

if __name__ == '__main__':
    app.cli() 