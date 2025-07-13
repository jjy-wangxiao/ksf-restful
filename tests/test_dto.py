"""
DTO测试文件
测试所有数据传输对象的创建和基本功能
"""
import pytest
from datetime import datetime
from app.dto.dict import (
    # 错误相关
    ErrorCode, ErrorResponse,
    # 分页相关
    PaginationMeta, PaginatedResponse,
    # 单位类别 DTO
    DwTypeRequestDTO, DwTypeUpdateRequestDTO, DwTypeResponseDTO, DwTypeInternalDTO,
    # 单位 DTO
    DwRequestDTO, DwUpdateRequestDTO, DwResponseDTO, DwInternalDTO,
    # 人材机二级分类属性 DTO
    RcjEjflSxRequestDTO, RcjEjflSxUpdateRequestDTO, RcjEjflSxResponseDTO, RcjEjflSxInternalDTO,
    # 人材机一级分类 DTO
    RcjYjflRequestDTO, RcjYjflUpdateRequestDTO, RcjYjflResponseDTO, RcjYjflInternalDTO,
    # 人材机二级分类 DTO
    RcjEjflRequestDTO, RcjEjflUpdateRequestDTO, RcjEjflResponseDTO, RcjEjflInternalDTO,
    # 人材机名称映射 DTO
    RcjMC2EjflidRequestDTO, RcjMC2EjflidUpdateRequestDTO, RcjMC2EjflidResponseDTO, RcjMC2EjflidInternalDTO,
    # 人材机名称分类 DTO
    RcjMCClassifyRequestDTO, RcjMCClassifyUpdateRequestDTO, RcjMCClassifyResponseDTO, RcjMCClassifyInternalDTO
)


class TestErrorCode:
    """测试错误码枚举"""
    
    def test_error_codes(self):
        """测试所有错误码"""
        assert ErrorCode.VALIDATION_ERROR.value == "VALIDATION_ERROR"
        assert ErrorCode.NOT_FOUND.value == "NOT_FOUND"
        assert ErrorCode.DUPLICATE_ENTRY.value == "DUPLICATE_ENTRY"
        assert ErrorCode.INTERNAL_ERROR.value == "INTERNAL_ERROR"
        assert ErrorCode.UNAUTHORIZED.value == "UNAUTHORIZED"
        assert ErrorCode.FORBIDDEN.value == "FORBIDDEN"


class TestErrorResponse:
    """测试错误响应DTO"""
    
    def test_error_response_creation(self):
        """测试错误响应创建"""
        error = ErrorResponse(
            code=ErrorCode.NOT_FOUND,
            message="资源未找到"
        )
        assert error.code == ErrorCode.NOT_FOUND
        assert error.message == "资源未找到"
        assert error.details is None
        assert error.timestamp is not None
    
    def test_error_response_with_details(self):
        """测试带详细信息的错误响应"""
        details = {"field": "id", "value": "123"}
        error = ErrorResponse(
            code=ErrorCode.VALIDATION_ERROR,
            message="验证失败",
            details=details
        )
        assert error.details == details


class TestPaginationMeta:
    """测试分页元数据DTO"""
    
    def test_pagination_meta_creation(self):
        """测试分页元数据创建"""
        meta = PaginationMeta(
            page=1,
            per_page=10,
            total=100,
            pages=10,
            has_next=True,
            has_prev=False
        )
        assert meta.page == 1
        assert meta.per_page == 10
        assert meta.total == 100
        assert meta.pages == 10
        assert meta.has_next is True
        assert meta.has_prev is False


class TestPaginatedResponse:
    """测试分页响应DTO"""
    
    def test_paginated_response_creation(self):
        """测试分页响应创建"""
        data = [{"id": 1}, {"id": 2}]
        meta = PaginationMeta(
            page=1,
            per_page=10,
            total=100,
            pages=10,
            has_next=True,
            has_prev=False
        )
        response = PaginatedResponse(data=data, meta=meta)
        assert response.data == data
        assert response.meta == meta


class TestDwTypeDTO:
    """测试单位类别DTO"""
    
    def test_dw_type_request_dto(self):
        """测试单位类别请求DTO"""
        dto = DwTypeRequestDTO(id="01", typeName="重量")
        assert dto.id == "01"
        assert dto.typeName == "重量"
    
    def test_dw_type_update_request_dto(self):
        """测试单位类别更新请求DTO"""
        dto = DwTypeUpdateRequestDTO(typeName="长度")
        assert dto.typeName == "长度"
    
    def test_dw_type_response_dto(self):
        """测试单位类别响应DTO"""
        now = datetime.now()
        dto = DwTypeResponseDTO(
            id="01",
            typeName="重量",
            create_time=now,
            update_time=now
        )
        assert dto.id == "01"
        assert dto.typeName == "重量"
        assert dto.create_time == now
        assert dto.update_time == now


