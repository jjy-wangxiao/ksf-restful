# KSF RESTful API 测试脚本使用说明

## 快速开始

### 1. 一键启动和测试（推荐）

```bash
python start_and_test.py
```

这个命令会：
- 自动启动Flask服务器
- 运行完整的API集成测试
- 显示测试结果
- 保持服务器运行

### 2. 快速测试（仅验证基本功能）

```bash
python quick_test.py
```

这个命令会快速验证API的基本功能，不进行完整的CRUD测试。

### 3. 查看API使用示例

```bash
python example_usage.py
```

这个命令会展示如何手动调用各种API接口。

## 测试脚本说明

| 脚本 | 功能 | 适用场景 |
|------|------|----------|
| `start_and_test.py` | 一键启动服务器并运行完整测试 | 项目部署验证 |
| `test_api_integration.py` | 完整的API集成测试 | 详细功能测试 |
| `quick_test.py` | 快速功能验证 | 日常检查 |
| `example_usage.py` | API使用示例 | 学习参考 |

## 手动测试

### 启动服务器

```bash
python run.py
```

### 运行测试

```bash
# 基本测试
python test_api_integration.py

# 指定服务器地址
python test_api_integration.py --url http://localhost:5678

# 设置超时时间
python test_api_integration.py --timeout 60
```

## 访问API

- **API地址**: http://127.0.0.1:5678/api/v1
- **Swagger文档**: http://127.0.0.1:5678/api/v1/docs

## 测试覆盖的接口

- ✅ 单位类别管理 (`/dict/dw-types`)
- ✅ 单位管理 (`/dict/dws`)
- ✅ 人材机二级分类属性 (`/dict/rcj-ejfl-sxs`)
- ✅ 人材机一级分类 (`/dict/rcj-yjfls`)
- ✅ 人材机二级分类 (`/dict/rcj-ejfls`)
- ✅ 人材机名称映射 (`/dict/rcj-mc2ejflids`)
- ✅ 人材机名称分类 (`/dict/rcj-mc-classifies`)

## 常见问题

### 服务器启动失败
- 检查端口5678是否被占用
- 确认Python环境和依赖正确安装

### 测试连接失败
- 确认服务器正在运行
- 检查服务器地址和端口

### 数据库错误
- 确认数据库配置正确
- 运行数据库迁移

## 更多信息

详细的使用说明请参考 `API_TEST_README.md` 文件。 