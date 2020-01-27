from marshmallow import Schema, fields, ValidationError


def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided')


class EmailSchema(Schema):
    id = fields.Int(dump_only=True)
    email_address = fields.Str(required=True)
    label = fields.Str()
    member = fields.Nested(
        lambda: MemberSchema(exclude=['emails']),
        required=True,
        validate=must_not_be_blank
    )


class PhoneNumberSchema(Schema):
    id = fields.Int(dump_only=True)
    member = fields.Nested(
        lambda: MemberSchema(exclude=['phone_numbers']),
        required=True,
        validate=must_not_be_blank
    )
    label = fields.Str()
    phone_number = fields.Str(required=True)


class ListSchema(Schema):
    id = fields.Int(dump_only=True)
    description = fields.Str(required=True)
    list_type = fields.Str(required=True)
    members = fields.List(
        fields.Nested(lambda: MemberSchema(exclude=['lists']))
    )
    name = fields.Str(required=True)


class CureCenterProfileSchema(Schema):
    id = fields.Int(dump_only=True)
    birthday = fields.Date()
    group = fields.Nested(lambda: GroupSchema(only=['id', 'name']))
    image_url = fields.Str()
    is_internal = fields.Boolean(missing=False)
    is_qura_funded = fields.Boolean(missing=False)
    member_id = fields.Int()
    nick_name = fields.Str()
    onyen = fields.Str()
    positions = fields.List(fields.Nested(lambda: PositionSchema()))
    staff_designation = fields.Str()
    suffix = fields.Str()


class GroupSchema(Schema):
    id = fields.Int(dump_only=True)
    contact = fields.Nested(
        lambda: MemberSchema(only=['id', 'first_name', 'last_name'])
    )
    members = fields.List(
        fields.Nested(lambda: MemberSchema(exclude=['group']))
    )
    name = fields.Str(required=True)


class PositionSchema(Schema):
    id = fields.Int(dump_only=True)
    department = fields.Str()
    title = fields.Str()


class MemberSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True, validate=must_not_be_blank)
    last_name = fields.Str(required=True, validate=must_not_be_blank)
    cure_center_profile = fields.Nested(CureCenterProfileSchema)
    emails = fields.List(fields.Nested(EmailSchema(exclude=['member'])))
    executive_assistant = fields.Nested(
        lambda: MemberSchema(exclude=['executive_assistant'])
    )
    institution = fields.Str(required=True, validate=must_not_be_blank)
    is_executive_assistant = fields.Boolean(missing=False)
    is_archived = fields.Boolean(missing=False)
    lists = fields.List(fields.Nested(ListSchema(only=['id', 'name'])))
    phone_numbers = fields.List(
        fields.Nested(PhoneNumberSchema(exclude=['member']))
    )
