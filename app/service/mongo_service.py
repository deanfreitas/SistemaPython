import logging

from ..mongo.mongo_wrapper import MongoWrapper

log = logging.getLogger(__name__)

mongo_wrapper = MongoWrapper()


class MongoService(object):
    name_collection = 'keys'

    def get_one(self, id):
        db = MongoWrapper.connect(mongo_wrapper)
        return db[self.name_collection].find_one({'id': id})

    def insert_one(self, json):
        db = MongoWrapper.connect(mongo_wrapper)
        return db[self.name_collection].insert_one(json)
