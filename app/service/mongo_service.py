import logging

from ..mongo.mongo_wrapper import MongoWrapper
from ..utils.json_utils import JsonUtils
from ..utils.object_utils import ObjectUtils

log = logging.getLogger(__name__)

mongo_wrapper = MongoWrapper()


class MongoService(object):
    name_collection = 'keys'

    def get_one(self, id):
        db = MongoWrapper.connect(mongo_wrapper)
        result = db[self.name_collection].find_one({'id': id})
        ObjectUtils.delete_attribute_object(result, '_id')
        return JsonUtils.object_to_json(result)
