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
    '''Get the total count of all the data items.'''
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

@blp.get('/transactions/')
def get_transaction_stats():
    '''Get the transactions stats: total income amount, total expense amount and net amount.'''
    result = {}
    income_amount = 0
    expense_amount = 0
    recent_records = TransactionModel.query.order_by(TransactionModel.created_at.desc()).limit(5).all()
    
    for record in recent_records:
        if record.type == 'expense':
            expense_amount += record.amount
        elif record.type == 'income':
            income_amount += record.amount
        
        result['income'] = income_amount
        result['expense'] = expense_amount
        result['net'] = income_amount - expense_amount
    return result

@blp.get('/transactions/count/')
def get_transaction_count():
    '''Get the count of income and expense transactions.'''
    result = {}
    income_count = 0
    expense_count = 0
    recent_records = TransactionModel.query.order_by(TransactionModel.created_at.desc()).limit(5).all()
    
    for record in recent_records:
        if record.type == 'expense':
            expense_count += 1
        elif record.type == 'income':
            income_count += 1
        
        result['income'] = income_count
        result['expense'] = expense_count
    return result