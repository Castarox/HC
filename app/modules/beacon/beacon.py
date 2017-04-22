import sqlite3
from sqlite3 import OperationalError

class Beacon:

    def __init__(self, beacon_id):
        self.connect = sqlite3.connect("cms.db")
        self.cur = self.connect.cursor()
        self.beacon_id = beacon_id

    def save(self):
        """ Saves beacon in database """
        print(self.beacon_id)
        try:
            self.cur.execute("INSERT INTO Beacon (BeaconIDX) VALUES (?);", [self.beacon_id])
            self.connect.commit()

        except sqlite3.OperationalError as w:
            print("Cant add/edit this {}".format(w))

        except sqlite3.Error:
            if self.connect:
                self.connect.rollback()
                print('There was a problem with SQL Data Base')
