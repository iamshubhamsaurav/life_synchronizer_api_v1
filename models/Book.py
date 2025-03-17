from db import db
from sqlalchemy.sql import func

class BookModel(db.Model):
    # Defining the table name explicitly
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    start_date = db.Column(db.DateTime)
    finish_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at= db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=False, nullable=False)
    user = db.relationship("UserModel", back_populates="books")

    