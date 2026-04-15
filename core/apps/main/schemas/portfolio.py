from uuid import UUID

from ninja import Schema


class PortfolioJobSchema(Schema):
    id: UUID
    job: str


class PortfolioImageSchema(Schema):
    id: UUID
    image: str


class PortfolioRead(Schema):
    id: UUID
    video: str
    jobs: list[PortfolioJobSchema]
    images: list[PortfolioImageSchema]
