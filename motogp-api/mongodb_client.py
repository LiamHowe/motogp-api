from pymongo import MongoClient
from bson import json_util
import json

class MongoDBClient(object):

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.motoGP

    def get_riders(self):
        return self.sanitize_bson(self.db.riders.find())

    def get_riders(self, year, classification):
        return self.sanitize_bson( \
            self.db.years.find( \
                { \
                    "$and": [ \
                        {"year": int(year)}, \
                        {"classifications.classification": str(classification)} \
                    ] \
                }, \
                { \
                    "_id": 0, "classifications": { "$elemMatch": {"classification": str(classification)} } \
                } \
            ) \
        )

    def get_rider(self, rider_id):
        return self.sanitize_bson(self.db.riders.find( { "riderId": int(rider_id) } ))

    def sanitize_bson(self, bson):
        return json.loads(json_util.dumps(bson))
