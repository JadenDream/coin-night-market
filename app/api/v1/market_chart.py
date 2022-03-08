import string
from fastapi import APIRouter
import json
from models.database import get_db_session
from crud.price_history import get_price_historys
from extension.alchemy_encoder import AlchemyEncoder

router = APIRouter()

@router.get('/market_chart/{id}/range', summary="市場圖表數據")
def get_market_chart_by_id(id:str="ETHUSD", start_date:str="2021/11/1", end_date:str="2021/11/3"):
    db_session = next(get_db_session())
    data = get_price_historys(db_session, id=id, start_date=start_date, end_date=end_date)
    data2 = json.dumps(data, cls=AlchemyEncoder)
    return data2

