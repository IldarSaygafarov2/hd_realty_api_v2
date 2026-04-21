from constance import config
from constance.signals import config_updated
from django.dispatch import receiver


@receiver(config_updated, sender=config)
def constance_updated(sender, key, old_value, new_value, **kwargs):
    print(sender, key, old_value, new_value)
