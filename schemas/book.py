from  marshmallow import fields, Schema

class _BaseBookSchema(Schema):
    id = fields.Int(dumy_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    status = fields.Str(required=True)
    start_date = fields.DateTime()
    finish_date = fields.DateTime() 
    user_id = fields.Integer(required=True)

class CreateBookSchema(_BaseBookSchema):
    pass

class ReadBookSchema(_BaseBookSchema):
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)