from db import db
from sqlalchemy.sql import func

class TransactionModel(db.Model):
     # Defining the table name explicitly
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    type = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String)
    date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at= db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=False, nullable=False)
    user = db.relationship("UserModel", back_populates="transactions")
