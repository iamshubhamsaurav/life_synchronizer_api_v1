# External Imports
from flask import jsonify
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
    TaskModel,
    TransactionModel
)

from schemas.book import ReadBookSchema
from schemas.entertainment import ReadEntertainmentSchema
from schemas.note import ReadNoteSchema
from schemas.task import ReadTaskSchema
from schemas.transaction import ReadTransactionSchema

blp = Blueprint("recents", "recents", url_prefix="/api/v1/recents")

@blp.route('/books/')
class BookList(MethodView):
    @blp.response(200, ReadBookSchema(many=True))
    def get(self):
        '''Get 5 recent books.'''
        recent_records = BookModel.query.order_by(BookModel.created_at.desc()).limit(5).all()
        return recent_records
    
@blp.get("/entertainments/")
@blp.response(200, ReadEntertainmentSchema(many=True))
def get_recent_entertainments():
    '''Get 5 recent expense entertainments.'''
    recent_records = EntertainmentModel.query.order_by(EntertainmentModel.created_at.desc()).limit(5).all()
    return recent_records

@blp.get("/notes/")
@blp.response(200, ReadNoteSchema(many=True))
def get_recent_notes():
    '''Get 5 recent notes.'''
    recent_records = NoteModel.query.order_by(NoteModel.created_at.desc()).limit(5).all()
    return recent_records

@blp.get("/tasks/")
@blp.response(200, ReadTaskSchema(many=True))
def get_recent_tasks():
    '''Get 5 recent tasks.'''
    recent_records = TaskModel.query.order_by(TaskModel.created_at.desc()).limit(5).all()
    return recent_records

@blp.get("/transactions/income/")
@blp.response(200, ReadTransactionSchema(many=True))
def get_recent_income_transaction():
    '''Get 5 recent income transactions.'''
    result = []
    recent_records = TransactionModel.query.order_by(TransactionModel.created_at.desc()).limit(5).all()
    for record in recent_records:
        if record.type == 'income':
            result.append(record)
    return result

@blp.get("/transactions/expense/")
@blp.response(200, ReadTransactionSchema(many=True))
def get_recent_expense_transaction():
    '''Get 5 recent expense transactions.'''
    result = []
    recent_records = TransactionModel.query.order_by(TransactionModel.created_at.desc()).limit(5).all()
    for record in recent_records:
        if record.type == 'expense':
            result.append(record)
    return result