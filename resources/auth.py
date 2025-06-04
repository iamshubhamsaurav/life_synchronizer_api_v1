
# External Imports 
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError


# Schema Imports
from schemas.user import ReadUserSchema
from schemas.auth import SignupSchema, LoginSchema
# Model Import
from models.User import UserModel
# db import
from db import db

blp = Blueprint("auth", "auth", url_prefix="/api/v1/auth")

@blp.post('/signup/')
@blp.arguments(SignupSchema)
@blp.response(200, ReadUserSchema)
def signup_user(user_data):
    '''Creates a new user'''
    user = UserModel(**user_data)
    try:
        db.session.add(user)
        db.session.commit()
    except SQLAlchemyError as e:
        abort(400, message = e._message)
    except Exception as e:
        abort(400, message="Some error occured in saving user")
        # Return the user if user was saved       
    return user

@blp.post('/login/')
@blp.arguments(LoginSchema)
@blp.response(200, ReadUserSchema)
def signup_user(user_data):
    '''Creates a new user'''
    email = user_data['email']
    password = user_data['password']
    user = UserModel.query.filter_by(email=email).first()
    print(user.password, password)
    if str(user.password) == str(password):
        return user
    else:
        abort(400, 'Incorrect username or password')
    
  