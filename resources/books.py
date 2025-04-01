# External Imports
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

# db Import
from db import db

# Model Import
from models import BookModel

# Schema Imports
from schemas.book import ReadBookSchema, CreateBookSchema, UpdateBookSchema

blp = Blueprint("books", "books", url_prefix="/api/v1/books")

@blp.route('/')
class BookList(MethodView):
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
    
@blp.route('/<int:id>/')
class Book(MethodView):
    
    @blp.response(200, ReadBookSchema)
    def get(id):
        '''Get a book by id'''
        book = BookModel.query.get_or_404(id)
        return book
    
    @blp.arguments(UpdateBookSchema)
    @blp.response(200, ReadBookSchema)
    def put(id, book_data):
        '''Update a book'''
        book = BookModel.query.get_or_404(id)
        book.title = book_data['title']
        book.author = book_data['author']
        book.status = book_data['status']
        if 'start_date' in book_data:
            book.start_date = book_data['start_date']
        if 'finish_date' in book_data:
            book.finish_date = book_data['finish_date']

        try:
            db.session.add(book)
            db.session.commit()
            return book
        except SQLAlchemyError as e:
            abort(400, e._message)
        except Exception as e:
            abort(400, "Error occured in updating book")

    def delete(self, id):
        '''Delete Book'''
        book = BookModel.query.get_or_404(id)
        try:
            db.session.delete(book)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, e._message)
        except Exception as e:
            abort(400, "Error occured in deleting book")
        return {"message": "Book Deleted"}