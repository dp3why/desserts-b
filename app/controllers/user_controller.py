from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin
from firebase_admin import auth

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/')
def hello():
    return jsonify(message='Flask app is running now')

@user_blueprint.route('/users', methods=['POST'])
@jwt_required()
@cross_origin(headers=['Content-Type', 'Authorization'])
def create_user():
    data = request.get_json()

    # Get the Firebase ID token from the request
    id_token = request.json.get('idToken')

    try:

        decoded_token = auth.verify_id_token(id_token)

        user_id = decoded_token['uid']

    
        username = data['username']
        message = data['message']
        return jsonify(
            username=username,
            message=message,
            user_id=user_id
        ), 201
    except Exception as e:
        return jsonify(e), 401
