from flask import Flask
from flask import request
from flask_api import status
from pymongo.errors import DuplicateKeyError

from app.service.mongo_service import MongoService
from app.utils.id_utils import IdUtils
from app.utils.object_utils import ObjectUtils
from app.utils.response_utils import ResponseUtils

mongo_service = MongoService()

app = Flask(__name__)


@app.route('/keys/<id>', methods=['GET'])
def get_one(id):
    if request.method == 'GET':
        try:
            obj = mongo_service.get_one(id)
            if not obj:
                return ResponseUtils.response('{}', status.HTTP_404_NOT_FOUND)

            result = ObjectUtils.delete_attribute_object(obj, '_id')
            return ResponseUtils.response(result, status.HTTP_200_OK)
        except Exception as err:
            return ResponseUtils.response(err.args, status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.route('/keys', methods=['POST'])
def insert_one():
    if request.method == 'POST':
        obj = request.json
        if not obj or obj is {}:
            return ResponseUtils.response({}, status.HTTP_400_BAD_REQUEST)

        try:
            id_vault = IdUtils.create_id()
            obj['id'] = id_vault
            result = mongo_service.insert_one(obj)
            if result.inserted_id:
                return ResponseUtils.response({'id': id_vault}, status.HTTP_201_CREATED)

            return ResponseUtils.response({'message': 'Error create register'},
                                          status.HTTP_500_INTERNAL_SERVER_ERROR)
        except DuplicateKeyError as err:
            return ResponseUtils.response(err.details, status.HTTP_409_CONFLICT)
        except Exception as err:
            return ResponseUtils.response(err.args, status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.route('/keys', methods=['PUT'])
def update_one():
    if request.method == 'PUT':
        obj = request.json
        try:
            if not obj or obj is {} or not obj['id']:
                return ResponseUtils.response({}, status.HTTP_400_BAD_REQUEST)

            key = mongo_service.get_one(obj['id'])
            if not key:
                return ResponseUtils.response({}, status.HTTP_404_NOT_FOUND)

            result = mongo_service.update_one(obj)
            if result.raw_result['n'] == 0:
                return ResponseUtils.response({}, status.HTTP_404_NOT_FOUND)

            if result.raw_result['nModified'] == 0:
                return ResponseUtils.response({}, status.HTTP_304_NOT_MODIFIED)

            return ResponseUtils.response({}, status.HTTP_200_OK)
        except KeyError as err:
            return ResponseUtils.response('missed ' + err.args[0], status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return ResponseUtils.response(err.args, status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
