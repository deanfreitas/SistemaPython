from flask import Response


class ResponseRequest(object):
    @staticmethod
    def response(object_return, status):
        return Response(object_return, status, mimetype='application/json')
