from  marshmallow import fields, Schema

class _BaseEntertainmentSchema(Schema):
    id = fields.Int(dumy_only=True)
    title = fields.Str(required=True)
    type = fields.Str(required=True)
    status = fields.Str(required=True)
    start_date = fields.DateTime()
    finish_date = fields.DateTime()
 
class CreateBookSchema(_BaseEntertainmentSchema):
    user_id = fields.Integer(required=True)

class ReadBookSchema(_BaseEntertainmentSchema):
    user_id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class UpdateBookSchema(_BaseEntertainmentSchema):
    pass
