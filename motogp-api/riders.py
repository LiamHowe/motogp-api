from mongodb_client import MongoDBClient

class Riders(object):

    def __init__(self):
        self.mongodb_client = MongoDBClient()

    def get_riders(self):
        cursor = self.mongodb_client.get_riders()
        riders = []
        for document in cursor:
            riders.append(document)
        return riders

    def get_rider(self, rider_id):
        result = self.mongodb_client.get_rider(rider_id)
        riders = []
        for document in result:
            riders.append(document)
        return riders
