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
### 一般
    uvicorn app.main:app --reload
    # --reload 在專案更新時，自動重新載入，類似Flask的debug模式
### use docker
    sudo ./build_amd64_docker.sh
    ./run_amd64_docker.sh
環境為 m1 mac 故採用amd64 的平台環境
### 瀏覽使用
啟動後即可從以下網址看到所有 api 文件
    http://127.0.0.1:8000/docs
