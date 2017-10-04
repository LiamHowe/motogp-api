from mongodb_client import MongoDBClient
from sql_client import SQLClient
from mappers.years_mapper import YearsMapper

hostname = 'localhost'
username = 'root'
password = '6howelia'
database = 'motogp'

if(__name__ == "__main__"):

    sql_client = SQLClient(
        hostname,
        username,
        password,
        database
    )
    mongodb_client = MongoDBClient()

    result_set = sql_client.get_riders_for_year()

    years_mapper = YearsMapper()

    years = years_mapper.map_years_for_riders(result_set)

    mongodb_client.insert_years_and_rider(years)
