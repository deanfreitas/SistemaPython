from flask import Response


class ResponseUtils(object):
    @staticmethod
    def response(object_return, status):
        return Response(object_return, status, mimetype='application/json')
