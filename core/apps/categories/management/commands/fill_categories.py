from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from slugify import slugify

from core.project.settings import CATEGORIES_LIST
from core.apps.categories.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        for category in CATEGORIES_LIST:
            category_slug = slugify(category)

            try:
                existing_category = Category.objects.get(name=category)
                if not existing_category.slug:
                    existing_category.slug = category_slug
                    existing_category.save()
            except Category.DoesNotExist:
                new_category = Category.objects.create(
                    name=category, slug=category_slug
                )
                new_category.save()
                print(f"Added: {new_category=}")
            except IntegrityError:
                category = Category.objects.get(name=category)
                category.slug = category_slug
                category.save()
        print(f"Added {len(CATEGORIES_LIST)} to categories")
