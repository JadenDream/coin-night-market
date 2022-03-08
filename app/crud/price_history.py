import string
from sqlalchemy.orm import Session
from models.price_history import PriceHistory

# 指定查詢符合 User.id 的 user table 資料
def get_price_historys(db: Session, id:str, start_date:str="2021/11/1", end_date:str="2021/11/30"):
    return db.query(PriceHistory).filter(PriceHistory.symbol == id).\
        filter(PriceHistory.date.between(start_date, end_date)).all()


