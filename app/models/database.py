from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+pymysql://root:123456@127.0.0.1:3306/testdemo"
Engine = create_engine(DB_URL, echo=True)
# 由於 session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
# 建立 Base，作為後續建立 ORM model 時需要繼承的對象
Base = declarative_base()

# 建立 get_db_session() 並實現一個 database session instance and yield it
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()