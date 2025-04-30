from app.celery_worker import celery_app
from datetime import datetime
from app.helpers.connections import redis_server

@celery_app.task
def trading_task(name="app.tasks.trading.trading_task"):
    bot_active = redis_server.get('bot_active')
    if bot_active == b'true':
        print(f"Trading task executed at {datetime.now()}")
    else:
        print(f"Trading task not executed at {datetime.now()}")

