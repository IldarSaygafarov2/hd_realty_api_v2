from django.http import HttpRequest
from ninja import Router

router = Router(tags=["Районы"])


@router.get("/")
def get_districts(request: HttpRequest):
    pass
