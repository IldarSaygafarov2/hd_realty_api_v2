from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from slugify import slugify

from core.apps.advertisements.choices import OperationTypeChoices
from core.apps.advertisements.models import Advertisement
from core.apps.categories.models import Category, RenovationType
from core.apps.districts.models import District
