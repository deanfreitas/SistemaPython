import json

from bson import json_util


class JsonUtils(object):
    @staticmethod
    def object_to_json(obj):
        return json.dumps(obj, default=json_util.default)
