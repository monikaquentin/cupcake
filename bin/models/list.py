from sqlalchemy import Boolean, Column, Integer, String

from bin.databases.index import Base


class List(Base):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete = Column(Boolean, default=False)
