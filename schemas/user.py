from marshmallow import Schema, fields

class BaseUserSchema(Schema):
    id = fields.Int(dumy_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    name = fields.Str(required=True)

class CreateUserSchema(BaseUserSchema):
    password = fields.Str(required=True)

class ReadUserSchema(CreateUserSchema):
    pass