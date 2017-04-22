import sqlite3

class Beacon:

    def __init__(self, beacon_id):
        self.beacon_id = beacon_id

    def save(self):
        """ Saves beacon in database """
        base = sqlite3.connect('cms.db')
        cursor = base.cursor()
        params = [self.beacon_id]
        cursor.execute("INSERT INTO Beacon (BeaconIDX) VALUES (?);", params)
        base.commit()
        base.close()