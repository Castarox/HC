import sqlite3

class Location:

    def __init__(self, id, location_id, name):
        self.id = id
        self.location_id = location_id
        self.name = name

    def save(self):
        """ Saves location in database """
        base = sqlite3.connect('cms.db')
        cursor = base.cursor()
        params = [self.id, self.location_id, name]
        cursor.execute("INSERT INTO Beacon (id, location_id) VALUES (?, ?, ?);", params)
        base.commit()
        base.close()