from flask import Blueprint, jsonify, request
from app.services.file_service import upload_file_to_s3
from app.models.file_model import *
from flask_jwt_extended import jwt_required

file_blueprint = Blueprint('file', __name__)


@file_blueprint.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    if 'file' not in request.files:
        return jsonify(error='No file part'), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify(error='No selected file'), 400

    # Upload file to AWS S3
    file_url = upload_file_to_s3(file)

    # Save file URL to MongoDB
    username = request.form.get('username')
    save_file_url_to_mongodb(file.filename, file_url, username)

    # Return the response as JSON
    return jsonify(
        message='File uploaded successfully',
        filename=file.filename,
        username=username,
        url=file_url
    ), 200


@file_blueprint.route('/files', methods=['GET'])
@jwt_required()
def get_files():

    files = get_all_files_from_mongodb()
    if files:
        return jsonify(files)
    return []