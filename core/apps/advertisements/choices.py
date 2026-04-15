from django.db import models


class OperationTypeChoices(models.TextChoices):
    RENT = "rent", "Аренда"
    BUY = "buy", "Покупка"
