"""
字典管理服务层
负责业务逻辑处理和数据模型与DTO之间的转换
"""
from typing import List, Optional, Dict, Any
from datetime import datetime
from app import db
from app.models.dict import (
    DwType, Dw, RcjEjflSx, RcjYjfl, RcjEjfl, 
    RcjMC2Ejflid, RcjMCClassify
)
from app.dto.dict import (
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
    RcjMCClassifyRequestDTO, RcjMCClassifyUpdateRequestDTO, RcjMCClassifyResponseDTO, RcjMCClassifyInternalDTO,
    # 通用 DTO
    PaginationMeta, PaginatedResponse
)
from app.services.base_service import BaseService


class DictService(BaseService):
    """字典管理服务类"""
    
    # ==================== 单位类别服务 ====================
    
    def get_dw_types(self, page: int = 1, per_page: int = 10) -> PaginatedResponse:
        """获取单位类别列表"""
        self.log_service_call("get_dw_types", page=page, per_page=per_page)
        
        try:
            pagination = DwType.query.paginate(
                page=page, per_page=per_page, error_out=False
            )
            
            # 转换为DTO
            dw_types_dto = [
                DwTypeResponseDTO(
                    id=dw_type.id,
                    typeName=dw_type.typeName,
                    create_time=dw_type.create_time,
                    update_time=dw_type.update_time
                )
                for dw_type in pagination.items
            ]
            
            meta = PaginationMeta(
                page=pagination.page,
                per_page=pagination.per_page,
                total=pagination.total,
                pages=pagination.pages,
                has_next=pagination.has_next,
                has_prev=pagination.has_prev
            )
            
            result = PaginatedResponse(data=dw_types_dto, meta=meta)
            self.log_service_result("get_dw_types", result, total_count=pagination.total)
            return result
            
        except Exception as e:
            self.log_error(e, {"method": "get_dw_types", "page": page, "per_page": per_page})
            raise
    
    def get_dw_type_by_id(self, type_id: str) -> Optional[DwTypeResponseDTO]:
        """根据ID获取单位类别"""
        self.log_service_call("get_dw_type_by_id", type_id=type_id)
        
        try:
            dw_type = DwType.query.get(type_id)
            if not dw_type:
                self.log_not_found("DwType", type_id)
                return None
                
            result = DwTypeResponseDTO(
                id=dw_type.id,
                typeName=dw_type.typeName,
                create_time=dw_type.create_time,
                update_time=dw_type.update_time
            )
            
            self.log_service_result("get_dw_type_by_id", result, type_id=type_id)
            return result
            
        except Exception as e:
            self.log_error(e, {"method": "get_dw_type_by_id", "type_id": type_id})
            raise
    
    def create_dw_type(self, dto: DwTypeRequestDTO) -> DwTypeResponseDTO:
        """创建单位类别"""
        self.log_service_call("create_dw_type", type_id=dto.id, type_name=dto.typeName)
        
        try:
            # 检查ID是否已存在
            if DwType.query.get(dto.id):
                self.log_duplicate_error("DwType", "id", dto.id)
                raise ValueError("单位类别ID已存在")
            
            # 检查名称是否已存在
            if DwType.query.filter_by(typeName=dto.typeName).first():
                self.log_duplicate_error("DwType", "typeName", dto.typeName)
                raise ValueError("单位类别名称已存在")
            
            # 创建实体
            dw_type = DwType(
                id=dto.id,
                typeName=dto.typeName
            )
            
            db.session.add(dw_type)
            db.session.commit()
            
            # 记录数据库操作
            self.log_database_operation("CREATE", "DwType", dto.id)
            
            # 返回响应DTO
            result = DwTypeResponseDTO(
                id=dw_type.id,
                typeName=dw_type.typeName,
                create_time=dw_type.create_time,
                update_time=dw_type.update_time
            )
            
            self.log_service_result("create_dw_type", result, type_id=dto.id)
            return result
            
        except Exception as e:
            self.log_error(e, {"method": "create_dw_type", "type_id": dto.id, "type_name": dto.typeName})
            raise
    
    def update_dw_type(self, type_id: str, dto: DwTypeUpdateRequestDTO) -> Optional[DwTypeResponseDTO]:
        """更新单位类别"""
        self.log_service_call("update_dw_type", type_id=type_id, type_name=dto.typeName)
        
        try:
            dw_type = DwType.query.get(type_id)
            if not dw_type:
                self.log_not_found("DwType", type_id)
                return None
            
            # 更新字段
            if dto.typeName is not None:
                # 检查名称是否已被其他记录使用
                existing = DwType.query.filter_by(typeName=dto.typeName).first()
                if existing and existing.id != type_id:
                    self.log_duplicate_error("DwType", "typeName", dto.typeName)
                    raise ValueError("单位类别名称已存在")
                dw_type.typeName = dto.typeName
            
            db.session.commit()
            
            # 记录数据库操作
            self.log_database_operation("UPDATE", "DwType", type_id)
            
            # 返回响应DTO
            result = DwTypeResponseDTO(
                id=dw_type.id,
                typeName=dw_type.typeName,
                create_time=dw_type.create_time,
                update_time=dw_type.update_time
            )
            
            self.log_service_result("update_dw_type", result, type_id=type_id)
            return result
            
        except Exception as e:
            self.log_error(e, {"method": "update_dw_type", "type_id": type_id, "type_name": dto.typeName})
            raise
    
    def delete_dw_type(self, type_id: str) -> bool:
        """删除单位类别"""
        self.log_service_call("delete_dw_type", type_id=type_id)
        
        try:
            dw_type = DwType.query.get(type_id)
            if not dw_type:
                self.log_not_found("DwType", type_id)
                return False
            
            db.session.delete(dw_type)
            db.session.commit()
            
            # 记录数据库操作
            self.log_database_operation("DELETE", "DwType", type_id)
            
            self.log_service_result("delete_dw_type", True, type_id=type_id)
            return True
            
        except Exception as e:
            self.log_error(e, {"method": "delete_dw_type", "type_id": type_id})
            raise
    
    # ==================== 单位服务 ====================
    
    def get_dws(self, page: int = 1, per_page: int = 10, type_id: Optional[str] = None) -> PaginatedResponse:
        """获取单位列表"""
        self.log_service_call("get_dws", page=page, per_page=per_page, type_id=type_id)
        
        try:
            query = Dw.query
            
            if type_id:
                query = query.filter_by(type_id=type_id)
            
            pagination = query.paginate(
                page=page, per_page=per_page, error_out=False
            )
            
            # 转换为DTO
            dws_dto = []
            for dw in pagination.items:
                dw_dto = DwResponseDTO(
                    id=dw.id,
                    type_id=dw.type_id,
                    dw=dw.dw,
                    create_time=dw.create_time,
                    update_time=dw.update_time
                )
                
                # 添加关联的类别信息
                if dw.type:
                    dw_dto.type = DwTypeResponseDTO(
                        id=dw.type.id,
                        typeName=dw.type.typeName,
                        create_time=dw.type.create_time,
                        update_time=dw.type.update_time
                    )
                
                dws_dto.append(dw_dto)
            
            meta = PaginationMeta(
                page=pagination.page,
                per_page=pagination.per_page,
                total=pagination.total,
                pages=pagination.pages,
                has_next=pagination.has_next,
                has_prev=pagination.has_prev
            )
            
            result = PaginatedResponse(data=dws_dto, meta=meta)
            self.log_service_result("get_dws", result, total_count=pagination.total)
            return result
            
        except Exception as e:
            self.log_error(e, {"method": "get_dws", "page": page, "per_page": per_page, "type_id": type_id})
            raise
    
    def get_dw_by_id(self, dw_id: str) -> Optional[DwResponseDTO]:
        """根据ID获取单位"""
        self.log_service_call("get_dw_by_id", dw_id=dw_id)
        
        try:
            dw = Dw.query.get(dw_id)
            if not dw:
                return None
            
            dw_dto = DwResponseDTO(
                id=dw.id,
                type_id=dw.type_id,
                dw=dw.dw,
                create_time=dw.create_time,
                update_time=dw.update_time
            )
            
            # 添加关联的类别信息
            if dw.type:
                dw_dto.type = DwTypeResponseDTO(
                    id=dw.type.id,
                    typeName=dw.type.typeName,
                    create_time=dw.type.create_time,
                    update_time=dw.type.update_time
                )
            
            return dw_dto
        except Exception as e:
            self.log_error(e, {"method": "get_dw_by_id", "dw_id": dw_id})
            raise

    def create_dw(self, dto: DwRequestDTO) -> DwResponseDTO:
        """创建单位"""
        self.log_service_call("create_dw", dw_id=dto.id, dw_name=dto.dw)
        
        try:
            # 检查ID是否已存在
            if Dw.query.get(dto.id):
                raise ValueError("单位ID已存在")
            
            # 检查名称是否已存在
            if Dw.query.filter_by(dw=dto.dw).first():
                raise ValueError("单位名称已存在")
            
            # 验证类别ID是否存在
            if dto.type_id and not DwType.query.get(dto.type_id):
                raise ValueError("指定的类别ID不存在")
            
            # 创建实体
            dw = Dw(
                id=dto.id,
                type_id=dto.type_id,
                dw=dto.dw
            )
            
            db.session.add(dw)
            db.session.commit()
            
            # 返回响应DTO
            return DwResponseDTO(
                id=dw.id,
                type_id=dw.type_id,
                dw=dw.dw,
                create_time=dw.create_time,
                update_time=dw.update_time
            )
        except Exception as e:
            self.log_error(e, {"method": "create_dw", "dw_id": dto.id, "dw_name": dto.dw})
            raise

    def update_dw(self, dw_id: str, dto: DwUpdateRequestDTO) -> Optional[DwResponseDTO]:
        """更新单位"""
        self.log_service_call("update_dw", dw_id=dw_id)
        
        try:
            dw = Dw.query.get(dw_id)
            if not dw:
                return None
            
            # 更新字段
            if dto.type_id is not None:
                # 验证类别ID是否存在
                if dto.type_id and not DwType.query.get(dto.type_id):
                    raise ValueError("指定的类别ID不存在")
                dw.type_id = dto.type_id
            
            if dto.dw is not None:
                # 检查名称是否已被其他记录使用
                existing = Dw.query.filter_by(dw=dto.dw).first()
                if existing and existing.id != dw_id:
                    raise ValueError("单位名称已存在")
                dw.dw = dto.dw
            
            db.session.commit()
            
            # 返回响应DTO
            return DwResponseDTO(
                id=dw.id,
                type_id=dw.type_id,
                dw=dw.dw,
                create_time=dw.create_time,
                update_time=dw.update_time
            )
        except Exception as e:
            self.log_error(e, {"method": "update_dw", "dw_id": dw_id})
            raise

    def delete_dw(self, dw_id: str) -> bool:
        """删除单位"""
        self.log_service_call("delete_dw", dw_id=dw_id)
        
        try:
            dw = Dw.query.get(dw_id)
            if not dw:
                return False
            
            db.session.delete(dw)
            db.session.commit()
            return True
        except Exception as e:
            self.log_error(e, {"method": "delete_dw", "dw_id": dw_id})
            raise
    
    # ==================== 人材机二级分类属性服务 ====================
    
    def get_rcj_ejfl_sxs(self, page: int = 1, per_page: int = 10) -> PaginatedResponse:
        """获取人材机二级分类属性列表"""
        pagination = RcjEjflSx.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        # 转换为DTO
        sxs_dto = [
            RcjEjflSxResponseDTO(
                id=sx.id,
                sx=sx.sx,
                create_time=sx.create_time,
                update_time=sx.update_time
            )
            for sx in pagination.items
        ]
        
        meta = PaginationMeta(
            page=pagination.page,
            per_page=pagination.per_page,
            total=pagination.total,
            pages=pagination.pages,
            has_next=pagination.has_next,
            has_prev=pagination.has_prev
        )
        
        return PaginatedResponse(data=sxs_dto, meta=meta)
    
    def get_rcj_ejfl_sx_by_id(self, sx_id: str) -> Optional[RcjEjflSxResponseDTO]:
        """根据ID获取人材机二级分类属性"""
        sx = RcjEjflSx.query.get(sx_id)
        if not sx:
            return None
            
        return RcjEjflSxResponseDTO(
            id=sx.id,
            sx=sx.sx,
            create_time=sx.create_time,
            update_time=sx.update_time
        )
    
    def create_rcj_ejfl_sx(self, dto: RcjEjflSxRequestDTO) -> RcjEjflSxResponseDTO:
        """创建人材机二级分类属性"""
        # 检查ID是否已存在
        if RcjEjflSx.query.get(dto.id):
            raise ValueError("属性ID已存在")
        
        # 检查名称是否已存在
        if RcjEjflSx.query.filter_by(sx=dto.sx).first():
            raise ValueError("属性名称已存在")
        
        # 创建实体
        sx = RcjEjflSx(
            id=dto.id,
            sx=dto.sx
        )
        
        db.session.add(sx)
        db.session.commit()
        
        # 返回响应DTO
        return RcjEjflSxResponseDTO(
            id=sx.id,
            sx=sx.sx,
            create_time=sx.create_time,
            update_time=sx.update_time
        )
    
    def update_rcj_ejfl_sx(self, sx_id: str, dto: RcjEjflSxUpdateRequestDTO) -> Optional[RcjEjflSxResponseDTO]:
        """更新人材机二级分类属性"""
        sx = RcjEjflSx.query.get(sx_id)
        if not sx:
            return None
        
        # 更新字段
        if dto.sx is not None:
            # 检查名称是否已被其他记录使用
            existing = RcjEjflSx.query.filter_by(sx=dto.sx).first()
            if existing and existing.id != sx_id:
                raise ValueError("属性名称已存在")
            sx.sx = dto.sx
        
        db.session.commit()
        
        # 返回响应DTO
        return RcjEjflSxResponseDTO(
            id=sx.id,
            sx=sx.sx,
            create_time=sx.create_time,
            update_time=sx.update_time
        )
    
    def delete_rcj_ejfl_sx(self, sx_id: str) -> bool:
        """删除人材机二级分类属性"""
        sx = RcjEjflSx.query.get(sx_id)
        if not sx:
            return False
        
        db.session.delete(sx)
        db.session.commit()
        return True
    
    # ==================== 人材机一级分类服务 ====================
    
    def get_rcj_yjfls(self, page: int = 1, per_page: int = 10) -> PaginatedResponse:
        """获取人材机一级分类列表"""
        pagination = RcjYjfl.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        # 转换为DTO
        yjfls_dto = [
            RcjYjflResponseDTO(
                id=yjfl.id,
                yjflmc=yjfl.yjflmc,
                yjflms=yjfl.yjflms,
                create_time=yjfl.create_time,
                update_time=yjfl.update_time
            )
            for yjfl in pagination.items
        ]
        
        meta = PaginationMeta(
            page=pagination.page,
            per_page=pagination.per_page,
            total=pagination.total,
            pages=pagination.pages,
            has_next=pagination.has_next,
            has_prev=pagination.has_prev
        )
        
        return PaginatedResponse(data=yjfls_dto, meta=meta)
    
    def get_rcj_yjfl_by_id(self, yjfl_id: str) -> Optional[RcjYjflResponseDTO]:
        """根据ID获取人材机一级分类"""
        yjfl = RcjYjfl.query.get(yjfl_id)
        if not yjfl:
            return None
            
        return RcjYjflResponseDTO(
            id=yjfl.id,
            yjflmc=yjfl.yjflmc,
            yjflms=yjfl.yjflms,
            create_time=yjfl.create_time,
            update_time=yjfl.update_time
        )
    
    def create_rcj_yjfl(self, dto: RcjYjflRequestDTO) -> RcjYjflResponseDTO:
        """创建人材机一级分类"""
        # 检查ID是否已存在
        if RcjYjfl.query.get(dto.id):
            raise ValueError("一级分类ID已存在")
        
        # 检查名称是否已存在
        if RcjYjfl.query.filter_by(yjflmc=dto.yjflmc).first():
            raise ValueError("一级分类名称已存在")
        
        # 创建实体
        yjfl = RcjYjfl(
            id=dto.id,
            yjflmc=dto.yjflmc,
            yjflms=dto.yjflms
        )
        
        db.session.add(yjfl)
        db.session.commit()
        
        # 返回响应DTO
        return RcjYjflResponseDTO(
            id=yjfl.id,
            yjflmc=yjfl.yjflmc,
            yjflms=yjfl.yjflms,
            create_time=yjfl.create_time,
            update_time=yjfl.update_time
        )
    
    def update_rcj_yjfl(self, yjfl_id: str, dto: RcjYjflUpdateRequestDTO) -> Optional[RcjYjflResponseDTO]:
        """更新人材机一级分类"""
        yjfl = RcjYjfl.query.get(yjfl_id)
        if not yjfl:
            return None
        
        # 更新字段
        if dto.yjflmc is not None:
            # 检查名称是否已被其他记录使用
            existing = RcjYjfl.query.filter_by(yjflmc=dto.yjflmc).first()
            if existing and existing.id != yjfl_id:
                raise ValueError("一级分类名称已存在")
            yjfl.yjflmc = dto.yjflmc
        
        if dto.yjflms is not None:
            yjfl.yjflms = dto.yjflms
        
        db.session.commit()
        
        # 返回响应DTO
        return RcjYjflResponseDTO(
            id=yjfl.id,
            yjflmc=yjfl.yjflmc,
            yjflms=yjfl.yjflms,
            create_time=yjfl.create_time,
            update_time=yjfl.update_time
        )
    
    def delete_rcj_yjfl(self, yjfl_id: str) -> bool:
        """删除人材机一级分类"""
        yjfl = RcjYjfl.query.get(yjfl_id)
        if not yjfl:
            return False
        
        db.session.delete(yjfl)
        db.session.commit()
        return True
    
    # ==================== 人材机二级分类服务 ====================
    
    def get_rcj_ejfls(self, page: int = 1, per_page: int = 10, yjfl_id: Optional[str] = None) -> PaginatedResponse:
        """获取人材机二级分类列表"""
        query = RcjEjfl.query
        
        if yjfl_id:
            query = query.filter_by(yjfl_id=yjfl_id)
        
        pagination = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        # 转换为DTO
        ejfls_dto = []
        for ejfl in pagination.items:
            ejfl_dto = RcjEjflResponseDTO(
                id=ejfl.id,
                yjfl_id=ejfl.yjfl_id,
                ejflmc=ejfl.ejflmc,
                ejflms=ejfl.ejflms,
                create_time=ejfl.create_time,
                update_time=ejfl.update_time,
                sxs=ejfl.sxs or [],
                dws=ejfl.dws or []
            )
            
            # 添加关联的一级分类信息
            if ejfl.yjfl:
                ejfl_dto.yjfl = RcjYjflResponseDTO(
                    id=ejfl.yjfl.id,
                    yjflmc=ejfl.yjfl.yjflmc,
                    yjflms=ejfl.yjfl.yjflms,
                    create_time=ejfl.yjfl.create_time,
                    update_time=ejfl.yjfl.update_time
                )
            
            ejfls_dto.append(ejfl_dto)
        
        meta = PaginationMeta(
            page=pagination.page,
            per_page=pagination.per_page,
            total=pagination.total,
            pages=pagination.pages,
            has_next=pagination.has_next,
            has_prev=pagination.has_prev
        )
        
        return PaginatedResponse(data=ejfls_dto, meta=meta)
    
    def get_rcj_ejfl_by_id(self, ejfl_id: str) -> Optional[RcjEjflResponseDTO]:
        """根据ID获取人材机二级分类"""
        ejfl = RcjEjfl.query.get(ejfl_id)
        if not ejfl:
            return None
        
        ejfl_dto = RcjEjflResponseDTO(
            id=ejfl.id,
            yjfl_id=ejfl.yjfl_id,
            ejflmc=ejfl.ejflmc,
            ejflms=ejfl.ejflms,
            create_time=ejfl.create_time,
            update_time=ejfl.update_time,
            sxs=ejfl.sxs or [],
            dws=ejfl.dws or []
        )
        
        # 添加关联的一级分类信息
        if ejfl.yjfl:
            ejfl_dto.yjfl = RcjYjflResponseDTO(
                id=ejfl.yjfl.id,
                yjflmc=ejfl.yjfl.yjflmc,
                yjflms=ejfl.yjfl.yjflms,
                create_time=ejfl.yjfl.create_time,
                update_time=ejfl.yjfl.update_time
            )
        
        return ejfl_dto
    
    def create_rcj_ejfl(self, dto: RcjEjflRequestDTO) -> RcjEjflResponseDTO:
        """创建人材机二级分类"""
        # 检查ID是否已存在
        if RcjEjfl.query.get(dto.id):
            raise ValueError("二级分类ID已存在")
        
        # 检查名称是否已存在
        if RcjEjfl.query.filter_by(ejflmc=dto.ejflmc).first():
            raise ValueError("二级分类名称已存在")
        
        # 验证一级分类ID是否存在
        if dto.yjfl_id and not RcjYjfl.query.get(dto.yjfl_id):
            raise ValueError("指定的一级分类ID不存在")
        
        # 创建实体
        ejfl = RcjEjfl(
            id=dto.id,
            yjfl_id=dto.yjfl_id,
            ejflmc=dto.ejflmc,
            ejflms=dto.ejflms
        )
        
        # 处理关联关系
        if dto.sx_ids:
            sxs = RcjEjflSx.query.filter(RcjEjflSx.id.in_(dto.sx_ids)).all()
            ejfl._sxs = sxs
        
        if dto.dw_ids:
            dws = Dw.query.filter(Dw.id.in_(dto.dw_ids)).all()
            ejfl._dws = dws
        
        db.session.add(ejfl)
        db.session.commit()
        
        # 返回响应DTO
        return RcjEjflResponseDTO(
            id=ejfl.id,
            yjfl_id=ejfl.yjfl_id,
            ejflmc=ejfl.ejflmc,
            ejflms=ejfl.ejflms,
            create_time=ejfl.create_time,
            update_time=ejfl.update_time,
            sxs=ejfl.sxs or [],
            dws=ejfl.dws or []
        )
    
    def update_rcj_ejfl(self, ejfl_id: str, dto: RcjEjflUpdateRequestDTO) -> Optional[RcjEjflResponseDTO]:
        """更新人材机二级分类"""
        ejfl = RcjEjfl.query.get(ejfl_id)
        if not ejfl:
            return None
        
        # 更新字段
        if dto.yjfl_id is not None:
            # 验证一级分类ID是否存在
            if dto.yjfl_id and not RcjYjfl.query.get(dto.yjfl_id):
                raise ValueError("指定的一级分类ID不存在")
            ejfl.yjfl_id = dto.yjfl_id
        
        if dto.ejflmc is not None:
            # 检查名称是否已被其他记录使用
            existing = RcjEjfl.query.filter_by(ejflmc=dto.ejflmc).first()
            if existing and existing.id != ejfl_id:
                raise ValueError("二级分类名称已存在")
            ejfl.ejflmc = dto.ejflmc
        
        if dto.ejflms is not None:
            ejfl.ejflms = dto.ejflms
        
        # 处理关联关系
        if dto.sx_ids is not None:
            sxs = RcjEjflSx.query.filter(RcjEjflSx.id.in_(dto.sx_ids)).all()
            ejfl._sxs = sxs
        
        if dto.dw_ids is not None:
            dws = Dw.query.filter(Dw.id.in_(dto.dw_ids)).all()
            ejfl._dws = dws
        
        db.session.commit()
        
        # 返回响应DTO
        return RcjEjflResponseDTO(
            id=ejfl.id,
            yjfl_id=ejfl.yjfl_id,
            ejflmc=ejfl.ejflmc,
            ejflms=ejfl.ejflms,
            create_time=ejfl.create_time,
            update_time=ejfl.update_time,
            sxs=ejfl.sxs or [],
            dws=ejfl.dws or []
        )
    
    def delete_rcj_ejfl(self, ejfl_id: str) -> bool:
        """删除人材机二级分类"""
        ejfl = RcjEjfl.query.get(ejfl_id)
        if not ejfl:
            return False
        
        db.session.delete(ejfl)
        db.session.commit()
        return True
    
    # ==================== 人材机名称映射服务 ====================
    
    def get_rcj_mc2ejflids(self, page: int = 1, per_page: int = 10, ejflid: Optional[str] = None) -> PaginatedResponse:
        """获取人材机名称映射列表"""
        query = RcjMC2Ejflid.query
        
        if ejflid:
            query = query.filter_by(ejflid=ejflid)
        
        pagination = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        # 转换为DTO
        mappings_dto = [
            RcjMC2EjflidResponseDTO(
                id=mapping.id,
                ejflid=mapping.ejflid,
                orignal_rcjmc=mapping.orignal_rcjmc,
                create_time=mapping.create_time,
                update_time=mapping.update_time
            )
            for mapping in pagination.items
        ]
        
        meta = PaginationMeta(
            page=pagination.page,
            per_page=pagination.per_page,
            total=pagination.total,
            pages=pagination.pages,
            has_next=pagination.has_next,
            has_prev=pagination.has_prev
        )
        
        return PaginatedResponse(data=mappings_dto, meta=meta)
    
    def get_rcj_mc2ejflid_by_id(self, mapping_id: int) -> Optional[RcjMC2EjflidResponseDTO]:
        """根据ID获取人材机名称映射"""
        mapping = RcjMC2Ejflid.query.get(mapping_id)
        if not mapping:
            return None
            
        return RcjMC2EjflidResponseDTO(
            id=mapping.id,
            ejflid=mapping.ejflid,
            orignal_rcjmc=mapping.orignal_rcjmc,
            create_time=mapping.create_time,
            update_time=mapping.update_time
        )
    
    def create_rcj_mc2ejflid(self, dto: RcjMC2EjflidRequestDTO) -> RcjMC2EjflidResponseDTO:
        """创建人材机名称映射"""
        # 验证二级分类ID是否存在
        if not RcjEjfl.query.get(dto.ejflid):
            raise ValueError("指定的二级分类ID不存在")
        
        # 检查名称是否已存在
        if RcjMC2Ejflid.query.filter_by(orignal_rcjmc=dto.orignal_rcjmc).first():
            raise ValueError("原始人材机名称已存在")
        
        # 创建实体
        mapping = RcjMC2Ejflid(
            ejflid=dto.ejflid,
            orignal_rcjmc=dto.orignal_rcjmc
        )
        
        db.session.add(mapping)
        db.session.commit()
        
        # 返回响应DTO
        return RcjMC2EjflidResponseDTO(
            id=mapping.id,
            ejflid=mapping.ejflid,
            orignal_rcjmc=mapping.orignal_rcjmc,
            create_time=mapping.create_time,
            update_time=mapping.update_time
        )
    
    def update_rcj_mc2ejflid(self, mapping_id: int, dto: RcjMC2EjflidUpdateRequestDTO) -> Optional[RcjMC2EjflidResponseDTO]:
        """更新人材机名称映射"""
        mapping = RcjMC2Ejflid.query.get(mapping_id)
        if not mapping:
            return None
        
        # 更新字段
        if dto.ejflid is not None:
            # 验证二级分类ID是否存在
            if not RcjEjfl.query.get(dto.ejflid):
                raise ValueError("指定的二级分类ID不存在")
            mapping.ejflid = dto.ejflid
        
        if dto.orignal_rcjmc is not None:
            # 检查名称是否已被其他记录使用
            existing = RcjMC2Ejflid.query.filter_by(orignal_rcjmc=dto.orignal_rcjmc).first()
            if existing and existing.id != mapping_id:
                raise ValueError("原始人材机名称已存在")
            mapping.orignal_rcjmc = dto.orignal_rcjmc
        
        db.session.commit()
        
        # 返回响应DTO
        return RcjMC2EjflidResponseDTO(
            id=mapping.id,
            ejflid=mapping.ejflid,
            orignal_rcjmc=mapping.orignal_rcjmc,
            create_time=mapping.create_time,
            update_time=mapping.update_time
        )
    
    def delete_rcj_mc2ejflid(self, mapping_id: int) -> bool:
        """删除人材机名称映射"""
        mapping = RcjMC2Ejflid.query.get(mapping_id)
        if not mapping:
            return False
        
        db.session.delete(mapping)
        db.session.commit()
        return True
    
    # ==================== 人材机名称分类服务 ====================
    
    def get_rcj_mc_classifies(self, page: int = 1, per_page: int = 10, 
                            yjflid: Optional[str] = None, ejflid: Optional[str] = None) -> PaginatedResponse:
        """获取人材机名称分类列表"""
        query = RcjMCClassify.query
        
        if yjflid:
            query = query.filter_by(yjflid=yjflid)
        
        if ejflid:
            query = query.filter_by(ejflid=ejflid)
        
        pagination = query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        # 转换为DTO
        classifies_dto = [
            RcjMCClassifyResponseDTO(
                id=classify.id,
                cleaned_rcj_original_mc=classify.cleaned_rcj_original_mc,
                yjflid=classify.yjflid,
                yjflmc=classify.yjflmc,
                ejflid=classify.ejflid,
                ejflmc=classify.ejflmc,
                create_time=classify.create_time,
                update_time=classify.update_time
            )
            for classify in pagination.items
        ]
        
        meta = PaginationMeta(
            page=pagination.page,
            per_page=pagination.per_page,
            total=pagination.total,
            pages=pagination.pages,
            has_next=pagination.has_next,
            has_prev=pagination.has_prev
        )
        
        return PaginatedResponse(data=classifies_dto, meta=meta)
    
    def get_rcj_mc_classify_by_id(self, classify_id: int) -> Optional[RcjMCClassifyResponseDTO]:
        """根据ID获取人材机名称分类"""
        classify = RcjMCClassify.query.get(classify_id)
        if not classify:
            return None
            
        return RcjMCClassifyResponseDTO(
            id=classify.id,
            cleaned_rcj_original_mc=classify.cleaned_rcj_original_mc,
            yjflid=classify.yjflid,
            yjflmc=classify.yjflmc,
            ejflid=classify.ejflid,
            ejflmc=classify.ejflmc,
            create_time=classify.create_time,
            update_time=classify.update_time
        )
    
    def create_rcj_mc_classify(self, dto: RcjMCClassifyRequestDTO) -> RcjMCClassifyResponseDTO:
        """创建人材机名称分类"""
        # 检查名称是否已存在
        if RcjMCClassify.query.filter_by(cleaned_rcj_original_mc=dto.cleaned_rcj_original_mc).first():
            raise ValueError("清洗后的人材机名称已存在")
        
        # 验证分类ID是否存在
        if dto.yjflid and not RcjYjfl.query.get(dto.yjflid):
            raise ValueError("指定的一级分类ID不存在")
        
        if dto.ejflid and not RcjEjfl.query.get(dto.ejflid):
            raise ValueError("指定的二级分类ID不存在")
        
        # 创建实体
        classify = RcjMCClassify(
            cleaned_rcj_original_mc=dto.cleaned_rcj_original_mc,
            yjflid=dto.yjflid,
            yjflmc=dto.yjflmc,
            ejflid=dto.ejflid,
            ejflmc=dto.ejflmc
        )
        
        db.session.add(classify)
        db.session.commit()
        
        # 返回响应DTO
        return RcjMCClassifyResponseDTO(
            id=classify.id,
            cleaned_rcj_original_mc=classify.cleaned_rcj_original_mc,
            yjflid=classify.yjflid,
            yjflmc=classify.yjflmc,
            ejflid=classify.ejflid,
            ejflmc=classify.ejflmc,
            create_time=classify.create_time,
            update_time=classify.update_time
        )
    
    def update_rcj_mc_classify(self, classify_id: int, dto: RcjMCClassifyUpdateRequestDTO) -> Optional[RcjMCClassifyResponseDTO]:
        """更新人材机名称分类"""
        classify = RcjMCClassify.query.get(classify_id)
        if not classify:
            return None
        
        # 更新字段
        if dto.cleaned_rcj_original_mc is not None:
            # 检查名称是否已被其他记录使用
            existing = RcjMCClassify.query.filter_by(cleaned_rcj_original_mc=dto.cleaned_rcj_original_mc).first()
            if existing and existing.id != classify_id:
                raise ValueError("清洗后的人材机名称已存在")
            classify.cleaned_rcj_original_mc = dto.cleaned_rcj_original_mc
        
        if dto.yjflid is not None:
            # 验证一级分类ID是否存在
            if dto.yjflid and not RcjYjfl.query.get(dto.yjflid):
                raise ValueError("指定的一级分类ID不存在")
            classify.yjflid = dto.yjflid
        
        if dto.yjflmc is not None:
            classify.yjflmc = dto.yjflmc
        
        if dto.ejflid is not None:
            # 验证二级分类ID是否存在
            if dto.ejflid and not RcjEjfl.query.get(dto.ejflid):
                raise ValueError("指定的二级分类ID不存在")
            classify.ejflid = dto.ejflid
        
        if dto.ejflmc is not None:
            classify.ejflmc = dto.ejflmc
        
        db.session.commit()
        
        # 返回响应DTO
        return RcjMCClassifyResponseDTO(
            id=classify.id,
            cleaned_rcj_original_mc=classify.cleaned_rcj_original_mc,
            yjflid=classify.yjflid,
            yjflmc=classify.yjflmc,
            ejflid=classify.ejflid,
            ejflmc=classify.ejflmc,
            create_time=classify.create_time,
            update_time=classify.update_time
        )
    
    def delete_rcj_mc_classify(self, classify_id: int) -> bool:
        """删除人材机名称分类"""
        classify = RcjMCClassify.query.get(classify_id)
        if not classify:
            return False
        
        db.session.delete(classify)
        db.session.commit()
        return True 