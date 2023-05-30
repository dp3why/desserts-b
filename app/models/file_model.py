from pymongo import MongoClient
import os

MONGODB_CONNECTION_STRING = os.getenv("MONGO_URI")
MONGODB_DATABASE = 'ch'
MONGODB_COLLECTION = 'upload'

def save_file_url_to_mongodb(filename, file_url, username):
    client = MongoClient(MONGODB_CONNECTION_STRING)
    db = client[MONGODB_DATABASE]
    collection = db[MONGODB_COLLECTION]
    document = {
        'filename': filename,
        'url': file_url,
        'username': username
    }
    collection.insert_one(document)
    client.close()
