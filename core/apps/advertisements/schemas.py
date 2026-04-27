from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel

from core.apps.advertisements.choices import OperationTypeChoices
from core.apps.categories.schemas import CategorySchema, RenovationTypeSchema
from core.apps.common.schemas import ORMModel
from core.apps.districts.schemas import DistrictSchema
from core.apps.advertisements.models import Advertisement

from typing import Optional

from ninja import Field


class AdvertisementBaseSchema(ORMModel):
    id: UUID
    title: str
    slug: str
    price_usd: Decimal
    price_uzs: Decimal | None = None
    # preview: str | None
    created_at: datetime


class AdvertisementListSchema(AdvertisementBaseSchema):
    complex_name: str | None = None

    def resolve_preview(obj):
        return "123"


class AdvertisementDetailSchema(AdvertisementBaseSchema):
    description: str
    total_area: float
    living_space: float
    address: str
    city: str

    operation_type: OperationTypeChoices
    category: CategorySchema
    renovation_type: RenovationTypeSchema
    district: DistrictSchema

    images: list["AdvertisementImageSchema"]

    # with default values
    complex_name: str | None = None
    special_conditions: str | None = None
    number_of_floors: int | None = None
    ceiling_height: float = 0.0
    year_of_construction: int | None = None
    rooms_quantity: int = 0
    is_moderated: bool = False


class AdvertisementImageSchema(ORMModel):
    id: UUID
    image: str
