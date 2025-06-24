from marshmallow import fields, Schema

class _BaseTaskSchema(Schema):
    id = fields.Int(dumy_only=True)
    title = fields.Str(required=True)
    type = fields.Str(required=True)
    description = fields.Str()
    status = fields.Str(required=True)
    deadline = fields.DateTime()
    user_id = fields.Integer(required=True)

class CreateTaskSchema(_BaseTaskSchema):
    pass

class UpdateTaskSchema(_BaseTaskSchema):
    user_id = fields.Integer(required=False)

class ReadTaskSchema(_BaseTaskSchema):
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
