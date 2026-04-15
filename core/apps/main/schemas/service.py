from uuid import UUID

from ninja import Schema


class ServiceIncludeSchema(Schema):
    id: UUID
    title: str


class ServiceRead(Schema):
    id: UUID
    title: str
    description: str
    deadlines: str
    format: str
    service_includes: list[ServiceIncludeSchema]
