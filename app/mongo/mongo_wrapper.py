from pymongo import MongoClient


class MongoWrapper:
    host = 'localhost'
    port = '27017'
    db = 'vault'
    url = 'mongodb://' + host + ':' + port + '/' + db

    async def connect(self):
        client = await MongoClient(self.url)
        return client.get_database()
