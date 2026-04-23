from datetime import datetime
from uuid import UUID

from core.apps.common.schemas import ORMModel


class DistrictSchema(ORMModel):
    id: UUID
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
