from django.apps import AppConfig


class AdvertisementsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.apps.advertisements"
    verbose_name = "Объявления"

    def ready(self):
        from . import signals

        return super().ready()
