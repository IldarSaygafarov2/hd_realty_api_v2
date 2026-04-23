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


class RenovationType(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=50, unique=True)
    slug = models.SlugField(verbose_name="Слаг", max_length=60, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип ремонта"
        verbose_name_plural = "Типы ремонта"
        ordering = ["-created_at"]


class PropertyType(BaseModel):
    name = models.CharField(verbose_name="Название", max_length=100, unique=True)
    slug = models.SlugField(verbose_name="Слаг", max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип недвижимости"
        verbose_name_plural = "Типы недвижимости"
        ordering = ["-created_at"]
