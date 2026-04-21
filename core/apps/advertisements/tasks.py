import requests

from core.project import celery_app, settings
from constance import config


@celery_app.task
def get_todays_currency_rate():
    currencies = requests.get(settings.CURRENCY_RATE_API).json()
    usd_rate = 0.0
    for currency in currencies:
        if currency["Code"] == "840":
            usd_rate = float(currency["Rate"])

    config.CURRENCY_RATE = usd_rate

    print("constance currency updated")
