import re
import uuid


class IdUtils(object):
    @staticmethod
    def create_id():
        return re.sub(u'[/\W/g]', '', str(uuid.uuid4()))
