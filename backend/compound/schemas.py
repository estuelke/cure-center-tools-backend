from marshmallow import Schema, fields, ValidationError


def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided')


class CompoundSchema(Schema):
    pass