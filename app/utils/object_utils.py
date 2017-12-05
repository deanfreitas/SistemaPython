class ObjectUtils(object):
    @staticmethod
    def delete_attribute_object(obj, attribute):
        if obj and attribute in obj:
            del obj[attribute]

        return obj
