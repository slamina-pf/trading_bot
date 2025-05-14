from fastapi import APIRouter
from app.helpers.connections import redis_server

router = APIRouter()

@router.get("/random_forest_5m/activate")
def get_users():
    redis_server.set('random_forest_5m', 1)
    return {"message": "Trading bot started"}