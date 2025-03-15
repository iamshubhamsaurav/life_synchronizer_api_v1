# External Imports
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

# Model Imports
from models import TaskModel

# Schema Imports
from schemas.task import CreateTaskSchema, ReadTaskSchema, UpdateTaskSchema

# db import
from db import db

blp = Blueprint("tasks", "tasks", url_prefix="/api/v1/tasks")

@blp.route("/")
class TaskList(MethodView):

    @blp.response(200, ReadTaskSchema(many=True))
    def get(self):
        '''Get All Tasks'''
        return TaskModel.query.all()
    
    @blp.arguments(CreateTaskSchema)
    @blp.response(201, ReadTaskSchema)
    def post(self, task_data):
        '''Create New Tasks'''
        task = TaskModel(**task_data)
        try:
            db.session.add(task)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, message=e._message)
        except Exception as e:
            abort(400, message="Error occured in saving task")
        return task
    
@blp.route('/<int:id>')
class Task(MethodView):

    @blp.response(200, ReadTaskSchema)
    def get(self, id):
        '''Get a task by id'''
        task = TaskModel.query.get_or_404(id)
        return task
    
    @blp.arguments(UpdateTaskSchema)
    @blp.response(200, ReadTaskSchema)
    def put(self, task_data, id):
        '''Update a task by id'''
        task = TaskModel.query.get_or_404(id)
        
        # Updating the task
        task.title = task_data["title"]
        task.type = task_data["type"]
        task.status = task_data["status"]
        task.description = task_data["description"]
        task.deadline = task_data["deadline"]
        
        # Saving the data 
        db.session.add(task)
        db.session.commit()
    
        return task
    
    def delete(self, id):
        '''Delete a task'''
        task = TaskModel.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return {"message": "Task Deleted"}, 200