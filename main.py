from flask import Flask, jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/user')
def test():
    return jsonify({"name": "another testing user"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
