# Poetry 使用指南

本项目使用 [Poetry](https://python-poetry.org/) 进行依赖管理。Poetry 是一个现代化的 Python 依赖管理和打包工具。

## 安装 Poetry

### macOS / Linux
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Windows
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### 使用 pip 安装
```bash
pip install poetry
```

## 基本使用

### 1. 安装依赖
```bash
# 安装所有依赖（包括开发依赖）
poetry install

# 只安装生产依赖
poetry install --only main

# 安装特定组的依赖
poetry install --only dev
poetry install --only test
```

### 2. 添加依赖
```bash
# 添加生产依赖
poetry add flask

# 添加开发依赖
poetry add --group dev pytest

# 添加测试依赖
poetry add --group test factory-boy

# 添加特定版本的依赖
poetry add "flask>=2.3.0,<3.0.0"
```

### 3. 移除依赖
```bash
# 移除依赖
poetry remove flask

# 移除开发依赖
poetry remove --group dev pytest
```

### 4. 更新依赖
```bash
# 更新所有依赖
poetry update

# 更新特定依赖
poetry update flask
```

### 5. 运行命令
```bash
# 在虚拟环境中运行命令
poetry run python run.py

# 激活虚拟环境
poetry shell

# 运行脚本（在 pyproject.toml 中定义）
poetry run ksf-restful
```

## 项目配置

### pyproject.toml 结构

```toml
[tool.poetry]
name = "ksf-restful"
version = "0.1.0"
description = "一个基于Flask-RESTful的完整REST API项目框架"
authors = ["Your Name <your.email@example.com>"]
readme = "README.md"
packages = [{include = "app"}]

[tool.poetry.dependencies]
python = "^3.8"
Flask = "^2.3.3"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.2"
black = "^23.9.1"

[tool.poetry.group.test.dependencies]
pytest = "^7.4.2"
factory-boy = "^3.3.0"

[tool.poetry.scripts]
ksf-restful = "run:app"
```

### 依赖组说明

- **main**: 生产环境必需的依赖
- **dev**: 开发环境需要的工具（格式化、检查等）
- **test**: 测试相关的依赖

## 开发工作流

### 1. 新功能开发
```bash
# 安装所有依赖
poetry install

# 激活虚拟环境
poetry shell

# 运行代码格式化
make format

# 运行代码检查
make lint

# 运行类型检查
make type-check

# 运行测试
make test
```

### 2. 添加新依赖
```bash
# 添加生产依赖
poetry add new-package

# 添加开发依赖
poetry add --group dev new-dev-package

# 添加测试依赖
poetry add --group test new-test-package
```

### 3. 提交前检查
```bash
# 安装 pre-commit 钩子
make pre-commit-install

# 手动运行 pre-commit 检查
make pre-commit-run
```

## 环境管理

### 虚拟环境位置
Poetry 默认在项目目录下创建虚拟环境：
```
ksf-restful/.venv/
```

### 配置虚拟环境位置
```bash
# 在项目目录下创建虚拟环境
poetry config virtualenvs.in-project true

# 查看当前配置
poetry config --list
```

## 与 pip 的对比

| 功能 | Poetry | pip + requirements.txt |
|------|--------|----------------------|
| 依赖解析 | ✅ 自动解析 | ❌ 手动管理 |
| 虚拟环境 | ✅ 自动管理 | ❌ 手动创建 |
| 依赖组 | ✅ 支持 | ❌ 不支持 |
| 锁定文件 | ✅ poetry.lock | ❌ 无 |
| 脚本定义 | ✅ pyproject.toml | ❌ 不支持 |
| 打包发布 | ✅ 内置支持 | ❌ 需要额外工具 |

## 常见问题

### 1. 锁定文件冲突
如果 `poetry.lock` 文件有冲突，可以重新生成：
```bash
rm poetry.lock
poetry install
```

### 2. 虚拟环境问题
如果虚拟环境有问题，可以重新创建：
```bash
poetry env remove python
poetry install
```

### 3. 依赖冲突
查看依赖树：
```bash
poetry show --tree
```

### 4. 更新到最新版本
```bash
poetry update --latest
```

## 最佳实践

1. **始终提交 `poetry.lock` 文件**：确保团队成员使用相同的依赖版本
2. **使用依赖组**：将开发工具和测试依赖分离
3. **定期更新依赖**：保持依赖的最新安全版本
4. **使用 pre-commit**：在提交前自动运行代码质量检查
5. **使用 Makefile**：简化常用命令的执行

## 迁移指南

### 从 pip 迁移到 Poetry

1. 创建 `pyproject.toml` 文件
2. 将 `requirements.txt` 中的依赖转换为 Poetry 格式
3. 运行 `poetry install` 安装依赖
4. 删除 `requirements.txt` 文件
5. 更新 CI/CD 配置

### 从 Poetry 迁移到 pip

1. 导出依赖：`poetry export -f requirements.txt --output requirements.txt`
2. 删除 `pyproject.toml` 和 `poetry.lock`
3. 使用 `pip install -r requirements.txt` 安装依赖 