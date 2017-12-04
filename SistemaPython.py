from flask import Flask
from flask import request
from flask_api import status

from app.service.mongo_service import MongoService
from app.utils.response_utils import ResponseRequest

mongo_service = MongoService()
response_request = ResponseRequest()

app = Flask(__name__)


@app.route('/vault/<id>', methods=['GET'])
def get_one(id):
    if request.method == 'GET':
        object = mongo_service.get_one(id)
        if not object or object == 'null':
            return response_request.response('{}', status.HTTP_404_NOT_FOUND)
        else:
            return response_request.response(object, status.HTTP_200_OK)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
