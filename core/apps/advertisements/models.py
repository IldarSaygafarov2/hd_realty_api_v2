from django.db import models


from core.apps.common.models import BaseModel

from .choices import OperationTypeChoices


class Advertisement(BaseModel):
    operation_type = models.CharField(
        verbose_name="Тип операции",
        choices=OperationTypeChoices.choices,
        max_length=20,
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="advertisements",
    )
    renovation_type = models.ForeignKey(
        "categories.RenovationType",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Тип ремонта",
    )

    title = models.CharField(verbose_name="Название", max_length=120)
    slug = models.SlugField(verbose_name="Слаг", max_length=200, null=True)
    price_usd = models.DecimalField(
        verbose_name="Цена в USD",
        max_digits=8,
        decimal_places=3,
    )
    price_uzs = models.DecimalField(
        verbose_name="Цена в UZS",
        max_digits=12,
        decimal_places=3,
        null=True,
        blank=True,
        help_text="Цена будет высчитываться от price_usd после сохранения объявления",
    )

    description = models.TextField(verbose_name="Описание")
    complex_name = models.CharField(
        verbose_name="Название жилого комплекса",
        max_length=150,
        blank=True,
        null=True,
    )
    special_conditions = models.TextField(
        verbose_name="Специальные условия",
        blank=True,
        null=True,
    )
    # общие характеристики
    total_area = models.FloatField(verbose_name="Общая площадь")
    living_space = models.FloatField(verbose_name="Жилая площадь")
    floor = models.IntegerField(verbose_name="Этаж", blank=True, null=True)
    number_of_floors = models.IntegerField(
        verbose_name="Этажность",
        blank=True,
        null=True,
    )
    ceiling_height = models.FloatField(verbose_name="Высота потолков", default=0)
    year_of_construction = models.IntegerField(
        verbose_name="Год постройки",
        null=True,
        blank=True,
    )
    rooms_quantity = models.IntegerField(verbose_name="Количество комнат", default=0)

    preview = models.ImageField(
        verbose_name="Заставка",
        upload_to="advertisements/previews/%Y/%m/%d/",
        null=True,
        blank=True,
    )
    is_moderated = models.BooleanField(verbose_name="Прошло модерацию?", default=False)

    # location
    address = models.CharField(verbose_name="Адрес", max_length=200)
    city = models.CharField(verbose_name="Город", max_length=100)
    district = models.ForeignKey(
        "districts.District",
        on_delete=models.CASCADE,
        verbose_name="Район",
        related_name="advertisements",
    )

    # TODO: добавить поле для карты
    # TODO: добавить поле для агента

    def __str__(self):
        return (
            f"{self.title}, {self.total_area}м², {self.floor}/{self.number_of_floors}"
        )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]


class AdvertisementImage(BaseModel):
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Объявление",
    )
    image = models.ImageField(
        verbose_name="Фотография",
        upload_to="advertisements/images/%Y/%m/%d/",
    )

    def __str__(self):
        return f"Фото объявления: {self.advertisement.title}"

    class Meta:
        verbose_name = "Фотография объявления"
        verbose_name_plural = "Фотографии объявления"
        ordering = ["-created_at"]


class AdvertisementCharacterstic(BaseModel):
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        related_name="characteristics",
    )
    key = models.CharField(verbose_name="Название характеристики", max_length=150)
    value = models.CharField(verbose_name="Значение характеристики", max_length=150)

    def __str__(self):
        return f"{self.key}: {self.value}"

    class Meta:
        verbose_name = "Характеристика объявления"
        verbose_name_plural = "Характеристики объявления"
        ordering = ["-created_at"]
