from app import create_app, db
from app.models import User, Post

app = create_app()

@app.shell_context_processor
def make_shell_context():
    """Flask shell上下文"""
    return {
        'db': db,
        'User': User,
        'Post': Post
    }

if __name__ == '__main__':
    app.run(debug=True) 