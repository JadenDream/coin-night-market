# coin-night-market
提供(虛擬幣/股票)商品歷史價格走勢資訊的api服務
主要拿來練習 python + fastapi + sqlalchemy

## 運行前說明
需要準備一個mysql,以供查詢對應歷史價格資訊,並將以下sql匯入資料庫
tools/testdemo_2022-03-08.sql
並在 .env 中設定對應資料庫資訊
docker 則是在 run_amd64_docker.sh 中設定


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
