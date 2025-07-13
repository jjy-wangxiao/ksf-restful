# 日志系统使用指南

## 概述

本项目使用结构化和JSON格式的日志系统，基于 `structlog` 和 `python-json-logger` 实现。日志系统提供了完整的请求追踪、错误记录、性能监控和业务操作日志功能。

## 特性

- **结构化日志**: 使用JSON格式，便于日志分析和处理
- **多环境支持**: 开发环境使用文本格式，生产环境使用JSON格式
- **文件轮转**: 自动管理日志文件大小和数量
- **请求追踪**: 记录所有API请求和响应信息
- **错误处理**: 完整的异常记录和错误追踪
- **性能监控**: 记录慢请求和性能指标
- **业务日志**: 记录数据库操作和业务逻辑

## 配置

### 环境变量

```bash
# 日志级别 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL=INFO

# 日志格式 (json, text)
LOG_FORMAT=json

# 日志文件路径
LOG_FILE=logs/ksf-restful.log

# 单个日志文件最大大小（字节）
LOG_MAX_BYTES=10485760

# 保留的日志文件数量
LOG_BACKUP_COUNT=5

# 是否启用控制台输出
LOG_ENABLE_CONSOLE=true

# 是否启用文件输出
LOG_ENABLE_FILE=true
```

### 不同环境的配置

#### 开发环境
```bash
LOG_LEVEL=DEBUG
LOG_FORMAT=text
LOG_ENABLE_FILE=false
```

#### 生产环境
```bash
LOG_LEVEL=INFO
LOG_FORMAT=json
LOG_ENABLE_CONSOLE=false
LOG_ENABLE_FILE=true
```

## 使用方式

### 1. 获取日志记录器

```python
from app.utils.logger import get_logger

# 获取特定模块的日志记录器
logger = get_logger('app.services.dict_service')
```

### 2. 使用LoggerMixin

```python
from app.services.base_service import BaseService

class MyService(BaseService):
    def my_method(self):
        # 使用self.logger记录日志
        self.logger.info("Processing request", user_id=123)
        self.logger.error("An error occurred", error="details")
```

### 3. 记录不同类型的日志

```python
# 信息日志
logger.info("User logged in", user_id=123, ip="192.168.1.1")

# 警告日志
logger.warning("Rate limit exceeded", user_id=123, endpoint="/api/users")

# 错误日志
logger.error("Database connection failed", error=str(e), exc_info=True)

# 调试日志
logger.debug("Processing request", request_data=data)
```

### 4. 记录业务操作

```python
# 记录数据库操作
self.log_database_operation("CREATE", "User", user_id, user_email=email)

# 记录业务操作
self.log_business_operation("User Registration", user_id=user_id, email=email)

# 记录错误
self.log_error(exception, {"method": "create_user", "user_id": user_id})
```

## 日志格式

### JSON格式（生产环境）

```json
{
  "timestamp": "2024-01-15T10:30:45.123456Z",
  "level": "INFO",
  "logger": "app.services.dict_service",
  "module": "dict_service",
  "function": "create_dw_type",
  "line": 99,
  "message": "Service method called: create_dw_type",
  "method": "create_dw_type",
  "type_id": "TYPE001",
  "type_name": "长度单位"
}
```

### 文本格式（开发环境）

```
2024-01-15 10:30:45 - app.services.dict_service - INFO - dict_service:99 - create_dw_type - Service method called: create_dw_type method=create_dw_type type_id=TYPE001 type_name=长度单位
```

## 日志类型

### 1. 请求日志

自动记录所有API请求和响应信息：

- 请求方法、URL、参数
- 响应状态码、响应时间
- 用户代理、IP地址
- 请求头信息

### 2. 错误日志

记录所有异常和错误：

- 异常类型和消息
- 堆栈跟踪
- 请求上下文
- 错误发生的位置

### 3. 性能日志

监控应用性能：

- 请求处理时间
- 慢请求警告（>1秒）
- 数据库查询时间
- 内存使用情况

### 4. 业务日志

记录业务操作：

- 数据库CRUD操作
- 用户操作
- 业务逻辑执行
- 数据验证结果

## 日志分析

### 使用ELK Stack

可以将日志发送到Elasticsearch进行分析：

```python
# 配置Elasticsearch处理器
import logging
from elasticsearch import Elasticsearch

es_handler = logging.handlers.HTTPHandler(
    'localhost:9200',
    '/logs/ksf-restful',
    method='POST'
)
```

### 使用Grafana

创建仪表板监控：

- 请求量趋势
- 错误率统计
- 响应时间分布
- 用户活跃度

### 使用命令行工具

```bash
# 查看错误日志
grep '"level":"ERROR"' logs/ksf-restful.log

# 查看慢请求
grep '"response_time":[0-9]\{4,\}' logs/ksf-restful.log

# 统计请求量
jq '.timestamp | split("T")[0]' logs/ksf-restful.log | sort | uniq -c
```

## 最佳实践

### 1. 日志级别使用

- **DEBUG**: 详细的调试信息，仅在开发环境使用
- **INFO**: 一般信息，记录重要的业务操作
- **WARNING**: 警告信息，可能的问题但不影响功能
- **ERROR**: 错误信息，功能异常但应用可以继续运行
- **CRITICAL**: 严重错误，应用无法继续运行

### 2. 日志内容

- 使用结构化数据，避免长文本
- 包含足够的上下文信息
- 避免记录敏感信息（密码、token等）
- 使用有意义的字段名

### 3. 性能考虑

- 避免在日志中执行复杂计算
- 使用异步日志记录（如需要）
- 定期清理旧日志文件
- 监控日志文件大小

### 4. 安全考虑

- 不记录敏感信息
- 对用户输入进行脱敏处理
- 限制日志文件访问权限
- 定期审查日志内容

## 故障排除

### 常见问题

1. **日志文件权限错误**
   ```bash
   chmod 755 logs/
   chmod 644 logs/ksf-restful.log
   ```

2. **磁盘空间不足**
   ```bash
   # 清理旧日志文件
   find logs/ -name "*.log.*" -mtime +30 -delete
   ```

3. **日志级别不生效**
   ```bash
   # 检查环境变量
   echo $LOG_LEVEL
   # 重启应用
   ```

### 调试模式

启用调试模式查看详细日志：

```bash
export LOG_LEVEL=DEBUG
export LOG_FORMAT=text
python run.py
```

## 扩展

### 添加自定义日志处理器

```python
from app.utils.logger import setup_logging

# 添加自定义处理器
def custom_handler(logger):
    # 实现自定义逻辑
    pass

setup_logging(
    log_level="INFO",
    custom_handlers=[custom_handler]
)
```

### 集成第三方服务

```python
# 集成Sentry
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FlaskIntegration()]
)
``` 