import MySQLdb

class SQLClient(object):

    def __init__(self, hostname, username, password, database):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database

    def get_riders_for_year(self) :

        conn = MySQLdb.connect(
            host=self.hostname,
            user=self.username,
            passwd=self.password,
            db=self.database
        )

        cursor = conn.cursor()

        get_riders_for_years_query = \
            "SELECT yr.year AS rs_year, \n \
    	        c.name AS rs_classification, \n \
                r.id AS rs_rider_id, \n \
    	        r.name AS rs_rider_name, \n \
            	r.date_of_birth AS rs_rider_date_of_birth, \n \
            	t.name AS rs_team, \n \
            	m.name AS rs_manufacturer, \n \
            	yr.number AS rs_number \n \
            FROM year_riders yr \n \
            	JOIN teams t ON t.id = yr.team_id \n \
            	JOIN riders r ON r.id = yr.rider_id \n \
            	JOIN manufacturers m ON m.id = t.manufacturer_id \n \
            	JOIN classification c ON c.id = yr.classification_id"

        cursor.execute(get_riders_for_years_query)

        conn.close()

        return cursor.fetchall()
