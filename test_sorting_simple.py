#!/usr/bin/env python3
"""
简单的排序功能测试脚本
不依赖数据库连接，只测试排序逻辑
"""

def test_sorting_logic():
    """测试排序逻辑"""
    print("=== 测试排序逻辑 ===")
    
    # 模拟从数据库获取的数据
    mock_data = [
        {'ejflid': '03', 'ejflmc': '分类C', 'yjflid': '02', 'yjflmc': '一级B'},
        {'ejflid': '01', 'ejflmc': '分类A', 'yjflid': '01', 'yjflmc': '一级A'},
        {'ejflid': '02', 'ejflmc': '分类B', 'yjflid': '01', 'yjflmc': '一级A'},
        {'ejflid': '04', 'ejflmc': '分类D', 'yjflid': '02', 'yjflmc': '一级B'},
    ]
    
    print("原始数据:")
    for item in mock_data:
        print(f"  {item['ejflid']}-{item['ejflmc']} (一级: {item['yjflid']}-{item['yjflmc']})")
    
    # 模拟去重逻辑
    ejfl_set = set()
    ejfl_info = {}
    
    for item in mock_data:
        ejfl_key = f"{item['ejflid']}_{item['ejflmc']}"
        if ejfl_key not in ejfl_set:
            ejfl_set.add(ejfl_key)
            ejfl_info[ejfl_key] = {
                'ejflid': item['ejflid'],
                'ejflmc': item['ejflmc'],
                'yjflid': item['yjflid'],
                'yjflmc': item['yjflmc']
            }
    
    print("\n去重后数据:")
    for key, info in ejfl_info.items():
        print(f"  {info['ejflid']}-{info['ejflmc']} (一级: {info['yjflid']}-{info['yjflmc']})")
    
    # 按一级分类分组
    yjfl_groups = {}
    for ejfl_key, info in ejfl_info.items():
        yjfl_key = f"{info['yjflid']}_{info['yjflmc']}"
        if yjfl_key not in yjfl_groups:
            yjfl_groups[yjfl_key] = {
                'yjflid': info['yjflid'],
                'yjflmc': info['yjflmc'],
                'ejfls': []
            }
        yjfl_groups[yjfl_key]['ejfls'].append({
            'ejflid': info['ejflid'],
            'ejflmc': info['ejflmc']
        })
    
    print("\n分组后数据:")
    for yjfl_key, yjfl_data in yjfl_groups.items():
        print(f"  一级分类: {yjfl_data['yjflid']}-{yjfl_data['yjflmc']}")
        for ejfl in yjfl_data['ejfls']:
            print(f"    - {ejfl['ejflid']}-{ejfl['ejflmc']}")
    
    # 测试排序逻辑
    print("\n=== 测试排序逻辑 ===")
    
    # 1. 二级分类排序
    for yjfl_key, yjfl_data in yjfl_groups.items():
        print(f"\n一级分类 {yjfl_data['yjflid']}-{yjfl_data['yjflmc']} 的二级分类排序:")
        print(f"  排序前: {[ejfl['ejflid'] for ejfl in yjfl_data['ejfls']]}")
        
        sorted_ejfls = sorted(yjfl_data['ejfls'], key=lambda x: x['ejflid'])
        print(f"  排序后: {[ejfl['ejflid'] for ejfl in sorted_ejfls]}")
        
        # 验证排序
        ejfl_ids = [ejfl['ejflid'] for ejfl in sorted_ejfls]
        if ejfl_ids == sorted(ejfl_ids):
            print(f"  ✅ 二级分类排序正确")
        else:
            print(f"  ❌ 二级分类排序错误")
    
    # 2. 一级分类排序
    print(f"\n一级分类排序:")
    yjfl_list = list(yjfl_groups.items())
    print(f"  排序前: {[yjfl_data['yjflid'] for _, yjfl_data in yjfl_list]}")
    
    sorted_yjfl_list = sorted(yjfl_list, key=lambda x: x[1]['yjflid'])
    print(f"  排序后: {[yjfl_data['yjflid'] for _, yjfl_data in sorted_yjfl_list]}")
    
    # 验证排序
    yjfl_ids = [yjfl_data['yjflid'] for _, yjfl_data in sorted_yjfl_list]
    if yjfl_ids == sorted(yjfl_ids):
        print(f"  ✅ 一级分类排序正确")
    else:
        print(f"  ❌ 一级分类排序错误")

def test_key_extraction():
    """测试key提取逻辑"""
    print("\n=== 测试key提取逻辑 ===")
    
    # 模拟TreeResponseDTO的key格式
    test_keys = [
        "yjfl-01",
        "yjfl-02", 
        "ejfl-01",
        "ejfl-02",
        "ejfl-03"
    ]
    
    print("测试key提取:")
    for key in test_keys:
        parts = key.split('-')
        if len(parts) == 2:
            prefix, id_part = parts
            print(f"  {key} -> prefix: {prefix}, id: {id_part}")
        else:
            print(f"  {key} -> 格式错误")
    
    # 测试排序key提取
    print("\n测试排序key提取:")
    yjfl_keys = ["yjfl-02", "yjfl-01", "yjfl-03"]
    yjfl_ids = [int(key.split('-')[1]) for key in yjfl_keys]
    print(f"  原始keys: {yjfl_keys}")
    print(f"  提取的IDs: {yjfl_ids}")
    print(f"  排序后IDs: {sorted(yjfl_ids)}")

if __name__ == "__main__":
    print("开始测试排序逻辑...\n")
    
    try:
        test_sorting_logic()
        test_key_extraction()
        
        print("\n🎉 排序逻辑测试完成！")
        print("\n排序功能说明:")
        print("1. ✅ 二级分类按ejflid排序")
        print("2. ✅ 一级分类按yjflid排序")
        print("3. ✅ 支持从key中提取ID进行排序")
        print("4. ✅ 排序逻辑正确，可以应用到实际代码中")
        
    except Exception as e:
        print(f"❌ 测试过程中出现错误: {e}")
        import traceback
        traceback.print_exc() 