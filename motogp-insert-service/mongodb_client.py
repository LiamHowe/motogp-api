from pymongo import MongoClient
from bson import json_util
import json
from .models.rider import Rider

class MongoDBClient(object):

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.motoGP

    def insert_years_and_rider(self, result_set):

        years = {}

        for rs_year, rs_classification, rs_rider_id, rs_rider_name, rs_rider_date_of_birth, rs_team, rs_manufacturer, rs_number in result_set :

            if not rs_year in years:
                years[rs_year] = {
                    "year": rs_year,
                    "classifications": []
                }

            classifications = years[rs_year]["classifications"]

            classification = {}

            for classification_entry in classifications:
                if classification_entry["classification"] == rs_classification:
                    classification = classification_entry

            if not classification:
                classification["classification"] = rs_classification
                classification["riders"] = []
                classifications.append(classification)

            rider = Rider(
                int(rs_rider_id),
                rs_rider_name,
                int(rs_number),
                str(rs_rider_date_of_birth),
                rs_manufacturer,
                rs_team
            )

            '''rider = {
                "riderId": int(rs_rider_id),
                "name": rs_rider_name,
                "dateOfBirth": str(rs_rider_date_of_birth),
                "team": rs_team,
                "manufacturer": rs_manufacturer,
                "number": int(rs_number)
            }   '''

            classification["riders"].append(rider)

        print json.dumps(years, indent=1)

        for year in years:
            self.db.years.delete_many({ "year" : year })
            self.db.years.insert(years[year])

    def sanitize_bson(self, bson):
        return json.loads(json_util.dumps(bson))
