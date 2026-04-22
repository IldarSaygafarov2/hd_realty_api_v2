from constance import config
from constance.signals import config_updated
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.advertisements.models import Advertisement

# 57206273,834


@receiver(config_updated, sender=config)
def currency_rate_constance_updated(sender, key, old_value, new_value, **kwargs):
    advertisements = Advertisement.objects.all()
    if old_value != new_value:
        for advertisement in advertisements:
            advertisement.price_uzs = round(
                (float(advertisement.price_usd) * new_value), 3
            )
            advertisement.save()
            print(f"Price updated for current currency rate")
    else:
        print("currency rate dont changed")


@receiver(post_save, sender=Advertisement)
def set_price_uzs_from_usd(sender, instance: Advertisement, created, **options):
    if created:
        current_price_usd = instance.price_usd
        price_uzs = config.CURRENCY_RATE * current_price_usd
        instance.price_uzs = round(price_uzs, 3)
        instance.save()
