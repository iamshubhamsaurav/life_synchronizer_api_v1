from marshmallow import Schema, fields

class _BaseNoteSchema(Schema):
    id = fields.Int(dumy_only=True)
    title = fields.Str(required=True)
    body = fields.Str(required=True)
    user_id = fields.Integer(required=True)

class CreateNoteSchema(_BaseNoteSchema):
    pass

class ReadNoteSchema(_BaseNoteSchema):
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class UpdateNoteSchema(_BaseNoteSchema):
    pass