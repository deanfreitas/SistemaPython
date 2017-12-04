import logging
from ..mongo.mongo_wrapper import MongoWrapper

log = logging.getLogger(__name__)
mongoWrapper = MongoWrapper()


class MongoService(object):
    name_collection = 'keys'

    def get_one(self, id):
        log.info('My method invoked')
        db = MongoWrapper.connect(mongoWrapper)
        return db[self.name_collection].find_one({'id': id})
