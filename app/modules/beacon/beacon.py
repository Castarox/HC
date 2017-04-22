import sqlite3

class Beacon:

    def __init__(self, id, beacon_id):
        self.id = id
        self.beacon_id = beacon_id

    def save(self):
        """ Saves beacon in database """
        base = sqlite3.connect('cms.db')
        cursor = base.cursor()
        params = [self.id, self.beacon_id]
        cursor.execute("INSERT INTO Beacon (id, beacon_id) VALUES (?, ?);", params)
        base.commit()
        base.close()