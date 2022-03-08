
#%%
# 載入資料並且正確轉換日期格式
import pandas as pd

filename = 'tools/datas/ETHUSD_2021_all.csv'
df = pd.read_csv(filename)

# 日期欄位處理 string to date
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d %H:%M:%S%z")

df.tail(5)

#%%
# 寫入至mysql
from sqlalchemy import create_engine

engine_url = "mysql+pymysql://root:123456@127.0.0.1:3306/testdemo"
engine = create_engine(engine_url, echo=True)

df.to_sql(name='price_history', con=engine, if_exists = 'append', index=False)

