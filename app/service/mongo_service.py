import json
import logging

from bson import json_util

from ..mongo.mongo_wrapper import MongoWrapper

log = logging.getLogger(__name__)
mongo_wrapper = MongoWrapper()


class MongoService(object):
    name_collection = 'keys'

    def get_one(self, id):
        db = MongoWrapper.connect(mongo_wrapper)
        result = db[self.name_collection].find_one({'id': id})
        del result['_id']
        return json.dumps(result, default=json_util.default)
