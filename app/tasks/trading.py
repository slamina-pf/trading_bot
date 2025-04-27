# app/tasks/trading.py
from app.celery_worker import celery_app
from datetime import datetime
from helpers.connections import redis_server

@celery_app.task
def trading_task():
    bot_active = redis_server.get('bot_active')
    if bot_active == b'true':
        return {"message": "Trading bot is active."}
    else:
        return {"message": "Trading bot is not active."}

