from fastapi import FastAPI
from app.endpoints import trading

app = FastAPI()

app.include_router(trading.router)  # Add the router
