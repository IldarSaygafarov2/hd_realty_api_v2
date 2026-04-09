from django.db import models

from core.apps.common.models import BaseModel


class District(BaseModel):
    name = models.CharField(verbose_name="Название", max_length=128, unique=True)
    slug = models.SlugField(verbose_name="Короткая ссылка", unique=True, max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"
        ordering = ["-created_at"]
