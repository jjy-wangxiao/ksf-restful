from app import create_app, db

app = create_app()


if __name__ == '__main__':
    # 从配置中读取主机和端口
    host = app.config.get('HOST', '127.0.0.1')
    port = app.config.get('PORT', 5678)
    debug = app.config.get('DEBUG', False)

    
    app.run(host=host, port=port, debug=debug) 