from sql_client import SQLClient

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

    for year, classification, rider_name, rider_date_of_birth, team, manufacturer, number in result_set :
        print year, classification, rider_name, rider_date_of_birth, team, manufacturer, number
