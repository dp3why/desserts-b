from flask import Blueprint, jsonify, request

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/')
def hello():
    return jsonify(message='Flask app is running now')


@user_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    # parse post data
    username = data['username']
    message = data['message']

    outdict = {}
    outdict['username'] = username
    outdict['message'] = message

    return jsonify(outdict), 201
