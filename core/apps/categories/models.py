from django.db import models
from core.apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(verbose_name="Название", max_length=128, unique=True)
    slug = models.SlugField(verbose_name="Короткая ссылка", max_length=150, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-created_at"]
