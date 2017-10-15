import unittest
from mappers.years_mapper import YearsMapper
import json
import datetime

class YearsMapperTest(unittest.TestCase):

    def setUp(self):

        self.years_mapper = YearsMapper()

    def test_map_years_for_riders_one_rider(self):

        result_set = [
            {
                u'classification': 'MotoGP',
                u'rider_id': 2,
                u'year': 2016,
                u'rider_date_of_birth': datetime.date(1993, 2, 17),
                u'number': 93,
                u'rider_name': 'Marc Marquez',
                u'team': 'Repsol Honda Team',
                u'manufacturer': 'Honda'
            }
        ]

        years = self.years_mapper.map_years_for_riders(result_set)

        self.assertIsNotNone(years)
        self.assertEquals(1, len(years.keys()))

        year = years[2016]

        self.assertEquals(2016, year["year"])

        classifications = year["classifications"]

        self.assertEquals(1, len(classifications))

        classification = classifications[0]

        self.assertEquals("MotoGP", classification["classification"])

        riders = classification["riders"]

        self.assertEquals(1, len(riders))

        rider = riders[0]

        self.assertEquals("Marc Marquez", rider["name"])
        self.assertEquals(2, rider["riderId"])
        self.assertEquals(93, rider["number"])
        self.assertEquals("Repsol Honda Team", rider["team"])
        self.assertEquals("Honda", rider["manufacturer"])
        self.assertEquals("1993-02-17", rider["dateOfBirth"])

    def test_map_years_for_riders_two_riders(self):

        result_set = [
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
                u'rider_id': 1,
                u'year': 2016,
                u'rider_date_of_birth': datetime.date(1979, 2, 16),
                u'number': 46,
                u'rider_name': 'Valentino Rossi',
                u'team': 'Movistar Yamaha MotoGP',
                u'manufacturer': 'Yamaha'
            }
        ]

        years = self.years_mapper.map_years_for_riders(result_set)

        self.assertIsNotNone(years)
        self.assertEquals(1, len(years.keys()))

        year = years[2016]

        self.assertEquals(2016, year["year"])

        classifications = year["classifications"]

        self.assertEquals(1, len(classifications))

        classification = classifications[0]

        self.assertEquals("MotoGP", classification["classification"])

        riders = classification["riders"]

        self.assertEquals(2, len(riders))

    def test_map_years_for_riders_two_classifications(self):

        result_set = [
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

        years = self.years_mapper.map_years_for_riders(result_set)

        self.assertIsNotNone(years)
        self.assertEquals(1, len(years.keys()))

        year = years[2016]

        self.assertEquals(2016, year["year"])

        classifications = year["classifications"]

        self.assertEquals(2, len(classifications))

        classification = classifications[0]

        self.assertEquals("MotoGP", classification["classification"])

        riders = classification["riders"]

        self.assertEquals(1, len(riders))

        classification = classifications[1]

        self.assertEquals("Moto2", classification["classification"])

        riders = classification["riders"]

        self.assertEquals(1, len(riders))

    def test_map_years_for_riders_two_years(self):

        result_set = [
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

        years = self.years_mapper.map_years_for_riders(result_set)

        self.assertIsNotNone(years)
        self.assertEquals(2, len(years.keys()))

        year = years[2016]

        self.assertEquals(2016, year["year"])

        classifications = year["classifications"]

        self.assertEquals(1, len(classifications))

        classification = classifications[0]

        self.assertEquals("Moto2", classification["classification"])

        riders = classification["riders"]

        self.assertEquals(1, len(riders))

        year = years[2015]

        self.assertEquals(2015, year["year"])

        classifications = year["classifications"]

        self.assertEquals(1, len(classifications))

        classification = classifications[0]

        self.assertEquals("MotoGP", classification["classification"])

        riders = classification["riders"]

        self.assertEquals(1, len(riders))

if __name__ == '__main__':
    unittest.main()
