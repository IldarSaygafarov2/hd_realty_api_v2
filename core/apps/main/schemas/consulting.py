from uuid import UUID

from ninja import Schema
from core.apps.common.schemas import ORMModel

from ..models import GoalChoices


class ConsultingRequestBase(ORMModel):
    name: str
    phone_number: str
    goal: GoalChoices


class ConsultingRequestWrite(ConsultingRequestBase):
    pass


class ConsultingRequestRead(ConsultingRequestBase):
    id: UUID
