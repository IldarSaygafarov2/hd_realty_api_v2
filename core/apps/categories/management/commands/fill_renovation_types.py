from django.core.management.base import BaseCommand
from slugify import slugify

from core.apps.categories.models import RenovationType
from core.project.settings import RENOVATION_TYPES


class Command(BaseCommand):
    def handle(self, *args, **options):
        for item in RENOVATION_TYPES:
            try:
                existing = RenovationType.objects.get(title=item)
                if not existing.slug:
                    existing.slug = slugify(item)
                    existing.save()
            except RenovationType.DoesNotExist:
                new_renovation_type = RenovationType.objects.create(
                    title=item, slug=slugify(item)
                )
                print(f"added: {new_renovation_type=}")
