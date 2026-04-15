from django.http import HttpRequest
from ninja import Router

from core.apps.main.schemas.consulting import (
    ConsultingRequestRead,
    ConsultingRequestWrite,
)
from core.apps.main.schemas.faq import FAQRead
from core.apps.main.schemas.feedback import FeedbackReadSchema, FeedbackWriteSchema
from core.apps.main.schemas.portfolio import PortfolioRead
from core.apps.main.schemas.service import ServiceRead

router = Router(tags=["Общее"])


@router.get("/faqs", response=list[FAQRead])
def get_faqs(request: HttpRequest):
    pass


@router.post("/consulting", response=ConsultingRequestRead)
def send_consulting_request(request: HttpRequest, data: ConsultingRequestWrite):
    pass


@router.get("/services", response=list[ServiceRead])
def get_services(request: HttpRequest):
    pass


@router.get("/portfolio", response=list[PortfolioRead])
def get_portfolio(request: HttpRequest):
    pass


@router.post("/feedback", response=FeedbackReadSchema)
def send_feedback(request: HttpRequest, data: FeedbackWriteSchema):
    pass
