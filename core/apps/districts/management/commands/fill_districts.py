from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from slugify import slugify

from core.apps.districts.models import District
from core.project.settings import DISTRICTS_LIST


class Command(BaseCommand):
    def handle(self, *args, **options):
        for idx, district in enumerate(DISTRICTS_LIST, start=1):
            slug = slugify(district)
            try:
                item = District.objects.get(name=district)
                if not item.slug:
                    item.slug = slug
                item.save()

            except District.DoesNotExist:
                new_district = District.objects.create(name=district, slug=slug)
                print(f"{idx}. Added {new_district=}")
            except IntegrityError:
                new_district = District.objects.get(name=district)
                new_district.slug = slug
                new_district.save()
                print(f"updated: {new_district=}")
