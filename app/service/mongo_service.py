import logging

from ..mongo.mongo_wrapper import MongoWrapper

log = logging.getLogger(__name__)

mongo_wrapper = MongoWrapper()


class MongoService(object):
    name_collection = 'keys'
    db = None

    def __db(self):
        if self.db:
            return self.db

        self.db = MongoWrapper.connect(mongo_wrapper)
        return self.db

    def get_one(self, id):
        db = self.__db()
        return db[self.name_collection].find_one({'id': id})

    def insert_one(self, key):
        db = self.__db()
        return db[self.name_collection].insert_one(key)

    def update_one(self, new_key):
        db = self.__db()
        return db[self.name_collection].update_one({'id': new_key['id']}, {'$set': new_key})

    def delete_one(self, id):
        db = self.__db()
        return db[self.name_collection].delete_one({'id': id})
