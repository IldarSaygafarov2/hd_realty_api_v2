from django.core.management.base import BaseCommand
from slugify import slugify

from core.apps.districts.models import District
from core.project.settings import DISTRICTS_LIST


class Command(BaseCommand):
    def handle(self, *args, **options):
        items = District.objects.all()
        for item in items:
            item.delete()

        for idx, district in enumerate(DISTRICTS_LIST, start=1):
            slug = slugify(district)
            new_district = District.objects.create(name=district, slug=slug)
            print(f"{idx}. Added {new_district=}")
