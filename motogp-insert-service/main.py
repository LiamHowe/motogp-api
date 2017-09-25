from sql_client import SQLClient
from mongodb_client import MongoDBClient

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

    result_set = sql_client.get_riders_for_year()

    mongodb_client = MongoDBClient()

    mongodb_client.insert_years_and_rider(result_set)
