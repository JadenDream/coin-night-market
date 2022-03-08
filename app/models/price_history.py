from sqlalchemy import Column, String, DateTime, Float, TIMESTAMP
from .database import Base

class PriceHistory(Base):
    # create __tablename__ attribute，宣告 model 對應的 database table name
    __tablename__ = "price_history"
    # create class attribute，宣告 model 對應的 table field/column
    symbol = Column(String(16), primary_key=True) 
    date = Column(DateTime, primary_key=True, index=True)
    close = Column(Float) 
    high = Column(Float)
    low = Column(Float)
    open = Column(Float)
    volume = Column(Float)
    adjClose = Column(Float)
    adjHigh = Column(Float)
    adjLow = Column(Float)
    adjOpen = Column(Float)
    adjVolume = Column(Float)
    divCash = Column(Float)
    splitFactor = Column(Float)

