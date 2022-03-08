#%%
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine_url = "mysql+pymysql://root:123456@127.0.0.1:3306/testdemo"
engine = create_engine(engine_url, echo=True)

#%%
from sqlalchemy import Column
from sqlalchemy import Integer, String, DATETIME
class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(55))
    time = Column(DATETIME)

def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)

def transform_date(self, date):
    y, m, d = date.split('/')
    return str(int(y)+1911) + '/' + m  + '/' + d  #民國轉西元

def transform_data(self, data):
    data[0] = datetime.datetime.strptime(self.transform_date(data[0]), '%Y/%m/%d')
    return data

    

#%%
if __name__ == '__main__':
    drop_table()
    create_table()

# %%
