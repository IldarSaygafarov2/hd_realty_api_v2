from ninja import Router
from django.http import HttpRequest
from core.apps.common.utils import serialize_items
from core.apps.advertisements.schemas import (
    AdvertisementListSchema,
    AdvertisementDetailSchema,
)
from core.apps.advertisements.models import Advertisement
from django.shortcuts import get_object_or_404

router = Router(tags=["Объявления"])


@router.get("/", response=list[AdvertisementListSchema])
def get_advertisements(request: HttpRequest):
    items = serialize_items(Advertisement, AdvertisementListSchema)
    return items


@router.get("/{advertisement_slug}", response=AdvertisementDetailSchema)
def get_advertisement_by_slug(request: HttpRequest, advertisement_slug: str):
    advertisement = get_object_or_404(Advertisement, slug=advertisement_slug)
    return advertisement
