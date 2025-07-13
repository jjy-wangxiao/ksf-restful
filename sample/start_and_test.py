#!/usr/bin/env python3
"""
KSF RESTful API 启动和测试脚本
自动启动Flask服务器并运行API集成测试
"""

import subprocess
import time
import sys
import os
import signal
import requests
from pathlib import Path

class ServerManager:
    """服务器管理器"""
    
    def __init__(self, host='127.0.0.1', port=5678):
        self.host = host
        self.port = port
        self.server_process = None
        self.base_url = f"http://{host}:{port}"
    
    def start_server(self):
        """启动Flask服务器"""
        print(f"🚀 正在启动Flask服务器...")
        print(f"   地址: {self.base_url}")
        print(f"   Swagger文档: {self.base_url}/api/v1/docs")
        
        try:
            # 启动服务器进程
            self.server_process = subprocess.Popen(
                [sys.executable, 'run.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # 等待服务器启动
            print("⏳ 等待服务器启动...")
            for i in range(30):  # 最多等待30秒
                try:
                    response = requests.get(f"{self.base_url}/api/v1/docs", timeout=2)
                    if response.status_code == 200:
                        print("✅ 服务器启动成功！")
                        return True
                except requests.exceptions.RequestException:
                    pass
                
                time.sleep(1)
                print(f"   等待中... ({i+1}/30)")
            
            print("❌ 服务器启动超时")
            return False
            
        except Exception as e:
            print(f"❌ 启动服务器失败: {e}")
            return False
    
    def stop_server(self):
        """停止Flask服务器"""
        if self.server_process:
            print("🛑 正在停止服务器...")
            try:
                self.server_process.terminate()
                self.server_process.wait(timeout=10)
                print("✅ 服务器已停止")
            except subprocess.TimeoutExpired:
                print("⚠️ 服务器停止超时，强制终止...")
                self.server_process.kill()
            except Exception as e:
                print(f"❌ 停止服务器时出错: {e}")
    
    def check_server_status(self):
        """检查服务器状态"""
        try:
            response = requests.get(f"{self.base_url}/api/v1/docs", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def run_tests(self):
        """运行API测试"""
        print("\n🧪 开始运行API集成测试...")
        
        try:
            # 运行测试脚本
            result = subprocess.run(
                [sys.executable, 'test_api_integration.py', '--url', self.base_url],
                capture_output=True,
                text=True
            )
            
            # 输出测试结果
            print(result.stdout)
            if result.stderr:
                print("错误输出:")
                print(result.stderr)
            
            return result.returncode == 0
            
        except Exception as e:
            print(f"❌ 运行测试失败: {e}")
            return False


def main():
    """主函数"""
    print("=" * 60)
    print("KSF RESTful API 启动和测试工具")
    print("=" * 60)
    
    # 检查必要文件
    required_files = ['run.py', 'test_api_integration.py']
    for file in required_files:
        if not Path(file).exists():
            print(f"❌ 缺少必要文件: {file}")
            sys.exit(1)
    
    # 创建服务器管理器
    server_manager = ServerManager()
    
    try:
        # 启动服务器
        if not server_manager.start_server():
            print("❌ 无法启动服务器，退出")
            sys.exit(1)
        
        # 等待一下确保服务器完全启动
        time.sleep(2)
        
        # 运行测试
        test_success = server_manager.run_tests()
        
        # 输出最终结果
        print("\n" + "=" * 60)
        if test_success:
            print("🎉 所有测试通过！项目运行正常")
        else:
            print("⚠️ 部分测试失败，请检查项目配置")
        print("=" * 60)
        
        # 询问是否保持服务器运行
        print("\n服务器仍在运行中...")
        print(f"访问地址: {server_manager.base_url}")
        print(f"Swagger文档: {server_manager.base_url}/api/v1/docs")
        print("\n按 Ctrl+C 停止服务器")
        
        # 保持服务器运行
        try:
            while True:
                time.sleep(1)
                if not server_manager.check_server_status():
                    print("⚠️ 服务器已停止运行")
                    break
        except KeyboardInterrupt:
            print("\n👋 收到停止信号")
    
    except KeyboardInterrupt:
        print("\n👋 收到停止信号")
    except Exception as e:
        print(f"❌ 运行过程中出错: {e}")
    finally:
        # 停止服务器
        server_manager.stop_server()


if __name__ == "__main__":
    main() 