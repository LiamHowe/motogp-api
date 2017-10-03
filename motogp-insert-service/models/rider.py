

class Rider(object):

    def __init__(self, rider_id, name, number, date_of_birth, manufacturer, team):
        self.riderId = int(rider_id)
        self.name = name
        self.number = int(number)
        self.dateOfBirth = str(date_of_birth)
        self.manufacturer = manufacturer
        self.team = team
