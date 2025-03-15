from marshmallow import Schema, fields

class BaseUserSchema(Schema):
    id = fields.Int(dumy_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    name = fields.Str(required=True)

class CreateUserSchema(BaseUserSchema):
    password = fields.Str(required=True)

class ReadUserSchema(BaseUserSchema):
    pass

class UpdateUserSchema(Schema):
    username = fields.Str(required=False)
    email = fields.Email(required=False)
    name = fields.Str(required=False)
    password = fields.Str(required=False)