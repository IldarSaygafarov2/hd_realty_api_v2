from django.http import HttpRequest
from ninja import Router

from core.apps.main.schemas import FAQRead


router = Router(tags=["Main"])


@router.get("/faqs", response=list[FAQRead])
def get_faqs(request: HttpRequest):
    pass
