from flask import Flask
from flask import request

from .app.service.mongo_service import MongoService

mongoService = MongoService()
app = Flask(__name__)


@app.route('/vault/<id>', methods=['GET'])
async def get_one(id):
    if request.method == 'GET':
        return await mongoService.get_one(id)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
