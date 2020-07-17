from cloudant.client import Cloudant
import json

username = ''
password = ''
url = ''
client = None
my_database = None
    
def init_db():
    global my_database
    client = Cloudant(username, password, url=url, connect=True)
    if hasattr(client, 'users'):
        my_database = client['user']
    else:
        my_database = client.create_database('my_database')


def add_user(data):
    my_document = my_database.create_document(data)
    error_message = {
        'message': 'An error occured'
    }
    if my_document.exists():
        return str(my_document)
    else:
        return json.dumps(error_message)

def close_db():
    client.disconnect()