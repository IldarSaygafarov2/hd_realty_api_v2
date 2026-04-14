from datetime import datetime
from uuid import UUID

from .models import GoalChoices
from ninja import Schema


class FAQRead(Schema):
    id: UUID
    question: str
    answer: str
    created_at: datetime
    updated_at: datetime


class ConsultingRequestWrite(Schema):
    name: str
    phone_number: str
    goal: GoalChoices
