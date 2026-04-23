from django.http import HttpRequest
from ninja import Router

from core.apps.common.utils import serialize_items
from core.apps.districts.models import District
from core.apps.districts.schemas import DistrictSchema

router = Router(tags=["Районы"])


@router.get("/", response=list[DistrictSchema])
def get_districts(request: HttpRequest):
    return serialize_items(District, DistrictSchema)
