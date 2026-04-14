from django.db import models

from core.apps.common.models import BaseModel


class FAQ(BaseModel):
    question = models.CharField(verbose_name="Вопрос", max_length=150, unique=True)
    answer = models.TextField(verbose_name="Ответ")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопрос-ответ"
        verbose_name_plural = "Вопросы-ответы"
        ordering = ["-created_at"]


class ConsultingRequest(BaseModel):
    class GoalChoices(models.TextChoices):
        BUY = "buy", "Купить"
        SELL = "sell", "Продать"

    name = models.CharField(verbose_name="Имя", max_length=50)
    phone_number = models.CharField(verbose_name="Номера телефона")
    goal = models.CharField(
        verbose_name="Цель",
        choices=GoalChoices.choices,
        max_length=20,
    )

    def __str__(self):
        return f"Заявка от {self.name}-{self.phone_number}"

    class Meta:
        verbose_name = "Заявка на консультацию"
        verbose_name_plural = "Заявки на консультацию"
        ordering = ["-created_at"]


class Service(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=60)
    description = models.TextField(verbose_name="Описание")
    deadlines = models.CharField(verbose_name="Сроки", max_length=20)
    format = models.CharField(verbose_name="Формат", max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["-created_at"]


class ServiceInclude(BaseModel):
    title = models.CharField(verbose_name="Название", max_length=60)
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="service_includes",
        verbose_name="Услуга",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пункт услуги"
        verbose_name_plural = "Пункты услуги"
        ordering = ["-created_at"]


JobsChoices = (
    ("photos_job", "Фотографии, подчеркивающие свет и пространство."),
    ("video_job", "Съемка и монтаж видео"),
    ("result_job", "AI контент"),
    ("ai_job", "Реализация от концепции до результата"),
)


class Portfolio(BaseModel):
    video = models.FileField(
        verbose_name="Видео",
        upload_to="portfolio/videos/%Y/%m/%d",
    )

    def __str__(self):
        return ", ".join([job.get_job_display() for job in self.jobs.all()])

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"
        ordering = ["-created_at"]


class PortfolioJob(BaseModel):
    job = models.CharField(
        verbose_name="Выполненная работа", choices=JobsChoices, max_length=70
    )
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name="jobs",
        verbose_name="Портфолио",
    )

    def __str__(self):
        return self.get_job_display()

    class Meta:
        verbose_name = "Выполненная работа"
        verbose_name_plural = "Выполненные работы"


class PortfolioImage(BaseModel):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        verbose_name="Проект в портфолио",
        related_name="images",
    )
    image = models.ImageField(
        verbose_name="Фото",
        upload_to="portfolio/images/%Y/%m/%d",
    )
