from db import db
from sqlalchemy.sql import func

class NoteModel(db.Model):
    # Defining the table name explicitly
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at= db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=False, nullable=False)
    user = db.relationship("UserModel", back_populates="notes")

    def __repr__(self):
        return f'''<Note - 
        id: {self.id}>, 
        title: {self.title}, 
        category: {self.category}, 
        body: {self.body}'''
    