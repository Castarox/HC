import sqlite3

class Location:

    def __init__(self, BeaconIDX, name):
        self.name = name
        self.BeaconIDX = BeaconIDX

    def save(self):
        """ Saves location in database """
        base = sqlite3.connect('cms.db')
        cursor = base.cursor()
        params = [self.name, self.BeaconIDX]
        cursor.execute("INSERT INTO Location (Name, BeaconIDX) VALUES (?, ?);", params)
        base.commit()
        base.close()