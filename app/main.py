from fastapi import FastAPI
from api.v1 import market_chart, user


app = FastAPI()

app.include_router(market_chart.router, 
    prefix='/vi',
    tags=['coin'],
    responses={520: {"description": "I'm a market_chart description!"}}
    )
app.include_router(user.router, 
    prefix='/vi',
    tags=['user'],
    responses={520: {"description": "I'm a user description!"}}
    )

    