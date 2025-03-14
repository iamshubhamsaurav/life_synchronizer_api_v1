
# External Imports 
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request


blp = Blueprint("users", "users", url_prefix="/api/v1/users")

@blp.route("/")
class UserList(MethodView):
    def get(self):
        '''Returns the list of all users'''
        return {"message": "GET method called"}

    def post(self):
        '''Creates a new user'''
        return {"message": "POST method called"}
    
@blp.route("/<int:id>")
class User(MethodView):
    def get(self, id):
        '''Return the user with the id'''
        return {"message": f"GET method called for user with id {id}"}
    
    def put(self, id):
        '''Update the user with the id'''
        return {"message": f"PUT method called for user with id {id}"}
    
    def delete(self, id):
        '''Delete the user with the id'''
        return {"message": f"DELETE method called for user with id {id}"}
