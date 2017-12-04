from pymongo import MongoClient


class MongoWrapper(object):
    host = 'localhost'
    port = '27017'
    db = 'vault'
    url = 'mongodb://' + host + ':' + port + '/' + db

    def connect(self):
        client = MongoClient(self.url)
        return client.get_database()