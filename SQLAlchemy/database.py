from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text, String
from config import settings
from typing import Annotated

engine = create_engine(url=settings.DATABASE_URL_pyodbc, echo=True, pool_size=5, max_overflow=10)

sync_session = sessionmaker(engine)

str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    type_annotation_map: {
        str_256: String(256)
    }