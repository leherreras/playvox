from bson.errors import InvalidId


class MongoBase:
    collection_name = ''
    indexes = {}

    def __init__(self, connection, db_name):
        self.collection = connection[db_name][self.collection_name]

        for key, value in self.indexes.items():
            self.collection.create_index(key, **value)

    def save(self, document):
        if '_id' not in document:
            self.collection.insert_one(document)
        else:
            try:
                self.collection.update({'_id': document['_id']}, document)
            except InvalidId:
                pass
