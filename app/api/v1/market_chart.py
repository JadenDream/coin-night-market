from fastapi import APIRouter

router = APIRouter()

@router.get('/market_chart/{id}', summary="市場圖表數據")
def get_market_chart_by_id(id: int):
    return {
        'id': id
    }
