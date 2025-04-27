from fastapi import FastAPI
from endpoints import trading

app = FastAPI()

app.include_router(trading.router)  # Add the router
