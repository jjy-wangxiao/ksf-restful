#!/bin/bash

echo "🚀 启动 KSF RESTful API 项目..."

# 检查Python版本
python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
if [[ $(echo "$python_version >= 3.8" | bc -l) -eq 0 ]]; then
    echo "❌ 需要Python 3.8或更高版本"
    exit 1
fi

echo "✅ Python版本: $python_version"

# 创建虚拟环境
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv ksf_restful_venv
fi

# 激活虚拟环境
echo "🔧 激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "📥 安装依赖..."
pip install -r requirements.txt

# 初始化数据库
echo "🗄️ 初始化数据库..."
python manage.py init-db

# 检查是否需要创建管理员用户
if [ ! -f ".admin_created" ]; then
    echo "👤 创建管理员用户..."
    python manage.py create-admin
    touch .admin_created
fi

echo "🎉 启动完成！"
echo "📝 运行以下命令启动应用："
echo "   python run.py"
echo ""
echo "🔗 API地址: http://localhost:5000"
echo "📚 API文档: 查看 README.md" 