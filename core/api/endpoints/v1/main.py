from django.http import HttpRequest
from ninja import Router

from core.apps.common.utils import serialize_items
from core.apps.main import models
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
    return serialize_items(models.FAQ, FAQRead)


@router.post("/consulting", response=ConsultingRequestRead)
def send_consulting_request(request: HttpRequest, data: ConsultingRequestWrite):
    new_request = models.ConsultingRequest(**data.model_dump())
    new_request.save()
    return serialize_items(
        models.ConsultingRequest, ConsultingRequestRead, many=False, id=new_request.id
    )


@router.get("/services", response=list[ServiceRead])
def get_services(request: HttpRequest):
    return serialize_items(models.Service, ServiceRead)


@router.get("/portfolio", response=list[PortfolioRead])
def get_portfolio(request: HttpRequest):
    return serialize_items(models.Portfolio, PortfolioRead)


@router.post("/feedback", response=FeedbackReadSchema)
def send_feedback(request: HttpRequest, data: FeedbackWriteSchema):
    feedback = models.FeedbackRequest(**data.model_dump())
    feedback.save()
    return serialize_items(
        models.FeedbackRequest, FeedbackReadSchema, many=False, id=feedback.id
    )
