# External Imports
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

# db Import
from db import db

# Model Import
from models import (
    BookModel,
    EntertainmentModel,
    NoteModel,
    TransactionModel,
    TaskModel,
    UserModel
)


blp = Blueprint("stats", "stats", url_prefix="/api/v1/stats")

@blp.get('/overview')
def get_overview():
    result = {}
    
    books = BookModel.query.count()
    entertainments = EntertainmentModel.query.count()
    notes = NoteModel.query.count()
    transactions = TransactionModel.query.count()
    tasks = TaskModel.query.count()

    result['books']  = books
    result['entertainments']  = entertainments
    result['notes']  = notes
    result['transactions']  = transactions
    result['tasks']  = tasks

    return result