# 树形结构API使用指南

## 概述

树形结构API提供了符合前端Ant Design Tree组件格式的数据结构，支持获取文件系统的树形结构展示。

## API端点

### GET /api/v1/matrix/tree

获取树形结构数据

#### 请求参数

| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| fileid | string | 否 | 文件ID，指定时获取该文件的树形结构，不指定时获取根目录结构 |

#### 响应格式

```json
[
  {
    "title": "根目录1",
    "key": "0-0",
    "children": [
      {
        "title": "子目录1-0",
        "key": "0-0-0",
        "children": [
          {
            "title": "叶子节点1",
            "key": "0-0-0-0"
          },
          {
            "title": "叶子节点2",
            "key": "0-0-0-1"
          }
        ]
      },
      {
        "title": "子目录1-1",
        "key": "0-0-1",
        "children": [
          {
            "title": "叶子节点3",
            "key": "0-0-1-0"
          }
        ]
      }
    ]
  }
]
```

#### 响应字段说明

| 字段名 | 类型 | 描述 |
|--------|------|------|
| title | string | 节点显示标题 |
| key | string | 节点唯一标识符 |
| children | array | 子节点列表，可选 |

## 使用示例

### 获取根目录树形结构

```bash
curl -X GET "http://localhost:5000/api/v1/matrix/tree"
```

### 获取特定文件的树形结构

```bash
curl -X GET "http://localhost:5000/api/v1/matrix/tree?fileid=your-file-id"
```

## 前端集成

### React + Ant Design

```jsx
import { Tree } from 'antd';
import { useState, useEffect } from 'react';

const TreeComponent = () => {
  const [treeData, setTreeData] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchTreeData = async (fileid = null) => {
    setLoading(true);
    try {
      const url = fileid 
        ? `/api/v1/matrix/tree?fileid=${fileid}`
        : '/api/v1/matrix/tree';
      
      const response = await fetch(url);
      const data = await response.json();
      setTreeData(data);
    } catch (error) {
      console.error('获取树形结构失败:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTreeData();
  }, []);

  return (
    <Tree
      treeData={treeData}
      loading={loading}
      onSelect={(selectedKeys, info) => {
        console.log('选中节点:', selectedKeys, info);
      }}
    />
  );
};
```

## 业务逻辑实现

### 需要修改的文件

1. **app/services/matrix_service.py**
   - `_build_file_tree()` - 实现特定文件的树形结构构建
   - `_build_root_tree()` - 实现根目录的树形结构构建

### 实现示例

```python
def _build_file_tree(self, fileid: str) -> List[TreeResponseDTO]:
    """构建特定文件的树形结构"""
    # 1. 查询文件信息
    file = File.query.filter_by(id=fileid).first()
    if not file:
        return []
    
    # 2. 查询文件的子节点（根据实际业务需求）
    children = []
    # TODO: 实现子节点查询逻辑
    
    # 3. 构建树形结构
    return [
        TreeResponseDTO(
            title=file.filename,
            key=file.id,
            children=children
        )
    ]

def _build_root_tree(self) -> List[TreeResponseDTO]:
    """构建根目录树形结构"""
    # 1. 查询所有根级文件/文件夹
    root_files = File.query.filter_by(parent_id=None).all()
    
    # 2. 构建树形结构
    tree_data = []
    for file in root_files:
        children = self._get_children_recursive(file.id)
        tree_data.append(
            TreeResponseDTO(
                title=file.filename,
                key=file.id,
                children=children
            )
        )
    
    return tree_data

def _get_children_recursive(self, parent_id: str) -> List[TreeResponseDTO]:
    """递归获取子节点"""
    children = File.query.filter_by(parent_id=parent_id).all()
    result = []
    
    for child in children:
        grand_children = self._get_children_recursive(child.id)
        result.append(
            TreeResponseDTO(
                title=child.filename,
                key=child.id,
                children=grand_children
            )
        )
    
    return result
```

## 错误处理

API支持以下错误响应：

- `400` - 参数错误
- `404` - 文件不存在
- `500` - 服务器错误

错误响应格式：

```json
{
  "code": "ERROR_CODE",
  "message": "错误描述",
  "details": {
    "error": "详细错误信息"
  },
  "timestamp": "2024-01-01T00:00:00"
}
```

## 测试

运行测试脚本验证功能：

```bash
python test_tree_api.py
```

## 注意事项

1. 树形结构的key必须是唯一的
2. 避免过深的嵌套层级，建议不超过5层
3. 大量数据时考虑分页或懒加载
4. 确保数据库查询性能，避免N+1查询问题 