from pymongo import MongoClient


class MongoDBClient:
    client = None
    mongodb_collection = None
    mongodb_database = None

    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)

    def set_database(self, database):
        self.mongodb_database = self.client[database]

    def set_collection(self, collection):
        self.mongodb_collection = self.mongodb_database[collection]

    def insert_one_collection(self, store_object):
        self.mongodb_collection.insert_one(store_object.__dict__)

    def update_one_collection(self, filter_object, store_object):
        self.mongodb_collection.update_one(filter_object, store_object, upsert=True)

    def find_all(self):
        return self.mongodb_collection.find()

    def find_one_element(self, key, value):
        return self.mongodb_collection.find_one({key: value})

    def delete_one(self, key, value):
        return self.mongodb_collection.delete_one({key: value})

    def close(self):
        self.client.close()
