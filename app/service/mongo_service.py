import logging

from ..mongo.mongo_wrapper import MongoWrapper

log = logging.getLogger(__name__)

mongo_wrapper = MongoWrapper()


class MongoService(object):
    __name_collection = 'keys'
    __db = None

    def __get_db(self):
        if self.__db:
            return self.__db

        self.__db = MongoWrapper.connect(mongo_wrapper)
        return self.__db

    def get_one(self, id):
        db = self.__get_db()
        return db[self.__name_collection].find_one({'id': id})

    def insert_one(self, key):
        db = self.__get_db()
        return db[self.__name_collection].insert_one(key)

    def update_one(self, new_key):
        db = self.__get_db()
        return db[self.__name_collection].update_one({'id': new_key['id']}, {'$set': new_key})

    def delete_one(self, id):
        db = self.__get_db()
        return db[self.__name_collection].delete_one({'id': id})
