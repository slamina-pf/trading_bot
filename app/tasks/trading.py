from app.celery_worker import celery_app
from datetime import datetime
from app.helpers.connections import redis_server

@celery_app.task
def random_forest_5m_task(name="app.tasks.trading.random_forest_5m_task"):
    bot_active = redis_server.get('bot_active')
    if bot_active:
        print(f"Trading task executed at {datetime.now()}")

