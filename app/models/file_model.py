from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

MONGODB_CONNECTION_STRING = os.getenv("MONGO_URI")
MONGODB_DATABASE = 'ch'


def connect_mongo(collection_name):
    client = MongoClient(MONGODB_CONNECTION_STRING ,  tls=True,
                             tlsAllowInvalidCertificates=True)
    db = client[MONGODB_DATABASE]
    collection = db[collection_name]
    return client, collection


def save_file_url_to_mongodb(filename, file_url, username):
    client, collection = connect_mongo('upload')
    document = {
        'filename': filename,
        'url': file_url,
        'username': username
    }
    collection.insert_one(document)
    client.close()

def get_all_files_from_mongodb():
    client, collection = connect_mongo('upload')
    
    files = collection.find()

    file_list = []
    for file in files:
        file_info = {
            'filename': file['filename'],
            'url': file['url'],
            'username': file['username']
        }
        file_list.append(file_info)

    client.close()
    return file_list


    

