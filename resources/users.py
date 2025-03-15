
# External Imports 
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError


# Schema Imports
from schemas.user import CreateUserSchema, ReadUserSchema, UpdateUserSchema
# Model Import
from models.User import UserModel
# db import
from db import db

blp = Blueprint("users", "users", url_prefix="/api/v1/users")

@blp.route("/")
class UserList(MethodView):
    @blp.response(200, ReadUserSchema(many=True))
    def get(self):
        '''Returns a list of users'''
        users = UserModel.query.all()
        return users
    
    @blp.arguments(CreateUserSchema)
    @blp.response(200, ReadUserSchema)
    def post(self, user_data):
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
    
@blp.route("/<int:id>")
class User(MethodView):
    @blp.response(200, ReadUserSchema)
    def get(self, id):
        '''Return the user with the id'''
        user = UserModel.query.get_or_404(id)
        return user

    @blp.arguments(UpdateUserSchema)
    @blp.response(200, ReadUserSchema)  
    def patch(self, user_data, id):
        '''Update the user with the id'''
        user = UserModel.query.get_or_404(id)
        user.name = user_data["name"]
        user.username = user_data["username"]
        user.email = user_data["email"]
        user.password = user_data["password"]
          
        db.session.add(user)
        db.session.commit()
        return user     

    def delete(self, id):
        '''Delete the user with the id'''
        user = UserModel.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User Deleted"}, 200
