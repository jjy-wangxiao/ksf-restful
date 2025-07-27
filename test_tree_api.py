#!/usr/bin/env python3
"""
树形结构API测试脚本
用于验证整个请求链条是否正常工作
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.dto.matrix_dto import TreeResponseDTO
from app.services.matrix_service import MatrixService

def test_tree_dto():
    """测试TreeResponseDTO的基本功能"""
    print("=== 测试TreeResponseDTO ===")
    
    # 创建简单的树形结构
    leaf1 = TreeResponseDTO(title="叶子节点1", key="0-0-0-0")
    leaf2 = TreeResponseDTO(title="叶子节点2", key="0-0-0-1")
    
    parent1 = TreeResponseDTO(
        title="父节点1-0",
        key="0-0-0",
        children=[leaf1, leaf2]
    )
    
    root = TreeResponseDTO(
        title="根节点",
        key="0-0",
        children=[parent1]
    )
    
    # 转换为字典
    result = root.to_dict()
    print("TreeResponseDTO转换结果:")
    print(result)
    print()
    
    return result

def test_matrix_service():
    """测试MatrixService的树形结构功能"""
    print("=== 测试MatrixService ===")
    
    service = MatrixService()
    
    # 测试获取根目录树形结构
    print("获取根目录树形结构:")
    root_tree = service.get_tree()
    for node in root_tree:
        print(f"- {node.title} (key: {node.key})")
        if node.children:
            for child in node.children:
                print(f"  - {child.title} (key: {child.key})")
                if child.children:
                    for grandchild in child.children:
                        print(f"    - {grandchild.title} (key: {grandchild.key})")
    print()
    
    # 测试获取特定文件的树形结构
    print("获取特定文件树形结构 (fileid: 1):")
    file_tree = service.get_tree(fileid="1")
    for node in file_tree:
        print(f"- {node.title} (key: {node.key})")
        if node.children:
            for child in node.children:
                print(f"  - {child.title} (key: {child.key})")
                if child.children:
                    for grandchild in child.children:
                        print(f"    - {grandchild.title} (key: {grandchild.key})")
    print()

def test_file_classification_tree():
    """测试文件分类树形结构构建"""
    print("=== 测试文件分类树形结构 ===")
    
    service = MatrixService()
    
    # 测试不同的文件ID
    test_fileids = ["1", "2", "999"]  # 包括可能存在的和不存在的文件ID
    
    for fileid in test_fileids:
        print(f"测试文件ID: {fileid}")
        try:
            tree_data = service._build_file_classification_tree(fileid)
            if tree_data:
                print(f"  ✅ 成功构建树形结构，包含 {len(tree_data)} 个一级分类")
                for yjfl_node in tree_data:
                    print(f"    - 一级分类: {yjfl_node.title} (key: {yjfl_node.key})")
                    if yjfl_node.children:
                        print(f"      包含 {len(yjfl_node.children)} 个二级分类:")
                        for ejfl_node in yjfl_node.children:
                            print(f"        - {ejfl_node.title} (key: {ejfl_node.key})")
                
                # 验证排序
                print(f"  🔍 验证排序:")
                yjfl_keys = [node.key for node in tree_data]
                yjfl_ids = [int(key.split('-')[1]) for key in yjfl_keys]
                if yjfl_ids == sorted(yjfl_ids):
                    print(f"    ✅ 一级分类按ID排序正确")
                else:
                    print(f"    ❌ 一级分类排序错误: {yjfl_ids}")
                
                # 验证二级分类排序
                for yjfl_node in tree_data:
                    if yjfl_node.children:
                        ejfl_keys = [child.key for child in yjfl_node.children]
                        ejfl_ids = [int(key.split('-')[1]) for key in ejfl_keys]
                        if ejfl_ids == sorted(ejfl_ids):
                            print(f"    ✅ 二级分类按ID排序正确: {yjfl_node.title}")
                        else:
                            print(f"    ❌ 二级分类排序错误: {yjfl_node.title} - {ejfl_ids}")
            else:
                print(f"  ⚠️  未找到相关数据或文件不存在")
        except Exception as e:
            print(f"  ❌ 构建失败: {e}")
        print()

def test_api_response_format():
    """测试API响应格式是否符合前端期望"""
    print("=== 测试API响应格式 ===")
    
    service = MatrixService()
    
    # 获取树形结构数据
    tree_data = service.get_tree()
    
    # 转换为API响应格式
    response_data = [node.to_dict() for node in tree_data]
    
    print("API响应格式:")
    print(response_data)
    print()
    
    # 验证格式是否符合前端期望
    expected_format = {
        'title': str,
        'key': str,
        'children': list
    }
    
    def validate_node(node):
        """验证节点格式"""
        if not isinstance(node, dict):
            return False
        if 'title' not in node or 'key' not in node:
            return False
        if not isinstance(node['title'], str) or not isinstance(node['key'], str):
            return False
        if 'children' in node and not isinstance(node['children'], list):
            return False
        return True
    
    def validate_tree(nodes):
        """递归验证树形结构"""
        for node in nodes:
            if not validate_node(node):
                print(f"❌ 节点格式错误: {node}")
                return False
            if 'children' in node and node['children']:
                if not validate_tree(node['children']):
                    return False
        return True
    
    if validate_tree(response_data):
        print("✅ API响应格式验证通过，符合前端期望")
    else:
        print("❌ API响应格式验证失败")
    
    print()

def test_data_flow():
    """测试数据流程"""
    print("=== 测试数据流程 ===")
    
    service = MatrixService()
    
    # 测试完整的数据流程
    print("1. 测试不带fileid的get_tree调用:")
    try:
        result1 = service.get_tree()
        print(f"   ✅ 成功，返回 {len(result1)} 个根节点")
    except Exception as e:
        print(f"   ❌ 失败: {e}")
    
    print("\n2. 测试带fileid的get_tree调用:")
    try:
        result2 = service.get_tree(fileid="1")
        print(f"   ✅ 成功，返回 {len(result2)} 个根节点")
    except Exception as e:
        print(f"   ❌ 失败: {e}")
    
    print("\n3. 测试不存在的fileid:")
    try:
        result3 = service.get_tree(fileid="999999")
        print(f"   ✅ 成功处理，返回 {len(result3)} 个根节点")
    except Exception as e:
        print(f"   ❌ 失败: {e}")
    
    print()

def test_sorting_functionality():
    """测试排序功能"""
    print("=== 测试排序功能 ===")
    
    service = MatrixService()
    
    # 测试完整分类树的排序
    print("1. 测试完整分类树的排序:")
    try:
        tree_data = service._build_classification_tree()
        if tree_data:
            print(f"   ✅ 成功构建完整分类树，包含 {len(tree_data)} 个一级分类")
            
            # 验证一级分类排序
            yjfl_keys = [node.key for node in tree_data]
            yjfl_ids = [int(key.split('-')[1]) for key in yjfl_keys]
            if yjfl_ids == sorted(yjfl_ids):
                print(f"   ✅ 一级分类按ID排序正确: {yjfl_ids}")
            else:
                print(f"   ❌ 一级分类排序错误: {yjfl_ids}")
            
            # 验证二级分类排序
            for yjfl_node in tree_data:
                if yjfl_node.children:
                    ejfl_keys = [child.key for child in yjfl_node.children]
                    ejfl_ids = [int(key.split('-')[1]) for key in ejfl_keys]
                    if ejfl_ids == sorted(ejfl_ids):
                        print(f"   ✅ 二级分类按ID排序正确: {yjfl_node.title}")
                    else:
                        print(f"   ❌ 二级分类排序错误: {yjfl_node.title} - {ejfl_ids}")
        else:
            print(f"   ⚠️  未找到分类数据")
    except Exception as e:
        print(f"   ❌ 构建失败: {e}")
    
    print("\n2. 测试文件分类树的排序:")
    try:
        tree_data = service._build_file_classification_tree("1")
        if tree_data:
            print(f"   ✅ 成功构建文件分类树，包含 {len(tree_data)} 个一级分类")
            
            # 验证一级分类排序
            yjfl_keys = [node.key for node in tree_data]
            yjfl_ids = [int(key.split('-')[1]) for key in yjfl_keys]
            if yjfl_ids == sorted(yjfl_ids):
                print(f"   ✅ 一级分类按ID排序正确: {yjfl_ids}")
            else:
                print(f"   ❌ 一级分类排序错误: {yjfl_ids}")
            
            # 验证二级分类排序
            for yjfl_node in tree_data:
                if yjfl_node.children:
                    ejfl_keys = [child.key for child in yjfl_node.children]
                    ejfl_ids = [int(key.split('-')[1]) for key in ejfl_keys]
                    if ejfl_ids == sorted(ejfl_ids):
                        print(f"   ✅ 二级分类按ID排序正确: {yjfl_node.title}")
                    else:
                        print(f"   ❌ 二级分类排序错误: {yjfl_node.title} - {ejfl_ids}")
        else:
            print(f"   ⚠️  未找到文件相关数据")
    except Exception as e:
        print(f"   ❌ 构建失败: {e}")
    
    print()

if __name__ == "__main__":
    print("开始测试树形结构API...\n")
    
    try:
        test_tree_dto()
        test_matrix_service()
        test_file_classification_tree()
        test_api_response_format()
        test_data_flow()
        test_sorting_functionality()
        
        print("🎉 所有测试完成！")
        print("\n修改说明:")
        print("1. ✅ 实现了通过fileid获取相关联的rcjhzmx")
        print("2. ✅ 通过rcjhzmx的classify_info属性获取RcjMCClassifyBig")
        print("3. ✅ 从RcjMCClassifyBig中获取二级分类信息")
        print("4. ✅ 根据已有的二级分类构造树形结构")
        print("5. ✅ 支持去重和按一级分类分组")
        print("6. ✅ 实现了按ID排序功能")
        print("   - 一级分类按yjflid排序")
        print("   - 二级分类按ejflid排序")
        print("   - 数据库查询时使用order_by确保排序")
        
    except Exception as e:
        print(f"❌ 测试过程中出现错误: {e}")
        import traceback
        traceback.print_exc() 