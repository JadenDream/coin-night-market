# coin-night-market
 提供幣圈商品歷史價格走勢資訊的api服務


## 套件安裝
### pip3
    pip3 install sqlalchemy
    pip3 install pymysql

### conda
    conda install -c anaconda sqlalchemy
    conda install -c anaconda pymysq

## 運行服務
    uvicorn app.main:app --reload
    # --reload 在專案更新時，自動重新載入，類似Flask的debug模式

啟動後即可從以下網址看到所有 api 文件
    http://127.0.0.1:8000/docs
