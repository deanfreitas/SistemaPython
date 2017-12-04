from flask_api import status
from flask import Flask
from flask import request

from app.service.mongo_service import MongoService

mongoService = MongoService()
app = Flask(__name__)


@app.route('/vault/<id>', methods=['GET'])
def get_one(id):
    if request.method == 'GET':
        object = mongoService.get_one(id)
        if object is None:
            return status.HTTP_404_NOT_FOUND
        else:
            return object


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
