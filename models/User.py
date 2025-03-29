from db import db

class UserModel(db.Model):
    # Defining the table name explicitly
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    tasks = db.relationship("TaskModel", back_populates="user", lazy="dynamic")
    notes = db.relationship("NoteModel", back_populates="user", lazy="dynamic")
    books = db.relationship("BookModel", back_populates="user", lazy="dynamic")

    def __repr__(self):
        return f'''<User - 
        id: {self.id}>, 
        username: {self.username}, 
        email: {self.email}, 
        password: {self.password}'''
    
