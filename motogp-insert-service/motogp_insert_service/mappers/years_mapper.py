from models.rider import Rider
import json

class YearsMapper(object):

    def __init__(self):
        pass

    def map_years_for_riders(self, result_set):

        years = {}

        for row in result_set:

            year = row["year"]

            if not year in years:
                years[year] = {
                    "year": year,
                    "classifications": []
                }

            classifications = years[year]["classifications"]

            classification = {}

            for classification_entry in classifications:
                if classification_entry["classification"] == row["classification"]:
                    classification = classification_entry

            if not classification:
                classification["classification"] = row["classification"]
                classification["riders"] = []
                classifications.append(classification)

            rider = Rider(
                row["rider_id"],
                row["rider_name"],
                row["number"],
                row["rider_date_of_birth"],
                row["manufacturer"],
                row["team"]
            )

            classification["riders"].append(rider.__dict__)

        print json.dumps(years, indent=1)

        return years
