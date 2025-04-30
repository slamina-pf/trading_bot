from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "trading-bot",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

celery_app.autodiscover_tasks(["app.tasks.trading"])

celery_app.conf.beat_schedule = {
    'run-trading-task-every-5-minutes': {
        'task': 'app.tasks.trading.trading_task',
        'schedule': crontab(minute='*/1'), 
    },
}

celery_app.conf.timezone = 'UTC' 