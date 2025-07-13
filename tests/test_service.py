"""
Service层测试文件
测试业务逻辑和数据转换功能
"""
import pytest
from unittest.mock import Mock, patch
from datetime import datetime
from app.services.dict_service import DictService
from app.dto.dict import (
    DwTypeRequestDTO, DwTypeUpdateRequestDTO, DwTypeResponseDTO,
    DwRequestDTO, DwUpdateRequestDTO, DwResponseDTO,
    RcjEjflSxRequestDTO, RcjEjflSxUpdateRequestDTO, RcjEjflSxResponseDTO,
    RcjYjflRequestDTO, RcjYjflUpdateRequestDTO, RcjYjflResponseDTO,
    RcjEjflRequestDTO, RcjEjflUpdateRequestDTO, RcjEjflResponseDTO,
    RcjMC2EjflidRequestDTO, RcjMC2EjflidUpdateRequestDTO, RcjMC2EjflidResponseDTO,
    RcjMCClassifyRequestDTO, RcjMCClassifyUpdateRequestDTO, RcjMCClassifyResponseDTO,
    PaginationMeta, PaginatedResponse
)


class TestDictService:
    """测试字典管理服务"""
    
    @pytest.fixture
    def mock_db_session(self):
        """模拟数据库会话"""
        with patch('app.services.dict_service.db') as mock_db:
            yield mock_db
    
    @pytest.fixture
    def mock_models(self):
        """模拟模型类"""
        with patch('app.services.dict_service.DwType') as mock_dw_type, \
             patch('app.services.dict_service.Dw') as mock_dw, \
             patch('app.services.dict_service.RcjEjflSx') as mock_rcj_ejfl_sx, \
             patch('app.services.dict_service.RcjYjfl') as mock_rcj_yjfl, \
             patch('app.services.dict_service.RcjEjfl') as mock_rcj_ejfl, \
             patch('app.services.dict_service.RcjMC2Ejflid') as mock_rcj_mc2ejflid, \
             patch('app.services.dict_service.RcjMCClassify') as mock_rcj_mc_classify:
            
            yield {
                'DwType': mock_dw_type,
                'Dw': mock_dw,
                'RcjEjflSx': mock_rcj_ejfl_sx,
                'RcjYjfl': mock_rcj_yjfl,
                'RcjEjfl': mock_rcj_ejfl,
                'RcjMC2Ejflid': mock_rcj_mc2ejflid,
                'RcjMCClassify': mock_rcj_mc_classify
            }
    
    def test_get_dw_types_success(self, mock_db_session, mock_models):
        """测试获取单位类别列表成功"""
        # 模拟分页对象
        mock_pagination = Mock()
        mock_pagination.page = 1
        mock_pagination.per_page = 10
        mock_pagination.total = 2
        mock_pagination.pages = 1
        mock_pagination.has_next = False
        mock_pagination.has_prev = False
        mock_pagination.items = [
            Mock(
                id="01",
                typeName="重量",
                create_time=datetime.now(),
                update_time=datetime.now()
            ),
            Mock(
                id="02",
                typeName="长度",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
        ]
        
        mock_models['DwType'].query.paginate.return_value = mock_pagination
        mock_models['DwType'].query.filter_by.return_value.paginate.return_value = mock_pagination
        
        # 执行测试
        dict_service = DictService()
        result = dict_service.get_dw_types(page=1, per_page=10)
        
        # 验证结果
        assert isinstance(result, PaginatedResponse)
        assert len(result.data) == 2
        assert result.data[0].id == "01"
        assert result.data[0].typeName == "重量"
        assert result.data[1].id == "02"
        assert result.data[1].typeName == "长度"
        assert result.meta.page == 1
        assert result.meta.total == 2
    
    def test_get_dw_type_by_id_found(self, mock_models):
        """测试根据ID获取单位类别成功"""
        # 模拟找到的记录
        mock_dw_type = Mock(
            id="01",
            typeName="重量",
            create_time=datetime.now(),
            update_time=datetime.now()
        )
        mock_models['DwType'].query.get.return_value = mock_dw_type
        
        # 执行测试
        dict_service = DictService()
        result = dict_service.get_dw_type_by_id("01")
        
        # 验证结果
        assert isinstance(result, DwTypeResponseDTO)
        assert result.id == "01"
        assert result.typeName == "重量"
    
    def test_get_dw_type_by_id_not_found(self, mock_models):
        """测试根据ID获取单位类别失败"""
        # 模拟未找到记录
        mock_models['DwType'].query.get.return_value = None
        
        # 执行测试
        dict_service = DictService()
        result = dict_service.get_dw_type_by_id("99")
        
        # 验证结果
        assert result is None
    
    def test_create_dw_type_success(self, mock_db_session, mock_models):
        """测试创建单位类别成功"""
        # 模拟不存在记录
        mock_models['DwType'].query.get.return_value = None
        mock_models['DwType'].query.filter_by.return_value.first.return_value = None
        
        # 模拟创建的记录
        mock_dw_type = Mock(
            id="01",
            typeName="重量",
            create_time=datetime.now(),
            update_time=datetime.now()
        )
        mock_models['DwType'].return_value = mock_dw_type
        
        # 执行测试
        dto = DwTypeRequestDTO(id="01", typeName="重量")
        dict_service = DictService()
        result = dict_service.create_dw_type(dto)
        
        # 验证结果
        assert isinstance(result, DwTypeResponseDTO)
        assert result.id == "01"
        assert result.typeName == "重量"
        mock_db_session.session.add.assert_called_once()
        mock_db_session.session.commit.assert_called_once()
    
    def test_create_dw_type_duplicate_id(self, mock_models):
        """测试创建单位类别ID重复"""
        # 模拟ID已存在
        mock_models['DwType'].query.get.return_value = Mock()
        
        # 执行测试
        dto = DwTypeRequestDTO(id="01", typeName="重量")
        
        with pytest.raises(ValueError, match="单位类别ID已存在"):
            dict_service = DictService()
            dict_service.create_dw_type(dto)
    
    def test_create_dw_type_duplicate_name(self, mock_models):
        """测试创建单位类别名称重复"""
        # 模拟ID不存在但名称已存在
        mock_models['DwType'].query.get.return_value = None
        mock_models['DwType'].query.filter_by.return_value.first.return_value = Mock()
        
        # 执行测试
        dto = DwTypeRequestDTO(id="01", typeName="重量")
        
        with pytest.raises(ValueError, match="单位类别名称已存在"):
            dict_service = DictService()
            dict_service.create_dw_type(dto)
    
    def test_update_dw_type_success(self, mock_db_session, mock_models):
        """测试更新单位类别成功"""
        # 模拟找到的记录
        mock_dw_type = Mock(
            id="01",
            typeName="重量",
            create_time=datetime.now(),
            update_time=datetime.now()
        )
        mock_models['DwType'].query.get.return_value = mock_dw_type
        mock_models['DwType'].query.filter_by.return_value.first.return_value = None
        
        # 执行测试
        dto = DwTypeUpdateRequestDTO(typeName="长度")
        dict_service = DictService()
        result = dict_service.update_dw_type("01", dto)
        
        # 验证结果
        assert isinstance(result, DwTypeResponseDTO)
        assert result.id == "01"
        assert result.typeName == "长度"
        mock_db_session.session.commit.assert_called_once()
    
    def test_update_dw_type_not_found(self, mock_models):
        """测试更新单位类别不存在"""
        # 模拟未找到记录
        mock_models['DwType'].query.get.return_value = None
        
        # 执行测试
        dto = DwTypeUpdateRequestDTO(typeName="长度")
        dict_service = DictService()
        result = dict_service.update_dw_type("99", dto)
        
        # 验证结果
        assert result is None
    
    def test_delete_dw_type_success(self, mock_db_session, mock_models):
        """测试删除单位类别成功"""
        # 模拟找到的记录
        mock_dw_type = Mock()
        mock_models['DwType'].query.get.return_value = mock_dw_type
        
        # 执行测试
        dict_service = DictService()
        result = dict_service.delete_dw_type("01")
        
        # 验证结果
        assert result is True
        mock_db_session.session.delete.assert_called_once_with(mock_dw_type)
        mock_db_session.session.commit.assert_called_once()
    
    def test_delete_dw_type_not_found(self, mock_models):
        """测试删除单位类别不存在"""
        # 模拟未找到记录
        mock_models['DwType'].query.get.return_value = None
        
        # 执行测试
        dict_service = DictService()
        result = dict_service.delete_dw_type("99")
        
        # 验证结果
        assert result is False
    
    def test_get_dws_with_type_filter(self, mock_models):
        """测试获取单位列表（带类别过滤）"""
        # 模拟分页对象
        mock_pagination = Mock()
        mock_pagination.page = 1
        mock_pagination.per_page = 10
        mock_pagination.total = 1
        mock_pagination.pages = 1
        mock_pagination.has_next = False
        mock_pagination.has_prev = False
        mock_pagination.items = [
            Mock(
                id="0010",
                type_id="01",
                dw="个",
                create_time=datetime.now(),
                update_time=datetime.now(),
                type=Mock(
                    id="01",
                    typeName="重量",
                    create_time=datetime.now(),
                    update_time=datetime.now()
                )
            )
        ]
        
        mock_models['Dw'].query.paginate.return_value = mock_pagination
        mock_models['Dw'].query.filter_by.return_value.paginate.return_value = mock_pagination
        
        # 执行测试
        dict_service = DictService()
        result = dict_service.get_dws(page=1, per_page=10, type_id="01")
        
        # 验证结果
        assert isinstance(result, PaginatedResponse)
        assert len(result.data) == 1
        assert result.data[0].id == "0010"
        assert result.data[0].dw == "个"
        assert result.data[0].type_id == "01"
        assert result.data[0].type is not None
        assert result.data[0].type.id == "01"
    
    def test_create_dw_success(self, mock_db_session, mock_models):
        """测试创建单位成功"""
        # 模拟不存在记录
        mock_models['Dw'].query.get.return_value = None
        mock_models['Dw'].query.filter_by.return_value.first.return_value = None
        mock_models['DwType'].query.get.return_value = Mock()
        
        # 模拟创建的记录
        mock_dw = Mock(
            id="0010",
            type_id="01",
            dw="个",
            create_time=datetime.now(),
            update_time=datetime.now()
        )
        mock_models['Dw'].return_value = mock_dw
        
        # 执行测试
        dto = DwRequestDTO(id="0010", dw="个", type_id="01")
        dict_service = DictService()
        result = dict_service.create_dw(dto)
        
        # 验证结果
        assert isinstance(result, DwResponseDTO)
        assert result.id == "0010"
        assert result.dw == "个"
        assert result.type_id == "01"
        mock_db_session.session.add.assert_called_once()
        mock_db_session.session.commit.assert_called_once()
    
    def test_create_dw_invalid_type_id(self, mock_models):
        """测试创建单位类别ID无效"""
        # 模拟ID不存在
        mock_models['Dw'].query.get.return_value = None
        mock_models['Dw'].query.filter_by.return_value.first.return_value = None
        mock_models['DwType'].query.get.return_value = None
        
        # 执行测试
        dto = DwRequestDTO(id="0010", dw="个", type_id="99")
        
        with pytest.raises(ValueError, match="指定的类别ID不存在"):
            dict_service = DictService()
            dict_service.create_dw(dto)


class TestRcjEjflSxService:
    """测试人材机二级分类属性服务"""
    
    @pytest.fixture
    def mock_models(self):
        """模拟模型类"""
        with patch('app.services.dict_service.RcjEjflSx') as mock_rcj_ejfl_sx:
            yield {'RcjEjflSx': mock_rcj_ejfl_sx}
    
    def test_get_rcj_ejfl_sxs_success(self, mock_models):
        """测试获取人材机二级分类属性列表成功"""
        # 模拟分页对象
        mock_pagination = Mock()
        mock_pagination.page = 1
        mock_pagination.per_page = 10
        mock_pagination.total = 1
        mock_pagination.pages = 1
        mock_pagination.has_next = False
        mock_pagination.has_prev = False
        mock_pagination.items = [
            Mock(
                id="0001",
                sx="规格",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
        ]
        
        mock_models['RcjEjflSx'].query.paginate.return_value = mock_pagination
        mock_models['RcjEjflSx'].query.filter_by.return_value.paginate.return_value = mock_pagination
        
        # 执行测试
        dict_service = DictService()
        result = dict_service.get_rcj_ejfl_sxs(page=1, per_page=10)
        
        # 验证结果
        assert isinstance(result, PaginatedResponse)
        assert len(result.data) == 1
        assert result.data[0].id == "0001"
        assert result.data[0].sx == "规格"


class TestRcjYjflService:
    """测试人材机一级分类服务"""
    
    @pytest.fixture
    def mock_models(self):
        """模拟模型类"""
        with patch('app.services.dict_service.RcjYjfl') as mock_rcj_yjfl:
            yield {'RcjYjfl': mock_rcj_yjfl}
    
    def test_get_rcj_yjfls_success(self, mock_models):
        """测试获取人材机一级分类列表成功"""
        # 模拟分页对象
        mock_pagination = Mock()
        mock_pagination.page = 1
        mock_pagination.per_page = 10
        mock_pagination.total = 1
        mock_pagination.pages = 1
        mock_pagination.has_next = False
        mock_pagination.has_prev = False
        mock_pagination.items = [
            Mock(
                id="01",
                yjflmc="人工费",
                yjflms="人工相关费用",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
        ]
        
        mock_models['RcjYjfl'].query.paginate.return_value = mock_pagination
        mock_models['RcjYjfl'].query.filter_by.return_value.paginate.return_value = mock_pagination
        
        # 执行测试
        dict_service = DictService()
        result = dict_service.get_rcj_yjfls(page=1, per_page=10)
        
        # 验证结果
        assert isinstance(result, PaginatedResponse)
        assert len(result.data) == 1
        assert result.data[0].id == "01"
        assert result.data[0].yjflmc == "人工费"
        assert result.data[0].yjflms == "人工相关费用"


class TestRcjEjflService:
    """测试人材机二级分类服务"""
    
    @pytest.fixture
    def mock_models(self):
        """模拟模型类"""
        with patch('app.services.dict_service.RcjEjfl') as mock_rcj_ejfl, \
             patch('app.services.dict_service.RcjYjfl') as mock_rcj_yjfl:
            yield {
                'RcjEjfl': mock_rcj_ejfl,
                'RcjYjfl': mock_rcj_yjfl
            }
    
    def test_get_rcj_ejfls_with_yjfl_filter(self, mock_models):
        """测试获取人材机二级分类列表（带一级分类过滤）"""
        # 模拟分页对象
        mock_pagination = Mock()
        mock_pagination.page = 1
        mock_pagination.per_page = 10
        mock_pagination.total = 1
        mock_pagination.pages = 1
        mock_pagination.has_next = False
        mock_pagination.has_prev = False
        mock_pagination.items = [
            Mock(
                id="0101",
                yjfl_id="01",
                ejflmc="砌筑工",
                ejflms="砌筑相关工种",
                create_time=datetime.now(),
                update_time=datetime.now(),
                sxs=["规格", "尺寸"],
                dws=["个", "米"],
                yjfl=Mock(
                    id="01",
                    yjflmc="人工费",
                    yjflms="人工相关费用",
                    create_time=datetime.now(),
                    update_time=datetime.now()
                )
            )
        ]
        
        mock_models['RcjEjfl'].query.paginate.return_value = mock_pagination
        mock_models['RcjEjfl'].query.filter_by.return_value.paginate.return_value = mock_pagination
        
        # 执行测试
        dict_service = DictService()
        result = dict_service.get_rcj_ejfls(page=1, per_page=10, yjfl_id="01")
        
        # 验证结果
        assert isinstance(result, PaginatedResponse)
        assert len(result.data) == 1
        assert result.data[0].id == "0101"
        assert result.data[0].ejflmc == "砌筑工"
        assert result.data[0].yjfl_id == "01"
        assert result.data[0].sxs == ["规格", "尺寸"]
        assert result.data[0].dws == ["个", "米"]
        assert result.data[0].yjfl is not None
        assert result.data[0].yjfl.id == "01"


class TestRcjMC2EjflidService:
    """测试人材机名称映射服务"""
    
    @pytest.fixture
    def mock_models(self):
        """模拟模型类"""
        with patch('app.services.dict_service.RcjMC2Ejflid') as mock_rcj_mc2ejflid, \
             patch('app.services.dict_service.RcjEjfl') as mock_rcj_ejfl:
            yield {
                'RcjMC2Ejflid': mock_rcj_mc2ejflid,
                'RcjEjfl': mock_rcj_ejfl
            }
    
    def test_get_rcj_mc2ejflids_with_ejfl_filter(self, mock_models):
        """测试获取人材机名称映射列表（带二级分类过滤）"""
        # 模拟分页对象
        mock_pagination = Mock()
        mock_pagination.page = 1
        mock_pagination.per_page = 10
        mock_pagination.total = 1
        mock_pagination.pages = 1
        mock_pagination.has_next = False
        mock_pagination.has_prev = False
        mock_pagination.items = [
            Mock(
                id=1,
                ejflid="0101",
                orignal_rcjmc="砌筑工",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
        ]
        
        mock_models['RcjMC2Ejflid'].query.paginate.return_value = mock_pagination
        mock_models['RcjMC2Ejflid'].query.filter_by.return_value.paginate.return_value = mock_pagination
        
        # 执行测试
        dict_service = DictService()
        result = dict_service.get_rcj_mc2ejflids(page=1, per_page=10, ejflid="0101")
        
        # 验证结果
        assert isinstance(result, PaginatedResponse)
        assert len(result.data) == 1
        assert result.data[0].id == 1
        assert result.data[0].ejflid == "0101"
        assert result.data[0].orignal_rcjmc == "砌筑工"


class TestRcjMCClassifyService:
    """测试人材机名称分类服务"""
    
    @pytest.fixture
    def mock_models(self):
        """模拟模型类"""
        with patch('app.services.dict_service.RcjMCClassify') as mock_rcj_mc_classify, \
             patch('app.services.dict_service.RcjYjfl') as mock_rcj_yjfl, \
             patch('app.services.dict_service.RcjEjfl') as mock_rcj_ejfl:
            yield {
                'RcjMCClassify': mock_rcj_mc_classify,
                'RcjYjfl': mock_rcj_yjfl,
                'RcjEjfl': mock_rcj_ejfl
            }
    
    def test_get_rcj_mc_classifies_with_filters(self, mock_models):
        """测试获取人材机名称分类列表（带过滤条件）"""
        # 模拟分页对象
        mock_pagination = Mock()
        mock_pagination.page = 1
        mock_pagination.per_page = 10
        mock_pagination.total = 1
        mock_pagination.pages = 1
        mock_pagination.has_next = False
        mock_pagination.has_prev = False
        mock_pagination.items = [
            Mock(
                id=1,
                cleaned_rcj_original_mc="砌筑工",
                yjflid="01",
                yjflmc="人工费",
                ejflid="0101",
                ejflmc="砌筑工",
                create_time=datetime.now(),
                update_time=datetime.now()
            )
        ]
        
        mock_models['RcjMCClassify'].query.paginate.return_value = mock_pagination
        mock_models['RcjMCClassify'].query.filter_by.return_value.paginate.return_value = mock_pagination
        mock_models['RcjMCClassify'].query.filter_by.return_value.filter_by.return_value.paginate.return_value = mock_pagination
        
        # 执行测试
        dict_service = DictService()
        result = dict_service.get_rcj_mc_classifies(
            page=1, per_page=10, yjflid="01", ejflid="0101"
        )
        
        # 验证结果
        assert isinstance(result, PaginatedResponse)
        assert len(result.data) == 1
        assert result.data[0].id == 1
        assert result.data[0].cleaned_rcj_original_mc == "砌筑工"
        assert result.data[0].yjflid == "01"
        assert result.data[0].ejflid == "0101"


if __name__ == "__main__":
    pytest.main([__file__]) 