# app/celery_worker.py
from celery import Celery

celery_app = Celery(
    "trading-bot",
    broker="redis://localhost:6379/0",  # Same Redis as FastAPI
    backend="redis://localhost:6379/0",
)

celery_app.autodiscover_tasks(["app.tasks.trading"])
