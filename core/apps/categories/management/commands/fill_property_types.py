from django.core.management.base import BaseCommand
from slugify import slugify

from core.apps.categories.models import PropertyType
from core.project.settings import PROPERTY_TYPES_LIST


class Command(BaseCommand):
    def handle(self, *args, **options):
        property_types = PropertyType.objects.all()
        for property_type in property_types:
            property_type.delete()

        for item in PROPERTY_TYPES_LIST:
            property_type = PropertyType.objects.create(name=item, slug=slugify(item))
            property_type.save()
            print(f"Added: {property_type=}")
