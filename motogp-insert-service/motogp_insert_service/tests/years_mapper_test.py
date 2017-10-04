import unittest
from mappers.years_mapper import YearsMapper
import json

class YearsMapperTest(unittest.TestCase):

    def setUp(self):

        self.result_set = create_result_set()
        self.years_mapper = YearsMapper()

    def test_map_years_for_riders(self):

        years = self.years_mapper.map_years_for_riders(self.result_set)

        with open('data.json') as data_file:
            data = json.load(data_file)



    def create_result_set(self):

        return [
            {
                u'classification': 'MotoGP',
                u'rider_id': 2,
                u'year': 2016,
                u'rider_date_of_birth': datetime.date(1993, 2, 17),
                u'number': 93,
                u'rider_name': 'Marc Marquez',
                u'team': 'Repsol Honda Team',
                u'manufacturer': 'Honda'
            },
            {
                u'classification': 'MotoGP',
                u'rider_id': 2,
                u'year': 2015,
                u'rider_date_of_birth': datetime.date(1993, 2, 17),
                u'number': 93,
                u'rider_name': 'Marc Marquez',
                u'team': 'Repsol Honda Team',
                u'manufacturer': 'Honda'
            },
            {
                u'classification': 'MotoGP',
                u'rider_id': 1,
                u'year': 2016,
                u'rider_date_of_birth': datetime.date(1979, 2, 16),
                u'number': 46,
                u'rider_name': 'Valentino Rossi',
                u'team': 'Movistar Yamaha MotoGP',
                u'manufacturer': 'Yamaha'
            },
            {
                u'classification': 'Moto2',
                u'rider_id': 3,
                u'year': 2016,
                u'rider_date_of_birth': datetime.date(1996, 4, 23),
                u'number': 73,
                u'rider_name': 'Alex Marquez',
                u'team': 'EG 0,0 Marc VDS',
                u'manufacturer': 'Kalex'
            }
        ]
