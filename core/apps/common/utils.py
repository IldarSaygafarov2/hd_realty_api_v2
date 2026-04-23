from django.db.models import Model
from ninja import Schema
from ninja.errors import ValidationError


def serialize_items(model: type[Model], schema: Schema, many: bool = True, **kwargs):
    if many:
        objects = model.objects.all()
        return [schema.model_validate(obj) for obj in objects]

    try:
        print(kwargs)
        return model.objects.get(id=kwargs["id"])
    except model.DoesNotExist:
        raise ValidationError(errors=[{"detail": "Some error"}])
