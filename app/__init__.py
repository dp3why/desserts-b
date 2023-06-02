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
import json

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(file_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)

    return app


# Initialize the Flask app
app = create_app()

secret = json.loads(os.getenv('CREDENTIAL'))
cred = credentials.Certificate(secret)
firebase_admin.initialize_app(cred, {
 'projectId': os.getenv('PROJECT_ID')
    })


app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)
cors = CORS(app)
