# External Imports
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

# db Imports
from db import db

# Model Imports
from models.Entertainment import EntertainmentModel

# Schema Imports
from schemas.entertainment import CreateEntertainmentSchema, ReadEntertainmentSchema, UpdateEntertainmentSchema

blp = Blueprint("entertainment", "entertainment", url_prefix="/api/v1/entertainment")

@blp.route('/')
class CreateReadAllEntertainment(MethodView):

    @blp.response(200, ReadEntertainmentSchema(many=True))
    def get(self):
        '''Read All Entertainment'''
        entertainment = EntertainmentModel.query.all()
        return entertainment
    
    @blp.arguments(CreateEntertainmentSchema)
    @blp.response(201, ReadEntertainmentSchema)
    def post(self, entertainment_data):
        '''Create Entertainment'''
        entertainment = EntertainmentModel(**entertainment_data)
        try:
            db.session.add(entertainment)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, e._message)
        except Exception as e:
            abort(400, 'Error occured in saving entertainment')
        return entertainment
    
@blp.route('/<int:id>/')
class Entertainment(MethodView):
    
    @blp.response(200, ReadEntertainmentSchema)
    def get(self, id):
        '''Fetch a entertainment by Id'''
        entertainment = EntertainmentModel.query.get_or_404(id)
        return entertainment
    
    @blp.arguments(UpdateEntertainmentSchema)
    @blp.response(200, ReadEntertainmentSchema)
    def put(self, entertainment_data, id):
        'Update a entertainment by Id'
        entertainment = EntertainmentModel.query.get_or_404(id)
        entertainment.title = entertainment_data['title']
        entertainment.author = entertainment_data['type']
        entertainment.status = entertainment_data['status']
        if 'start_date' in entertainment_data:
            entertainment.start_date = entertainment_data['start_date']
        if 'finish_date' in entertainment_data:
            entertainment.finish_date = entertainment_data['finish_date']

        try:
            db.session.add(entertainment)
            db.session.commit()
            return entertainment
        except SQLAlchemyError as e:
            abort(400, e._message)
        except Exception as e:
            abort(400, "Error occured in updating entertainment")

    def delete(self, id):
        '''Delete a entertainment by Id'''
        entertainment = EntertainmentModel.query.get_or_404(id)
        try:
            db.session.delete(entertainment)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, e._message)
        except Exception as e:
            abort(400, "Error occured in deleting entertainment")
        return {"message": "Entertainment Deleted"}