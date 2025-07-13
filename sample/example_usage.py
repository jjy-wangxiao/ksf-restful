#!/usr/bin/env python3
"""
KSF RESTful API 使用示例
展示如何手动调用各种API接口
"""

import requests
import json
from datetime import datetime

class APIExample:
    """API使用示例类"""
    
    def __init__(self, base_url: str = "http://127.0.0.1:5678"):
        self.base_url = base_url
        self.api_prefix = "/api/v1"
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def log(self, message: str):
        """日志输出"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def make_request(self, method: str, endpoint: str, data: dict = None, params: dict = None):
        """发送HTTP请求"""
        url = f"{self.base_url}{self.api_prefix}{endpoint}"
        
        try:
            self.log(f"发送 {method} 请求到 {url}")
            if data:
                self.log(f"请求数据: {json.dumps(data, ensure_ascii=False, indent=2)}")
            if params:
                self.log(f"请求参数: {params}")
            
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                params=params,
                timeout=30
            )
            
            self.log(f"响应状态码: {response.status_code}")
            
            try:
                response_data = response.json()
                self.log(f"响应数据: {json.dumps(response_data, ensure_ascii=False, indent=2)}")
                return response_data
            except json.JSONDecodeError:
                self.log(f"响应内容: {response.text}")
                return {"raw_text": response.text}
                
        except requests.exceptions.RequestException as e:
            self.log(f"请求异常: {str(e)}")
            return {"error": str(e)}
    
    def example_dw_types(self):
        """单位类别API使用示例"""
        self.log("=" * 60)
        self.log("📋 单位类别API使用示例")
        
        # 1. 获取单位类别列表
        self.log("1. 获取单位类别列表")
        response = self.make_request("GET", "/dict/dw-types", params={"page": 1, "per_page": 10})
        
        # 2. 创建单位类别
        self.log("2. 创建单位类别")
        dw_type_data = {
            "id": "EXAMPLE_TYPE_001",
            "typeName": "示例单位类别"
        }
        response = self.make_request("POST", "/dict/dw-types", data=dw_type_data)
        
        # 3. 获取单个单位类别
        self.log("3. 获取单个单位类别")
        response = self.make_request("GET", "/dict/dw-types/EXAMPLE_TYPE_001")
        
        # 4. 更新单位类别
        self.log("4. 更新单位类别")
        update_data = {"typeName": "更新后的示例单位类别"}
        response = self.make_request("PUT", "/dict/dw-types/EXAMPLE_TYPE_001", data=update_data)
        
        # 5. 删除单位类别
        self.log("5. 删除单位类别")
        response = self.make_request("DELETE", "/dict/dw-types/EXAMPLE_TYPE_001")
    
    def example_dws(self):
        """单位API使用示例"""
        self.log("=" * 60)
        self.log("📋 单位API使用示例")
        
        # 1. 获取单位列表
        self.log("1. 获取单位列表")
        response = self.make_request("GET", "/dict/dws", params={"page": 1, "per_page": 10})
        
        # 2. 创建单位
        self.log("2. 创建单位")
        dw_data = {
            "id": "EXAMPLE_DW_001",
            "type_id": "EXAMPLE_TYPE_002",
            "dw": "示例单位"
        }
        response = self.make_request("POST", "/dict/dws", data=dw_data)
        
        # 3. 获取单个单位
        self.log("3. 获取单个单位")
        response = self.make_request("GET", "/dict/dws/EXAMPLE_DW_001")
        
        # 4. 更新单位
        self.log("4. 更新单位")
        update_data = {"dw": "更新后的示例单位"}
        response = self.make_request("PUT", "/dict/dws/EXAMPLE_DW_001", data=update_data)
        
        # 5. 删除单位
        self.log("5. 删除单位")
        response = self.make_request("DELETE", "/dict/dws/EXAMPLE_DW_001")
    
    def example_rcj_yjfls(self):
        """人材机一级分类API使用示例"""
        self.log("=" * 60)
        self.log("📋 人材机一级分类API使用示例")
        
        # 1. 获取一级分类列表
        self.log("1. 获取一级分类列表")
        response = self.make_request("GET", "/dict/rcj-yjfls", params={"page": 1, "per_page": 10})
        
        # 2. 创建一级分类
        self.log("2. 创建一级分类")
        yjfl_data = {
            "id": "EXAMPLE_YJFL_001",
            "yjflmc": "示例一级分类",
            "yjflms": "示例一级分类描述"
        }
        response = self.make_request("POST", "/dict/rcj-yjfls", data=yjfl_data)
        
        # 3. 获取单个一级分类
        self.log("3. 获取单个一级分类")
        response = self.make_request("GET", "/dict/rcj-yjfls/EXAMPLE_YJFL_001")
        
        # 4. 更新一级分类
        self.log("4. 更新一级分类")
        update_data = {"yjflmc": "更新后的示例一级分类"}
        response = self.make_request("PUT", "/dict/rcj-yjfls/EXAMPLE_YJFL_001", data=update_data)
        
        # 5. 删除一级分类
        self.log("5. 删除一级分类")
        response = self.make_request("DELETE", "/dict/rcj-yjfls/EXAMPLE_YJFL_001")
    
    def example_rcj_ejfls(self):
        """人材机二级分类API使用示例"""
        self.log("=" * 60)
        self.log("📋 人材机二级分类API使用示例")
        
        # 1. 获取二级分类列表
        self.log("1. 获取二级分类列表")
        response = self.make_request("GET", "/dict/rcj-ejfls", params={"page": 1, "per_page": 10})
        
        # 2. 创建二级分类
        self.log("2. 创建二级分类")
        ejfl_data = {
            "id": "EXAMPLE_EJFL_001",
            "yjfl_id": "EXAMPLE_YJFL_002",
            "ejflmc": "示例二级分类",
            "ejflms": "示例二级分类描述",
            "sx_ids": ["EXAMPLE_SX_001"],
            "dw_ids": ["EXAMPLE_DW_002"]
        }
        response = self.make_request("POST", "/dict/rcj-ejfls", data=ejfl_data)
        
        # 3. 获取单个二级分类
        self.log("3. 获取单个二级分类")
        response = self.make_request("GET", "/dict/rcj-ejfls/EXAMPLE_EJFL_001")
        
        # 4. 更新二级分类
        self.log("4. 更新二级分类")
        update_data = {"ejflmc": "更新后的示例二级分类"}
        response = self.make_request("PUT", "/dict/rcj-ejfls/EXAMPLE_EJFL_001", data=update_data)
        
        # 5. 删除二级分类
        self.log("5. 删除二级分类")
        response = self.make_request("DELETE", "/dict/rcj-ejfls/EXAMPLE_EJFL_001")
    
    def example_pagination(self):
        """分页功能示例"""
        self.log("=" * 60)
        self.log("📋 分页功能示例")
        
        # 测试不同的分页参数
        pagination_examples = [
            {"page": 1, "per_page": 5},
            {"page": 2, "per_page": 10},
            {"page": 1, "per_page": 20}
        ]
        
        for i, params in enumerate(pagination_examples, 1):
            self.log(f"{i}. 分页参数: {params}")
            response = self.make_request("GET", "/dict/dw-types", params=params)
    
    def example_error_handling(self):
        """错误处理示例"""
        self.log("=" * 60)
        self.log("📋 错误处理示例")
        
        # 1. 访问不存在的资源
        self.log("1. 访问不存在的资源")
        response = self.make_request("GET", "/dict/dw-types/NONEXISTENT")
        
        # 2. 发送无效数据
        self.log("2. 发送无效数据")
        invalid_data = {"invalid": "data"}
        response = self.make_request("POST", "/dict/dw-types", data=invalid_data)
        
        # 3. 访问不存在的端点
        self.log("3. 访问不存在的端点")
        response = self.make_request("GET", "/dict/nonexistent")
    
    def run_all_examples(self):
        """运行所有示例"""
        self.log("🚀 开始KSF RESTful API使用示例")
        self.log(f"API地址: {self.base_url}")
        
        try:
            # 运行各种示例
            self.example_dw_types()
            self.example_dws()
            self.example_rcj_yjfls()
            self.example_rcj_ejfls()
            self.example_pagination()
            self.example_error_handling()
            
            self.log("=" * 60)
            self.log("✅ 所有示例运行完成")
            
        except Exception as e:
            self.log(f"❌ 运行示例时出错: {str(e)}")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='KSF RESTful API 使用示例')
    parser.add_argument('--url', default='http://127.0.0.1:5678',
                       help='API服务器地址 (默认: http://127.0.0.1:5678)')
    
    args = parser.parse_args()
    
    # 创建示例对象并运行
    example = APIExample(args.url)
    example.run_all_examples()


if __name__ == "__main__":
    main() 