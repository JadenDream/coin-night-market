import json
from fastapi import APIRouter
from models.database import get_db_session
from crud.user import get_user
from extension.alchemy_encoder import AlchemyEncoder

router = APIRouter()

@router.get('/user/{user_id}')
def get_book_by_id(user_id: int):
    # 取得 database session instance，這邊，
    db_session = next(get_db_session())
    # 執行 database query，並回傳 User model
    user = get_user(db_session, user_id=user_id)
    return json.dumps(user, cls=AlchemyEncoder)
