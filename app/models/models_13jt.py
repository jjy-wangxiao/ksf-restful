from typing import List, Optional

from sqlalchemy import DateTime, ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from datetime import datetime
from app import db




class File(db.Model):
    __tablename__ = 'origin_13jt_file'
    __table_args__ = (
        Index('ix_file_create_time', 'create_time'),
        Index('ix_file_filename', 'filename'),
        Index('ix_file_filesize', 'filesize'),
        Index('ix_file_filetype', 'filetype'),
        Index('ix_file_hash', 'hash'),
        Index('ix_file_id', 'id'),
        Index('ix_file_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    hash: Mapped[str] = mapped_column(String(100),unique=True,nullable=False)
    filename: Mapped[str] = mapped_column(String(100))
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    filesize: Mapped[Optional[int]] = mapped_column(Integer)
    filetype: Mapped[Optional[str]] = mapped_column(String(10))

    jingjibiao: Mapped[List['Jingjibiao']] = relationship('Jingjibiao', back_populates='file')
    dxgcxx: Mapped[List['Dxgcxx']] = relationship('Dxgcxx', back_populates='file')
    qtxinxi: Mapped[List['Qtxinxi']] = relationship('Qtxinxi', back_populates='file')
    toubiaoxx: Mapped[List['Toubiaoxx']] = relationship('Toubiaoxx', back_populates='file')
    dwgcxx: Mapped[List['Dwgcxx']] = relationship('Dwgcxx', back_populates='file')
    cbrgycl: Mapped[List['Cbrgycl']] = relationship('Cbrgycl', back_populates='file')
    clzg: Mapped[List['Clzg']] = relationship('Clzg', back_populates='file')
    csxm: Mapped[List['Csxm']] = relationship('Csxm', back_populates='file')
    fbrgycl: Mapped[List['Fbrgycl']] = relationship('Fbrgycl', back_populates='file')
    fywj: Mapped[List['Fywj']] = relationship('Fywj', back_populates='file')
    gfsj: Mapped[List['Gfsj']] = relationship('Gfsj', back_populates='file')
    jrg: Mapped[List['Jrg']] = relationship('Jrg', back_populates='file')
    qdxm: Mapped[List['Qdxm']] = relationship('Qdxm', back_populates='file')
    qtxm: Mapped[List['Qtxm']] = relationship('Qtxm', back_populates='file')
    rcjhz: Mapped[List['Rcjhz']] = relationship('Rcjhz', back_populates='file')
    zcbfwf: Mapped[List['Zcbfwf']] = relationship('Zcbfwf', back_populates='file')
    zjxmjdkzffj: Mapped[List['Zjxmjdkzffj']] = relationship('Zjxmjdkzffj', back_populates='file')
    zlje: Mapped[List['Zlje']] = relationship('Zlje', back_populates='file')
    zygczg: Mapped[List['Zygczg']] = relationship('Zygczg', back_populates='file')
    djcs: Mapped[List['Djcs']] = relationship('Djcs', back_populates='file')
    fywjmx: Mapped[List['Fywjmx']] = relationship('Fywjmx', back_populates='file')
    gfsjmx: Mapped[List['Gfsjmx']] = relationship('Gfsjmx', back_populates='file')
    jrgbt: Mapped[List['Jrgbt']] = relationship('Jrgbt', back_populates='file')
    qdbt: Mapped[List['Qdbt']] = relationship('Qdbt', back_populates='file')
    qtxmmx: Mapped[List['Qtxmmx']] = relationship('Qtxmmx', back_populates='file')
    rcjhzmx: Mapped[List['Rcjhzmx']] = relationship('Rcjhzmx', back_populates='file')
    zjcs: Mapped[List['Zjcs']] = relationship('Zjcs', back_populates='file')
    zjxmjdkzffjmx: Mapped[List['Zjxmjdkzffjmx']] = relationship('Zjxmjdkzffjmx', back_populates='file')
    zljemx: Mapped[List['Zljemx']] = relationship('Zljemx', back_populates='file')
    djcsmx: Mapped[List['Djcsmx']] = relationship('Djcsmx', back_populates='file')
    qdmx: Mapped[List['Qdmx']] = relationship('Qdmx', back_populates='file')
    zfmx: Mapped[List['Zfmx']] = relationship('Zfmx', back_populates='file')
    zjcsmx: Mapped[List['Zjcsmx']] = relationship('Zjcsmx', back_populates='file')
    aqwmfmx: Mapped[List['Aqwmfmx']] = relationship('Aqwmfmx', back_populates='file')
    csxdezj: Mapped[List['Csxdezj']] = relationship('Csxdezj', back_populates='file')
    csxrcjhl: Mapped[List['Csxrcjhl']] = relationship('Csxrcjhl', back_populates='file')
    qdxdezj: Mapped[List['Qdxdezj']] = relationship('Qdxdezj', back_populates='file')
    qdxrcjhl: Mapped[List['Qdxrcjhl']] = relationship('Qdxrcjhl', back_populates='file')
    csxdezjmx: Mapped[List['Csxdezjmx']] = relationship('Csxdezjmx', back_populates='file')
    csxrcjhlmx: Mapped[List['Csxrcjhlmx']] = relationship('Csxrcjhlmx', back_populates='file')
    qdxdezjmx: Mapped[List['Qdxdezjmx']] = relationship('Qdxdezjmx', back_populates='file')
    qdxrcjhlmx: Mapped[List['Qdxrcjhlmx']] = relationship('Qdxrcjhlmx', back_populates='file')
    csxdercjhl: Mapped[List['Csxdercjhl']] = relationship('Csxdercjhl', back_populates='file')
    qdxdercjhl: Mapped[List['Qdxdercjhl']] = relationship('Qdxdercjhl', back_populates='file')
    csxdercjhlmx: Mapped[List['Csxdercjhlmx']] = relationship('Csxdercjhlmx', back_populates='file')
    qdxdercjhlmx: Mapped[List['Qdxdercjhlmx']] = relationship('Qdxdercjhlmx', back_populates='file')


class Jingjibiao(db.Model):
    __tablename__ = 'origin_13jt_jingjibiao'
    __table_args__ = (
        Index('ix_jingjibiao_create_time', 'create_time'),
        Index('ix_jingjibiao_file_id', 'file_id'),
        Index('ix_jingjibiao_id', 'id'),
        Index('ix_jingjibiao_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    biaoduanno: Mapped[Optional[str]] = mapped_column(String(100))
    xmmc: Mapped[Optional[str]] = mapped_column(String(100))
    jsfs: Mapped[Optional[str]] = mapped_column(String(100))
    version: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))

    file: Mapped[Optional['File']] = relationship('File', back_populates='jingjibiao')
    dxgcxx: Mapped[List['Dxgcxx']] = relationship('Dxgcxx', back_populates='jingjibiao')
    qtxinxi: Mapped[List['Qtxinxi']] = relationship('Qtxinxi', back_populates='jingjibiao')
    toubiaoxx: Mapped[List['Toubiaoxx']] = relationship('Toubiaoxx', back_populates='jingjibiao')
    dwgcxx: Mapped[List['Dwgcxx']] = relationship('Dwgcxx', back_populates='jingjibiao')
    cbrgycl: Mapped[List['Cbrgycl']] = relationship('Cbrgycl', back_populates='jingjibiao')
    clzg: Mapped[List['Clzg']] = relationship('Clzg', back_populates='jingjibiao')
    csxm: Mapped[List['Csxm']] = relationship('Csxm', back_populates='jingjibiao')
    fbrgycl: Mapped[List['Fbrgycl']] = relationship('Fbrgycl', back_populates='jingjibiao')
    fywj: Mapped[List['Fywj']] = relationship('Fywj', back_populates='jingjibiao')
    gfsj: Mapped[List['Gfsj']] = relationship('Gfsj', back_populates='jingjibiao')
    jrg: Mapped[List['Jrg']] = relationship('Jrg', back_populates='jingjibiao')
    qdxm: Mapped[List['Qdxm']] = relationship('Qdxm', back_populates='jingjibiao')
    qtxm: Mapped[List['Qtxm']] = relationship('Qtxm', back_populates='jingjibiao')
    rcjhz: Mapped[List['Rcjhz']] = relationship('Rcjhz', back_populates='jingjibiao')
    zcbfwf: Mapped[List['Zcbfwf']] = relationship('Zcbfwf', back_populates='jingjibiao')
    zjxmjdkzffj: Mapped[List['Zjxmjdkzffj']] = relationship('Zjxmjdkzffj', back_populates='jingjibiao')
    zlje: Mapped[List['Zlje']] = relationship('Zlje', back_populates='jingjibiao')
    zygczg: Mapped[List['Zygczg']] = relationship('Zygczg', back_populates='jingjibiao')
    djcs: Mapped[List['Djcs']] = relationship('Djcs', back_populates='jingjibiao')
    fywjmx: Mapped[List['Fywjmx']] = relationship('Fywjmx', back_populates='jingjibiao')
    gfsjmx: Mapped[List['Gfsjmx']] = relationship('Gfsjmx', back_populates='jingjibiao')
    jrgbt: Mapped[List['Jrgbt']] = relationship('Jrgbt', back_populates='jingjibiao')
    qdbt: Mapped[List['Qdbt']] = relationship('Qdbt', back_populates='jingjibiao')
    qtxmmx: Mapped[List['Qtxmmx']] = relationship('Qtxmmx', back_populates='jingjibiao')
    rcjhzmx: Mapped[List['Rcjhzmx']] = relationship('Rcjhzmx', back_populates='jingjibiao')
    zjcs: Mapped[List['Zjcs']] = relationship('Zjcs', back_populates='jingjibiao')
    zjxmjdkzffjmx: Mapped[List['Zjxmjdkzffjmx']] = relationship('Zjxmjdkzffjmx', back_populates='jingjibiao')
    zljemx: Mapped[List['Zljemx']] = relationship('Zljemx', back_populates='jingjibiao')
    djcsmx: Mapped[List['Djcsmx']] = relationship('Djcsmx', back_populates='jingjibiao')
    qdmx: Mapped[List['Qdmx']] = relationship('Qdmx', back_populates='jingjibiao')
    zfmx: Mapped[List['Zfmx']] = relationship('Zfmx', back_populates='jingjibiao')
    zjcsmx: Mapped[List['Zjcsmx']] = relationship('Zjcsmx', back_populates='jingjibiao')
    aqwmfmx: Mapped[List['Aqwmfmx']] = relationship('Aqwmfmx', back_populates='jingjibiao')
    csxdezj: Mapped[List['Csxdezj']] = relationship('Csxdezj', back_populates='jingjibiao')
    csxrcjhl: Mapped[List['Csxrcjhl']] = relationship('Csxrcjhl', back_populates='jingjibiao')
    qdxdezj: Mapped[List['Qdxdezj']] = relationship('Qdxdezj', back_populates='jingjibiao')
    qdxrcjhl: Mapped[List['Qdxrcjhl']] = relationship('Qdxrcjhl', back_populates='jingjibiao')
    csxdezjmx: Mapped[List['Csxdezjmx']] = relationship('Csxdezjmx', back_populates='jingjibiao')
    csxrcjhlmx: Mapped[List['Csxrcjhlmx']] = relationship('Csxrcjhlmx', back_populates='jingjibiao')
    qdxdezjmx: Mapped[List['Qdxdezjmx']] = relationship('Qdxdezjmx', back_populates='jingjibiao')
    qdxrcjhlmx: Mapped[List['Qdxrcjhlmx']] = relationship('Qdxrcjhlmx', back_populates='jingjibiao')
    csxdercjhl: Mapped[List['Csxdercjhl']] = relationship('Csxdercjhl', back_populates='jingjibiao')
    qdxdercjhl: Mapped[List['Qdxdercjhl']] = relationship('Qdxdercjhl', back_populates='jingjibiao')
    csxdercjhlmx: Mapped[List['Csxdercjhlmx']] = relationship('Csxdercjhlmx', back_populates='jingjibiao')
    qdxdercjhlmx: Mapped[List['Qdxdercjhlmx']] = relationship('Qdxdercjhlmx', back_populates='jingjibiao')


class Dxgcxx(db.Model):
    __tablename__ = 'origin_13jt_dxgcxx'
    __table_args__ = (
        Index('ix_dxgcxx_create_time', 'create_time'),
        Index('ix_dxgcxx_file_id', 'file_id'),
        Index('ix_dxgcxx_id', 'id'),
        Index('ix_dxgcxx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_dxgcxx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    dxgcmc: Mapped[Optional[str]] = mapped_column(String(100))
    dxgcbh: Mapped[Optional[str]] = mapped_column(String(100))
    je: Mapped[Optional[str]] = mapped_column(String(100))
    zgj: Mapped[Optional[str]] = mapped_column(String(100))
    aqwmf: Mapped[Optional[str]] = mapped_column(String(100))
    gf: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))

    file: Mapped[Optional['File']] = relationship('File', back_populates='dxgcxx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='dxgcxx')
    dwgcxx: Mapped[List['Dwgcxx']] = relationship('Dwgcxx', back_populates='dxgcxx')
    cbrgycl: Mapped[List['Cbrgycl']] = relationship('Cbrgycl', back_populates='dxgcxx')
    clzg: Mapped[List['Clzg']] = relationship('Clzg', back_populates='dxgcxx')
    csxm: Mapped[List['Csxm']] = relationship('Csxm', back_populates='dxgcxx')
    fbrgycl: Mapped[List['Fbrgycl']] = relationship('Fbrgycl', back_populates='dxgcxx')
    fywj: Mapped[List['Fywj']] = relationship('Fywj', back_populates='dxgcxx')
    gfsj: Mapped[List['Gfsj']] = relationship('Gfsj', back_populates='dxgcxx')
    jrg: Mapped[List['Jrg']] = relationship('Jrg', back_populates='dxgcxx')
    qdxm: Mapped[List['Qdxm']] = relationship('Qdxm', back_populates='dxgcxx')
    qtxm: Mapped[List['Qtxm']] = relationship('Qtxm', back_populates='dxgcxx')
    rcjhz: Mapped[List['Rcjhz']] = relationship('Rcjhz', back_populates='dxgcxx')
    zcbfwf: Mapped[List['Zcbfwf']] = relationship('Zcbfwf', back_populates='dxgcxx')
    zjxmjdkzffj: Mapped[List['Zjxmjdkzffj']] = relationship('Zjxmjdkzffj', back_populates='dxgcxx')
    zlje: Mapped[List['Zlje']] = relationship('Zlje', back_populates='dxgcxx')
    zygczg: Mapped[List['Zygczg']] = relationship('Zygczg', back_populates='dxgcxx')
    djcs: Mapped[List['Djcs']] = relationship('Djcs', back_populates='dxgcxx')
    fywjmx: Mapped[List['Fywjmx']] = relationship('Fywjmx', back_populates='dxgcxx')
    gfsjmx: Mapped[List['Gfsjmx']] = relationship('Gfsjmx', back_populates='dxgcxx')
    jrgbt: Mapped[List['Jrgbt']] = relationship('Jrgbt', back_populates='dxgcxx')
    qdbt: Mapped[List['Qdbt']] = relationship('Qdbt', back_populates='dxgcxx')
    qtxmmx: Mapped[List['Qtxmmx']] = relationship('Qtxmmx', back_populates='dxgcxx')
    rcjhzmx: Mapped[List['Rcjhzmx']] = relationship('Rcjhzmx', back_populates='dxgcxx')
    zjcs: Mapped[List['Zjcs']] = relationship('Zjcs', back_populates='dxgcxx')
    zjxmjdkzffjmx: Mapped[List['Zjxmjdkzffjmx']] = relationship('Zjxmjdkzffjmx', back_populates='dxgcxx')
    zljemx: Mapped[List['Zljemx']] = relationship('Zljemx', back_populates='dxgcxx')
    djcsmx: Mapped[List['Djcsmx']] = relationship('Djcsmx', back_populates='dxgcxx')
    qdmx: Mapped[List['Qdmx']] = relationship('Qdmx', back_populates='dxgcxx')
    zfmx: Mapped[List['Zfmx']] = relationship('Zfmx', back_populates='dxgcxx')
    zjcsmx: Mapped[List['Zjcsmx']] = relationship('Zjcsmx', back_populates='dxgcxx')
    aqwmfmx: Mapped[List['Aqwmfmx']] = relationship('Aqwmfmx', back_populates='dxgcxx')
    csxdezj: Mapped[List['Csxdezj']] = relationship('Csxdezj', back_populates='dxgcxx')
    csxrcjhl: Mapped[List['Csxrcjhl']] = relationship('Csxrcjhl', back_populates='dxgcxx')
    qdxdezj: Mapped[List['Qdxdezj']] = relationship('Qdxdezj', back_populates='dxgcxx')
    qdxrcjhl: Mapped[List['Qdxrcjhl']] = relationship('Qdxrcjhl', back_populates='dxgcxx')
    csxdezjmx: Mapped[List['Csxdezjmx']] = relationship('Csxdezjmx', back_populates='dxgcxx')
    csxrcjhlmx: Mapped[List['Csxrcjhlmx']] = relationship('Csxrcjhlmx', back_populates='dxgcxx')
    qdxdezjmx: Mapped[List['Qdxdezjmx']] = relationship('Qdxdezjmx', back_populates='dxgcxx')
    qdxrcjhlmx: Mapped[List['Qdxrcjhlmx']] = relationship('Qdxrcjhlmx', back_populates='dxgcxx')
    csxdercjhl: Mapped[List['Csxdercjhl']] = relationship('Csxdercjhl', back_populates='dxgcxx')
    qdxdercjhl: Mapped[List['Qdxdercjhl']] = relationship('Qdxdercjhl', back_populates='dxgcxx')
    csxdercjhlmx: Mapped[List['Csxdercjhlmx']] = relationship('Csxdercjhlmx', back_populates='dxgcxx')
    qdxdercjhlmx: Mapped[List['Qdxdercjhlmx']] = relationship('Qdxdercjhlmx', back_populates='dxgcxx')


class Qtxinxi(db.Model):
    __tablename__ = 'origin_13jt_qtxinxi'
    __table_args__ = (
        Index('ix_qtxinxi_create_time', 'create_time'),
        Index('ix_qtxinxi_file_id', 'file_id'),
        Index('ix_qtxinxi_id', 'id'),
        Index('ix_qtxinxi_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qtxinxi_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))

    file: Mapped[Optional['File']] = relationship('File', back_populates='qtxinxi')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qtxinxi')


class Toubiaoxx(db.Model):
    __tablename__ = 'origin_13jt_toubiaoxx'
    __table_args__ = (
        Index('ix_toubiaoxx_create_time', 'create_time'),
        Index('ix_toubiaoxx_file_id', 'file_id'),
        Index('ix_toubiaoxx_id', 'id'),
        Index('ix_toubiaoxx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_toubiaoxx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    zbr: Mapped[Optional[str]] = mapped_column(String(100))
    tbr: Mapped[Optional[str]] = mapped_column(String(100))
    tbrdb: Mapped[Optional[str]] = mapped_column(String(100))
    bzr: Mapped[Optional[str]] = mapped_column(String(100))
    bztime: Mapped[Optional[str]] = mapped_column(String(100))
    tbzj: Mapped[Optional[str]] = mapped_column(String(100))
    zgj: Mapped[Optional[str]] = mapped_column(String(100))
    aqwmf: Mapped[Optional[str]] = mapped_column(String(100))
    gf: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))

    file: Mapped[Optional['File']] = relationship('File', back_populates='toubiaoxx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='toubiaoxx')


class Dwgcxx(db.Model):
    __tablename__ = 'origin_13jt_dwgcxx'
    __table_args__ = (
        Index('ix_dwgcxx_create_time', 'create_time'),
        Index('ix_dwgcxx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_dwgcxx_file_id', 'file_id'),
        Index('ix_dwgcxx_id', 'id'),
        Index('ix_dwgcxx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_dwgcxx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    dwgcbh: Mapped[Optional[str]] = mapped_column(String(100))
    dwgcmc: Mapped[Optional[str]] = mapped_column(String(100))
    zylb: Mapped[Optional[str]] = mapped_column(String(100))
    softname: Mapped[Optional[str]] = mapped_column(String(100))
    softnum: Mapped[Optional[str]] = mapped_column(String(100))
    dognum: Mapped[Optional[str]] = mapped_column(String(100))
    machinekey: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))

    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='dwgcxx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='dwgcxx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='dwgcxx')
    cbrgycl: Mapped[List['Cbrgycl']] = relationship('Cbrgycl', back_populates='dwgcxx')
    clzg: Mapped[List['Clzg']] = relationship('Clzg', back_populates='dwgcxx')
    csxm: Mapped[List['Csxm']] = relationship('Csxm', back_populates='dwgcxx')
    fbrgycl: Mapped[List['Fbrgycl']] = relationship('Fbrgycl', back_populates='dwgcxx')
    fywj: Mapped[List['Fywj']] = relationship('Fywj', back_populates='dwgcxx')
    gfsj: Mapped[List['Gfsj']] = relationship('Gfsj', back_populates='dwgcxx')
    jrg: Mapped[List['Jrg']] = relationship('Jrg', back_populates='dwgcxx')
    qdxm: Mapped[List['Qdxm']] = relationship('Qdxm', back_populates='dwgcxx')
    qtxm: Mapped[List['Qtxm']] = relationship('Qtxm', back_populates='dwgcxx')
    rcjhz: Mapped[List['Rcjhz']] = relationship('Rcjhz', back_populates='dwgcxx')
    zcbfwf: Mapped[List['Zcbfwf']] = relationship('Zcbfwf', back_populates='dwgcxx')
    zjxmjdkzffj: Mapped[List['Zjxmjdkzffj']] = relationship('Zjxmjdkzffj', back_populates='dwgcxx')
    zlje: Mapped[List['Zlje']] = relationship('Zlje', back_populates='dwgcxx')
    zygczg: Mapped[List['Zygczg']] = relationship('Zygczg', back_populates='dwgcxx')
    djcs: Mapped[List['Djcs']] = relationship('Djcs', back_populates='dwgcxx')
    fywjmx: Mapped[List['Fywjmx']] = relationship('Fywjmx', back_populates='dwgcxx')
    gfsjmx: Mapped[List['Gfsjmx']] = relationship('Gfsjmx', back_populates='dwgcxx')
    jrgbt: Mapped[List['Jrgbt']] = relationship('Jrgbt', back_populates='dwgcxx')
    qdbt: Mapped[List['Qdbt']] = relationship('Qdbt', back_populates='dwgcxx')
    qtxmmx: Mapped[List['Qtxmmx']] = relationship('Qtxmmx', back_populates='dwgcxx')
    rcjhzmx: Mapped[List['Rcjhzmx']] = relationship('Rcjhzmx', back_populates='dwgcxx')
    zjcs: Mapped[List['Zjcs']] = relationship('Zjcs', back_populates='dwgcxx')
    zjxmjdkzffjmx: Mapped[List['Zjxmjdkzffjmx']] = relationship('Zjxmjdkzffjmx', back_populates='dwgcxx')
    zljemx: Mapped[List['Zljemx']] = relationship('Zljemx', back_populates='dwgcxx')
    djcsmx: Mapped[List['Djcsmx']] = relationship('Djcsmx', back_populates='dwgcxx')
    qdmx: Mapped[List['Qdmx']] = relationship('Qdmx', back_populates='dwgcxx')
    zfmx: Mapped[List['Zfmx']] = relationship('Zfmx', back_populates='dwgcxx')
    zjcsmx: Mapped[List['Zjcsmx']] = relationship('Zjcsmx', back_populates='dwgcxx')
    aqwmfmx: Mapped[List['Aqwmfmx']] = relationship('Aqwmfmx', back_populates='dwgcxx')
    csxdezj: Mapped[List['Csxdezj']] = relationship('Csxdezj', back_populates='dwgcxx')
    csxrcjhl: Mapped[List['Csxrcjhl']] = relationship('Csxrcjhl', back_populates='dwgcxx')
    qdxdezj: Mapped[List['Qdxdezj']] = relationship('Qdxdezj', back_populates='dwgcxx')
    qdxrcjhl: Mapped[List['Qdxrcjhl']] = relationship('Qdxrcjhl', back_populates='dwgcxx')
    csxdezjmx: Mapped[List['Csxdezjmx']] = relationship('Csxdezjmx', back_populates='dwgcxx')
    csxrcjhlmx: Mapped[List['Csxrcjhlmx']] = relationship('Csxrcjhlmx', back_populates='dwgcxx')
    qdxdezjmx: Mapped[List['Qdxdezjmx']] = relationship('Qdxdezjmx', back_populates='dwgcxx')
    qdxrcjhlmx: Mapped[List['Qdxrcjhlmx']] = relationship('Qdxrcjhlmx', back_populates='dwgcxx')
    csxdercjhl: Mapped[List['Csxdercjhl']] = relationship('Csxdercjhl', back_populates='dwgcxx')
    qdxdercjhl: Mapped[List['Qdxdercjhl']] = relationship('Qdxdercjhl', back_populates='dwgcxx')
    csxdercjhlmx: Mapped[List['Csxdercjhlmx']] = relationship('Csxdercjhlmx', back_populates='dwgcxx')
    qdxdercjhlmx: Mapped[List['Qdxdercjhlmx']] = relationship('Qdxdercjhlmx', back_populates='dwgcxx')


class Cbrgycl(db.Model):
    __tablename__ = 'origin_13jt_cbrgycl'
    __table_args__ = (
        Index('ix_cbrgycl_create_time', 'create_time'),
        Index('ix_cbrgycl_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_cbrgycl_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_cbrgycl_file_id', 'file_id'),
        Index('ix_cbrgycl_id', 'id'),
        Index('ix_cbrgycl_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_cbrgycl_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='cbrgycl')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='cbrgycl')
    file: Mapped[Optional['File']] = relationship('File', back_populates='cbrgycl')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='cbrgycl')


class Clzg(db.Model):
    __tablename__ = 'origin_13jt_clzg'
    __table_args__ = (
        Index('ix_clzg_create_time', 'create_time'),
        Index('ix_clzg_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_clzg_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_clzg_file_id', 'file_id'),
        Index('ix_clzg_id', 'id'),
        Index('ix_clzg_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_clzg_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='clzg')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='clzg')
    file: Mapped[Optional['File']] = relationship('File', back_populates='clzg')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='clzg')


class Csxm(db.Model):
    __tablename__ = 'origin_13jt_csxm'
    __table_args__ = (
        Index('ix_csxm_create_time', 'create_time'),
        Index('ix_csxm_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_csxm_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_csxm_file_id', 'file_id'),
        Index('ix_csxm_id', 'id'),
        Index('ix_csxm_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_csxm_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='csxm')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='csxm')
    file: Mapped[Optional['File']] = relationship('File', back_populates='csxm')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='csxm')
    djcs: Mapped[List['Djcs']] = relationship('Djcs', back_populates='csxm')
    zjcs: Mapped[List['Zjcs']] = relationship('Zjcs', back_populates='csxm')
    djcsmx: Mapped[List['Djcsmx']] = relationship('Djcsmx', back_populates='csxm')
    zjcsmx: Mapped[List['Zjcsmx']] = relationship('Zjcsmx', back_populates='csxm')
    aqwmfmx: Mapped[List['Aqwmfmx']] = relationship('Aqwmfmx', back_populates='csxm')
    csxdezj: Mapped[List['Csxdezj']] = relationship('Csxdezj', back_populates='csxm')
    csxrcjhl: Mapped[List['Csxrcjhl']] = relationship('Csxrcjhl', back_populates='csxm')
    csxdezjmx: Mapped[List['Csxdezjmx']] = relationship('Csxdezjmx', back_populates='csxm')
    csxrcjhlmx: Mapped[List['Csxrcjhlmx']] = relationship('Csxrcjhlmx', back_populates='csxm')
    csxdercjhl: Mapped[List['Csxdercjhl']] = relationship('Csxdercjhl', back_populates='csxm')
    csxdercjhlmx: Mapped[List['Csxdercjhlmx']] = relationship('Csxdercjhlmx', back_populates='csxm')


class Fbrgycl(db.Model):
    __tablename__ = 'origin_13jt_fbrgycl'
    __table_args__ = (
        Index('ix_fbrgycl_create_time', 'create_time'),
        Index('ix_fbrgycl_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_fbrgycl_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_fbrgycl_file_id', 'file_id'),
        Index('ix_fbrgycl_id', 'id'),
        Index('ix_fbrgycl_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_fbrgycl_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='fbrgycl')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='fbrgycl')
    file: Mapped[Optional['File']] = relationship('File', back_populates='fbrgycl')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='fbrgycl')


class Fywj(db.Model):
    __tablename__ = 'origin_13jt_fywj'
    __table_args__ = (
        Index('ix_fywj_create_time', 'create_time'),
        Index('ix_fywj_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_fywj_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_fywj_file_id', 'file_id'),
        Index('ix_fywj_id', 'id'),
        Index('ix_fywj_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_fywj_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='fywj')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='fywj')
    file: Mapped[Optional['File']] = relationship('File', back_populates='fywj')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='fywj')
    fywjmx: Mapped[List['Fywjmx']] = relationship('Fywjmx', back_populates='fywj')


class Gfsj(db.Model):
    __tablename__ = 'origin_13jt_gfsj'
    __table_args__ = (
        Index('ix_gfsj_create_time', 'create_time'),
        Index('ix_gfsj_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_gfsj_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_gfsj_file_id', 'file_id'),
        Index('ix_gfsj_id', 'id'),
        Index('ix_gfsj_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_gfsj_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='gfsj')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='gfsj')
    file: Mapped[Optional['File']] = relationship('File', back_populates='gfsj')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='gfsj')
    gfsjmx: Mapped[List['Gfsjmx']] = relationship('Gfsjmx', back_populates='gfsj')


class Jrg(db.Model):
    __tablename__ = 'origin_13jt_jrg'
    __table_args__ = (
        Index('ix_jrg_create_time', 'create_time'),
        Index('ix_jrg_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_jrg_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_jrg_file_id', 'file_id'),
        Index('ix_jrg_id', 'id'),
        Index('ix_jrg_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_jrg_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='jrg')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='jrg')
    file: Mapped[Optional['File']] = relationship('File', back_populates='jrg')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='jrg')
    jrgbt: Mapped[List['Jrgbt']] = relationship('Jrgbt', back_populates='jrg')


class Qdxm(db.Model):
    __tablename__ = 'origin_13jt_qdxm'
    __table_args__ = (
        Index('ix_qdxm_create_time', 'create_time'),
        Index('ix_qdxm_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_qdxm_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_qdxm_file_id', 'file_id'),
        Index('ix_qdxm_id', 'id'),
        Index('ix_qdxm_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qdxm_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='qdxm')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='qdxm')
    file: Mapped[Optional['File']] = relationship('File', back_populates='qdxm')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qdxm')
    qdbt: Mapped[List['Qdbt']] = relationship('Qdbt', back_populates='qdxm')
    qdmx: Mapped[List['Qdmx']] = relationship('Qdmx', back_populates='qdxm')
    qdxdezj: Mapped[List['Qdxdezj']] = relationship('Qdxdezj', back_populates='qdxm')
    qdxrcjhl: Mapped[List['Qdxrcjhl']] = relationship('Qdxrcjhl', back_populates='qdxm')
    qdxdezjmx: Mapped[List['Qdxdezjmx']] = relationship('Qdxdezjmx', back_populates='qdxm')
    qdxrcjhlmx: Mapped[List['Qdxrcjhlmx']] = relationship('Qdxrcjhlmx', back_populates='qdxm')
    qdxdercjhl: Mapped[List['Qdxdercjhl']] = relationship('Qdxdercjhl', back_populates='qdxm')
    qdxdercjhlmx: Mapped[List['Qdxdercjhlmx']] = relationship('Qdxdercjhlmx', back_populates='qdxm')


class Qtxm(db.Model):
    __tablename__ = 'origin_13jt_qtxm'
    __table_args__ = (
        Index('ix_qtxm_create_time', 'create_time'),
        Index('ix_qtxm_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_qtxm_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_qtxm_file_id', 'file_id'),
        Index('ix_qtxm_id', 'id'),
        Index('ix_qtxm_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qtxm_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='qtxm')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='qtxm')
    file: Mapped[Optional['File']] = relationship('File', back_populates='qtxm')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qtxm')
    qtxmmx: Mapped[List['Qtxmmx']] = relationship('Qtxmmx', back_populates='qtxm')


class Rcjhz(db.Model):
    __tablename__ = 'origin_13jt_rcjhz'
    __table_args__ = (
        Index('ix_rcjhz_create_time', 'create_time'),
        Index('ix_rcjhz_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_rcjhz_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_rcjhz_file_id', 'file_id'),
        Index('ix_rcjhz_id', 'id'),
        Index('ix_rcjhz_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_rcjhz_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='rcjhz')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='rcjhz')
    file: Mapped[Optional['File']] = relationship('File', back_populates='rcjhz')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='rcjhz')
    rcjhzmx: Mapped[List['Rcjhzmx']] = relationship('Rcjhzmx', back_populates='rcjhz')


class Zcbfwf(db.Model):
    __tablename__ = 'origin_13jt_zcbfwf'
    __table_args__ = (
        Index('ix_zcbfwf_create_time', 'create_time'),
        Index('ix_zcbfwf_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_zcbfwf_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_zcbfwf_file_id', 'file_id'),
        Index('ix_zcbfwf_id', 'id'),
        Index('ix_zcbfwf_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_zcbfwf_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='zcbfwf')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='zcbfwf')
    file: Mapped[Optional['File']] = relationship('File', back_populates='zcbfwf')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='zcbfwf')


class Zjxmjdkzffj(db.Model):
    __tablename__ = 'origin_13jt_zjxmjdkzffj'
    __table_args__ = (
        Index('ix_zjxmjdkzffj_create_time', 'create_time'),
        Index('ix_zjxmjdkzffj_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_zjxmjdkzffj_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_zjxmjdkzffj_file_id', 'file_id'),
        Index('ix_zjxmjdkzffj_id', 'id'),
        Index('ix_zjxmjdkzffj_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_zjxmjdkzffj_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='zjxmjdkzffj')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='zjxmjdkzffj')
    file: Mapped[Optional['File']] = relationship('File', back_populates='zjxmjdkzffj')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='zjxmjdkzffj')
    zjxmjdkzffjmx: Mapped[List['Zjxmjdkzffjmx']] = relationship('Zjxmjdkzffjmx', back_populates='zjxmjdkzffj')
    zfmx: Mapped[List['Zfmx']] = relationship('Zfmx', back_populates='zjxmjdkzffj')


class Zlje(db.Model):
    __tablename__ = 'origin_13jt_zlje'
    __table_args__ = (
        Index('ix_zlje_create_time', 'create_time'),
        Index('ix_zlje_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_zlje_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_zlje_file_id', 'file_id'),
        Index('ix_zlje_id', 'id'),
        Index('ix_zlje_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_zlje_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='zlje')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='zlje')
    file: Mapped[Optional['File']] = relationship('File', back_populates='zlje')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='zlje')
    zljemx: Mapped[List['Zljemx']] = relationship('Zljemx', back_populates='zlje')


class Zygczg(db.Model):
    __tablename__ = 'origin_13jt_zygczg'
    __table_args__ = (
        Index('ix_zygczg_create_time', 'create_time'),
        Index('ix_zygczg_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_zygczg_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_zygczg_file_id', 'file_id'),
        Index('ix_zygczg_id', 'id'),
        Index('ix_zygczg_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_zygczg_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='zygczg')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='zygczg')
    file: Mapped[Optional['File']] = relationship('File', back_populates='zygczg')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='zygczg')


class Djcs(db.Model):
    __tablename__ = 'origin_13jt_djcs'
    __table_args__ = (
        Index('ix_djcs_create_time', 'create_time'),
        Index('ix_djcs_csxm_id', 'csxm_id'),
        Index('ix_djcs_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_djcs_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_djcs_file_id', 'file_id'),
        Index('ix_djcs_id', 'id'),
        Index('ix_djcs_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_djcs_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    csxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxm.id'))

    csxm: Mapped[Optional['Csxm']] = relationship('Csxm', back_populates='djcs')
    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='djcs')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='djcs')
    file: Mapped[Optional['File']] = relationship('File', back_populates='djcs')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='djcs')
    djcsmx: Mapped[List['Djcsmx']] = relationship('Djcsmx', back_populates='djcs')
    csxdezj: Mapped[List['Csxdezj']] = relationship('Csxdezj', back_populates='djcs')
    csxrcjhl: Mapped[List['Csxrcjhl']] = relationship('Csxrcjhl', back_populates='djcs')
    csxdezjmx: Mapped[List['Csxdezjmx']] = relationship('Csxdezjmx', back_populates='djcs')
    csxrcjhlmx: Mapped[List['Csxrcjhlmx']] = relationship('Csxrcjhlmx', back_populates='djcs')
    csxdercjhl: Mapped[List['Csxdercjhl']] = relationship('Csxdercjhl', back_populates='djcs')
    csxdercjhlmx: Mapped[List['Csxdercjhlmx']] = relationship('Csxdercjhlmx', back_populates='djcs')


class Fywjmx(db.Model):
    __tablename__ = 'origin_13jt_fywjmx'
    __table_args__ = (
        Index('ix_fywjmx_create_time', 'create_time'),
        Index('ix_fywjmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_fywjmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_fywjmx_file_id', 'file_id'),
        Index('ix_fywjmx_fywj_id', 'fywj_id'),
        Index('ix_fywjmx_id', 'id'),
        Index('ix_fywjmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_fywjmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    xh: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    je: Mapped[Optional[str]] = mapped_column(String(100))
    zgj: Mapped[Optional[str]] = mapped_column(String(100))
    fyxlb: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    fywj_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_fywj.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='fywjmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='fywjmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='fywjmx')
    fywj: Mapped[Optional['Fywj']] = relationship('Fywj', back_populates='fywjmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='fywjmx')


class Gfsjmx(db.Model):
    __tablename__ = 'origin_13jt_gfsjmx'
    __table_args__ = (
        Index('ix_gfsjmx_create_time', 'create_time'),
        Index('ix_gfsjmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_gfsjmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_gfsjmx_file_id', 'file_id'),
        Index('ix_gfsjmx_gfsj_id', 'gfsj_id'),
        Index('ix_gfsjmx_id', 'id'),
        Index('ix_gfsjmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_gfsjmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    xh: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    qfjs: Mapped[Optional[str]] = mapped_column(String(100))
    jsjc: Mapped[Optional[str]] = mapped_column(String(100))
    fl: Mapped[Optional[str]] = mapped_column(String(100))
    je: Mapped[Optional[str]] = mapped_column(String(100))
    fyxlb: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    gfsj_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_gfsj.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='gfsjmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='gfsjmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='gfsjmx')
    gfsj: Mapped[Optional['Gfsj']] = relationship('Gfsj', back_populates='gfsjmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='gfsjmx')


class Jrgbt(db.Model):
    __tablename__ = 'origin_13jt_jrgbt'
    __table_args__ = (
        Index('ix_jrgbt_create_time', 'create_time'),
        Index('ix_jrgbt_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_jrgbt_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_jrgbt_file_id', 'file_id'),
        Index('ix_jrgbt_id', 'id'),
        Index('ix_jrgbt_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_jrgbt_jrg_id', 'jrg_id'),
        Index('ix_jrgbt_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    xh: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    je: Mapped[Optional[str]] = mapped_column(String(100))
    lb: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    jrg_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jrg.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='jrgbt')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='jrgbt')
    file: Mapped[Optional['File']] = relationship('File', back_populates='jrgbt')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='jrgbt')
    jrg: Mapped[Optional['Jrg']] = relationship('Jrg', back_populates='jrgbt')


class Qdbt(db.Model):
    __tablename__ = 'origin_13jt_qdbt'
    __table_args__ = (
        Index('ix_qdbt_create_time', 'create_time'),
        Index('ix_qdbt_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_qdbt_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_qdbt_file_id', 'file_id'),
        Index('ix_qdbt_id', 'id'),
        Index('ix_qdbt_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qdbt_qdxm_id', 'qdxm_id'),
        Index('ix_qdbt_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    xh: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    je: Mapped[Optional[str]] = mapped_column(String(100))
    zgj: Mapped[Optional[str]] = mapped_column(String(100))
    bz: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    qdxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxm.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='qdbt')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='qdbt')
    file: Mapped[Optional['File']] = relationship('File', back_populates='qdbt')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qdbt')
    qdxm: Mapped[Optional['Qdxm']] = relationship('Qdxm', back_populates='qdbt')
    qdmx: Mapped[List['Qdmx']] = relationship('Qdmx', back_populates='qdbt')
    qdxdezj: Mapped[List['Qdxdezj']] = relationship('Qdxdezj', back_populates='qdbt')
    qdxrcjhl: Mapped[List['Qdxrcjhl']] = relationship('Qdxrcjhl', back_populates='qdbt')
    qdxdezjmx: Mapped[List['Qdxdezjmx']] = relationship('Qdxdezjmx', back_populates='qdbt')
    qdxrcjhlmx: Mapped[List['Qdxrcjhlmx']] = relationship('Qdxrcjhlmx', back_populates='qdbt')
    qdxdercjhl: Mapped[List['Qdxdercjhl']] = relationship('Qdxdercjhl', back_populates='qdbt')
    qdxdercjhlmx: Mapped[List['Qdxdercjhlmx']] = relationship('Qdxdercjhlmx', back_populates='qdbt')


class Qtxmmx(db.Model):
    __tablename__ = 'origin_13jt_qtxmmx'
    __table_args__ = (
        Index('ix_qtxmmx_create_time', 'create_time'),
        Index('ix_qtxmmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_qtxmmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_qtxmmx_file_id', 'file_id'),
        Index('ix_qtxmmx_id', 'id'),
        Index('ix_qtxmmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qtxmmx_qtxm_id', 'qtxm_id'),
        Index('ix_qtxmmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    xh: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    je: Mapped[Optional[str]] = mapped_column(String(100))
    bz: Mapped[Optional[str]] = mapped_column(String(100))
    xmlb: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    qtxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qtxm.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='qtxmmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='qtxmmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='qtxmmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qtxmmx')
    qtxm: Mapped[Optional['Qtxm']] = relationship('Qtxm', back_populates='qtxmmx')


class Rcjhzmx(db.Model):
    __tablename__ = 'origin_13jt_rcjhzmx'
    __table_args__ = (
        Index('ix_rcjhzmx_create_time', 'create_time'),
        Index('ix_rcjhzmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_rcjhzmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_rcjhzmx_file_id', 'file_id'),
        Index('ix_rcjhzmx_id', 'id'),
        Index('ix_rcjhzmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_rcjhzmx_rcjhz_id', 'rcjhz_id'),
        Index('ix_rcjhzmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    rcjid: Mapped[Optional[str]] = mapped_column(String(100))
    rcjbm: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    ggxh: Mapped[Optional[str]] = mapped_column(String(100))
    dw: Mapped[Optional[str]] = mapped_column(String(100))
    dj: Mapped[Optional[str]] = mapped_column(String(100))
    sl: Mapped[Optional[str]] = mapped_column(String(100))
    hj: Mapped[Optional[str]] = mapped_column(String(100))
    gycs: Mapped[Optional[str]] = mapped_column(String(100))
    cd: Mapped[Optional[str]] = mapped_column(String(100))
    rcjlb: Mapped[Optional[str]] = mapped_column(String(100))
    jgbz: Mapped[Optional[str]] = mapped_column(String(100))
    zyclbz: Mapped[Optional[str]] = mapped_column(String(100))
    zgjbz: Mapped[Optional[str]] = mapped_column(String(100))
    zcbz: Mapped[Optional[str]] = mapped_column(String(100))
    sbbz: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    rcjhz_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_rcjhz.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='rcjhzmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='rcjhzmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='rcjhzmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='rcjhzmx')
    rcjhz: Mapped[Optional['Rcjhz']] = relationship('Rcjhz', back_populates='rcjhzmx')


class Zjcs(db.Model):
    __tablename__ = 'origin_13jt_zjcs'
    __table_args__ = (
        Index('ix_zjcs_create_time', 'create_time'),
        Index('ix_zjcs_csxm_id', 'csxm_id'),
        Index('ix_zjcs_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_zjcs_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_zjcs_file_id', 'file_id'),
        Index('ix_zjcs_id', 'id'),
        Index('ix_zjcs_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_zjcs_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    csxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxm.id'))

    csxm: Mapped[Optional['Csxm']] = relationship('Csxm', back_populates='zjcs')
    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='zjcs')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='zjcs')
    file: Mapped[Optional['File']] = relationship('File', back_populates='zjcs')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='zjcs')
    zjcsmx: Mapped[List['Zjcsmx']] = relationship('Zjcsmx', back_populates='zjcs')
    aqwmfmx: Mapped[List['Aqwmfmx']] = relationship('Aqwmfmx', back_populates='zjcs')


class Zjxmjdkzffjmx(db.Model):
    __tablename__ = 'origin_13jt_zjxmjdkzffjmx'
    __table_args__ = (
        Index('ix_zjxmjdkzffjmx_create_time', 'create_time'),
        Index('ix_zjxmjdkzffjmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_zjxmjdkzffjmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_zjxmjdkzffjmx_file_id', 'file_id'),
        Index('ix_zjxmjdkzffjmx_id', 'id'),
        Index('ix_zjxmjdkzffjmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_zjxmjdkzffjmx_update_time', 'update_time'),
        Index('ix_zjxmjdkzffjmx_zjxmjdkzffj_id', 'zjxmjdkzffj_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    xh: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    zjje: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    zjxmjdkzffj_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_zjxmjdkzffj.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='zjxmjdkzffjmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='zjxmjdkzffjmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='zjxmjdkzffjmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='zjxmjdkzffjmx')
    zjxmjdkzffj: Mapped[Optional['Zjxmjdkzffj']] = relationship('Zjxmjdkzffj', back_populates='zjxmjdkzffjmx')
    zfmx: Mapped[List['Zfmx']] = relationship('Zfmx', back_populates='zjxmjdkzffjmx')


class Zljemx(db.Model):
    __tablename__ = 'origin_13jt_zljemx'
    __table_args__ = (
        Index('ix_zljemx_create_time', 'create_time'),
        Index('ix_zljemx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_zljemx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_zljemx_file_id', 'file_id'),
        Index('ix_zljemx_id', 'id'),
        Index('ix_zljemx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_zljemx_update_time', 'update_time'),
        Index('ix_zljemx_zlje_id', 'zlje_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    xh: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    dw: Mapped[Optional[str]] = mapped_column(String(100))
    zdje: Mapped[Optional[str]] = mapped_column(String(100))
    bz: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    zlje_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_zlje.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='zljemx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='zljemx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='zljemx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='zljemx')
    zlje: Mapped[Optional['Zlje']] = relationship('Zlje', back_populates='zljemx')


class Djcsmx(db.Model):
    __tablename__ = 'origin_13jt_djcsmx'
    __table_args__ = (
        Index('ix_djcsmx_create_time', 'create_time'),
        Index('ix_djcsmx_csxm_id', 'csxm_id'),
        Index('ix_djcsmx_djcs_id', 'djcs_id'),
        Index('ix_djcsmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_djcsmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_djcsmx_file_id', 'file_id'),
        Index('ix_djcsmx_id', 'id'),
        Index('ix_djcsmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_djcsmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    xh: Mapped[Optional[str]] = mapped_column(String(100))
    bm: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    xmtz: Mapped[Optional[str]] = mapped_column(Text)
    jsgz: Mapped[Optional[str]] = mapped_column(Text)
    dw: Mapped[Optional[str]] = mapped_column(String(100))
    sl: Mapped[Optional[str]] = mapped_column(String(100))
    zhdj: Mapped[Optional[str]] = mapped_column(String(100))
    rgf: Mapped[Optional[str]] = mapped_column(String(100))
    zcf: Mapped[Optional[str]] = mapped_column(String(100))
    fcf: Mapped[Optional[str]] = mapped_column(String(100))
    clf: Mapped[Optional[str]] = mapped_column(String(100))
    jxf: Mapped[Optional[str]] = mapped_column(String(100))
    glf: Mapped[Optional[str]] = mapped_column(String(100))
    lr: Mapped[Optional[str]] = mapped_column(String(100))
    zhhj: Mapped[Optional[str]] = mapped_column(String(100))
    zgj: Mapped[Optional[str]] = mapped_column(String(100))
    zgr: Mapped[Optional[str]] = mapped_column(String(100))
    sbf: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    csxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxm.id'))
    djcs_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcs.id'))

    csxm: Mapped[Optional['Csxm']] = relationship('Csxm', back_populates='djcsmx')
    djcs: Mapped[Optional['Djcs']] = relationship('Djcs', back_populates='djcsmx')
    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='djcsmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='djcsmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='djcsmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='djcsmx')
    csxdezj: Mapped[List['Csxdezj']] = relationship('Csxdezj', back_populates='djcsmx')
    csxrcjhl: Mapped[List['Csxrcjhl']] = relationship('Csxrcjhl', back_populates='djcsmx')
    csxdezjmx: Mapped[List['Csxdezjmx']] = relationship('Csxdezjmx', back_populates='djcsmx')
    csxrcjhlmx: Mapped[List['Csxrcjhlmx']] = relationship('Csxrcjhlmx', back_populates='djcsmx')
    csxdercjhl: Mapped[List['Csxdercjhl']] = relationship('Csxdercjhl', back_populates='djcsmx')
    csxdercjhlmx: Mapped[List['Csxdercjhlmx']] = relationship('Csxdercjhlmx', back_populates='djcsmx')


class Qdmx(db.Model):
    __tablename__ = 'origin_13jt_qdmx'
    __table_args__ = (
        Index('ix_qdmx_create_time', 'create_time'),
        Index('ix_qdmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_qdmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_qdmx_file_id', 'file_id'),
        Index('ix_qdmx_id', 'id'),
        Index('ix_qdmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qdmx_qdbt_id', 'qdbt_id'),
        Index('ix_qdmx_qdxm_id', 'qdxm_id'),
        Index('ix_qdmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    xh: Mapped[Optional[str]] = mapped_column(String(100))
    qdbm: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    xmtz: Mapped[Optional[str]] = mapped_column(Text)
    jsgz: Mapped[Optional[str]] = mapped_column(Text)
    dw: Mapped[Optional[str]] = mapped_column(String(100))
    sl: Mapped[Optional[str]] = mapped_column(String(100))
    zhdj: Mapped[Optional[str]] = mapped_column(String(100))
    rgf: Mapped[Optional[str]] = mapped_column(String(100))
    zcf: Mapped[Optional[str]] = mapped_column(String(100))
    fcf: Mapped[Optional[str]] = mapped_column(String(100))
    clf: Mapped[Optional[str]] = mapped_column(String(100))
    jxf: Mapped[Optional[str]] = mapped_column(String(100))
    glf: Mapped[Optional[str]] = mapped_column(String(100))
    lr: Mapped[Optional[str]] = mapped_column(String(100))
    zhhj: Mapped[Optional[str]] = mapped_column(String(100))
    zgj: Mapped[Optional[str]] = mapped_column(String(100))
    zgr: Mapped[Optional[str]] = mapped_column(String(100))
    bz: Mapped[Optional[str]] = mapped_column(String(100))
    sbf: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    qdxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxm.id'))
    qdbt_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdbt.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='qdmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='qdmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='qdmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qdmx')
    qdbt: Mapped[Optional['Qdbt']] = relationship('Qdbt', back_populates='qdmx')
    qdxm: Mapped[Optional['Qdxm']] = relationship('Qdxm', back_populates='qdmx')
    qdxdezj: Mapped[List['Qdxdezj']] = relationship('Qdxdezj', back_populates='qdmx')
    qdxrcjhl: Mapped[List['Qdxrcjhl']] = relationship('Qdxrcjhl', back_populates='qdmx')
    qdxdezjmx: Mapped[List['Qdxdezjmx']] = relationship('Qdxdezjmx', back_populates='qdmx')
    qdxrcjhlmx: Mapped[List['Qdxrcjhlmx']] = relationship('Qdxrcjhlmx', back_populates='qdmx')
    qdxdercjhl: Mapped[List['Qdxdercjhl']] = relationship('Qdxdercjhl', back_populates='qdmx')
    qdxdercjhlmx: Mapped[List['Qdxdercjhlmx']] = relationship('Qdxdercjhlmx', back_populates='qdmx')


class Zfmx(db.Model):
    __tablename__ = 'origin_13jt_zfmx'
    __table_args__ = (
        Index('ix_zfmx_create_time', 'create_time'),
        Index('ix_zfmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_zfmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_zfmx_file_id', 'file_id'),
        Index('ix_zfmx_id', 'id'),
        Index('ix_zfmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_zfmx_update_time', 'update_time'),
        Index('ix_zfmx_zjxmjdkzffj_id', 'zjxmjdkzffj_id'),
        Index('ix_zfmx_zjxmjdkzffjmx_id', 'zjxmjdkzffjmx_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    zfcs: Mapped[Optional[str]] = mapped_column(String(100))
    zfje: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    zjxmjdkzffj_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_zjxmjdkzffj.id'))
    zjxmjdkzffjmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_zjxmjdkzffjmx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='zfmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='zfmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='zfmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='zfmx')
    zjxmjdkzffj: Mapped[Optional['Zjxmjdkzffj']] = relationship('Zjxmjdkzffj', back_populates='zfmx')
    zjxmjdkzffjmx: Mapped[Optional['Zjxmjdkzffjmx']] = relationship('Zjxmjdkzffjmx', back_populates='zfmx')


class Zjcsmx(db.Model):
    __tablename__ = 'origin_13jt_zjcsmx'
    __table_args__ = (
        Index('ix_zjcsmx_create_time', 'create_time'),
        Index('ix_zjcsmx_csxm_id', 'csxm_id'),
        Index('ix_zjcsmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_zjcsmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_zjcsmx_file_id', 'file_id'),
        Index('ix_zjcsmx_id', 'id'),
        Index('ix_zjcsmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_zjcsmx_update_time', 'update_time'),
        Index('ix_zjcsmx_zjcs_id', 'zjcs_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    xh: Mapped[Optional[str]] = mapped_column(String(100))
    bm: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    js: Mapped[Optional[str]] = mapped_column(String(100))
    jsjc: Mapped[Optional[str]] = mapped_column(String(100))
    fl: Mapped[Optional[str]] = mapped_column(String(100))
    je: Mapped[Optional[str]] = mapped_column(String(100))
    xmlb: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    csxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxm.id'))
    zjcs_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_zjcs.id'))

    csxm: Mapped[Optional['Csxm']] = relationship('Csxm', back_populates='zjcsmx')
    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='zjcsmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='zjcsmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='zjcsmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='zjcsmx')
    zjcs: Mapped[Optional['Zjcs']] = relationship('Zjcs', back_populates='zjcsmx')
    aqwmfmx: Mapped[List['Aqwmfmx']] = relationship('Aqwmfmx', back_populates='zjcsmx')


class Aqwmfmx(db.Model):
    __tablename__ = 'origin_13jt_aqwmfmx'
    __table_args__ = (
        Index('ix_aqwmfmx_create_time', 'create_time'),
        Index('ix_aqwmfmx_csxm_id', 'csxm_id'),
        Index('ix_aqwmfmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_aqwmfmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_aqwmfmx_file_id', 'file_id'),
        Index('ix_aqwmfmx_id', 'id'),
        Index('ix_aqwmfmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_aqwmfmx_update_time', 'update_time'),
        Index('ix_aqwmfmx_zjcs_id', 'zjcs_id'),
        Index('ix_aqwmfmx_zjcsmx_id', 'zjcsmx_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    js: Mapped[Optional[str]] = mapped_column(String(100))
    jsjc: Mapped[Optional[str]] = mapped_column(String(100))
    fl: Mapped[Optional[str]] = mapped_column(String(100))
    je: Mapped[Optional[str]] = mapped_column(String(100))
    xmlb: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    csxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxm.id'))
    zjcs_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_zjcs.id'))
    zjcsmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_zjcsmx.id'))

    csxm: Mapped[Optional['Csxm']] = relationship('Csxm', back_populates='aqwmfmx')
    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='aqwmfmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='aqwmfmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='aqwmfmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='aqwmfmx')
    zjcs: Mapped[Optional['Zjcs']] = relationship('Zjcs', back_populates='aqwmfmx')
    zjcsmx: Mapped[Optional['Zjcsmx']] = relationship('Zjcsmx', back_populates='aqwmfmx')


class Csxdezj(db.Model):
    __tablename__ = 'origin_13jt_csxdezj'
    __table_args__ = (
        Index('ix_csxdezj_create_time', 'create_time'),
        Index('ix_csxdezj_csxm_id', 'csxm_id'),
        Index('ix_csxdezj_djcs_id', 'djcs_id'),
        Index('ix_csxdezj_djcsmx_id', 'djcsmx_id'),
        Index('ix_csxdezj_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_csxdezj_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_csxdezj_file_id', 'file_id'),
        Index('ix_csxdezj_id', 'id'),
        Index('ix_csxdezj_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_csxdezj_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    csxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxm.id'))
    djcs_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcs.id'))
    djcsmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcsmx.id'))

    csxm: Mapped[Optional['Csxm']] = relationship('Csxm', back_populates='csxdezj')
    djcs: Mapped[Optional['Djcs']] = relationship('Djcs', back_populates='csxdezj')
    djcsmx: Mapped[Optional['Djcsmx']] = relationship('Djcsmx', back_populates='csxdezj')
    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='csxdezj')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='csxdezj')
    file: Mapped[Optional['File']] = relationship('File', back_populates='csxdezj')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='csxdezj')
    csxdezjmx: Mapped[List['Csxdezjmx']] = relationship('Csxdezjmx', back_populates='csxdezj')
    csxdercjhl: Mapped[List['Csxdercjhl']] = relationship('Csxdercjhl', back_populates='csxdezj')
    csxdercjhlmx: Mapped[List['Csxdercjhlmx']] = relationship('Csxdercjhlmx', back_populates='csxdezj')


class Csxrcjhl(db.Model):
    __tablename__ = 'origin_13jt_csxrcjhl'
    __table_args__ = (
        Index('ix_csxrcjhl_create_time', 'create_time'),
        Index('ix_csxrcjhl_csxm_id', 'csxm_id'),
        Index('ix_csxrcjhl_djcs_id', 'djcs_id'),
        Index('ix_csxrcjhl_djcsmx_id', 'djcsmx_id'),
        Index('ix_csxrcjhl_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_csxrcjhl_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_csxrcjhl_file_id', 'file_id'),
        Index('ix_csxrcjhl_id', 'id'),
        Index('ix_csxrcjhl_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_csxrcjhl_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    csxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxm.id'))
    djcs_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcs.id'))
    djcsmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcsmx.id'))

    csxm: Mapped[Optional['Csxm']] = relationship('Csxm', back_populates='csxrcjhl')
    djcs: Mapped[Optional['Djcs']] = relationship('Djcs', back_populates='csxrcjhl')
    djcsmx: Mapped[Optional['Djcsmx']] = relationship('Djcsmx', back_populates='csxrcjhl')
    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='csxrcjhl')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='csxrcjhl')
    file: Mapped[Optional['File']] = relationship('File', back_populates='csxrcjhl')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='csxrcjhl')
    csxrcjhlmx: Mapped[List['Csxrcjhlmx']] = relationship('Csxrcjhlmx', back_populates='csxrcjhl')


class Qdxdezj(db.Model):
    __tablename__ = 'origin_13jt_qdxdezj'
    __table_args__ = (
        Index('ix_qdxdezj_create_time', 'create_time'),
        Index('ix_qdxdezj_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_qdxdezj_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_qdxdezj_file_id', 'file_id'),
        Index('ix_qdxdezj_id', 'id'),
        Index('ix_qdxdezj_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qdxdezj_qdbt_id', 'qdbt_id'),
        Index('ix_qdxdezj_qdmx_id', 'qdmx_id'),
        Index('ix_qdxdezj_qdxm_id', 'qdxm_id'),
        Index('ix_qdxdezj_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    qdxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxm.id'))
    qdbt_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdbt.id'))
    qdmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdmx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='qdxdezj')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='qdxdezj')
    file: Mapped[Optional['File']] = relationship('File', back_populates='qdxdezj')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qdxdezj')
    qdbt: Mapped[Optional['Qdbt']] = relationship('Qdbt', back_populates='qdxdezj')
    qdmx: Mapped[Optional['Qdmx']] = relationship('Qdmx', back_populates='qdxdezj')
    qdxm: Mapped[Optional['Qdxm']] = relationship('Qdxm', back_populates='qdxdezj')
    qdxdezjmx: Mapped[List['Qdxdezjmx']] = relationship('Qdxdezjmx', back_populates='qdxdezj')
    qdxdercjhl: Mapped[List['Qdxdercjhl']] = relationship('Qdxdercjhl', back_populates='qdxdezj')
    qdxdercjhlmx: Mapped[List['Qdxdercjhlmx']] = relationship('Qdxdercjhlmx', back_populates='qdxdezj')


class Qdxrcjhl(db.Model):
    __tablename__ = 'origin_13jt_qdxrcjhl'
    __table_args__ = (
        Index('ix_qdxrcjhl_create_time', 'create_time'),
        Index('ix_qdxrcjhl_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_qdxrcjhl_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_qdxrcjhl_file_id', 'file_id'),
        Index('ix_qdxrcjhl_id', 'id'),
        Index('ix_qdxrcjhl_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qdxrcjhl_qdbt_id', 'qdbt_id'),
        Index('ix_qdxrcjhl_qdmx_id', 'qdmx_id'),
        Index('ix_qdxrcjhl_qdxm_id', 'qdxm_id'),
        Index('ix_qdxrcjhl_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    qdxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxm.id'))
    qdbt_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdbt.id'))
    qdmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdmx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='qdxrcjhl')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='qdxrcjhl')
    file: Mapped[Optional['File']] = relationship('File', back_populates='qdxrcjhl')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qdxrcjhl')
    qdbt: Mapped[Optional['Qdbt']] = relationship('Qdbt', back_populates='qdxrcjhl')
    qdmx: Mapped[Optional['Qdmx']] = relationship('Qdmx', back_populates='qdxrcjhl')
    qdxm: Mapped[Optional['Qdxm']] = relationship('Qdxm', back_populates='qdxrcjhl')
    qdxrcjhlmx: Mapped[List['Qdxrcjhlmx']] = relationship('Qdxrcjhlmx', back_populates='qdxrcjhl')


class Csxdezjmx(db.Model):
    __tablename__ = 'origin_13jt_csxdezjmx'
    __table_args__ = (
        Index('ix_csxdezjmx_create_time', 'create_time'),
        Index('ix_csxdezjmx_csxdezj_id', 'csxdezj_id'),
        Index('ix_csxdezjmx_csxm_id', 'csxm_id'),
        Index('ix_csxdezjmx_djcs_id', 'djcs_id'),
        Index('ix_csxdezjmx_djcsmx_id', 'djcsmx_id'),
        Index('ix_csxdezjmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_csxdezjmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_csxdezjmx_file_id', 'file_id'),
        Index('ix_csxdezjmx_id', 'id'),
        Index('ix_csxdezjmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_csxdezjmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    debm: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(100))
    dw: Mapped[Optional[str]] = mapped_column(String(100))
    dwqdsl: Mapped[Optional[str]] = mapped_column(String(100))
    dj: Mapped[Optional[str]] = mapped_column(String(100))
    rgf: Mapped[Optional[str]] = mapped_column(String(100))
    zcf: Mapped[Optional[str]] = mapped_column(String(100))
    fcf: Mapped[Optional[str]] = mapped_column(String(100))
    clf: Mapped[Optional[str]] = mapped_column(String(100))
    jxf: Mapped[Optional[str]] = mapped_column(String(100))
    glf: Mapped[Optional[str]] = mapped_column(String(100))
    lr: Mapped[Optional[str]] = mapped_column(String(100))
    hj: Mapped[Optional[str]] = mapped_column(String(100))
    sbf: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    csxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxm.id'))
    djcs_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcs.id'))
    djcsmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcsmx.id'))
    csxdezj_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxdezj.id'))

    csxdezj: Mapped[Optional['Csxdezj']] = relationship('Csxdezj', back_populates='csxdezjmx')
    csxm: Mapped[Optional['Csxm']] = relationship('Csxm', back_populates='csxdezjmx')
    djcs: Mapped[Optional['Djcs']] = relationship('Djcs', back_populates='csxdezjmx')
    djcsmx: Mapped[Optional['Djcsmx']] = relationship('Djcsmx', back_populates='csxdezjmx')
    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='csxdezjmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='csxdezjmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='csxdezjmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='csxdezjmx')
    csxdercjhl: Mapped[List['Csxdercjhl']] = relationship('Csxdercjhl', back_populates='csxdezjmx')
    csxdercjhlmx: Mapped[List['Csxdercjhlmx']] = relationship('Csxdercjhlmx', back_populates='csxdezjmx')


class Csxrcjhlmx(db.Model):
    __tablename__ = 'origin_13jt_csxrcjhlmx'
    __table_args__ = (
        Index('ix_csxrcjhlmx_create_time', 'create_time'),
        Index('ix_csxrcjhlmx_csxm_id', 'csxm_id'),
        Index('ix_csxrcjhlmx_csxrcjhl_id', 'csxrcjhl_id'),
        Index('ix_csxrcjhlmx_djcs_id', 'djcs_id'),
        Index('ix_csxrcjhlmx_djcsmx_id', 'djcsmx_id'),
        Index('ix_csxrcjhlmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_csxrcjhlmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_csxrcjhlmx_file_id', 'file_id'),
        Index('ix_csxrcjhlmx_id', 'id'),
        Index('ix_csxrcjhlmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_csxrcjhlmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    rcjid: Mapped[Optional[str]] = mapped_column(String(100))
    rcjhl: Mapped[Optional[str]] = mapped_column(String(100))
    rcjhj: Mapped[Optional[str]] = mapped_column(String(100))
    zgjbz: Mapped[Optional[str]] = mapped_column(String(100))
    zcbz: Mapped[Optional[str]] = mapped_column(String(100))
    zyclbz: Mapped[Optional[str]] = mapped_column(String(100))
    sbbz: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    csxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxm.id'))
    djcs_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcs.id'))
    djcsmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcsmx.id'))
    csxrcjhl_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxrcjhl.id'))

    csxm: Mapped[Optional['Csxm']] = relationship('Csxm', back_populates='csxrcjhlmx')
    csxrcjhl: Mapped[Optional['Csxrcjhl']] = relationship('Csxrcjhl', back_populates='csxrcjhlmx')
    djcs: Mapped[Optional['Djcs']] = relationship('Djcs', back_populates='csxrcjhlmx')
    djcsmx: Mapped[Optional['Djcsmx']] = relationship('Djcsmx', back_populates='csxrcjhlmx')
    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='csxrcjhlmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='csxrcjhlmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='csxrcjhlmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='csxrcjhlmx')


class Qdxdezjmx(db.Model):
    __tablename__ = 'origin_13jt_qdxdezjmx'
    __table_args__ = (
        Index('ix_qdxdezjmx_create_time', 'create_time'),
        Index('ix_qdxdezjmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_qdxdezjmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_qdxdezjmx_file_id', 'file_id'),
        Index('ix_qdxdezjmx_id', 'id'),
        Index('ix_qdxdezjmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qdxdezjmx_qdbt_id', 'qdbt_id'),
        Index('ix_qdxdezjmx_qdmx_id', 'qdmx_id'),
        Index('ix_qdxdezjmx_qdxdezj_id', 'qdxdezj_id'),
        Index('ix_qdxdezjmx_qdxm_id', 'qdxm_id'),
        Index('ix_qdxdezjmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    debm: Mapped[Optional[str]] = mapped_column(String(100))
    mc: Mapped[Optional[str]] = mapped_column(String(500))
    dw: Mapped[Optional[str]] = mapped_column(String(100))
    dwqdsl: Mapped[Optional[str]] = mapped_column(String(100))
    dj: Mapped[Optional[str]] = mapped_column(String(100))
    rgf: Mapped[Optional[str]] = mapped_column(String(100))
    zcf: Mapped[Optional[str]] = mapped_column(String(100))
    fcf: Mapped[Optional[str]] = mapped_column(String(100))
    clf: Mapped[Optional[str]] = mapped_column(String(100))
    jxf: Mapped[Optional[str]] = mapped_column(String(100))
    glf: Mapped[Optional[str]] = mapped_column(String(100))
    lr: Mapped[Optional[str]] = mapped_column(String(100))
    hj: Mapped[Optional[str]] = mapped_column(String(100))
    sbf: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    qdxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxm.id'))
    qdbt_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdbt.id'))
    qdmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdmx.id'))
    qdxdezj_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxdezj.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='qdxdezjmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='qdxdezjmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='qdxdezjmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qdxdezjmx')
    qdbt: Mapped[Optional['Qdbt']] = relationship('Qdbt', back_populates='qdxdezjmx')
    qdmx: Mapped[Optional['Qdmx']] = relationship('Qdmx', back_populates='qdxdezjmx')
    qdxdezj: Mapped[Optional['Qdxdezj']] = relationship('Qdxdezj', back_populates='qdxdezjmx')
    qdxm: Mapped[Optional['Qdxm']] = relationship('Qdxm', back_populates='qdxdezjmx')
    qdxdercjhl: Mapped[List['Qdxdercjhl']] = relationship('Qdxdercjhl', back_populates='qdxdezjmx')
    qdxdercjhlmx: Mapped[List['Qdxdercjhlmx']] = relationship('Qdxdercjhlmx', back_populates='qdxdezjmx')


class Qdxrcjhlmx(db.Model):
    __tablename__ = 'origin_13jt_qdxrcjhlmx'
    __table_args__ = (
        Index('ix_qdxrcjhlmx_create_time', 'create_time'),
        Index('ix_qdxrcjhlmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_qdxrcjhlmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_qdxrcjhlmx_file_id', 'file_id'),
        Index('ix_qdxrcjhlmx_id', 'id'),
        Index('ix_qdxrcjhlmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qdxrcjhlmx_qdbt_id', 'qdbt_id'),
        Index('ix_qdxrcjhlmx_qdmx_id', 'qdmx_id'),
        Index('ix_qdxrcjhlmx_qdxm_id', 'qdxm_id'),
        Index('ix_qdxrcjhlmx_qdxrcjhl_id', 'qdxrcjhl_id'),
        Index('ix_qdxrcjhlmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    rcjid: Mapped[Optional[str]] = mapped_column(String(100))
    rcjhl: Mapped[Optional[str]] = mapped_column(String(100))
    rcjhj: Mapped[Optional[str]] = mapped_column(String(100))
    zgjbz: Mapped[Optional[str]] = mapped_column(String(100))
    zcbz: Mapped[Optional[str]] = mapped_column(String(100))
    zyclbz: Mapped[Optional[str]] = mapped_column(String(100))
    sbbz: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    qdxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxm.id'))
    qdbt_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdbt.id'))
    qdmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdmx.id'))
    qdxrcjhl_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxrcjhl.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='qdxrcjhlmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='qdxrcjhlmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='qdxrcjhlmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qdxrcjhlmx')
    qdbt: Mapped[Optional['Qdbt']] = relationship('Qdbt', back_populates='qdxrcjhlmx')
    qdmx: Mapped[Optional['Qdmx']] = relationship('Qdmx', back_populates='qdxrcjhlmx')
    qdxm: Mapped[Optional['Qdxm']] = relationship('Qdxm', back_populates='qdxrcjhlmx')
    qdxrcjhl: Mapped[Optional['Qdxrcjhl']] = relationship('Qdxrcjhl', back_populates='qdxrcjhlmx')


class Csxdercjhl(db.Model):
    __tablename__ = 'origin_13jt_csxdercjhl'
    __table_args__ = (
        Index('ix_csxdercjhl_create_time', 'create_time'),
        Index('ix_csxdercjhl_csxdezj_id', 'csxdezj_id'),
        Index('ix_csxdercjhl_csxdezjmx_id', 'csxdezjmx_id'),
        Index('ix_csxdercjhl_csxm_id', 'csxm_id'),
        Index('ix_csxdercjhl_djcs_id', 'djcs_id'),
        Index('ix_csxdercjhl_djcsmx_id', 'djcsmx_id'),
        Index('ix_csxdercjhl_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_csxdercjhl_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_csxdercjhl_file_id', 'file_id'),
        Index('ix_csxdercjhl_id', 'id'),
        Index('ix_csxdercjhl_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_csxdercjhl_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    csxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxm.id'))
    djcs_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcs.id'))
    djcsmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcsmx.id'))
    csxdezj_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxdezj.id'))
    csxdezjmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxdezjmx.id'))

    csxdezj: Mapped[Optional['Csxdezj']] = relationship('Csxdezj', back_populates='csxdercjhl')
    csxdezjmx: Mapped[Optional['Csxdezjmx']] = relationship('Csxdezjmx', back_populates='csxdercjhl')
    csxm: Mapped[Optional['Csxm']] = relationship('Csxm', back_populates='csxdercjhl')
    djcs: Mapped[Optional['Djcs']] = relationship('Djcs', back_populates='csxdercjhl')
    djcsmx: Mapped[Optional['Djcsmx']] = relationship('Djcsmx', back_populates='csxdercjhl')
    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='csxdercjhl')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='csxdercjhl')
    file: Mapped[Optional['File']] = relationship('File', back_populates='csxdercjhl')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='csxdercjhl')
    csxdercjhlmx: Mapped[List['Csxdercjhlmx']] = relationship('Csxdercjhlmx', back_populates='csxdercjhl')


class Qdxdercjhl(db.Model):
    __tablename__ = 'origin_13jt_qdxdercjhl'
    __table_args__ = (
        Index('ix_qdxdercjhl_create_time', 'create_time'),
        Index('ix_qdxdercjhl_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_qdxdercjhl_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_qdxdercjhl_file_id', 'file_id'),
        Index('ix_qdxdercjhl_id', 'id'),
        Index('ix_qdxdercjhl_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qdxdercjhl_qdbt_id', 'qdbt_id'),
        Index('ix_qdxdercjhl_qdmx_id', 'qdmx_id'),
        Index('ix_qdxdercjhl_qdxdezj_id', 'qdxdezj_id'),
        Index('ix_qdxdercjhl_qdxdezjmx_id', 'qdxdezjmx_id'),
        Index('ix_qdxdercjhl_qdxm_id', 'qdxm_id'),
        Index('ix_qdxdercjhl_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    qdxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxm.id'))
    qdbt_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdbt.id'))
    qdmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdmx.id'))
    qdxdezj_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxdezj.id'))
    qdxdezjmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxdezjmx.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='qdxdercjhl')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='qdxdercjhl')
    file: Mapped[Optional['File']] = relationship('File', back_populates='qdxdercjhl')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qdxdercjhl')
    qdbt: Mapped[Optional['Qdbt']] = relationship('Qdbt', back_populates='qdxdercjhl')
    qdmx: Mapped[Optional['Qdmx']] = relationship('Qdmx', back_populates='qdxdercjhl')
    qdxdezj: Mapped[Optional['Qdxdezj']] = relationship('Qdxdezj', back_populates='qdxdercjhl')
    qdxdezjmx: Mapped[Optional['Qdxdezjmx']] = relationship('Qdxdezjmx', back_populates='qdxdercjhl')
    qdxm: Mapped[Optional['Qdxm']] = relationship('Qdxm', back_populates='qdxdercjhl')
    qdxdercjhlmx: Mapped[List['Qdxdercjhlmx']] = relationship('Qdxdercjhlmx', back_populates='qdxdercjhl')


class Csxdercjhlmx(db.Model):
    __tablename__ = 'origin_13jt_csxdercjhlmx'
    __table_args__ = (
        Index('ix_csxdercjhlmx_create_time', 'create_time'),
        Index('ix_csxdercjhlmx_csxdercjhl_id', 'csxdercjhl_id'),
        Index('ix_csxdercjhlmx_csxdezj_id', 'csxdezj_id'),
        Index('ix_csxdercjhlmx_csxdezjmx_id', 'csxdezjmx_id'),
        Index('ix_csxdercjhlmx_csxm_id', 'csxm_id'),
        Index('ix_csxdercjhlmx_djcs_id', 'djcs_id'),
        Index('ix_csxdercjhlmx_djcsmx_id', 'djcsmx_id'),
        Index('ix_csxdercjhlmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_csxdercjhlmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_csxdercjhlmx_file_id', 'file_id'),
        Index('ix_csxdercjhlmx_id', 'id'),
        Index('ix_csxdercjhlmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_csxdercjhlmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    rcjid: Mapped[Optional[str]] = mapped_column(String(100))
    rcjhl: Mapped[Optional[str]] = mapped_column(String(100))
    rcjhj: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    csxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxm.id'))
    djcs_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcs.id'))
    djcsmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_djcsmx.id'))
    csxdezj_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxdezj.id'))
    csxdezjmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxdezjmx.id'))
    csxdercjhl_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_csxdercjhl.id'))

    csxdercjhl: Mapped[Optional['Csxdercjhl']] = relationship('Csxdercjhl', back_populates='csxdercjhlmx')
    csxdezj: Mapped[Optional['Csxdezj']] = relationship('Csxdezj', back_populates='csxdercjhlmx')
    csxdezjmx: Mapped[Optional['Csxdezjmx']] = relationship('Csxdezjmx', back_populates='csxdercjhlmx')
    csxm: Mapped[Optional['Csxm']] = relationship('Csxm', back_populates='csxdercjhlmx')
    djcs: Mapped[Optional['Djcs']] = relationship('Djcs', back_populates='csxdercjhlmx')
    djcsmx: Mapped[Optional['Djcsmx']] = relationship('Djcsmx', back_populates='csxdercjhlmx')
    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='csxdercjhlmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='csxdercjhlmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='csxdercjhlmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='csxdercjhlmx')


class Qdxdercjhlmx(db.Model):
    __tablename__ = 'origin_13jt_qdxdercjhlmx'
    __table_args__ = (
        Index('ix_qdxdercjhlmx_create_time', 'create_time'),
        Index('ix_qdxdercjhlmx_dwgcxx_id', 'dwgcxx_id'),
        Index('ix_qdxdercjhlmx_dxgcxx_id', 'dxgcxx_id'),
        Index('ix_qdxdercjhlmx_file_id', 'file_id'),
        Index('ix_qdxdercjhlmx_id', 'id'),
        Index('ix_qdxdercjhlmx_jingjibiao_id', 'jingjibiao_id'),
        Index('ix_qdxdercjhlmx_qdbt_id', 'qdbt_id'),
        Index('ix_qdxdercjhlmx_qdmx_id', 'qdmx_id'),
        Index('ix_qdxdercjhlmx_qdxdercjhl_id', 'qdxdercjhl_id'),
        Index('ix_qdxdercjhlmx_qdxdezj_id', 'qdxdezj_id'),
        Index('ix_qdxdercjhlmx_qdxdezjmx_id', 'qdxdezjmx_id'),
        Index('ix_qdxdercjhlmx_qdxm_id', 'qdxm_id'),
        Index('ix_qdxdercjhlmx_update_time', 'update_time')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    create_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    update_time: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    rcjid: Mapped[Optional[str]] = mapped_column(String(100))
    rcjhl: Mapped[Optional[str]] = mapped_column(String(100))
    rcjhj: Mapped[Optional[str]] = mapped_column(String(100))
    file_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_file.id'))
    jingjibiao_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_jingjibiao.id'))
    dxgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dxgcxx.id'))
    dwgcxx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_dwgcxx.id'))
    qdxm_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxm.id'))
    qdbt_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdbt.id'))
    qdmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdmx.id'))
    qdxdezj_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxdezj.id'))
    qdxdezjmx_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxdezjmx.id'))
    qdxdercjhl_id: Mapped[Optional[int]] = mapped_column(ForeignKey('origin_13jt_qdxdercjhl.id'))

    dwgcxx: Mapped[Optional['Dwgcxx']] = relationship('Dwgcxx', back_populates='qdxdercjhlmx')
    dxgcxx: Mapped[Optional['Dxgcxx']] = relationship('Dxgcxx', back_populates='qdxdercjhlmx')
    file: Mapped[Optional['File']] = relationship('File', back_populates='qdxdercjhlmx')
    jingjibiao: Mapped[Optional['Jingjibiao']] = relationship('Jingjibiao', back_populates='qdxdercjhlmx')
    qdbt: Mapped[Optional['Qdbt']] = relationship('Qdbt', back_populates='qdxdercjhlmx')
    qdmx: Mapped[Optional['Qdmx']] = relationship('Qdmx', back_populates='qdxdercjhlmx')
    qdxdercjhl: Mapped[Optional['Qdxdercjhl']] = relationship('Qdxdercjhl', back_populates='qdxdercjhlmx')
    qdxdezj: Mapped[Optional['Qdxdezj']] = relationship('Qdxdezj', back_populates='qdxdercjhlmx')
    qdxdezjmx: Mapped[Optional['Qdxdezjmx']] = relationship('Qdxdezjmx', back_populates='qdxdercjhlmx')
    qdxm: Mapped[Optional['Qdxm']] = relationship('Qdxm', back_populates='qdxdercjhlmx')
