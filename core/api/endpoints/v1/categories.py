from django.http import HttpRequest
from ninja import Router

from core.apps.categories.models import Category, RenovationType
from core.apps.categories.schemas import CategorySchema, RenovationTypeSchema
from core.apps.common.utils import serialize_items

router = Router(tags=["Категории"])


@router.get("/", response=list[CategorySchema])
def get_categories(request: HttpRequest):
    return serialize_items(Category, CategorySchema)


@router.get("/renovation-types", response=list[RenovationTypeSchema])
def get_renovation_types(request: HttpRequest):
    return serialize_items(RenovationType, RenovationTypeSchema)
