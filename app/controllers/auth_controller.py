from flask import request, jsonify, Blueprint
from flask_jwt_extended import  create_access_token, jwt_required, get_jwt_identity
from firebase_admin import auth
from flask_cors import cross_origin

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
@cross_origin(headers=['Content-Type', 'Authorization'])
def login():
    # Get the Firebase ID token from the request
    id_token = request.json.get('idToken')

    try:
        # Verify the ID token with Firebase
        decoded_token = auth.verify_id_token(id_token)
        # Get the user's UID from the decoded token
        user_id = decoded_token['uid']

        # Generate JWT token using Firebase UID as the identity
        access_token = create_access_token(identity=user_id)
        return jsonify({'access_token': access_token}), 200

    except auth.InvalidIdTokenError or auth.ExpiredIdTokenError or auth.RevokedIdTokenError:
        return jsonify({'error': 'Invalid ID token'}), 401



