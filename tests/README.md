# 测试文档

本文档描述了项目的测试结构、运行方法和最佳实践。

## 测试结构

```
tests/
├── __init__.py              # 测试包初始化
├── conftest.py              # pytest配置文件
├── test_dto.py              # DTO层测试
├── test_service.py          # Service层测试
├── test_api.py              # API层测试
└── README.md                # 测试文档
```

## 测试层次

### 1. DTO层测试 (`test_dto.py`)
- **目的**: 测试数据传输对象的创建和基本功能
- **范围**: 所有DTO类的实例化、字段验证、序列化
- **类型**: 单元测试
- **特点**: 快速、无依赖、纯逻辑测试

### 2. Service层测试 (`test_service.py`)
- **目的**: 测试业务逻辑和数据转换功能
- **范围**: 服务类的方法、DTO-Entity转换、业务规则验证
- **类型**: 单元测试
- **特点**: 使用Mock模拟数据库和外部依赖

### 3. API层测试 (`test_api.py`)
- **目的**: 测试API端点的请求和响应
- **范围**: HTTP方法、状态码、响应格式、错误处理
- **类型**: 集成测试
- **特点**: 测试完整的请求-响应流程

## 测试标记

项目使用pytest标记来分类测试：

- `@pytest.mark.unit`: 单元测试
- `@pytest.mark.integration`: 集成测试
- `@pytest.mark.slow`: 慢速测试（可选择性跳过）

## 运行测试

### 使用测试脚本（推荐）

```bash
# 运行所有测试
./run_tests.sh all

# 运行单元测试
./run_tests.sh unit

# 运行集成测试
./run_tests.sh integration

# 运行快速测试（排除慢速测试）
./run_tests.sh fast

# 运行特定测试文件
./run_tests.sh file test_dto.py

# 运行测试并生成覆盖率报告
./run_tests.sh coverage

# 运行测试并生成HTML报告
./run_tests.sh html

# 安装测试依赖
./run_tests.sh install

# 清理测试缓存
./run_tests.sh clean

# 显示帮助信息
./run_tests.sh help
```

### 直接使用pytest

```bash
# 运行所有测试
pytest tests/ -v

# 运行单元测试
pytest tests/ -m unit -v

# 运行集成测试
pytest tests/ -m integration -v

# 运行特定测试文件
pytest tests/test_dto.py -v

# 运行特定测试类
pytest tests/test_dto.py::TestDwTypeDTO -v

# 运行特定测试方法
pytest tests/test_dto.py::TestDwTypeDTO::test_dw_type_request_dto -v

# 生成覆盖率报告
pytest tests/ --cov=app --cov-report=html

# 生成HTML报告
pytest tests/ --html=reports/test_report.html --self-contained-html
```

## 测试配置

### 环境变量
测试环境会自动设置以下环境变量：
- `FLASK_ENV=testing`
- `DATABASE_URL=sqlite:///:memory:`

### 共享Fixture
`conftest.py` 中定义了多个共享的fixture：

- `app`: 测试应用实例
- `client`: 测试客户端
- `runner`: 测试运行器
- `mock_db`: 模拟数据库会话
- `sample_*_data`: 示例数据
- `mock_pagination`: 模拟分页对象
- `mock_models`: 模拟所有模型类

## 测试最佳实践

### 1. 测试命名
- 测试类名: `Test<ClassName>`
- 测试方法名: `test_<method_name>_<scenario>`
- 使用描述性的名称，清楚表达测试目的

### 2. 测试结构
遵循AAA模式（Arrange-Act-Assert）：
```python
def test_example(self):
    # Arrange: 准备测试数据
    data = {"id": "01", "name": "test"}
    
    # Act: 执行被测试的操作
    result = some_function(data)
    
    # Assert: 验证结果
    assert result.id == "01"
    assert result.name == "test"
```

### 3. Mock使用
- 使用`@patch`装饰器模拟外部依赖
- 为每个测试方法提供独立的mock
- 验证mock的调用次数和参数

### 4. 测试数据
- 使用fixture提供可重用的测试数据
- 避免硬编码测试数据
- 使用有意义的测试数据

### 5. 错误测试
- 测试正常流程和异常流程
- 验证错误消息和状态码
- 测试边界条件和无效输入

## 覆盖率报告

运行覆盖率测试后，可以在 `htmlcov/` 目录中查看详细的覆盖率报告：

```bash
# 生成覆盖率报告
./run_tests.sh coverage

# 在浏览器中打开报告
open htmlcov/index.html
```

## 持续集成

建议在CI/CD流程中包含以下测试步骤：

1. 运行单元测试
2. 运行集成测试
3. 生成覆盖率报告
4. 检查覆盖率阈值

示例GitHub Actions配置：
```yaml
- name: Run tests
  run: |
    ./run_tests.sh unit
    ./run_tests.sh integration
    ./run_tests.sh coverage
```

## 故障排除

### 常见问题

1. **导入错误**
   - 确保在虚拟环境中运行测试
   - 检查Python路径设置

2. **Mock不工作**
   - 检查patch路径是否正确
   - 确保在正确的位置应用patch

3. **测试失败**
   - 查看详细的错误信息
   - 检查测试数据是否正确
   - 验证mock设置

### 调试技巧

1. 使用 `-s` 参数查看print输出：
   ```bash
   pytest tests/ -s
   ```

2. 使用 `--pdb` 参数在失败时进入调试器：
   ```bash
   pytest tests/ --pdb
   ```

3. 使用 `-x` 参数在第一个失败时停止：
   ```bash
   pytest tests/ -x
   ```

## 扩展测试

### 添加新测试

1. 创建新的测试文件：`tests/test_new_feature.py`
2. 编写测试类和方法
3. 添加适当的测试标记
4. 更新本文档

### 添加新的Fixture

1. 在 `conftest.py` 中定义新的fixture
2. 添加文档字符串说明用途
3. 在相关测试中使用

### 性能测试

对于性能敏感的代码，可以添加性能测试：

```python
import time

def test_performance():
    start_time = time.time()
    # 执行被测试的操作
    result = some_operation()
    end_time = time.time()
    
    # 验证性能要求
    assert end_time - start_time < 1.0  # 1秒内完成
```

## 总结

良好的测试覆盖是项目质量的重要保证。通过分层测试、合理使用Mock、遵循最佳实践，可以构建可靠、可维护的测试套件。 