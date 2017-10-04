import MySQLdb
import pymysql.cursors

class SQLClient(object):

    def __init__(self, hostname, username, password, database):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database

    def get_riders_for_year(self) :

        connection = pymysql.connect(
            host=self.hostname,
            user=self.username,
            password=self.password,
            db=self.database,
            autocommit=True
        )

        try:

            get_riders_for_years_query = '''
                SELECT
                    yr.year AS year,
        	        c.name AS classification,
                    r.id AS rider_id,
        	        r.name AS rider_name,
                	r.date_of_birth AS rider_date_of_birth,
                	t.name AS team,
                	m.name AS manufacturer,
                	yr.number AS number
                FROM
                    year_riders yr
                	JOIN teams t ON t.id = yr.team_id
                	JOIN riders r ON r.id = yr.rider_id
                	JOIN manufacturers m ON m.id = t.manufacturer_id
                	JOIN classification c ON c.id = yr.classification_id
                '''

            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(get_riders_for_years_query)

        except Exception as exc:
            print exc
        finally:
            connection.close()

        return cursor.fetchall()
