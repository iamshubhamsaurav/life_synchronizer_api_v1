# External Imports
from flask import Flask

# Internal Imports
from db import db

# Blueprint Imports
from resources.users import blp as users_blueprint

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

with app.app_context():
    db.create_all()

# Registering the blueprints
app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    app.run(debug=True)