from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, text, BigInteger
from database import Base, str_256
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated
import enum
from datetime import datetime
import pandas as pd

metadata_obj = MetaData()

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("GETUTCDATE()"))]
updated_at = Annotated[datetime, mapped_column(server_default=text("GETUTCDATE()"), onupdate=datetime.utcnow)]

class Workload(enum.Enum):
    parttime = 'parttime'
    fulltime = 'fulltime'






class WorkersOrm(Base):
    __tablename__ = 'workers'
    # id: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[intpk]
    username: Mapped[str]

class TestTable(Base):
    __tablename__ = 'test_table'
    id: Mapped[intpk]
    column1: Mapped[str]
    column2: Mapped[int]
    column3: Mapped[int]


class MagnitCategory(Base):
    __tablename__ = 'magnit_category'
    
    id_key: Mapped[intpk]
    id: Mapped[int] = mapped_column(BigInteger)
    tk1: Mapped[str]
    tk2: Mapped[str|None]
    tk3: Mapped[str|None]
    id1: Mapped[int]
    id2: Mapped[int|None]
    id3: Mapped[int|None]











class ResumesOrm(Base):
    __tablename__ = 'resumes'

    id: Mapped[intpk]
    title: Mapped[str_256]
    # compensation: Mapped[int] = mapped_column(nullable=True)
    compensation: Mapped[int|None]
    workload: Mapped[Workload]
    # worker_id: Mapped[int] = mapped_column(ForeignKey(WorkersOrm.id))
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers.id', ondelete='CASCADE'))
    # created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]