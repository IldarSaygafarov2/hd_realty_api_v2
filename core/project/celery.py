import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.project.settings")

celery_app = Celery("project")

celery_app.conf.beat_schedule = {
    "get-currency-rate-every-day-at-9": {
        "task": "core.apps.advertisements.tasks.get_todays_currency_rate",
        "schedule": 60.0,
    },
}

celery_app.config_from_object("django.conf:settings", namespace="CELERY")

celery_app.autodiscover_tasks()
