# External Imports
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

# Model Imports
from models import TransactionModel

# Schema Imports
from schemas.transaction import CreateTransactionSchema, ReadTransactionSchema, UpdateTransactionSchema

# db import
from db import db

blp = Blueprint("transactions", "transactions", url_prefix="/api/v1/transactions")

@blp.route('/')
class CreateAndReadAllTransaction(MethodView):
    
    @blp.response(200, ReadTransactionSchema(many=True))
    def get(self):
        '''Read all transactions'''
        transactions = TransactionModel.query.all()
        return transactions
    
    @blp.arguments(CreateTransactionSchema)
    @blp.response(201, ReadTransactionSchema)
    def post(self, transaction_data):
        '''Create a transaction'''
        transaction = TransactionModel(**transaction_data)
        try:
            db.session.add(transaction)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e._message)
            abort(400, e._message)
        except Exception as e:
            print('Error', e)
            abort(400, "Error occured in saving Transaction")
        return transaction

@blp.route('/<int:id>/')
class Transaction(MethodView):

    @blp.response(200, ReadTransactionSchema)
    def get(self, id):
        '''Get Transaction By Id'''
        transaction = TransactionModel.query.get_or_404(id)
        return transaction
    
    @blp.arguments(UpdateTransactionSchema)
    @blp.response(201, ReadTransactionSchema)
    def put(self, transaction_data, id):
        '''Update Transaction By Id'''
        transaction = TransactionModel.query.get_or_404(id)
        transaction.title = transaction_data['title']
        transaction.type = transaction_data['type']
        transaction.amount = transaction_data['amount']
        
        if "description" in transaction_data:
            transaction.description = transaction_data['description']
        
        if "date" in transaction_data:
            transaction.date = transaction_data['date']
        
        try:
            db.session.add(transaction)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, e._message)
        except Exception as e:
            abort(400, 'Error occured in updating Transaction')

        return transaction
    
    def delete(self, id):
        '''Delete Transaction By Id'''
        transaction = TransactionModel.query.get_or_404(id)
        try:
            db.session.delete(transaction)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, e._message)
        except Exception as e:
            abort(400, "Error occured in deleting Transaction")
        return {"message": "Transaction Deleted"}