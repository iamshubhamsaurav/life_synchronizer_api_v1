from marshmallow import fields, Schema

class _BaseTransactionSchema(Schema):
    id = fields.Int(dumy_only=True)
    title = fields.Str(required=True)
    type = fields.Str(required=True)
    amount = fields.Float(required=True)
    description = fields.Str(required=False)
    date = fields.DateTime(required=False)

class CreateTransactionSchema(_BaseTransactionSchema):
    user_id = fields.Integer(required=True)

class ReadTransactionSchema(_BaseTransactionSchema):
    user_id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class UpdateTransactionSchema(_BaseTransactionSchema):
    pass