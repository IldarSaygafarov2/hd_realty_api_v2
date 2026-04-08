import uuid
from django.db import models


class BaseModel(models.Model):
    """Base model for project."""

    id = models.UUIDField(
        verbose_name="ID",
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        abstract = True
