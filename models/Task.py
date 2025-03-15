from db import db
from sqlalchemy.sql import func

class TaskModel(db.Model):
    # Defining the table name explicitly
    __tablename__ = 'tasks'
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(20), nullable=False)
    deadline = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at= db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=False, nullable=False)
    user = db.relationship("UserModel", back_populates="tasks")
    # TODO: Check FK constraint check are working or not
    
    def __repr__(self):
        return f'''<Task - 
        id: {self.id}>, 
        title: {self.title}, 
        type: {self.type}, 
        description: {self.description},
        status: {self.status},
        deadline: {self.deadline},
        created_at: {self.created_at},
        updated_at: {self.updated_at}'''
    
