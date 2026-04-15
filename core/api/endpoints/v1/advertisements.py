from ninja import Router
from django.http import HttpRequest

router = Router(tags=["Объявления"])


@router.get("/")
def get_advertisements(request: HttpRequest):
    pass


@router.get("/{advertisement_slug}")
def get_advertisement_by_slug(request: HttpRequest, advertisement_slug: str):
    pass
