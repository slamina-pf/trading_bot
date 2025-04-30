from fastapi import APIRouter
from app.helpers.connections import redis_server

router = APIRouter()

@router.get("/bot-activate")
def get_users():
    redis_server.set('bot_active', 'true')
    return {"message": "Trading bot started"}