import uuid
from datetime import datetime

from ninja import Schema


class CategorySchema(Schema):
    id: uuid.UUID
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
