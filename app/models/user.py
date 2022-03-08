from sqlalchemy import Boolean, Column, Integer, String
from .database import Base

class User(Base):
    # create __tablename__ attribute，宣告 model 對應的 database table name
    __tablename__ = "users"
    # create class attribute，宣告 model 對應的 table field/column
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(55), index=True) 
    email = Column(String(125), unique=True)
    active = Column(Boolean, default=True)


