from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.ext.declarative import declarative_base

class User(Base):
    # create __tablename__ attribute，宣告 model 對應的 database table name
    __tablename__ = "users"
    # create class attribute，宣告 model 對應的 table field/column
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(55), index=True) 
    email = Column(String(125), unique=True)
    active = Column(Boolean, default=True)
    # create relationship 建立 Table 關聯


