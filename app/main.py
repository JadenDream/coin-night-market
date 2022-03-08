from fastapi import FastAPI
from api.v1 import market_chart, user
from models.database import DB_URL


app = FastAPI()

print(f"db-url:{DB_URL}")

app.include_router(market_chart.router, 
    prefix='/v1',
    tags=['coin'],
    responses={520: {"description": "I'm a market_chart description!"}}
    )
app.include_router(user.router, 
    prefix='/v1',
    tags=['user'],
    responses={520: {"description": "I'm a user description!"}}
    )

    