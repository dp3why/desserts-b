from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from app.controllers.file_controller import file_blueprint
from app.controllers.user_controller import user_blueprint
from app.controllers.auth_controller import auth_blueprint
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(file_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)

    return app


# Initialize the Flask app
app = create_app()

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
 'projectId': os.getenv('PROJECT_ID')
    })


app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)
cors = CORS(app)

#     The create_app() function is defined to create and configure the Flask app.
#     The app instance is created using Flask(__name__).
#     The file_blueprint is imported from the file_controller.py module(assuming it's defined there). It represents the blueprint for the file-related routes.
#     The blueprint is registered with the app using app.register_blueprint(file_blueprint).
#     The app instance is returned from the create_app() function.

# By structuring your code in this way, you can easily add more blueprints or routes to the __init__.py file and keep your application well-organized.
