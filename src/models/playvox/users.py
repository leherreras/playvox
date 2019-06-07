from models import MongoBase

class Users(MongoBase):
    collection_name = 'users'
    indexes = {
        'email': {
            'unique': True,
        }
    }
