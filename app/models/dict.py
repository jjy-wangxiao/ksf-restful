from app import db
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import Optional, List
from sqlalchemy.ext.associationproxy import association_proxy

class DwType(db.Model):
    __tablename__ = 'dict_dw_type'
    __table_args__ = (
        # Index('ix_dict_dw_type_id', 'id'),
        # Index('ix_dict_dw_type_typeName', 'typeName'),
        {'comment': '单位类别,定义单位所属类别，00为无类别，01为重量，02为长度，03为面积，04为体积，05为数量等'}
    )
    id: Mapped[str] = mapped_column(String(2), primary_key=True)
    typeName: Mapped[Optional[str]] = mapped_column(String(50),index=True,unique=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    dws: Mapped[Optional['Dw']] = relationship('Dw', back_populates='type')

    def __repr__(self):
        return f"<DwType(id={self.id}, typeName='{self.typeName}')>"

class Dw(db.Model):
    __tablename__ = 'dict_dw'
    __table_args__ = (
        # Index('ix_dict_dw_id', 'id'),
        # Index('ix_dict_dw_type_id', 'type_id'),
        {'comment': '单位,六位组成，前三位为单位id，后一位为id下十倍百倍等扩展位，比如0010为个，0011为十个。0000为无单位'}
    )

    id: Mapped[str] = mapped_column(String(4), primary_key=True)
    type_id: Mapped[Optional[str]] = mapped_column(ForeignKey('dict_dw_type.id'),index=True)
    dw: Mapped[Optional[str]] = mapped_column(String(50),unique=True,index=True)

    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    type: Mapped[Optional[List['DwType']]] = relationship('DwType', back_populates='dws')

    def __repr__(self):
        return f"<Dw(id={self.id}, dw='{self.dw}', type_id='{self.type_id}')>"

class RcjEjflSx(db.Model):
    __tablename__ = 'dict_rcjejflsx'
    __table_args__ = (
        {'comment': '用来描述人材机二级分类下的各种型号，规格，大小，尺寸等属性'}
    )

    # 四位数字字符串
    id: Mapped[str] = mapped_column(String(4), primary_key=True)
    sx: Mapped[Optional[str]] = mapped_column(String(100),unique=True,index=True)

    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    def __repr__(self):
        return f"<RcjEjflSx(id={self.id}, sx='{self.sx}')>"

class RcjYjfl(db.Model):
    __tablename__ = 'dict_rcjyjfl'
    __table_args__ = (
        {'comment': '用来描述人材机的一级分类ID及名称和描述'}
    )

    # 四位数字字符串，为rcj一级分类id,基本信息
    id: Mapped[str] = mapped_column(String(4), primary_key=True)
    yjflmc: Mapped[Optional[str]] = mapped_column(String(100),index=True,unique=True)
    yjflms: Mapped[Optional[str]] = mapped_column(String(1024))

    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    ejfls: Mapped[Optional[List['RcjEjfl']]] = relationship('RcjEjfl', back_populates='yjfl')

    def __repr__(self):
        return f"<RcjYjfl(id={self.id}, yjflmc='{self.yjflmc}', yjflms='{self.yjflms}')>"

# 分类与单位的关联表
ejfl_dw_association = Table(
    'association_ejfl_dw',
    db.metadata,
    Column('ejfl_id', String(4), ForeignKey('dict_rcjejfl.id'),index=True),
    Column('dwid', String(4), ForeignKey('dict_dw.id'),index=True),
    Column('create_time', DateTime, default=datetime.now, nullable=False),
    Column('update_time', DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
)

# 分类与属性的关联表
ejfl_sx_association = Table(
    'association_ejfl_sx',
    db.metadata,
    Column('ejfl_id', String(4), ForeignKey('dict_rcjejfl.id'),index=True),
    Column('sxid', String(4), ForeignKey('dict_rcjejflsx.id'),index=True),
    Column('create_time', DateTime, default=datetime.now, nullable=False),
    Column('update_time', DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
)


class RcjEjfl(db.Model):
    __tablename__ = 'dict_rcjejfl'
    __table_args__ = (
        {'comment': '用来描述人材机的二级分类ID及名称和描述'}
    )

    # 四位数字字符串，为rcj二级分类id,基本信息
    id: Mapped[str] = mapped_column(String(4), primary_key=True)
    yjfl_id: Mapped[Optional[str]] = mapped_column(String(2),ForeignKey('dict_rcjyjfl.id'),index=True)
    ejflmc: Mapped[Optional[str]] = mapped_column(String(100),index=True)
    ejflms: Mapped[Optional[str]] = mapped_column(String(1024))

    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    yjfl: Mapped[Optional['RcjYjfl']] = relationship('RcjYjfl', back_populates='ejfls')

    # 与属性的多对多关系
    _sxs = relationship(
        "RcjEjflSx",
        secondary=ejfl_sx_association,
        backref="rcjejfls"
    )

    # 与单位的多对多关系
    _dws = relationship(
        "Dw",
        secondary=ejfl_dw_association,
        backref="rcjejfls"
    )
    
    # 使用association_proxy简化访问
    sxs = association_proxy('_sxs', 'sx')
    dws = association_proxy('_dws', 'dw')
    sxids = association_proxy('_sxs', 'id')
    dwids = association_proxy('_dws', 'id')

    def __repr__(self):
        return f"<RcjEjfl(id={self.id}, ejflmc='{self.ejflmc}', sxs={self.sxs}, dws={self.dws})>"



class RcjMC2Ejflid(db.Model):
    __tablename__ = 'dict_rcjmc2ejflid'
    __table_args__ = (
        {'comment': '用来描述人材机名称到二级分类id的映射关系'}
    )

    # 四位数字字符串
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4),index=True)
    orignal_rcjmc: Mapped[Optional[str]] = mapped_column(String(300),index=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    def __repr__(self):
        return f"<RcjMC2Ejflid(id={self.id}, ejflid='{self.ejflid}', orignal_rcjmc='{self.orignal_rcjmc}')>"
    
class RcjMCClassify(db.Model):
    __tablename__ = 'dict_rcjmc_classify'
    __table_args__ = (
        {'comment': '用来存储大模型分析后的分类信息'}
    )

    # 四位数字字符串
    id: Mapped[Integer] = mapped_column(Integer, primary_key=True)
    cleaned_rcj_original_mc: Mapped[Optional[str]] = mapped_column(String(300),unique=True,index=True,comment='对原始人材机名称进行清洗后的名称')
    yjflid: Mapped[Optional[str]] = mapped_column(String(2),index=True,comment='一级分类id')
    yjflmc: Mapped[Optional[str]] = mapped_column(String(100),comment='一级分类名称')    
    ejflid: Mapped[Optional[str]] = mapped_column(String(4),index=True,comment='二级分类id')
    ejflmc: Mapped[Optional[str]] = mapped_column(String(100),index=True,comment='二级分类名称')
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    def __repr__(self):
        return f"<RcjMCClassify(id={self.id}, cleaned_rcj_original_mc='{self.cleaned_rcj_original_mc}', yjflid='{self.yjflid}', yjflmc='{self.yjflmc}', ejflid='{self.ejflid}', ejflmc='{self.ejflmc}')>"