class TestDwDTO:
    """测试单位DTO"""
    
    def test_dw_request_dto(self):
        """测试单位请求DTO"""
        dto = DwRequestDTO(id="0010", dw="个", type_id="01")
        assert dto.id == "0010"
        assert dto.dw == "个"
        assert dto.type_id == "01"
    
    def test_dw_request_dto_without_type(self):
        """测试单位请求DTO（无类别）"""
        dto = DwRequestDTO(id="0010", dw="个")
        assert dto.id == "0010"
        assert dto.dw == "个"
        assert dto.type_id is None
    
    def test_dw_update_request_dto(self):
        """测试单位更新请求DTO"""
        dto = DwUpdateRequestDTO(dw="米", type_id="02")
        assert dto.dw == "米"
        assert dto.type_id == "02"
    
    def test_dw_response_dto(self):
        """测试单位响应DTO"""
        now = datetime.now()
        dto = DwResponseDTO(
            id="0010",
            dw="个",
            type_id="01",
            create_time=now,
            update_time=now
        )
        assert dto.id == "0010"
        assert dto.dw == "个"
        assert dto.type_id == "01"
        assert dto.create_time == now
        assert dto.update_time == now


class TestRcjEjflSxDTO:
    """测试人材机二级分类属性DTO"""
    
    def test_rcj_ejfl_sx_request_dto(self):
        """测试人材机二级分类属性请求DTO"""
        dto = RcjEjflSxRequestDTO(id="0001", sx="规格")
        assert dto.id == "0001"
        assert dto.sx == "规格"
    
    def test_rcj_ejfl_sx_update_request_dto(self):
        """测试人材机二级分类属性更新请求DTO"""
        dto = RcjEjflSxUpdateRequestDTO(sx="尺寸")
        assert dto.sx == "尺寸"
    
    def test_rcj_ejfl_sx_response_dto(self):
        """测试人材机二级分类属性响应DTO"""
        now = datetime.now()
        dto = RcjEjflSxResponseDTO(
            id="0001",
            sx="规格",
            create_time=now,
            update_time=now
        )
        assert dto.id == "0001"
        assert dto.sx == "规格"
        assert dto.create_time == now
        assert dto.update_time == now


class TestRcjYjflDTO:
    """测试人材机一级分类DTO"""
    
    def test_rcj_yjfl_request_dto(self):
        """测试人材机一级分类请求DTO"""
        dto = RcjYjflRequestDTO(
            id="01",
            yjflmc="人工费",
            yjflms="人工相关费用"
        )
        assert dto.id == "01"
        assert dto.yjflmc == "人工费"
        assert dto.yjflms == "人工相关费用"
    
    def test_rcj_yjfl_update_request_dto(self):
        """测试人材机一级分类更新请求DTO"""
        dto = RcjYjflUpdateRequestDTO(
            yjflmc="材料费",
            yjflms="材料相关费用"
        )
        assert dto.yjflmc == "材料费"
        assert dto.yjflms == "材料相关费用"
    
    def test_rcj_yjfl_response_dto(self):
        """测试人材机一级分类响应DTO"""
        now = datetime.now()
        dto = RcjYjflResponseDTO(
            id="01",
            yjflmc="人工费",
            yjflms="人工相关费用",
            create_time=now,
            update_time=now
        )
        assert dto.id == "01"
        assert dto.yjflmc == "人工费"
        assert dto.yjflms == "人工相关费用"
        assert dto.create_time == now
        assert dto.update_time == now


