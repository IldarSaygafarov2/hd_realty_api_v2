import uuid
from datetime import datetime

from core.apps.common.schemas import ORMModel


class BaseSchema(ORMModel):
    id: uuid.UUID
    slug: str
    created_at: datetime
    updated_at: datetime


class CategorySchema(BaseSchema):
    name: str


class RenovationTypeSchema(BaseSchema):
    title: str
