from flask import Response

from .json_utils import JsonUtils


class ResponseUtils(object):
    @staticmethod
    def response(object_return, status):
        result = JsonUtils.object_to_json(object_return)
        return Response(result, status, mimetype='application/json')
