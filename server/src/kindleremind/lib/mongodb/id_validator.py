from bson.objectid import ObjectId
from bson.errors import InvalidId


def validate_mongodb_id(val_str):
    if type(val_str) is not str:
        return False

    try:
        ObjectId(val_str)
        return True
    except InvalidId:
        return False
