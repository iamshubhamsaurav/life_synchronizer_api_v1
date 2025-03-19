# External Imports
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

# db Import
from db import db

# Model Import
from models import BookModel

# Schema Imports
from schemas.book import ReadBookSchema, CreateBookSchema

blp = Blueprint("books", "books", url_prefix="/api/v1/books")

@blp.route('/')
class NoteList(MethodView):
    @blp.response(200, ReadBookSchema(many=True))
    def get():
        '''Read all books'''
        return BookModel.query.all()
    
    @blp.arguments(CreateBookSchema)
    @blp.response(201, ReadBookSchema)
    def post(book_data):
        '''Create Book'''
        book = BookModel(**book_data)
        try:
            db.session.add(book)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, e._message)
        except Exception as e:
            abort(400, "Error occured in saving book")
        return book  
