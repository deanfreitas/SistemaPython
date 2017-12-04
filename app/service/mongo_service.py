from ..mongo.mongo_wrapper import MongoWrapper

mongoWrapper = MongoWrapper()


class MongoService:
    name_collection = 'vault'

    async def get_one(self, id):
        db = await MongoWrapper.connect(mongoWrapper)
        return await db[self.name_collection].findOne({id: id})
