from pymongo import MongoClient


class MongoWrapper(object):
    __host = 'localhost'
    __port = '27017'
    __db = 'vault'
    __url = 'mongodb://' + __host + ':' + __port + '/' + __db

    def connect(self):
        client = MongoClient(self.__url)
        return client.get_database()
