from uuid import UUID

from ninja import Schema

from ..models import GoalChoices


class ConsultingRequestBase(Schema):
    name: str
    phone_number: str
    goal: GoalChoices


class ConsultingRequestWrite(ConsultingRequestBase):
    pass


class ConsultingRequestRead(ConsultingRequestBase):
    id: UUID
