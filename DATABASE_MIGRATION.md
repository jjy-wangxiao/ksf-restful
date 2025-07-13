# 数据库迁移使用指南

本项目使用 Flask-Migrate 进行数据库版本管理，确保数据库结构的变更能够被追踪和管理。

## 🚀 快速开始

### 1. 初始化迁移系统（首次使用）

```bash
# 初始化migration系统
python manage.py init_migrations
```

这会在项目根目录创建 `migrations/` 文件夹，包含迁移相关的文件。

### 2. 生成第一个迁移

```bash
# 生成初始迁移
python manage.py migrate -m "Initial migration"
```

### 3. 应用迁移

```bash
# 应用所有待执行的迁移
python manage.py upgrade
```

## 📋 常用命令

### 基础命令

```bash
# 检查数据库连接
python manage.py check

# 初始化数据库（不使用migration）
python manage.py init_db

# 重置数据库
python manage.py reset

# 填充示例数据
python manage.py seed
```

### 迁移命令

```bash
# 生成新的迁移文件
python manage.py migrate -m "描述变更内容"

# 应用迁移
python manage.py upgrade

# 回滚最后一次迁移
python manage.py downgrade

# 查看迁移历史
python manage.py history

# 查看当前数据库版本
python manage.py current

# 查看所有迁移
python manage.py show
```

### 直接使用Flask命令

```bash
# 初始化migration系统
flask db init

# 生成迁移
flask db migrate -m "迁移描述"

# 应用迁移
flask db upgrade

# 回滚迁移
flask db downgrade

# 查看历史
flask db history

# 查看当前版本
flask db current

# 查看所有迁移
flask db show
```

## 🔄 工作流程

### 开发新功能时的流程

1. **修改模型** - 在 `app/models/` 中修改或添加模型
2. **生成迁移** - 运行 `python manage.py migrate -m "描述变更"`
3. **检查迁移文件** - 查看 `migrations/versions/` 中的迁移文件
4. **应用迁移** - 运行 `python manage.py upgrade`
5. **测试验证** - 确保功能正常工作

### 示例工作流程

```bash
# 1. 添加新字段到模型
# 编辑 app/models/dict.py，添加新字段

# 2. 生成迁移
python manage.py migrate -m "Add new field to DwType model"

# 3. 检查生成的迁移文件
# 查看 migrations/versions/xxx_add_new_field_to_dwtype_model.py

# 4. 应用迁移
python manage.py upgrade

# 5. 验证变更
python manage.py check
```

## 📁 项目结构

```
ksf-restful/
├── migrations/                 # 迁移文件目录
│   ├── versions/              # 迁移版本文件
│   │   ├── 001_initial_migration.py
│   │   ├── 002_add_new_field.py
│   │   └── ...
│   ├── alembic.ini           # Alembic配置文件
│   ├── env.py                # 迁移环境配置
│   ├── README                # 迁移说明
│   └── script.py.mako        # 迁移模板
├── app/
│   ├── models/               # 数据模型
│   │   ├── __init__.py       # 模型导入
│   │   └── dict.py           # 具体模型
│   └── ...
├── manage.py                 # 数据库管理脚本
└── ...
```

## ⚙️ 环境配置

### 开发环境

```bash
# .env 文件
FLASK_CONFIG=development
DEV_DATABASE_URL=sqlite:///data-dev.sqlite
```

### 测试环境

```bash
# 测试环境使用内存数据库
FLASK_CONFIG=testing
TEST_DATABASE_URL=sqlite:///:memory:
```

### 生产环境

```bash
# 生产环境使用PostgreSQL
FLASK_CONFIG=production
DATABASE_URL=postgresql://user:pass@host:5432/dbname
```

## 🔧 高级配置

### 自定义迁移模板

可以修改 `migrations/script.py.mako` 来自定义迁移文件的模板。

### 数据迁移

对于需要迁移数据的复杂变更，可以在迁移文件中添加数据迁移逻辑：

```python
def upgrade():
    # 结构变更
    op.add_column('dw_type', sa.Column('new_field', sa.String(50)))
    
    # 数据迁移
    connection = op.get_bind()
    connection.execute("UPDATE dw_type SET new_field = 'default_value'")

def downgrade():
    op.drop_column('dw_type', 'new_field')
```

### 多数据库支持

如果需要支持多个数据库，可以在 `migrations/env.py` 中配置多个数据库连接。

## 🚨 注意事项

### 1. 迁移文件管理

- **不要删除迁移文件** - 迁移文件是数据库变更的历史记录
- **不要手动修改迁移文件** - 除非你非常了解Alembic的工作原理
- **备份重要数据** - 在生产环境应用迁移前，务必备份数据库

### 2. 团队协作

- **提交迁移文件** - 将生成的迁移文件提交到版本控制系统
- **同步迁移** - 团队成员需要及时应用新的迁移
- **冲突处理** - 如果多个分支都有迁移，需要手动解决冲突

### 3. 生产环境

- **测试迁移** - 在生产环境应用迁移前，在测试环境验证
- **备份策略** - 建立完善的数据库备份策略
- **回滚计划** - 准备迁移失败时的回滚方案

## 🐛 常见问题

### Q: 迁移文件生成失败怎么办？

A: 检查模型定义是否正确，确保所有模型都已正确导入。

### Q: 如何回滚到特定版本？

A: 使用 `flask db downgrade <revision_id>` 命令。

### Q: 迁移文件冲突怎么解决？

A: 手动编辑冲突的迁移文件，或者重新生成迁移文件。

### Q: 如何查看迁移的SQL语句？

A: 使用 `flask db upgrade --sql` 命令查看SQL语句而不执行。

## 📚 相关资源

- [Flask-Migrate 文档](https://flask-migrate.readthedocs.io/)
- [Alembic 文档](https://alembic.sqlalchemy.org/)
- [SQLAlchemy 文档](https://docs.sqlalchemy.org/) 