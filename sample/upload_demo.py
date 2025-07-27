#!/usr/bin/env python3
"""
文件上传API演示脚本
展示如何使用Flask应用的文件上传功能
"""
import requests
import os
import tempfile
from pathlib import Path

# API基础URL
BASE_URL = "http://localhost:5678/api/v1"

def create_test_file(content="这是一个测试文件的内容", filename="test.txt"):
    """创建测试文件"""
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, filename)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return file_path

def test_single_upload():
    """测试单个文件上传"""
    print("=== 测试单个文件上传 ===")
    
    # 创建测试文件
    file_path = create_test_file("这是单个文件上传测试", "single_test.txt")
    
    try:
        with open(file_path, 'rb') as f:
            files = {'file': ('single_test.txt', f, 'text/plain')}
            data = {
                'fileType': 'document',
                'description': '单个文件上传测试',
                'category': '测试'
            }
            
            response = requests.post(f"{BASE_URL}/upload/files", files=files, data=data)
            
            if response.status_code == 201:
                result = response.json()
                print(f"✅ 上传成功!")
                print(f"   文件ID: {result['id']}")
                print(f"   文件名: {result['filename']}")
                print(f"   文件大小: {result['file_size']} 字节")
                print(f"   下载链接: {result['download_url']}")
                return result['id']
            else:
                print(f"❌ 上传失败: {response.status_code}")
                print(f"   错误信息: {response.text}")
                return None
                
    finally:
        # 清理临时文件
        os.unlink(file_path)
        os.rmdir(os.path.dirname(file_path))

def test_batch_upload():
    """测试批量文件上传"""
    print("\n=== 测试批量文件上传 ===")
    
    # 创建多个测试文件
    files_data = []
    temp_files = []
    
    try:
        for i in range(3):
            content = f"这是批量上传测试文件 {i+1} 的内容"
            filename = f"batch_test_{i+1}.txt"
            file_path = create_test_file(content, filename)
            temp_files.append(file_path)
            
            with open(file_path, 'rb') as f:
                files_data.append(('files', (filename, f, 'text/plain')))
        
        data = {
            'fileType': 'document',
            'description': '批量文件上传测试',
            'category': '测试'
        }
        
        response = requests.post(f"{BASE_URL}/upload/files/batch", files=files_data, data=data)
        
        if response.status_code == 201:
            result = response.json()
            print(f"✅ 批量上传成功!")
            print(f"   成功数量: {result['success_count']}")
            print(f"   失败数量: {result['failed_count']}")
            print(f"   上传的文件:")
            for file_info in result['files']:
                print(f"     - {file_info['original_filename']} (ID: {file_info['id']})")
            
            if result['errors']:
                print(f"   错误信息:")
                for error in result['errors']:
                    print(f"     - {error}")
        else:
            print(f"❌ 批量上传失败: {response.status_code}")
            print(f"   错误信息: {response.text}")
            
    finally:
        # 清理临时文件
        for file_path in temp_files:
            os.unlink(file_path)
            os.rmdir(os.path.dirname(file_path))

def test_file_list():
    """测试获取文件列表"""
    print("\n=== 测试获取文件列表 ===")
    
    response = requests.get(f"{BASE_URL}/upload/files?page=1&per_page=10")
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ 获取文件列表成功!")
        print(f"   总文件数: {result['meta']['total']}")
        print(f"   当前页: {result['meta']['page']}")
        print(f"   每页数量: {result['meta']['per_page']}")
        print(f"   文件列表:")
        
        for file_info in result['data']:
            print(f"     - {file_info['filename']} (ID: {file_info['id']}, 大小: {file_info['file_size']} 字节)")
        
        return result['data']
    else:
        print(f"❌ 获取文件列表失败: {response.status_code}")
        print(f"   错误信息: {response.text}")
        return []

def test_file_download(file_id):
    """测试文件下载"""
    print(f"\n=== 测试文件下载 (ID: {file_id}) ===")
    
    response = requests.get(f"{BASE_URL}/upload/files/{file_id}/download")
    
    if response.status_code == 200:
        print(f"✅ 文件下载成功!")
        print(f"   文件大小: {len(response.content)} 字节")
        print(f"   内容类型: {response.headers.get('Content-Type', 'unknown')}")
        
        # 保存下载的文件
        download_path = f"downloaded_file_{file_id}.txt"
        with open(download_path, 'wb') as f:
            f.write(response.content)
        print(f"   文件已保存到: {download_path}")
        
        return download_path
    else:
        print(f"❌ 文件下载失败: {response.status_code}")
        print(f"   错误信息: {response.text}")
        return None

def test_file_info(file_id):
    """测试获取文件信息"""
    print(f"\n=== 测试获取文件信息 (ID: {file_id}) ===")
    
    response = requests.get(f"{BASE_URL}/upload/files/{file_id}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ 获取文件信息成功!")
        print(f"   文件ID: {result['id']}")
        print(f"   文件名: {result['filename']}")
        print(f"   文件大小: {result['file_size']} 字节")
        print(f"   文件类型: {result['file_type']}")
        print(f"   上传时间: {result['upload_time']}")
        print(f"   文件哈希: {result['hash']}")
    else:
        print(f"❌ 获取文件信息失败: {response.status_code}")
        print(f"   错误信息: {response.text}")

def test_file_delete(file_id):
    """测试文件删除"""
    print(f"\n=== 测试文件删除 (ID: {file_id}) ===")
    
    response = requests.delete(f"{BASE_URL}/upload/files/{file_id}")
    
    if response.status_code == 200:
        print(f"✅ 文件删除成功!")
        result = response.json()
        print(f"   消息: {result.get('message', '删除成功')}")
    else:
        print(f"❌ 文件删除失败: {response.status_code}")
        print(f"   错误信息: {response.text}")

def main():
    """主函数"""
    print("🚀 开始文件上传API演示")
    print("=" * 50)
    
    # 测试单个文件上传
    file_id = test_single_upload()
    
    if file_id:
        # 测试获取文件信息
        test_file_info(file_id)
        
        # 测试文件下载
        downloaded_file = test_file_download(file_id)
        
        # 测试文件删除
        test_file_delete(file_id)
    
    # 测试批量文件上传
    test_batch_upload()
    
    # 测试获取文件列表
    files = test_file_list()
    
    print("\n" + "=" * 50)
    print("🎉 文件上传API演示完成!")
    
    # 清理下载的文件
    if 'downloaded_file' in locals() and downloaded_file and os.path.exists(downloaded_file):
        os.unlink(downloaded_file)
        print(f"🧹 已清理下载的文件: {downloaded_file}")

if __name__ == "__main__":
    main() 