docker run -d \
--platform linux/amd64 \
--name coin_night_market \
-p 8000:80 \
-e db_host=mysql02:3306 \
-e db_user=root \
-e db_password=123456 \
--link mysql02 \
coin_night_market_image 