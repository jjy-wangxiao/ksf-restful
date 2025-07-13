from typing import Optional

from sqlalchemy import Date, Float, Index, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

class Base(DeclarativeBase):
    pass


class Dw(Base):
    __tablename__ = 'dw'
    __table_args__ = (
        Index('ix_dw_dw', 'dw'),
        Index('ix_dw_dw_desc', 'dw_desc')
    )

    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    dw: Mapped[Optional[str]] = mapped_column(String(20))
    dw_desc: Mapped[Optional[str]] = mapped_column(String(255))


class L100(Base):
    __tablename__ = 'l1_00'
    __table_args__ = (
        Index('ix_l1_00_bjsj', 'bjsj'),
        Index('ix_l1_00_ejflid', 'ejflid'),
        Index('ix_l1_00_ejflmc', 'ejflmc'),
        Index('ix_l1_00_id', 'id'),
        Index('ix_l1_00_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_00_rcjdj', 'rcjdj'),
        Index('ix_l1_00_rcjdw', 'rcjdw'),
        Index('ix_l1_00_rcjmc', 'rcjmc'),
        Index('ix_l1_00_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0306: Mapped[Optional[str]] = mapped_column(String(30))


class L101(Base):
    __tablename__ = 'l1_01'
    __table_args__ = (
        Index('ix_l1_01_bjsj', 'bjsj'),
        Index('ix_l1_01_ejflid', 'ejflid'),
        Index('ix_l1_01_ejflmc', 'ejflmc'),
        Index('ix_l1_01_id', 'id'),
        Index('ix_l1_01_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_01_rcjdj', 'rcjdj'),
        Index('ix_l1_01_rcjdw', 'rcjdw'),
        Index('ix_l1_01_rcjmc', 'rcjmc'),
        Index('ix_l1_01_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0591: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0625: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0328: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0781: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0254: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0456: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0367: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0490: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0736: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0352: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0626: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0454: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0275: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0270: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0753: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0338: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0765: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0744: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0137: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0852: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0768: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0271: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0748: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0756: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0188: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0716: Mapped[Optional[str]] = mapped_column(String(30))


class L102(Base):
    __tablename__ = 'l1_02'
    __table_args__ = (
        Index('ix_l1_02_bjsj', 'bjsj'),
        Index('ix_l1_02_ejflid', 'ejflid'),
        Index('ix_l1_02_ejflmc', 'ejflmc'),
        Index('ix_l1_02_id', 'id'),
        Index('ix_l1_02_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_02_rcjdj', 'rcjdj'),
        Index('ix_l1_02_rcjdw', 'rcjdw'),
        Index('ix_l1_02_rcjmc', 'rcjmc'),
        Index('ix_l1_02_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0338: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0129: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0353: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0389: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0068: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0737: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0839: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0349: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))


class L103(Base):
    __tablename__ = 'l1_03'
    __table_args__ = (
        Index('ix_l1_03_bjsj', 'bjsj'),
        Index('ix_l1_03_ejflid', 'ejflid'),
        Index('ix_l1_03_ejflmc', 'ejflmc'),
        Index('ix_l1_03_id', 'id'),
        Index('ix_l1_03_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_03_rcjdj', 'rcjdj'),
        Index('ix_l1_03_rcjdw', 'rcjdw'),
        Index('ix_l1_03_rcjmc', 'rcjmc'),
        Index('ix_l1_03_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0339: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0328: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0361: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0591: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0626: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0135: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0625: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0327: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0888: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0887: Mapped[Optional[str]] = mapped_column(String(30))


class L104(Base):
    __tablename__ = 'l1_04'
    __table_args__ = (
        Index('ix_l1_04_bjsj', 'bjsj'),
        Index('ix_l1_04_ejflid', 'ejflid'),
        Index('ix_l1_04_ejflmc', 'ejflmc'),
        Index('ix_l1_04_id', 'id'),
        Index('ix_l1_04_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_04_rcjdj', 'rcjdj'),
        Index('ix_l1_04_rcjdw', 'rcjdw'),
        Index('ix_l1_04_rcjmc', 'rcjmc'),
        Index('ix_l1_04_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0328: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0119: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0022: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0364: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0577: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0018: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0664: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0209: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0120: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0761: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0032: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0108: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0171: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0739: Mapped[Optional[str]] = mapped_column(String(30))


class L105(Base):
    __tablename__ = 'l1_05'
    __table_args__ = (
        Index('ix_l1_05_bjsj', 'bjsj'),
        Index('ix_l1_05_ejflid', 'ejflid'),
        Index('ix_l1_05_ejflmc', 'ejflmc'),
        Index('ix_l1_05_id', 'id'),
        Index('ix_l1_05_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_05_rcjdj', 'rcjdj'),
        Index('ix_l1_05_rcjdw', 'rcjdw'),
        Index('ix_l1_05_rcjmc', 'rcjmc'),
        Index('ix_l1_05_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0477: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0337: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0860: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0596: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0777: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0222: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0270: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0861: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0338: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0652: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0936: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0762: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0871: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0463: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0740: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0754: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0135: Mapped[Optional[str]] = mapped_column(String(30))


class L106(Base):
    __tablename__ = 'l1_06'
    __table_args__ = (
        Index('ix_l1_06_bjsj', 'bjsj'),
        Index('ix_l1_06_ejflid', 'ejflid'),
        Index('ix_l1_06_ejflmc', 'ejflmc'),
        Index('ix_l1_06_id', 'id'),
        Index('ix_l1_06_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_06_rcjdj', 'rcjdj'),
        Index('ix_l1_06_rcjdw', 'rcjdw'),
        Index('ix_l1_06_rcjmc', 'rcjmc'),
        Index('ix_l1_06_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0338: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0711: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0709: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0710: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0006: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0499: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0708: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0007: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0307: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0757: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0856: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0746: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0728: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0107: Mapped[Optional[str]] = mapped_column(String(30))


class L107(Base):
    __tablename__ = 'l1_07'
    __table_args__ = (
        Index('ix_l1_07_bjsj', 'bjsj'),
        Index('ix_l1_07_ejflid', 'ejflid'),
        Index('ix_l1_07_ejflmc', 'ejflmc'),
        Index('ix_l1_07_id', 'id'),
        Index('ix_l1_07_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_07_rcjdj', 'rcjdj'),
        Index('ix_l1_07_rcjdw', 'rcjdw'),
        Index('ix_l1_07_rcjmc', 'rcjmc'),
        Index('ix_l1_07_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0757: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0890: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0777: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0725: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0703: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0373: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0477: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0389: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0230: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0440: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0605: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0374: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0463: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0596: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0733: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0338: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0726: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0704: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0935: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0195: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0701: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0092: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0093: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0673: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0868: Mapped[Optional[str]] = mapped_column(String(30))


class L108(Base):
    __tablename__ = 'l1_08'
    __table_args__ = (
        Index('ix_l1_08_bjsj', 'bjsj'),
        Index('ix_l1_08_ejflid', 'ejflid'),
        Index('ix_l1_08_ejflmc', 'ejflmc'),
        Index('ix_l1_08_id', 'id'),
        Index('ix_l1_08_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_08_rcjdj', 'rcjdj'),
        Index('ix_l1_08_rcjdw', 'rcjdw'),
        Index('ix_l1_08_rcjmc', 'rcjmc'),
        Index('ix_l1_08_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0173: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0757: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0725: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0018: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0841: Mapped[Optional[str]] = mapped_column(String(30))


class L109(Base):
    __tablename__ = 'l1_09'
    __table_args__ = (
        Index('ix_l1_09_bjsj', 'bjsj'),
        Index('ix_l1_09_ejflid', 'ejflid'),
        Index('ix_l1_09_ejflmc', 'ejflmc'),
        Index('ix_l1_09_id', 'id'),
        Index('ix_l1_09_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_09_rcjdj', 'rcjdj'),
        Index('ix_l1_09_rcjdw', 'rcjdw'),
        Index('ix_l1_09_rcjmc', 'rcjmc'),
        Index('ix_l1_09_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0757: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0338: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0936: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0477: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0777: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0867: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0596: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0275: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0697: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0093: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0725: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0758: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0751: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0863: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0950: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0876: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0251: Mapped[Optional[str]] = mapped_column(String(30))


class L110(Base):
    __tablename__ = 'l1_10'
    __table_args__ = (
        Index('ix_l1_10_bjsj', 'bjsj'),
        Index('ix_l1_10_ejflid', 'ejflid'),
        Index('ix_l1_10_ejflmc', 'ejflmc'),
        Index('ix_l1_10_id', 'id'),
        Index('ix_l1_10_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_10_rcjdj', 'rcjdj'),
        Index('ix_l1_10_rcjdw', 'rcjdw'),
        Index('ix_l1_10_rcjmc', 'rcjmc'),
        Index('ix_l1_10_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0421: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0419: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0861: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0270: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0420: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0760: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0477: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0576: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0418: Mapped[Optional[str]] = mapped_column(String(30))


class L111(Base):
    __tablename__ = 'l1_11'
    __table_args__ = (
        Index('ix_l1_11_bjsj', 'bjsj'),
        Index('ix_l1_11_ejflid', 'ejflid'),
        Index('ix_l1_11_ejflmc', 'ejflmc'),
        Index('ix_l1_11_id', 'id'),
        Index('ix_l1_11_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_11_rcjdj', 'rcjdj'),
        Index('ix_l1_11_rcjdw', 'rcjdw'),
        Index('ix_l1_11_rcjmc', 'rcjmc'),
        Index('ix_l1_11_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0872: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0937: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0477: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0321: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0868: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0338: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0601: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0759: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0647: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0307: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0599: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0165: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0484: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0249: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0126: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0607: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0108: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0024: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0927: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0243: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0780: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0779: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0411: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0102: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0135: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0777: Mapped[Optional[str]] = mapped_column(String(30))


class L112(Base):
    __tablename__ = 'l1_12'
    __table_args__ = (
        Index('ix_l1_12_bjsj', 'bjsj'),
        Index('ix_l1_12_ejflid', 'ejflid'),
        Index('ix_l1_12_ejflmc', 'ejflmc'),
        Index('ix_l1_12_id', 'id'),
        Index('ix_l1_12_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_12_rcjdj', 'rcjdj'),
        Index('ix_l1_12_rcjdw', 'rcjdw'),
        Index('ix_l1_12_rcjmc', 'rcjmc'),
        Index('ix_l1_12_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0477: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0750: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0596: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0777: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0458: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0757: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0111: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0657: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0311: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0685: Mapped[Optional[str]] = mapped_column(String(30))


class L113(Base):
    __tablename__ = 'l1_13'
    __table_args__ = (
        Index('ix_l1_13_bjsj', 'bjsj'),
        Index('ix_l1_13_ejflid', 'ejflid'),
        Index('ix_l1_13_ejflmc', 'ejflmc'),
        Index('ix_l1_13_id', 'id'),
        Index('ix_l1_13_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_13_rcjdj', 'rcjdj'),
        Index('ix_l1_13_rcjdw', 'rcjdw'),
        Index('ix_l1_13_rcjmc', 'rcjmc'),
        Index('ix_l1_13_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0351: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0350: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0652: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0158: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0108: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0596: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0035: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0055: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0595: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0203: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0159: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0305: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0013: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0591: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0707: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0127: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0738: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0450: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0870: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0868: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0122: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))


class L114(Base):
    __tablename__ = 'l1_14'
    __table_args__ = (
        Index('ix_l1_14_bjsj', 'bjsj'),
        Index('ix_l1_14_ejflid', 'ejflid'),
        Index('ix_l1_14_ejflmc', 'ejflmc'),
        Index('ix_l1_14_id', 'id'),
        Index('ix_l1_14_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_14_rcjdj', 'rcjdj'),
        Index('ix_l1_14_rcjdw', 'rcjdw'),
        Index('ix_l1_14_rcjmc', 'rcjmc'),
        Index('ix_l1_14_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0592: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0509: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0949: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0003: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0206: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0719: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0208: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0214: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0596: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0186: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0205: Mapped[Optional[str]] = mapped_column(String(30))


class L115(Base):
    __tablename__ = 'l1_15'
    __table_args__ = (
        Index('ix_l1_15_bjsj', 'bjsj'),
        Index('ix_l1_15_ejflid', 'ejflid'),
        Index('ix_l1_15_ejflmc', 'ejflmc'),
        Index('ix_l1_15_id', 'id'),
        Index('ix_l1_15_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_15_rcjdj', 'rcjdj'),
        Index('ix_l1_15_rcjdw', 'rcjdw'),
        Index('ix_l1_15_rcjmc', 'rcjmc'),
        Index('ix_l1_15_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0757: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0261: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0128: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0262: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0871: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0777: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0091: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0662: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0276: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0275: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0591: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0702: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0089: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0610: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0469: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0700: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))


class L116(Base):
    __tablename__ = 'l1_16'
    __table_args__ = (
        Index('ix_l1_16_bjsj', 'bjsj'),
        Index('ix_l1_16_ejflid', 'ejflid'),
        Index('ix_l1_16_ejflmc', 'ejflmc'),
        Index('ix_l1_16_id', 'id'),
        Index('ix_l1_16_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_16_rcjdj', 'rcjdj'),
        Index('ix_l1_16_rcjdw', 'rcjdw'),
        Index('ix_l1_16_rcjmc', 'rcjmc'),
        Index('ix_l1_16_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0734: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0934: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0135: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0605: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0217: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0722: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0277: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0944: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0435: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0370: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0170: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0211: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0818: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0865: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0291: Mapped[Optional[str]] = mapped_column(String(30))


class L117(Base):
    __tablename__ = 'l1_17'
    __table_args__ = (
        Index('ix_l1_17_bjsj', 'bjsj'),
        Index('ix_l1_17_ejflid', 'ejflid'),
        Index('ix_l1_17_ejflmc', 'ejflmc'),
        Index('ix_l1_17_id', 'id'),
        Index('ix_l1_17_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_17_rcjdj', 'rcjdj'),
        Index('ix_l1_17_rcjdw', 'rcjdw'),
        Index('ix_l1_17_rcjmc', 'rcjmc'),
        Index('ix_l1_17_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0069: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0216: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0582: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0240: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0389: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0655: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0394: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0068: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0514: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0439: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0248: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0741: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0452: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0654: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0061: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0071: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0247: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0814: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0303: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0302: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0051: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0052: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0049: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0062: Mapped[Optional[str]] = mapped_column(String(30))


class L118(Base):
    __tablename__ = 'l1_18'
    __table_args__ = (
        Index('ix_l1_18_bjsj', 'bjsj'),
        Index('ix_l1_18_ejflid', 'ejflid'),
        Index('ix_l1_18_ejflmc', 'ejflmc'),
        Index('ix_l1_18_id', 'id'),
        Index('ix_l1_18_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_18_rcjdj', 'rcjdj'),
        Index('ix_l1_18_rcjdw', 'rcjdw'),
        Index('ix_l1_18_rcjmc', 'rcjmc'),
        Index('ix_l1_18_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0216: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0389: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0069: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0061: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0218: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0272: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0441: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0550: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0068: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0814: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0861: Mapped[Optional[str]] = mapped_column(String(30))


class L119(Base):
    __tablename__ = 'l1_19'
    __table_args__ = (
        Index('ix_l1_19_bjsj', 'bjsj'),
        Index('ix_l1_19_ejflid', 'ejflid'),
        Index('ix_l1_19_ejflmc', 'ejflmc'),
        Index('ix_l1_19_id', 'id'),
        Index('ix_l1_19_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_19_rcjdj', 'rcjdj'),
        Index('ix_l1_19_rcjdw', 'rcjdw'),
        Index('ix_l1_19_rcjmc', 'rcjmc'),
        Index('ix_l1_19_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0864: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0069: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0061: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0273: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0023: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0389: Mapped[Optional[str]] = mapped_column(String(30))


class L120(Base):
    __tablename__ = 'l1_20'
    __table_args__ = (
        Index('ix_l1_20_bjsj', 'bjsj'),
        Index('ix_l1_20_ejflid', 'ejflid'),
        Index('ix_l1_20_ejflmc', 'ejflmc'),
        Index('ix_l1_20_id', 'id'),
        Index('ix_l1_20_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_20_rcjdj', 'rcjdj'),
        Index('ix_l1_20_rcjdw', 'rcjdw'),
        Index('ix_l1_20_rcjmc', 'rcjmc'),
        Index('ix_l1_20_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0069: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0061: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0272: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0202: Mapped[Optional[str]] = mapped_column(String(30))


class L121(Base):
    __tablename__ = 'l1_21'
    __table_args__ = (
        Index('ix_l1_21_bjsj', 'bjsj'),
        Index('ix_l1_21_ejflid', 'ejflid'),
        Index('ix_l1_21_ejflmc', 'ejflmc'),
        Index('ix_l1_21_id', 'id'),
        Index('ix_l1_21_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_21_rcjdj', 'rcjdj'),
        Index('ix_l1_21_rcjdw', 'rcjdw'),
        Index('ix_l1_21_rcjmc', 'rcjmc'),
        Index('ix_l1_21_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0239: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0491: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0181: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0505: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0812: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0087: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0764: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0600: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0943: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0862: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0152: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0108: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0196: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0076: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0077: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0842: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0383: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0811: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0265: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0231: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0106: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0346: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0866: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0069: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0640: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0389: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0864: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0061: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0274: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0538: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0256: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0105: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0488: Mapped[Optional[str]] = mapped_column(String(30))


class L122(Base):
    __tablename__ = 'l1_22'
    __table_args__ = (
        Index('ix_l1_22_bjsj', 'bjsj'),
        Index('ix_l1_22_ejflid', 'ejflid'),
        Index('ix_l1_22_ejflmc', 'ejflmc'),
        Index('ix_l1_22_id', 'id'),
        Index('ix_l1_22_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_22_rcjdj', 'rcjdj'),
        Index('ix_l1_22_rcjdw', 'rcjdw'),
        Index('ix_l1_22_rcjmc', 'rcjmc'),
        Index('ix_l1_22_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0162: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0294: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0242: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0269: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0414: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0724: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0270: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0161: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0106: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0062: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0132: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0408: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0069: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0258: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0033: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0878: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0798: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0436: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0109: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0813: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0061: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0021: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0731: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0653: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0285: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0933: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0873: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0766: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0814: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0868: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0848: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0550: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0924: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0024: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0585: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0326: Mapped[Optional[str]] = mapped_column(String(30))


class L123(Base):
    __tablename__ = 'l1_23'
    __table_args__ = (
        Index('ix_l1_23_bjsj', 'bjsj'),
        Index('ix_l1_23_ejflid', 'ejflid'),
        Index('ix_l1_23_ejflmc', 'ejflmc'),
        Index('ix_l1_23_id', 'id'),
        Index('ix_l1_23_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_23_rcjdj', 'rcjdj'),
        Index('ix_l1_23_rcjdw', 'rcjdw'),
        Index('ix_l1_23_rcjmc', 'rcjmc'),
        Index('ix_l1_23_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0078: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0641: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0554: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0553: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0069: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0061: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0389: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0656: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0659: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0807: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0541: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0513: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0512: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0542: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0638: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0745: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0145: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0119: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0338: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0628: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0281: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0848: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0528: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0526: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0180: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0694: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0342: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0773: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0300: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0615: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0675: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0301: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0895: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0251: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0679: Mapped[Optional[str]] = mapped_column(String(30))


class L124(Base):
    __tablename__ = 'l1_24'
    __table_args__ = (
        Index('ix_l1_24_bjsj', 'bjsj'),
        Index('ix_l1_24_ejflid', 'ejflid'),
        Index('ix_l1_24_ejflmc', 'ejflmc'),
        Index('ix_l1_24_id', 'id'),
        Index('ix_l1_24_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_24_rcjdj', 'rcjdj'),
        Index('ix_l1_24_rcjdw', 'rcjdw'),
        Index('ix_l1_24_rcjmc', 'rcjmc'),
        Index('ix_l1_24_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0069: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0218: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0066: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0067: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0427: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0062: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0814: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0296: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0083: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0204: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0669: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0732: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0537: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0865: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0061: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0536: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0749: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0163: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0147: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0068: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0535: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0533: Mapped[Optional[str]] = mapped_column(String(30))


class L125(Base):
    __tablename__ = 'l1_25'
    __table_args__ = (
        Index('ix_l1_25_bjsj', 'bjsj'),
        Index('ix_l1_25_ejflid', 'ejflid'),
        Index('ix_l1_25_ejflmc', 'ejflmc'),
        Index('ix_l1_25_id', 'id'),
        Index('ix_l1_25_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_25_rcjdj', 'rcjdj'),
        Index('ix_l1_25_rcjdw', 'rcjdw'),
        Index('ix_l1_25_rcjmc', 'rcjmc'),
        Index('ix_l1_25_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0912: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0895: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0567: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0560: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0398: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0056: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0566: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0106: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0019: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0396: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0841: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0571: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0563: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0160: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0558: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0573: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0559: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0865: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0564: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0561: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0572: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0057: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0570: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0556: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0568: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0143: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0415: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0233: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0104: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0251: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0318: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0365: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0001: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0250: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0555: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0608: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0565: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0562: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0557: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0313: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0047: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0314: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0050: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0144: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0682: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0231: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0178: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0569: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0410: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0857: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0793: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0795: Mapped[Optional[str]] = mapped_column(String(30))


class L126(Base):
    __tablename__ = 'l1_26'
    __table_args__ = (
        Index('ix_l1_26_bjsj', 'bjsj'),
        Index('ix_l1_26_ejflid', 'ejflid'),
        Index('ix_l1_26_ejflmc', 'ejflmc'),
        Index('ix_l1_26_id', 'id'),
        Index('ix_l1_26_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_26_rcjdj', 'rcjdj'),
        Index('ix_l1_26_rcjdw', 'rcjdw'),
        Index('ix_l1_26_rcjmc', 'rcjmc'),
        Index('ix_l1_26_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0912: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0914: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0236: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0317: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0874: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0819: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0895: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0237: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0316: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0893: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0399: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0618: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0650: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0353: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0881: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0405: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0235: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0403: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0238: Mapped[Optional[str]] = mapped_column(String(30))


class L127(Base):
    __tablename__ = 'l1_27'
    __table_args__ = (
        Index('ix_l1_27_bjsj', 'bjsj'),
        Index('ix_l1_27_ejflid', 'ejflid'),
        Index('ix_l1_27_ejflmc', 'ejflmc'),
        Index('ix_l1_27_id', 'id'),
        Index('ix_l1_27_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_27_rcjdj', 'rcjdj'),
        Index('ix_l1_27_rcjdw', 'rcjdw'),
        Index('ix_l1_27_rcjmc', 'rcjmc'),
        Index('ix_l1_27_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0912: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0584: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0583: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0834: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0065: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0064: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0393: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0715: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0914: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0903: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0916: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0909: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0163: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0911: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0329: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0850: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0907: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0444: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0443: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0308: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0309: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0253: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0174: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0506: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0120: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0699: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0698: Mapped[Optional[str]] = mapped_column(String(30))


class L128(Base):
    __tablename__ = 'l1_28'
    __table_args__ = (
        Index('ix_l1_28_bjsj', 'bjsj'),
        Index('ix_l1_28_ejflid', 'ejflid'),
        Index('ix_l1_28_ejflmc', 'ejflmc'),
        Index('ix_l1_28_id', 'id'),
        Index('ix_l1_28_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_28_rcjdj', 'rcjdj'),
        Index('ix_l1_28_rcjdw', 'rcjdw'),
        Index('ix_l1_28_rcjmc', 'rcjmc'),
        Index('ix_l1_28_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0769: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0721: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0471: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0677: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0125: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0353: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0911: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0692: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0369: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0304: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0298: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0241: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0072: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0416: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0470: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0473: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0073: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0058: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0112: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0059: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0060: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0292: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0912: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0279: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0278: Mapped[Optional[str]] = mapped_column(String(30))


class L129(Base):
    __tablename__ = 'l1_29'
    __table_args__ = (
        Index('ix_l1_29_bjsj', 'bjsj'),
        Index('ix_l1_29_ejflid', 'ejflid'),
        Index('ix_l1_29_ejflmc', 'ejflmc'),
        Index('ix_l1_29_id', 'id'),
        Index('ix_l1_29_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_29_rcjdj', 'rcjdj'),
        Index('ix_l1_29_rcjdw', 'rcjdw'),
        Index('ix_l1_29_rcjmc', 'rcjmc'),
        Index('ix_l1_29_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0455: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0752: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0216: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0485: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0676: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0494: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0231: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0865: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0914: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0047: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0672: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0611: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0721: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0830: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0039: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0255: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0280: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0686: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0251: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0338: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0826: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0824: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0825: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0823: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0821: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0822: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0833: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0831: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0832: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0486: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0609: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0250: Mapped[Optional[str]] = mapped_column(String(30))


class L130(Base):
    __tablename__ = 'l1_30'
    __table_args__ = (
        Index('ix_l1_30_bjsj', 'bjsj'),
        Index('ix_l1_30_ejflid', 'ejflid'),
        Index('ix_l1_30_ejflmc', 'ejflmc'),
        Index('ix_l1_30_id', 'id'),
        Index('ix_l1_30_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_30_rcjdj', 'rcjdj'),
        Index('ix_l1_30_rcjdw', 'rcjdw'),
        Index('ix_l1_30_rcjmc', 'rcjmc'),
        Index('ix_l1_30_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0138: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0874: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0882: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0404: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0620: Mapped[Optional[str]] = mapped_column(String(30))


class L131(Base):
    __tablename__ = 'l1_31'
    __table_args__ = (
        Index('ix_l1_31_bjsj', 'bjsj'),
        Index('ix_l1_31_ejflid', 'ejflid'),
        Index('ix_l1_31_ejflmc', 'ejflmc'),
        Index('ix_l1_31_id', 'id'),
        Index('ix_l1_31_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_31_rcjdj', 'rcjdj'),
        Index('ix_l1_31_rcjdw', 'rcjdw'),
        Index('ix_l1_31_rcjmc', 'rcjmc'),
        Index('ix_l1_31_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0332: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0284: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0312: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0674: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0841: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0099: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0038: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0776: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0331: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0632: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0025: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0598: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0737: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0633: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0163: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0151: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0803: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0720: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))


class L132(Base):
    __tablename__ = 'l1_32'
    __table_args__ = (
        Index('ix_l1_32_bjsj', 'bjsj'),
        Index('ix_l1_32_ejflid', 'ejflid'),
        Index('ix_l1_32_ejflmc', 'ejflmc'),
        Index('ix_l1_32_id', 'id'),
        Index('ix_l1_32_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_32_rcjdj', 'rcjdj'),
        Index('ix_l1_32_rcjdw', 'rcjdw'),
        Index('ix_l1_32_rcjmc', 'rcjmc'),
        Index('ix_l1_32_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0177: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0712: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0480: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0192: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0193: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0075: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0602: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0120: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0010: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0121: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0465: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0883: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0194: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0081: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0493: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0191: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0481: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0727: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0476: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0859: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0334: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0467: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0187: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0769: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0189: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0002: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0264: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0190: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0293: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0179: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0527: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0281: Mapped[Optional[str]] = mapped_column(String(30))


class L133(Base):
    __tablename__ = 'l1_33'
    __table_args__ = (
        Index('ix_l1_33_bjsj', 'bjsj'),
        Index('ix_l1_33_ejflid', 'ejflid'),
        Index('ix_l1_33_ejflmc', 'ejflmc'),
        Index('ix_l1_33_id', 'id'),
        Index('ix_l1_33_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_33_rcjdj', 'rcjdj'),
        Index('ix_l1_33_rcjdw', 'rcjdw'),
        Index('ix_l1_33_rcjmc', 'rcjmc'),
        Index('ix_l1_33_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0123: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0288: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0258: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0265: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0767: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0063: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0150: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0836: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0270: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0813: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0594: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))


class L134(Base):
    __tablename__ = 'l1_34'
    __table_args__ = (
        Index('ix_l1_34_bjsj', 'bjsj'),
        Index('ix_l1_34_ejflid', 'ejflid'),
        Index('ix_l1_34_ejflmc', 'ejflmc'),
        Index('ix_l1_34_id', 'id'),
        Index('ix_l1_34_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_34_rcjdj', 'rcjdj'),
        Index('ix_l1_34_rcjdw', 'rcjdw'),
        Index('ix_l1_34_rcjmc', 'rcjmc'),
        Index('ix_l1_34_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0449: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0755: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0348: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0760: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))


class L135(Base):
    __tablename__ = 'l1_35'
    __table_args__ = (
        Index('ix_l1_35_bjsj', 'bjsj'),
        Index('ix_l1_35_ejflid', 'ejflid'),
        Index('ix_l1_35_ejflmc', 'ejflmc'),
        Index('ix_l1_35_id', 'id'),
        Index('ix_l1_35_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_35_rcjdj', 'rcjdj'),
        Index('ix_l1_35_rcjdw', 'rcjdw'),
        Index('ix_l1_35_rcjmc', 'rcjmc'),
        Index('ix_l1_35_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0777: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0596: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0687: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0422: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0333: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0215: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0409: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0861: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0319: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0848: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0548: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0837: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0778: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0468: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0105: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0784: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0297: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0835: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0705: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0912: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0920: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0854: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0320: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0859: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0921: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0474: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0545: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0535: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0534: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0360: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0639: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0855: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0430: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0103: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0608: Mapped[Optional[str]] = mapped_column(String(30))


class L136(Base):
    __tablename__ = 'l1_36'
    __table_args__ = (
        Index('ix_l1_36_bjsj', 'bjsj'),
        Index('ix_l1_36_ejflid', 'ejflid'),
        Index('ix_l1_36_ejflmc', 'ejflmc'),
        Index('ix_l1_36_id', 'id'),
        Index('ix_l1_36_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_36_rcjdj', 'rcjdj'),
        Index('ix_l1_36_rcjdw', 'rcjdw'),
        Index('ix_l1_36_rcjmc', 'rcjmc'),
        Index('ix_l1_36_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0729: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0483: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0696: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0187: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0366: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0407: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0031: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0457: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0648: Mapped[Optional[str]] = mapped_column(String(30))


class L137(Base):
    __tablename__ = 'l1_37'
    __table_args__ = (
        Index('ix_l1_37_bjsj', 'bjsj'),
        Index('ix_l1_37_ejflid', 'ejflid'),
        Index('ix_l1_37_ejflmc', 'ejflmc'),
        Index('ix_l1_37_id', 'id'),
        Index('ix_l1_37_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_37_rcjdj', 'rcjdj'),
        Index('ix_l1_37_rcjdw', 'rcjdw'),
        Index('ix_l1_37_rcjmc', 'rcjmc'),
        Index('ix_l1_37_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0853: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0591: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0344: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0497: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0747: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0861: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0671: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0022: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0498: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0838: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0456: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0139: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0243: Mapped[Optional[str]] = mapped_column(String(30))


class L138(Base):
    __tablename__ = 'l1_38'
    __table_args__ = (
        Index('ix_l1_38_bjsj', 'bjsj'),
        Index('ix_l1_38_ejflid', 'ejflid'),
        Index('ix_l1_38_ejflmc', 'ejflmc'),
        Index('ix_l1_38_id', 'id'),
        Index('ix_l1_38_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_38_rcjdj', 'rcjdj'),
        Index('ix_l1_38_rcjdw', 'rcjdw'),
        Index('ix_l1_38_rcjmc', 'rcjmc'),
        Index('ix_l1_38_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0540: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0164: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0459: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0723: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0074: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0245: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0520: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0591: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0366: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0649: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0525: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0500: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0511: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0327: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))


class L139(Base):
    __tablename__ = 'l1_39'
    __table_args__ = (
        Index('ix_l1_39_bjsj', 'bjsj'),
        Index('ix_l1_39_ejflid', 'ejflid'),
        Index('ix_l1_39_ejflmc', 'ejflmc'),
        Index('ix_l1_39_id', 'id'),
        Index('ix_l1_39_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_39_rcjdj', 'rcjdj'),
        Index('ix_l1_39_rcjdw', 'rcjdw'),
        Index('ix_l1_39_rcjmc', 'rcjmc'),
        Index('ix_l1_39_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0148: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0735: Mapped[Optional[str]] = mapped_column(String(30))


class L140(Base):
    __tablename__ = 'l1_40'
    __table_args__ = (
        Index('ix_l1_40_bjsj', 'bjsj'),
        Index('ix_l1_40_ejflid', 'ejflid'),
        Index('ix_l1_40_ejflmc', 'ejflmc'),
        Index('ix_l1_40_id', 'id'),
        Index('ix_l1_40_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_40_rcjdj', 'rcjdj'),
        Index('ix_l1_40_rcjdw', 'rcjdw'),
        Index('ix_l1_40_rcjmc', 'rcjmc'),
        Index('ix_l1_40_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0283: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0847: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0651: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0889: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0198: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0861: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0681: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0858: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0268: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0134: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0030: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0946: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0492: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0927: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0267: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0774: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0945: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0491: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0266: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0338: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0036: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0325: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0466: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0820: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0482: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0340: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0948: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0593: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0539: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0660: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0295: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0029: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0108: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0357: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0358: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0851: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0356: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0228: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0227: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0229: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0226: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0423: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0347: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0363: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0041: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0037: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0392: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0034: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0637: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0636: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0390: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0221: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0424: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0447: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0446: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0445: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0070: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0220: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0289: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0635: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0355: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0742: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))


class L150(Base):
    __tablename__ = 'l1_50'
    __table_args__ = (
        Index('ix_l1_50_bjsj', 'bjsj'),
        Index('ix_l1_50_ejflid', 'ejflid'),
        Index('ix_l1_50_ejflmc', 'ejflmc'),
        Index('ix_l1_50_id', 'id'),
        Index('ix_l1_50_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_50_rcjdj', 'rcjdj'),
        Index('ix_l1_50_rcjdw', 'rcjdw'),
        Index('ix_l1_50_rcjmc', 'rcjmc'),
        Index('ix_l1_50_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0097: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0101: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0095: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0100: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0094: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0233: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0859: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0269: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0947: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0931: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0713: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0182: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0616: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0016: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0251: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0580: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0079: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0133: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0544: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0597: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0806: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0343: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0246: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0925: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0933: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0849: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0212: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0232: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0244: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0382: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0809: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0260: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0613: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0082: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0521: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0928: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0084: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0929: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0105: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0815: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0375: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0207: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0118: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0114: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0219: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0379: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0294: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0378: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0380: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0808: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0068: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0771: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0460: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0020: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0524: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0864: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0293: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0387: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0786: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0772: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0529: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0085: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0504: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0184: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0930: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0816: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0644: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0401: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0333: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0080: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0799: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0891: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0892: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0920: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0503: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0880: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0183: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0098: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0785: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0156: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0926: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0024: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0131: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0932: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0530: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0130: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0912: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0895: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0153: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0157: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0894: Mapped[Optional[str]] = mapped_column(String(30))


class L151(Base):
    __tablename__ = 'l1_51'
    __table_args__ = (
        Index('ix_l1_51_bjsj', 'bjsj'),
        Index('ix_l1_51_ejflid', 'ejflid'),
        Index('ix_l1_51_ejflmc', 'ejflmc'),
        Index('ix_l1_51_id', 'id'),
        Index('ix_l1_51_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_51_rcjdj', 'rcjdj'),
        Index('ix_l1_51_rcjdw', 'rcjdw'),
        Index('ix_l1_51_rcjmc', 'rcjmc'),
        Index('ix_l1_51_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0530: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0785: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0359: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0606: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0516: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0166: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0381: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0155: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0167: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0413: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0515: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0156: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0517: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0496: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0154: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0507: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0412: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0908: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0919: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0904: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0522: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0523: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0336: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0940: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0787: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0129: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0782: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0805: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0168: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0616: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0612: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0426: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0388: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0642: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0372: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0105: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0532: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0259: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0884: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0233: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0508: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0912: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0172: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0199: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0625: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0695: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0046: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0531: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0012: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0282: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0011: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0294: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0141: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0622: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0914: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0406: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0398: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0345: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0865: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))


class L152(Base):
    __tablename__ = 'l1_52'
    __table_args__ = (
        Index('ix_l1_52_bjsj', 'bjsj'),
        Index('ix_l1_52_ejflid', 'ejflid'),
        Index('ix_l1_52_ejflmc', 'ejflmc'),
        Index('ix_l1_52_id', 'id'),
        Index('ix_l1_52_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_52_rcjdj', 'rcjdj'),
        Index('ix_l1_52_rcjdw', 'rcjdw'),
        Index('ix_l1_52_rcjmc', 'rcjmc'),
        Index('ix_l1_52_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0617: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0914: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0105: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0294: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0265: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0322: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0588: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0578: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0257: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0040: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0804: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0425: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0579: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0543: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0770: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0461: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0462: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0068: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0376: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0377: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0616: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0589: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0590: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0045: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0910: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0896: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0587: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0730: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0690: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0086: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))


class L153(Base):
    __tablename__ = 'l1_53'
    __table_args__ = (
        Index('ix_l1_53_bjsj', 'bjsj'),
        Index('ix_l1_53_ejflid', 'ejflid'),
        Index('ix_l1_53_ejflmc', 'ejflmc'),
        Index('ix_l1_53_id', 'id'),
        Index('ix_l1_53_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_53_rcjdj', 'rcjdj'),
        Index('ix_l1_53_rcjdw', 'rcjdw'),
        Index('ix_l1_53_rcjmc', 'rcjmc'),
        Index('ix_l1_53_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0769: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0807: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0817: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0105: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0294: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0270: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0612: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0333: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0252: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0438: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0068: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0017: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0088: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0298: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0441: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0479: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0478: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0623: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0624: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0223: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0526: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0233: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0827: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0146: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0116: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0797: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0800: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0683: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0142: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0199: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0717: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0785: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0054: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0810: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0224: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0941: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0115: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0547: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0501: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0688: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0626: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0213: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0875: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0865: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0869: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0678: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0828: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0829: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0938: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0546: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0549: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0307: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0113: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0897: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0384: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0090: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0395: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0008: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0009: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0429: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0335: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0495: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0646: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0451: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0663: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0136: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0209: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0665: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0225: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0802: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0801: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0551: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0634: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0341: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0939: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0354: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0877: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0290: Mapped[Optional[str]] = mapped_column(String(30))


class L154(Base):
    __tablename__ = 'l1_54'
    __table_args__ = (
        Index('ix_l1_54_bjsj', 'bjsj'),
        Index('ix_l1_54_ejflid', 'ejflid'),
        Index('ix_l1_54_ejflmc', 'ejflmc'),
        Index('ix_l1_54_id', 'id'),
        Index('ix_l1_54_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_54_rcjdj', 'rcjdj'),
        Index('ix_l1_54_rcjdw', 'rcjdw'),
        Index('ix_l1_54_rcjmc', 'rcjmc'),
        Index('ix_l1_54_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0687: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0616: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0105: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0096: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0437: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0714: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0519: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0310: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0448: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0518: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0538: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0575: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0257: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0488: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0861: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0270: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0948: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0371: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0609: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0574: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0586: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0706: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0233: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0608: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0104: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))


class L155(Base):
    __tablename__ = 'l1_55'
    __table_args__ = (
        Index('ix_l1_55_bjsj', 'bjsj'),
        Index('ix_l1_55_ejflid', 'ejflid'),
        Index('ix_l1_55_ejflmc', 'ejflmc'),
        Index('ix_l1_55_id', 'id'),
        Index('ix_l1_55_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_55_rcjdj', 'rcjdj'),
        Index('ix_l1_55_rcjdw', 'rcjdw'),
        Index('ix_l1_55_rcjmc', 'rcjmc'),
        Index('ix_l1_55_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0845: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0687: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0110: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0912: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0914: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0631: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0899: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0865: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0234: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0433: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0911: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0630: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0685: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0149: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0041: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0658: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0552: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0442: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0691: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0510: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0629: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0689: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0898: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0005: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0669: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0790: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0794: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0796: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0645: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0900: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0775: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0643: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0581: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0117: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0913: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0901: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0124: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0915: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0905: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0464: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0840: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0042: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0902: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0104: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0397: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0627: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0169: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0846: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0400: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0391: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0026: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0027: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0028: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0895: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0475: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0621: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0684: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0894: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0296: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0038: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0472: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0693: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0004: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0015: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0619: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0614: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0783: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0917: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0612: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0792: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0923: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0176: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0791: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))


class L156(Base):
    __tablename__ = 'l1_56'
    __table_args__ = (
        Index('ix_l1_56_bjsj', 'bjsj'),
        Index('ix_l1_56_ejflid', 'ejflid'),
        Index('ix_l1_56_ejflmc', 'ejflmc'),
        Index('ix_l1_56_id', 'id'),
        Index('ix_l1_56_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_56_rcjdj', 'rcjdj'),
        Index('ix_l1_56_rcjdw', 'rcjdw'),
        Index('ix_l1_56_rcjmc', 'rcjmc'),
        Index('ix_l1_56_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0922: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0918: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0014: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0286: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0428: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0789: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0287: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0323: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0324: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0788: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0048: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0886: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0315: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0398: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0885: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0432: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0053: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0402: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0487: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0431: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))


class L157(Base):
    __tablename__ = 'l1_57'
    __table_args__ = (
        Index('ix_l1_57_bjsj', 'bjsj'),
        Index('ix_l1_57_ejflid', 'ejflid'),
        Index('ix_l1_57_ejflmc', 'ejflmc'),
        Index('ix_l1_57_id', 'id'),
        Index('ix_l1_57_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_57_rcjdj', 'rcjdj'),
        Index('ix_l1_57_rcjdw', 'rcjdw'),
        Index('ix_l1_57_rcjmc', 'rcjmc'),
        Index('ix_l1_57_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0385: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0660: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0185: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0603: Mapped[Optional[str]] = mapped_column(String(30))


class L158(Base):
    __tablename__ = 'l1_58'
    __table_args__ = (
        Index('ix_l1_58_bjsj', 'bjsj'),
        Index('ix_l1_58_ejflid', 'ejflid'),
        Index('ix_l1_58_ejflmc', 'ejflmc'),
        Index('ix_l1_58_id', 'id'),
        Index('ix_l1_58_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_58_rcjdj', 'rcjdj'),
        Index('ix_l1_58_rcjdw', 'rcjdw'),
        Index('ix_l1_58_rcjmc', 'rcjmc'),
        Index('ix_l1_58_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0670: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0489: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0140: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0173: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0386: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0299: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0434: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0879: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0906: Mapped[Optional[str]] = mapped_column(String(30))


class L159(Base):
    __tablename__ = 'l1_59'
    __table_args__ = (
        Index('ix_l1_59_bjsj', 'bjsj'),
        Index('ix_l1_59_ejflid', 'ejflid'),
        Index('ix_l1_59_ejflmc', 'ejflmc'),
        Index('ix_l1_59_id', 'id'),
        Index('ix_l1_59_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_59_rcjdj', 'rcjdj'),
        Index('ix_l1_59_rcjdw', 'rcjdw'),
        Index('ix_l1_59_rcjmc', 'rcjmc'),
        Index('ix_l1_59_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0453: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0763: Mapped[Optional[str]] = mapped_column(String(30))


class L180(Base):
    __tablename__ = 'l1_80'
    __table_args__ = (
        Index('ix_l1_80_bjsj', 'bjsj'),
        Index('ix_l1_80_ejflid', 'ejflid'),
        Index('ix_l1_80_ejflmc', 'ejflmc'),
        Index('ix_l1_80_id', 'id'),
        Index('ix_l1_80_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_80_rcjdj', 'rcjdj'),
        Index('ix_l1_80_rcjdw', 'rcjdw'),
        Index('ix_l1_80_rcjmc', 'rcjmc'),
        Index('ix_l1_80_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0328: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0604: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0044: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0843: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0667: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0502: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0210: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0338: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0368: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0942: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0680: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0668: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0330: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0666: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0043: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0718: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0844: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0201: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0200: Mapped[Optional[str]] = mapped_column(String(30))


class L198(Base):
    __tablename__ = 'l1_98'
    __table_args__ = (
        Index('ix_l1_98_bjsj', 'bjsj'),
        Index('ix_l1_98_ejflid', 'ejflid'),
        Index('ix_l1_98_ejflmc', 'ejflmc'),
        Index('ix_l1_98_id', 'id'),
        Index('ix_l1_98_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_98_rcjdj', 'rcjdj'),
        Index('ix_l1_98_rcjdw', 'rcjdw'),
        Index('ix_l1_98_rcjmc', 'rcjmc'),
        Index('ix_l1_98_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))


class L199(Base):
    __tablename__ = 'l1_99'
    __table_args__ = (
        Index('ix_l1_99_bjsj', 'bjsj'),
        Index('ix_l1_99_ejflid', 'ejflid'),
        Index('ix_l1_99_ejflmc', 'ejflmc'),
        Index('ix_l1_99_id', 'id'),
        Index('ix_l1_99_rcj_foreign_id', 'rcj_foreign_id'),
        Index('ix_l1_99_rcjdj', 'rcjdj'),
        Index('ix_l1_99_rcjdw', 'rcjdw'),
        Index('ix_l1_99_rcjmc', 'rcjmc'),
        Index('ix_l1_99_sjflmc', 'sjflmc')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rcj_foreign_id: Mapped[Optional[int]] = mapped_column(Integer)
    rcjmc: Mapped[Optional[str]] = mapped_column(String(255))
    rcjdw: Mapped[Optional[str]] = mapped_column(String(10))
    rcjdj: Mapped[Optional[float]] = mapped_column(Float)
    bjsj: Mapped[Optional[datetime.date]] = mapped_column(Date)
    ejflid: Mapped[Optional[str]] = mapped_column(String(4))
    ejflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sjflmc: Mapped[Optional[str]] = mapped_column(String(50))
    sx_0175: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0417: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0024: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0362: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0128: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0263: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0197: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0743: Mapped[Optional[str]] = mapped_column(String(30))
    sx_0661: Mapped[Optional[str]] = mapped_column(String(30))
