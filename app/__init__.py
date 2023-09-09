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
import boto3
from botocore.exceptions import ClientError
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


def get_secret():

    secret_name = "CREDENTIAL"
    region_name = "us-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    return json.loads(secret)


secret = get_secret()

cred = credentials.Certificate(secret)

firebase_admin.initialize_app(cred, {
 'projectId': os.getenv('PROJECT_ID')
    })


app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)
cors = CORS(app)
