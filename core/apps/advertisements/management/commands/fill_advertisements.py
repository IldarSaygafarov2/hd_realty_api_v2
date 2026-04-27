import random

from django.core.management.base import BaseCommand
from faker import Faker
from slugify import slugify

from core.apps.advertisements.choices import OperationTypeChoices
from core.apps.advertisements.models import Advertisement
from core.apps.categories.models import Category, RenovationType
from core.apps.districts.models import District
from constance import config

faker = Faker()

categories = Category.objects.all()
districts = District.objects.all()
renovation_types = RenovationType.objects.all()


class Command(BaseCommand):
    def handle(self, *args, **options):
        advertisements = Advertisement.objects.all()

        for adv in advertisements:
            adv.delete()

        for i in range(1, 25):
            operation_type = (
                OperationTypeChoices.RENT if i % 2 == 0 else OperationTypeChoices.BUY
            )
            category = random.choice(list(categories))
            district = random.choice(list(districts))
            renovation_type = random.choice(list(renovation_types))
            title = faker.sentence()

            price_usd = round(random.uniform(300, 5000), 3)
            price_uzs = round(price_usd * config.CURRENCY_RATE, 3)

            new_advertisement = Advertisement.objects.create(
                title=title,
                slug=slugify(title),
                operation_type=operation_type,
                category=category,
                district=district,
                renovation_type=renovation_type,
                price_usd=price_usd,
                price_uzs=price_uzs,
                description=faker.text(),
                total_area=round(random.uniform(40, 150), 3),
                living_space=round(random.uniform(40, 150), 3),
                complex_name=(
                    f"ЖК {faker.text(max_nb_chars=5)}"
                    if category.name == "Новостройка"
                    else None
                ),
                rooms_quantity=random.randint(3, 10),
                year_of_construction=(
                    random.randint(2018, 2026)
                    if category.name == "Новостройки"
                    else None
                ),
                ceiling_height=random.randint(3, 10),
            )
            new_advertisement.save()
            print(f"Added: {new_advertisement=}")
