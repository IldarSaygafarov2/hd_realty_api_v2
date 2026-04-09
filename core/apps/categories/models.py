from django.db import models
from core.apps.common.models import BaseModel
from .schemas import CategorySchema


class Category(BaseModel):
    name = models.CharField(verbose_name="Название", max_length=128, unique=True)
    slug = models.SlugField(verbose_name="Короткая ссылка", max_length=150, unique=True)

    def __str__(self) -> str:
        return self.name

    def to_entity(self) -> CategorySchema:
        return CategorySchema(
            id=self.id,
            name=self.name,
            slug=self.slug,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-created_at"]
