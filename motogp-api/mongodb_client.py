from pymongo import MongoClient
from bson import json_util
import json

class MongoDBClient(object):

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.motoGP

    def get_riders(self):
        return self.sanitize_bson(self.db.riders.find())

    def get_rider(self, rider_id):
        return self.sanitize_bson(self.db.riders.find( { "riderId": rider_id } ))

    def sanitize_bson(self, bson):
        return json.loads(json_util.dumps(bson))
