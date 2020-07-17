from flask import Flask
import os, json, atexit
from db_utils import init_db, add_user, close_db

app = Flask(__name__, static_url_path='')
port = int(os.getenv('PORT', 8000))

init_db()

@app.route('/user/add/<name>')
def user_add(name):
    data = {
        'name': name
    }
    result = add_user(data)
    return result

@atexit.register
def shutdown():
   close_db()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)