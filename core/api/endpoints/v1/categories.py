from django.http import HttpRequest
from ninja import Router

from core.apps.categories.schemas import CategorySchema

router = Router(tags=["Категории"])


@router.get("/", response=list[CategorySchema])
def get_categories(request: HttpRequest):
    pass
