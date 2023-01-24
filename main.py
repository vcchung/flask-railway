from flask import Flask, jsonify
import os
from flask_cors import CORS
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
CORS(app)

def get_db():
    client=MongoClient("mongodb://mongo:jx5Y2trR0XXHiyUPTfdE@containers-us-west-170.railway.app:6336")
    return client['flask-db']
    
@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/user')
def test():
    return jsonify({"name": "testing user again"})

@app.route('/mongo-user')
def mongo_user():
    print("calling mongo-user")
    user=get_db()["user"].find_one()
    print('result is {}'.format(user))
    return dumps(user)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))


