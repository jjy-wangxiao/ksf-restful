#!/bin/bash

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color
PROJECT_NAME="ksf-restful-api"

echo -e "${BLUE}🚀 启动 KSF RESTful API 项目环境准备${NC}"
echo ""

# 检查并安装 conda
check_and_install_conda() {
    if ! command -v conda &> /dev/null; then
        echo -e "${YELLOW}⚠️  conda 未安装${NC}"
        echo -e "${BLUE}📥 正在安装 Miniconda...${NC}"
        
        if [[ "$OSTYPE" == "darwin"* ]]; then
            # macOS
            if command -v brew &> /dev/null; then
                brew install --cask miniconda
            else
                echo -e "${RED}❌ 请先安装 Homebrew: https://brew.sh/${NC}"
                echo -e "${BLUE}💡 或者手动下载安装: https://docs.conda.io/en/latest/miniconda.html${NC}"
                exit 1
            fi
        else
            # Linux
            wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
            bash miniconda.sh -b -p $HOME/miniconda3
            export PATH="$HOME/miniconda3/bin:$PATH"
        fi
        
        echo -e "${GREEN}✅ conda 安装完成${NC}"
    else
        echo -e "${GREEN}✅ conda 已安装: $(conda --version)${NC}"
    fi
}

# 检查并安装 Poetry
check_and_install_poetry() {
    if ! command -v poetry &> /dev/null; then
        echo -e "${YELLOW}⚠️  Poetry 未安装${NC}"
        echo -e "${BLUE}📥 正在安装 Poetry...${NC}"
        
        # 使用官方安装脚本
        curl -sSL https://install.python-poetry.org | python3 -
        
        # 添加到 PATH
        export PATH="$HOME/.local/bin:$PATH"
        
        echo -e "${GREEN}✅ Poetry 安装完成${NC}"
    else
        echo -e "${GREEN}✅ Poetry 已安装: $(poetry --version)${NC}"
    fi
}

# 步骤1: 检查并安装 conda 和 Poetry
check_and_install_conda
check_and_install_poetry

# 检查是否存在现有虚拟环境
if [ -d ".venv" ] || [ -d ".conda" ]; then
    echo -e "${YELLOW}⚠️  检测到现有虚拟环境:${NC}"
    if [ -d ".venv" ]; then
        echo "   - .venv"
    fi
    if [ -d ".conda" ]; then
        echo "   - .conda"
    fi
    echo ""
    read -p "是否删除现有虚拟环境？(y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        if [ -d ".venv" ]; then
            echo -e "${YELLOW}🗑️  删除 .venv 虚拟环境...${NC}"
            rm -rf .venv
        fi
        if [ -d ".conda" ]; then
            echo -e "${YELLOW}🗑️  删除 .conda 虚拟环境...${NC}"
            rm -rf .conda
        fi
    else
        echo -e "${YELLOW}❌ 用户取消操作${NC}"
        exit 1
    fi
fi

# 通过 which 查找 conda 并加载其初始化脚本
CONDA_PATH=$(which conda 2>/dev/null)
if [ -n "$CONDA_PATH" ]; then
    CONDA_SH="$(dirname "$(dirname "$CONDA_PATH")")/etc/profile.d/conda.sh"
    if [ -f "$CONDA_SH" ]; then
        echo -e "${BLUE}🔧 加载 Conda 初始化脚本...${NC}"
        source "$CONDA_SH"
    fi
fi

# 步骤2: 使用 conda 创建虚拟环境并安装指定 Python
echo -e "${BLUE}📦 创建虚拟环境...${NC}"
REQUIRED_PYTHON="3.12.0"

# 使用 conda 创建虚拟环境并安装指定 Python 版本，虚拟环境目录为 .conda，名称为 PROJECT_NAME
echo -e "${BLUE}🐍 使用 conda 在 .conda 目录下创建默认的虚拟环境并安装 Python $REQUIRED_PYTHON...${NC}"
conda create -p .conda python=$REQUIRED_PYTHON -y

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ conda 虚拟环境创建成功${NC}"
    echo -e "${GREEN}✅ 虚拟环境已配置使用 Python $REQUIRED_PYTHON${NC}"
else
    echo -e "${RED}❌ conda 虚拟环境创建失败${NC}"
    exit 1
fi

# 步骤3: 激活虚拟环境并配置 Poetry
echo -e "${BLUE}📦 激活虚拟环境...${NC}"
conda activate ./.conda

echo -e "${BLUE}⚙️  配置 Poetry...${NC}"
poetry config virtualenvs.create false
poetry config virtualenvs.in-project false

# 步骤4: 使用 Poetry 安装项目依赖
echo -e "${BLUE}📦 使用 Poetry 安装项目依赖...${NC}"
poetry install

echo -e "${BLUE}🧪 安装开发依赖...${NC}"
# 分别安装 dev 和 test 可选依赖
poetry install --extras dev
poetry install --extras test

echo ""
echo -e "${GREEN}🎉 环境准备完成！${NC}"
echo ""
echo -e "${BLUE}📝 运行以下命令启动应用：${NC}"
echo "   source .conda/bin/activate"
echo "   poetry run python run.py"
echo "   或者"
echo "   ./run-app.sh"
echo -e "${BLUE}🔗 API地址: http://localhost:5000${NC}"
echo ""
echo -e "${BLUE}💡 提示：每次使用前需要激活虚拟环境：${NC}"
echo "   source .conda/bin/activate"
echo -e "${BLUE}💡 Poetry 已配置使用 conda 虚拟环境，可以直接使用 poetry 命令${NC}" 