#!/usr/bin/env python3
"""
KSF RESTful API 集成测试脚本
模拟真实的API访问请求，验证项目是否正常工作
"""

import requests
import json
import time
import sys
from datetime import datetime
from typing import Dict, Any, List, Optional

class APITester:
    """API测试器类"""
    
    def __init__(self, base_url: str = "http://127.0.0.1:5678"):
        self.base_url = base_url
        self.api_prefix = "/api/v1"
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
        # 存储测试过程中创建的数据ID，用于清理
        self.created_ids = {
            'dw_types': [],
            'dws': [],
            'rcj_ejfl_sxs': [],
            'rcj_yjfls': [],
            'rcj_ejfls': [],
            'rcj_mc2ejflids': [],
            'rcj_mc_classifies': []
        }
        
        # 测试结果统计
        self.test_results = {
            'total': 0,
            'passed': 0,
            'failed': 0,
            'errors': []
        }
    
    def log(self, message: str, level: str = "INFO"):
        """日志输出"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")
    
    def make_request(self, method: str, endpoint: str, data: Dict = None, 
                    params: Dict = None, expected_status: int = 200) -> Dict:
        """发送HTTP请求并验证响应"""
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
            
            # 尝试解析JSON响应
            try:
                response_data = response.json()
                self.log(f"响应数据: {json.dumps(response_data, ensure_ascii=False, indent=2)}")
            except json.JSONDecodeError:
                self.log(f"响应内容: {response.text}")
                response_data = {"raw_text": response.text}
            
            # 验证状态码
            if response.status_code == expected_status:
                self.log("✅ 请求成功")
                return response_data
            else:
                self.log(f"❌ 请求失败，期望状态码 {expected_status}，实际 {response.status_code}")
                return {"error": f"Unexpected status code: {response.status_code}"}
                
        except requests.exceptions.RequestException as e:
            self.log(f"❌ 请求异常: {str(e)}", "ERROR")
            return {"error": str(e)}
    
    def test_health_check(self) -> bool:
        """测试健康检查"""
        self.log("=" * 60)
        self.log("开始测试健康检查")
        
        # 测试根路径
        response = self.make_request("GET", "/", expected_status=404)  # 根路径应该返回404
        if "error" not in response:
            self.log("✅ 根路径测试通过")
            return True
        else:
            self.log("❌ 根路径测试失败")
            return False
    
    def test_swagger_docs(self) -> bool:
        """测试Swagger文档"""
        self.log("=" * 60)
        self.log("开始测试Swagger文档")
        
        # 测试Swagger UI
        response = self.make_request("GET", "/docs", expected_status=200)
        if "error" not in response:
            self.log("✅ Swagger文档测试通过")
            return True
        else:
            self.log("❌ Swagger文档测试失败")
            return False
    
    def test_dw_types(self) -> bool:
        """测试单位类别API"""
        self.log("=" * 60)
        self.log("开始测试单位类别API")
        
        # 1. 获取单位类别列表
        self.log("1. 测试获取单位类别列表")
        response = self.make_request("GET", "/dict/dw-types", params={"page": 1, "per_page": 5})
        if "error" in response:
            return False
        
        # 2. 创建单位类别
        self.log("2. 测试创建单位类别")
        dw_type_data = {
            "id": "01",
            "typeName": "测试单位类别"
        }
        response = self.make_request("POST", "/dict/dw-types", data=dw_type_data, expected_status=201)
        if "error" in response:
            return False
        
        type_id = dw_type_data["id"]
        self.created_ids['dw_types'].append(type_id)
        
        # 3. 获取单个单位类别
        self.log("3. 测试获取单个单位类别")
        response = self.make_request("GET", f"/dict/dw-types/{type_id}")
        if "error" in response:
            return False
        
        # 4. 更新单位类别
        self.log("4. 测试更新单位类别")
        update_data = {"typeName": "更新后的测试单位类别"}
        response = self.make_request("PUT", f"/dict/dw-types/{type_id}", data=update_data)
        if "error" in response:
            return False
        
        # 5. 删除单位类别
        self.log("5. 测试删除单位类别")
        response = self.make_request("DELETE", f"/dict/dw-types/{type_id}", expected_status=204)
        if "error" in response:
            return False
        
        self.created_ids['dw_types'].remove(type_id)
        self.log("✅ 单位类别API测试通过")
        return True
    
    def test_dws(self) -> bool:
        """测试单位API"""
        self.log("=" * 60)
        self.log("开始测试单位API")
        
        # 1. 获取单位列表
        self.log("1. 测试获取单位列表")
        response = self.make_request("GET", "/dict/dws", params={"page": 1, "per_page": 5})
        if "error" in response:
            return False
        
        # 2. 先创建单位类别（如果不存在）
        self.log("2. 创建必要的单位类别")
        dw_type_data = {
            "id": "02",
            "typeName": "测试单位类别02"
        }
        self.make_request("POST", "/dict/dw-types", data=dw_type_data, expected_status=201)
        
        # 3. 创建单位
        self.log("3. 测试创建单位")
        dw_data = {
            "id": "0001",
            "type_id": "02",
            "dw": "测试单位"
        }
        response = self.make_request("POST", "/dict/dws", data=dw_data, expected_status=201)
        if "error" in response:
            return False
        
        dw_id = dw_data["id"]
        self.created_ids['dws'].append(dw_id)
        
        # 4. 获取单个单位
        self.log("4. 测试获取单个单位")
        response = self.make_request("GET", f"/dict/dws/{dw_id}")
        if "error" in response:
            return False
        
        # 5. 更新单位
        self.log("5. 测试更新单位")
        update_data = {"dw": "更新后的测试单位"}
        response = self.make_request("PUT", f"/dict/dws/{dw_id}", data=update_data)
        if "error" in response:
            return False
        
        # 6. 删除单位
        self.log("6. 测试删除单位")
        response = self.make_request("DELETE", f"/dict/dws/{dw_id}", expected_status=204)
        if "error" in response:
            return False
        
        # 7. 清理单位类别
        self.log("7. 清理单位类别")
        self.make_request("DELETE", f"/dict/dw-types/02", expected_status=204)
        
        self.created_ids['dws'].remove(dw_id)
        self.log("✅ 单位API测试通过")
        return True
    
    def test_rcj_ejfl_sxs(self) -> bool:
        """测试人材机二级分类属性API"""
        self.log("=" * 60)
        self.log("开始测试人材机二级分类属性API")
        
        # 1. 获取属性列表
        self.log("1. 测试获取属性列表")
        response = self.make_request("GET", "/dict/rcj-ejfl-sxs", params={"page": 1, "per_page": 5})
        if "error" in response:
            return False
        
        # 2. 创建属性
        self.log("2. 测试创建属性")
        sx_data = {
            "id": "0001",
            "sx": "测试属性"
        }
        response = self.make_request("POST", "/dict/rcj-ejfl-sxs", data=sx_data, expected_status=201)
        if "error" in response:
            return False
        
        sx_id = sx_data["id"]
        self.created_ids['rcj_ejfl_sxs'].append(sx_id)
        
        # 3. 获取单个属性
        self.log("3. 测试获取单个属性")
        response = self.make_request("GET", f"/dict/rcj-ejfl-sxs/{sx_id}")
        if "error" in response:
            return False
        
        # 4. 更新属性
        self.log("4. 测试更新属性")
        update_data = {"sx": "更新后的测试属性"}
        response = self.make_request("PUT", f"/dict/rcj-ejfl-sxs/{sx_id}", data=update_data)
        if "error" in response:
            return False
        
        # 5. 删除属性
        self.log("5. 测试删除属性")
        response = self.make_request("DELETE", f"/dict/rcj-ejfl-sxs/{sx_id}", expected_status=204)
        if "error" in response:
            return False
        
        self.created_ids['rcj_ejfl_sxs'].remove(sx_id)
        self.log("✅ 人材机二级分类属性API测试通过")
        return True
    
    def test_rcj_yjfls(self) -> bool:
        """测试人材机一级分类API"""
        self.log("=" * 60)
        self.log("开始测试人材机一级分类API")
        
        # 1. 获取一级分类列表
        self.log("1. 测试获取一级分类列表")
        response = self.make_request("GET", "/dict/rcj-yjfls", params={"page": 1, "per_page": 5})
        if "error" in response:
            return False
        
        # 2. 创建一级分类
        self.log("2. 测试创建一级分类")
        yjfl_data = {
            "id": "0001",
            "yjflmc": "测试一级分类",
            "yjflms": "测试一级分类描述"
        }
        response = self.make_request("POST", "/dict/rcj-yjfls", data=yjfl_data, expected_status=201)
        if "error" in response:
            return False
        
        yjfl_id = yjfl_data["id"]
        self.created_ids['rcj_yjfls'].append(yjfl_id)
        
        # 3. 获取单个一级分类
        self.log("3. 测试获取单个一级分类")
        response = self.make_request("GET", f"/dict/rcj-yjfls/{yjfl_id}")
        if "error" in response:
            return False
        
        # 4. 更新一级分类
        self.log("4. 测试更新一级分类")
        update_data = {"yjflmc": "更新后的测试一级分类"}
        response = self.make_request("PUT", f"/dict/rcj-yjfls/{yjfl_id}", data=update_data)
        if "error" in response:
            return False
        
        # 5. 删除一级分类
        self.log("5. 测试删除一级分类")
        response = self.make_request("DELETE", f"/dict/rcj-yjfls/{yjfl_id}", expected_status=204)
        if "error" in response:
            return False
        
        self.created_ids['rcj_yjfls'].remove(yjfl_id)
        self.log("✅ 人材机一级分类API测试通过")
        return True
    
    def test_rcj_ejfls(self) -> bool:
        """测试人材机二级分类API"""
        self.log("=" * 60)
        self.log("开始测试人材机二级分类API")
        
        # 1. 获取二级分类列表
        self.log("1. 测试获取二级分类列表")
        response = self.make_request("GET", "/dict/rcj-ejfls", params={"page": 1, "per_page": 5})
        if "error" in response:
            return False
        
        # 2. 先创建必要的一级分类
        self.log("2. 创建必要的一级分类")
        yjfl_data = {
            "id": "01",
            "yjflmc": "测试一级分类",
            "yjflms": "测试一级分类描述"
        }
        self.make_request("POST", "/dict/rcj-yjfls", data=yjfl_data, expected_status=201)
        
        # 3. 创建二级分类
        self.log("3. 测试创建二级分类")
        ejfl_data = {
            "id": "0001",
            "yjfl_id": "01",
            "ejflmc": "测试二级分类",
            "ejflms": "测试二级分类描述",
            "sx_ids": ["0002"],
            "dw_ids": ["0002"]
        }
        response = self.make_request("POST", "/dict/rcj-ejfls", data=ejfl_data, expected_status=201)
        if "error" in response:
            return False
        
        ejfl_id = ejfl_data["id"]
        self.created_ids['rcj_ejfls'].append(ejfl_id)
        
        # 4. 获取单个二级分类
        self.log("4. 测试获取单个二级分类")
        response = self.make_request("GET", f"/dict/rcj-ejfls/{ejfl_id}")
        if "error" in response:
            return False
        
        # 5. 更新二级分类
        self.log("5. 测试更新二级分类")
        update_data = {"ejflmc": "更新后的测试二级分类"}
        response = self.make_request("PUT", f"/dict/rcj-ejfls/{ejfl_id}", data=update_data)
        if "error" in response:
            return False
        
        # 6. 删除二级分类
        self.log("6. 测试删除二级分类")
        response = self.make_request("DELETE", f"/dict/rcj-ejfls/{ejfl_id}", expected_status=204)
        if "error" in response:
            return False
        
        # 7. 清理一级分类
        self.log("7. 清理一级分类")
        self.make_request("DELETE", f"/dict/rcj-yjfls/01", expected_status=204)
        
        self.created_ids['rcj_ejfls'].remove(ejfl_id)
        self.log("✅ 人材机二级分类API测试通过")
        return True
    
    def test_rcj_mc2ejflids(self) -> bool:
        """测试人材机名称映射API"""
        self.log("=" * 60)
        self.log("开始测试人材机名称映射API")
        
        # 1. 获取映射列表
        self.log("1. 测试获取映射列表")
        response = self.make_request("GET", "/dict/rcj-mc2ejflids", params={"page": 1, "per_page": 5})
        if "error" in response:
            return False
        
        # 2. 先创建必要的二级分类
        self.log("2. 创建必要的二级分类")
        # 创建一级分类
        yjfl_data = {
            "id": "03",
            "yjflmc": "测试一级分类03",
            "yjflms": "测试一级分类描述03"
        }
        self.make_request("POST", "/dict/rcj-yjfls", data=yjfl_data, expected_status=201)
        
        # 创建二级分类
        ejfl_data = {
            "id": "0003",
            "yjfl_id": "03",
            "ejflmc": "测试二级分类03",
            "ejflms": "测试二级分类描述03"
        }
        self.make_request("POST", "/dict/rcj-ejfls", data=ejfl_data, expected_status=201)
        
        # 3. 创建映射
        self.log("3. 测试创建映射")
        mapping_data = {
            "ejflid": "0003",
            "orignal_rcjmc": "测试原始人材机名称"
        }
        response = self.make_request("POST", "/dict/rcj-mc2ejflids", data=mapping_data, expected_status=201)
        if "error" in response:
            return False
        
        # 获取创建的映射ID
        mapping_id = response.get('id')
        if mapping_id:
            self.created_ids['rcj_mc2ejflids'].append(mapping_id)
        
        # 4. 获取单个映射
        self.log("4. 测试获取单个映射")
        response = self.make_request("GET", f"/dict/rcj-mc2ejflids/{mapping_id}")
        if "error" in response:
            return False
        
        # 5. 更新映射
        self.log("5. 测试更新映射")
        update_data = {"orignal_rcjmc": "更新后的测试原始人材机名称"}
        response = self.make_request("PUT", f"/dict/rcj-mc2ejflids/{mapping_id}", data=update_data)
        if "error" in response:
            return False
        
        # 6. 删除映射
        self.log("6. 测试删除映射")
        response = self.make_request("DELETE", f"/dict/rcj-mc2ejflids/{mapping_id}", expected_status=204)
        if "error" in response:
            return False
        
        # 7. 清理分类数据
        self.log("7. 清理分类数据")
        self.make_request("DELETE", f"/dict/rcj-ejfls/0003", expected_status=204)
        self.make_request("DELETE", f"/dict/rcj-yjfls/03", expected_status=204)
        
        if mapping_id in self.created_ids['rcj_mc2ejflids']:
            self.created_ids['rcj_mc2ejflids'].remove(mapping_id)
        self.log("✅ 人材机名称映射API测试通过")
        return True
    
    def test_rcj_mc_classifies(self) -> bool:
        """测试人材机名称分类API"""
        self.log("=" * 60)
        self.log("开始测试人材机名称分类API")
        
        # 1. 获取分类列表
        self.log("1. 测试获取分类列表")
        response = self.make_request("GET", "/dict/rcj-mc-classifies", params={"page": 1, "per_page": 5})
        if "error" in response:
            return False
        
        # 2. 先创建必要的分类数据
        self.log("2. 创建必要的分类数据")
        # 创建一级分类
        yjfl_data = {
            "id": "03",
            "yjflmc": "测试一级分类名称",
            "yjflms": "测试一级分类描述"
        }
        self.make_request("POST", "/dict/rcj-yjfls", data=yjfl_data, expected_status=201)
        
        # 创建二级分类
        ejfl_data = {
            "id": "0004",
            "yjfl_id": "03",
            "ejflmc": "测试二级分类名称",
            "ejflms": "测试二级分类描述"
        }
        self.make_request("POST", "/dict/rcj-ejfls", data=ejfl_data, expected_status=201)
        
        # 3. 创建分类
        self.log("3. 测试创建分类")
        classify_data = {
            "cleaned_rcj_original_mc": "测试清洗后的人材机名称",
            "yjflid": "03",
            "yjflmc": "测试一级分类名称",
            "ejflid": "0004",
            "ejflmc": "测试二级分类名称"
        }
        response = self.make_request("POST", "/dict/rcj-mc-classifies", data=classify_data, expected_status=201)
        if "error" in response:
            return False
        
        # 获取创建的分类ID
        classify_id = response.get('id')
        if classify_id:
            self.created_ids['rcj_mc_classifies'].append(classify_id)
        
        # 4. 获取单个分类
        self.log("4. 测试获取单个分类")
        response = self.make_request("GET", f"/dict/rcj-mc-classifies/{classify_id}")
        if "error" in response:
            return False
        
        # 5. 更新分类
        self.log("5. 测试更新分类")
        update_data = {"cleaned_rcj_original_mc": "更新后的测试清洗后的人材机名称"}
        response = self.make_request("PUT", f"/dict/rcj-mc-classifies/{classify_id}", data=update_data)
        if "error" in response:
            return False
        
        # 6. 删除分类
        self.log("6. 测试删除分类")
        response = self.make_request("DELETE", f"/dict/rcj-mc-classifies/{classify_id}", expected_status=204)
        if "error" in response:
            return False
        
        # 7. 清理分类数据
        self.log("7. 清理分类数据")
        self.make_request("DELETE", f"/dict/rcj-ejfls/0004", expected_status=204)
        self.make_request("DELETE", f"/dict/rcj-yjfls/03", expected_status=204)
        
        if classify_id in self.created_ids['rcj_mc_classifies']:
            self.created_ids['rcj_mc_classifies'].remove(classify_id)
        self.log("✅ 人材机名称分类API测试通过")
        return True
    
    def test_error_handling(self) -> bool:
        """测试错误处理"""
        self.log("=" * 60)
        self.log("开始测试错误处理")
        
        # 1. 测试不存在的资源
        self.log("1. 测试获取不存在的资源")
        response = self.make_request("GET", "/dict/dw-types/NONEXISTENT", expected_status=404)
        if "error" not in response:
            self.log("✅ 404错误处理测试通过")
        else:
            self.log("❌ 404错误处理测试失败")
            return False
        
        # 2. 测试无效的JSON数据
        self.log("2. 测试无效的JSON数据")
        # 这里我们发送一个无效的请求来测试错误处理
        response = self.make_request("POST", "/dict/dw-types", data={"invalid": "data"}, expected_status=500)
        if "error" not in response:
            self.log("✅ 500错误处理测试通过")
        else:
            self.log("❌ 500错误处理测试失败")
            return False
        
        self.log("✅ 错误处理测试通过")
        return True
    
    def test_pagination(self) -> bool:
        """测试分页功能"""
        self.log("=" * 60)
        self.log("开始测试分页功能")
        
        # 测试分页参数
        response = self.make_request("GET", "/dict/dw-types", params={
            "page": 1,
            "per_page": 3
        })
        
        if "error" not in response:
            self.log("✅ 分页功能测试通过")
            return True
        else:
            self.log("❌ 分页功能测试失败")
            return False
    
    def cleanup_test_data(self):
        """清理测试数据"""
        self.log("=" * 60)
        self.log("开始清理测试数据")
        
        # 清理各种测试数据
        for category, ids in self.created_ids.items():
            for item_id in ids[:]:  # 使用切片创建副本避免修改迭代中的列表
                try:
                    if category == 'rcj_mc2ejflids' or category == 'rcj_mc_classifies':
                        # 这些是整数ID
                        endpoint = f"/dict/{category.replace('_', '-')}/{item_id}"
                    else:
                        # 这些是字符串ID
                        endpoint = f"/dict/{category.replace('_', '-')}/{item_id}"
                    
                    self.make_request("DELETE", endpoint)
                    self.log(f"已清理 {category}: {item_id}")
                except Exception as e:
                    self.log(f"清理 {category}: {item_id} 失败: {str(e)}", "WARNING")
        
        self.log("✅ 测试数据清理完成")
    
    def run_all_tests(self):
        """运行所有测试"""
        self.log("🚀 开始KSF RESTful API集成测试")
        self.log(f"测试目标: {self.base_url}")
        
        start_time = time.time()
        
        # 测试列表
        tests = [
            ("健康检查", self.test_health_check),
            ("Swagger文档", self.test_swagger_docs),
            ("分页功能", self.test_pagination),
            ("单位类别API", self.test_dw_types),
            ("单位API", self.test_dws),
            ("人材机二级分类属性API", self.test_rcj_ejfl_sxs),
            ("人材机一级分类API", self.test_rcj_yjfls),
            ("人材机二级分类API", self.test_rcj_ejfls),
            ("人材机名称映射API", self.test_rcj_mc2ejflids),
            ("人材机名称分类API", self.test_rcj_mc_classifies),
            ("错误处理", self.test_error_handling),
        ]
        
        # 运行测试
        for test_name, test_func in tests:
            self.test_results['total'] += 1
            try:
                if test_func():
                    self.test_results['passed'] += 1
                    self.log(f"✅ {test_name} 测试通过")
                else:
                    self.test_results['failed'] += 1
                    self.log(f"❌ {test_name} 测试失败")
            except Exception as e:
                self.test_results['failed'] += 1
                self.test_results['errors'].append(f"{test_name}: {str(e)}")
                self.log(f"❌ {test_name} 测试异常: {str(e)}", "ERROR")
        
        # 清理测试数据
        self.cleanup_test_data()
        
        # 输出测试结果
        end_time = time.time()
        duration = end_time - start_time
        
        self.log("=" * 60)
        self.log("📊 测试结果汇总")
        self.log(f"总测试数: {self.test_results['total']}")
        self.log(f"通过: {self.test_results['passed']}")
        self.log(f"失败: {self.test_results['failed']}")
        self.log(f"测试耗时: {duration:.2f}秒")
        
        if self.test_results['errors']:
            self.log("错误详情:")
            for error in self.test_results['errors']:
                self.log(f"  - {error}", "ERROR")
        
        success_rate = (self.test_results['passed'] / self.test_results['total']) * 100
        self.log(f"成功率: {success_rate:.1f}%")
        
        if self.test_results['failed'] == 0:
            self.log("🎉 所有测试通过！项目运行正常")
            return True
        else:
            self.log("⚠️ 部分测试失败，请检查项目配置")
            return False


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='KSF RESTful API 集成测试')
    parser.add_argument('--url', default='http://127.0.0.1:5678', 
                       help='API服务器地址 (默认: http://127.0.0.1:5678)')
    parser.add_argument('--timeout', type=int, default=30,
                       help='请求超时时间 (默认: 30秒)')
    
    args = parser.parse_args()
    
    # 创建测试器
    tester = APITester(args.url)
    tester.session.timeout = args.timeout
    
    # 运行测试
    success = tester.run_all_tests()
    
    # 根据测试结果设置退出码
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main() 