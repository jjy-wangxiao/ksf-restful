import os
import click
from flask.cli import with_appcontext
from app import create_app, db
from app.models import User, Post

app = create_app()

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """运行测试"""
    import pytest
    if test_names:
        pytest.main(list(test_names))
    else:
        pytest.main()

@app.cli.command()
@with_appcontext
def init_db():
    """初始化数据库"""
    db.create_all()
    click.echo('数据库表创建完成')

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
    
    # 生成用户
    User.generate_fake(10)
    click.echo('生成10个测试用户')
    
    # 生成文章
    Post.generate_fake(50)
    click.echo('生成50篇测试文章')

if __name__ == '__main__':
    app.cli() 