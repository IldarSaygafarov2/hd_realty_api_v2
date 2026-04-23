from datetime import datetime
from decimal import Decimal
from uuid import UUID

from core.apps.advertisements.choices import OperationTypeChoices
from core.apps.categories.schemas import CategorySchema, RenovationTypeSchema
from core.apps.common.schemas import ORMModel
from core.apps.districts.schemas import DistrictSchema


class AdvertisementBaseSchema(ORMModel):
    id: UUID
    title: str
    slug: str
    price_usd: Decimal
    prise_uzs: Decimal | None = None
    preview: str | None = None
    created_at: datetime


class AdvertisementListSchema(AdvertisementBaseSchema):
    complex_name: str | None = None


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

    # with default values
    complex_name: str | None = None
    special_conditions: str | None = None
    number_of_floors: int | None = None
    ceiling_height: float = 0.0
    year_of_construction: int | None = None
    rooms_quantity: int = 0
    is_moderated: bool = False
