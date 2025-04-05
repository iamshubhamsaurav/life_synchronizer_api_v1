# External Imports
from flask import Flask
from flask_smorest import Api

# Internal Imports
from db import db

# Blueprint Imports
from resources.users import blp as users_blueprint
from resources.tasks import blp as tasks_blueprint
from resources.notes import blp as notes_blueprint
from resources.books import blp as books_blueprint
from resources.transactions import blp as transaction_blueprint
from resources.entertainment import blp as entertainment_blueprint

def create_app():
    app = Flask(__name__)

    # Configuring the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    # Configuring the Swagger documentation
    app.config["API_TITLE"] = "Life Synchronizer API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()

    # Registering the blueprints
    api.register_blueprint(users_blueprint)
    api.register_blueprint(tasks_blueprint)
    api.register_blueprint(notes_blueprint)
    api.register_blueprint(books_blueprint)
    api.register_blueprint(transaction_blueprint)
    api.register_blueprint(entertainment_blueprint)

    return app

# if __name__ == '__main__':
#     app.run(debug=True)