from django.core.management.base import BaseCommand
from slugify import slugify

from core.apps.categories.models import Category
from core.project.settings import CATEGORIES_LIST


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = Category.objects.all()
        for category in categories:
            category.delete()

        for category in CATEGORIES_LIST:
            category_slug = slugify(category)
            new_category = Category.objects.create(name=category, slug=category_slug)
            new_category.save()
            print(f"Added: {new_category=}")
