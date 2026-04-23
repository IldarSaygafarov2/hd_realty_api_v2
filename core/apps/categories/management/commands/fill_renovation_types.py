from django.core.management.base import BaseCommand
from slugify import slugify

from core.apps.categories.models import RenovationType
from core.project.settings import RENOVATION_TYPES


class Command(BaseCommand):
    def handle(self, *args, **options):
        renovation_types = RenovationType.objects.all()
        for renovation_type in renovation_types:
            renovation_type.delete()

        for item in RENOVATION_TYPES:
            new_renovation_type = RenovationType.objects.create(
                title=item, slug=slugify(item)
            )
            print(f"added: {new_renovation_type=}")
