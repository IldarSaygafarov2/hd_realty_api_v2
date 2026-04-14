from datetime import datetime
from uuid import UUID

from ninja import Schema


class FAQRead(Schema):
    id: UUID
    question: str
    answer: str
    created_at: datetime
    updated_at: datetime
