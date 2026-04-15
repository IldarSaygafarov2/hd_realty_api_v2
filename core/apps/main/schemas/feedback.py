from uuid import UUID

from ninja import Schema


class FeedbackBaseSchema(Schema):
    name: str
    phone_number: str
    message: str


class FeedbackWriteSchema(FeedbackBaseSchema):
    pass


class FeedbackReadSchema(FeedbackBaseSchema):
    id: UUID
