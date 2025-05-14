from celery import Celery

celery_app = Celery(
    "trading-bot",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=['app.tasks.trading']
)

celery_app.conf.timezone = 'UTC'