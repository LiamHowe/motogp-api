from pymongo import MongoClient
from bson import json_util
import json
from models.rider import Rider

class MongoDBClient(object):

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.motoGP

    def insert_years_and_rider(self, years):

        for year in years:
            self.db.years.delete_many({ "year" : year })
            self.db.years.insert(years[year])

    def sanitize_bson(self, bson):
        return json.loads(json_util.dumps(bson))
