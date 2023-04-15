from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS

from resources.dummy import DummyResource
from resources.authentication import Login, Register

from config import config

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/', methods=["GET"])
def index():
    return jsonify({"status" : "ok"})

api.add_resource(DummyResource, '/api/v1/dummy')
api.add_resource(Login, '/api/v1/login')
api.add_resource(Register, '/api/v1/register')

if __name__ == '__main__':
    app.run(host=config["HOST"], port=config["PORT"], debug=config['DEBUG'])