# KSF RESTful API 测试指南

本文档介绍如何使用测试脚本来验证KSF RESTful API项目的功能。

## 测试脚本说明

### 1. `test_api_integration.py` - API集成测试脚本

这是一个全面的API集成测试脚本，模拟真实的API访问请求，测试所有字典管理接口的功能。

**功能特性：**
- ✅ 测试所有CRUD操作（创建、读取、更新、删除）
- ✅ 测试分页功能
- ✅ 测试错误处理
- ✅ 测试Swagger文档访问
- ✅ 自动清理测试数据
- ✅ 详细的测试日志输出
- ✅ 测试结果统计

**测试覆盖的API接口：**
- 单位类别管理 (`/api/v1/dict/dw-types`)
- 单位管理 (`/api/v1/dict/dws`)
- 人材机二级分类属性管理 (`/api/v1/dict/rcj-ejfl-sxs`)
- 人材机一级分类管理 (`/api/v1/dict/rcj-yjfls`)
- 人材机二级分类管理 (`/api/v1/dict/rcj-ejfls`)
- 人材机名称映射管理 (`/api/v1/dict/rcj-mc2ejflids`)
- 人材机名称分类管理 (`/api/v1/dict/rcj-mc-classifies`)

### 2. `start_and_test.py` - 一键启动和测试脚本

这是一个便捷的脚本，可以自动启动Flask服务器并运行API测试。

**功能特性：**
- 🚀 自动启动Flask服务器
- 🧪 自动运行API集成测试
- 📊 显示测试结果
- 🛑 优雅停止服务器
- 🔄 保持服务器运行（可选）

## 使用方法

### 方法一：一键启动和测试（推荐）

```bash
# 运行一键启动和测试脚本
python start_and_test.py
```

这个脚本会：
1. 自动启动Flask服务器
2. 等待服务器完全启动
3. 运行所有API测试
4. 显示测试结果
5. 保持服务器运行（按Ctrl+C停止）

### 方法二：手动测试

```bash
# 1. 首先启动Flask服务器
python run.py

# 2. 在另一个终端中运行测试
python test_api_integration.py

# 或者指定自定义服务器地址
python test_api_integration.py --url http://localhost:5678
```

### 方法三：仅运行测试（服务器已运行）

```bash
# 基本用法
python test_api_integration.py

# 指定服务器地址
python test_api_integration.py --url http://127.0.0.1:5678

# 指定超时时间
python test_api_integration.py --timeout 60
```

## 测试参数说明

### `test_api_integration.py` 参数

- `--url`: API服务器地址（默认: http://127.0.0.1:5678）
- `--timeout`: 请求超时时间，单位秒（默认: 30）

### 示例

```bash
# 测试远程服务器
python test_api_integration.py --url http://192.168.1.100:5678

# 设置更长的超时时间
python test_api_integration.py --timeout 60
```

## 测试输出说明

### 测试过程输出

测试脚本会输出详细的测试过程信息：

```
[2024-01-01 12:00:00] [INFO] 🚀 开始KSF RESTful API集成测试
[2024-01-01 12:00:00] [INFO] 测试目标: http://127.0.0.1:5678
[2024-01-01 12:00:01] [INFO] ============================================================
[2024-01-01 12:00:01] [INFO] 开始测试健康检查
[2024-01-01 12:00:01] [INFO] 发送 GET 请求到 http://127.0.0.1:5678/api/v1/
[2024-01-01 12:00:01] [INFO] 响应状态码: 404
[2024-01-01 12:00:01] [INFO] ✅ 请求成功
[2024-01-01 12:00:01] [INFO] ✅ 根路径测试通过
```

### 测试结果汇总

测试完成后会显示结果汇总：

```
============================================================
📊 测试结果汇总
总测试数: 11
通过: 11
失败: 0
测试耗时: 15.23秒
成功率: 100.0%
🎉 所有测试通过！项目运行正常
============================================================
```

## 测试数据管理

### 自动清理

测试脚本会自动清理测试过程中创建的数据，确保不会在数据库中留下测试数据。

### 测试数据隔离

每个测试用例都使用唯一的测试ID，避免数据冲突：

- 单位类别: `TEST_TYPE_001`
- 单位: `TEST_DW_001`
- 属性: `TEST_SX_001`
- 一级分类: `TEST_YJFL_001`
- 二级分类: `TEST_EJFL_001`

## 故障排除

### 常见问题

1. **服务器启动失败**
   - 检查端口5678是否被占用
   - 检查Python环境和依赖是否正确安装
   - 查看错误日志

2. **测试连接失败**
   - 确认服务器正在运行
   - 检查服务器地址和端口是否正确
   - 检查防火墙设置

3. **数据库错误**
   - 确认数据库配置正确
   - 检查数据库连接
   - 运行数据库迁移

### 调试模式

如果需要更详细的调试信息，可以修改测试脚本中的日志级别：

```python
# 在 test_api_integration.py 中
self.log(f"详细调试信息", "DEBUG")
```

## 扩展测试

### 添加新的测试用例

可以在 `APITester` 类中添加新的测试方法：

```python
def test_custom_api(self) -> bool:
    """测试自定义API"""
    self.log("开始测试自定义API")
    
    # 添加测试逻辑
    response = self.make_request("GET", "/custom/endpoint")
    
    if "error" not in response:
        self.log("✅ 自定义API测试通过")
        return True
    else:
        self.log("❌ 自定义API测试失败")
        return False
```

然后在 `run_all_tests` 方法中添加新的测试：

```python
tests = [
    # ... 现有测试
    ("自定义API", self.test_custom_api),
]
```

## 性能测试

### 压力测试示例

```python
import concurrent.futures
import time

def stress_test():
    """简单的压力测试"""
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for i in range(100):
            future = executor.submit(make_api_request)
            futures.append(future)
        
        # 等待所有请求完成
        concurrent.futures.wait(futures)
    
    end_time = time.time()
    print(f"压力测试完成，耗时: {end_time - start_time:.2f}秒")
```

## 总结

这些测试脚本提供了全面的API功能验证，确保项目能够正常工作。建议在以下情况下运行测试：

- 🚀 项目初始部署后
- 🔄 代码更新后
- 🐛 修复bug后
- 📦 发布新版本前

通过定期运行这些测试，可以确保API的稳定性和可靠性。 