class TestRcjEjflDTO:
    """测试人材机二级分类DTO"""
    
    def test_rcj_ejfl_request_dto(self):
        """测试人材机二级分类请求DTO"""
        dto = RcjEjflRequestDTO(
            id="0101",
            ejflmc="砌筑工",
            yjfl_id="01",
            ejflms="砌筑相关工种",
            sx_ids=["0001", "0002"],
            dw_ids=["0010", "0011"]
        )
        assert dto.id == "0101"
        assert dto.ejflmc == "砌筑工"
        assert dto.yjfl_id == "01"
        assert dto.ejflms == "砌筑相关工种"
        assert dto.sx_ids == ["0001", "0002"]
        assert dto.dw_ids == ["0010", "0011"]
    
    def test_rcj_ejfl_update_request_dto(self):
        """测试人材机二级分类更新请求DTO"""
        dto = RcjEjflUpdateRequestDTO(
            ejflmc="抹灰工",
            yjfl_id="01",
            ejflms="抹灰相关工种"
        )
        assert dto.ejflmc == "抹灰工"
        assert dto.yjfl_id == "01"
        assert dto.ejflms == "抹灰相关工种"
    
    def test_rcj_ejfl_response_dto(self):
        """测试人材机二级分类响应DTO"""
        now = datetime.now()
        dto = RcjEjflResponseDTO(
            id="0101",
            yjfl_id="01",
            ejflmc="砌筑工",
            ejflms="砌筑相关工种",
            create_time=now,
            update_time=now,
            sxs=["规格", "尺寸"],
            dws=["个", "米"]
        )
        assert dto.id == "0101"
        assert dto.yjfl_id == "01"
        assert dto.ejflmc == "砌筑工"
        assert dto.ejflms == "砌筑相关工种"
        assert dto.create_time == now
        assert dto.update_time == now
        assert dto.sxs == ["规格", "尺寸"]
        assert dto.dws == ["个", "米"]


class TestRcjMC2EjflidDTO:
    """测试人材机名称映射DTO"""
    
    def test_rcj_mc2ejflid_request_dto(self):
        """测试人材机名称映射请求DTO"""
        dto = RcjMC2EjflidRequestDTO(
            ejflid="0101",
            orignal_rcjmc="砌筑工"
        )
        assert dto.ejflid == "0101"
        assert dto.orignal_rcjmc == "砌筑工"
    
    def test_rcj_mc2ejflid_update_request_dto(self):
        """测试人材机名称映射更新请求DTO"""
        dto = RcjMC2EjflidUpdateRequestDTO(
            orignal_rcjmc="抹灰工",
            ejflid="0102"
        )
        assert dto.orignal_rcjmc == "抹灰工"
        assert dto.ejflid == "0102"
    
    def test_rcj_mc2ejflid_response_dto(self):
        """测试人材机名称映射响应DTO"""
        now = datetime.now()
        dto = RcjMC2EjflidResponseDTO(
            id=1,
            ejflid="0101",
            orignal_rcjmc="砌筑工",
            create_time=now,
            update_time=now
        )
        assert dto.id == 1
        assert dto.ejflid == "0101"
        assert dto.orignal_rcjmc == "砌筑工"
        assert dto.create_time == now
        assert dto.update_time == now


class TestRcjMCClassifyDTO:
    """测试人材机名称分类DTO"""
    
    def test_rcj_mc_classify_request_dto(self):
        """测试人材机名称分类请求DTO"""
        dto = RcjMCClassifyRequestDTO(
            cleaned_rcj_original_mc="砌筑工",
            yjflid="01",
            yjflmc="人工费",
            ejflid="0101",
            ejflmc="砌筑工"
        )
        assert dto.cleaned_rcj_original_mc == "砌筑工"
        assert dto.yjflid == "01"
        assert dto.yjflmc == "人工费"
        assert dto.ejflid == "0101"
        assert dto.ejflmc == "砌筑工"
    
    def test_rcj_mc_classify_update_request_dto(self):
        """测试人材机名称分类更新请求DTO"""
        dto = RcjMCClassifyUpdateRequestDTO(
            cleaned_rcj_original_mc="抹灰工",
            yjflid="01",
            yjflmc="人工费"
        )
        assert dto.cleaned_rcj_original_mc == "抹灰工"
        assert dto.yjflid == "01"
        assert dto.yjflmc == "人工费"
    
    def test_rcj_mc_classify_response_dto(self):
        """测试人材机名称分类响应DTO"""
        now = datetime.now()
        dto = RcjMCClassifyResponseDTO(
            id=1,
            cleaned_rcj_original_mc="砌筑工",
            yjflid="01",
            yjflmc="人工费",
            ejflid="0101",
            ejflmc="砌筑工",
            create_time=now,
            update_time=now
        )
        assert dto.id == 1
        assert dto.cleaned_rcj_original_mc == "砌筑工"
        assert dto.yjflid == "01"
        assert dto.yjflmc == "人工费"
        assert dto.ejflid == "0101"
        assert dto.ejflmc == "砌筑工"
        assert dto.create_time == now
        assert dto.update_time == now


if __name__ == "__main__":
    pytest.main([__file__]) 