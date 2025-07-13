#!/bin/bash

# 设置环境变量
export FLASK_APP=run.py
export FLASK_ENV=development

echo "启动KSF RESTful API应用（测试版本，无认证）..."
echo "应用将在 http://localhost:8080 运行"
echo "Swagger UI地址: http://localhost:8080/api/v1/docs"
echo "按 Ctrl+C 停止应用"

# 运行应用
python run.py 