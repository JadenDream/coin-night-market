# import database session 定義 function parameter 的型別
from sqlalchemy.orm import Session
from models.database import Base
from models.user import User

# 指定查詢符合 User.id 的 user table 資料
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# 查詢所有 user 資料，並限制每次查詢數量
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_table(db: Session):
    Base.metadata.create_all(db)

def drop_table(db: Session):
    Base.metadata.drop_all(db)

# 建立 user table 資料
def craete(db: Session):
    # 轉化 pydantic model to orm model
    created_user = User()
    # add instance object into database session
    # 增加 user orm model 所建立的 instance 到 database session
    db.add(created_user)
    # 提交 transaction to database (該 instance 會確實保存在 database)
    db.commit()
    # refresh instance (從 database 抽取該 instance 資料)
    db.refresh(created_user)