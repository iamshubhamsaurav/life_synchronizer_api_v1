# External Imports
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

# db Import
from db import db

# Model Imports
from models import NoteModel

# Schema Imports
from schemas.note import ReadNoteSchema, CreateNoteSchema, UpdateNoteSchema

blp = Blueprint("notes", "notes", url_prefix="/api/v1/notes")

@blp.route('/')
class NoteList(MethodView):
    
    @blp.response(200, ReadNoteSchema(many=True))
    def get(self):
        '''Get All Notes'''
        return NoteModel.query.all()
    
    @blp.arguments(CreateNoteSchema)
    @blp.response(201, CreateNoteSchema)
    def post(self, note_data):
        '''Create Note'''
        note = NoteModel(**note_data)
        try:
            db.session.add(note)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, e._message)
        except Exception as e:
            abort(400, "Error occured in saving note")
        return note

@blp.route('/<int:id>/')
class Note(MethodView):

    @blp.response(200, ReadNoteSchema)
    def get(self, id):
        '''Get Note by Id'''
        note = NoteModel.query.get_or_404(id)
        return note
    
    @blp.arguments(UpdateNoteSchema)
    @blp.response(200, ReadNoteSchema)
    def put(self, note_data, id):
        '''Update Note'''
        note = NoteModel.query.get_or_404(id)
        note.title = note_data["title"]
        note.body = note_data["body"]
        try:
            db.session.add(note)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, e._message)
        except Exception as e:
            abort(400, "Error occured in updating note")
        return note
    
    def delete(self, id):
        '''Delete Note'''
        note = NoteModel.query.get_or_404(id)
        try:
            db.session.delete(note)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, e._message)
        except Exception as e:
            abort(400, "Error occured in deleting note")
        return {"message": "Note Deleted"}
