from  marshmallow import fields, Schema

class _BaseBookSchema(Schema):
    id = fields.Int(dumy_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    status = fields.Str(required=True)
    start_date = fields.DateTime()
    finish_date = fields.DateTime() 

class CreateBookSchema(_BaseBookSchema):
    user_id = fields.Integer(required=True)

class ReadBookSchema(_BaseBookSchema):
    user_id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

# class UpdateBookSchema(_BaseBookSchema):
#     user_id = fields.Integer(required=False)
#     created_at = fields.DateTime(dump_only=True)
#     updated_at = fields.DateTime(dump_only=True)

class UpdateBookSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    status = fields.Str(required=True)
    start_date = fields.DateTime()
    finish_date = fields.DateTime()