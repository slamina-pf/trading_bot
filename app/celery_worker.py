from app.celery_app import celery_app
from celery.schedules import crontab

celery_app.conf.beat_schedule = {
    'run-trading-task-every-5-minutes': {
        'task': 'app.tasks.trading.random_forest_5m_task',
        'schedule': crontab(minute='*/1'), 
    },
}