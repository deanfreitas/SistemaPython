from flask import Flask
from flask import request
from flask_api import status

from app.service.mongo_service import MongoService
from app.utils.response_utils import ResponseUtils

mongo_service = MongoService()

app = Flask(__name__)


@app.route('/keys/<id>', methods=['GET'])
def get_one(id):
    if request.method == 'GET':
        obj = mongo_service.get_one(id)
        if not obj or obj == 'null':
            return ResponseUtils.response('{}', status.HTTP_404_NOT_FOUND)
        else:
            return ResponseUtils.response(obj, status.HTTP_200_OK)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
